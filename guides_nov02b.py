# -*- coding: utf-8 -*-
"""Guia: como hacer imagenes en Claude (EN + ES), plantilla de guides.py.

Datos, todos del 2 nov 2026:
- Claude no genera fotos ni ilustraciones: Claude Help Center 9002504 («Can Claude produce images?», 16 mar 2026);
  diagramas y visuales en HTML y SVG, beta en web y escritorio: Help Center 13979539 (Custom visuals in chat).
- Conectores propios: Help Center 11175166 (Free, Pro, Max, Ultra, Team y Enterprise; Free, uno solo).
- Pasos para anadir Dora: doravideo.com/claude y doravideo.com/blog/how-to-make-videos-in-claude.
- Coste: list_models del conector (Nano Banana 2 paso de 8 a 10 monedas el 2 nov, 13:53 UTC; las 4 del catalogo se cobraron a 8).
  Las 4 imagenes del catalogo de saga-growth (data/generaciones/catalogo.csv, origen claude_mcp) costaron 8 cada una.
- Precio de la moneda: doravideo.com/pricing (ver guides_nov02.py).
No se generan imagenes nuevas. Sin precios de herramientas de terceros. Sin Veo. Aviso de Dora al final. Sin rayas.
"""
from guides_oct24 import (DORA_STORE, a, _human)

ISO = "2026-11-02"
D = _human(ISO)

EN_PATH = "dora/how-to-make-images-in-claude.html"
ES_PATH = "dora/es/como-hacer-imagenes-con-claude.html"

U = "?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=claude_images"
DORA_CLAUDE = "https://doravideo.com/claude" + U
CONNECTORS = "https://doravideo.com/connectors" + U
PRICING = "https://doravideo.com/pricing" + U
VIDEO_GUIDE = "https://doravideo.com/blog/how-to-make-videos-in-claude" + U
HC_IMAGES = "https://support.claude.com/en/articles/9002504-can-claude-produce-images"
HC_VISUALS = "https://support.claude.com/en/articles/13979539-custom-visuals-in-chat"
HC_CONNECTORS = "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp"

IMG = "../images/dora/claude/"
IMG_ES = "../../images/dora/claude/"

# (archivo, ancho, alto, modelo y ajustes EN, ES, prompt exacto, nota EN, nota ES)
SAMPLES = [
    ("app-icon-keyhole.webp", 512, 512, "Nano Banana 2, square, 1K, 8 coins", "Nano Banana 2, cuadrada, 1K, 8 monedas",
     "iOS app icon, flat vector, minimal, centered, no text, no letters. A single rounded photo frame shape with a "
     "keyhole cut out of its center, the keyhole revealing a soft gradient of a landscape behind it. Deep navy background "
     "with a bright cyan and blue gradient inside the photo shape. Clean geometric, high contrast, unmistakable at 60 "
     "pixels, Apple App Store icon style, square, no rounded corner mask.",
     "It followed the brief closely. It is a picture of an icon, not an editable vector file.",
     "Siguió bien el encargo. Es una imagen de un icono, no un archivo vectorial editable."),
    ("sunrise-path-illustration.webp", 424, 760, "Nano Banana 2, vertical 9:16, 2K, 8 coins", "Nano Banana 2, vertical 9:16, 2K, 8 monedas",
     "Vertical background illustration for an App Store screenshot of a calm meditation app about building a daily "
     "habit, soft painterly premium style like Calm/Headspace: a gentle sunrise over soft rolling hills with a winding "
     "stone path made of small round stepping stones, a few small flowers, soft peach and warm light blending into teal "
     "and aqua (#7FD3C9). The TOP 35% is an almost empty pale sunrise sky reserved for a headline. The center is calm and "
     "low-detail (a phone mockup goes on top); detail on the edges and the bottom. No text, no letters, no logos, no "
     "phone, no people.",
     "The empty sky at the top and the quiet centre came out as asked, ready for a headline and a phone on top.",
     "El cielo vacío arriba y el centro tranquilo salieron como se pidió, listos para un titular y un móvil encima."),
    ("vanity-flatlay.webp", 424, 760, "Nano Banana 2, vertical 9:16, 1K, 8 coins", "Nano Banana 2, vertical 9:16, 1K, 8 monedas",
     "Aesthetic vertical flatlay shot from directly above, luxury beauty vanity on white marble: elegant unbranded "
     "skincare bottles, a gold compact, a crystal perfume, pearl earrings, fresh peonies and a silk ribbon, soft morning "
     "window light, gold accents, clean rich beauty aesthetic, subtle film grain, editorial. No text, no watermark, no logos.",
     "Every object in the list is there, with blank labels and no logos.",
     "Están todos los objetos de la lista, con etiquetas en blanco y sin logos."),
    ("quill-parchment.webp", 424, 760, "Nano Banana 2, vertical 9:16, 1K, 8 coins", "Nano Banana 2, vertical 9:16, 1K, 8 monedas",
     "Extreme close-up macro insert of a hand holding a sharpened goose-quill writing Latin court records on aged cream "
     "parchment by candlelight. The parchment shows gothic Latin script in dark brown ink, and in the lower-right margin a "
     "tiny faint pencil-and-ink sketch of a pig is visible. Beside the parchment on the wooden writing desk: a small clay "
     "inkwell with dark ink, a red wax seal stamp, a few loose quills. Warm candle glow from the upper left, a single "
     "candle flame visible at the edge of frame creating soft golden light, shallow depth of field with the script in "
     "sharp focus. Photorealistic, cinematic, 35mm macro lens, vertical 9:16, no anachronisms, no modern objects.",
     "Not everything came out: the pig sketch in the margin is missing, the quill has a metal nib, and the candle "
     "flame is not in the frame. Long prompts with many small details lose some of them.",
     "No salió todo: falta el cerdito del margen, la pluma tiene plumín de metal y la llama de la vela no se ve. "
     "En un prompt largo con muchos detalles pequeños, algunos se pierden."),
]


