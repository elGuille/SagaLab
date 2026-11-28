# -*- coding: utf-8 -*-
"""Pagina de Speakboard (dictado en iPhone y Mac): /speakboard/ (EN) y /speakboard/es/.

No sale de build_app_landings.py porque esa plantilla es para apps con capturas
de tienda; esta lleva descarga directa del Mac, precios y FAQ. Mismo diseno
(studio.css, body.landing). El DMG y appcast.xml (Sparkle) viven en
speakboard/downloads/ y los sube quien compila la app.

Uso: python3 build_speakboard.py
"""
import html as H

SITE = "https://aisagalab.com"
BG = "linear-gradient(150deg,#7113fb 0%,#4a0bb0 60%,#1d0540 100%)"
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg>'
LOGO = '<svg viewBox="0 0 22 22" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff4f8f"/><stop offset=".55" stop-color="#ff9f1c"/><stop offset="1" stop-color="#19c3b4"/></linearGradient></defs><rect width="22" height="22" rx="6.5" fill="url(#lg)"/><path d="M7 14.6c.9.8 2.3 1.3 3.9 1.3 2 0 3.3-.9 3.3-2.3 0-3.2-6.8-1.6-6.8-4.7 0-1.3 1.2-2.3 3.1-2.3 1.3 0 2.5.4 3.3 1.1" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg>'
DMG = "/speakboard/downloads/Speakboard-1.0.0-7.dmg"  # subir con cada release (build) y borrar el anterior

CSS = """
.sb-wave{display:flex;align-items:center;gap:4px;height:64px;margin-bottom:20px}
.sb-wave i{flex:1;background:#fff;border-radius:3px;height:var(--h);opacity:.9;animation:sbp 1.4s ease-in-out infinite;animation-delay:var(--d)}
@keyframes sbp{50%{transform:scaleY(.35)}}
.sb-demo{background:rgba(0,0,0,.28);border:1px solid rgba(255,255,255,.2);border-radius:22px;padding:26px;min-width:0}
.sb-demo p{margin:0;font-size:20px;line-height:1.4}
.sb-demo .raw{opacity:.7;font-size:16px;margin-bottom:10px}
.landing .btn.mac{background:#fff;color:#111;min-height:44px;border-radius:9px;padding:0 18px;font-size:16px}
.l-hero h1{max-width:none}
.sb-grid+.sb-note{margin-top:24px}
.sb-note{margin:14px 0 0;font-size:14px;opacity:.8}
.sb-sec{padding:72px 0;border-top:1px solid rgba(255,255,255,.16)}
.sb-sec h2{margin:0 0 28px;font-size:clamp(30px,4vw,52px);line-height:1.05;letter-spacing:-.035em;font-weight:800;max-width:20ch}
.sb-grid{display:grid;gap:24px;grid-template-columns:repeat(3,minmax(0,1fr))}
.sb-grid.two{grid-template-columns:repeat(2,minmax(0,1fr))}
.sb-grid h3{margin:0 0 6px;font-size:20px}
.sb-grid p,.sb-sec p{margin:0;opacity:.88;line-height:1.55;max-width:60ch}
.sb-plan{background:rgba(0,0,0,.28);border:1px solid rgba(255,255,255,.2);border-radius:18px;padding:24px;min-width:0}
.sb-plan.best{border:2px solid #fff}
.sb-plan h3{margin:0}
.sb-price{font-size:40px;font-weight:800;letter-spacing:-.03em;margin:6px 0 10px}
.sb-price small{font-size:16px;font-weight:500;opacity:.8}
.sb-plan ul{margin:0;padding-left:20px;opacity:.88;line-height:1.6}
.sb-sec details{border-bottom:1px solid rgba(255,255,255,.16);padding:16px 0}
.sb-sec summary{cursor:pointer;font-weight:650;font-size:18px}
.sb-sec details p{margin-top:8px}
.sb-sec a:not(.btn){color:#fff}
.sb-lang{position:static}
@media(max-width:800px){.sb-grid,.sb-grid.two{grid-template-columns:minmax(0,1fr)}.l-hero{min-height:0}.l-hero .wrap{grid-template-columns:minmax(0,1fr)}.sb-sec{padding:48px 0}}
@media(prefers-reduced-motion:reduce){.sb-wave i{animation:none}}
"""
HEIGHTS = [30, 55, 80, 45, 95, 60, 35, 70, 100, 50, 75, 40, 85, 55, 30, 65, 90, 45, 70, 35]

