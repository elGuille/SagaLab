# -*- coding: utf-8 -*-
"""Guia: mejores plugins de ChatGPT para hacer videos e imagenes (EN + ES), con la plantilla de guides.py.

Datos (todos de fuentes publicas ya usadas en guides_oct24.py):
- Fichas de plugins de video del directorio de ChatGPT (Runway, Kling AI, Higgsfield, OpenArt, HeyGen,
  VEED, invideo, Visla, Descript): fichas publicas de OpenAI (openai.com/business/plugins), comprobadas el
  7 oct 2026 para el blog de doravideo.com (post how-to-make-videos-in-chatgpt-without-sora). Las fichas
  de openai.com dan 403 a curl: no se han vuelto a leer el 26 oct, se repite lo ya comprobado.
- Como se instalan los plugins: OpenAI Help Center 20001256.
- Dora AI Video: publicado en ChatGPT Plugins (categoria Creativity; «Turn a photo into a video»), datos
  de la ficha que nos pasa Marta (26 oct 2026) y de guides_oct24.py. Resultados guardados en la galeria de
  doravideo.com y en la app de Dora.
De nuestras apps: sin precios y sin la palabra «free/gratis». Sin rayas. Dora va en 4.o lugar, no la primera.
"""
from guides_oct24 import (CHATGPT_APP, DORA_STORE, DORA_CHATGPT, PLUGINS, DEV_MODE, OPENAI_LISTINGS, a, _human)

ISO = "2026-10-26"
D = _human(ISO)

EN_PATH = "dora/best-chatgpt-plugins-video-images-2026.html"
ES_PATH = "dora/es/mejores-plugins-chatgpt-video-imagenes-2026.html"

