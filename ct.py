# -*- coding: utf-8 -*-
"""Un ct= distinto por pagina en los enlaces a la App Store de nuestras apps.

Apple deja 40 caracteres como mucho en ct. Clave: aisagalab-<slug de la pagina>
(con -de, -fr... si va en un idioma); si no cabe, se corta y se pone un hash
corto para que dos paginas no compartan campana. Los enlaces a apps de otros
no se tocan, ni los del JSON-LD. Es idempotente: se puede pasar dos veces.
"""
import hashlib
import os
import re

PT = "118348020"
OURS = {"1667947372", "6754878073", "1143691286", "6754180384",
        "1553693943", "1462269642", "1662608035", "1532670722"}
MAX = 40
LANGS = {"de", "fr", "pt", "ja", "es", "ru", "zh"}

_URL = re.compile(r'https://apps\.apple\.com/[^"\'\s<>\\]*?id(\d+)[^"\'\s<>\\]*')
_LD = re.compile(r'(<script type="application/ld\+json">.*?</script>)', re.S)


def ct_for(path, site="aisagalab"):
    """path: ruta de la pagina dentro del sitio (blog/de/foo.html)."""
    parts = path.replace("\\", "/").split("/")
    slug = os.path.splitext(parts[-1])[0]
    lang = parts[-2] if len(parts) > 1 and parts[-2] in LANGS else ""
    if lang:
        slug += "-" + lang
    key = "%s-%s" % (site, slug)
    key = re.sub(r"[^A-Za-z0-9_-]", "-", key)
    if len(key) > MAX:
        h = hashlib.sha1(key.encode()).hexdigest()[:4]
        key = key[:MAX - 5].rstrip("-") + "-" + h
    return key


def _fix(url, ct, plain=False):
    m = _URL.match(url)
    if not m or m.group(1) not in OURS:
        return url
    base, _, q = url.partition("?")
    sep = "&" if plain or ("&" in q and "&amp;" not in q) else "&amp;"
    rest = [p for p in re.split(r"&amp;|&", q) if p and not p.startswith(("ct=", "pt="))]
    return base + "?" + sep.join(["pt=" + PT, "ct=" + ct] + rest)


def retag(html, path, site="aisagalab"):
    ct = ct_for(path, site)
    out = []
    for i, chunk in enumerate(_LD.split(html)):
        out.append(chunk if i % 2 else _URL.sub(lambda m: _fix(m.group(0), ct, path.endswith(".txt")), chunk))
    return "".join(out)


def retag_static(root, site="aisagalab"):
    """Paginas escritas a mano en la raiz (index, fichas de app) y llms.txt."""
    n = 0
    for f in sorted(os.listdir(root)):
        if not f.endswith((".html", ".txt")) or f.startswith("google") or f == "robots.txt":
            continue
        p = os.path.join(root, f)
        s = open(p, encoding="utf-8").read()
        t = retag(s, f, site)
        if t != s:
            open(p, "w", encoding="utf-8").write(t)
            n += 1
    return n