def _figures(lang):
    base = IMG if lang == "en" else IMG_ES
    out = []
    for f, w, h, en, es, prompt, n_en, n_es in SAMPLES:
        alt = prompt.split(".")[0] if lang == "en" else prompt.split(".")[0]
        out.append(
            '<figure style="margin:28px 0">\n'
            '<img src="%s%s" width="%d" height="%d" loading="lazy" alt="%s" '
            'style="display:block;width:100%%;max-width:%dpx;height:auto;border-radius:8px">\n'
            '<figcaption><strong>%s.</strong> %s</figcaption>\n'
            '</figure>\n<p><strong>%s</strong></p>\n<blockquote>%s</blockquote>\n'
            % (base, f, w, h, alt.replace('"', "'"), 300 if w == h else 280,
               en if lang == "en" else es, n_en if lang == "en" else n_es,
               "Exact prompt:" if lang == "en" else "Prompt exacto (en inglés, tal cual):", prompt))
    return "".join(out)


# --------------------------------------------------------------------------
BP_EN = dict(
    path=EN_PATH,
    app_name="Dora",
    date_iso=ISO, date=D,
    h1="How to make images in Claude (2026)",
    desc=("Can Claude make images? Not by itself. With an image connector it can: how to add one, what to ask, what it "
          "costs per image, four real results with their exact prompts, and the options without a connector."),
    section="Guides", kicker="How to",
    standfirst=("Claude does not generate photos or illustrations on its own. Add an image connector and you can ask "
                "for them in a normal chat. Here is how, what it costs, and four images made that way, with the exact "
                "prompts."),
    tools=["Claude", "Dora connector"],
    intro=f"""
<p><strong>Short answer:</strong> Claude cannot make a photo or an illustration by itself; Anthropic's
help center says so ({a(HC_IMAGES, "Can Claude produce images?")}). It can draw diagrams and charts in
code, and it can ask an image service to make a picture through a connector. This page uses Dora's
connector, because we have checked it and can show what it made. The default image model, Nano
Banana 2, costs 10 coins an image, roughly $0.10 to $0.20, paid with Dora coins, not your Claude
plan.</p>

<h2>Three ways to get an image out of Claude</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Way</th><th>What you get</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>An image connector</td><td>A real picture (photo-like or illustrated) shown in the chat</td><td>Illustrations, product shots, icons, backgrounds, edits of your photo</td></tr>
<tr><td>Claude draws in code</td><td>SVG or HTML: diagrams, charts, simple shapes</td><td>Diagrams, charts, flat graphics you can edit</td></tr>
<tr><td>Claude writes the prompt</td><td>Text you paste into another image tool</td><td>When you already use another image tool</td></tr>
</tbody>
</table>
</div>

<h2>Before you start</h2>
<ul>
<li><strong>A Claude plan with custom connectors.</strong> Anthropic lists Free, Pro, Max, Ultra, Team
and Enterprise; Free is limited to one custom connector ({a(HC_CONNECTORS, "Claude Help Center")}).</li>
<li><strong>A Dora account with coins.</strong> You can create it when Claude asks you to sign in.
Coins come from a plan or a pack ({a(PRICING, "pricing")}).</li>
</ul>
""",
    steps=[
        ("Open the connector form.",
         "In Claude, go to Customize, then Connectors, click + Add and choose Add custom connector. The button on "
         "Dora's Claude page opens the same form and copies the address."),
        ("Paste the address.",
         "Name it Dora, paste https://doravideo.com/mcp, click Continue, leave the sign-in settings as they are and click Add."),
        ("Sign in.",
         "Sign in to Dora with Apple, Google or email. If you already use Dora, use the same account."),
        ("Switch it on in a chat.",
         "In a chat, click +, open Connectors and check that Dora is on."),
        ("Ask for the image.",
         "Describe it in normal words, with the shape you want (square, vertical or horizontal). Add “tell me the cost "
         "first and wait for my confirmation” if you want to approve it before it is made."),
    ],
    after=f"""
<p>On Team and Enterprise plans an Owner adds the connector for the organisation and each member
connects it. Full setup, with a button that opens the form: {a(DORA_CLAUDE, "Dora for Claude")}; other
assistants: {a(CONNECTORS, "Dora connectors")}.</p>

<h2>What to ask for</h2>
<ul>
<li><strong>Say what it is for.</strong> “An app icon”, “a background for an App Store screenshot with
room for a headline at the top”, “a product shot from above”. The use decides the shape and the empty
space.</li>
<li><strong>Name the shape.</strong> Square for icons and posts, vertical 9:16 for stories and phone
screens, horizontal for web headers.</li>
<li><strong>Say what you do not want.</strong> “No text, no logos, no people” keeps stray letters and
brand marks out.</li>
<li><strong>Keep the details few.</strong> In our longest prompt below, three small details were lost.</li>
<li><strong>Starting from your own photo:</strong> give Claude a public https link to it. Dora's guide
tested links; attaching a photo to the chat was not tested there.</li>
</ul>

<h2>Four images made this way, with the exact prompts</h2>
<p>These came from Dora's connector called from Claude, between June and October 2026, and are kept
in Dora's records with their prompt and cost. None was made for this page. We picked them to show
different uses, including one where the model missed part of the prompt.</p>
{_figures("en")}

<h2>What it costs</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Image model in Dora's connector</th><th>Coins</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Z-Image</td><td>1</td><td>Cheapest, from text only</td></tr>
<tr><td>Nano Banana</td><td>4</td><td>Also edits a reference photo at the same price</td></tr>
<tr><td>GPT Image 2</td><td>6</td><td>OpenAI's image model</td></tr>
<tr><td>Nano Banana 2</td><td>10</td><td>The default; can take a reference photo; more at higher resolution</td></tr>
<tr><td>Nano Banana Pro</td><td>18</td><td>Best at keeping a face from a photo; 24 at 4K</td></tr>
</tbody>
</table>
</div>
<p>A coin costs about $0.01 on Dora's weekly plan and about $0.02 on the yearly one
({a(PRICING, "pricing")}, 2 November 2026), so a default image is roughly $0.10 to $0.20. The four
images above were charged 8 coins each, the price before 2 November. With no coins, nothing is made and nothing is charged; if a
generation fails, the coins go back. For the same costs in ChatGPT, see
<a href="chatgpt-video-generator-cost.html">ChatGPT video generator cost</a>.</p>

<h2>Without a connector</h2>
<h3>Let Claude draw it in code</h3>
<p>Claude can build diagrams, charts and interactive visuals in HTML and SVG right in the chat, and
adjust them when you ask (a beta on Claude web and desktop, per {a(HC_VISUALS, "Anthropic")}). Ask for
“an SVG of…” when you want a flowchart, a chart, a simple logo shape or a flat illustration you can
edit. It will not look like a photo.</p>
<h3>Let Claude write the prompt</h3>
<p>Describe the image you want and ask Claude for a detailed prompt for the image tool you already
use, with the shape, the light, what to leave out and where to keep empty space. Then paste it there.
Prices are that tool's.</p>

<h2>Videos too</h2>
<p>The same connector makes videos; they come back as a link rather than inside the chat. The default
video model is Seedance 2 Mini. Steps, real tests and costs: {a(VIDEO_GUIDE, "how to make videos in Claude")}.
On iPhone, the same account and coins work in the {a(DORA_STORE, "Dora app")}.</p>

<h2>Sources</h2>
<ul>
<li>{a(HC_IMAGES, "Claude Help Center, Can Claude produce images?")} and {a(HC_VISUALS, "Custom visuals in chat")}, checked 2 November 2026.</li>
<li>{a(HC_CONNECTORS, "Claude Help Center, Get started with custom connectors using remote MCP")}, checked 2 November 2026.</li>
<li>{a(DORA_CLAUDE, "Dora for Claude")}, {a(PRICING, "Dora pricing")} and Dora's connector model list, read on 2 November 2026.</li>
<li>Dora's generation records for the four images: model, settings, coins and prompt.</li>
</ul>
<p><strong>Disclosure:</strong> Saga Labs, which publishes this site, makes Dora. The four images were
made with Dora; costs are Dora's own, read on 2 November 2026.</p>
""",
    faq=[
        ("Can Claude make images?",
         "Not by itself: Anthropic's help center says Claude does not generate photos or illustrations the way image "
         "tools do. It can draw diagrams and charts in HTML and SVG, and with an image connector such as Dora it can ask "
         "an image service to make a picture and show it in the chat."),
        ("Is there a Claude AI image generator?",
         "Not built in. You add one as a connector under Customize, then Connectors, Add custom connector. With Dora the "
         "address is https://doravideo.com/mcp."),
        ("How much does an image in Claude cost?",
         "Your Claude plan does not pay for it. With Dora the default image model, Nano Banana 2, is 10 coins, "
         "roughly $0.10 to $0.20; the cheapest model is 1 coin."),
        ("Does it work on the free Claude plan?",
         "Anthropic lists custom connectors on Free, limited to one. You still need coins in your Dora account."),
        ("Can Claude make an SVG?",
         "Yes. Ask for an SVG and Claude writes it in the chat; it suits diagrams, charts, icons and flat shapes, not photos."),
        ("Can I edit my own photo?",
         "Give Claude a public https link to the photo and say what to change. Dora's guide tested links; attaching a "
         "photo to the chat was not tested."),
    ],
)

