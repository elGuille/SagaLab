# -*- coding: utf-8 -*-
"""Ranking de Dora (2 nov 2026): de foto a video con fotos propias y de familia, EN + ES.

Angulo propio, distinto de doravideo.com: que pasa con las fotos de tu familia. Datos del 2 nov 2026:
descripcion y etiqueta de privacidad de cada ficha de EE. UU.; nota de EE. UU. en EN y de Espana en ES (API de lookup);
Google Fotos en support.google.com/photos/answer/16763021. Sin prueba de calidad. Se dice como cobra cada app, no cuanto.
Sin bailes ni abrazos. Sin rayas.
"""
import json
import re

ISO = "2026-11-02"
EN = "blog/best-photo-to-video-ai-apps-iphone.html"
ES = "blog/es/mejores-apps-ia-foto-a-video-iphone.html"
GP = "https://support.google.com/photos/answer/16763021"
DORA = "https://apps.apple.com/app/id6754180384"
DORA_WEB = "https://doravideo.com/create?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=photo_to_video"
IDS = dict(myheritage=477971748, gphotos=962194608, kling=6738049229, dora=6754180384, runway=1665024375, motionleap=1381206010)
NAMES = dict(myheritage="MyHeritage", gphotos="Google Photos", kling="Kling AI", dora="Dora", runway="Runway", motionleap="Motionleap")
ORDER = ["myheritage", "gphotos", "kling", "dora", "runway", "motionleap"]


def url(k):
    return DORA if k == "dora" else "https://apps.apple.com/us/app/id%d" % IDS[k]


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


