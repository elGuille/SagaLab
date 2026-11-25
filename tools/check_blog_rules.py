#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Control automatico de las reglas del blog. Sale con codigo 1 si hay incumplimientos.

Reglas (todas sobre blog/**/*.html):
  1. Sin rayas: em dash o en dash (caracter o entidad).
  2. Sin valoraciones numericas de App Store (4.6, 4,6 estrellas, estrellas, columna de rating con numeros).
  3. Sin el encabezado "From the team at Saga Labs" / "Del equipo de Saga Labs" (ni sus traducciones).
  4. Dora no puede aparecer en una pagina cuyo <title> contenga gratis/free o equivalente.

Uso: python3 tools/check_blog_rules.py [--tracked-only]
  --tracked-only: solo ficheros que git ya sigue (ignora borradores sin commitear).
"""
import glob
import html
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
