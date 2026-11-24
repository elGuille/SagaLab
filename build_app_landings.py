# -*- coding: utf-8 -*-
"""Landings minimalistas de cada app en /apps/<slug>.html (diseño de studio.css).

Cada landing es la ficha del home en grande: mismo fondo, capturas grandes,
la frase de la app, una línea descriptiva y las insignias de tienda. Al hacer
scroll, las funcionalidades: los titulares de las capturas de la tienda, con la
captura fija que cambia. Las páginas largas de cada app (pinku.html,
keeper.html...) se quedan como están y se enlazan en el footer, discretas,
para los buscadores y las IAs.

Uso: python3 build_app_landings.py   (regenera apps/*.html y aplica ct.retag)
"""
import os
import ct

SITE = "https://aisagalab.com"
EXT = ' target="_blank" rel="noopener noreferrer"'
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg>'
GPL = '<svg viewBox="0 0 24 26" aria-hidden="true"><path fill="#4285F4" d="M1.2.6 13.6 13 1.2 25.4C.5 25.1 0 24.4 0 23.5v-21C0 1.6.5.9 1.2.6z"/><path fill="#34A853" d="M1.2.6 13.6 13l4-4L3.6.9C2.7.4 1.8.3 1.2.6z"/><path fill="#EA4335" d="M1.2 25.4 13.6 13l4 4-14 8.1c-.9.5-1.8.6-2.4.3z"/><path fill="#FBBC04" d="m17.6 9 4.4 2.5c1.3.8 1.3 2.2 0 3L17.6 17l-4-4z"/></svg>'
LOGO = '<svg viewBox="0 0 22 22" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff4f8f"/><stop offset=".55" stop-color="#ff9f1c"/><stop offset="1" stop-color="#19c3b4"/></linearGradient></defs><rect width="22" height="22" rx="6.5" fill="url(#lg)"/><path d="M7 14.6c.9.8 2.3 1.3 3.9 1.3 2 0 3.3-.9 3.3-2.3 0-3.2-6.8-1.6-6.8-4.7 0-1.3 1.2-2.3 3.1-2.3 1.3 0 2.5.4 3.3 1.1" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg>'


def AS(i):
    return "https://apps.apple.com/app/apple-store/id%s?pt=118348020&amp;mt=8" % i


def GP(pkg):
    return "https://play.google.com/store/apps/details?id=com.sagalabs.%s" % pkg