T = {
 "en": dict(lang="en", path="/speakboard/", other="/speakboard/es/", back="All apps", skip="Skip to content",
  title="Speakboard: voice dictation for iPhone and Mac, on your device | Saga Lab",
  desc="Dictation for iPhone and Mac. Speech recognition runs on your device, your voice is never uploaded, and Pro costs less than the alternatives.",
  plat="Dictation · iPhone and Mac", h1="Speak. It types.",
  lead="Voice dictation for iPhone and Mac that runs on your device. Your voice is never uploaded.",
  mac="Download for Mac", macn="macOS 14+ · Apple silicon", ios_small="Download on the", ios_aria="Download Speakboard on the App Store",
  raw="you say: can you send me the report by friday", clean="You get: Can you send me the report by Friday?",
  how="How it works", steps=[("Press the key or the microphone", "On iPhone, switch to the Speakboard keyboard and tap the microphone. On Mac, hold the dictation key (Fn by default) and release it when you finish."), ("Speak normally", "Speech is recognized on your device."), ("Text appears where you type", "Messages, mail, notes or a browser: it is inserted where your cursor is. The Mac app also drops hesitation sounds such as um and uh.")],
  priv="Your voice stays on your device", privp=("Speech recognition runs locally on your iPhone and your Mac. Audio is never sent to a server.", "Nothing is processed in the cloud."), privl="Privacy policy", privu="/privacy.html",
  price="Pricing", free="Free", freeli=["3,000 words a week on Mac, 1,500 on iPhone", "iPhone sessions of up to 5 minutes", "Last 20 dictations in history"], mo="/ month", yr="/ year",
  pro="Pro Monthly", proa="Pro Annual", proli=["Unlimited words", "iPhone sessions of 20 minutes or until you stop", "Full history", "One account on iPhone and Mac"], annli=["Unlimited words", "iPhone sessions of 20 minutes or until you stop", "Full history", "One account on iPhone and Mac", "3-day free trial"],
  getfree="Start free", sub="Subscribe", tryb="Try free for 3 days",
  pn="One Pro account works on iPhone and Mac. On iPhone you subscribe in the app. On Mac you subscribe from the app after signing in.",
  faq="Questions",
  faqs=[("Which languages are supported?", "More than 25, including most European languages plus others such as Japanese, Chinese and Korean. The full list is in the language settings of the app."), ("Is one subscription enough for iPhone and Mac?", "Yes. Pro is tied to one account and works on both devices."), ("Can I cancel anytime?", "Yes. Cancel whenever you want and Pro stays active until the end of the paid period."), ("Is my voice uploaded?", "No. Audio is processed on your device and is not sent anywhere.")],
  foot=("Saga Lab", "Privacy", "Terms", "Support"), termsu="/terms.html", supu="/support.html", home="/index.html", hreflang_other="es"),
 "es": dict(lang="es", path="/speakboard/es/", other="/speakboard/", back="Todas las apps", skip="Saltar al contenido",
  title="Speakboard: dictado por voz para iPhone y Mac, en tu dispositivo | Saga Lab",
  desc="Dictado para iPhone y Mac. El reconocimiento de voz se ejecuta en tu dispositivo, tu voz nunca se sube y Pro cuesta menos que las alternativas.",
  plat="Dictado · iPhone y Mac", h1="Habla. Se escribe.",
  lead="Dictado por voz para iPhone y Mac que funciona en tu dispositivo. Tu voz nunca se sube a ningún servidor.",
  mac="Descargar para Mac", macn="macOS 14+ · Apple silicon", ios_small="Descargar en la", ios_aria="Descargar Speakboard en la App Store",
  raw="dices: puedes enviarme el informe antes del viernes", clean="Obtienes: ¿Puedes enviarme el informe antes del viernes?",
  how="Cómo funciona", steps=[("Pulsa la tecla o el micrófono", "En iPhone, cambia al teclado Speakboard y toca el micrófono. En Mac, mantén pulsada la tecla de dictado (Fn por defecto) y suéltala al terminar."), ("Habla con normalidad", "La voz se reconoce en tu dispositivo."), ("El texto aparece donde escribes", "Mensajes, correo, notas o el navegador: se inserta donde está el cursor. La app de Mac también quita muletillas como eh y um.")],
  priv="Tu voz no sale de tu dispositivo", privp=("El reconocimiento de voz se ejecuta en local, en tu iPhone y en tu Mac. El audio no se envía a ningún servidor.", "No se procesa nada en la nube."), privl="Política de privacidad", privu="/privacy.html",
  price="Precios", free="Gratis", freeli=["3.000 palabras a la semana en Mac, 1.500 en iPhone", "Sesiones de hasta 5 minutos en iPhone", "Últimos 20 dictados en el historial"], mo="/ mes", yr="/ año",
  pro="Pro mensual", proa="Pro anual", proli=["Palabras ilimitadas", "Sesiones de 20 minutos o hasta que las pares en iPhone", "Historial completo", "Una cuenta en iPhone y Mac"], annli=["Palabras ilimitadas", "Sesiones de 20 minutos o hasta que las pares en iPhone", "Historial completo", "Una cuenta en iPhone y Mac", "3 días de prueba gratis"],
  getfree="Empezar gratis", sub="Suscribirme", tryb="Probar 3 días gratis",
  pn="Una cuenta Pro funciona en iPhone y Mac. En iPhone te suscribes en la app. En Mac te suscribes desde la app tras iniciar sesión.",
  faq="Preguntas frecuentes",
  faqs=[("¿Qué idiomas admite?", "Más de 25, entre ellos la mayoría de los idiomas europeos y otros como japonés, chino y coreano. La lista completa está en los ajustes de idioma de la app."), ("¿Una suscripción sirve para iPhone y Mac?", "Sí. Pro va ligado a una cuenta y funciona en ambos dispositivos."), ("¿Puedo cancelar cuando quiera?", "Sí. Cancela en cualquier momento y Pro sigue activo hasta el final del periodo pagado."), ("¿Se sube mi voz?", "No. El audio se procesa en tu dispositivo y no se envía a ningún sitio.")],
  foot=("Saga Lab", "Privacidad", "Términos", "Soporte"), termsu="/terms.html", supu="/support.html", home="/index.html", hreflang_other="en"),
}