# --------------------------------------------------------------------------
BP_EN = dict(
    path=EN_PATH,
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="Best ChatGPT plugins for making videos and images (2026)",
    desc=("Ten ChatGPT plugins that make video or images from a chat: Runway, Kling AI, Higgsfield, Dora AI Video, "
          "OpenArt, HeyGen, VEED, invideo, Visla and Descript. What each does, which is best for what, and how to install one."),
    section="Guides", kicker="Comparison",
    standfirst=("ChatGPT has no video model of its own since Sora closed, so video and images come from plugins in "
                "ChatGPT Plugins. Here are ten, what each one is for, and how to add one."),
    tools=["ChatGPT", "a video or image plugin from ChatGPT Plugins"],
    intro=f"""
<p><strong>We make Dora AI Video, one of the ten plugins below.</strong> We list it where it fits
by what it does, not first. Everything about the other plugins comes from OpenAI's public plugin
listings and Help Center, checked 7 October 2026; we have not tested them for this page, so check
each listing for what your plan and region allow.</p>

<h2>The ten plugins at a glance</h2>

<div class="table-scroll">
<table>
<thead><tr><th>#</th><th>Plugin</th><th>What its listing says it does</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>1</td><td>Runway</td><td>Generates and edits images, videos and audio using your Runway account</td><td>Clips from a prompt or an image</td></tr>
<tr><td>2</td><td>Kling AI</td><td>Image and video generation</td><td>Clips from a prompt or an image</td></tr>
<tr><td>3</td><td>Higgsfield</td><td>Images and videos from text or reference images, including animating a still photo</td><td>Clips from a prompt or a photo</td></tr>
<tr><td>4</td><td>{a(CHATGPT_APP, "Dora AI Video")}</td><td>Short videos and images from a description or a photo, in vertical, horizontal or square</td><td>Turning a photo into a video; keeping one character across clips</td></tr>
<tr><td>5</td><td>OpenArt</td><td>Images and video, with reference images and a choice of models</td><td>Clips from a prompt or a photo</td></tr>
<tr><td>6</td><td>HeyGen</td><td>AI videos with avatars, voices and translations</td><td>A presenter talking to camera</td></tr>
<tr><td>7</td><td>VEED Video Generator</td><td>A library of characters and voices turned into a finished video</td><td>A presenter talking to camera</td></tr>
<tr><td>8</td><td>invideo</td><td>Script, visuals, voiceover and music from a text prompt</td><td>A produced video from a brief</td></tr>
<tr><td>9</td><td>Visla Video Maker</td><td>Narrated videos from scripts and source material</td><td>A produced video from a brief</td></tr>
<tr><td>10</td><td>Descript</td><td>A video editor you direct by chatting</td><td>Editing a recording you already have</td></tr>
</tbody>
</table>
</div>

<p>The order is by kind of use, generators first, then presenter and produced-video tools, then
editing. It is not a quality ranking.</p>

<h2>What each one is good for</h2>

<h3>Runway, Kling AI, Higgsfield: generators from the big video model makers</h3>
<p>Runway, Kling AI and Higgsfield make clips from a prompt or an image with their own models and
bill on your account with them. Higgsfield's listing also mentions animating a still photo. Pick one
if you already use that service or want its specific look.</p>

<h3>Dora AI Video: photo to video, one character, several shapes</h3>
<p>{a(CHATGPT_APP, "Dora AI Video")} is published in ChatGPT Plugins in the Creativity category,
with the line “Turn a photo into a video”. It makes short videos and images from a description or a
photo; it can keep the same character across clips; it outputs vertical, horizontal or square; and
it can copy dance moves onto a photo. Results are saved to the doravideo.com gallery and to the
{a(DORA_STORE, "Dora iPhone app")}, so you can pick them up outside ChatGPT. It needs a Dora
account. It makes clips and images; it does not edit a recording you already have or use an avatar
presenter, and it does not post to social networks. More: {a(DORA_CHATGPT, "Dora's ChatGPT page")}.</p>

<h3>OpenArt: images and video with a choice of models</h3>
<p>OpenArt's listing mentions reference images and a choice of models, which suits trying the same
idea on different models.</p>

<h3>HeyGen and VEED: a presenter talking to camera</h3>
<p>If you need a person on screen (explainer, training, translated message), HeyGen's avatars,
voices and translations, or VEED's library of characters and voices, fit better than a clip
generator.</p>

<h3>invideo and Visla: a produced video from a brief</h3>
<p>Both build a finished video from a script or prompt: invideo adds visuals, voiceover and music;
Visla makes narrated videos from scripts and source material.</p>

<h3>Descript: editing, not generating</h3>
<p>Descript is a video editor you direct by chatting. Choose it when you already have the footage.</p>

<h2>Which one should you pick?</h2>
<ul>
<li>A clip or image from a prompt or photo: Runway, Kling AI, Higgsfield, Dora AI Video or OpenArt.</li>
<li>A person talking to camera: HeyGen or VEED.</li>
<li>A finished video with voiceover from a script: invideo or Visla.</li>
<li>Cutting a recording: Descript.</li>
<li>None available on your plan: write the prompt in ChatGPT and paste it into a video app.</li>
</ul>
""",
    steps=[
        ("Open Plugins.",
         "In ChatGPT, open Plugins in the sidebar and search for the plugin's name."),
        ("Install it.",
         "Select Install plugin. If it asks, choose Connect and sign in to your account with that service."),
        ("Mention it in a chat.",
         "Type @ and the plugin's name, then describe what you want in normal words."),
        ("If it does not appear.",
         "Installing or using a given plugin depends on your ChatGPT plan, workspace, role and region. In a company "
         "workspace an administrator may have to allow it."),
    ],
    after=f"""
<p>Credits and plans are the service's, not OpenAI's: the video or image is made by the plugin's
service and paid under your account with it. For a step-by-step with one plugin, see
<a href="how-to-make-a-video-with-chatgpt.html">how to make a video with ChatGPT</a>. A service
that is not in the list can still be added as a custom app in developer mode, with actions that
create content on ChatGPT Business, Enterprise or Edu ({a(DEV_MODE, "OpenAI")}).</p>

<h2>Sources</h2>
<ul>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT and Codex")}: how plugins are installed and what limits availability.</li>
<li>{a(OPENAI_LISTINGS, "OpenAI plugin listings")} for Runway, Kling AI, Higgsfield, OpenArt, HeyGen, VEED, invideo, Visla and Descript, checked 7 October 2026.</li>
<li>{a(DEV_MODE, "OpenAI Help Center, Developer mode and MCP apps in ChatGPT")}.</li>
<li>{a(CHATGPT_APP, "Dora AI Video in ChatGPT Plugins")}.</li>
</ul>
""",
    faq=[
        ("Is Dora a ChatGPT plugin?",
         "Yes. Dora AI Video by Saga Labs is published in ChatGPT Plugins, in the Creativity category: "
         + CHATGPT_APP),
        ("What are the best ChatGPT plugins for making videos?",
         "For clips from a prompt or photo: Runway, Kling AI, Higgsfield, Dora AI Video and OpenArt. For a presenter "
         "talking to camera: HeyGen and VEED. For a produced video from a script: invideo and Visla. For editing: Descript."),
        ("How do I install a ChatGPT plugin?",
         "Open Plugins in the ChatGPT sidebar, search for the name, select Install plugin and, if asked, Connect your "
         "account with the service. Then type @ and its name in a chat. Availability depends on your plan, workspace, "
         "role and region (OpenAI Help Center)."),
        ("Can ChatGPT make images and videos by itself?",
         "Not video: OpenAI closed the Sora app on April 26, 2026 and the Sora API on September 24, 2026. Video "
         "comes from a plugin or a custom app."),
        ("Who pays for the video?",
         "The plugin's service, under your account with it, not your ChatGPT plan."),
    ],
)

