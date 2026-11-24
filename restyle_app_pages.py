# -*- coding: utf-8 -*-
"""Pone las páginas de cada app (pinku.html, ai-video-generator.html...) con el
diseño de su tarjeta del home: arriba la landing (fondo de la tarjeta, capturas
grandes, frase, tiendas y funcionalidades al hacer scroll) y debajo el
contenido de la página de siempre, con el mismo estilo.

Lee los datos de build_app_landings.APPS. Uso:
    python3 restyle_app_pages.py pinku.html ai-video-generator.html
Idempotente: si la página ya está convertida, reconstruye la parte de arriba.
"""
import re
import sys
import ct
import build_app_landings as L

PAGE = {"ai-video-generator.html": "dora", "pinku.html": "pinku", "keeper.html": "photo-vault",
        "fastai.html": "ask-ai", "brainy.html": "brainy", "drop.html": "drop",
        "crypton.html": "crypton", "3things.html": "3-tasks"}
HEAD_ADD = ('<link rel="preload" href="fonts/bricolage-grotesque-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
            '<link rel="stylesheet" href="studio.css">\n<meta name="theme-color" content="#08090c">\n')


def old_content(body):
    """El contenido propio de la página, sin su hero, nav, footer ni scripts."""
    if '<div class="l-more-body">' in body:
        return body.split('<div class="l-more-body">', 1)[1].split("<!-- /l-more -->", 1)[0].rsplit("</div>", 1)[0]
    m = re.search(r"<main[^>]*>(.*)</main>", body, re.S)
    c = m.group(1)
    if '<div class="card">' in c:  # crypton.html, 3things.html: una tarjeta con logo, titulo y boton
        desc = re.search(r'<div class="card-content">.*?(<p>.*?</p>)', c, re.S)
        rel = re.search(r"<!-- related:start -->.*?<!-- related:end -->", c, re.S)
        c = (desc.group(1) if desc else "") + "\n" + (rel.group(0) if rel else "")
    c = re.sub(r'<section class="hero">.*?</section>', "", c, count=1, flags=re.S)
    c = re.sub(r"<footer>.*?</footer>", "", c, flags=re.S)
    c = re.sub(r'<section class="dora-final">.*?</section>', "", c, flags=re.S)
    c = re.sub(r'<span class="dora-kicker">.*?</span>', "", c)
    return c.strip()


def convert(path):
    slug = PAGE[path]
    a = next(x for x in L.APPS if x[0] == slug)
    src = open(path, encoding="utf-8").read()
    head, body = src.split("<body", 1)
    body = body.split(">", 1)[1]
    content = old_content(body)
    # head: fuera el estilo antiguo, dentro studio.css
    head = re.sub(r"\s*<style>.*?</style>", "", head, flags=re.S)
    head = re.sub(r'\s*<link rel="(?:stylesheet|preload)" href="style\.css"[^>]*>', "", head)
    head = re.sub(r'\s*<meta name="theme-color"[^>]*>', "", head)
    if "studio.css" not in head:
        head = head.replace("</head>", HEAD_ADD + "</head>")
    # parte de arriba: la landing generada, con rutas desde la raíz
    links = [(t, u) for t, u in a[10] if u != "../" + path]
    a = a[:10] + (links,)
    land = L.page(a).replace('src="../', 'src="').replace('href="../', 'href="')
    top = land[land.index("<a class=\"skip\""):land.index('<section class="l-end">')]
    end = land[land.index('<section class="l-end">'):land.index("</body>")]
    end = end.replace('<script src="studio.js" defer></script>', "")
    more = ('<section class="l-more" aria-label="%s in detail"><div class="wrap"><div class="l-more-body">\n%s\n</div></div></section><!-- /l-more -->\n'
            % (a[2], content))
    end = end.replace('<section class="l-end">', more + '<section class="l-end">', 1)
    body = top + end
    html = "%s<body class=\"landing\" style=\"--bg:%s\">\n%s\n<script src=\"studio.js\" defer></script>\n</body>\n</html>\n" % (head, a[6], body.strip())
    html = ct.retag(html, path)
    open(path, "w", encoding="utf-8").write(html)
    print(path)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        convert(p)
