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
        "1553693943", "1462269642", "1662608035", "1532670722", "6833951195"}
MAX = 40
LANGS = {"de", "fr", "pt", "ja", "es", "ru", "zh", "ar"}

# Sin ")" y sin puntuacion final: en texto plano (llms.txt) la URL va entre
# parentesis o acaba la frase, y el ct se colaba detras ("id123).?pt=").
_URL = re.compile(r'https://apps\.apple\.com/[^"\'\s<>\\()]*?id(\d+)(?:[^"\'\s<>\\()]*[^"\'\s<>\\().,;:])?')
_LD = re.compile(r'(<script type="application/ld\+json">.*?</script>)', re.S)


# Ask AI: Custom Product Pages aprobadas el 7 nov 2026 (#80). Cada enlace va a la página de su tema.
ASKAI_ID = "1662608035"
ASKAI_PPID = {
    "fotos": "2275a5f5-5264-4ade-98ab-7f7ca0ccdb1a",
    "modelo": "420fcaf3-b818-460e-a74f-1cb8fe2a787a",
    "traducir": "735d27ce-2811-4b20-9d3c-7bfad431030d",
}


def askai_ppid(ct):
    """Tema de la página (por su ct): imágenes -> fotos; traducir -> traducir; lo demás (chat, modelos) -> modelo."""
    c = (ct or "").lower()
    if re.search(r"translat|tradu|uebersetz|ubersetz|perevod", c):
        return ASKAI_PPID["traducir"]
    if re.search(r"image|photo|picture|imagen|imagem|bild|foto|kartink|画像", c):
        return ASKAI_PPID["fotos"]
    return ASKAI_PPID["modelo"]


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


# Un solo ct por web y app (Growth, 24 nov 2026): aisagalab-dora, aisagalab-photovault...
# Apple oculta las campanas con pocas descargas; la atribucion por pagina sale del evento store_click de Umami.
APP_SLUG = {"6754180384": "dora", "1532670722": "photovault", "6754878073": "pinku", "6833951195": "carscreen",
            "1662608035": "askai", "1667947372": "brainy", "1462269642": "drop", "1143691286": "crypton",
            "1553693943": "3tasks"}


def site_ct(app_id, site="aisagalab"):
    return "%s-%s" % (site, APP_SLUG.get(app_id, app_id))


def _fix(url, ct, plain=False, page_ct=None):
    m = _URL.match(url)
    if not m or m.group(1) not in OURS:
        return url
    base, _, q = url.partition("?")
    sep = "&" if plain or ("&" in q and "&amp;" not in q) else "&amp;"
    rest = [p for p in re.split(r"&amp;|&", q) if p and not p.startswith(("ct=", "pt=", "ppid="))]
    extra = ["ppid=" + askai_ppid(page_ct or ct)] if m.group(1) == ASKAI_ID else []
    return base + "?" + sep.join(["pt=" + PT, "ct=" + ct] + extra + rest)


# Google Play (Android): junto a cada enlace nuestro al App Store de Dora y Photo Vault, otro a Google Play con
# referrer de atribucion (Marta, 24 nov 2026). Idempotente.
PLAY = {"6754180384": "com.sagalabs.aivideo", "1532670722": "com.sagalabs.photovault"}
_A = re.compile(r'<a\b([^>]*?)href="https://apps\.apple\.com/[^"]*?id(6754180384|1532670722)[^"]*"([^>]*)>((?:(?!</a>).)*)</a>(?!\s*(?:\(|·)?\s*<a [^>]*play\.google\.com)', re.S)


def play_url(app_id, path, site="aisagalab"):
    parts = path.replace("\\", "/").split("/")
    slug = os.path.splitext(parts[-1])[0]
    if slug == "index" and len(parts) > 1:
        slug = parts[-2]
    lang = parts[-2] if len(parts) > 1 and parts[-2] in LANGS else ""
    if lang:
        slug += "-" + lang
    slug = re.sub(r"[^A-Za-z0-9_-]", "-", slug)
    return ("https://play.google.com/store/apps/details?id=%s&amp;referrer=utm_source%%3D%s%%26utm_medium%%3Darticle%%26utm_campaign%%3D%s"
            % (PLAY[app_id], site, slug))


def add_play(html, path, site="aisagalab"):
    def sub(m):
        attrs = m.group(1) + m.group(3)
        extra = ' target="_blank" rel="noopener"' if "target=" in attrs else ""
        u = play_url(m.group(2), path, site)
        if 'class="cta"' in attrs:
            return m.group(0) + ' <a class="cta"%s href="%s">Google Play</a>' % (extra, u)
        return m.group(0) + ' (<a href="%s"%s>Google Play</a>)' % (u, extra)
    return _A.sub(sub, html)


def add_banner(html, path, site="aisagalab"):
    """Smart App Banner (una meta por pagina): Dora en paginas de IA video; Photo Vault si la pagina va de fotos privadas."""
    html = re.sub(r'<meta name="apple-itunes-app"[^>]*>\n?', "", html)
    p = path.replace("\\", "/")
    if not (p.startswith("blog/") and p.endswith(".html") and not p.endswith("index.html")) or "<head" not in html:
        return html
    body = _LD.sub("", html)
    dora = len(re.findall(r"apps\.apple\.com/[^\"'\s<>]*id6754180384", body))
    pv = len(re.findall(r"apps\.apple\.com/[^\"'\s<>]*id1532670722", body))
    if pv > dora:
        app, tag = "1532670722", "pv"
    elif dora:
        app, tag = "6754180384", "dora"
    else:
        return html
    meta = '<meta name="apple-itunes-app" content="app-id=%s, affiliate-data=ct=%s-%s-banner&amp;pt=%s">' % (app, site, tag, PT)
    return re.sub(r"(<meta charset=[^>]*>)", lambda m: m.group(1) + "\n" + meta, html, count=1) if "<meta charset" in html else html.replace("<head>", "<head>\n" + meta, 1)


def retag(html, path, site="aisagalab"):
    page_ct = ct_for(path, site)
    out = []
    for i, chunk in enumerate(_LD.split(html)):
        out.append(chunk if i % 2 else _URL.sub(lambda m: _fix(m.group(0), site_ct(m.group(1), site), path.endswith(".txt"), page_ct), chunk))
    html = "".join(out)
    if not path.endswith(".txt"):
        html = "".join(c if i % 2 else add_play(c, path, site) for i, c in enumerate(_LD.split(html)))
    if not path.endswith(".txt"):
        html = add_banner(html, path, site)
    return html


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
