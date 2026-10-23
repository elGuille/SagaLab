# -*- coding: utf-8 -*-
"""Cuatro guias mas (23 oct 2026, noche), EN + ES, con la plantilla de guides.py.

Cada una lleva un dato de primera mano, comprobado el 23 oct 2026 y dicho en la pagina:
- Brainy (imagenes con IA): codigo de la 1.4.0 en venta (CreateView.swift: una foto de
  referencia, formatos 1:1, 9:16, 16:9, 2:3, 3:2, coste en creditos antes de crear, Pro para
  crear) y firebase/brainy/models.js desplegado (cinco opciones de imagen con nombres llanos).
  Valoraciones del App Store de EE. UU. leidas por la API de lookup. support.apple.com 121115
  (Image Playground con modelos en servidor y limites de uso, 22 oct 2026).
- 3 Tasks (procrastinar): Steel 2007 (PMID 17201571), Gollwitzer y Sheeran 2006 (Advances in
  Experimental Social Psychology 38, 94 pruebas, d = 0,65), Masicampo y Baumeister 2011 (PMID
  21688924). Codigo de la 1.3.0 (Reminders.swift: aviso de la manana, 9:00 por defecto).
- 3 Tasks (Pomodoro): guia de Apple de temporizadores (iph8241d6b2a) y Focus (iphd6288a67f);
  codigo de la 1.3.0 (limite por tarea de 15, 25, 45 o 60 min con aviso). El widget que arranca
  el tiempo y la frase de Siri son de la 1.4.0, que no esta a la venta: se dice que llegan.
- Pinku (IA local): codigo de la 1.1 en venta (ModelMemory.swift y OnboardingInstallModelView:
  60 % de la RAM para listar, memoria disponible + 10 % para cargar; models.json). Apple ML
  Research, 9 jun 2025 (modelo en el dispositivo de ~3B a 2 bits por peso).
De nuestras apps: sin precios y sin la palabra «free/gratis». Sin rayas.
"""

D = {"en": "23 October 2026", "es": "23 de octubre de 2026"}
ISO = "2026-10-23"

BRAINY_STORE = "https://apps.apple.com/app/apple-store/id1667947372?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
TT_STORE = "https://apps.apple.com/app/apple-store/id1553693943?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
PINKU_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


AI_FEATURES = "https://support.apple.com/en-us/121115"
AI_FEATURES_ES = "https://support.apple.com/es-es/121115"
IP_AS = "https://apps.apple.com/us/app/id6479176117"
CHATGPT_AS = "https://apps.apple.com/us/app/id6448311069"
GEMINI_AS = "https://apps.apple.com/us/app/id6477489729"
META_AS = "https://apps.apple.com/us/app/id1558240027"
GROK_AS = "https://apps.apple.com/us/app/id6670324846"
FIREFLY_AS = "https://apps.apple.com/us/app/id6742595426"

STEEL = "https://pubmed.ncbi.nlm.nih.gov/17201571/"
GOLLWITZER = "https://doi.org/10.1016/S0065-2601(06)38002-1"
MASICAMPO = "https://pubmed.ncbi.nlm.nih.gov/21688924/"

CLOCK_TIMER = "https://support.apple.com/guide/iphone/set-timers-iph8241d6b2a/ios"
CLOCK_TIMER_ES = "https://support.apple.com/es-es/guide/iphone/iph8241d6b2a/ios"
FOCUS = "https://support.apple.com/guide/iphone/set-up-a-focus-iphd6288a67f/ios"
FOCUS_ES = "https://support.apple.com/es-es/guide/iphone/iphd6288a67f/ios"
POMODORO = "https://www.pomodorotechnique.com/"
FOCUS_KEEPER_AS = "https://apps.apple.com/us/app/id867374917"
BE_FOCUSED_AS = "https://apps.apple.com/us/app/id973130201"
FOREST_AS = "https://apps.apple.com/us/app/id866450515"
FLOW_AS = "https://apps.apple.com/us/app/id1423210932"

APPLE_FM = "https://machinelearning.apple.com/research/apple-foundation-models-2025-updates"
MLX = "https://github.com/ml-explore/mlx"

# --------------------------------------------------------------------------
# Brainy: como crear imagenes con IA en el iPhone
# --------------------------------------------------------------------------

