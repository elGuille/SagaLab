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

# Ilustraciones: SVG a mano, trazo unico de 3 px, violeta de la app + neutros. Sin texto dentro (no necesitan traduccion).
SW = 'stroke="#1d1233" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
ICON = '<svg class="sb-icon" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="15" fill="#7113fb"/><rect x="22" y="9" width="20" height="30" rx="10" fill="#fff"/><circle cx="28" cy="20" r="2" fill="#7113fb"/><circle cx="36" cy="20" r="2" fill="#7113fb"/><path d="M15 31a17 17 0 0 0 34 0M32 48v6M24 54h16" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>'
PILL_BARS = [(0, 18, "#7a7a85"), (1, 26, "#6f5a8f"), (2, 38, "#5b2d9c"), (3, 34, "#5b2d9c"), (4, 46, "#5a1fb5"), (5, 34, "#5b2d9c"), (6, 38, "#5b2d9c"), (7, 26, "#6f5a8f"), (8, 18, "#7a7a85")]


def pill(cx, cy):
    bars = "".join('<path d="M%d %d v%d" stroke="%s" stroke-width="7" stroke-linecap="round"/>' % (cx - 52 + i * 13, cy - h / 2 + 3.5, h - 7, c) for i, h, c in PILL_BARS)
    return '<rect x="%d" y="%d" width="150" height="52" rx="26" fill="#ecebf4" %s/>%s' % (cx - 75, cy - 26, SW, bars)


HERO_SVG = f"""<svg class="sb-art" viewBox="0 0 720 510" aria-hidden="true" focusable="false">
<ellipse cx="360" cy="478" rx="330" ry="14" fill="#e6def7"/>
<g transform="translate(0 40)">
<rect x="10" y="40" width="520" height="320" rx="22" fill="#fff" {SW}/>
<rect x="26" y="56" width="488" height="288" rx="10" fill="#efe9fd"/>
<g fill="#d8d0ea"><circle cx="46" cy="76" r="5"/><circle cx="62" cy="76" r="5"/></g>
{pill(270, 84)}
<rect x="80" y="150" width="380" height="170" rx="14" fill="#fff" {SW}/>
<path d="M104 190h150M104 218h250M104 246h200" stroke="#d8d0ea" stroke-width="10" stroke-linecap="round"/>
<path d="M312 246h40" stroke="#7113fb" stroke-width="10" stroke-linecap="round"/>
<path d="M362 236v20" stroke="#1d1233" stroke-width="3" stroke-linecap="round"/>
<path d="M236 360l-10 40h88l-10-40" fill="#d8d0ea" {SW}/>
<rect x="166" y="398" width="208" height="18" rx="9" fill="#fff" {SW}/>
</g>
<g transform="translate(0 40)">
<rect x="470" y="70" width="220" height="380" rx="40" fill="#fff" {SW}/>
<rect x="484" y="84" width="192" height="352" rx="28" fill="#faf8ff"/>
<rect x="550" y="94" width="60" height="14" rx="7" fill="#1d1233"/>
<path d="M500 144h92a14 14 0 0 1 0 0v26a14 14 0 0 1-14 14h-64a14 14 0 0 1-14-14v-12a14 14 0 0 1 14-14z" fill="#e6def7"/>
<rect x="540" y="196" width="124" height="40" rx="16" fill="#7113fb"/>
<path d="M556 212h72M556 224h44" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M484 296h192v112a28 28 0 0 1-28 28h-136a28 28 0 0 1-28-28z" fill="#ece8f6"/>
<g fill="#fff" {SW}><rect x="494" y="308" width="30" height="26" rx="8"/><rect x="530" y="308" width="30" height="26" rx="8"/><rect x="566" y="308" width="30" height="26" rx="8"/><rect x="602" y="308" width="30" height="26" rx="8"/><rect x="638" y="308" width="30" height="26" rx="8"/><rect x="494" y="342" width="30" height="26" rx="8"/><rect x="530" y="342" width="30" height="26" rx="8"/><rect x="566" y="342" width="30" height="26" rx="8"/><rect x="602" y="342" width="30" height="26" rx="8"/><rect x="638" y="342" width="30" height="26" rx="8"/></g>
<rect x="494" y="376" width="174" height="44" rx="16" fill="#7113fb" {SW}/>
<g stroke="#fff" stroke-width="5" stroke-linecap="round"><path d="M531 392v12M545 388v20M559 384v28M573 390v16M587 386v24M601 391v14M615 388v20M629 393v10"/></g>
</g>
<rect x="430" y="10" width="200" height="66" rx="33" fill="#fff" {SW}/>
<path d="M590 74l14 36 18-40" fill="#fff" {SW}/>
<g stroke="#7113fb" stroke-width="7" stroke-linecap="round"><path d="M464 33v20M480 26v34M496 21v44M512 28v30M528 17v52M544 28v30M560 22v42M576 31v24M592 37v12"/></g>
<g fill="#7113fb"><circle cx="410" cy="150" r="5"/><circle cx="650" cy="20" r="5"/></g>
<path d="M690 120v18M681 129h18" stroke="#7113fb" stroke-width="3" stroke-linecap="round"/>
</svg>"""


