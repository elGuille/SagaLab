# -*- coding: utf-8 -*-
"""Guia: como animar una foto en Claude (EN + ES), mismo formato que guides_nov02b.py (imagenes en Claude).

Datos:
- Tres videos reales del catalogo de saga-growth (data/generaciones/catalogo.csv, origen claude_mcp), todos de
  Seedance 2 Mini, con su foto de partida en foto_referencia (URL publica de Storage de una imagen hecha con Dora):
  5e512cfb (8 s, 480p, 31 monedas), 694a2d73 y 8c2756d0 (4 s, 480p, 16 monedas). Ninguno trae pista de sonido.
  Fotos de partida: 7a72cfe9 (persona generada, Nano Banana 2) y dos versiones de epoca hechas a partir de ella
  (80692be7 y fc31b0e2, Nano Banana 2, 8 monedas cada una el 1 nov). Ninguna es una persona real.
- Comprobado mirando los fotogramas: saluda y se acerca; descuelga el telefono; la lampara se apaga y se enciende
  (brillo de la pantalla de la lampara de 210 a 165 y vuelta).
- Costes: list_models del 2 nov (Seedance 2 Mini 31; Grok Imagine 1.5 20; Kling 2.6 Motion Control 11 por segundo,
  minimo 3 s; Nano Banana 2 10). 4 s a 480p = 16, 8 s a 720p = 66: doravideo.com/models.
- Como se pasa la foto: en los tres, como enlace https publico. Adjuntarla al chat no esta probado: no se afirma.
- Pasos del conector: no se repiten, se enlaza a la guia de imagenes en Claude.
Sin Veo. Aviso de Dora al final. Sin rayas.
"""
from guides_oct24 import (DORA_STORE, a, _human)

ISO = "2026-11-03"
D = _human(ISO)

EN_PATH = "dora/how-to-animate-a-photo-in-claude.html"
ES_PATH = "dora/es/como-animar-una-foto-con-claude.html"

U = "?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=claude_animate"
DORA_CLAUDE = "https://doravideo.com/claude" + U
PRICING = "https://doravideo.com/pricing" + U
MODELS = "https://doravideo.com/models" + U
VIDEO_GUIDE = "https://doravideo.com/blog/how-to-make-videos-in-claude" + U
HC_IMAGES = "https://support.claude.com/en/articles/9002504-can-claude-produce-images"
HC_CONNECTORS = "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp"

IMG = "../images/dora/claude/"
IMG_ES = "../../images/dora/claude/"

