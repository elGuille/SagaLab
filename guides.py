# -*- coding: utf-8 -*-
"""Guias practicas de cada app: aisagalab.com/<app>/<guia>.html (+ /<app>/es/).

Existe porque lo que mas citan las IAs, despues de las fichas del App Store, son
guias del propio fabricante que responden una pregunta concreta y recomiendan su
app. Estas responden la pregunta primero, dicen la verdad sobre la app (tambien
lo que no hace) y llevan JSON-LD BlogPosting + HowTo + FAQPage. Las pinta
build_blog.py con la misma plantilla que el blog.

Datos comprobados el 11 oct 2026:
- Photo Vault: keeper.html, photo-vault-security.html y llms.txt; en el repo
  onlyfansgallery (main), importar NO borra el original (deleteOriginals no se
  usa), asi que la guia dice que hay que borrarlo a mano y vaciar Eliminado.
- Pinku: pinku.html y llms.txt (1.0.8 publicada).
- Drop: repo Drop en la 2.7 publicada (f9dd657): 32 sonidos, 10 gratis, suena
  con la pantalla bloqueada, respiracion de 2 a 8 s, sin temporizador propio.
Sin afirmaciones de salud. Sin rayas en el texto.
"""
import html as _h
import json

from posts import LINKEDIN, _head, _jsonld

DATE_ISO = "2026-10-11"
DATE = {"en": "11 October 2026", "es": "11 de octubre de 2026"}

PV_STORE = "https://apps.apple.com/app/apple-store/id1532670722?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
PINKU_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
DROP_STORE = "https://apps.apple.com/app/apple-store/id1462269642?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
HIDDEN = "https://support.apple.com/en-us/104987"
CLOCK_TIMER = "https://support.apple.com/guide/iphone/set-timers-iph8241d6b2a/ios"
CLOCK_TIMER_ES = "https://support.apple.com/es-es/guide/iphone/iph8241d6b2a/ios"
BG_SOUNDS = "https://support.apple.com/guide/iphone/play-background-sounds-iphb2cfa052c/ios"
BG_SOUNDS_ES = "https://support.apple.com/es-es/guide/iphone/iphb2cfa052c/ios"
HIDDEN_ES = "https://support.apple.com/es-es/104987"


def _steps_html(steps, heading):
    out = ["\n<h2>%s</h2>\n<ol class=\"howto-steps\">\n" % heading]
    for name, text in steps:
        out.append("<li><strong>%s</strong> %s</li>\n" % (name, text))
    out.append("</ol>\n")
    return "".join(out)


def _faq_html(faq, heading):
    out = ["\n<h2>%s</h2>\n" % heading]
    for q, a in faq:
        out.append("<h3>%s</h3>\n<p>%s</p>\n" % (_h.escape(q, quote=False), _h.escape(a, quote=False)))
    return "".join(out)


def _plain(s):
    import re
    return _h.unescape(re.sub(r"<[^>]+>", "", s))