# --------------------------------------------------------------------------
BP_ES = dict(
    path=ES_PATH,
    app_name="Dora",
    date_iso=ISO, date=D,
    h1="Cómo hacer imágenes con Claude (2026)",
    desc=("¿Claude puede crear imágenes? Por sí solo, no. Con un conector de imágenes, sí: cómo se añade, qué pedir, "
          "cuánto cuesta cada imagen, cuatro resultados reales con su prompt exacto y las opciones sin conector."),
    section="Guías", kicker="Cómo se hace",
    standfirst=("Claude no genera fotos ni ilustraciones por sí solo. Con un conector de imágenes se las puedes pedir "
                "en un chat normal. Aquí va cómo, cuánto cuesta y cuatro imágenes hechas así, con el prompt exacto."),
    tools=["Claude", "conector de Dora"],
    intro=f"""
<p><strong>En corto:</strong> Claude no puede hacer una foto ni una ilustración por sí solo; lo dice el
centro de ayuda de Anthropic ({a(HC_IMAGES, "Can Claude produce images?")}). Puede dibujar diagramas y
gráficos con código, y puede pedirle una imagen a un servicio a través de un conector. Esta página usa
el conector de Dora, porque lo hemos comprobado y podemos enseñar lo que hizo. El modelo de imagen por
defecto, Nano Banana 2, cuesta 10 monedas por imagen, entre 0,10 y 0,20 $, que se pagan con
monedas de Dora, no con tu plan de Claude.</p>

<h2>Tres formas de sacar una imagen de Claude</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Forma</th><th>Qué obtienes</th><th>Sirve para</th></tr></thead>
<tbody>
<tr><td>Un conector de imágenes</td><td>Una imagen de verdad (tipo foto o ilustración) que se ve en el chat</td><td>Ilustraciones, fotos de producto, iconos, fondos, retocar tu foto</td></tr>
<tr><td>Claude dibuja con código</td><td>SVG o HTML: diagramas, gráficos, formas sencillas</td><td>Diagramas, gráficos, dibujos planos que puedes editar</td></tr>
<tr><td>Claude escribe el prompt</td><td>Un texto que pegas en otra herramienta de imágenes</td><td>Si ya usas otra herramienta de imágenes</td></tr>
</tbody>
</table>
</div>

<h2>Antes de empezar</h2>
<ul>
<li><strong>Un plan de Claude con conectores propios.</strong> Anthropic cita Free, Pro, Max, Ultra,
Team y Enterprise; en Free, uno solo ({a(HC_CONNECTORS, "Claude Help Center")}).</li>
<li><strong>Una cuenta de Dora con monedas.</strong> Puedes crearla cuando Claude te pida entrar. Las
monedas vienen de un plan o de un paquete ({a(PRICING, "precios")}).</li>
</ul>
""",
    steps=[
        ("Abre el formulario del conector.",
         "En Claude, ve a Customize, luego Connectors, pulsa + Add y elige Add custom connector. El botón de la página "
         "de Dora para Claude abre el mismo formulario y copia la dirección."),
        ("Pega la dirección.",
         "Ponle de nombre Dora, pega https://doravideo.com/mcp, pulsa Continue, deja los ajustes de acceso como están y pulsa Add."),
        ("Entra en tu cuenta.",
         "Entra en Dora con Apple, Google o correo. Si ya usas Dora, con la misma cuenta."),
        ("Actívalo en un chat.",
         "En un chat, pulsa +, abre Connectors y comprueba que Dora está activado."),
        ("Pide la imagen.",
         "Descríbela con palabras normales y di la forma (cuadrada, vertical u horizontal). Añade «dime antes lo que "
         "cuesta y espera a que lo confirme» si quieres aprobarlo antes."),
    ],
    after=f"""
<p>En los planes Team y Enterprise, un Owner añade el conector para la organización y cada miembro lo
conecta. Todos los pasos, con un botón que abre el formulario: {a(DORA_CLAUDE, "Dora para Claude")};
otros asistentes: {a(CONNECTORS, "conectores de Dora")}.</p>

<h2>Qué pedir</h2>
<ul>
<li><strong>Di para qué es.</strong> «Un icono de app», «un fondo para una captura del App Store con
sitio para un titular arriba», «una foto de producto desde arriba». El uso decide la forma y el
espacio vacío.</li>
<li><strong>Di la forma.</strong> Cuadrada para iconos y publicaciones, vertical 9:16 para historias y
pantallas de móvil, horizontal para cabeceras de web.</li>
<li><strong>Di lo que no quieres.</strong> «Sin texto, sin logos, sin personas» evita letras sueltas y
marcas.</li>
<li><strong>Pocos detalles.</strong> En el prompt más largo de abajo se perdieron tres detalles pequeños.</li>
<li><strong>Si partes de tu foto:</strong> dale a Claude un enlace https público. La guía de Dora probó
enlaces; adjuntar la foto al chat no se probó.</li>
</ul>

<h2>Cuatro imágenes hechas así, con el prompt exacto</h2>
<p>Salieron del conector de Dora usado desde Claude, entre junio y octubre de 2026, y están guardadas
en los registros de Dora con su prompt y su coste. Ninguna se hizo para esta página. Las elegimos para
enseñar usos distintos, incluida una en la que el modelo no hizo parte de lo que se pedía.</p>
{_figures("es")}

<h2>Cuánto cuesta</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Modelo de imagen del conector de Dora</th><th>Monedas</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>Z-Image</td><td>1</td><td>El más barato, solo desde texto</td></tr>
<tr><td>Nano Banana</td><td>4</td><td>También retoca una foto de referencia, al mismo precio</td></tr>
<tr><td>GPT Image 2</td><td>6</td><td>El modelo de imagen de OpenAI</td></tr>
<tr><td>Nano Banana 2</td><td>10</td><td>El de por defecto; admite una foto de referencia; más a más resolución</td></tr>
<tr><td>Nano Banana Pro</td><td>18</td><td>El que mejor conserva una cara de la foto; 24 en 4K</td></tr>
</tbody>
</table>
</div>
<p>Una moneda sale por unos 0,01 $ en el plan semanal de Dora y unos 0,02 $ en el anual
({a(PRICING, "precios")}, 2 de noviembre de 2026), así que una imagen por defecto cuesta entre 0,10 y
0,20 $. Las cuatro imágenes de arriba se cobraron a 8 monedas cada una, el precio de antes del 2 de noviembre. Sin monedas no se genera ni se
cobra nada; si una generación falla, las monedas vuelven. Para los mismos costes en ChatGPT, mira
<a href="cuanto-cuesta-generar-video-con-chatgpt.html">cuánto cuesta generar un vídeo con ChatGPT</a>.</p>

<h2>Sin conector</h2>
<h3>Que Claude lo dibuje con código</h3>
<p>Claude puede hacer diagramas, gráficos y visuales interactivos en HTML y SVG dentro del chat, y
cambiarlos cuando se lo pides (en beta en Claude web y escritorio, según {a(HC_VISUALS, "Anthropic")}).
Pide «un SVG de…» cuando quieras un diagrama de flujo, un gráfico, la forma de un logo sencillo o una
ilustración plana que puedas editar. No parecerá una foto.</p>
<h3>Que Claude escriba el prompt</h3>
<p>Describe la imagen y pídele a Claude un prompt detallado para la herramienta de imágenes que ya
uses, con la forma, la luz, lo que no debe salir y dónde dejar espacio vacío. Luego pégalo allí. Los
precios son los de esa herramienta.</p>

<h2>También vídeos</h2>
<p>El mismo conector hace vídeos; llegan como un enlace, no dentro del chat. El modelo de vídeo por
defecto es Seedance 2 Mini. Pasos, pruebas reales y costes, en inglés:
{a(VIDEO_GUIDE, "how to make videos in Claude")}. En el iPhone, la misma cuenta y las mismas monedas
sirven en la {a(DORA_STORE, "app de Dora")}.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(HC_IMAGES, "Claude Help Center, Can Claude produce images?")} y {a(HC_VISUALS, "Custom visuals in chat")}, comprobados el 2 de noviembre de 2026.</li>
<li>{a(HC_CONNECTORS, "Claude Help Center, Get started with custom connectors using remote MCP")}, comprobado el 2 de noviembre de 2026.</li>
<li>{a(DORA_CLAUDE, "Dora para Claude")}, {a(PRICING, "precios de Dora")} y la lista de modelos del conector de Dora, leídos el 2 de noviembre de 2026.</li>
<li>Registros de generación de Dora de las cuatro imágenes: modelo, ajustes, monedas y prompt.</li>
</ul>
<p><strong>Aviso:</strong> Saga Labs, que publica esta web, hace Dora. Las cuatro imágenes se hicieron
con Dora; los costes son de Dora, leídos el 2 de noviembre de 2026.</p>
""",
    faq=[
        ("¿Claude puede crear imágenes?",
         "Por sí solo, no: el centro de ayuda de Anthropic dice que Claude no genera fotos ni ilustraciones como las "
         "herramientas de imágenes. Puede dibujar diagramas y gráficos en HTML y SVG, y con un conector de imágenes como "
         "Dora puede pedirle la imagen a un servicio y enseñarla en el chat."),
        ("¿Claude tiene un generador de imágenes?",
         "No viene incluido. Se añade como conector en Customize, Connectors, Add custom connector. Con Dora, la dirección "
         "es https://doravideo.com/mcp."),
        ("¿Cuánto cuesta una imagen en Claude?",
         "Tu plan de Claude no la paga. Con Dora, el modelo de imagen por defecto, Nano Banana 2, cuesta 10 monedas, "
         "entre 0,10 y 0,20 $; el más barato, 1 moneda."),
        ("¿Funciona con el plan gratis de Claude?",
         "Anthropic incluye los conectores propios en Free, con uno solo. Necesitas igualmente monedas en tu cuenta de Dora."),
        ("¿Claude puede hacer un SVG?",
         "Sí. Pídele un SVG y Claude lo escribe en el chat; sirve para diagramas, gráficos, iconos y formas planas, no para fotos."),
        ("¿Puedo retocar una foto mía?",
         "Dale a Claude un enlace https público a la foto y di qué cambiar. La guía de Dora probó enlaces; adjuntar la "
         "foto al chat no se probó."),
    ],
)

GUIDES = [(BP_EN, BP_ES)]