# (foto, fotograma, enlace al video, ajustes EN, ES, prompt de la foto o None, prompt del video, que salio EN, ES)
EXAMPLES = [
    ("photo-living-room.webp", "clip-walk-wave.webp", "https://doravideo.com/v/3V5hZeAlmR2wFIm_jNXwzA",
     "Seedance 2 Mini, vertical 9:16, 8 seconds, 480p, 31 coins", "Seedance 2 Mini, vertical 9:16, 8 segundos, 480p, 31 monedas",
     None,
     "The woman from the photo walks toward the camera across the bright room, smiles and waves, her hair moving "
     "slightly, handheld camera, natural daylight",
     "She walks up to the camera, smiles and waves, and the room stays the same. The camera follows her so closely "
     "that the clip ends on her face and shoulders, not her whole body.",
     "Se acerca a la cámara, sonríe y saluda, y la habitación no cambia. La cámara la sigue tan de cerca que el vídeo "
     "acaba en su cara y sus hombros, no de cuerpo entero."),
    ("photo-1980s-wall-phone.webp", "clip-wall-phone.webp", "https://doravideo.com/v/RCSbVmF_CT1CYPfOry6xkg",
     "Seedance 2 Mini, vertical 9:16, 4 seconds, 480p, 16 coins", "Seedance 2 Mini, vertical 9:16, 4 segundos, 480p, 16 monedas",
     "Turn the person in the reference photo into a real 1980s snapshot: same face, big curly 80s hair, patterned "
     "blouse, standing against wood-panelled wall next to a beige wall phone, warm faded film colours, soft flash, "
     "slight grain, natural smile, looks like a genuine photo from 1985, vertical, no text",
     "She smiles, tilts her head and picks up the wall phone, curls moving slightly, fixed camera, warm 1980s film look "
     "with slight grain",
     "She takes the receiver off the wall and holds it to her ear, smiling, with the cord moving. Four seconds is "
     "enough for one action like this.",
     "Descuelga el auricular de la pared y se lo acerca a la oreja, sonriendo, y el cable se mueve. Cuatro segundos "
     "bastan para una acción así."),
    ("photo-1970s-lamp.webp", "clip-lamp.webp", "https://doravideo.com/v/9gLNAZWk_OgTeBplOA0gmw",
     "Seedance 2 Mini, vertical 9:16, 4 seconds, 480p, 16 coins", "Seedance 2 Mini, vertical 9:16, 4 segundos, 480p, 16 monedas",
     "Turn the person in the reference photo into a real 1970s snapshot: same face, long feathered wavy hair, brown "
     "patterned blouse with a wide collar, warm wood-panelled living room with a lamp, golden faded film colours, slight "
     "grain, soft smile, looks like a genuine photo from 1975, vertical, no text",
     "She smiles, turns to the table and switches the lamp off and on, wavy hair moving slightly, warm light changes on "
     "the wood walls, fixed camera, golden 1970s film look with slight grain",
     "She reaches for the lamp and it goes off and on again near the end. The change of light on the walls is weaker "
     "than the prompt asked.",
     "Alarga la mano hacia la lámpara, que se apaga y se vuelve a encender hacia el final. El cambio de luz en las "
     "paredes es más flojo de lo que pedía el prompt."),
]


TITLES = [("A walk and a wave", "Cruza la habitación y saluda"),
          ("A 1980s photo picks up the phone", "Una foto de los 80 descuelga el teléfono"),
          ("A 1970s photo switches the lamp off and on", "Una foto de los 70 apaga y enciende la lámpara")]


def _examples(lang):
    base = IMG if lang == "en" else IMG_ES
    en = lang == "en"
    out = []
    for i, (ph, fr, link, s_en, s_es, img_prompt, vid_prompt, n_en, n_es) in enumerate(EXAMPLES, 1):
        cap_ph = ("Starting photo" if en else "Foto de partida")
        cap_fr = ("A frame from the video" if en else "Un fotograma del vídeo")
        out.append(
            '<h3>%d. %s</h3>\n'
            '<div style="display:flex;gap:12px;flex-wrap:wrap;margin:16px 0">\n'
            '<figure style="margin:0;flex:1 1 140px;max-width:240px"><img src="%s%s" width="360" height="645" loading="lazy" '
            'alt="%s" style="display:block;width:100%%;height:auto;border-radius:8px"><figcaption>%s</figcaption></figure>\n'
            '<figure style="margin:0;flex:1 1 140px;max-width:240px"><a href="%s" target="_blank" rel="noopener">'
            '<img src="%s%s" width="360" height="628" loading="lazy" alt="%s" '
            'style="display:block;width:100%%;height:auto;border-radius:8px"></a><figcaption>%s</figcaption></figure>\n'
            '</div>\n'
            '<p><a href="%s" target="_blank" rel="noopener">%s</a> &middot; %s.</p>\n'
            '<p><strong>%s</strong></p>\n<blockquote>%s</blockquote>\n'
            '<p>%s</p>\n'
            % (i, TITLES[i - 1][0 if en else 1],
               base, ph, cap_ph, cap_ph,
               link, base, fr, cap_fr, cap_fr,
               link, "Watch the video (MP4)" if en else "Ver el vídeo (MP4)", s_en if en else s_es,
               "Exact video prompt:" if en else "Prompt exacto del vídeo (en inglés, tal cual):", vid_prompt,
               n_en if en else n_es))
        if img_prompt:
            out.append('<p>%s</p>\n<blockquote>%s</blockquote>\n' % (
                "The starting photo was itself made from the first one, with this prompt (Nano Banana 2, 8 coins):" if en
                else "La foto de partida se hizo a su vez a partir de la primera, con este prompt (Nano Banana 2, 8 monedas):",
                img_prompt))
    return "".join(out)