def page(t):
    up = "../../" if t["lang"] == "es" else "../"
    e = H.escape
    bars = "".join('<i style="--h:%d%%;--d:%.2fs"></i>' % (h, i * 0.09) for i, h in enumerate(HEIGHTS))
    steps = "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in t["steps"])
    faqs = "".join('<details><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in t["faqs"])
    li = lambda xs: "".join("<li>%s</li>" % e(x) for x in xs)
    en_url, es_url = SITE + "/speakboard/", SITE + "/speakboard/es/"
    ios = '<a class="badge" href="https://apps.apple.com/app/id6834709098" aria-label="%s">%s<span><small>%s</small>App Store</span></a>' % (e(t["ios_aria"]), APPLE, e(t["ios_small"]))
    mac = '<a class="btn mac" href="%s" download>%s</a>' % (DMG, e(t["mac"]))
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{SITE}{t['path']}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:title" content="Speakboard: {e(t['h1'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{SITE}{t['path']}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/images/apps/speakboard/icon.webp">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#08090c">
<link rel="icon" href="{up}images/apps/speakboard/icon.webp" type="image/webp">
<link rel="preload" href="{up}fonts/bricolage-grotesque-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{up}studio.css">
<style>{CSS}</style>
<script src="/umami.js" defer></script>
</head>
<body class="landing" style="--bg:{BG}">
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="nav">
  <div class="wrap">
    <a href="{t['home']}" class="brand" aria-label="Saga Lab">{LOGO}Saga Lab</a>
    <a class="l-back" href="{t['other']}" hreflang="{t['hreflang_other']}">{'Español' if t['lang']=='en' else 'English'}</a>
  </div>
</header>
<main id="main">
  <section class="l-hero">
    <div class="wrap">
      <div class="l-copy">
        <div class="app-id"><img src="{up}images/apps/speakboard/icon.webp" alt="" width="64" height="64"><div><p class="l-name">Speakboard</p><span class="platform">{e(t['plat'])}</span></div></div>
        <h1>{e(t['h1'])}</h1>
        <p class="l-desc">{e(t['lead'])}</p>
        <div class="links">{mac}{ios}</div>
        <p class="sb-note">{e(t['macn'])}</p>
      </div>
      <div class="sb-demo" aria-hidden="true"><div class="sb-wave">{bars}</div><p class="raw">{e(t['raw'])}</p><p>{e(t['clean'])}</p></div>
    </div>
  </section>
  <section class="sb-sec" id="how"><div class="wrap"><h2>{e(t['how'])}</h2><div class="sb-grid">{steps}</div></div></section>
  <section class="sb-sec" id="privacy"><div class="wrap"><h2>{e(t['priv'])}</h2><div class="sb-grid two"><p>{e(t['privp'][0])}</p><p>{e(t['privp'][1])} <a href="{t['privu']}">{e(t['privl'])}</a></p></div></div></section>
  <section class="sb-sec" id="pricing"><div class="wrap"><h2>{e(t['price'])}</h2><div class="sb-grid">
    <div class="sb-plan"><h3>{e(t['free'])}</h3><div class="sb-price">$0</div><ul>{li(t['freeli'])}</ul><div class="links"><a class="btn btn-light btn-sm" href="https://apps.apple.com/app/id6834709098">{e(t['getfree'])}</a></div></div>
    <div class="sb-plan"><h3>{e(t['pro'])}</h3><div class="sb-price">$5.99 <small>{e(t['mo'])}</small></div><ul>{li(t['proli'])}</ul><div class="links"><a class="btn btn-light btn-sm" href="{DMG}" download>{e(t['mac'])}</a></div></div>
    <div class="sb-plan best"><h3>{e(t['proa'])}</h3><div class="sb-price">$29.99 <small>{e(t['yr'])}</small></div><ul>{li(t['annli'])}</ul><div class="links"><a class="btn btn-light btn-sm" href="{DMG}" download>{e(t['mac'])}</a></div></div>
  </div><p class="sb-note">{e(t['pn'])}</p></div></section>
  <section class="sb-sec" id="faq"><div class="wrap"><h2>{e(t['faq'])}</h2>{faqs}</div></section>
</main>
<footer class="l-foot">
  <div class="wrap">
    <span>&copy; 2026 Saga Lab</span>
    <nav aria-label="Speakboard"><a href="{t['home']}">{t['foot'][0]}</a><a href="{t['privu']}">{t['foot'][1]}</a><a href="{t['termsu']}">{t['foot'][2]}</a><a href="{t['supu']}">{t['foot'][3]}</a></nav>
  </div>
</footer>
</body>
</html>
'''


def main():
    for t, p in ((T["en"], "speakboard/index.html"), (T["es"], "speakboard/es/index.html")):
        open(p, "w", encoding="utf-8").write(page(t))
        print(p)


if __name__ == "__main__":
    main()