# slug, carpeta de imágenes, nombre, plataforma, frase, descripción, fondo,
# tiendas, capturas del hero, titulares de las capturas 1-4 (de la tienda),
# enlaces del footer (página larga, guías...)
APPS = [
    ("dora", "dora", "Dora", "AI video · Web, iPhone and Android",
     "Turn text or photos into videos.",
     "Upload a photo or write a prompt and get a finished video back. On the web, on iPhone and on Android.",
     "linear-gradient(150deg,#b30e54 0%,#7d0a3d 60%,#4a0624 100%)",
     [("Web", "https://doravideo.com/?utm_source=sagalab&amp;utm_medium=landing&amp;utm_campaign=dora"), ("App Store", AS("6754180384")), ("Google Play", GP("aivideo"))],
     [2, 1, 3],
     ["A month of videos in one morning.", "Your photo, any video's moves.", "Cartoon stories from one idea.", "Old family photos, moving again."],
     [("Dora in detail", "../ai-video-generator.html"), ("doravideo.com", "https://doravideo.com/")]),
    ("pinku", "pinku", "Pinku", "Private local AI · iPhone",
     "Offline AI chat that stays private.",
     "AI models that run on your iPhone. No account, no servers, and it works in airplane mode.",
     "linear-gradient(150deg,#8f1550 0%,#4c0d2e 60%,#1f0714 100%)",
     [("App Store", AS("6754878073"))],
     [1, 3, 2],
     ["Works in airplane mode.", "Download a model. That's it.", "Your privacy. For real.", "Only models your device can run."],
     [("Pinku in detail", "../pinku.html"), ("Which model fits my iPhone", "../pinku/which-ai-model-fits-my-iphone-mac.html")]),
    ("photo-vault", "keeper", "Photo Vault", "Private photos · iPhone and Android",
     "Lock away private photos and videos.",
     "Private albums, each with its own lock, on iPhone and Android.",
     "linear-gradient(150deg,#1d3b8a 0%,#142a63 60%,#0a1533 100%)",
     [("App Store", AS("1532670722")), ("Google Play", GP("photovault"))],
     [1, 2, 4],
     ["For your eyes only.", "Every album, its own lock.", "Opens with one glance.", "Flip it. It's gone."],
     [("Photo Vault in detail", "../keeper.html"), ("Security", "../photo-vault-security.html")]),
    ("ask-ai", "all-ai", "Ask AI", "All AI models in one · iPhone",
     "The top AI models in one chat.",
     "Ask questions, analyse photos and write, choosing the model for each chat.",
     "linear-gradient(150deg,#1c2f8f 0%,#141b55 60%,#0a0c24 100%)",
     [("App Store", AS("1662608035"))],
     [1, 2, 4],
     ["All models, one chat.", "Ask AI anything.", "Analyse photos.", "Write anything."],
     [("Ask AI in detail", "../fastai.html")]),
    ("brainy", "easy-ai", "Brainy", "AI chat and images · iPhone",
     "Answers, homework help and AI images.",
     "Ask anything and get the answer step by step, with help for homework.",
     "linear-gradient(150deg,#0b63b8 0%,#0a4785 60%,#062a52 100%)",
     [("App Store", AS("1667947372"))],
     [1, 2, 3],
     ["Ask AI anything.", "Answers, step by step.", "Homework made easy.", "Create with AI."],
     [("Brainy in detail", "../brainy.html")]),
    ("carscreen", "carscreen", "CarScreen", "Car widgets and video · iPhone",
     "Widgets and parked video on your car screen.",
     "Your videos and your own M3U playlists on the car screen, while parked.",
     "linear-gradient(150deg,#13733f 0%,#0c4a29 60%,#062214 100%)",
     [("App Store", AS("6833951195"))],
     [1, 3, 4],
     ["Your videos on your car screen.", "Check your car first.", "Your own M3U playlists.", "Browse and play on the big screen."],
     []),
    ("drop", "drop", "Drop", "Sleep sounds and focus · iPhone",
     "Sounds for sleep and focus.",
     "Sounds, a focus timer, slow breathing and a sleep timer, in hand-painted night scenes.",
     "linear-gradient(150deg,#28407a 0%,#1a2a52 55%,#7a3550 100%)",
     [("App Store", AS("1462269642"))],
     [1, 3, 2],
     ["Sounds for sleep.", "Stay focused.", "Breathe slowly.", "Sleep timer."],
     [("Drop in detail", "../drop.html")]),
    ("crypton", "crypton", "Crypton", "Crypto tracker · iPhone",
     "Live prices, alerts and your portfolio.",
     "Every coin with its live price, charts from one day to one year, and home screen widgets.",
     "linear-gradient(150deg,#0b6b5a 0%,#123f6b 60%,#2b1d6b 100%)",
     [("App Store", AS("1143691286"))],
     [2, 3, 1],
     ["Home screen widgets.", "Every coin, live prices.", "Beautifully simple.", "Charts from 1D to 1Y."],
     [("Crypton in detail", "../crypton.html")]),
    ("3-tasks", "3tasks", "3 Tasks", "Daily to-do list · iPhone",
     "Three tasks a day. Get what matters done.",
     "Pick three tasks each day and work through them with a timer.",
     "linear-gradient(150deg,#2a50c4 0%,#1c3485 60%,#0f1c4a 100%)",
     [("App Store", AS("1553693943"))],
     [1, 2, 4],
     ["Just 3 tasks. Every day.", "A timer for every task.", "Fewer tasks. More done.", "Finish and celebrate."],
     [("3 Tasks in detail", "../3things.html")]),
    ("bible-videos", "android-biblevideo", "Bible Videos", "Stories and verses · Android",
     "Bible stories told as short films.",
     "Stories told in episodes, with the scripture on screen.",
     "linear-gradient(150deg,#6b4a1f 0%,#3a2812 55%,#140d06 100%)",
     [("Google Play", GP("biblevideo"))],
     [1, 2, 4],
     ["Bible stories as films.", "Stories told in episodes.", "Scripture, on screen.", "Hold to say Amen."],
     []),
]