BR_EN = dict(
    path="brainy/how-to-make-ai-images-on-iphone.html",
    app_name="AI Homework Helper: Brainy",
    date_iso=ISO, date=D,
    h1="How to make AI images on iPhone: Image Playground and 6 apps compared (2026)",
    desc=("How to make an image with AI on an iPhone, step by step: Apple's Image Playground, and the ChatGPT, "
          "Gemini, Meta AI, Grok, Adobe Firefly and Brainy apps, with App Store ratings checked on 23 October 2026 "
          "and how to write a prompt that works."),
    section="Guides", kicker="Brainy guide",
    standfirst=("You do not need a computer or a design tool: describe the picture, pick a shape, and an AI model "
                "draws it in seconds. What changes from app to app is where it runs, what it limits and what it is good at."),
    tools=["Image Playground", "an AI chat app that makes images"],
    intro=f"""
<p><strong>We make Brainy, number five of the seven options on this page.</strong> Apple's own
app comes first because it is already on many iPhones.</p>

<h2>Seven ways to make an AI image on iPhone</h2>

<p>Ratings are from the US App Store, read on 23 October 2026.</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>What it does with images</th><th>Good to know</th><th>Rating</th></tr></thead>
<tbody>
<tr><td>{a(IP_AS, "Image Playground")} (Apple)</td><td>Images from a description, from your photos or from people in your library; tap or circle part of an image to change it; choose the aspect ratio</td><td>Needs an iPhone with Apple Intelligence; Apple says it uses server models with daily usage limits ({a(AI_FEATURES, "Apple, 121115")})</td><td>2.7 (about 5,000 ratings)</td></tr>
<tr><td>{a(CHATGPT_AS, "ChatGPT")}</td><td>Generates images from a description and transforms existing ones with words</td><td>Images live inside a general chat app</td><td>4.8 (11.5 million)</td></tr>
<tr><td>{a(GEMINI_AS, "Google Gemini")}</td><td>Generates and edits photos with Nano Banana 2: camera and lighting controls, mockups from several images, posters with sharp text</td><td>Google account</td><td>4.7 (2.4 million)</td></tr>
<tr><td>{a(META_AS, "Meta AI")}</td><td>Creates and edits images; edit a photo by sketching on it or asking for a change</td><td>Tied to Meta's apps and account</td><td>4.7 (282,000)</td></tr>
<tr><td><a href="{BRAINY_STORE}">Brainy</a></td><td>A Create tab for images and short videos, from words or from one photo, with five image options and five shapes</td><td>Creating needs Brainy Pro; cost in credits shown before you create</td><td>4.7 (3 ratings)</td></tr>
<tr><td>{a(GROK_AS, "Grok")}</td><td>Grok Imagine: images from text or voice, edits to existing images, photos turned into videos</td><td>X account</td><td>4.9 (1.5 million)</td></tr>
<tr><td>{a(FIREFLY_AS, "Adobe Firefly")}</td><td>Images and video from text, Generative Fill, background removal, a choice of resolutions and aspect ratios, partner models</td><td>Made for creative work; Adobe account</td><td>4.7 (10,900)</td></tr>
</tbody>
</table>
</div>

<h2>What we checked in Brainy's code</h2>

<p>We read the Create screen of the version on sale today (1.4.0) and the server list it loads.
You can add <strong>one reference photo</strong> or start from words only; choose between
<strong>five image options</strong>, named by what they are good at (Fast, Detailed, Best
quality, Text &amp; posters, Creative); and pick one of <strong>five shapes</strong>: 1:1, 9:16,
16:9, 2:3 or 3:2. The credit cost of each option is shown before you tap, and a Surprise Me
button writes an example prompt. Creating is part of Brainy Pro, and before the first image the
app asks your permission to send the prompt to the image provider.</p>
""",
    steps=[
        ("Pick where the image is made.",
         "Image Playground if your iPhone has Apple Intelligence and you want it built in; a chat app you already "
         "use (ChatGPT, Gemini, Meta AI, Grok) if you also want to talk the idea through; Firefly or Brainy if you "
         "want a screen made only for creating."),
        ("Describe the picture in one sentence.",
         "Subject, what it is doing, where, and the style: \"a golden retriever in a velvet cape, oil painting, "
         "museum lighting\". Concrete words beat adjectives like \"beautiful\"."),
        ("Choose the shape before you generate.",
         "Square (1:1) for a profile picture or post, tall (9:16) for a story or wallpaper, wide (16:9) for a "
         "slide or video thumbnail."),
        ("Start from a photo when likeness matters.",
         "For your pet, your product or your living room, add a photo as reference and say what to change. Only "
         "use photos of people who agree to it."),
        ("Change one thing at a time.",
         "If the result is close, ask for a single change (\"warmer light\", \"remove the text\") instead of "
         "rewriting the whole prompt."),
        ("For text in the image, say the exact words.",
         "Put the words in quotes and keep them short. Some models spell better than others; in Brainy that is "
         "the Text &amp; posters option."),
        ("Save it and check how you may use it.",
         "Save to Photos, then read the app's terms before using an image commercially, and label AI images as AI "
         "when you share them."),
    ],
    after=f"""
<h2>Which one to choose</h2>
<ul>
<li><strong>Image Playground</strong> is already there on iPhones with Apple Intelligence and works across Messages,
Keynote and Freeform. Its App Store rating is the lowest here, and Apple warns of daily limits.</li>
<li><strong>ChatGPT, Gemini, Meta AI and Grok</strong> are general assistants that also draw; useful if you already
use one of them every day.</li>
<li><strong>Adobe Firefly</strong> is the most complete for design work: fills, background removal and video.</li>
<li><strong>Brainy</strong> puts chat, homework help from a photo and image and video creation in one iPhone app,
with the cost of each image shown before you make it. It has very few ratings so far, it is iPhone only, and you
cannot make images without Brainy Pro. More on <a href="../brainy.html">the Brainy page</a> and in our comparison
of <a href="../blog/best-ai-chat-and-image-generator-apps-iphone.html">AI apps for chat and images</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
<li>App Store pages (descriptions and ratings, US store) of Image Playground, ChatGPT, Google Gemini, Meta AI, Grok, Adobe Firefly and Brainy, read 23 October 2026.</li>
<li>{a(AI_FEATURES, "Apple, Apple Intelligence features and requirements (121115)")}, published 22 October 2026.</li>
<li>Brainy 1.4.0 source code (Create screen) and its server model list, read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("How do I make an AI image on my iPhone?",
         "Open an app that makes images (Image Playground on iPhones with Apple Intelligence, or an app such as "
         "ChatGPT, Gemini, Meta AI, Grok, Adobe Firefly or Brainy), describe the picture, choose the shape and "
         "generate. Most can also start from one of your photos."),
        ("Does Image Playground run on the iPhone?",
         "Apple lists Image Playground among the Apple Intelligence features that rely on server models and have "
         "daily usage limits."),
        ("Which iPhones have Image Playground?",
         "iPhones with Apple Intelligence: iPhone 15 Pro and Pro Max, iPhone 16 and later, iPhone Air and iPhone "
         "Duo, according to Apple's list of 22 October 2026."),
        ("Can I turn my own photo into an AI image?",
         "Yes. Image Playground, ChatGPT, Gemini, Meta AI, Grok, Firefly and Brainy can all start from a photo and "
         "change it from a description."),
        ("How do I get readable text in an AI image?",
         "Write the exact words in quotes and keep them short. Gemini says its model designs posters with sharp "
         "text; in Brainy, pick the Text & posters option."),
        ("Does Brainy make images?",
         "Yes, in its Create tab, from words or one photo, with five image options and five shapes. Creating "
         "needs Brainy Pro."),
    ],
)

BR_ES = dict(
    path="brainy/es/como-crear-imagenes-con-ia-en-el-iphone.html",
    app_name="AI Homework Helper: Brainy",
    date_iso=ISO, date=D,
    h1="Cómo crear imágenes con IA en el iPhone: Image Playground y 6 apps comparadas (2026)",
    desc=("Cómo hacer una imagen con IA en el iPhone, paso a paso: Image Playground de Apple y las apps ChatGPT, "
          "Gemini, Meta AI, Grok, Adobe Firefly y Brainy, con las valoraciones del App Store del 23 de octubre de "
          "2026 y cómo escribir una descripción que funcione."),
    section="Guías", kicker="Guía de Brainy",
    standfirst=("No necesitas ordenador ni programa de diseño: describes la imagen, eliges el formato y un modelo de "
                "IA la dibuja en segundos. Lo que cambia de una app a otra es dónde se hace, qué límites tiene y en qué es buena."),
    tools=["Image Playground", "una app de IA que crea imágenes"],
    intro=f"""
<p><strong>Hacemos Brainy, la quinta de las siete opciones de esta página.</strong> La app de
Apple va primero porque ya está en muchos iPhone.</p>

<h2>Siete formas de crear una imagen con IA en el iPhone</h2>

<p>Valoraciones del App Store de EE. UU., leídas el 23 de octubre de 2026.</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Qué hace con imágenes</th><th>Conviene saber</th><th>Valoración</th></tr></thead>
<tbody>
<tr><td>{a(IP_AS, "Image Playground")} (Apple)</td><td>Imágenes a partir de una descripción, de tus fotos o de personas de tu fototeca; toca o rodea una parte para cambiarla; eliges el formato</td><td>Necesita un iPhone con Apple Intelligence; Apple dice que usa modelos en servidor con límites diarios ({a(AI_FEATURES_ES, "Apple, 121115")})</td><td>2,7 (unas 5.000)</td></tr>
<tr><td>{a(CHATGPT_AS, "ChatGPT")}</td><td>Genera imágenes a partir de una descripción y transforma las que ya tienes con palabras</td><td>Las imágenes van dentro de una app de chat general</td><td>4,8 (11,5 millones)</td></tr>
<tr><td>{a(GEMINI_AS, "Google Gemini")}</td><td>Genera y edita fotos con Nano Banana 2: controles de cámara y luz, montajes con varias imágenes, carteles con texto nítido</td><td>Cuenta de Google</td><td>4,7 (2,4 millones)</td></tr>
<tr><td>{a(META_AS, "Meta AI")}</td><td>Crea y edita imágenes; cambias una foto dibujando encima o pidiéndolo</td><td>Unida a las apps y la cuenta de Meta</td><td>4,7 (282.000)</td></tr>
<tr><td><a href="{BRAINY_STORE}">Brainy</a></td><td>Una pestaña Create para imágenes y vídeos cortos, desde palabras o desde una foto, con cinco opciones de imagen y cinco formatos</td><td>Crear necesita Brainy Pro; el coste en créditos sale antes de crear</td><td>4,7 (3 valoraciones)</td></tr>
<tr><td>{a(GROK_AS, "Grok")}</td><td>Grok Imagine: imágenes desde texto o voz, cambios en imágenes, fotos convertidas en vídeo</td><td>Cuenta de X</td><td>4,9 (1,5 millones)</td></tr>
<tr><td>{a(FIREFLY_AS, "Adobe Firefly")}</td><td>Imágenes y vídeo desde texto, Relleno generativo, quitar fondos, varias resoluciones y formatos, modelos de socios</td><td>Pensada para trabajo creativo; cuenta de Adobe</td><td>4,7 (10.900)</td></tr>
</tbody>
</table>
</div>

<h2>Lo que comprobamos en el código de Brainy</h2>

<p>Leímos la pantalla Create de la versión que está hoy a la venta (1.4.0) y la lista del
servidor que carga. Puedes añadir <strong>una foto de referencia</strong> o empezar solo con
palabras; elegir entre <strong>cinco opciones de imagen</strong>, con el nombre de lo que hacen
bien (Fast, Detailed, Best quality, Text &amp; posters, Creative), y uno de <strong>cinco
formatos</strong>: 1:1, 9:16, 16:9, 2:3 o 3:2. El coste en créditos de cada opción se ve antes de
tocar, y el botón Surprise Me escribe una descripción de ejemplo. Crear forma parte de Brainy
Pro, y antes de la primera imagen la app te pide permiso para mandar la descripción al proveedor
de imágenes. La app está en inglés.</p>
""",
    steps=[
        ("Elige dónde se hace la imagen.",
         "Image Playground si tu iPhone tiene Apple Intelligence y la quieres de serie; una app de chat que ya uses "
         "(ChatGPT, Gemini, Meta AI, Grok) si además quieres hablar la idea; Firefly o Brainy si quieres una "
         "pantalla solo para crear."),
        ("Describe la imagen en una frase.",
         "Qué sale, qué hace, dónde y en qué estilo: «un golden retriever con capa de terciopelo, óleo, luz de "
         "museo». Las palabras concretas funcionan mejor que «bonito»."),
        ("Elige el formato antes de generar.",
         "Cuadrado (1:1) para un perfil o una publicación, vertical (9:16) para una historia o un fondo de "
         "pantalla, horizontal (16:9) para una diapositiva o una miniatura."),
        ("Parte de una foto si importa el parecido.",
         "Para tu mascota, tu producto o tu salón, añade una foto de referencia y di qué cambiar. Usa solo fotos "
         "de personas que estén de acuerdo."),
        ("Cambia una cosa cada vez.",
         "Si el resultado se acerca, pide un solo cambio («luz más cálida», «quita el texto») en vez de reescribir "
         "toda la descripción."),
        ("Para texto en la imagen, escribe las palabras exactas.",
         "Ponlas entre comillas y que sean pocas. Unos modelos escriben mejor que otros; en Brainy es la opción "
         "Text &amp; posters."),
        ("Guárdala y mira cómo puedes usarla.",
         "Guárdala en Fotos, lee las condiciones de la app antes de usarla para un negocio y di que es de IA cuando "
         "la compartas."),
    ],
    after=f"""
<h2>Cuál elegir</h2>
<ul>
<li><strong>Image Playground</strong> ya está en los iPhone con Apple Intelligence y funciona en Mensajes, Keynote y
Freeform. Su valoración en el App Store es la más baja de la lista, y Apple avisa de límites diarios.</li>
<li><strong>ChatGPT, Gemini, Meta AI y Grok</strong> son asistentes generales que también dibujan; útiles si ya usas
uno a diario.</li>
<li><strong>Adobe Firefly</strong> es la más completa para diseño: rellenos, quitar fondos y vídeo.</li>
<li><strong>Brainy</strong> junta chat, ayuda con deberes desde una foto y creación de imágenes y vídeos en una app de
iPhone, con el coste de cada imagen a la vista antes de hacerla. Aún tiene muy pocas valoraciones, es solo para
iPhone y no se pueden hacer imágenes sin Brainy Pro. Más en <a href="../../brainy.html">la página de Brainy</a> (en
inglés) y en nuestra comparativa de <a href="../../blog/es/mejores-apps-ia-chat-e-imagenes-iphone.html">apps de IA
para chat e imágenes</a>.</li>
</ul>

<h2>Fuentes</h2>
<ul>
<li>Páginas del App Store (descripciones y valoraciones, tienda de EE. UU.) de Image Playground, ChatGPT, Google Gemini, Meta AI, Grok, Adobe Firefly y Brainy, leídas el 23 de octubre de 2026.</li>
<li>{a(AI_FEATURES_ES, "Apple, funciones y requisitos de Apple Intelligence (121115)")}, publicada el 22 de octubre de 2026.</li>
<li>Código de Brainy 1.4.0 (pantalla Create) y su lista de modelos del servidor, leídos el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Cómo creo una imagen con IA en el iPhone?",
         "Abre una app que haga imágenes (Image Playground en los iPhone con Apple Intelligence, o una app como "
         "ChatGPT, Gemini, Meta AI, Grok, Adobe Firefly o Brainy), describe la imagen, elige el formato y genera. "
         "Casi todas pueden partir también de una foto tuya."),
        ("¿Image Playground funciona en el propio iPhone?",
         "Apple pone Image Playground entre las funciones de Apple Intelligence que usan modelos en servidor y "
         "tienen límites diarios de uso."),
        ("¿Qué iPhone tienen Image Playground?",
         "Los que tienen Apple Intelligence: iPhone 15 Pro y Pro Max, iPhone 16 y posteriores, iPhone Air e "
         "iPhone Duo, según la lista de Apple del 22 de octubre de 2026."),
        ("¿Puedo convertir una foto mía en una imagen con IA?",
         "Sí. Image Playground, ChatGPT, Gemini, Meta AI, Grok, Firefly y Brainy pueden partir de una foto y "
         "cambiarla a partir de una descripción."),
        ("¿Cómo consigo texto legible en una imagen con IA?",
         "Escribe las palabras exactas entre comillas y que sean pocas. Gemini dice que su modelo hace carteles con "
         "texto nítido; en Brainy, elige la opción Text & posters."),
        ("¿Brainy crea imágenes?",
         "Sí, en su pestaña Create, desde palabras o desde una foto, con cinco opciones de imagen y cinco "
         "formatos. Crear necesita Brainy Pro."),
    ],
)

