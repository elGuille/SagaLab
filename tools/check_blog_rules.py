#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Control automatico de las reglas del blog. Sale con codigo 1 si hay incumplimientos.

Reglas (todas sobre blog/**/*.html):
  1. Sin rayas: em dash o en dash (caracter o entidad).
  2. Sin valoraciones numericas de App Store (4.6, 4,6 estrellas, estrellas, columna de rating con numeros).
  3. Sin el encabezado "From the team at Saga Labs" / "Del equipo de Saga Labs" (ni sus traducciones).
  4. Dora no puede aparecer en una pagina cuyo <title> contenga gratis/free o equivalente.
  5. Dora (cualquier frase, fila de tabla o parrafo bajo un encabezado que la nombre, y JSON-LD):
     sin "gratis/free/free to download", sin monedas/creditos, sin tiempos de generacion.
  6. Nuestras apps (apps.json) no pueden ir en la posicion 1 de una lista ordenada
     (fila "1" de tabla, encabezado "1. ...", primer <li> de un <ol>).

Uso: python3 tools/check_blog_rules.py [--tracked-only]
  Codigo de salida: 0 sin incumplimientos, 1 con incumplimientos (apto para CI).
  --tracked-only: solo ficheros que git ya sigue (ignora borradores sin commitear).
"""
import glob
import html
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DASH = re.compile(r"—|–|&mdash;|&ndash;|&#0*821[12];|&#x0*201[34];", re.I)

HEADING = re.compile(
    r"From the team at Saga Labs|Del equipo de Saga Labs|Aus dem Team von Saga Labs|"
    r"De l['’&#39;]*[ée]quipe (?:de )?Saga Labs|Da equipe da Saga Labs|Do time da Saga Labs|"
    r"От команды Saga Labs|Saga Labsチームより|Saga Labs团队|Saga Labs 团队", re.I)

FREE_TITLE = re.compile(r"free|gratis|gratuit|kostenlos|無料|무료|бесплат", re.I)

# Cabecera de columna de valoracion (no "age rating").
RATING_TH = re.compile(r"rating|评分|التقييم|تقييم|valoraci|bewertung|avalia|^nota?\b|評価|оценк|рейтинг|stars|estrellas", re.I)
AGE_TH = re.compile(r"age|edad|alter|idade|âge|年齢|возраст", re.I)
NUM = re.compile(r"^\s*[0-5][.,]\d{1,2}\s*(?:\([^)]*\))?\s*$")

STAR = r"(?:stars?|estrellas?|étoiles?|sterne?n?|estrelas?|звезд\w*|星|/\s*5|out of 5|de 5|sur 5|von 5)"
RATING_TEXT = [
    re.compile(r"★|⭐|☆"),
    re.compile(r"\b[0-5][.,]\d\s*" + STAR, re.I),
    re.compile(r"\brated\s+[0-5][.,]\d\b", re.I),
    re.compile(r"\b[0-5][.,]\d\s+(?:from|de|von|sur|из|на основе)\s+[\d.,\s]+\s*(?:ratings?|valoraciones|bewertungen|avaliações|notes|avis|оценок|評価)", re.I),
    re.compile(r"ratingValue|aggregateRating", re.I),
    # "(free, 3.9 from 9,770)"
    re.compile(r"\b[0-5][.,]\d\s+(?:from|de|von|sur|из)\s+\d[\d.,]*\b", re.I),
    # "su valoracion es 4,1", "Its US rating is 4.1", "Bewertung 4,7", "評価は4.7"
    re.compile(r"(?:ratings?|التقييم|تقييم|valoraci(?:ón|ones|&oacute;n)|calificaci(?:ón|&oacute;n)|bewertung(?:en)?|avalia(?:ção|ções|ç&atilde;o)|notes?|évaluation|оценк\w*|рейтинг\w*|評価|评分|星)[^<>\d]{0,25}\b[0-5][.,]\d\b", re.I),
    re.compile(r"\b[0-5][.,]\d\b[^<>\d]{0,12}(?:ratings?|valoraci|bewertung|avalia|évaluation|оценк|рейтинг|評価|评分)", re.I),
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self._cell = None
        self._row = None
        self._table = None  # filas de la tabla actual
        self.tables = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        elif tag == "table":
            self._table = []
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = [tag, ""]

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("td", "th") and self._cell is not None and self._row is not None:
            self._row.append(tuple(self._cell))
            self._cell = None
        elif tag == "tr" and self._row is not None and self._table is not None:
            self._table.append(self._row)
            self._row = None
        elif tag == "table" and self._table is not None:
            self.tables.append(self._table)
            self._table = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._cell is not None:
            self._cell[1] += data

# ---- Reglas 5 y 6: Dora y posicion 1 -------------------------------------------------
DORA = re.compile(r"\bDora\b")
DORA_FREE = re.compile(
    r"\bfree\b|\bgratis\b|gratuit\w*|kostenlos\w*|\bgrátis\b|\bgratuit[oa]s?\b|無料|무료|бесплатн\w*|免费|免費|"
    r"descarga\s+gratuita|free\s+to\s+download|\bsin\s+coste\b|\bohne\s+kosten\b|\bsans\s+frais\b", re.I)
DORA_COINS = re.compile(
    r"\bcoins?\b|\bmonedas?\b|\bcredits?\b|\bcr[ée]ditos?\b|\bcr[ée]dits?\b|\bkredite?s?\b|\bm[üu]nzen\b|\bpi[èe]ces\b|"
    r"\bmoedas?\b|\bcr[ée]ditos\b|\bmonete\b|\bcrediti\b|コイン|クレジット|コインを|\bтокен\w*|\bкредит\w*|\bмонет\w*|金币|积分|點數|코인|크레딧", re.I)
_TIME_UNITS = (r"(?:minutes?|mins?|seconds?|secs?|minutos?|segundos?|minuten|sekunden|minutes?|secondes?|"
               r"minuti|secondi|分|秒|分間|минут\w*|секунд\w*|分钟|秒钟|분|초)")
_TIME_NUM = (r"(?:\d+(?:[.,]\d+)?(?:\s*[-–to]+\s*\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|a\s+few|couple|"
             r"un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|unos|unas|ein|eine|zwei|drei|vier|fünf|"
             r"deux|trois|quatre|cinq|um|uma|duas|dois|três|due|tre|quattro|cinque)")
DORA_TIME = re.compile(
    r"\b" + _TIME_NUM + r"\s*(?:or\s+\w+\s+)?" + _TIME_UNITS + r"(?![a-zà-ÿ])|\b\d+\s*(?:m|s)\b(?=\s*(?:to|per|or|-))|"
    r"\d\s*(?:分間|分钟|秒钟|分|秒)|"
    r"generation\s+times?|(?:times?|tiempos?|temps|zeiten?|tempos?)\s+(?:de\s+)?(?:generaci\w+|g[ée]n[ée]ration|gera[çc]\w+|erzeugung)|"
    r"tiempos?\s+de\s+Dora|generierungszeit\w*|生成時間|生成时间|中央値|medianas?\s+medid|measured\s+medians?", re.I)
# "up to 30 seconds" / "hasta 30 segundos" describen duracion del clip, no tiempo de generacion.
CLIP_LEN = re.compile(r"\b\d+-(?:second|minute)\b|\b(?:de|von|von)\s+\d+\s*(?:segundos|sekunden)\b|\b\d+\s*(?:segundos|segundos)\s+(?:y|und)\b|\b(?:30|60|10|15|5)\s+(?:segundos|sekunden|secondes|segundos)\s+(?:y|et|und|e)\b|\b(?:up\s+to|hasta|bis\s+zu|jusqu.{1,3}[àa]|até|fino\s+a|最大|最長)\s+\d+\s*" + _TIME_UNITS +
                      r"|\b\d+\s*" + _TIME_UNITS + r"\s+(?:clips?|videos?|vídeos?|long|de\s+duraci|lang)|"
                      r"\b(?:clips?|videos?|vídeos?)\s+(?:of|de|von|du)\s+(?:up\s+to\s+|hasta\s+)?\d+", re.I)
GEN_WORDS = re.compile(
    r"generat|generaci|generar|genera\b|render|come[sn]?\s+back|vuelve|tarda|takes?\b|ready|listo|have\s+the|tienes|"
    r"erzeug|dauert|g[ée]n[ée]r|prend|dispon|pronto|demora|leva|gera[çc]|genera|出来|完成|生成|median|mediana|medi[ae]n|"
    r"measured|medid|gemessen|mesur", re.I)
BLOCK_TAG = re.compile(r"</?(?:p|li|tr|td|th|h[1-6]|div|section|article|ul|ol|table|thead|tbody|br|blockquote|dd|dt|details|summary|figure|figcaption|header|footer|nav|main)\b[^>]*>", re.I)
SCRIPT_STYLE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.I | re.S)
JSONLD = re.compile(r"<script[^>]+application/ld\+json[^>]*>(.*?)</script>", re.I | re.S)
TAGS = re.compile(r"<[^>]+>")
SENT = re.compile(r"(?<=[.!?。！？])\s+|\n+")


def load_apps():
    names, ids = set(), set()
    try:
        data = json.load(open(os.path.join(ROOT, "apps.json"), encoding="utf-8"))
    except Exception:
        return names, ids
    for a in data.get("apps", []):
        ids.add(str(a.get("appStoreId", "")))
        # Nombres distintivos del id (se descartan los que son palabras comunes: drop).
        if a.get("id") not in ("drop", "photovault", "fastai"):
            names.add(a["id"].capitalize() if a["id"] != "3tasks" else "3 Tasks")
    names |= {"Dora", "Pinku", "Brainy", "Crypton", "CarScreen", "3 Tasks"}
    return names, {i for i in ids if i}


OUR_NAMES, OUR_IDS = load_apps()
OUR_RX = re.compile(r"\b(?:" + "|".join(re.escape(n) for n in sorted(OUR_NAMES, key=len, reverse=True)) + r")\b")


def text_blocks(fragment):
    """Texto visible por bloques (linea por elemento de bloque)."""
    t = SCRIPT_STYLE.sub(" ", fragment).replace("\n", " ")
    t = BLOCK_TAG.sub("\n", t)
    t = TAGS.sub("", t)
    t = html.unescape(t)
    return [re.sub(r"[ \t\u00a0]+", " ", ln).strip() for ln in t.split("\n") if ln.strip()]


NEG = re.compile(
    r"\b(?:no|not|none|nor|without|never|n't|sin|ni|ning[uú]n\w*|kein\w*|ohne|nicht|aucun\w*|pas|sans|non|sem|nenhum\w*|n[ãa]o|senza|niente)\b"
    r"|なし|ない|なく|ません|無し|不|没有|沒有|없", re.I)


def free_hit(text):
    """'free' solo cuenta si no esta negado (p. ej. 'no free generations' describe un limite, no una promocion)."""
    for m in DORA_FREE.finditer(text):
        before = text[max(0, m.start() - 45):m.start()]
        after = text[m.end():m.end() + 12]
        if NEG.search(before) or (NEG.search(after) and re.search(r"[無无免]", m.group(0))):
            continue
        return m
    return None


def dora_violations(text, para=False):
    """Devuelve (regla, fragmento) para un trozo de texto que habla de Dora."""
    out = []
    m = None if para else free_hit(text)
    if m:
        out.append(("Dora: 'gratis/free'", m.group(0)))
    m = None if para else DORA_COINS.search(text)
    if m:
        out.append(("Dora: monedas/creditos", m.group(0)))
    clean = CLIP_LEN.sub(" ", text)
    m = DORA_TIME.search(clean)
    if m and (GEN_WORDS.search(clean) or re.search(r"times?|tiempos?|temps|zeit|時間|时间", m.group(0), re.I)):
        out.append(("Dora: tiempo de generacion", m.group(0)))
    return out


def jsonld_strings(s):
    out = []
    def walk(o, key=""):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, k)
        elif isinstance(o, list):
            for v in o:
                walk(v, key)
        elif isinstance(o, str) and key not in ("url", "@id", "@type", "image", "sameAs", "mainEntityOfPage"):
            out.append(o)
    for m in JSONLD.finditer(s):
        try:
            walk(json.loads(m.group(1)))
        except ValueError:
            out.append(m.group(1))
    return out


def check_dora(s):
    errs, seen = [], set()

    def add(frag_for_line, kind, what):
        k = (kind, what, frag_for_line[:60])
        if k in seen:
            return
        seen.add(k)
        pos = s.find(frag_for_line[:25]) if frag_for_line else -1
        errs.append((line_of(s, pos) if pos >= 0 else 0, kind, what + "  <- " + frag_for_line[:400]))

    # a) frases del texto visible que nombran a Dora (incluye title y meta description)
    head_meta = " \n ".join(re.findall(r'<meta[^>]+content="([^"]*)"', s, re.I) + re.findall(r"<title>(.*?)</title>", s, re.I | re.S))
    units = [html.unescape(x) for x in head_meta.split(" \n ")]
    body = re.sub(r"(?is)<head\b.*?</head>", " ", s)
    lines = text_blocks(body)
    for ln in lines:
        units.extend(x for x in SENT.split(ln) if x)
    units.extend(jsonld_strings(s))
    for u in units:
        # JSON-LD / meta: dividir tambien en frases
        for sent in SENT.split(u):
            if DORA.search(sent):
                for kind, what in dora_violations(sent):
                    add(sent, kind, what)
    for ln in lines:
        if DORA.search(ln):
            for kind, what in dora_violations(ln, para=True):
                add(ln, kind, what)
    # b) filas de tabla que nombran a Dora (la columna de precio no lleva el nombre)
    for tr in re.findall(r"(?is)<tr\b.*?</tr>", body):
        txt = " | ".join(text_blocks(tr))
        if DORA.search(txt):
            for kind, what in dora_violations(txt):
                add(txt, kind, what)
    # c) apartado de Dora: parrafos bajo un h2/h3/h4 que nombra a Dora, hasta el siguiente encabezado
    parts = re.split(r"(?is)(?=<h[1-4]\b)", body)
    for part in parts:
        mh = re.match(r"(?is)<h[1-4]\b[^>]*>(.*?)</h[1-4]>", part)
        if mh and DORA.search(html.unescape(TAGS.sub("", mh.group(1)))):
            for ln in text_blocks(part):
                for kind, what in dora_violations(ln):
                    add(ln, kind, what)
    return errs


def is_ours(fragment):
    if re.search(r"apps\.apple\.com/[^\"']*id(" + "|".join(map(re.escape, OUR_IDS)) + r")\b", fragment):
        return True
    return bool(OUR_RX.search(html.unescape(TAGS.sub(" ", fragment))))


def check_first_place(s):
    errs = []
    body = re.sub(r"(?is)<head\b.*?</head>|<script\b.*?</script>", " ", s)
    for tr in re.finditer(r"(?is)<tr\b[^>]*>\s*<t[dh][^>]*>\s*#?\s*1\.?\s*</t[dh]>(.*?)</tr>", body):
        if is_ours(tr.group(1)):
            errs.append((line_of(s, s.find(tr.group(0)[:40])), "nuestra app en posicion 1 (tabla)", html.unescape(TAGS.sub(" ", tr.group(1)))[:70].strip()))
    for h in re.finditer(r"(?is)<h[2-4]\b[^>]*>\s*(?:#\s*)?1\s*[.)]\s*(.*?)</h[2-4]>", body):
        if is_ours(h.group(1)):
            errs.append((line_of(s, s.find(h.group(0)[:40])), "nuestra app en posicion 1 (encabezado)", html.unescape(TAGS.sub("", h.group(1)))[:70]))
    for ol in re.finditer(r"(?is)<ol\b[^>]*>\s*<li\b[^>]*>(.*?)</li>", body):
        if is_ours(ol.group(1)):
            errs.append((line_of(s, s.find(ol.group(0)[:40])), "nuestra app en posicion 1 (lista ordenada)", html.unescape(TAGS.sub("", ol.group(1)))[:70]))
    for m in re.finditer(r'"position"\s*:\s*1\s*,\s*"item"\s*:\s*\{(.*?)\}\s*\}', s, re.S):
        if is_ours(m.group(1)) or re.search(r'"name"\s*:\s*"[^"]*\bDORA\b', m.group(1)):
            errs.append((line_of(s, m.start()), "nuestra app en posicion 1 (JSON-LD)", m.group(1)[:70].strip()))
    return errs


def files(tracked_only):
    paths = sorted(glob.glob(os.path.join(ROOT, "blog", "**", "*.html"), recursive=True))
    if tracked_only:
        out = subprocess.run(["git", "ls-files", "blog"], cwd=ROOT, capture_output=True, text=True).stdout.split()
        tracked = {os.path.join(ROOT, p) for p in out}
        paths = [p for p in paths if p in tracked]
    return paths


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check(path):
    rel = os.path.relpath(path, ROOT)
    s = open(path, encoding="utf-8").read()
    errs = []
    for m in DASH.finditer(s):
        errs.append((line_of(s, m.start()), "raya", m.group(0)))
    for m in HEADING.finditer(s):
        errs.append((line_of(s, m.start()), "encabezado prohibido", m.group(0)))
    for rx in RATING_TEXT:
        for m in rx.finditer(s):
            errs.append((line_of(s, m.start()), "valoracion numerica", m.group(0)))
    p = Page()
    p.feed(s)
    for rows in p.tables:
        heads = []
        for r in rows:
            if r and all(c[0] == "th" for c in r):
                heads = [html.unescape(c[1]).strip() for c in r]
                break
        for ci, h in enumerate(heads):
            if RATING_TH.search(h) and not AGE_TH.search(h):
                for r in rows:
                    if len(r) == len(heads) and r[ci][0] == "td" and NUM.match(html.unescape(r[ci][1])):
                        errs.append((0, "columna de valoracion", "%s = %s" % (h, r[ci][1].strip())))
                        break
    title = html.unescape(p.title).strip()
    if FREE_TITLE.search(title) and re.search(r"\bDora\b", s):
        errs.append((line_of(s, s.find("<title")), "Dora en pagina con 'gratis' en el title", title))
    errs += check_dora(s)
    errs += check_first_place(s)
    return rel, errs


def main():
    tracked_only = "--tracked-only" in sys.argv
    bad = 0
    total = 0
    for path in files(tracked_only):
        total += 1
        rel, errs = check(path)
        if errs:
            bad += 1
            for ln, kind, what in errs:
                print("%s:%s: %s: %s" % (rel, ln or "-", kind, what))
    print("check_blog_rules: %d ficheros revisados, %d con incumplimientos" % (total, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