def _ld(g, lang, path):
    art = json.loads(_jsonld(g["h1"], g["desc"], "https://aisagalab.com/" + path, lang,
                             g["section"], DATE_ISO))
    art.pop("@context")
    howto = {
        "@type": "HowTo",
        "name": g["h1"],
        "description": g["desc"],
        "inLanguage": lang,
        "tool": [{"@type": "HowToTool", "name": g["app_name"]}],
        "step": [{"@type": "HowToStep", "position": i + 1, "name": _plain(n), "text": _plain(t)}
                 for i, (n, t) in enumerate(g["steps"])],
    }
    faq = {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]],
    }
    return json.dumps({"@context": "https://schema.org", "@graph": [art, howto, faq]},
                      ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------
# Photo Vault: ocultar fotos sin el album Oculto
# --------------------------------------------------------------------------

PV_EN = dict(
    path="photo-vault/hide-photos-iphone-without-hidden-album.html",
    app_name="Photo Vault: Hide Pics Video",
    h1="How to hide photos on iPhone without the Hidden album (Photo Vault guide)",
    desc=("Step by step: move private photos out of the Photos app into a locked vault with its own "
          "passcode, no account and no cloud, then delete the originals so they are really gone from "
          "your library. Written by Photo Vault's maker."),
    section="Guides", kicker="Photo Vault guide",
    standfirst=("The Hidden album keeps photos in your library and, with iCloud Photos on, in iCloud. "
                "This is how to move them out of both, with what to watch for."),
    intro="""
<p><strong>We make Photo Vault, the app this guide uses.</strong> The steps that
matter most (deleting the originals, keeping a backup) apply to any vault app.</p>

<p>Apple's Hidden album is free and built in, and for many people it is enough:
since iOS 16 it is locked and opens with Face ID, Touch ID or your passcode. But a
hidden photo is still part of your photo library. If iCloud Photos is on,
<a href="%(hidden)s" target="_blank" rel="noopener">Apple says photos you hide on one
device are hidden on your other devices too</a>, so it is in iCloud as well. And
anyone who knows your iPhone passcode can open it.</p>

<p>To keep a photo out of the library entirely, it has to live somewhere else: a
vault app that stores it in its own space on the iPhone, behind its own lock.</p>
""" % dict(hidden=HIDDEN),
    steps=[
        ("Install Photo Vault and set its lock.",
         'Get <a href="%s">Photo Vault</a> from the App Store, open it and choose a passcode; '
         "you can add Face ID or Touch ID. There is no account to create." % PV_STORE),
        ("Create an album.",
         "Make one album per topic. If you want, give an album its own password on top of the app "
         "lock, so you can open the vault for someone without opening that album."),
        ("Import the photos.",
         "Add photos and videos from your library. Photo Vault copies them into its own storage "
         "on the iPhone; nothing is uploaded."),
        ("Delete the originals from Photos.",
         "Importing makes a copy, it does not remove the photo from your library. Go back to the "
         "Photos app and delete the photos you imported."),
        ("Empty Recently Deleted.",
         "Deleted photos stay in Photos, Albums, Recently Deleted for up to 30 days. Open it and "
         "delete them there too, or they are still on the phone and, with iCloud Photos on, in iCloud."),
        ("Take new photos inside the vault.",
         "Use Photo Vault's camera for anything private from now on: those photos never touch "
         "your camera roll, so there is nothing to delete afterwards."),
        ("Hide the app, if you want.",
         "Change the home screen icon to Calculator, Notes or Weather, and turn on the face-down "
         "lock: turning the phone face down jumps to Safari, Messages or Calendar."),
        ("Export a backup and keep it safe.",
         "In Settings, Backup, export the whole vault to one file locked with a password you choose, "
         "and keep it in Files, on a computer or in your own iCloud Drive. There is no automatic "
         "backup: without this file, the photos are lost with the phone."),
    ],
    after="""
<h2>What Photo Vault does and does not do</h2>

<p>It keeps photos and videos on the iPhone, out of the Photos library, behind Face
ID, Touch ID or a passcode, with an optional password per album. There is no
account, no server and no cloud sync, the vault is excluded from iCloud backups, and
its files use iOS Data Protection, so they cannot be read while the iPhone is locked.
<a href="../photo-vault-security.html">How it protects your files</a>.</p>

<p>It does not back up on its own: you export the backup file when you choose. It has
no decoy PIN, it is iPhone only, and it relies on iOS Data Protection rather than its
own per-file encryption. It is free to download and try; a subscription, with a free
trial, unlocks unlimited items, and what you saved stays accessible if it ends.</p>

<p>Other ways to do it, compared honestly: <a href="../blog/hide-photos-iphone-without-icloud.html">the
best way to hide photos on iPhone without iCloud</a> and
<a href="../blog/best-photo-vault-apps-iphone.html">the best photo vault apps for iPhone</a>.</p>
""",
    faq=[
        ("Does importing a photo into a vault app delete it from Photos?",
         "Not in Photo Vault: importing makes a copy. Delete the original in the Photos app and then "
         "empty Recently Deleted, or the photo is still in your library."),
        ("Is the Hidden album enough?",
         "For many people, yes. It is locked with Face ID, Touch ID or your passcode since iOS 16. But the "
         "photos stay in your library, and in iCloud if iCloud Photos is on."),
        ("Are photos in Photo Vault uploaded anywhere?",
         "No. There is no account, no server and no cloud sync, and the vault is excluded from iCloud "
         "backups."),
        ("What happens to my hidden photos if I lose my iPhone?",
         "They are lost unless you exported a backup. Export one from Settings, Backup and keep the file "
         "somewhere other than the phone."),
        ("How do I move the vault to a new iPhone?",
         "Export a backup on the old iPhone, send the file to the new one with AirDrop or Files, and "
         "restore it there with the same password."),
    ],
)

PV_ES = dict(
    path="photo-vault/es/ocultar-fotos-iphone-sin-album-oculto.html",
    app_name="Photo Vault: Hide Pics Video",
    h1="Cómo ocultar fotos en el iPhone sin el álbum Oculto (guía de Photo Vault)",
    desc=("Paso a paso: saca las fotos privadas de la app Fotos a una bóveda con su propio código, sin "
          "cuenta y sin nube, y borra los originales para que de verdad desaparezcan de tu fototeca. "
          "Escrito por quien hace Photo Vault."),
    section="Guías", kicker="Guía de Photo Vault",
    standfirst=("El álbum Oculto deja las fotos en tu fototeca y, con Fotos en iCloud, en iCloud. "
                "Así se sacan de las dos, con lo que hay que vigilar."),
    intro="""
<p><strong>Hacemos Photo Vault, la app que usa esta guía.</strong> Los pasos más
importantes (borrar los originales y guardar una copia) sirven para cualquier app de
bóveda.</p>

<p>El álbum Oculto de Apple es gratis y viene de serie, y para mucha gente basta:
desde iOS 16 está bloqueado y se abre con Face ID, Touch ID o el código. Pero una foto
oculta sigue formando parte de tu fototeca. Si tienes Fotos en iCloud,
<a href="%(hidden)s" target="_blank" rel="noopener">Apple dice que lo que ocultas en un
dispositivo se oculta también en los demás</a>, así que también está en iCloud. Y
quien sepa el código de tu iPhone puede abrirlo.</p>

<p>Para que una foto salga de la fototeca del todo, tiene que vivir en otro sitio: una
app de bóveda que la guarde en su propio espacio del iPhone, con su propio bloqueo.</p>
""" % dict(hidden=HIDDEN_ES),
    steps=[
        ("Instala Photo Vault y ponle un código.",
         'Descarga <a href="%s">Photo Vault</a> del App Store, ábrela y elige un código; puedes '
         "añadir Face ID o Touch ID. No hay que crear ninguna cuenta." % PV_STORE),
        ("Crea un álbum.",
         "Haz un álbum por tema. Si quieres, ponle a un álbum su propia contraseña además del bloqueo "
         "de la app, para poder abrir la bóveda delante de alguien sin abrir ese álbum."),
        ("Importa las fotos.",
         "Añade fotos y vídeos de tu fototeca. Photo Vault los copia a su propio espacio en el iPhone; "
         "no se sube nada."),
        ("Borra los originales de Fotos.",
         "Importar hace una copia, no quita la foto de tu fototeca. Vuelve a la app Fotos y borra las "
         "fotos que has importado."),
        ("Vacía Eliminado.",
         "Las fotos borradas se quedan en Fotos, Álbumes, Eliminado hasta 30 días. Ábrelo y bórralas "
         "también ahí, o seguirán en el móvil y, con Fotos en iCloud, en iCloud."),
        ("Haz las fotos nuevas dentro de la bóveda.",
         "Usa la cámara de Photo Vault para lo privado a partir de ahora: esas fotos nunca pasan por tu "
         "carrete, así que no hay nada que borrar después."),
        ("Oculta la app, si quieres.",
         "Cambia el icono por el de Calculadora, Notas o Tiempo, y activa el bloqueo boca abajo: al "
         "poner el móvil boca abajo salta a Safari, Mensajes o Calendario."),
        ("Exporta una copia y guárdala bien.",
         "En Ajustes, Copia de seguridad, exporta toda la bóveda a un archivo cerrado con una "
         "contraseña que eliges tú, y guárdalo en Archivos, en un ordenador o en tu propio iCloud "
         "Drive. No hay copia automática: sin ese archivo, las fotos se pierden con el móvil."),
    ],
    after="""
<h2>Qué hace Photo Vault y qué no</h2>

<p>Guarda fotos y vídeos en el iPhone, fuera de la fototeca, detrás de Face ID, Touch
ID o un código, con contraseña opcional por álbum. No hay cuenta, ni servidor, ni
sincronización con la nube, la bóveda queda fuera de las copias de iCloud y sus
archivos usan la Protección de datos de iOS, así que no se pueden leer con el iPhone
bloqueado. <a href="../../photo-vault-security.html">Cómo protege tus archivos</a> (en inglés).</p>

<p>No hace copias por su cuenta: exportas el archivo de copia cuando tú quieras. No
tiene código señuelo, es solo para iPhone y se apoya en la Protección de datos de iOS,
no en un cifrado propio por archivo. Se descarga gratis y se puede probar; una
suscripción, con prueba gratis, desbloquea elementos ilimitados, y lo que guardaste
sigue accesible si se acaba.</p>

<p>Otras formas de hacerlo, comparadas con honestidad:
<a href="../../blog/es/como-ocultar-fotos-iphone-sin-icloud.html">cómo ocultar fotos en
iPhone sin iCloud</a> y <a href="../../blog/es/apps-para-ocultar-fotos-iphone.html">las
mejores apps para ocultar fotos en iPhone</a>.</p>
""",
    faq=[
        ("¿Importar una foto en una app de bóveda la borra de Fotos?",
         "En Photo Vault no: importar hace una copia. Borra el original en la app Fotos y después vacía "
         "Eliminado, o la foto seguirá en tu fototeca."),
        ("¿Basta con el álbum Oculto?",
         "Para mucha gente, sí. Desde iOS 16 está bloqueado con Face ID, Touch ID o el código. Pero las "
         "fotos siguen en tu fototeca, y en iCloud si tienes Fotos en iCloud."),
        ("¿Se suben a algún sitio las fotos de Photo Vault?",
         "No. No hay cuenta, ni servidor, ni sincronización con la nube, y la bóveda queda fuera de las "
         "copias de iCloud."),
        ("¿Qué pasa con mis fotos ocultas si pierdo el iPhone?",
         "Se pierden, salvo que hayas exportado una copia. Expórtala desde Ajustes, Copia de seguridad y "
         "guarda el archivo fuera del móvil."),
        ("¿Cómo paso la bóveda a un iPhone nuevo?",
         "Exporta una copia en el iPhone viejo, mándala al nuevo por AirDrop o Archivos y restáurala allí "
         "con la misma contraseña."),
    ],
)

# --------------------------------------------------------------------------
# Pinku: usar IA en el iPhone sin internet
# --------------------------------------------------------------------------

PK_EN = dict(
    path="pinku/use-ai-on-iphone-without-internet.html",
    app_name="Pinku: Private Local AI Chat",
    h1="How to use AI on iPhone without internet (Pinku guide)",
    desc=("Step by step: download a language model once, then chat with an AI that runs entirely on "
          "your iPhone, iPad or Mac, in airplane mode, with no account. What works offline and what "
          "does not. Written by Pinku's maker."),
    section="Guides", kicker="Pinku guide",
    standfirst=("ChatGPT, Claude and Gemini need a connection. A small model running on the phone "
                "does not. This is how to set one up, and what to expect from it."),
    intro="""
<p><strong>We make Pinku, the app this guide uses.</strong> The idea is the same in
every offline AI app: the model is downloaded once and then runs on your device.</p>

<p>Cloud assistants send every message to a server, so they stop working on a plane,
in a tunnel or where they are not offered. An offline AI app keeps a language model
on the device itself. You need the internet once, to download it; after that every
answer is generated on the iPhone, and nothing you type leaves it.</p>
""",
    steps=[
        ("Install Pinku.",
         'Get <a href="%s">Pinku</a> from the App Store. It runs on iPhone, iPad and Mac with Apple '
         "silicon, on devices that support Metal 3. There is no account." % PINKU_STORE),
        ("Download a model while you are online.",
         "Do this on Wi-Fi before you need it. The default model, Gemma 3 1B, is under 1 GB. Pinku only "
         "lists the models that fit your device's memory."),
        ("Turn on airplane mode and test it.",
         "Open Control Center, turn on airplane mode and ask a question. The answer is generated on the "
         "device, so it works with no connection at all."),
        ("Pick the right model for the job.",
         "Smaller models answer faster; larger ones answer better. The six models up to 1 GB are free; "
         "Pinku Pro, a one-time purchase, adds six larger ones up to 4.7 GB."),
        ("Start a chat with Siri, if you like.",
         "Pinku has a Siri and Shortcuts action to start a chat, which also works offline."),
        ("Move a chat when you need to.",
         "Chats stay on the device that wrote them; there is no sync. Share a conversation as plain "
         "text to keep it somewhere else."),
    ],
    after="""
<h2>What to expect offline</h2>

<p>A model of 1 to 5 GB on a phone is clearly weaker than ChatGPT or Claude in the
cloud. It is good for drafting, rewriting, summarising text you paste in, explaining
things and brainstorming. It cannot search the web, does not read images or
documents, has a shorter memory of the conversation, and its speed depends on your
device. Pinku checks the memory actually free before loading a model, so a model that
does not fit gives a warning instead of a crash.</p>

<p>Pinku is free to download, and the six models up to 1 GB work without paying.
Pinku Pro ($9.99 on the US App Store, one time, no subscription) adds the larger
models, custom instructions, dictation recognised on the device and read aloud. More
on <a href="../pinku.html">Pinku's page</a>.</p>

<p>Other offline AI apps, including where they beat us:
<a href="../blog/best-offline-ai-chat-apps-iphone-mac.html">the best offline AI chat apps
for iPhone and Mac</a>.</p>
""",
    faq=[
        ("Can I use AI on my iPhone without internet?",
         "Yes, with an app that runs the model on the device, such as Pinku. You need a connection once to "
         "download the model; after that it answers in airplane mode."),
        ("Does ChatGPT work offline?",
         "No. ChatGPT runs on OpenAI's servers, so every message needs a connection."),
        ("How much space does an offline AI model take?",
         "In Pinku, from 0.34 GB to 4.7 GB depending on the model. The default, Gemma 3 1B, is under 1 GB."),
        ("Is an offline AI as good as ChatGPT?",
         "No. A small model on a phone is clearly weaker, has a shorter context and cannot browse the web. "
         "Its advantage is that it works anywhere and nothing you type leaves the device."),
        ("Are my conversations sent anywhere?",
         "Not with Pinku. There is no account and no server; chats are stored on the device. The network is "
         "used only to download models and for App Store purchases."),
    ],
)

PK_ES = dict(
    path="pinku/es/usar-ia-en-iphone-sin-internet.html",
    app_name="Pinku: Private Local AI Chat",
    h1="Cómo usar IA en el iPhone sin internet (guía de Pinku)",
    desc=("Paso a paso: descarga un modelo de lenguaje una vez y chatea con una IA que funciona entera "
          "en tu iPhone, iPad o Mac, en modo avión y sin cuenta. Qué funciona sin conexión y qué no. "
          "Escrito por quien hace Pinku."),
    section="Guías", kicker="Guía de Pinku",
    standfirst=("ChatGPT, Claude y Gemini necesitan conexión. Un modelo pequeño que funciona en el "
                "móvil, no. Así se prepara uno, y esto es lo que puedes esperar de él."),
    intro="""
<p><strong>Hacemos Pinku, la app que usa esta guía.</strong> La idea es la misma en
todas las apps de IA sin conexión: el modelo se descarga una vez y luego funciona en tu
dispositivo.</p>

<p>Los asistentes en la nube mandan cada mensaje a un servidor, así que dejan de
funcionar en un avión, en un túnel o donde no se ofrecen. Una app de IA sin conexión
guarda un modelo de lenguaje en el propio dispositivo. Necesitas internet una vez,
para descargarlo; después cada respuesta se genera en el iPhone y nada de lo que
escribes sale de él.</p>
""",
    steps=[
        ("Instala Pinku.",
         'Descarga <a href="%s">Pinku</a> del App Store. Funciona en iPhone, iPad y Mac con Apple '
         "silicon, en dispositivos compatibles con Metal 3. No hay cuenta." % PINKU_STORE),
        ("Descarga un modelo mientras tienes conexión.",
         "Hazlo con wifi antes de necesitarlo. El modelo por defecto, Gemma 3 1B, ocupa menos de 1 GB. Pinku "
         "solo te enseña los modelos que caben en la memoria de tu dispositivo."),
        ("Pon el modo avión y pruébalo.",
         "Abre el Centro de control, activa el modo avión y haz una pregunta. La respuesta se genera en "
         "el dispositivo, así que funciona sin ninguna conexión."),
        ("Elige el modelo adecuado.",
         "Los modelos pequeños responden más rápido; los grandes, mejor. Los seis de hasta 1 GB son "
         "gratis; Pinku Pro, una compra única, añade seis más grandes de hasta 4,7 GB."),
        ("Empieza un chat con Siri, si quieres.",
         "Pinku tiene una acción de Siri y Atajos para empezar un chat, que también funciona sin conexión."),
        ("Mueve un chat cuando lo necesites.",
         "Los chats se quedan en el dispositivo donde se escribieron; no hay sincronización. Comparte una "
         "conversación como texto para guardarla en otro sitio."),
    ],
    after="""
<h2>Qué esperar sin conexión</h2>

<p>Un modelo de 1 a 5 GB en un móvil es claramente más flojo que ChatGPT o Claude en
la nube. Sirve para redactar, reescribir, resumir un texto que pegas, explicar cosas
y sacar ideas. No busca en internet, no lee imágenes ni documentos, recuerda menos de
la conversación y su velocidad depende de tu dispositivo. Pinku comprueba la memoria
libre antes de cargar un modelo, así que si no cabe te avisa en lugar de cerrarse.</p>

<p>Pinku se descarga gratis, y los seis modelos de hasta 1 GB funcionan sin pagar.
Pinku Pro (9,99 $ en el App Store de EE. UU., una sola vez, sin suscripción) añade los
modelos grandes, instrucciones propias, dictado reconocido en el dispositivo y lectura
en voz alta. Más en <a href="../../pinku.html">la página de Pinku</a> (en inglés).</p>

<p>Otras apps de IA sin conexión, también donde nos ganan:
<a href="../../blog/es/mejores-apps-ia-sin-conexion-iphone-mac.html">las mejores apps de
IA sin conexión para iPhone y Mac</a>.</p>
""",
    faq=[
        ("¿Puedo usar IA en el iPhone sin internet?",
         "Sí, con una app que ejecute el modelo en el dispositivo, como Pinku. Necesitas conexión una vez "
         "para descargar el modelo; después responde en modo avión."),
        ("¿ChatGPT funciona sin conexión?",
         "No. ChatGPT funciona en los servidores de OpenAI, así que cada mensaje necesita conexión."),
        ("¿Cuánto ocupa un modelo de IA sin conexión?",
         "En Pinku, de 0,34 GB a 4,7 GB según el modelo. El de por defecto, Gemma 3 1B, ocupa menos de 1 GB."),
        ("¿Una IA sin conexión es tan buena como ChatGPT?",
         "No. Un modelo pequeño en un móvil es claramente más flojo, recuerda menos y no busca en internet. "
         "Su ventaja es que funciona en cualquier sitio y nada de lo que escribes sale del dispositivo."),
        ("¿Se mandan mis conversaciones a algún sitio?",
         "Con Pinku, no. No hay cuenta ni servidor; los chats se guardan en el dispositivo. La red solo se "
         "usa para descargar modelos y para las compras del App Store."),
    ],
)

# --------------------------------------------------------------------------
# Drop: ruido blanco para dormir en el iPhone
# --------------------------------------------------------------------------

DR_EN = dict(
    path="drop/white-noise-to-fall-asleep-iphone.html",
    app_name="Drop - Meditation & Focus",
    h1="How to use white noise to fall asleep on iPhone (Drop guide)",
    desc=("Step by step: pick a steady sound, keep it playing with the screen locked, stop it "
          "automatically with Drop's sleep timer, and add a few slow breaths before sleep. With Drop or "
          "with what is built into iOS. Written by Drop's maker."),
    section="Guides", kicker="Drop guide",
    standfirst=("A steady sound covers the noises that wake you: traffic, a neighbour, a dripping "
                "tap. This is how to set it up on an iPhone so it plays all night or stops on its own."),
    intro="""
<p><strong>We make Drop, the app this guide uses.</strong> Every step also works with
other sound apps, and the first option below is free and already on your iPhone.</p>

<p>White noise, rain or a fan do not make you sleep; what they do is mask sudden
sounds, so a car door or a voice in the corridor stands out less. Whether it helps you
is personal, and so is the sound: some people prefer rain or a fan to pure noise. If
you have ongoing trouble sleeping, talk to a doctor.</p>

<p>No app needed: iOS has <a href="%(bg)s" target="_blank" rel="noopener">Background
Sounds</a> (Settings, Accessibility, Audio &amp; Visual) with a few sounds such as noise,
rain, ocean and stream, and its own timer to stop them. If that is enough for you, use it.</p>
""" % dict(bg=BG_SOUNDS),
    steps=[
        ("Install Drop.",
         'Get <a href="%s">Drop</a> from the App Store. Ten sounds are free, with no ads and no account: '
         "rain, dewdrops, fire, forest, river, coffee shop, ocean waves, thunderstorm, bus and fan."
         % DROP_STORE),
        ("Pick one steady sound.",
         "Choose a sound without sudden changes. A fan, rain or the bus are steadier than birds or a "
         "storm. Try one for a few nights before switching."),
        ("Set the volume low.",
         "Turn it down until it just covers the room's noises. It should not be the loudest thing you "
         "hear, and lower is gentler on your ears over a whole night."),
        ("Lock the screen.",
         "Drop keeps playing with the screen locked, so the phone can stay dark on the nightstand."),
        ("Make it stop on its own, if you want.",
         "Tap Timer on the sound screen and pick 15, 30 or 45 minutes, 1, 2 or 8 hours. The sound fades "
         "out over the last 30 seconds and stops. Or choose no timer and leave it on all night. You can "
         'also use the Clock app (Timers, <a href="%s" target="_blank" rel="noopener">When Timer '
         'Ends</a>, Stop Playing).' % CLOCK_TIMER),
        ("Take a few slow breaths first.",
         "Before you start the sound, open Drop's breathing guide, set how long each breath lasts "
         "(2 to 8 seconds) and how many cycles, and follow the animation. Each session grows the plant "
         "in the app, which makes it easier to keep the habit."),
    ],
    after="""
<h2>What Drop does and does not do</h2>

<p>Drop has 32 nature, ambient and noise sounds, ten of them free, a breathing guide,
a plant that grows with each session, streaks, widgets and no ads. It works offline,
needs no account, and runs on iPhone, iPad and Mac. Drop Pro unlocks the other 22
sounds, by subscription or with a one-time lifetime purchase.</p>

<p>It has a sleep timer (15 minutes to 8 hours, with a 30-second fade-out), plays one sound at a time with no mixer, and
has no white, pink or brown noise generator: its noise sounds are a fan, a bus and an
electric hum. More on <a href="../drop.html">Drop's page</a>. If you want to mix sounds or fine-tune noise, other apps do it better,
and we say which in <a href="../blog/best-white-noise-sleep-sound-apps-iphone.html">the
best white noise and sleep sound apps for iPhone</a>.</p>
""",
    faq=[
        ("Does white noise help you fall asleep?",
         "It masks sudden noises such as traffic or voices, which some people find helps them fall and "
         "stay asleep. It does not work for everyone; try it for a few nights."),
        ("How do I make white noise stop automatically on iPhone?",
         "In Drop, tap Timer on the sound screen and pick 15, 30 or 45 minutes, 1, 2 or 8 hours; the sound "
         "fades out and stops. Without an app, use the Clock app: set a timer and choose When Timer Ends, "
         "Stop Playing."),
        ("Can I play white noise on iPhone without an app?",
         "Yes. Settings, Accessibility, Audio & Visual, Background Sounds plays a few built-in sounds such as "
         "noise, rain, ocean and stream, and can stop on its own with a timer."),
        ("Does Drop keep playing when the screen is locked?",
         "Yes. The sound keeps playing with the screen locked."),
        ("Is Drop free?",
         "It is free to download, with ten sounds free and no ads. Drop Pro unlocks the other 22 sounds by "
         "subscription or with a one-time lifetime purchase."),
    ],
)

DR_ES = dict(
    path="drop/es/ruido-blanco-para-dormir-iphone.html",
    app_name="Drop - Meditation & Focus",
    h1="Cómo usar ruido blanco para dormirte con el iPhone (guía de Drop)",
    desc=("Paso a paso: elige un sonido constante, déjalo sonando con la pantalla bloqueada, apágalo "
          "solo con el temporizador de Drop y haz unas respiraciones lentas antes de dormir. Con Drop "
          "o con lo que trae iOS. Escrito por quien hace Drop."),
    section="Guías", kicker="Guía de Drop",
    standfirst=("Un sonido constante tapa los ruidos que te despiertan: el tráfico, un vecino, un grifo "
                "que gotea. Así se prepara en el iPhone para que suene toda la noche o se apague solo."),
    intro="""
<p><strong>Hacemos Drop, la app que usa esta guía.</strong> Todos los pasos sirven
también con otras apps de sonidos, y la primera opción de abajo es gratis y ya está en
tu iPhone.</p>

<p>El ruido blanco, la lluvia o un ventilador no te hacen dormir; lo que hacen es tapar
los ruidos repentinos, para que un portazo o una voz en el pasillo destaquen menos. Si
te ayuda o no es algo personal, y el sonido también: hay quien prefiere lluvia o un
ventilador al ruido puro. Si te cuesta dormir a menudo, consulta a un médico.</p>

<p>Sin ninguna app: iOS tiene <a href="%(bg)s" target="_blank" rel="noopener">Sonidos de
fondo</a> (Ajustes, Accesibilidad, Audio y efectos visuales) con algunos sonidos como
ruido, lluvia, mar y arroyo, y su propio temporizador para apagarlos. Si con eso te basta, úsalo.</p>
""" % dict(bg=BG_SOUNDS_ES),
    steps=[
        ("Instala Drop.",
         'Descarga <a href="%s">Drop</a> del App Store. Diez sonidos son gratis, sin anuncios y sin '
         "cuenta: lluvia, gotas, fuego, bosque, río, cafetería, olas, tormenta, autobús y ventilador."
         % DROP_STORE),
        ("Elige un sonido constante.",
         "Busca un sonido sin cambios bruscos. Un ventilador, la lluvia o el autobús son más constantes "
         "que los pájaros o una tormenta. Prueba uno varias noches antes de cambiar."),
        ("Pon el volumen bajo.",
         "Bájalo hasta que justo tape los ruidos de la habitación. No debería ser lo que más se oye, y más "
         "bajo es más suave para tus oídos durante toda la noche."),
        ("Bloquea la pantalla.",
         "Drop sigue sonando con la pantalla bloqueada, así que el móvil puede quedarse a oscuras en la "
         "mesilla."),
        ("Haz que se apague solo, si quieres.",
         "Toca Temporizador en la pantalla del sonido y elige 15, 30 o 45 minutos, 1, 2 u 8 horas. El "
         "sonido baja poco a poco durante los últimos 30 segundos y se para. O no pongas temporizador y "
         'déjalo toda la noche. También puedes usar la app Reloj (Temporizador, <a href="%s" '
         'target="_blank" rel="noopener">Al finalizar</a>, Detener reproducción).' % CLOCK_TIMER_ES),
        ("Haz antes unas respiraciones lentas.",
         "Antes de poner el sonido, abre la guía de respiración de Drop, elige cuánto dura cada "
         "respiración (de 2 a 8 segundos) y cuántos ciclos, y sigue la animación. Cada sesión hace crecer "
         "la planta de la app, y así cuesta menos mantener el hábito."),
    ],
    after="""
<h2>Qué hace Drop y qué no</h2>

<p>Drop tiene 32 sonidos de naturaleza, ambiente y ruido, diez gratis, una guía de
respiración, una planta que crece con cada sesión, rachas, widgets y ningún anuncio.
Funciona sin conexión, no pide cuenta y va en iPhone, iPad y Mac. Drop Pro desbloquea
los otros 22 sonidos, por suscripción o con una compra de por vida.</p>

<p>Tiene temporizador (de 15 minutos a 8 horas, con fundido de 30 segundos), suena un sonido cada vez, sin mezclador, y no
genera ruido blanco, rosa ni marrón: sus sonidos de ruido son un ventilador, un autobús
y un zumbido eléctrico. Si quieres mezclar sonidos o afinar el ruido, otras apps lo
hacen mejor, y decimos cuáles en
<a href="../../blog/es/mejores-apps-ruido-blanco-sonidos-dormir-iphone.html">las mejores
apps de ruido blanco y sonidos para dormir en iPhone</a>.</p>
""",
    faq=[
        ("¿El ruido blanco ayuda a dormir?",
         "Tapa los ruidos repentinos, como el tráfico o las voces, y a algunas personas eso les ayuda a "
         "dormirse y a no despertarse. No le funciona a todo el mundo; pruébalo varias noches."),
        ("¿Cómo hago que el ruido blanco se apague solo en el iPhone?",
         "En Drop, toca Temporizador en la pantalla del sonido y elige 15, 30 o 45 minutos, 1, 2 u 8 horas; "
         "el sonido baja poco a poco y se para. Sin app, usa la app Reloj: pon un temporizador y elige Al "
         "finalizar, Detener reproducción."),
        ("¿Puedo poner ruido blanco en el iPhone sin una app?",
         "Sí. Ajustes, Accesibilidad, Audio y efectos visuales, Sonidos de fondo reproduce algunos sonidos "
         "de serie como ruido, lluvia, mar y arroyo, y puede apagarse sola con un temporizador."),
        ("¿Drop sigue sonando con la pantalla bloqueada?",
         "Sí. El sonido sigue con la pantalla bloqueada."),
        ("¿Drop es gratis?",
         "Se descarga gratis, con diez sonidos gratis y sin anuncios. Drop Pro desbloquea los otros 22 "
         "sonidos por suscripción o con una compra de por vida."),
    ],
)

GUIDES = [(PV_EN, PV_ES), (PK_EN, PK_ES), (DR_EN, DR_ES)]


def _alts(en, es):
    s = "https://aisagalab.com/"
    return ('    <link rel="alternate" hreflang="en" href="%s%s">\n'
            '    <link rel="alternate" hreflang="es" href="%s%s">\n'
            '    <link rel="alternate" hreflang="x-default" href="%s%s">' % (s, en, s, es, s, en))


def build(render):
    import os
    out = []
    byline = '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN
    for en, es in GUIDES:
        for lang, g, other in (("en", en, es), ("es", es, en)):
            rel = os.path.relpath(other["path"], os.path.dirname(g["path"]))
            label = "Leer en espa&ntilde;ol" if lang == "en" else "Read in English"
            body = (_head(g["kicker"], g["h1"], g["standfirst"], byline + DATE[lang], label, rel)
                    + '\n        <div class="article-body">' + g["intro"]
                    + _steps_html(g["steps"], "Step by step" if lang == "en" else "Paso a paso")
                    + g["after"]
                    + _faq_html(g["faq"], "Questions people ask" if lang == "en" else "Preguntas frecuentes")
                    + "</div>")
            out.append(render(path=g["path"], lang=lang, title=g["h1"] + " | Saga Labs",
                              desc=g["desc"], og_title=g["h1"], body=body,
                              jsonld=_ld(g, lang, g["path"]), alternates=_alts(en["path"], es["path"])))
    return out