def spot(body):
    return '<svg class="sb-spot" viewBox="0 0 140 110" aria-hidden="true" focusable="false"><ellipse cx="70" cy="58" rx="62" ry="48" fill="#efe9fd"/>%s</svg>' % body


SPOTS = [
    # 1. pulsar la tecla
    spot(f'<rect x="32" y="60" width="76" height="36" rx="12" fill="#7113fb" {SW}/><rect x="62" y="67" width="16" height="16" rx="8" fill="#fff"/><path d="M57 82a13 13 0 0 0 26 0M70 95v-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" transform="translate(0 -3)"/><rect x="58" y="8" width="24" height="56" rx="12" fill="#fff" {SW}/><path d="M36 50l-8-6M104 50l8-6M32 62l-10 0M108 62l10 0" stroke="#7113fb" stroke-width="3" stroke-linecap="round"/>'),
    # 2. hablar: el micro con ojos del icono y ondas
    spot(f'<rect x="52" y="14" width="36" height="54" rx="18" fill="#fff" {SW}/><circle cx="62" cy="34" r="3" fill="#1d1233"/><circle cx="78" cy="34" r="3" fill="#1d1233"/><path d="M42 54a28 28 0 0 0 56 0M70 82v10M58 94h24" fill="none" {SW}/><path d="M18 38q-6 14 0 28M28 44q-4 8 0 16M122 38q6 14 0 28M112 44q4 8 0 16" fill="none" stroke="#7113fb" stroke-width="3" stroke-linecap="round"/>'),
    # 3. aparece el texto
    spot(f'<rect x="16" y="24" width="104" height="66" rx="12" fill="#fff" {SW}/><path d="M16 44h104" stroke="#1d1233" stroke-width="3"/><circle cx="29" cy="34" r="3" fill="#d8d0ea"/><circle cx="40" cy="34" r="3" fill="#d8d0ea"/><path d="M30 60h56M30 74h30" stroke="#d8d0ea" stroke-width="7" stroke-linecap="round"/><path d="M68 74h22" stroke="#7113fb" stroke-width="7" stroke-linecap="round"/><path d="M98 66v16" stroke="#1d1233" stroke-width="3" stroke-linecap="round"/><path d="M118 8l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#7113fb"/>'),
]