T = {
"en": dict(
 path=EN, kicker="AI video", date="2 November 2026",
 h1="Best photo-to-video AI apps on iPhone for your own and family photos (2026)",
 desc="Six iPhone apps that animate your own and family photos: MyHeritage, Google Photos, Kling AI, Dora, Runway and Motionleap, compared by what each does with your pictures, from App Store pages and privacy labels.",
 stand="A family photo is not a product shot. Here is which apps are built for it, and what each one's privacy label says about the pictures you give it.",
 switch='<a href="es/mejores-apps-ia-foto-a-video-iphone.html" hreflang="es">Leer en espa&ntilde;ol</a>',
 disc="Everything here comes from App Store pages, privacy labels and help pages read on 2 November 2026. We did not test video quality, so the order is by how directly each app serves this job, not by which looks best.",
 intro="<p>Most photo-to-video rankings judge effects and models. With your own photos, and above all with photos of relatives, two other questions come first: is the app made for this kind of picture, and where do the pictures go? Read the label column before you upload anything.</p>",
 th=("#", "App", "Best for", "How it charges", "User content on its privacy label", "US rating"),
 rows=dict(
  myheritage=("Old family photos and ancestors' faces", "Subscriptions", "Linked to you and not linked to you", "4.9"),
  gphotos=("Photos already backed up in Google Photos", "Limited generations a day; a Google AI plan gives more", "Linked to you", "4.8"),
  kling=("Recent photos, clips up to 15 seconds that can be extended", "Plans and credit packs", "Linked to you and not linked to you", "4.7"),
  dora=("A photo of you, a pet or a product", "Subscription with coins, plus coin packs", "Not linked to you", "4.3"),
  runway=("Choosing the model yourself", "Free to start; plans and credit packs", "Not linked to you", "4.5"),
  motionleap=("Moving water, sky or one detail", "Paid unlimited access", "Not listed", "4.8")),
 note="The label is what each developer declares to Apple, not an audit. &ldquo;User Content&rdquo; is Apple's category for things such as photos and videos.",
 sec=dict(
  myheritage=("MyHeritage: made for family photos", "It is a family tree app first. Its page says Deep Nostalgia makes the faces in historical family photos move, and LiveMemory turns photos into video clips and can animate entire family photos. It also repairs, colorizes and scans old photos in the same app. Choose it for grandparents' pictures, especially if you want the tree too. The app is much bigger than this one job, and it charges through subscriptions."),
  gphotos=("Google Photos: if your photos are already there", "Its help page says Photo to video needs the photo to be backed up, needs a connection and a personal Google Account, and requires you to be at least 13, or 18 for the text prompt option. You get a limited number of generations a day, more with a Google AI plan, and Google warns of &ldquo;unexpected or inaccurate results&rdquo;. It also says these features are not available in all regions. If your library is not in Google Photos, using this means putting it there first."),
  kling=("Kling AI: when the clip matters more than the memory", "A general generator. Its page promises up to 15 seconds in native 1080p or 4K, and extension up to 3 minutes. Nothing on the page is aimed at family photos. It also has a community feed, so check what you share. If it does not fit, see these <a href=\"https://reditor.cloud/kling-ai-alternatives-iphone/\" target=\"_blank\" rel=\"noopener\">Kling AI alternatives for iPhone</a>."),
  dora=("Dora: a photo of you, a pet or a product", "You upload a photo and pick a template or describe what should happen, then get the video in about two minutes. Its page says the cost is shown before you generate, the coins come back if a generation fails, and videos have no watermark. Its account also works on the web and inside Claude and ChatGPT. One limit matters here: its page says it does not create content involving minors, so it is not for photos of your children. It needs a paid plan."),
  runway=("Runway: several models in one app", "Its page says it turns any photo into motion and lists models such as Seedance 2.5, Kling 3 Pro and Gen-4.5, with a first generation in about two minutes. Characters can stay consistent across shots, and work syncs with your computer. It suits someone who wants to compare and make a short film more than someone animating one picture. Other options: <a href=\"https://reditor.cloud/runway-alternatives-iphone/\" target=\"_blank\" rel=\"noopener\">Runway alternatives for iPhone</a>."),
  motionleap=("Motionleap: move part of the photo", "You choose what moves in the picture: water, clouds, a candle flame, steam from a cup. Its page is about moving elements in still photos, not about people, so it suits a holiday or landscape picture. Its label is the only one here that does not list user content.")),
 tips_h="Before you upload a photo of someone else",
 tips=["Ask them if you can. It is their face, and the app's servers may keep it for a time set by its own privacy policy.", "Keep the original. An AI video is a new interpretation, not a restored copy: expressions and movements are invented.", "Read the label and the privacy policy linked from the App Store page. Our table covers only the label.", "Do not present the result as real footage. Say it was made with AI when you share it."],
 left_h="Who we left out",
 left="Apps built mainly around jokes and viral effects, such as Revive and Pika, do animate photos (here are some <a href=\"https://reditor.cloud/pika-alternatives-iphone/\" target=\"_blank\" rel=\"noopener\">Pika alternatives</a>), but we kept this list to apps where a family picture is treated as more than a meme. For a wider comparison of AI video apps, see <a href=\"best-ai-video-generator-apps-iphone.html\">the best AI video generator apps for iPhone</a>.",
 faq_h="Questions people ask",
 faq=[("What is the best app to animate old family photos on iPhone?", "MyHeritage is the one on this list built for it: its page describes Deep Nostalgia for historical family photos and LiveMemory for video clips. We did not test quality."),
  ("Can I animate photos with Google Photos on iPhone?", "Google's help page describes Photo to video, for backed-up photos, with a limited number of generations a day and not in all regions."),
  ("Can I use an AI video app with photos of my children?", "It depends on the app. Dora's page says it does not create content involving minors. Google Photos sets a minimum age for the account holder, 13. Check each app's own rules, and think about whether the picture should leave your phone at all."),
  ("Do these apps keep my photos?", "We can only say what the labels declare. MyHeritage, Google Photos and Kling AI list user content as linked to you, at least in part. Dora and Runway list it as not linked. Motionleap does not list it. How long a photo is kept is set by each privacy policy."),
  ("Are these apps free?", "All can be downloaded for free and sell in-app purchases. Runway says it is free to start. Google Photos gives a limited number of generations a day. Dora needs a paid plan.")],
 src_h="Sources",
 src=["App Store pages and privacy labels, US, read on 2 November 2026: %s." % ", ".join(a(url(k), NAMES[k]) for k in ORDER), "Ratings: Apple's public lookup API, US store, 2 November 2026.", a(GP, "Use AI to create with Google Photos") + ", Google Photos Help, read on 2 November 2026."],
 own='Disclosure: we make Dora, number 4 on this list.',
 fix='If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
 cta='Dora on the <a href="%s" target="_blank" rel="noopener">App Store</a> or <a href="%s">on the web</a>.' % (DORA, DORA_WEB),
),
"es": dict(
 path=ES, kicker="V&iacute;deo con IA", date="2 de noviembre de 2026",
 h1="Mejores apps de IA para convertir tus fotos y las de tu familia en vídeo en iPhone (2026)",
 desc="Seis apps de iPhone para animar fotos propias y familiares: MyHeritage, Google Fotos, Kling AI, Dora, Runway y Motionleap, comparadas por lo que hace cada una con tus imágenes, según su ficha y su etiqueta de privacidad.",
 stand="Una foto de familia no es una foto de producto. Aquí va qué apps están pensadas para ella y qué dice la etiqueta de privacidad de cada una sobre las imágenes que le das.",
 switch='<a href="../best-photo-to-video-ai-apps-iphone.html" hreflang="en">Read in English</a>',
 disc="Todo sale de las fichas del App Store, las etiquetas de privacidad y las páginas de ayuda, leídas el 2 de noviembre de 2026. No hemos probado la calidad de los vídeos: el orden va por lo directamente que cada app resuelve esta tarea, no por cuál se ve mejor.",
 intro="<p>Casi todas las listas de foto a vídeo juzgan efectos y modelos. Con tus propias fotos, y sobre todo con las de tus familiares, antes van otras dos preguntas: si la app está hecha para ese tipo de imagen y adónde van las fotos. Lee la columna de la etiqueta antes de subir nada.</p>",
 th=("#", "App", "Mejor para", "Cómo cobra", "Contenido del usuario en su etiqueta", "Nota (España)"),
 rows=dict(
  myheritage=("Fotos antiguas de la familia y caras de antepasados", "Suscripciones", "Vinculado a ti y no vinculado", "4,8"),
  gphotos=("Fotos que ya están en Google Fotos", "Generaciones limitadas al día; más con un plan de Google AI", "Vinculado a ti", "4,8"),
  kling=("Fotos recientes, clips de hasta 15 segundos ampliables", "Planes y paquetes de créditos", "Vinculado a ti y no vinculado", "4,6"),
  dora=("Una foto tuya, de tu mascota o de un producto", "Suscripción con monedas, más paquetes de monedas", "No vinculado a ti", "4,3 (EE. UU.)"),
  runway=("Elegir tú el modelo", "Gratis para empezar; planes y paquetes de créditos", "No vinculado a ti", "4,4"),
  motionleap=("Mover el agua, el cielo o un detalle", "Acceso ilimitado de pago", "No aparece", "4,7")),
 note="La etiqueta es lo que cada desarrollador declara a Apple, no una auditoría. «Contenido del usuario» es la categoría de Apple para cosas como fotos y vídeos. Las etiquetas y descripciones son de la ficha de EE. UU.",
 sec=dict(
  myheritage=("MyHeritage: hecha para fotos de familia", "Es ante todo una app de árbol genealógico. Su ficha dice que Deep Nostalgia hace que se muevan las caras de las fotos familiares históricas y que LiveMemory convierte fotos en clips de vídeo y anima fotos de familia enteras. En la misma app repara, colorea y escanea fotos antiguas. Elígela para las fotos de los abuelos, sobre todo si también quieres el árbol. La app es mucho más grande que esta tarea y cobra con suscripciones."),
  gphotos=("Google Fotos: si tus fotos ya están allí", "Su página de ayuda dice que Foto a vídeo necesita que la foto tenga copia de seguridad, conexión y una cuenta personal de Google, y tener al menos 13 años, o 18 para la opción de texto. Hay un número limitado de generaciones al día, más con un plan de Google AI, y Google avisa de «resultados inesperados o incorrectos». También dice que estas funciones no están disponibles en todas las regiones, así que comprueba si te aparece. Si tu biblioteca no está en Google Fotos, usarla significa subirla primero."),
  kling=("Kling AI: cuando importa más el clip que el recuerdo", "Un generador general. Su ficha promete hasta 15 segundos en 1080p o 4K nativos, y ampliar hasta 3 minutos. Nada en la ficha va dirigido a fotos de familia. También tiene un apartado de comunidad: mira qué compartes."),
  dora=("Dora: una foto tuya, de tu mascota o de un producto", "Subes una foto, eliges una plantilla o describes lo que debe pasar y tienes el vídeo en unos dos minutos. Su ficha dice que el coste se ve antes de generar, que las monedas vuelven si la generación falla y que los vídeos no llevan marca de agua. La cuenta también funciona en la web y dentro de Claude y ChatGPT. Aquí importa un límite: su ficha dice que no crea contenido con menores, así que no sirve para fotos de tus hijos. Necesita un plan de pago."),
  runway=("Runway: varios modelos en una app", "Su ficha dice que da movimiento a cualquier foto y nombra modelos como Seedance 2.5, Kling 3 Pro y Gen-4.5, con una primera generación en unos dos minutos. Los personajes pueden seguir iguales entre planos y el trabajo se sincroniza con tu ordenador. Encaja más con quien quiere comparar y montar un corto que con quien anima una sola imagen."),
  motionleap=("Motionleap: mover una parte de la foto", "Tú eliges qué se mueve en la imagen: el agua, las nubes, la llama de una vela, el vapor de una taza. Su ficha habla de mover elementos en fotos fijas, no de personas, así que encaja con una foto de vacaciones o de paisaje. Su etiqueta es la única de aquí que no incluye contenido del usuario.")),
 tips_h="Antes de subir una foto de otra persona",
 tips=["Pregúntale. Es su cara, y cuánto tiempo la guardan los servidores de la app depende de su política de privacidad.", "Guarda el original. Un vídeo con IA es una interpretación nueva, no una copia restaurada: los gestos y movimientos son inventados.", "Lee la etiqueta y la política de privacidad enlazada en la ficha. Nuestra tabla solo cubre la etiqueta.", "No lo presentes como una grabación real. Di que está hecho con IA cuando lo compartas."],
 left_h="Las que hemos dejado fuera",
 left="Las apps centradas sobre todo en bromas y efectos virales, como Revive y Pika, también animan fotos, pero hemos limitado la lista a las que tratan una foto de familia como algo más que un meme. Para una comparativa más amplia, mira <a href=\"mejores-apps-generador-video-ia-iphone.html\">las mejores apps para generar vídeo con IA en iPhone</a>.",
 faq_h="Preguntas frecuentes",
 faq=[("¿Cuál es la mejor app para animar fotos antiguas de la familia en iPhone?", "MyHeritage es la de esta lista hecha para eso: su ficha describe Deep Nostalgia para fotos familiares históricas y LiveMemory para clips de vídeo. No hemos probado la calidad."),
  ("¿Puedo animar fotos con Google Fotos en iPhone?", "La ayuda de Google describe Foto a vídeo, para fotos con copia de seguridad, con un número limitado de generaciones al día y no en todas las regiones."),
  ("¿Puedo usar una app de vídeo con IA con fotos de mis hijos?", "Depende de la app. La ficha de Dora dice que no crea contenido con menores. Google Fotos pide una edad mínima de 13 años al titular de la cuenta. Mira las normas de cada app y piensa si esa foto debe salir de tu móvil."),
  ("¿Estas apps guardan mis fotos?", "Solo podemos decir lo que declaran las etiquetas. MyHeritage, Google Fotos y Kling AI incluyen contenido del usuario vinculado a ti, al menos en parte. Dora y Runway lo declaran no vinculado. Motionleap no lo incluye. Cuánto se guarda una foto lo fija cada política de privacidad."),
  ("¿Son gratis estas apps?", "Todas se descargan gratis y venden compras dentro de la app. Runway dice que es gratis para empezar. Google Fotos da un número limitado de generaciones al día. Dora necesita un plan de pago.")],
 src_h="Fuentes",
 src=["Fichas del App Store y etiquetas de privacidad, EE. UU., leídas el 2 de noviembre de 2026: %s." % ", ".join(a(url(k), NAMES[k]) for k in ORDER), "Notas: API pública de Apple, tienda de España, 2 de noviembre de 2026; la de Dora, de EE. UU.", a(GP + "?hl=es", "Usar la IA para crear con Google Fotos") + ", Ayuda de Google Fotos, leída el 2 de noviembre de 2026."],
 own='Aviso: hacemos Dora, la número 4 de esta lista.',
 fix='Si algo está desactualizado, <a href="mailto:sagalabs@proton.me">avísanos</a> y lo corregimos.',
 cta='Dora en el <a href="%s" target="_blank" rel="noopener">App Store</a> o <a href="%s">en la web</a>.' % (DORA, DORA_WEB),
)}
T["es"]["names"] = dict(NAMES, gphotos="Google Fotos")