BP_ES = dict(
    path=ES_PATH,
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="Mejores plugins de ChatGPT para hacer vídeos e imágenes (2026)",
    desc=("Diez plugins de ChatGPT que hacen vídeo o imágenes desde un chat: Runway, Kling AI, Higgsfield, Dora AI Video, "
          "OpenArt, HeyGen, VEED, invideo, Visla y Descript. Qué hace cada uno, para qué sirve y cómo instalarlo."),
    section="Guías", kicker="Comparativa",
    standfirst=("ChatGPT no tiene modelo de vídeo propio desde que cerró Sora, así que el vídeo y las imágenes salen de "
                "plugins de ChatGPT Plugins. Aquí van diez, para qué sirve cada uno y cómo añadirlo."),
    tools=["ChatGPT", "un plugin de vídeo o imagen de ChatGPT Plugins"],
    intro=f"""
<p><strong>Hacemos Dora AI Video, uno de los diez plugins de abajo.</strong> Lo ponemos donde encaja
por lo que hace, no el primero. Lo de los demás plugins viene de las fichas públicas de OpenAI y de
su Help Center, comprobadas el 7 de octubre de 2026; no los hemos probado para esta página, así que
mira cada ficha para saber qué permiten tu plan y tu país.</p>

<h2>Los diez plugins de un vistazo</h2>

<div class="table-scroll">
<table>
<thead><tr><th>N.º</th><th>Plugin</th><th>Qué dice su ficha que hace</th><th>Mejor para</th></tr></thead>
<tbody>
<tr><td>1</td><td>Runway</td><td>Genera y edita imágenes, vídeos y audio con tu cuenta de Runway</td><td>Clips a partir de un texto o una imagen</td></tr>
<tr><td>2</td><td>Kling AI</td><td>Generación de imagen y vídeo</td><td>Clips a partir de un texto o una imagen</td></tr>
<tr><td>3</td><td>Higgsfield</td><td>Imágenes y vídeos a partir de texto o imágenes de referencia, incluido animar una foto fija</td><td>Clips a partir de un texto o una foto</td></tr>
<tr><td>4</td><td>{a(CHATGPT_APP, "Dora AI Video")}</td><td>Vídeos e imágenes cortos a partir de una descripción o una foto, en vertical, horizontal o cuadrado</td><td>Convertir una foto en vídeo; mantener el mismo personaje entre clips</td></tr>
<tr><td>5</td><td>OpenArt</td><td>Imágenes y vídeo, con imágenes de referencia y varios modelos a elegir</td><td>Clips a partir de un texto o una foto</td></tr>
<tr><td>6</td><td>HeyGen</td><td>Vídeos con avatares, voces y traducciones</td><td>Un presentador que habla a cámara</td></tr>
<tr><td>7</td><td>VEED Video Generator</td><td>Una biblioteca de personajes y voces convertida en un vídeo terminado</td><td>Un presentador que habla a cámara</td></tr>
<tr><td>8</td><td>invideo</td><td>Guion, imágenes, voz en off y música a partir de un texto</td><td>Un vídeo montado a partir de un guion</td></tr>
<tr><td>9</td><td>Visla Video Maker</td><td>Vídeos narrados a partir de guiones y material de partida</td><td>Un vídeo montado a partir de un guion</td></tr>
<tr><td>10</td><td>Descript</td><td>Un editor de vídeo que diriges chateando</td><td>Editar una grabación que ya tienes</td></tr>
</tbody>
</table>
</div>

<p>El orden va por tipo de uso: primero los generadores, luego presentadores y vídeos montados, y al
final la edición. No es una clasificación de calidad.</p>

<h2>Para qué sirve cada uno</h2>

<h3>Runway, Kling AI, Higgsfield: generadores de los grandes del vídeo con IA</h3>
<p>Runway, Kling AI y Higgsfield hacen clips a partir de un texto o una imagen con sus propios modelos
y cobran en tu cuenta con ellos. La ficha de Higgsfield menciona también animar una foto fija. Elige
uno si ya usas ese servicio o te gusta su estilo.</p>

<h3>Dora AI Video: de foto a vídeo, un personaje, varios formatos</h3>
<p>{a(CHATGPT_APP, "Dora AI Video")} está publicado en ChatGPT Plugins, en la categoría Creativity,
con la frase «Turn a photo into a video». Hace vídeos e imágenes cortos a partir de una descripción o
una foto; puede mantener el mismo personaje entre clips; los saca en vertical, horizontal o cuadrado;
y puede copiar movimientos de baile sobre una foto. Los resultados se guardan en la galería de
doravideo.com y en la {a(DORA_STORE, "app de Dora para iPhone")}, así que puedes retomarlos fuera de
ChatGPT. Necesita una cuenta de Dora. Hace clips e imágenes; no edita una grabación que ya tengas, no
usa un presentador con avatar y no publica en redes. Más (en inglés): {a(DORA_CHATGPT, "la página de Dora para ChatGPT")}.</p>

<h3>OpenArt: imágenes y vídeo con varios modelos</h3>
<p>La ficha de OpenArt menciona imágenes de referencia y varios modelos a elegir, útil para probar la
misma idea en modelos distintos.</p>

<h3>HeyGen y VEED: un presentador que habla a cámara</h3>
<p>Si necesitas una persona en pantalla (explicación, formación, mensaje traducido), los avatares, voces
y traducciones de HeyGen, o la biblioteca de personajes y voces de VEED, encajan mejor que un
generador de clips.</p>

<h3>invideo y Visla: un vídeo montado a partir de un guion</h3>
<p>Los dos construyen un vídeo terminado a partir de un guion o un texto: invideo añade imágenes, voz en
off y música; Visla hace vídeos narrados a partir de guiones y material de partida.</p>

<h3>Descript: editar, no generar</h3>
<p>Descript es un editor de vídeo que diriges chateando. Elígelo cuando ya tienes las imágenes grabadas.</p>

<h2>Cuál elegir</h2>
<ul>
<li>Un clip o imagen a partir de un texto o una foto: Runway, Kling AI, Higgsfield, Dora AI Video u OpenArt.</li>
<li>Una persona hablando a cámara: HeyGen o VEED.</li>
<li>Un vídeo terminado con voz en off a partir de un guion: invideo o Visla.</li>
<li>Cortar una grabación: Descript.</li>
<li>Ninguno disponible en tu plan: escribe el prompt en ChatGPT y pégalo en una app de vídeo.</li>
</ul>
""",
    steps=[
        ("Abre Plugins.",
         "En ChatGPT, abre Plugins en la barra lateral y busca el nombre del plugin."),
        ("Instálalo.",
         "Pulsa Install plugin. Si te lo pide, elige Connect e inicia sesión con tu cuenta de ese servicio."),
        ("Nómbralo en un chat.",
         "Escribe @ y el nombre del plugin, y describe lo que quieres con palabras normales."),
        ("Si no te aparece.",
         "Instalar o usar un plugin concreto depende de tu plan de ChatGPT, tu espacio de trabajo, tu rol y tu país. "
         "En un espacio de trabajo de empresa, puede que un administrador tenga que permitirlo."),
    ],
    after=f"""
<p>Los créditos y los planes son los del servicio, no los de OpenAI: el vídeo o la imagen los hace el
servicio del plugin y se pagan en tu cuenta con él. Para un paso a paso con un plugin, mira
<a href="como-hacer-un-video-con-chatgpt.html">cómo hacer un vídeo con ChatGPT</a>. Un servicio que no
está en la lista se puede añadir igualmente como app propia en modo desarrollador, con acciones que crean
contenido en ChatGPT Business, Enterprise o Edu ({a(DEV_MODE, "OpenAI")}).</p>

<h2>Fuentes</h2>
<ul>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT and Codex")}: cómo se instalan los plugins y qué limita su disponibilidad.</li>
<li>{a(OPENAI_LISTINGS, "Fichas de plugins de OpenAI")} de Runway, Kling AI, Higgsfield, OpenArt, HeyGen, VEED, invideo, Visla y Descript, comprobadas el 7 de octubre de 2026.</li>
<li>{a(DEV_MODE, "OpenAI Help Center, Developer mode and MCP apps in ChatGPT")}.</li>
<li>{a(CHATGPT_APP, "Dora AI Video en ChatGPT Plugins")}.</li>
</ul>
""",
    faq=[
        ("¿Es Dora un plugin de ChatGPT?",
         "Sí. Dora AI Video, de Saga Labs, está publicado en ChatGPT Plugins, en la categoría Creativity: "
         + CHATGPT_APP),
        ("¿Cuáles son los mejores plugins de ChatGPT para hacer vídeos?",
         "Para clips a partir de un texto o una foto: Runway, Kling AI, Higgsfield, Dora AI Video y OpenArt. Para un "
         "presentador que habla a cámara: HeyGen y VEED. Para un vídeo montado a partir de un guion: invideo y Visla. "
         "Para editar: Descript."),
        ("¿Cómo instalo un plugin de ChatGPT?",
         "Abre Plugins en la barra lateral de ChatGPT, busca el nombre, pulsa Install plugin y, si te lo pide, Connect "
         "para conectar tu cuenta del servicio. Luego escribe @ y su nombre en un chat. Que esté disponible depende de "
         "tu plan, espacio de trabajo, rol y país (OpenAI Help Center)."),
        ("¿ChatGPT puede hacer vídeos e imágenes por sí solo?",
         "Vídeo no: OpenAI cerró la app de Sora el 26 de abril de 2026 y su API el 24 de septiembre de 2026. El vídeo "
         "sale de un plugin o de una app propia."),
        ("¿Quién paga el vídeo?",
         "El servicio del plugin, en tu cuenta con él, no tu plan de ChatGPT."),
    ],
)

GUIDES = [(BP_EN, BP_ES)]
