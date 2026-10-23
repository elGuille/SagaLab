# -*- coding: utf-8 -*-
"""Guia de Dora: como hacer un video con ChatGPT (EN + ES), con la plantilla de guides.py.

Sale el dia que Dora AI Video aparece en el directorio de apps/plugins de ChatGPT.
CHATGPT_APP_URL y DATE_LIVE son marcadores que se sustituyen con sed ese dia.

Datos (todos ya publicados y comprobados):
- Sora: app cerrada el 26 abr 2026, API el 24 sep 2026 (OpenAI Help Center 20001152).
- Plugins de video del directorio de ChatGPT (Runway, Kling AI, Higgsfield, OpenArt, HeyGen,
  VEED, invideo, Visla, Descript): fichas publicas de OpenAI, comprobadas el 7 oct 2026 para el
  blog de doravideo.com. Como se instalan: OpenAI Help Center 20001256.
- Modo desarrollador (apps MCP propias): Business, Enterprise y Edu con acciones; Pro solo lectura
  (OpenAI Help Center 12584461).
- Dora: 16 modelos por MCP (9 de video, 7 de imagen), cuatro herramientas, preguntas antes de
  generar y prueba cronometrada del 23 oct 2026: doravideo.com/llms.txt, web/lib/mcp-facts.ts y
  doravideo.com/blog/make-a-video-with-chatgpt-or-claude.
De nuestras apps: sin precios y sin la palabra «free/gratis». Sin rayas. Dora va como una opcion
mas, no la primera.
"""
import datetime

ISO = "DATE_LIVE"


def _human(iso):
    months_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                 "septiembre", "octubre", "noviembre", "diciembre"]
    try:
        d = datetime.date.fromisoformat(iso)
    except ValueError:
        return {"en": iso, "es": iso}
    return {"en": "%d %s %d" % (d.day, d.strftime("%B"), d.year),
            "es": "%d de %s de %d" % (d.day, months_es[d.month - 1], d.year)}


D = _human(ISO)

CHATGPT_APP = "CHATGPT_APP_URL"
DORA_STORE = "https://apps.apple.com/app/apple-store/id6754180384?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
DORA_CHATGPT = "https://doravideo.com/chatgpt?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=chatgpt_guide"
DORA_TEST = "https://doravideo.com/blog/make-a-video-with-chatgpt-or-claude"
DORA_SPEC = "https://doravideo.com/ai-video-mcp"
SORA_END = "https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation"
PLUGINS = "https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex"
DEV_MODE = "https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt"
OPENAI_LISTINGS = "https://openai.com/business/plugins/runway"


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


# --------------------------------------------------------------------------
# Dora: como hacer un video con ChatGPT
# --------------------------------------------------------------------------