def build(render):
    alts = ('    <link rel="alternate" hreflang="en" href="https://aisagalab.com/%s">\n'
            '    <link rel="alternate" hreflang="es" href="https://aisagalab.com/%s">\n'
            '    <link rel="alternate" hreflang="x-default" href="https://aisagalab.com/%s">' % (EN, ES, EN))
    out = []
    for lang, c in T.items():
        names = c.get("names", NAMES)
        rows = "".join('<tr><td>%d</td><td><a href="%s" target="_blank" rel="noopener">%s</a></td>%s</tr>\n' % (
            i, url(k), names[k], "".join("<td>%s</td>" % x for x in c["rows"][k])) for i, k in enumerate(ORDER, 1))
        secs = "".join("<h2>%d. %s</h2>\n<p>%s</p>\n" % (i, c["sec"][k][0], c["sec"][k][1]) for i, k in enumerate(ORDER, 1))
        faq = "".join("<h3>%s</h3>\n<p>%s</p>\n" % q for q in c["faq"])
        body = ('<p class="article-kicker">%s</p>\n<h1>%s</h1>\n<p class="article-standfirst">%s</p>\n'
                '<p class="article-meta"><a href="https://www.linkedin.com/in/maruta/" rel="author me noopener" target="_blank">Maruta G</a> &middot; %s <span class="lang-switch"> &middot; %s</span></p>\n'
                '<div class="article-body">\n<p>%s</p>\n%s\n<div class="table-scroll"><table><thead><tr>%s</tr></thead><tbody>\n%s</tbody></table></div>\n<p class="article-note">%s</p>\n%s<p>%s</p>\n'
                '<h2>%s</h2>\n<ul>\n%s</ul>\n<h2>%s</h2>\n<p>%s</p>\n<h2>%s</h2>\n%s</div>\n'
                '<div class="article-body article-sources">\n<h2>%s</h2>\n<ul>\n%s</ul>\n<p>%s</p>\n<p>%s</p>\n</div>') % (
            c["kicker"], c["h1"], c["stand"], c["date"], c["switch"], c["disc"], c["intro"],
            "".join("<th>%s</th>" % h for h in c["th"]), rows, c["note"], secs, c["cta"], c["tips_h"],
            "".join("<li>%s</li>\n" % t for t in c["tips"]), c["left_h"], c["left"], c["faq_h"], faq, c["src_h"],
            "".join("<li>%s</li>\n" % s for s in c["src"]), c["own"], c["fix"])
        art = {"@type": "BlogPosting", "headline": c["h1"], "description": c["desc"], "inLanguage": lang, "datePublished": ISO, "dateModified": ISO,
               "mainEntityOfPage": {"@type": "WebPage", "@id": "https://aisagalab.com/" + c["path"]},
               "author": {"@type": "Person", "name": "Maruta G", "url": "https://www.linkedin.com/in/maruta/"},
               "publisher": {"@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/"}}
        items = {"@type": "ItemList", "name": c["h1"], "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": len(ORDER),
                 "itemListElement": [{"@type": "ListItem", "position": i, "name": names[k], "url": "https://apps.apple.com/app/id%d" % IDS[k]} for i, k in enumerate(ORDER, 1)]}
        faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", r)}} for q, r in c["faq"]]}
        out.append(render(path=c["path"], lang=lang, title=c["h1"] + " | Saga Labs", desc=c["desc"], og_title=c["h1"], body=body,
                          jsonld=json.dumps({"@context": "https://schema.org", "@graph": [art, items, faqld]}, ensure_ascii=False, indent=2), alternates=alts))
    return out