# --------------------------------------------------------------------------
BP_EN = dict(
    path=EN_PATH,
    app_name="Dora",
    date_iso=ISO, date=D,
    h1="How to animate a photo in Claude (2026)",
    desc=("Claude cannot animate a photo by itself; with a video connector it can. How to give it the photo, how to write "
          "the motion, what it costs (31 coins for 8 seconds by default) and three real photo-to-video results with their prompts."),
    section="Guides", kicker="How to",
    standfirst=("Give Claude a photo, say how it should move, and a video connector turns it into a short clip. Here "
                "is how, what it costs, and three photos animated that way, with the exact prompts."),
    tools=["Claude", "Dora connector"],
    intro=f"""
<p><strong>Short answer:</strong> Claude has no image or video model of its own (Anthropic's help
center says it does not generate photos or illustrations, {a(HC_IMAGES, "Can Claude produce images?")}),
so it cannot animate a photo by itself. With a video connector it can: you give it the photo and
describe the movement, and the connector makes the clip. With Dora's connector the default model,
Seedance 2 Mini, costs 31 coins for 8 seconds, roughly $0.31 to $0.62, paid with Dora coins, not your
Claude plan.</p>

<h2>Before you start</h2>
<p>You need Claude with a custom connector (Anthropic lists every plan, Free limited to one,
{a(HC_CONNECTORS, "Claude Help Center")}) and a Dora account with coins. Adding the connector takes
about a minute; the steps are in <a href="how-to-make-images-in-claude.html">how to make images in
Claude</a>, so they are not repeated here.</p>
""",
    steps=[
        ("Have the photo ready.",
         "In our three examples the photo was a public https link to an image. See below for what we know about other ways."),
        ("Say how it should move.",
         "One or two actions, who does them, and what the camera does: “she smiles and picks up the phone, fixed camera”."),
        ("Choose the length.",
         "Four seconds for one action, eight for a walk and a wave. Say vertical, horizontal or square."),
        ("Ask for the price first.",
         "Add “tell me the cost first and wait for my confirmation”; otherwise Claude may start straight away."),
        ("Open the video.",
         "The video comes back as a link to the file, not inside the chat. Download it from there."),
    ],
    after=f"""
<h2>How to give Claude the photo</h2>
<p>In all three examples below, the photo was passed as a public https link to an image (the address
of a picture already stored in Dora). That is what we can show worked. We have not tested attaching a
photo straight to the Claude chat for this, so we do not say whether it works; if it fails, put the
photo somewhere it has a public link and give Claude that link.</p>

<h2>How to write the movement</h2>
<ul>
<li><strong>Start from what is in the photo.</strong> “The woman from the photo…” keeps the person;
naming objects that are in the picture (the wall phone, the lamp) gives the motion something to act on.</li>
<li><strong>One action per short clip.</strong> Picking up a phone fits in 4 seconds; walking across a
room and waving needed 8.</li>
<li><strong>Say what the camera does.</strong> “Fixed camera” keeps the frame still; “handheld” lets it
move and follow.</li>
<li><strong>Keep the look.</strong> Repeat the style of the photo (“warm 1980s film look”) so the clip
matches it.</li>
</ul>

<h2>Three photos animated this way</h2>
<p>All three were made with Dora's connector called from Claude, on 1 and 2 November 2026, with
Seedance 2 Mini, and are kept in Dora's records with their prompt, settings and cost. None was made
for this page. The woman is not a real person: the first photo was generated with Dora, and the other
two are versions of it. None of the three files has a sound track. Click a frame to watch the clip.</p>
{_examples("en")}

<h2>What it costs</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Video model in Dora's connector</th><th>Coins</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Seedance 2 Mini</td><td>31 for 8 s</td><td>The default; 16 for 4 s at 480p, 66 for 8 s at 720p</td></tr>
<tr><td>Grok Imagine 1.5</td><td>20</td><td>Cheaper; one photo at most</td></tr>
<tr><td>Kling 2.6 Motion Control</td><td>11 per second</td><td>Copies the movement of a video you give it onto the person in the photo; 3 seconds minimum</td></tr>
</tbody>
</table>
</div>
<p>Prices from Dora's connector model list on 2 November 2026; longer clips, higher resolution and
sound cost more ({a(MODELS, "Dora's models page")}). A coin is about $0.01 on the weekly plan and $0.02
on the yearly one ({a(PRICING, "pricing")}). If you first change the photo, as in examples 2 and 3,
add the image: 10 coins with Nano Banana 2 (8 when those were made). With no coins nothing is made or
charged, and a failed generation gives the coins back.</p>

<h2>More</h2>
<p>For videos from a description instead of a photo, and Dora's own timed tests, see
{a(VIDEO_GUIDE, "how to make videos in Claude")}. For still images, see
<a href="how-to-make-images-in-claude.html">how to make images in Claude</a>. Setup with a button that
opens the form: {a(DORA_CLAUDE, "Dora for Claude")}. On iPhone, the same account and coins work in the
{a(DORA_STORE, "Dora app")}.</p>

<h2>Sources</h2>
<ul>
<li>{a(HC_IMAGES, "Claude Help Center, Can Claude produce images?")} and {a(HC_CONNECTORS, "Get started with custom connectors using remote MCP")}, checked 2 November 2026.</li>
<li>Dora's connector model list and {a(PRICING, "pricing")}, read on 2 November 2026; {a(MODELS, "Dora models and costs")}.</li>
<li>Dora's generation records for the three videos and their starting photos: model, settings, coins, prompt and photo link.</li>
</ul>
<p><strong>Disclosure:</strong> Saga Labs, which publishes this site, makes Dora. The photos and videos
were made with Dora; costs are Dora's own.</p>
""",
    faq=[
        ("Can Claude animate a photo?",
         "Not by itself: Claude has no video model. With a video connector such as Dora, you give it the photo and describe "
         "the movement, and the connector makes a short clip and returns a link to it."),
        ("How much does it cost to animate a photo in Claude?",
         "Your Claude plan does not pay for it. With Dora the default, Seedance 2 Mini, is 31 coins for 8 seconds and 16 for "
         "4 seconds at 480p, roughly $0.16 to $0.62."),
        ("How do I give Claude the photo?",
         "In our examples the photo was a public https link to the image. We have not tested attaching it straight to the "
         "chat, so if that fails, use a public link."),
        ("How long should the clip be?",
         "Four seconds is enough for one action, like picking up a phone; a walk and a wave took eight."),
        ("Does the video come with sound?",
         "None of our three examples has a sound track. Some models can add sound, and it costs more."),
        ("Is the result shown in the chat?",
         "Videos come back as a link to the file, not inside the chat."),
    ],
)