# --------------------------------------------------------------------------
# 3 Tasks: dejar de procrastinar con una lista de 3 tareas
# --------------------------------------------------------------------------

TT2_EN = dict(
    path="3-tasks/stop-procrastinating-with-a-3-task-list.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D,
    h1="How to stop procrastinating with a 3-task list (what the research says, 2026)",
    desc=("A short list plus an if-then plan for each item: what studies on procrastination (Steel 2007) and "
          "implementation intentions (Gollwitzer and Sheeran 2006, 94 tests) found, and how to turn that into a "
          "3-task list on paper or on iPhone."),
    section="Guides", kicker="3 Tasks guide",
    standfirst=("A long list makes it easy to pick the pleasant task and leave the hard one. Three items, each with a "
                "time and a first step, leaves less room to hide."),
    tools=["paper or a to-do app", "Clock or a timer", "3 Tasks"],
    intro=f"""
<p><strong>We make 3 Tasks, one of the ways to keep a 3-task list described here.</strong> Paper
works just as well for the method; the research below is about planning, not about any app.</p>

<h2>What the research says</h2>

<ul>
<li><strong>What predicts putting things off.</strong> Piers Steel's meta-analysis of 691
correlations ({a(STEEL, "Psychological Bulletin, 2007")}) found the strongest, most consistent
predictors were how unpleasant the task feels, how far away its reward or deadline is, low
confidence that you can do it, and impulsiveness.</li>
<li><strong>If-then plans help people act.</strong> Gollwitzer and Sheeran's meta-analysis of 94
independent tests ({a(GOLLWITZER, "Advances in Experimental Social Psychology, 2006")}) found that
plans of the form <em>"when situation X happens, I will do Y"</em>, called implementation
intentions, had a medium-to-large effect on reaching goals (d = 0.65) compared with intentions alone.</li>
<li><strong>A plan quiets the open loop.</strong> In Masicampo and Baumeister's experiments
({a(MASICAMPO, "Journal of Personality and Social Psychology, 2011")}), unfinished goals caused
intrusive thoughts during other work; letting people write a specific plan for them removed that
interference.</li>
</ul>

<p>What no study shows is that <em>three</em> is a magic number. Ivy Lee's 1918 method used six
items, and the "Rule of 3" is a rule of thumb (we cover both in
<a href="3-task-method-ivy-lee-rule-of-3.html">the 3-task method</a>). The short list matters
because it forces a choice; the if-then plan is what the evidence is about.</p>

<p>This page is about everyday procrastination. If putting things off is hurting your work,
studies or health, talk to a professional.</p>

<h2>What we checked in 3 Tasks' code</h2>

<p>We read the reminder code of the version on sale today (1.3.0). Its morning reminder, off until
you turn it on, fires at a time you choose (9:00 unless you change it) with the title "Your 3 tasks
for today" and the question "What are the 3 things that matter most today?". In the terms of the
research, that fixed time is the "when" of the plan. Each task can also get a time limit of 15,
25, 45 or 60 minutes that sends a notification when it is reached, even with the app closed.</p>
""",
    steps=[
        ("Pick the time you will choose.",
         "Same time every day, linked to something you already do: \"after the first coffee\" or \"when I sit "
         "down at my desk\". A reminder at that time helps."),
        ("Write three tasks, not more.",
         "Ask what would make today count if only three things got done. Everything else goes on a separate list "
         "for later."),
        ("Put the one you are avoiding first.",
         "Steel's review links procrastination to unpleasant tasks; doing that one before the easy two stops it "
         "sliding to tomorrow."),
        ("Make each task a first physical step.",
         "\"Open the report and write the first paragraph\", not \"report\". Low confidence predicts delay; a "
         "small first step is one you know you can do."),
        ("Add an if-then plan to each.",
         "\"When it is 9:30, I will call the bank.\" \"If I open social media, I will close it and start the "
         "timer.\" Write the situation and the action."),
        ("Start a timer and work on one task only.",
         "A timer makes the start concrete. Stop when it ends or when the task is done, whichever comes first."),
        ("Write tomorrow's three before you stop.",
         "Masicampo and Baumeister found that writing a specific plan for an unfinished goal reduced intrusive "
         "thoughts about it. Unfinished tasks move to tomorrow's list or get dropped."),
    ],
    after=f"""
<h2>Ways to keep the list</h2>
<ul>
<li><strong>Paper or a sticky note</strong>: nothing to install, nothing to distract you.</li>
<li><strong>Reminders or Notes on iPhone</strong>: make a list called Today and keep it to three items yourself.</li>
<li><strong>A general to-do app</strong> such as Todoist or Things, with a "today" filter you limit by hand.</li>
<li><strong><a href="{TT_STORE}">3 Tasks</a></strong>: built around exactly three tasks a day, with a start/pause
timer on each that keeps counting with the screen locked, the optional time limit and morning reminder above,
Repeat Daily, and a Home Screen widget that shows the three. It has no subtasks, projects or due dates, and no
way to add a fourth task; if you need those, a general to-do app fits better. More on
<a href="../3things.html">the 3 Tasks page</a>.</li>
</ul>

<p>We compared apps built around three tasks in
<a href="../blog/best-3-task-todo-apps-iphone.html">the best 3-task to-do apps for iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(STEEL, "Steel P. The nature of procrastination: a meta-analytic and theoretical review. Psychological Bulletin 2007;133(1):65-94")}.</li>
<li>{a(GOLLWITZER, "Gollwitzer PM, Sheeran P. Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 2006;38:69-119")}.</li>
<li>{a(MASICAMPO, "Masicampo EJ, Baumeister RF. Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals. J Pers Soc Psychol 2011;101(4):667-83")}.</li>
<li>3 Tasks 1.3.0 source code (reminders), read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Does a 3-task list really help with procrastination?",
         "No study tests the number three. What the research supports is planning: specific if-then plans had a "
         "medium-to-large effect on reaching goals in a meta-analysis of 94 tests. A short list makes those plans "
         "easy to write."),
        ("What is an implementation intention?",
         "A plan of the form \"when situation X happens, I will do Y\", for example \"when I sit down after lunch, "
         "I will write the first paragraph\". Gollwitzer and Sheeran's 2006 meta-analysis found it works better "
         "than a goal alone."),
        ("Why do I put off some tasks and not others?",
         "Steel's 2007 meta-analysis found task aversiveness, a distant reward or deadline, low confidence and "
         "impulsiveness to be the strongest predictors."),
        ("Which task should go first?",
         "The one you are most likely to avoid, broken down to its first physical step."),
        ("Can 3 Tasks remind me to pick my three tasks?",
         "Yes. Its morning reminder fires at a time you choose, 9:00 by default, once you turn it on."),
    ],
)

TT2_ES = dict(
    path="3-tasks/es/dejar-de-procrastinar-con-una-lista-de-3-tareas.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D,
    h1="Cómo dejar de procrastinar con una lista de 3 tareas (lo que dicen los estudios, 2026)",
    desc=("Una lista corta y un plan «si pasa X, hago Y» para cada tarea: lo que encontraron los estudios sobre la "
          "procrastinación (Steel 2007) y las intenciones de implementación (Gollwitzer y Sheeran 2006, 94 pruebas), "
          "y cómo llevarlo a una lista de 3 tareas en papel o en el iPhone."),
    section="Guías", kicker="Guía de 3 Tasks",
    standfirst=("Con una lista larga es fácil elegir la tarea agradable y dejar la difícil. Con tres, cada una con su "
                "hora y su primer paso, queda menos sitio donde esconderse."),
    tools=["papel o una app de tareas", "Reloj o un temporizador", "3 Tasks"],
    intro=f"""
<p><strong>Hacemos 3 Tasks, una de las formas de llevar una lista de 3 tareas que salen
aquí.</strong> Para el método vale igual el papel; los estudios de abajo hablan de planificar,
no de ninguna app.</p>

<h2>Lo que dicen los estudios</h2>

<ul>
<li><strong>Qué hace que dejemos las cosas para luego.</strong> El metaanálisis de Piers Steel con
691 correlaciones ({a(STEEL, "Psychological Bulletin, 2007")}) encontró que lo que más y con más
constancia lo predice es lo desagradable que resulta la tarea, lo lejos que queda su recompensa o
su plazo, la poca confianza en poder hacerla y la impulsividad.</li>
<li><strong>Los planes «si... entonces» ayudan a actuar.</strong> El metaanálisis de Gollwitzer y
Sheeran con 94 pruebas independientes ({a(GOLLWITZER, "Advances in Experimental Social Psychology, 2006")})
encontró que los planes del tipo <em>«cuando pase X, haré Y»</em>, llamados intenciones de
implementación, tenían un efecto de medio a grande en conseguir objetivos (d = 0,65) frente a solo
proponérselo.</li>
<li><strong>Un plan calma lo pendiente.</strong> En los experimentos de Masicampo y Baumeister
({a(MASICAMPO, "Journal of Personality and Social Psychology, 2011")}), los objetivos sin terminar
provocaban pensamientos intrusivos durante otro trabajo; dejar que la gente escribiera un plan
concreto para ellos quitaba esa interferencia.</li>
</ul>

<p>Lo que ningún estudio dice es que <em>tres</em> sea un número mágico. El método de Ivy Lee de
1918 usaba seis, y la «regla de 3» es una costumbre (las dos están en
<a href="metodo-de-3-tareas-ivy-lee-regla-de-3.html">el método de 3 tareas</a>). La lista corta
sirve porque obliga a elegir; el plan «si... entonces» es lo que tiene pruebas detrás.</p>

<p>Esta página trata de la procrastinación de todos los días. Si dejar las cosas para luego te
está afectando al trabajo, a los estudios o a la salud, habla con un profesional.</p>

<h2>Lo que comprobamos en el código de 3 Tasks</h2>

<p>Leímos el código de avisos de la versión que está hoy a la venta (1.3.0). Su aviso de la
mañana, apagado hasta que lo activas, sale a la hora que elijas (las 9:00 si no la cambias) con el
título «Your 3 tasks for today» y la pregunta «What are the 3 things that matter most today?» (la
app está en inglés). En el lenguaje de los estudios, esa hora fija es el «cuándo» del plan. Cada
tarea puede llevar además un tiempo límite de 15, 25, 45 o 60 minutos que avisa al llegar, aunque
la app esté cerrada.</p>
""",
    steps=[
        ("Fija la hora a la que eliges.",
         "La misma cada día y unida a algo que ya haces: «después del primer café» o «al sentarme a la mesa». Un "
         "aviso a esa hora ayuda."),
        ("Escribe tres tareas, no más.",
         "Pregúntate qué haría que hoy valiera la pena si solo salieran tres cosas. Lo demás va a otra lista para "
         "más adelante."),
        ("Pon primero la que estás evitando.",
         "La revisión de Steel relaciona la procrastinación con las tareas desagradables; hacer esa antes que las "
         "dos fáciles evita que pase a mañana."),
        ("Convierte cada tarea en un primer paso físico.",
         "«Abrir el informe y escribir el primer párrafo», no «informe». La poca confianza predice el retraso; un "
         "primer paso pequeño es uno que sabes que puedes hacer."),
        ("Añade un plan «si... entonces» a cada una.",
         "«Cuando sean las 9:30, llamo al banco.» «Si abro las redes, las cierro y pongo el temporizador.» Escribe "
         "la situación y la acción."),
        ("Pon un temporizador y trabaja en una sola tarea.",
         "Un temporizador hace concreto el empezar. Para cuando acabe o cuando termines la tarea, lo que llegue antes."),
        ("Escribe las tres de mañana antes de parar.",
         "Masicampo y Baumeister vieron que escribir un plan concreto para un objetivo sin terminar reducía los "
         "pensamientos intrusivos sobre él. Lo que no acabaste pasa a la lista de mañana o se tacha."),
    ],
    after=f"""
<h2>Formas de llevar la lista</h2>
<ul>
<li><strong>Papel o una nota adhesiva</strong>: nada que instalar, nada que te distraiga.</li>
<li><strong>Recordatorios o Notas del iPhone</strong>: una lista llamada Hoy y el límite de tres lo pones tú.</li>
<li><strong>Una app de tareas general</strong> como Todoist o Things, con un filtro de «hoy» que limitas a mano.</li>
<li><strong><a href="{TT_STORE}">3 Tasks</a></strong>: hecha para tres tareas al día, con un temporizador de iniciar y
pausar en cada una que sigue contando con la pantalla bloqueada, el tiempo límite y el aviso de la mañana de
arriba, Repeat Daily y un widget de pantalla de inicio que enseña las tres. No tiene subtareas, proyectos ni fechas
de vencimiento, y no deja añadir una cuarta tarea; si necesitas eso, encaja mejor una app de tareas general. Más
en <a href="../../3things.html">la página de 3 Tasks</a> (en inglés).</li>
</ul>

<p>Comparamos las apps de tres tareas en
<a href="../../blog/es/mejores-apps-3-tareas-al-dia-iphone.html">las mejores apps de 3 tareas al día para iPhone</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(STEEL, "Steel P. The nature of procrastination: a meta-analytic and theoretical review. Psychological Bulletin 2007;133(1):65-94")}.</li>
<li>{a(GOLLWITZER, "Gollwitzer PM, Sheeran P. Implementation intentions and goal achievement: a meta-analysis of effects and processes. Advances in Experimental Social Psychology 2006;38:69-119")}.</li>
<li>{a(MASICAMPO, "Masicampo EJ, Baumeister RF. Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals. J Pers Soc Psychol 2011;101(4):667-83")}.</li>
<li>Código de 3 Tasks 1.3.0 (avisos), leído el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Una lista de 3 tareas ayuda de verdad a no procrastinar?",
         "Ningún estudio prueba el número tres. Lo que tiene apoyo es planificar: los planes concretos «si... "
         "entonces» tuvieron un efecto de medio a grande en un metaanálisis de 94 pruebas. Una lista corta hace "
         "fácil escribirlos."),
        ("¿Qué es una intención de implementación?",
         "Un plan del tipo «cuando pase X, haré Y», por ejemplo «cuando me siente después de comer, escribo el "
         "primer párrafo». El metaanálisis de Gollwitzer y Sheeran de 2006 vio que funciona mejor que solo el objetivo."),
        ("¿Por qué dejo para luego unas tareas y otras no?",
         "El metaanálisis de Steel de 2007 encontró como predictores más fuertes lo desagradable de la tarea, una "
         "recompensa o un plazo lejanos, la poca confianza y la impulsividad."),
        ("¿Qué tarea va primero?",
         "La que más probablemente vas a evitar, reducida a su primer paso físico."),
        ("¿3 Tasks me recuerda elegir mis tres tareas?",
         "Sí. Su aviso de la mañana sale a la hora que elijas, las 9:00 por defecto, cuando lo activas."),
    ],
)