def badge(label, url, name):
    if label == "App Store":
        return '<a class="badge" href="%s"%s aria-label="Download %s on the App Store">%s<span><small>Download on the</small>App Store</span></a>' % (url, EXT, name, APPLE)
    if label == "Google Play":
        return '<a class="badge" href="%s"%s aria-label="Get %s on Google Play">%s<span><small>GET IT ON</small>Google Play</span></a>' % (url, EXT, name, GPL)
    return '<a class="btn btn-light btn-sm" href="%s"%s>Open on the %s</a>' % (url, EXT, label.lower())


def page(a):
    slug, img, name, plat, line, desc, bg, stores, hero, feats, links = a
    shots = "".join('<img src="../images/apps/%s/shot%d.webp" alt="%s screenshot" width="1290" height="2796"%s>' % (img, k, name, ' fetchpriority="high"' if i == 1 else ' loading="lazy"' if i else "") for i, k in enumerate(hero))
    badges = "".join(badge(l, u, name) for l, u in stores)
    phone = "".join('<img src="../images/apps/%s/shot%d.webp" alt="" width="1290" height="2796" loading="lazy"%s>' % (img, k + 1, ' class="on"' if k == 0 else "") for k in range(4))
    items = "".join('<li%s><img class="m-only" src="../images/apps/%s/shot%d.webp" alt="" width="1290" height="2796" loading="lazy"><h2>%s</h2></li>' % (' class="on"' if k == 0 else "", img, k + 1, t) for k, t in enumerate(feats))
    foot = "".join('<a href="%s"%s>%s</a>' % (u, EXT if u.startswith("http") else "", t) for t, u in links)
    title = "%s: %s | Saga Lab" % (name, line.rstrip("."))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/apps/{slug}.html">
<meta property="og:title" content="{name}: {line}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/apps/{slug}.html">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/images/apps/{img}/shot{hero[1]}.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#08090c">
<link rel="icon" href="../images/apps/{img}/icon.webp" type="image/webp">
<link rel="preload" href="../fonts/bricolage-grotesque-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../studio.css">
<script src="/umami.js" defer></script>
</head>
<body class="landing" style="--bg:{bg}">
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a href="../index.html" class="brand" aria-label="Saga Lab home">{LOGO}Saga Lab</a>
    <a class="l-back" href="../index.html#apps">All apps</a>
  </div>
</header>
<main id="main">
  <section class="l-hero">
    <div class="wrap">
      <div class="l-copy">
        <div class="app-id"><img src="../images/apps/{img}/icon.webp" alt="" width="64" height="64"><div><p class="l-name">{name}</p><span class="platform">{plat}</span></div></div>
        <h1>{line}</h1>
        <p class="l-desc">{desc}</p>
        <div class="links">{badges}</div>
      </div>
      <div class="l-shots" aria-hidden="true">{shots}</div>
    </div>
  </section>
  <section class="l-feat" aria-label="What {name} does">
    <div class="wrap feat-grid">
      <div class="feat-phone" aria-hidden="true">{phone}</div>
      <ol class="feat-list">{items}</ol>
    </div>
  </section>
  <section class="l-end">
    <div class="wrap">
      <h2>{name}</h2>
      <div class="links">{badges}</div>
    </div>
  </section>
</main>
<footer class="l-foot">
  <div class="wrap">
    <span>&copy; 2026 Saga Lab</span>
    <nav aria-label="More about {name}">{foot}<a href="../index.html">Saga Lab</a><a href="../privacy.html">Privacy</a><a href="../support.html">Support</a></nav>
  </div>
</footer>
<script src="../studio.js" defer></script>
</body>
</html>
'''


def main():
    os.makedirs("apps", exist_ok=True)
    for a in APPS:
        path = "apps/%s.html" % a[0]
        html = ct.retag(page(a), path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(path)


if __name__ == "__main__":
    main()