DV_EN = dict(
    path="dora/how-to-make-a-video-with-chatgpt.html",
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="How to make a video with ChatGPT: video plugins, Dora AI Video and the manual route (2026)",
    desc=("ChatGPT has no video model of its own since Sora closed. How to make a video from a ChatGPT chat "
          "today: video plugins from its directory, Dora AI Video step by step, the manual MCP route and what "
          "each needs."),
    section="Guides", kicker="Dora guide",
    standfirst=("ChatGPT does not draw video itself any more. It asks an outside video service to do it, through a "
                "plugin from its directory or an app you connect by hand. You set that up once and then ask in normal words."),
    tools=["ChatGPT", "a video plugin such as Dora AI Video"],
    intro=f"""
<p><strong>We make Dora, one of several video services you can use from ChatGPT.</strong> We use
it as the worked example because we can show exactly what it does; the steps have the same shape
for the other plugins below.</p>

<h2>Why ChatGPT needs a plugin to make video</h2>

<p>OpenAI closed the Sora app and website on April 26, 2026 and the Sora API on September 24, 2026
({a(SORA_END, "OpenAI Help Center")}), so ChatGPT has no built-in video model. A plugin connects
ChatGPT to a video service: you add it, connect your account with that service, and the video is
made by the service and paid with its credits, not with your ChatGPT plan.</p>

<h2>Ways to get a video from inside ChatGPT</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Route</th><th>What makes the video</th><th>Good to know</th></tr></thead>
<tbody>
<tr><td>Runway, Kling AI, Higgsfield or OpenArt plugins</td><td>Clips from a prompt or a photo, with each vendor's models</td><td>Listed in the ChatGPT directory ({a(OPENAI_LISTINGS, "OpenAI listings")}, checked 7 October 2026)</td></tr>
<tr><td>HeyGen or VEED plugins</td><td>A presenter talking to camera</td><td>Avatars and voices</td></tr>
<tr><td>invideo or Visla plugins</td><td>A produced video from a brief or script</td><td>Voiceover and music</td></tr>
<tr><td>Descript plugin</td><td>Edits a recording you already have</td><td>An editor, not a generator</td></tr>
<tr><td>{a(CHATGPT_APP, "Dora AI Video")} plugin</td><td>Short clips and images from a prompt or a photo: 9 video and 7 image models from Google, ByteDance, Kuaishou, xAI and OpenAI</td><td>Shows the coin cost of each model before generating; uses a Dora account</td></tr>
<tr><td>A custom app by URL (developer mode)</td><td>Any service with an MCP server</td><td>Actions that create content need ChatGPT Business, Enterprise or Edu ({a(DEV_MODE, "OpenAI")})</td></tr>
<tr><td>No plugin</td><td>Whatever video app you paste the prompt into</td><td>Works on any plan: ChatGPT writes the prompt, the app makes the video</td></tr>
</tbody>
</table>
</div>

<p>OpenAI says the directory is available across ChatGPT plans, while installing or using a given
plugin depends on your plan, workspace, role and region ({a(PLUGINS, "OpenAI Help Center")}).</p>
""",
    steps=[
        ("Add the plugin.",
         f"Open {a(CHATGPT_APP, 'Dora AI Video in ChatGPT')}, or search for it under Plugins in the ChatGPT "
         "sidebar, and add it. For another service, search for its name instead."),
        ("Connect your Dora account.",
         "ChatGPT asks you to sign in to Dora. Use the same Apple, Google or email account you use in the app or "
         "on doravideo.com. Generating needs a paid Dora plan or credit pack."),
        ("Ask for the video in normal words.",
         "For example: “Animate this product photo as a short vertical clip. Use the cheapest model and show "
         "me the cost before you start.” You can mention the plugin by name in the chat."),
        ("Answer the four questions.",
         "Before generating, Dora's connector has the assistant ask what you have not said: aspect ratio (9:16, "
         "16:9 or 1:1), duration (4, 8 or 12 seconds), sound on or off, and resolution (480p, 720p or 1080p). "
         "Higher resolution and sound cost more coins."),
        ("Wait for the file.",
         "The assistant checks the job until it is ready and gives you a link to an MP4. In our timed test on 23 "
         "October 2026 (through the same Dora server, from Claude) a 4-second 480p vertical clip was ready 30 "
         "seconds after the request; longer or premium clips take 1 to 5 minutes."),
        ("If Dora does not appear for you.",
         "Your plan, workspace or region may not allow it. On ChatGPT Business, Enterprise or Edu you can add "
         "https://doravideo.com/mcp as a custom app in developer mode; on any plan you can write the prompt in "
         "ChatGPT and make the video at doravideo.com or in the Dora iPhone app."),
    ],
    after=f"""
<h2>Where Dora fits, and where it does not</h2>

<p>Dora is for short clips and images from a prompt or a photo, with several model families in one
account and the cost in coins shown first. The same account works in ChatGPT, Claude, Cursor and
other MCP clients, on {a(DORA_STORE, "iPhone")} and at doravideo.com. It does not post to social
networks or edit clips together: you get a file. To animate your own photo, the connector needs a
public https link to the image. Unless you name a model or say “cheapest”, the assistant
chooses. For a presenter talking to camera, HeyGen or VEED fit better; for editing a recording,
Descript.</p>

<p>More detail: {a(DORA_CHATGPT, "Dora's ChatGPT page")}, the
{a(DORA_TEST, "timed test with ChatGPT and Claude")} and the {a(DORA_SPEC, "server specification")}.</p>

<h2>Sources</h2>
<ul>
<li>{a(SORA_END, "OpenAI Help Center, What to know about the Sora discontinuation")}.</li>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT")}.</li>
<li>{a(DEV_MODE, "OpenAI Help Center, Developer mode and MCP apps in ChatGPT")}.</li>
<li>{a(OPENAI_LISTINGS, "OpenAI plugin listings")} for Runway, Kling AI, Higgsfield, OpenArt, HeyGen, VEED, invideo, Visla and Descript, checked 7 October 2026.</li>
<li>{a(CHATGPT_APP, "Dora AI Video in the ChatGPT directory")}; Dora's connector code and timed test, 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Can ChatGPT make videos?",
         "Not on its own since OpenAI closed Sora (the app on April 26, 2026 and the API on September 24, 2026). "
         "It can make a video through a plugin from its directory, such as Runway, Kling AI, Higgsfield, HeyGen "
         "or Dora AI Video, or through a custom app on ChatGPT Business, Enterprise or Edu."),
        ("Is Dora in the ChatGPT app directory?",
         "Yes, as Dora AI Video. Add it, sign in with your Dora account and ask for a video in a chat. Whether you "
         "can use it depends on your ChatGPT plan, workspace, role and region."),
        ("Do I need a paid ChatGPT plan?",
         "Directory plugins depend on each plugin, your plan and your region. Custom apps that create content need "
         "Business, Enterprise or Edu. The video itself is paid with the video service's credits."),
        ("How long does a video take?",
         "In our test on 23 October 2026, a 4-second 480p clip through Dora's server was ready in 30 seconds. "
         "Longer, higher-resolution or premium clips take 1 to 5 minutes."),
        ("Can I turn my own photo into a video in ChatGPT?",
         "Yes, with a plugin that supports image-to-video. With Dora the photo must be a public https link to the "
         "image."),
        ("Does ChatGPT post the video for me?",
         "Not with Dora: you get an MP4 to download and post yourself."),
    ],
)

DV_ES = dict(
    path="dora/es/como-hacer-un-video-con-chatgpt.html",
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="Cómo hacer un vídeo con ChatGPT: plugins de vídeo, Dora AI Video y la vía manual (2026)",
    desc=("ChatGPT no tiene modelo de vídeo propio desde que cerró Sora. Cómo hacer un vídeo desde un chat de "
          "ChatGPT hoy: plugins de vídeo de su directorio, Dora AI Video paso a paso, la vía manual por MCP y qué "
          "necesita cada una."),
    section="Guías", kicker="Guía de Dora",
    standfirst=("ChatGPT ya no hace el vídeo él mismo. Se lo pide a un servicio de vídeo de fuera, con un plugin de "
                "su directorio o con una app que conectas a mano. Lo preparas una vez y luego lo pides con palabras normales."),
    tools=["ChatGPT", "un plugin de vídeo como Dora AI Video"],
    intro=f"""
<p><strong>Hacemos Dora, uno de los varios servicios de vídeo que se pueden usar desde
ChatGPT.</strong> Lo usamos de ejemplo porque podemos enseñar exactamente qué hace; con los demás
plugins de abajo los pasos son parecidos.</p>

<h2>Por qué ChatGPT necesita un plugin para hacer vídeo</h2>

<p>OpenAI cerró la app y la web de Sora el 26 de abril de 2026 y su API el 24 de septiembre de 2026
({a(SORA_END, "OpenAI Help Center")}), así que ChatGPT no tiene modelo de vídeo propio. Un plugin
conecta ChatGPT con un servicio de vídeo: lo añades, conectas tu cuenta de ese servicio, y el vídeo
lo hace el servicio y se paga con sus créditos, no con tu plan de ChatGPT.</p>

<h2>Formas de sacar un vídeo desde ChatGPT</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Vía</th><th>Qué hace el vídeo</th><th>Conviene saber</th></tr></thead>
<tbody>
<tr><td>Plugins de Runway, Kling AI, Higgsfield u OpenArt</td><td>Clips a partir de un texto o una foto, con los modelos de cada uno</td><td>Están en el directorio de ChatGPT ({a(OPENAI_LISTINGS, "fichas de OpenAI")}, comprobadas el 7 de octubre de 2026)</td></tr>
<tr><td>Plugins de HeyGen o VEED</td><td>Un presentador que habla a cámara</td><td>Avatares y voces</td></tr>
<tr><td>Plugins de invideo o Visla</td><td>Un vídeo montado a partir de un guion</td><td>Voz en off y música</td></tr>
<tr><td>Plugin de Descript</td><td>Edita una grabación que ya tienes</td><td>Es un editor, no un generador</td></tr>
<tr><td>Plugin {a(CHATGPT_APP, "Dora AI Video")}</td><td>Clips cortos e imágenes a partir de un texto o una foto: 9 modelos de vídeo y 7 de imagen de Google, ByteDance, Kuaishou, xAI y OpenAI</td><td>Enseña el coste en monedas de cada modelo antes de generar; usa una cuenta de Dora</td></tr>
<tr><td>Una app propia por URL (modo desarrollador)</td><td>Cualquier servicio con servidor MCP</td><td>Las acciones que crean contenido piden ChatGPT Business, Enterprise o Edu ({a(DEV_MODE, "OpenAI")})</td></tr>
<tr><td>Sin plugin</td><td>La app de vídeo donde pegues el prompt</td><td>Vale con cualquier plan: ChatGPT escribe el prompt y la app hace el vídeo</td></tr>
</tbody>
</table>
</div>

<p>OpenAI dice que el directorio está en todos los planes de ChatGPT, pero que instalar o usar un
plugin concreto depende del plan, el espacio de trabajo, el rol y el país ({a(PLUGINS, "OpenAI Help Center")}).</p>
""",
    steps=[
        ("Añade el plugin.",
         f"Abre {a(CHATGPT_APP, 'Dora AI Video en ChatGPT')}, o búscalo en Plugins, en la barra lateral de "
         "ChatGPT, y añádelo. Para otro servicio, busca su nombre."),
        ("Conecta tu cuenta de Dora.",
         "ChatGPT te pide que inicies sesión en Dora. Usa la misma cuenta de Apple, Google o correo que en la app o "
         "en doravideo.com. Para generar hace falta un plan de pago de Dora o un pack de créditos."),
        ("Pide el vídeo con palabras normales.",
         "Por ejemplo: «Anima esta foto de producto como un clip vertical corto. Usa el modelo más barato y "
         "dime cuánto cuesta antes de empezar». Puedes nombrar el plugin en el chat."),
        ("Contesta las cuatro preguntas.",
         "Antes de generar, el conector de Dora hace que el asistente pregunte lo que no hayas dicho: formato (9:16, "
         "16:9 o 1:1), duración (4, 8 o 12 segundos), con o sin sonido y resolución (480p, 720p o 1080p). Más "
         "resolución y el sonido cuestan más monedas."),
        ("Espera el archivo.",
         "El asistente consulta el trabajo hasta que está listo y te da un enlace a un MP4. En nuestra prueba "
         "cronometrada del 23 de octubre de 2026 (con el mismo servidor de Dora, desde Claude) un clip vertical de "
         "4 segundos a 480p estuvo listo 30 segundos después de pedirlo; los más largos o de modelos premium tardan "
         "de 1 a 5 minutos."),
        ("Si Dora no te aparece.",
         "Puede que tu plan, tu espacio de trabajo o tu país no lo permitan. Con ChatGPT Business, Enterprise o Edu "
         "puedes añadir https://doravideo.com/mcp como app propia en modo desarrollador; con cualquier plan puedes "
         "escribir el prompt en ChatGPT y hacer el vídeo en doravideo.com o en la app de Dora para iPhone."),
    ],
    after=f"""
<h2>Para qué sirve Dora y para qué no</h2>

<p>Dora sirve para clips cortos e imágenes a partir de un texto o una foto, con varias familias de
modelos en una sola cuenta y el coste en monedas a la vista antes de generar. La misma cuenta
funciona en ChatGPT, Claude, Cursor y otros clientes MCP, en el {a(DORA_STORE, "iPhone")} y en
doravideo.com. No publica en redes ni monta clips: te da un archivo. Para animar tu propia foto, el
conector necesita un enlace https público a la imagen. Si no nombras un modelo ni dices
«el más barato», elige el asistente. Para un presentador que habla a cámara encajan mejor
HeyGen o VEED; para editar una grabación, Descript.</p>

<p>Más detalle (en inglés): {a(DORA_CHATGPT, "la página de Dora para ChatGPT")}, la
{a(DORA_TEST, "prueba cronometrada con ChatGPT y Claude")} y la {a(DORA_SPEC, "especificación del servidor")}.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(SORA_END, "OpenAI Help Center, What to know about the Sora discontinuation")}.</li>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT")}.</li>
<li>{a(DEV_MODE, "OpenAI Help Center, Developer mode and MCP apps in ChatGPT")}.</li>
<li>{a(OPENAI_LISTINGS, "Fichas de plugins de OpenAI")} de Runway, Kling AI, Higgsfield, OpenArt, HeyGen, VEED, invideo, Visla y Descript, comprobadas el 7 de octubre de 2026.</li>
<li>{a(CHATGPT_APP, "Dora AI Video en el directorio de ChatGPT")}; código del conector de Dora y prueba cronometrada, 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿ChatGPT puede hacer vídeos?",
         "Por sí solo no, desde que OpenAI cerró Sora (la app el 26 de abril de 2026 y la API el 24 de septiembre "
         "de 2026). Puede hacerlo con un plugin de su directorio, como Runway, Kling AI, Higgsfield, HeyGen o Dora "
         "AI Video, o con una app propia en ChatGPT Business, Enterprise o Edu."),
        ("¿Está Dora en el directorio de apps de ChatGPT?",
         "Sí, como Dora AI Video. Añádelo, inicia sesión con tu cuenta de Dora y pide el vídeo en un chat. Que "
         "puedas usarlo depende de tu plan de ChatGPT, tu espacio de trabajo, tu rol y tu país."),
        ("¿Necesito un plan de pago de ChatGPT?",
         "Los plugins del directorio dependen de cada plugin, de tu plan y de tu país. Las apps propias que crean "
         "contenido piden Business, Enterprise o Edu. El vídeo se paga con los créditos del servicio de vídeo."),
        ("¿Cuánto tarda un vídeo?",
         "En nuestra prueba del 23 de octubre de 2026, un clip de 4 segundos a 480p con el servidor de Dora estuvo "
         "listo en 30 segundos. Los más largos, de más resolución o de modelos premium tardan de 1 a 5 minutos."),
        ("¿Puedo convertir mi propia foto en vídeo en ChatGPT?",
         "Sí, con un plugin que haga de imagen a vídeo. Con Dora la foto tiene que ser un enlace https público a la "
         "imagen."),
        ("¿ChatGPT publica el vídeo por mí?",
         "Con Dora no: te da un MP4 para descargarlo y publicarlo tú."),
    ],
)

GUIDES = [(DV_EN, DV_ES)]