# --------------------------------------------------------------------------
BP_ES = dict(
    path=ES_PATH,
    app_name="Dora",
    date_iso=ISO, date=D,
    h1="Cómo animar una foto con Claude (2026)",
    desc=("Claude no puede animar una foto por sí solo; con un conector de vídeo, sí. Cómo pasarle la foto, cómo escribir "
          "el movimiento, cuánto cuesta (31 monedas por 8 segundos por defecto) y tres fotos animadas de verdad, con su prompt."),
    section="Guías", kicker="Cómo se hace",
    standfirst=("Le das a Claude una foto, le dices cómo se mueve, y un conector de vídeo la convierte en un vídeo "
                "corto. Aquí va cómo, cuánto cuesta y tres fotos animadas así, con el prompt exacto."),
    tools=["Claude", "conector de Dora"],
    intro=f"""
<p><strong>En corto:</strong> Claude no tiene modelo de imagen ni de vídeo propio (el centro de ayuda
de Anthropic dice que no genera fotos ni ilustraciones, {a(HC_IMAGES, "Can Claude produce images?")}),
así que no puede animar una foto por sí solo. Con un conector de vídeo, sí: le das la foto, describes
el movimiento y el conector hace el vídeo. Con el conector de Dora, el modelo por defecto, Seedance 2
Mini, cuesta 31 monedas por 8 segundos, entre 0,31 y 0,62 $, que se pagan con monedas de Dora, no con
tu plan de Claude.</p>

<h2>Antes de empezar</h2>
<p>Necesitas Claude con un conector propio (Anthropic lo incluye en todos los planes, en Free uno
solo, {a(HC_CONNECTORS, "Claude Help Center")}) y una cuenta de Dora con monedas. Añadir el conector
lleva un minuto; los pasos están en <a href="como-hacer-imagenes-con-claude.html">cómo hacer imágenes
con Claude</a> y no se repiten aquí.</p>
""",
    steps=[
        ("Ten la foto a mano.",
         "En nuestros tres ejemplos, la foto era un enlace https público a una imagen. Más abajo, lo que sabemos de otras formas."),
        ("Di cómo se mueve.",
         "Una o dos acciones, quién las hace y qué hace la cámara: «sonríe y descuelga el teléfono, cámara fija»."),
        ("Elige la duración.",
         "Cuatro segundos para una acción, ocho para cruzar una habitación y saludar. Di vertical, horizontal o cuadrado."),
        ("Pide antes el precio.",
         "Añade «dime antes lo que cuesta y espera a que lo confirme»; si no, Claude puede empezar directamente."),
        ("Abre el vídeo.",
         "El vídeo llega como un enlace al archivo, no dentro del chat. Descárgalo desde ahí."),
    ],
    after=f"""
<h2>Cómo pasarle la foto a Claude</h2>
<p>En los tres ejemplos de abajo, la foto se pasó como un enlace https público a una imagen (la
dirección de una imagen ya guardada en Dora). Eso es lo que podemos enseñar que funcionó. No hemos
probado a adjuntar la foto directamente al chat de Claude para esto, así que no decimos si funciona; si
falla, pon la foto en un sitio con enlace público y dale ese enlace a Claude.</p>

<h2>Cómo escribir el movimiento</h2>
<ul>
<li><strong>Parte de lo que hay en la foto.</strong> «La mujer de la foto…» mantiene a la persona;
nombrar objetos que salen en la imagen (el teléfono de pared, la lámpara) le da al movimiento algo con
lo que actuar.</li>
<li><strong>Una acción por vídeo corto.</strong> Descolgar un teléfono cabe en 4 segundos; cruzar una
habitación y saludar necesitó 8.</li>
<li><strong>Di qué hace la cámara.</strong> «Cámara fija» deja el encuadre quieto; «cámara en mano» le
deja moverse y seguir.</li>
<li><strong>Mantén el estilo.</strong> Repite el aspecto de la foto («película cálida de los 80») para
que el vídeo case con ella.</li>
</ul>

<h2>Tres fotos animadas así</h2>
<p>Las tres se hicieron con el conector de Dora usado desde Claude, el 1 y el 2 de noviembre de 2026,
con Seedance 2 Mini, y están guardadas en los registros de Dora con su prompt, sus ajustes y su coste.
Ninguna se hizo para esta página. La mujer no es una persona real: la primera foto se generó con Dora y
las otras dos son versiones de ella. Ninguno de los tres archivos tiene pista de sonido. Pulsa un
fotograma para ver el vídeo.</p>
{_examples("es")}

<h2>Cuánto cuesta</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Modelo de vídeo del conector de Dora</th><th>Monedas</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>Seedance 2 Mini</td><td>31 por 8 s</td><td>El de por defecto; 16 por 4 s a 480p, 66 por 8 s a 720p</td></tr>
<tr><td>Grok Imagine 1.5</td><td>20</td><td>Más barato; una foto como mucho</td></tr>
<tr><td>Kling 2.6 Motion Control</td><td>11 por segundo</td><td>Copia el movimiento de un vídeo que le das en la persona de la foto; mínimo 3 segundos</td></tr>
</tbody>
</table>
</div>
<p>Precios de la lista de modelos del conector de Dora el 2 de noviembre de 2026; más duración, más
resolución y sonido cuestan más ({a(MODELS, "página de modelos de Dora")}). Una moneda sale por unos
0,01 $ en el plan semanal y 0,02 $ en el anual ({a(PRICING, "precios")}). Si antes cambias la foto, como
en los ejemplos 2 y 3, suma la imagen: 10 monedas con Nano Banana 2 (8 cuando se hicieron). Sin monedas
no se genera ni se cobra nada, y si una generación falla, las monedas vuelven.</p>

<h2>Más</h2>
<p>Para vídeos a partir de una descripción en lugar de una foto, y las pruebas cronometradas de Dora,
mira {a(VIDEO_GUIDE, "how to make videos in Claude")} (en inglés). Para imágenes fijas,
<a href="como-hacer-imagenes-con-claude.html">cómo hacer imágenes con Claude</a>. Configuración con un
botón que abre el formulario: {a(DORA_CLAUDE, "Dora para Claude")}. En el iPhone, la misma cuenta y las
mismas monedas sirven en la {a(DORA_STORE, "app de Dora")}.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(HC_IMAGES, "Claude Help Center, Can Claude produce images?")} y {a(HC_CONNECTORS, "Get started with custom connectors using remote MCP")}, comprobados el 2 de noviembre de 2026.</li>
<li>Lista de modelos del conector de Dora y {a(PRICING, "precios")}, leídos el 2 de noviembre de 2026; {a(MODELS, "modelos y costes de Dora")}.</li>
<li>Registros de generación de Dora de los tres vídeos y sus fotos de partida: modelo, ajustes, monedas, prompt y enlace de la foto.</li>
</ul>
<p><strong>Aviso:</strong> Saga Labs, que publica esta web, hace Dora. Las fotos y los vídeos se
hicieron con Dora; los costes son de Dora.</p>
""",
    faq=[
        ("¿Claude puede animar una foto?",
         "Por sí solo, no: Claude no tiene modelo de vídeo. Con un conector de vídeo como Dora, le das la foto y describes "
         "el movimiento, y el conector hace un vídeo corto y te devuelve un enlace."),
        ("¿Cuánto cuesta animar una foto con Claude?",
         "Tu plan de Claude no lo paga. Con Dora, el modelo por defecto, Seedance 2 Mini, cuesta 31 monedas por 8 segundos "
         "y 16 por 4 segundos a 480p, entre unos 0,16 y 0,62 $."),
        ("¿Cómo le paso la foto a Claude?",
         "En nuestros ejemplos, la foto era un enlace https público a la imagen. No hemos probado a adjuntarla directamente "
         "al chat; si falla, usa un enlace público."),
        ("¿Cuánto debe durar el vídeo?",
         "Cuatro segundos bastan para una acción, como descolgar un teléfono; cruzar una habitación y saludar llevó ocho."),
        ("¿El vídeo tiene sonido?",
         "Ninguno de nuestros tres ejemplos tiene pista de sonido. Algunos modelos pueden añadirlo, y cuesta más."),
        ("¿El resultado se ve en el chat?",
         "Los vídeos llegan como un enlace al archivo, no dentro del chat."),
    ],
)

GUIDES = [(BP_EN, BP_ES)]