# --------------------------------------------------------------------------
# 3 Tasks: temporizador Pomodoro en el iPhone
# --------------------------------------------------------------------------

TT3_EN = dict(
    path="3-tasks/pomodoro-timer-on-iphone.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D,
    h1="Pomodoro timer on iPhone: how to do it with the Clock app, Focus or an app (2026)",
    desc=("How to run Pomodoro sessions on an iPhone: a 25-minute timer in Clock with Siri, presets and multiple "
          "timers, a Focus to silence notifications, and apps such as Focus Keeper, Be Focused, Forest, Flow and 3 "
          "Tasks. Checked against Apple's guide on 23 October 2026."),
    section="Guides", kicker="3 Tasks guide",
    standfirst=("You do not need an app for Pomodoro: your iPhone's Clock and Focus already do the two things it needs. "
                "An app helps when you want the timer tied to the task, or a record of the time."),
    tools=["Clock app", "Focus", "a Pomodoro or task timer app"],
    intro=f"""
<p><strong>We make 3 Tasks, one of the apps on this page.</strong> The built-in way comes first
and is enough for many people.</p>

<h2>Pomodoro in one paragraph</h2>

<p>Francesco Cirillo created the {a(POMODORO, "Pomodoro Technique")} in the 1980s. In its usual
form you work on one task for 25 minutes, take a short break of about 5 minutes, and take a longer
break after four rounds. His own site stresses that it is more than a timer: you choose the day's
work first, handle interruptions and look back at how long things took.</p>

<h2>What the iPhone already does (Apple's guide, read 23 October 2026)</h2>

<ul>
<li><strong>Timer in Clock.</strong> Set a duration, give it a label such as "Pomodoro" and pick the
sound for when it ends. "The timer continues even if you open another app or if iPhone goes to
sleep." A custom timer then appears under Recent, so the next 25 minutes is one tap
({a(CLOCK_TIMER, "Apple")}).</li>
<li><strong>Several timers at once.</strong> After starting one you can add more, from presets or
recent ones, so a 25-minute work timer and a 5-minute break timer can sit side by side.</li>
<li><strong>Siri.</strong> "Set the timer for 25 minutes."</li>
<li><strong>Lock Screen.</strong> When a timer ends you get a notification and can tap Repeat or
Stop from the Lock Screen.</li>
<li><strong>Focus.</strong> A Focus such as Work silences all notifications or lets only some
people and apps through, and can turn on automatically at a set time, place or "while using a
certain app" ({a(FOCUS, "Apple")}).</li>
</ul>

<h2>What we checked in 3 Tasks' code</h2>

<p>We read the timer and reminder code of the version on sale today (1.3.0). Each of the three
tasks has a start/pause timer that counts up and keeps counting in the background. You can give a
task a <strong>time limit of 15, 25, 45 or 60 minutes</strong>: a ring fills towards it, and when
it is reached a notification says "Time's up" with the task's name, even with the app closed.
There is no break timer: for the 5-minute break, use Clock. Starting a task's timer straight from
the Home Screen widget is coming in the next version; today the widget shows your
three tasks and the timer starts in the app.</p>
""",
    steps=[
        ("Choose the task first.",
         "Pomodoro works on one task at a time. Write it down, or pick one of your three for the day."),
        ("Turn on a Focus.",
         "Control Center, Focus, then Do Not Disturb or Work. In Settings, Focus, you can make Work turn on by "
         "itself when you open the app you work in."),
        ("Start a 25-minute timer.",
         "Clock, Timers, 25 minutes, label it \"Pomodoro\", Start; or say \"Set the timer for 25 minutes\". In 3 "
         "Tasks, set the task's limit to 25 min and tap the task."),
        ("Work only on that task until it rings.",
         "If something else comes up, note it on paper and return to the task."),
        ("Take a 5-minute break.",
         "Start a 5-minute timer from Presets or Recent in Clock. Stand up, look away from the screen."),
        ("After four rounds, take a longer break.",
         "Fifteen to thirty minutes is the usual range."),
        ("Look at the time you actually spent.",
         "Compare it with your guess. Apps that keep a history make this easier; on paper, a tick per round is enough."),
    ],
    after=f"""
<h2>Apps for Pomodoro on iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>What it does</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Clock + Focus (built in)</td><td>Countdown timers, presets, several at once, Siri; Focus silences notifications</td><td>Anyone who wants nothing new on the phone</td></tr>
<tr><td>{a(FOCUS_KEEPER_AS, "Focus Keeper")}</td><td>A dedicated Pomodoro timer with work and break rounds</td><td>Classic Pomodoro with breaks counted for you</td></tr>
<tr><td>{a(BE_FOCUSED_AS, "Be Focused")}</td><td>Tasks split into intervals separated by short breaks, configurable</td><td>Pomodoro rounds attached to a task list</td></tr>
<tr><td>{a(FOREST_AS, "Forest")}</td><td>A tree grows while you stay off your phone and withers if you leave early</td><td>People whose problem is picking up the phone</td></tr>
<tr><td>{a(FLOW_AS, "Flow")}</td><td>A small focus and Pomodoro timer that divides work into sessions</td><td>A simple timer on iPhone and Mac</td></tr>
<tr><td><a href="{TT_STORE}">3 Tasks</a></td><td>Three tasks a day, a timer on each that counts up, optional 15/25/45/60 min limit with a notification, Home Screen widget with the three tasks</td><td>Timing the few tasks that matter today, without a break timer</td></tr>
</tbody>
</table>
</div>

<p>If you want breaks counted for you, a dedicated Pomodoro app does it; 3 Tasks does not. If you
want to know how long each of today's tasks really took, 3 Tasks keeps the time per task, and 3
Tasks Pro adds a history of it. More on <a href="../3things.html">the 3 Tasks page</a> and in
<a href="stop-procrastinating-with-a-3-task-list.html">how to stop procrastinating with a 3-task list</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(CLOCK_TIMER, "Apple, Set timers in Clock on iPhone")} and {a(FOCUS, "Set up a Focus on iPhone")}, iPhone User Guide, read 23 October 2026.</li>
<li>{a(POMODORO, "pomodorotechnique.com")} (Francesco Cirillo), read 23 October 2026.</li>
<li>App Store pages of Focus Keeper, Be Focused, Forest and Flow (US store), read 23 October 2026.</li>
<li>3 Tasks 1.3.0 source code (timer and reminders), read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Does the iPhone have a Pomodoro timer?",
         "Not by that name, but the Clock app's Timer does the job: set 25 minutes, label it, and start it again "
         "from Recent. You can run a work timer and a break timer at the same time."),
        ("Does the iPhone timer keep running if I lock the phone?",
         "Yes. Apple says the timer continues if you open another app or iPhone goes to sleep, and you can Repeat "
         "or Stop it from the Lock Screen."),
        ("How long is a Pomodoro?",
         "Usually 25 minutes of work and a short break of about 5 minutes, with a longer break after four rounds."),
        ("How do I block distractions during a Pomodoro?",
         "Turn on a Focus such as Do Not Disturb or Work. A Focus can also turn on by itself when you open a "
         "certain app."),
        ("Can 3 Tasks do Pomodoro?",
         "It times each task and can notify you after 15, 25, 45 or 60 minutes, but it has no break timer. Use "
         "Clock for the breaks, or a dedicated Pomodoro app if you want breaks counted for you."),
        ("Can I start the 3 Tasks timer from the widget?",
         "Not yet. Today the widget shows your three tasks; starting a task's timer from the widget "
         "comes in the next version."),
    ],
)

TT3_ES = dict(
    path="3-tasks/es/temporizador-pomodoro-en-el-iphone.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D,
    h1="Temporizador Pomodoro en el iPhone: cómo hacerlo con Reloj, Concentración o una app (2026)",
    desc=("Cómo hacer Pomodoro en el iPhone: un temporizador de 25 minutos en Reloj con Siri, predefinidos y varios "
          "a la vez, un modo Concentración para silenciar avisos, y apps como Focus Keeper, Be Focused, Forest, Flow "
          "y 3 Tasks. Comprobado con la guía de Apple el 23 de octubre de 2026."),
    section="Guías", kicker="Guía de 3 Tasks",
    standfirst=("No hace falta una app para hacer Pomodoro: Reloj y Concentración ya hacen las dos cosas que necesita. "
                "Una app ayuda si quieres el tiempo unido a la tarea o un registro de cuánto tardaste."),
    tools=["app Reloj", "Concentración", "una app de Pomodoro o de tareas con temporizador"],
    intro=f"""
<p><strong>Hacemos 3 Tasks, una de las apps de esta página.</strong> La forma que trae el iPhone
va primero y a mucha gente le basta.</p>

<h2>Pomodoro en un párrafo</h2>

<p>Francesco Cirillo creó la {a(POMODORO, "técnica Pomodoro")} en los años ochenta. En su forma
habitual trabajas en una sola tarea 25 minutos, descansas unos 5 y, tras cuatro rondas, haces un
descanso más largo. Su web insiste en que es más que un temporizador: eliges antes el trabajo del
día, apuntas las interrupciones y miras después cuánto te llevó cada cosa.</p>

<h2>Lo que ya hace el iPhone (guía de Apple, leída el 23 de octubre de 2026)</h2>

<ul>
<li><strong>Temporizador en Reloj.</strong> Pones una duración, una etiqueta como «Pomodoro» y el
sonido del final. El temporizador sigue aunque abras otra app o el iPhone entre en reposo. Después
aparece en Recientes, así que los siguientes 25 minutos están a un toque ({a(CLOCK_TIMER_ES, "Apple")}).</li>
<li><strong>Varios a la vez.</strong> Con uno en marcha puedes añadir otros, predefinidos o
recientes: uno de 25 minutos para trabajar y otro de 5 para el descanso.</li>
<li><strong>Siri.</strong> «Pon el temporizador en 25 minutos.»</li>
<li><strong>Pantalla bloqueada.</strong> Al terminar llega un aviso y puedes tocar Repetir o
Detener desde la pantalla bloqueada.</li>
<li><strong>Concentración.</strong> Un modo como Trabajo silencia todos los avisos o deja pasar
solo a algunas personas y apps, y puede activarse solo a una hora, en un lugar o al usar una app
concreta ({a(FOCUS_ES, "Apple")}).</li>
</ul>

<h2>Lo que comprobamos en el código de 3 Tasks</h2>

<p>Leímos el código del temporizador y de los avisos de la versión que está hoy a la venta
(1.3.0). Cada una de las tres tareas tiene un temporizador de iniciar y pausar que cuenta hacia
arriba y sigue contando en segundo plano. Puedes darle a una tarea un <strong>tiempo límite de 15,
25, 45 o 60 minutos</strong>: un anillo se va llenando y, al llegar, un aviso dice «Time's up» con
el nombre de la tarea, aunque la app esté cerrada. No hay temporizador de descanso: para los 5
minutos, usa Reloj. Arrancar el tiempo de una tarea desde el widget de la pantalla de inicio
llega en la próxima versión; hoy el widget enseña tus tres tareas y el tiempo se arranca
en la app.</p>
""",
    steps=[
        ("Elige antes la tarea.",
         "Pomodoro funciona con una tarea cada vez. Apúntala, o escoge una de tus tres del día."),
        ("Activa un modo Concentración.",
         "Centro de control, Concentración, y No molestar o Trabajo. En Ajustes, Concentración, puedes hacer que "
         "Trabajo se active solo al abrir la app con la que trabajas."),
        ("Pon un temporizador de 25 minutos.",
         "Reloj, Temporizadores, 25 minutos, etiqueta «Pomodoro», Iniciar; o dile a Siri «Pon el temporizador en 25 "
         "minutos». En 3 Tasks, pon el límite de la tarea en 25 min y tócala."),
        ("Trabaja solo en esa tarea hasta que suene.",
         "Si surge otra cosa, apúntala en un papel y vuelve a la tarea."),
        ("Descansa 5 minutos.",
         "Arranca uno de 5 minutos desde Predefinidos o Recientes en Reloj. Levántate y aparta la vista de la pantalla."),
        ("Tras cuatro rondas, un descanso largo.",
         "Lo habitual es de quince a treinta minutos."),
        ("Mira el tiempo que de verdad te llevó.",
         "Compáralo con lo que pensabas. Las apps con historial lo facilitan; en papel basta una marca por ronda."),
    ],
    after=f"""
<h2>Apps para hacer Pomodoro en el iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Qué hace</th><th>Para quién</th></tr></thead>
<tbody>
<tr><td>Reloj + Concentración (de serie)</td><td>Temporizadores, predefinidos, varios a la vez, Siri; Concentración silencia avisos</td><td>Quien no quiere instalar nada</td></tr>
<tr><td>{a(FOCUS_KEEPER_AS, "Focus Keeper")}</td><td>Un temporizador Pomodoro con rondas de trabajo y descanso</td><td>Pomodoro clásico con los descansos contados por la app</td></tr>
<tr><td>{a(BE_FOCUSED_AS, "Be Focused")}</td><td>Tareas divididas en intervalos con descansos cortos, configurables</td><td>Rondas Pomodoro unidas a una lista de tareas</td></tr>
<tr><td>{a(FOREST_AS, "Forest")}</td><td>Un árbol crece mientras no tocas el móvil y se seca si sales antes</td><td>Quien se distrae cogiendo el teléfono</td></tr>
<tr><td>{a(FLOW_AS, "Flow")}</td><td>Un temporizador pequeño de concentración y Pomodoro que divide el trabajo en sesiones</td><td>Un temporizador sencillo en iPhone y Mac</td></tr>
<tr><td><a href="{TT_STORE}">3 Tasks</a></td><td>Tres tareas al día, un temporizador en cada una que cuenta hacia arriba, límite opcional de 15/25/45/60 min con aviso, widget con las tres tareas</td><td>Medir el tiempo de las pocas tareas que importan hoy, sin temporizador de descanso</td></tr>
</tbody>
</table>
</div>

<p>Si quieres que la app cuente los descansos, una app de Pomodoro lo hace; 3 Tasks no. Si quieres
saber cuánto te llevó de verdad cada tarea del día, 3 Tasks guarda el tiempo de cada una, y 3 Tasks
Pro añade el historial. Más en <a href="../../3things.html">la página de 3 Tasks</a> (en inglés) y en
<a href="dejar-de-procrastinar-con-una-lista-de-3-tareas.html">cómo dejar de procrastinar con una lista
de 3 tareas</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(CLOCK_TIMER_ES, "Apple, Configurar temporizadores en Reloj del iPhone")} y {a(FOCUS_ES, "Configurar un modo de concentración en el iPhone")}, Manual del usuario del iPhone, leídos el 23 de octubre de 2026.</li>
<li>{a(POMODORO, "pomodorotechnique.com")} (Francesco Cirillo), leída el 23 de octubre de 2026.</li>
<li>Páginas del App Store de Focus Keeper, Be Focused, Forest y Flow (tienda de EE. UU.), leídas el 23 de octubre de 2026.</li>
<li>Código de 3 Tasks 1.3.0 (temporizador y avisos), leído el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿El iPhone tiene temporizador Pomodoro?",
         "No con ese nombre, pero el Temporizador de Reloj sirve: pones 25 minutos, le das una etiqueta y lo vuelves "
         "a arrancar desde Recientes. Puedes tener a la vez uno de trabajo y otro de descanso."),
        ("¿El temporizador sigue si bloqueo el iPhone?",
         "Sí. Apple dice que sigue aunque abras otra app o el iPhone entre en reposo, y puedes Repetir o Detener "
         "desde la pantalla bloqueada."),
        ("¿Cuánto dura un Pomodoro?",
         "Lo habitual son 25 minutos de trabajo y un descanso corto de unos 5, con uno más largo tras cuatro rondas."),
        ("¿Cómo bloqueo distracciones durante un Pomodoro?",
         "Activa un modo Concentración como No molestar o Trabajo. Puede activarse solo al abrir una app concreta."),
        ("¿3 Tasks sirve para Pomodoro?",
         "Mide el tiempo de cada tarea y puede avisarte a los 15, 25, 45 o 60 minutos, pero no tiene temporizador "
         "de descanso. Usa Reloj para los descansos, o una app de Pomodoro si quieres que los cuente por ti."),
        ("¿Puedo arrancar el tiempo de 3 Tasks desde el widget?",
         "Todavía no. Hoy el widget enseña tus tres tareas; arrancar el tiempo desde el widget llega "
         "en la próxima versión."),
    ],
)