PRIV_SVG = f"""<svg class="sb-art priv" viewBox="0 0 260 190" aria-hidden="true" focusable="false">
<ellipse cx="108" cy="92" rx="100" ry="82" fill="#efe9fd"/>
<rect x="62" y="14" width="92" height="160" rx="22" fill="#fff" {SW}/>
<rect x="92" y="24" width="32" height="8" rx="4" fill="#1d1233"/>
<g stroke="#7113fb" stroke-width="7" stroke-linecap="round"><path d="M80 90v14M92 78v38M104 66v62M116 74v46M128 84v26M140 92v10"/></g>
<path d="M170 60q18 0 18 18M170 44q34 0 34 34" fill="none" stroke="#d8d0ea" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>
<path d="M158 86h4" stroke="#d8d0ea" stroke-width="3" stroke-linecap="round"/>
<path d="M206 130c-14 0-20-8-20-16s7-15 16-15c3-9 11-14 20-12 10 2 15 10 14 18 8 1 12 6 12 12 0 7-6 13-14 13z" transform="translate(-6 -14)" fill="#fff" stroke="#9a90b5" stroke-width="3" stroke-linejoin="round" stroke-dasharray="1 8" stroke-linecap="round"/>
<path d="M200 80l48 52" stroke="#1d1233" stroke-width="3" stroke-linecap="round" transform="translate(-6 -14)"/>
<rect x="116" y="124" width="52" height="46" rx="12" fill="#7113fb" {SW}/>
<path d="M128 124v-12a14 14 0 0 1 28 0v12" fill="none" {SW}/>
<circle cx="142" cy="144" r="5" fill="#fff"/><path d="M142 147v10" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
</svg>"""

