# -*- coding: utf-8 -*-
"""Traducciones de las comparativas a mas idiomas (de, fr, pt-BR, ja...).

Existe para no copiar cada articulo de posts.py una vez por idioma. Cada
traduccion es un JSON en i18n/<dir>/<pagina-en>.json con el <main> de la
pagina inglesa traducido; este script lo pinta con la misma plantilla, rehace
el JSON-LD a partir del de la pagina inglesa y pone los hreflang y el selector
de idioma en todas las versiones (tambien en la inglesa y la espanola, que
build_blog.py acaba de regenerar). Lo llama build_blog.py al final.

Formato del JSON:
  {"path": "blog/de/<slug>.html", "h1": "...", "desc": "...", "section": "...",
   "main": "<inner HTML del <main>, con los href tal cual en la inglesa>",
   "faq": [["pregunta", "respuesta"], ...]}   # mismo orden que la inglesa, o []
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://aisagalab.com"

# carpeta -> (codigo hreflang / html lang, nombre en su idioma)
LANGS = {
    "de": ("de", "Deutsch"),
    "fr": ("fr", "Fran&ccedil;ais"),
    "pt": ("pt-BR", "Portugu&ecirc;s"),
    "ja": ("ja", "&#26085;&#26412;&#35486;"),
}
NAMES = {"en": "English", "es": "Espa&ntilde;ol", "ru": "&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;"}
for _d, (_c, _n) in LANGS.items():
    NAMES[_c] = _n

_ALT = re.compile(r'    <link rel="alternate" hreflang="([^"]+)" href="([^"]+)">\n?')
_SWITCH = re.compile(r'<span class="lang-switch">.*?</span>', re.S)


def _read(path):
    return open(os.path.join(ROOT, path), encoding="utf-8").read()


def _write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)


def _rel(src, dst):
    """Enlace relativo de la pagina src a la pagina dst (las dos bajo blog/)."""
    return os.path.relpath(dst, os.path.dirname(src)).replace(os.sep, "/")


def _deeper(html, siblings=None):
    """Los href relativos de una pagina de blog/ valen un nivel mas abajo.

    `siblings` lleva cada articulo ingles (nombre de fichero) a su traduccion en
    el mismo idioma, para que una comparativa traducida enlace a las otras
    traducidas y no a la inglesa."""
    siblings = siblings or {}
    def fix(m):
        url = m.group(2)
        if re.match(r"(https?:|mailto:|#|/)", url):
            return m.group(0)
        base, _, frag = url.partition("#")
        if base in siblings:
            return '%s="%s%s"' % (m.group(1), siblings[base], "#" + frag if frag else "")
        return '%s="../%s"' % (m.group(1), url)
    return re.sub(r'(href|src)="([^"]*)"', fix, html)


def _switch(here, versions):
    """Selector de idioma de la pagina `here`: enlaces a todas las demas versiones."""
    links = ['<a href="%s" hreflang="%s">%s</a>' % (_rel(here, p), code, NAMES.get(code, code))
             for code, p in versions if p != here]
    return '<span class="lang-switch"> &middot; %s</span>' % " &middot; ".join(links)


def _alternates(versions):
    lines = ['    <link rel="alternate" hreflang="%s" href="%s/%s">' % (c, SITE, p) for c, p in versions]
    en = [p for c, p in versions if c == "en"][0]
    lines.append('    <link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, en))
    return "\n".join(lines) + "\n"


def _jsonld(en_html, t, path, code):
    data = json.loads(re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
                                en_html, re.S).group(1))
    graph = data.get("@graph", [data])
    for node in graph:
        if node.get("@type") == "BlogPosting":
            node["headline"] = t["h1"]
            node["description"] = t["desc"]
            node["inLanguage"] = code
            node["articleSection"] = t.get("section", node.get("articleSection"))
            node["mainEntityOfPage"]["@id"] = "%s/%s" % (SITE, path)
        elif node.get("@type") == "ItemList" and "name" in node:
            node["name"] = t["h1"]
        elif node.get("@type") == "FAQPage":
            qs = node["mainEntity"]
            if len(t.get("faq") or []) != len(qs):
                raise SystemExit("%s: la inglesa tiene %d preguntas y la traduccion %d"
                                 % (path, len(qs), len(t.get("faq") or [])))
            for q, (tq, ta) in zip(qs, t["faq"]):
                q["name"] = tq
                q["acceptedAnswer"]["text"] = ta
    return json.dumps(data, ensure_ascii=False, indent=2)


def build(render):
    out = []
    by_en = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "i18n", "*", "*.json"))):
        d = os.path.basename(os.path.dirname(f))
        if d not in LANGS:
            raise SystemExit("idioma desconocido: %s" % f)
        t = json.load(open(f, encoding="utf-8"))
        en_path = "blog/" + os.path.basename(f)[:-5] + ".html"
        if not t["path"].startswith("blog/%s/" % d):
            raise SystemExit("%s: path debe ir en blog/%s/" % (f, d))
        by_en.setdefault(en_path, []).append((LANGS[d][0], t))

    # por idioma: articulo ingles -> nombre del fichero traducido (misma carpeta)
    same_lang = {}
    for en_path, trans in by_en.items():
        for code, t in trans:
            same_lang.setdefault(code, {})[os.path.basename(en_path)] = os.path.basename(t["path"])

    for en_path, trans in by_en.items():
        en_html = _read(en_path)
        # versiones que ya tiene la inglesa (en, es, ru...) + las nuevas
        versions = [(c, u[len(SITE) + 1:]) for c, u in _ALT.findall(en_html) if c != "x-default"]
        versions = [v for v in versions if v[0] not in {c for c, _ in trans}]
        versions += [(c, t["path"]) for c, t in trans]

        # paginas traducidas
        for code, t in trans:
            main = _deeper(t["main"], same_lang.get(code))
            main = _SWITCH.sub(lambda m: _switch(t["path"], versions), main, count=1)
            out.append(render(
                path=t["path"], lang=code, title=t["h1"] + " | Saga Labs", desc=t["desc"],
                og_title=t["h1"], body=main, jsonld=_jsonld(en_html, t, t["path"], code),
                alternates=_alternates(versions).rstrip("\n"),
            ))

        # hreflang y selector en las versiones que no salen de este script
        mine = {t["path"] for _, t in trans}
        for code, p in versions:
            if p in mine:
                continue
            html = _read(p)
            first = _ALT.search(html)
            html = _ALT.sub("", html)
            html = html[:first.start()] + _alternates(versions) + html[first.start():]
            html = _SWITCH.sub(lambda m: _switch(p, versions), html, count=1)
            _write(p, html)
    return out


if __name__ == "__main__":
    import build_blog
    for path, size in build(build_blog.render):
        print("%-60s %6d bytes" % (path, size))