# --------------------------------------------------------------------------
# Pinku: como funciona la IA local en el iPhone
# --------------------------------------------------------------------------

PK5_EN = dict(
    path="pinku/how-does-local-ai-work-on-iphone.html",
    app_name="Private Offline AI Chat: Pinku",
    date_iso=ISO, date=D,
    h1="How does local AI work on iPhone? On-device models, memory and what runs where (2026)",
    desc=("A plain explanation of on-device AI on iPhone: what a model file is, why memory (RAM) decides which "
          "models run, how quantization shrinks them, what Apple Intelligence runs on the device and on its servers, "
          "and the memory rule we read in Pinku's code."),
    section="Guides", kicker="Pinku guide",
    standfirst=("A cloud chatbot sends your message to a data centre. A local one keeps a model file on your phone and "
                "does the maths on its own chip. That changes what you can run, how fast, and who sees your words."),
    tools=["an iPhone with enough memory", "an on-device AI chat app"],
    intro=f"""
<p><strong>We make Pinku, one of several apps that run AI models on the iPhone.</strong> The
explanation applies to all of them.</p>

<h2>What "local AI" means</h2>

<p>A language model is a large file of numbers (its weights) plus code that uses them to predict
the next word. With a cloud chatbot such as ChatGPT, Gemini or Claude, the weights stay in the
provider's data centre and every message travels there. With local AI, you download the weights
once and the iPhone's own chip runs them. After that it works in airplane mode, and your text does
not leave the device.</p>

<h2>Why memory decides what runs</h2>

<ul>
<li><strong>Size comes from parameters and bits.</strong> A model's weights take roughly
<em>parameters x bits per weight / 8</em> bytes. A 1-billion-parameter model stored at 4 bits is
around half a gigabyte of weights; real files are a bit larger. In Pinku's catalogue, Llama 3.2 1B
at 4 bits is 0.7 GB and Qwen 3 8B is 4.7 GB.</li>
<li><strong>Quantization is what makes phones possible.</strong> Storing each weight in 4 bits
instead of 16 makes the file about four times smaller, at some cost in quality. Apple compresses
its own on-device model, about 3 billion parameters, to 2 bits per weight
({a(APPLE_FM, "Apple Machine Learning Research, 2025")}).</li>
<li><strong>The whole model must fit in RAM while it runs</strong>, next to iOS and the app, plus
working memory that grows with the length of the conversation. iOS closes an app that asks for too
much, so the limit is the memory iOS lets one app use, not storage.</li>
<li><strong>Speed comes from the GPU.</strong> Apps such as Pinku and Locally AI use Apple's
{a(MLX, "MLX")} framework to run the model on the iPhone's graphics processor; smaller models answer faster.</li>
</ul>

<h2>The rule we read in Pinku's code</h2>

<p>We read the model code of the version on sale today (1.1). Pinku lists a model only if its
download is <strong>no more than 60% of the device's physical memory</strong>. Before loading one
on an iPhone, it asks iOS how much memory the app may still use (<code>os_proc_available_memory</code>)
and loads the model only if that is at least the model's size <strong>plus 10%</strong>; if not, it
says so and suggests a smaller model instead of crashing. In practice Gemma 3 1B (0.8 GB, the
default) needs about 1.4 GB of memory, Qwen 3 4B (2.3 GB) about 3.9 GB, and Qwen 3 8B (4.7 GB) about
7.9 GB, which on most iPhones rules it out and leaves it to iPads and Macs with more memory.</p>

<h2>What runs where on an iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>What</th><th>Where it runs</th></tr></thead>
<tbody>
<tr><td>Apple Intelligence on-device model (writing tools, summaries)</td><td>On the iPhone, a ~3B model at 2 bits per weight ({a(APPLE_FM, "Apple")})</td></tr>
<tr><td>Bigger Apple Intelligence requests</td><td>Apple's server model on Private Cloud Compute; Apple lists features that rely on server models, such as Image Playground, as having daily limits ({a(AI_FEATURES, "Apple, 121115")})</td></tr>
<tr><td>ChatGPT, Gemini, Claude and other cloud apps</td><td>The provider's servers; needs a connection for every message</td></tr>
<tr><td>On-device chat apps: Locally AI, PocketPal AI, Private LLM, Enclave, Pinku</td><td>On the iPhone, with open models you download (Llama, Qwen, Gemma and others)</td></tr>
</tbody>
</table>
</div>
""",
    steps=[
        ("Check your iPhone.",
         "Apple Intelligence needs an iPhone 15 Pro or later. For open models, more memory means bigger models: "
         "a 1B model runs on most recent iPhones, an 8B model needs a device with about 8 GB."),
        ("Free some storage.",
         "Models are 0.4 to 5 GB each. Settings, General, iPhone Storage shows how much room you have."),
        ("Install an on-device chat app.",
         f"Locally AI, PocketPal AI, Private LLM, Enclave or <a href=\"{PINKU_STORE}\">Pinku</a>. Read the App Store "
         "privacy label: local inference does not stop an app from collecting other data."),
        ("Download a small model on Wi-Fi.",
         "Start with a 1B model. It answers fast and leaves memory for the rest of the phone."),
        ("Test it in airplane mode.",
         "Turn on airplane mode and send a message. If it answers, it is really running on the iPhone."),
        ("Try a bigger model if it fits.",
         "A 3B or 4B model gives better answers but is slower and needs more memory. Close other heavy apps first."),
        ("Know the limits.",
         "Local models are smaller than cloud ones: less knowledge, more mistakes, no web search. Check anything important."),
    ],
    after=f"""
<h2>Where Pinku fits</h2>

<p>{a("https://apps.apple.com/us/app/id6754878073", "Pinku")} runs open models (Gemma, Llama, Qwen,
SmolLM3, DeepSeek-R1 Distill and others) on iPhone and Mac with MLX, keeps chat history only on the
device and has no account. It lists only the models your device can hold, and its larger models are
part of Pinku Pro. It has no web search, no image input and no image generation. Other apps go further
in some directions: PocketPal AI loads any GGUF model from Hugging Face, and Private LLM works with Siri
and Shortcuts. To see which models fit your device, use
<a href="which-ai-model-fits-my-iphone-mac.html">which AI model fits my iPhone or Mac</a>; for a trip,
<a href="use-ai-offline-on-a-plane-or-travelling.html">how to use AI offline on a plane</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(APPLE_FM, "Apple Machine Learning Research, Updates to Apple's On-Device and Server Foundation Language Models")}, 9 June 2025, updated 17 July 2025.</li>
<li>{a(AI_FEATURES, "Apple, Apple Intelligence features and requirements (121115)")}, published 22 October 2026.</li>
<li>Pinku 1.1 source code (ModelMemory.swift, model list filter, models.json), read 23 October 2026.</li>
<li>{a(MLX, "MLX, Apple's array framework for Apple silicon")}.</li>
</ul>
""",
    faq=[
        ("How does AI run locally on an iPhone?",
         "You download a model file once, and the app runs it on the iPhone's GPU. The text you type is processed "
         "on the device, so it works without internet."),
        ("How much RAM do I need to run an AI model on iPhone?",
         "Roughly the model's size plus room for iOS and the conversation. Pinku lists a model only if it is at "
         "most 60% of the device's memory: about 1.4 GB for a 0.8 GB model, about 7.9 GB for a 4.7 GB one."),
        ("Is Apple Intelligence local?",
         "Partly. Apple runs a model of about 3 billion parameters on the device and sends bigger requests to its "
         "server model on Private Cloud Compute."),
        ("Why are local models smaller than ChatGPT?",
         "They have to fit in the phone's memory. Cloud models run on data-centre hardware with far more memory, "
         "so they know more and make fewer mistakes."),
        ("What is quantization?",
         "Storing each weight in fewer bits, for example 4 instead of 16, which makes the model about four times "
         "smaller at some cost in quality."),
        ("Does local AI drain the battery?",
         "Generating text uses the GPU hard, so long chats use noticeable battery and warm the phone. Smaller "
         "models use less."),
    ],
)