CSS = """
:root{--ink:#1d1233;--ink2:#4b4266;--v:#7113fb;--vt:#efe9fd;--line:#d8d0ea}
body.landing{background:#fbfaff;color:var(--ink)}
.landing .brand,.landing .l-back{color:var(--ink);opacity:1}
.landing .brand svg{border-radius:7px}
.l-back{font-weight:600;padding:8px 14px;border:3px solid var(--ink);border-radius:999px;background:#fff}
.landing a:focus-visible,.landing summary:focus-visible{outline:3px solid var(--v);outline-offset:3px;border-radius:8px}
.nav .wrap{padding:0 24px}
.l-hero{min-height:0;padding:120px 0 72px}
.l-hero .wrap{grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:40px}
.l-hero h1{max-width:none;margin-top:28px;font-size:clamp(44px,4.6vw,68px)}
.l-desc{color:var(--ink2);max-width:36ch}
.landing .platform{opacity:1;color:var(--ink2)}
.l-name{color:var(--ink)}
.sb-icon{width:64px;height:64px;flex:none;border:3px solid var(--ink);border-radius:18px;box-sizing:border-box;background:#7113fb}
.app-id{display:flex;align-items:center;gap:16px}
.sb-art{display:block;width:100%;height:auto}
.sb-spot{display:block;width:140px;height:110px;margin-bottom:12px}
.landing .btn{min-height:48px;border:3px solid var(--ink);border-radius:14px;box-shadow:0 4px 0 var(--ink);background:var(--v);color:#fff;font-weight:700;transition:transform .15s,box-shadow .15s}
.landing .btn:hover{transform:translateY(2px);box-shadow:0 2px 0 var(--ink)}
.landing .btn.mac,.landing .btn.btn-light{background:var(--v);color:#fff;border-radius:14px;padding:0 20px;font-size:16px}
.landing .badge{border:3px solid var(--ink);border-radius:14px;height:48px;box-shadow:0 4px 0 var(--ink)}
.landing .badge:hover{border-color:var(--ink);transform:translateY(2px);box-shadow:0 2px 0 var(--ink)}
.sb-grid+.sb-note{margin-top:28px}
.sb-note{margin:16px 0 0;font-size:14px;color:var(--ink2)}
.sb-demo{margin-top:28px;background:#fff;border:3px solid var(--ink);border-radius:22px;padding:18px 20px;max-width:440px}
.sb-demo p{margin:0;font-size:18px;line-height:1.4;color:var(--ink)}
.sb-demo .raw{color:var(--ink2);font-size:15px;margin-bottom:8px}
.sb-sec{padding:72px 0}
.sb-sec.tint{background:var(--vt);border-block:3px solid var(--ink)}
.sb-sec h2{margin:0 0 32px;font-size:clamp(30px,4vw,52px);line-height:1.05;letter-spacing:-.035em;font-weight:800;max-width:20ch;color:var(--ink)}
.sb-grid{display:grid;gap:28px;grid-template-columns:repeat(3,minmax(0,1fr))}
.sb-grid h3{margin:0 0 6px;font-size:21px;color:var(--ink)}
.sb-grid p,.sb-sec p{margin:0;color:var(--ink2);line-height:1.55;max-width:60ch}
.sb-priv{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,320px);gap:40px;align-items:center}
.sb-priv p+p{margin-top:12px}
.sb-priv .sb-art{max-width:320px}
.sb-plan{background:#fff;border:3px solid var(--ink);border-radius:22px;padding:24px;min-width:0;display:flex;flex-direction:column}
.sb-plan.best{background:var(--vt);box-shadow:8px 8px 0 var(--v)}
.sb-plan h3{margin:0;color:var(--ink)}
.sb-price{font-size:42px;font-weight:800;letter-spacing:-.03em;margin:6px 0 12px;color:var(--ink)}
.sb-price small{font-size:16px;font-weight:500;color:var(--ink2)}
.sb-plan ul{margin:0;padding-left:20px;color:var(--ink2);line-height:1.6;flex:1}
.sb-plan .links{margin-top:22px}
.sb-sec details{background:#fff;border:3px solid var(--ink);border-radius:16px;padding:16px 20px;margin-bottom:12px;max-width:820px}
.sb-sec summary{cursor:pointer;font-weight:650;font-size:18px;color:var(--ink);list-style:none;display:flex;justify-content:space-between;gap:16px;align-items:center}
.sb-sec summary::-webkit-details-marker{display:none}
.sb-sec summary::after{content:"+";font-size:26px;line-height:1;color:var(--v);flex:none}
.sb-sec details[open] summary::after{content:"\\2212"}
.sb-sec details p{margin-top:10px}
.sb-sec a:not(.btn){color:var(--v);font-weight:600}
.l-foot{color:var(--ink2);padding:32px 0 36px}
.l-foot a{color:var(--ink2)}
@media(max-width:800px){.sb-grid{grid-template-columns:minmax(0,1fr)}.sb-priv{grid-template-columns:minmax(0,1fr)}.sb-priv .sb-art{max-width:240px}.l-hero{padding-top:96px}.l-hero .wrap{grid-template-columns:minmax(0,1fr);gap:32px}.l-hero .wrap,.nav .wrap,.sb-sec .wrap,.l-foot .wrap{padding-left:16px;padding-right:16px}.sb-sec{padding:48px 0}.sb-sec.tint{border-block-width:3px}.sb-plan.best{box-shadow:5px 5px 0 var(--v)}}
@media(prefers-reduced-motion:reduce){.landing .btn,.landing .badge{transition:none}}
"""

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
    steps = "".join('<div>%s<h3>%s</h3><p>%s</p></div>' % (SPOTS[i], e(a), e(b)) for i, (a, b) in enumerate(t["steps"]))
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
        <div class="app-id">{ICON}<div><p class="l-name">Speakboard</p><span class="platform">{e(t['plat'])}</span></div></div>
        <h1>{e(t['h1'])}</h1>
        <p class="l-desc">{e(t['lead'])}</p>
        <div class="links">{mac}{ios}</div>
        <p class="sb-note">{e(t['macn'])}</p>
        <div class="sb-demo" aria-hidden="true"><p class="raw">{e(t['raw'])}</p><p>{e(t['clean'])}</p></div>
      </div>
      <div>{HERO_SVG}</div>
    </div>
  </section>
  <section class="sb-sec" id="how"><div class="wrap"><h2>{e(t['how'])}</h2><div class="sb-grid">{steps}</div></div></section>
  <section class="sb-sec tint" id="privacy"><div class="wrap"><div class="sb-priv"><div><h2>{e(t['priv'])}</h2><p>{e(t['privp'][0])}</p><p>{e(t['privp'][1])} <a href="{t['privu']}">{e(t['privl'])}</a></p></div>{PRIV_SVG}</div></div></section>
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
