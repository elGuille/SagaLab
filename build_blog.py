# -*- coding: utf-8 -*-
"""Genera las paginas del blog a partir de posts.py.

Existe para que las 10 paginas compartan navbar, footer, JSON-LD y hreflang.
El sitio es HTML estatico escrito a mano y cada landing repite el chrome; con
diez articulos eso se descuadra solo. La navbar y el footer se leen de
faq.html en cada build, asi que si cambian alli, cambian aqui.
"""
import os
import re

import ct

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://aisagalab.com"


def _block(html, tag, cls=None):
    if cls:
        pat = re.compile(r'(<%s class="%s">.*?</%s>)' % (tag, cls, tag), re.S)
    else:
        pat = re.compile(r'(<%s>.*?</%s>)' % (tag, tag), re.S)
    m = pat.search(html)
    if not m:
        raise SystemExit("no encuentro <%s> en faq.html" % tag)
    return m.group(1)


_faq = open(os.path.join(ROOT, "faq.html"), encoding="utf-8").read()
NAV = _block(_faq, "nav", "navbar")
FOOTER = _block(_faq, "footer")


def chrome(depth):
    """Reescribe las rutas del chrome segun la profundidad de la pagina."""
    up = "../" * depth
    nav = NAV.replace('href="index.html#', 'href="%sindex.html#' % up)
    nav = nav.replace('href="index.html"', 'href="%sindex.html"' % up)
    nav = nav.replace('href="agentic-ai.html"', 'href="%sagentic-ai.html"' % up)
    nav = nav.replace('href="faq.html" class="nav-link active"',
                      'href="%sfaq.html" class="nav-link"' % up)
    nav = nav.replace('href="faq.html"', 'href="%sfaq.html"' % up)
    return nav, FOOTER


PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{canonical}">
{alternates}
    <link rel="stylesheet" href="{up}style.css">
    <link rel="stylesheet" href="{up}blog.css">
    <link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
    <script src="/umami.js" defer></script>

    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:image" content="{site}/images/preview.jpg">
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{og_title}">
    <meta property="twitter:description" content="{desc}">

    <script type="application/ld+json">
{jsonld}
    </script>
</head>
<body>
{nav}

    <main class="article-wrap">
{body}
    </main>

{footer}

    <script src="{up}script.js"></script>
</body>
</html>
"""


def render(*, path, lang, title, desc, og_title, body, jsonld,
           alternates="", og_type="article"):
    depth = path.count("/")
    up = "../" * depth
    nav, footer = chrome(depth)
    html = PAGE.format(
        lang=lang, title=title, desc=desc, og_title=og_title,
        canonical="%s/%s" % (SITE, path[:-len("index.html")] if path.endswith("index.html") else path), alternates=alternates,
        up=up, site=SITE, og_type=og_type, jsonld=jsonld,
        nav=nav, body=body, footer=footer,
    )
    html = ct.retag(html, path)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)
    return path, len(html)


def hreflang(en_path, es_path):
    return (
        '    <link rel="alternate" hreflang="en" href="%s/%s">\n'
        '    <link rel="alternate" hreflang="es" href="%s/%s">\n'
        '    <link rel="alternate" hreflang="x-default" href="%s/%s">'
        % (SITE, en_path, SITE, es_path, SITE, en_path)
    )


if __name__ == "__main__":
    import posts
    for path, size in posts.build(render, hreflang):
        print("%-42s %6d bytes" % (path, size))
    import posts_oct19
    for path, size in posts_oct19.build(render, hreflang):
        print("%-42s %6d bytes" % (path, size))
    import privacy_oct20
    for path, size in privacy_oct20.build(render, hreflang):
        print("%-42s %6d bytes" % (path, size))
    import guides
    for path, size in guides.build(render):
        print("%-42s %6d bytes" % (path, size))
    import pinku_models
    for path, size in pinku_models.build(render):
        print("%-42s %6d bytes" % (path, size))
    import build_i18n
    for path, size in build_i18n.build(render):
        print("%-42s %6d bytes" % (path, size))
    # paginas escritas a mano (index, fichas de app, llms.txt) y las que build_i18n reescribe in situ
    print("ct= en %d ficheros estaticos" % ct.retag_static(ROOT))
    n = 0
    for dp, _, fs in os.walk(os.path.join(ROOT, "blog")):
        for f in fs:
            if f.endswith(".html"):
                p = os.path.join(dp, f)
                s = open(p, encoding="utf-8").read()
                t = ct.retag(s, os.path.relpath(p, ROOT))
                if t != s:
                    open(p, "w", encoding="utf-8").write(t)
                    n += 1
    print("ct= en %d paginas del blog" % n)
    # enlaces internos: «Related guides» en cada guia y «Guides» en cada ficha de app
    import related
    print("related: %d ficheros" % related.inject())