PK5_ES = dict(
    path="pinku/es/como-funciona-la-ia-local-en-el-iphone.html",
    app_name="Private Offline AI Chat: Pinku",
    date_iso=ISO, date=D,
    h1="¿Cómo funciona la IA local en el iPhone? Modelos en el dispositivo, memoria y qué se ejecuta dónde (2026)",
    desc=("Explicación sencilla de la IA en el propio iPhone: qué es el archivo de un modelo, por qué la memoria (RAM) "
          "decide qué modelos funcionan, cómo los encoge la cuantización, qué hace Apple Intelligence en el "
          "dispositivo y en sus servidores, y la regla de memoria que leímos en el código de Pinku."),
    section="Guías", kicker="Guía de Pinku",
    standfirst=("Un chatbot en la nube manda tu mensaje a un centro de datos. Uno local guarda el archivo del modelo en el "
                "móvil y hace las cuentas con su propio chip. Eso cambia qué puedes usar, a qué velocidad y quién ve lo que escribes."),
    tools=["un iPhone con memoria suficiente", "una app de chat con IA en el dispositivo"],
    intro=f"""
<p><strong>Hacemos Pinku, una de las varias apps que ejecutan modelos de IA en el
iPhone.</strong> La explicación vale para todas.</p>

<h2>Qué quiere decir «IA local»</h2>

<p>Un modelo de lenguaje es un archivo grande de números (sus pesos) y un código que los usa para
predecir la siguiente palabra. Con un chatbot en la nube como ChatGPT, Gemini o Claude, los pesos se
quedan en el centro de datos del proveedor y cada mensaje viaja hasta allí. Con IA local descargas
los pesos una vez y los ejecuta el chip del iPhone. A partir de ahí funciona en modo avión y tu
texto no sale del dispositivo.</p>

<h2>Por qué manda la memoria</h2>

<ul>
<li><strong>El tamaño sale de los parámetros y los bits.</strong> Los pesos ocupan más o menos
<em>parámetros x bits por peso / 8</em> bytes. Un modelo de mil millones de parámetros guardado a 4
bits son unos 0,5 GB de pesos; los archivos reales son algo mayores. En el catálogo de Pinku, Llama
3.2 1B a 4 bits ocupa 0,7 GB y Qwen 3 8B, 4,7 GB.</li>
<li><strong>La cuantización es lo que lo hace posible en un móvil.</strong> Guardar cada peso en 4
bits en vez de 16 deja el archivo unas cuatro veces más pequeño, a cambio de algo de calidad. Apple
comprime su propio modelo del dispositivo, de unos 3.000 millones de parámetros, a 2 bits por peso
({a(APPLE_FM, "Apple Machine Learning Research, 2025")}).</li>
<li><strong>El modelo entero tiene que caber en la RAM mientras funciona</strong>, junto a iOS y la
app, más una memoria de trabajo que crece con lo larga que sea la conversación. iOS cierra la app
que pide demasiado, así que el límite es la memoria que iOS deja usar a una app, no el almacenamiento.</li>
<li><strong>La velocidad viene de la GPU.</strong> Apps como Pinku y Locally AI usan
{a(MLX, "MLX")}, el framework de Apple, para ejecutar el modelo en el procesador gráfico del
iPhone; los modelos pequeños contestan antes.</li>
</ul>

<h2>La regla que leímos en el código de Pinku</h2>

<p>Leímos el código de modelos de la versión que está hoy a la venta (1.1). Pinku solo enseña un
modelo si su descarga es <strong>como mucho el 60 % de la memoria física del dispositivo</strong>.
Antes de cargarlo en un iPhone, le pregunta a iOS cuánta memoria puede usar todavía la app
(<code>os_proc_available_memory</code>) y solo lo carga si es al menos el tamaño del modelo
<strong>más un 10 %</strong>; si no, lo dice y propone uno más pequeño en vez de cerrarse. En la
práctica, Gemma 3 1B (0,8 GB, el que viene por defecto) necesita unos 1,4 GB de memoria, Qwen 3 4B
(2,3 GB) unos 3,9 GB y Qwen 3 8B (4,7 GB) unos 7,9 GB, lo que lo deja fuera de la mayoría de iPhone y
para iPad y Mac con más memoria.</p>

<h2>Qué se ejecuta dónde en un iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Qué</th><th>Dónde se ejecuta</th></tr></thead>
<tbody>
<tr><td>Modelo de Apple Intelligence en el dispositivo (herramientas de escritura, resúmenes)</td><td>En el iPhone, un modelo de ~3B a 2 bits por peso ({a(APPLE_FM, "Apple")})</td></tr>
<tr><td>Peticiones más grandes de Apple Intelligence</td><td>El modelo de servidor de Apple en Private Cloud Compute; Apple dice que las funciones que usan modelos en servidor, como Image Playground, tienen límites diarios ({a(AI_FEATURES_ES, "Apple, 121115")})</td></tr>
<tr><td>ChatGPT, Gemini, Claude y otras apps en la nube</td><td>Los servidores del proveedor; necesitan conexión en cada mensaje</td></tr>
<tr><td>Apps de chat en el dispositivo: Locally AI, PocketPal AI, Private LLM, Enclave, Pinku</td><td>En el iPhone, con modelos abiertos que descargas (Llama, Qwen, Gemma y otros)</td></tr>
</tbody>
</table>
</div>
""",
    steps=[
        ("Mira tu iPhone.",
         "Apple Intelligence necesita un iPhone 15 Pro o posterior. Con modelos abiertos, más memoria es igual a "
         "modelos más grandes: uno de 1B funciona en casi todos los iPhone recientes; uno de 8B necesita unos 8 GB."),
        ("Libera espacio.",
         "Cada modelo ocupa de 0,4 a 5 GB. En Ajustes, General, Almacenamiento del iPhone ves cuánto tienes."),
        ("Instala una app de chat en el dispositivo.",
         f"Locally AI, PocketPal AI, Private LLM, Enclave o <a href=\"{PINKU_STORE}\">Pinku</a>. Lee la etiqueta de "
         "privacidad del App Store: ejecutar en local no impide que una app recoja otros datos."),
        ("Descarga un modelo pequeño con wifi.",
         "Empieza por uno de 1B. Contesta rápido y deja memoria para el resto del móvil."),
        ("Pruébalo en modo avión.",
         "Activa el modo avión y manda un mensaje. Si contesta, de verdad se ejecuta en el iPhone."),
        ("Prueba uno mayor si cabe.",
         "Uno de 3B o 4B contesta mejor pero va más lento y pide más memoria. Cierra antes otras apps pesadas."),
        ("Conoce los límites.",
         "Los modelos locales son más pequeños que los de la nube: saben menos, se equivocan más y no buscan en "
         "internet. Comprueba lo importante."),
    ],
    after=f"""
<h2>Dónde encaja Pinku</h2>

<p>{a("https://apps.apple.com/us/app/id6754878073", "Pinku")} ejecuta modelos abiertos (Gemma, Llama,
Qwen, SmolLM3, DeepSeek-R1 Distill y otros) en iPhone y Mac con MLX, guarda el historial solo en el
dispositivo y no tiene cuenta. Solo enseña los modelos que caben en tu dispositivo, y los más grandes
forman parte de Pinku Pro. No busca en internet, no lee imágenes ni las crea. Otras apps llegan más lejos
en algunas cosas: PocketPal AI carga cualquier modelo GGUF de Hugging Face y Private LLM funciona con Siri y
Atajos. Para un viaje, mira
<a href="usar-ia-sin-conexion-en-el-avion-o-de-viaje.html">cómo usar IA sin conexión en el avión o de viaje</a>,
y para ver qué modelos caben en tu dispositivo,
<a href="../which-ai-model-fits-my-iphone-mac.html">which AI model fits my iPhone or Mac</a> (en inglés).</p>

<h2>Fuentes</h2>
<ul>
<li>{a(APPLE_FM, "Apple Machine Learning Research, Updates to Apple's On-Device and Server Foundation Language Models")}, 9 de junio de 2025, actualizado el 17 de julio de 2025.</li>
<li>{a(AI_FEATURES_ES, "Apple, funciones y requisitos de Apple Intelligence (121115)")}, publicada el 22 de octubre de 2026.</li>
<li>Código de Pinku 1.1 (ModelMemory.swift, filtro de la lista de modelos, models.json), leído el 23 de octubre de 2026.</li>
<li>{a(MLX, "MLX, el framework de Apple para Apple silicon")}.</li>
</ul>
""",
    faq=[
        ("¿Cómo funciona la IA en local en un iPhone?",
         "Descargas una vez el archivo del modelo y la app lo ejecuta en la GPU del iPhone. Lo que escribes se "
         "procesa en el dispositivo, así que funciona sin internet."),
        ("¿Cuánta RAM hace falta para un modelo de IA en el iPhone?",
         "Más o menos el tamaño del modelo más sitio para iOS y la conversación. Pinku solo enseña un modelo si es "
         "como mucho el 60 % de la memoria: unos 1,4 GB para uno de 0,8 GB y unos 7,9 GB para uno de 4,7 GB."),
        ("¿Apple Intelligence es local?",
         "En parte. Apple ejecuta en el dispositivo un modelo de unos 3.000 millones de parámetros y manda las "
         "peticiones más grandes a su modelo de servidor en Private Cloud Compute."),
        ("¿Por qué los modelos locales son más pequeños que ChatGPT?",
         "Tienen que caber en la memoria del móvil. Los de la nube funcionan en máquinas de centro de datos con "
         "mucha más memoria, así que saben más y se equivocan menos."),
        ("¿Qué es la cuantización?",
         "Guardar cada peso con menos bits, por ejemplo 4 en vez de 16, para que el modelo ocupe unas cuatro veces "
         "menos a cambio de algo de calidad."),
        ("¿La IA local gasta mucha batería?",
         "Generar texto usa mucho la GPU, así que las conversaciones largas gastan batería y calientan el móvil. Los "
         "modelos pequeños gastan menos."),
    ],
)

GUIDES = [(BR_EN, BR_ES), (TT2_EN, TT2_ES), (TT3_EN, TT3_ES), (PK5_EN, PK5_ES)]
