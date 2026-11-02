# -*- coding: utf-8 -*-
"""Guia: cuanto cuesta un video o una imagen desde ChatGPT, modelo a modelo (EN + ES), plantilla de guides.py.

Datos, todos del 2 nov 2026:
- Coste en monedas por modelo: respuesta de list_models del conector de Dora (lo que ve ChatGPT), 12 modelos tras quitar Veo.
- Configuraciones concretas: doravideo.com/chatgpt (Grok Imagine 1.5 4 s 480p = 10; Seedance 2 Mini 4 s 480p = 16;
  Veo 3 salio del conector a las 11:11 UTC del 2 nov, issue #114 de ios-playbook) y doravideo.com/models (Seedance 2 Mini 31 para 8 s y 66 para 8 s a 720p;
  SeeDance 2 328 para 8 s a 720p).
- Precio de la moneda: doravideo.com/pricing (Annual Pro 119,99 $ con 500 monedas al mes, 6.000 al ano; Weekly Pro
  1,99 $ la primera semana con 300 monedas, luego 4,99 $ con 500 a la semana; recargas desde 3,99 $ para Pro, sin
  caducidad). Cuantas monedas trae cada recarga no se dice en la pagina: no se pone.
- Sin monedas: doravideo.com/chatgpt y doravideo.com/blog/dora-ai-video-chatgpt-plugin. Si falla la generacion, las
  monedas se devuelven: functions/src/mcp/errors.js y tools.js del repo de Dora (refundCredits).
- De los otros plugins no se dan precios: no se han comprobado para esta pagina.
El aviso de que Dora es nuestra va al final (norma de aisagalab.com del 2 nov). Sin rayas.
"""
from guides_oct24 import (CHATGPT_APP, DORA_STORE, PLUGINS, a, _human)

ISO = "2026-11-02"
D = _human(ISO)

EN_PATH = "dora/chatgpt-video-generator-cost.html"
ES_PATH = "dora/es/cuanto-cuesta-generar-video-con-chatgpt.html"

U = "?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=chatgpt_cost"
PRICING = "https://doravideo.com/pricing" + U
MODELS = "https://doravideo.com/models" + U
DORA_GPT = "https://doravideo.com/chatgpt" + U
NO_COINS = "https://doravideo.com/blog/dora-ai-video-chatgpt-plugin" + U

# --------------------------------------------------------------------------
BP_EN = dict(
    path=EN_PATH,
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="ChatGPT video generator cost: what a video or image really costs, model by model",
    desc=("What it costs to make a video or an image from ChatGPT with the Dora AI Video plugin, model by model: "
          "coins per clip from 1 to 76, the price of a coin on each plan, and what happens with no coins or a failed clip. "
          "Checked 2 November 2026."),
    section="Guides", kicker="Prices",
    standfirst=("ChatGPT has no video model of its own since Sora closed, so a video made in a chat is paid to the "
                "plugin that makes it, not to OpenAI. Here is what that costs with Dora AI Video, model by model, "
                "with the numbers read on 2 November 2026."),
    tools=["ChatGPT", "Dora AI Video plugin"],
    intro=f"""
<p><strong>Short answer:</strong> with the {a(CHATGPT_APP, "Dora AI Video")} plugin, an image costs
1 to 18 coins and a video 15 to 76 coins at the default settings. A coin costs about 1 cent on the
weekly plan and 2 cents on the yearly one, so a default video (Seedance 2 Mini, 31 coins) is about
$0.31 to $0.62, and the priciest default (Seedance 2, 76 coins) about $0.76 to $1.52. Your ChatGPT
plan pays for none of it.</p>

<h2>Who you pay when ChatGPT makes a video</h2>
<p>OpenAI closed the Sora app in April 2026 and its API in September 2026, so ChatGPT itself no
longer makes video. Video in a chat comes from a plugin in ChatGPT Plugins, and each plugin bills on
your account with its own service, in its own credits. That is why the question “how much does a
ChatGPT video cost” has no single answer: it depends on the plugin and on the model it uses. This
page gives the numbers for one plugin, Dora AI Video, because they are public and we could read
them on the same day. For what the other video plugins do, see
<a href="best-chatgpt-plugins-video-images-2026.html">the best ChatGPT plugins for video and images</a>;
we have not checked their prices for this page.</p>

<h2>Cost per model, in coins and dollars</h2>
<p>These are the starting costs Dora's plugin gives ChatGPT when it lists its models (12 of them,
6 for video and 6 for images). Dollars use the coin price of each plan below: about $0.01 a coin
weekly, $0.02 yearly.</p>

<div class="table-scroll">
<table>
<thead><tr><th>Model</th><th>Makes</th><th>Coins</th><th>About, in dollars</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Z-Image</td><td>Image</td><td>1</td><td>$0.01 to $0.02</td><td>Cheapest image, text only</td></tr>
<tr><td>Nano Banana</td><td>Image</td><td>4</td><td>$0.04 to $0.08</td><td>Also an edit version from a reference photo, same price</td></tr>
<tr><td>GPT Image 2</td><td>Image</td><td>6</td><td>$0.06 to $0.12</td><td>OpenAI's image model, flat price</td></tr>
<tr><td>Nano Banana 2</td><td>Image</td><td>8</td><td>$0.08 to $0.16</td><td>Default image model; can take a reference photo; Dora's models page lists 10 coins; more at higher resolution</td></tr>
<tr><td>Nano Banana Pro</td><td>Image</td><td>18</td><td>$0.18 to $0.36</td><td>Best at keeping a face from a photo; 24 coins at 4K</td></tr>
<tr><td>Grok Imagine</td><td>Video</td><td>15</td><td>$0.15 to $0.30</td><td>From text or from an image, up to 15 s</td></tr>
<tr><td>Grok Imagine 1.5</td><td>Video</td><td>20</td><td>$0.20 to $0.40</td><td>With sound; 10 coins for 4 s at 480p</td></tr>
<tr><td>Seedance 2 Mini</td><td>Video</td><td>31</td><td>$0.31 to $0.62</td><td>Default video model; 16 coins for 4 s at 480p, 66 for 8 s at 720p</td></tr>
<tr><td>Kling 2.6 Motion Control</td><td>Video</td><td>55</td><td>$0.55 to $1.10</td><td>Moves the person in a photo like a video you give it; 11 coins per second of that video, 3 s minimum</td></tr>
<tr><td>Seedance 2</td><td>Video</td><td>76</td><td>$0.76 to $1.52</td><td>Highest quality; 328 coins for 8 s at 720p</td></tr>
</tbody>
</table>
</div>

<p>The coins column is a starting price. Longer clips, higher resolution and sound cost more, which
is why Seedance 2 Mini goes from 16 coins (4 seconds, 480p) to 66 (8 seconds, 720p). Dora's
{a(MODELS, "models page")} lists the price of each configuration; Dora's app and website also have
models that the ChatGPT plugin does not offer.</p>

<h2>What a coin costs</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Plan</th><th>Price</th><th>Coins</th><th>Per coin</th></tr></thead>
<tbody>
<tr><td>Weekly Pro, first week</td><td>$1.99</td><td>300</td><td>about $0.007</td></tr>
<tr><td>Weekly Pro, after that</td><td>$4.99 a week</td><td>500 a week</td><td>about $0.01</td></tr>
<tr><td>Annual Pro</td><td>$119.99 a year</td><td>500 a month, 6,000 a year</td><td>about $0.02</td></tr>
<tr><td>Extra credits</td><td>from $3.99</td><td>not stated on the page</td><td>not known</td></tr>
</tbody>
</table>
</div>
<p>Prices in US dollars from {a(PRICING, "Dora's pricing page")} on 2 November 2026; they can differ
by country and change. The weekly plan gives more coins per dollar; the yearly one costs less per
month ($10). Extra credits are for Pro members and do not expire.</p>

<h2>What a plan buys, in clips</h2>
<ul>
<li>500 coins (one week weekly, or one month yearly): about 16 default videos (Seedance 2 Mini, 31
coins), 25 Grok Imagine 1.5 clips or 62 default images (Nano Banana 2, 8 coins).</li>
<li>The first week's 300 coins: about 9 default videos or 37 default images.</li>
</ul>
<p>These are at the default settings. Longer or sharper clips use more coins each.</p>

<h2>No coins, or a clip that fails</h2>
<ul>
<li><strong>No coins:</strong> nothing is made and nothing is charged. ChatGPT says that generating
needs coins and links to the page with your balance and the plans; once you have coins, ask again
in the same chat ({a(NO_COINS, "Dora's plugin guide")}).</li>
<li><strong>A clip that fails:</strong> the coins go back to your balance, and the plugin tells
ChatGPT the generation failed and the credits were refunded.</li>
<li><strong>Coins and credits</strong> are the same thing; Dora's pages use both words.</li>
</ul>
""",
    steps=[
        ("Add the plugin.",
         "In ChatGPT, open Plugins, search for Dora AI Video, install it and sign in with a Dora account (Apple, Google or email)."),
        ("Ask for the prices first.",
         "Write “list Dora's models and what each costs in coins”. ChatGPT reads the list from the plugin."),
        ("Ask for the clip and a quote.",
         "Describe the video and add “tell me the cost first and wait for my confirmation”. ChatGPT proposes a model, "
         "length and resolution with its cost."),
        ("Confirm.",
         "Say yes, or ask for a cheaper model or a shorter clip. ChatGPT returns the file and what it cost in coins."),
    ],
    after=f"""
<p>For the whole process from the first prompt, see
<a href="how-to-make-a-video-with-chatgpt.html">how to make a video with ChatGPT</a>. On iPhone, the
same account and coins work in the {a(DORA_STORE, "Dora app")}.</p>

<h2>Sources</h2>
<ul>
<li>Dora plugin model list, as ChatGPT receives it, read on 2 November 2026.</li>
<li>{a(PRICING, "Dora pricing")}, {a(MODELS, "Dora models and costs")} and {a(DORA_GPT, "Dora for ChatGPT")}, read on 2 November 2026.</li>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT and Codex")}: how plugins are installed and what limits availability.</li>
<li>{a(CHATGPT_APP, "Dora AI Video in ChatGPT Plugins")}.</li>
</ul>
<p><strong>Disclosure:</strong> Saga Labs, which publishes this site, makes Dora AI Video. All prices on
this page are Dora's own, read from its pages and its plugin on 2 November 2026.</p>
""",
    faq=[
        ("How much does it cost to make a video with ChatGPT?",
         "ChatGPT does not charge for it: the plugin that makes the video does. With Dora AI Video a video costs "
         "15 to 76 coins at the default settings, about $0.15 to $1.52; the default model, Seedance 2 Mini, is 31 "
         "coins (about $0.31 to $0.62). Longer, sharper clips and sound cost more."),
        ("Does ChatGPT Plus pay for videos made with a plugin?",
         "No. The video is made by the plugin's service and paid with your account there, not with your ChatGPT plan."),
        ("What is the cheapest video I can make from ChatGPT with Dora?",
         "Grok Imagine 1.5 at 4 seconds and 480p, 10 coins, about $0.10 to $0.20."),
        ("How much is an image?",
         "1 to 18 coins: Z-Image 1, Nano Banana 4, GPT Image 2 6, Nano Banana 2 (the default) 8 and Nano Banana Pro 18."),
        ("What happens if I have no coins?",
         "Nothing is made and nothing is charged. ChatGPT tells you that generating needs coins and links to your "
         "balance and the plans."),
        ("Do I lose coins if a video fails?",
         "No. If the generation fails, the coins go back to your balance."),
    ],
)

# --------------------------------------------------------------------------
BP_ES = dict(
    path=ES_PATH,
    app_name="Dora AI Video",
    date_iso=ISO, date=D,
    h1="Cuánto cuesta generar un vídeo o una imagen con ChatGPT, modelo a modelo",
    desc=("Lo que cuesta hacer un vídeo o una imagen desde ChatGPT con el plugin Dora AI Video, modelo a modelo: "
          "de 1 a 76 monedas, el precio de la moneda en cada plan y qué pasa si no tienes monedas o si falla. "
          "Comprobado el 2 de noviembre de 2026."),
    section="Guías", kicker="Precios",
    standfirst=("ChatGPT no tiene modelo de vídeo propio desde que cerró Sora, así que un vídeo hecho en un chat lo "
                "cobra el plugin que lo hace, no OpenAI. Esto es lo que cuesta con Dora AI Video, modelo a modelo, "
                "con los datos del 2 de noviembre de 2026."),
    tools=["ChatGPT", "plugin Dora AI Video"],
    intro=f"""
<p><strong>En corto:</strong> con el plugin {a(CHATGPT_APP, "Dora AI Video")}, una imagen cuesta de 1
a 18 monedas y un vídeo de 15 a 76 con los ajustes por defecto. Una moneda sale por unos 0,01 $ en
el plan semanal y 0,02 $ en el anual, así que un vídeo por defecto (Seedance 2 Mini, 31 monedas)
cuesta entre 0,31 y 0,62 $, y el más caro por defecto (Seedance 2, 76 monedas) entre 0,76 y 1,52 $.
Tu plan de ChatGPT no paga nada de esto.</p>

<h2>A quién pagas cuando ChatGPT hace un vídeo</h2>
<p>OpenAI cerró la app de Sora en abril de 2026 y su API en septiembre, así que ChatGPT ya no hace
vídeo por sí mismo. El vídeo en un chat sale de un plugin de ChatGPT Plugins, y cada plugin cobra en
tu cuenta con su servicio y con sus propios créditos. Por eso «cuánto cuesta un vídeo de ChatGPT» no
tiene una sola respuesta: depende del plugin y del modelo que use. Aquí van las cifras de un plugin,
Dora AI Video, porque son públicas y las pudimos leer el mismo día. Para lo que hacen los demás
plugins de vídeo, mira <a href="mejores-plugins-chatgpt-video-imagenes-2026.html">los mejores plugins
de ChatGPT para vídeo e imágenes</a>; sus precios no los hemos comprobado para esta página.</p>

<h2>Coste por modelo, en monedas y en dólares</h2>
<p>Son los costes de partida que el plugin de Dora da a ChatGPT cuando le pasa la lista de modelos
(12: 6 de vídeo y 6 de imagen). Los dólares salen del precio de la moneda en cada plan, más abajo:
unos 0,01 $ la moneda en el semanal y 0,02 $ en el anual.</p>

<div class="table-scroll">
<table>
<thead><tr><th>Modelo</th><th>Hace</th><th>Monedas</th><th>Aprox. en dólares</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>Z-Image</td><td>Imagen</td><td>1</td><td>0,01 a 0,02 $</td><td>La imagen más barata, solo desde texto</td></tr>
<tr><td>Nano Banana</td><td>Imagen</td><td>4</td><td>0,04 a 0,08 $</td><td>También edita a partir de una foto, al mismo precio</td></tr>
<tr><td>GPT Image 2</td><td>Imagen</td><td>6</td><td>0,06 a 0,12 $</td><td>El modelo de imagen de OpenAI, precio fijo</td></tr>
<tr><td>Nano Banana 2</td><td>Imagen</td><td>8</td><td>0,08 a 0,16 $</td><td>Modelo de imagen por defecto; admite una foto de referencia; la página de modelos de Dora dice 10 monedas; más a más resolución</td></tr>
<tr><td>Nano Banana Pro</td><td>Imagen</td><td>18</td><td>0,18 a 0,36 $</td><td>El que mejor conserva una cara de la foto; 24 monedas en 4K</td></tr>
<tr><td>Grok Imagine</td><td>Vídeo</td><td>15</td><td>0,15 a 0,30 $</td><td>Desde texto o desde una imagen, hasta 15 s</td></tr>
<tr><td>Grok Imagine 1.5</td><td>Vídeo</td><td>20</td><td>0,20 a 0,40 $</td><td>Con sonido; 10 monedas por 4 s a 480p</td></tr>
<tr><td>Seedance 2 Mini</td><td>Vídeo</td><td>31</td><td>0,31 a 0,62 $</td><td>Modelo de vídeo por defecto; 16 monedas por 4 s a 480p, 66 por 8 s a 720p</td></tr>
<tr><td>Kling 2.6 Motion Control</td><td>Vídeo</td><td>55</td><td>0,55 a 1,10 $</td><td>Mueve a la persona de una foto como en un vídeo que le das; 11 monedas por segundo de ese vídeo, mínimo 3 s</td></tr>
<tr><td>Seedance 2</td><td>Vídeo</td><td>76</td><td>0,76 a 1,52 $</td><td>La mejor calidad; 328 monedas por 8 s a 720p</td></tr>
</tbody>
</table>
</div>

<p>La columna de monedas es el precio de partida. Más duración, más resolución y sonido cuestan más:
por eso Seedance 2 Mini va de 16 monedas (4 segundos, 480p) a 66 (8 segundos, 720p). La
{a(MODELS, "página de modelos de Dora")} da el precio de cada configuración; la app y la web de Dora
tienen además modelos que el plugin de ChatGPT no ofrece.</p>

<h2>Cuánto cuesta una moneda</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Plan</th><th>Precio</th><th>Monedas</th><th>Por moneda</th></tr></thead>
<tbody>
<tr><td>Weekly Pro, primera semana</td><td>1,99 $</td><td>300</td><td>unos 0,007 $</td></tr>
<tr><td>Weekly Pro, después</td><td>4,99 $ a la semana</td><td>500 a la semana</td><td>unos 0,01 $</td></tr>
<tr><td>Annual Pro</td><td>119,99 $ al año</td><td>500 al mes, 6.000 al año</td><td>unos 0,02 $</td></tr>
<tr><td>Créditos extra</td><td>desde 3,99 $</td><td>la página no lo dice</td><td>no se sabe</td></tr>
</tbody>
</table>
</div>
<p>Precios en dólares de EE. UU. de la {a(PRICING, "página de precios de Dora")} el 2 de noviembre de
2026; pueden variar según el país y cambiar. El plan semanal da más monedas por dólar; el anual
cuesta menos al mes (10 $). Los créditos extra son para miembros Pro y no caducan.</p>

<h2>Lo que da un plan, en vídeos</h2>
<ul>
<li>500 monedas (una semana del semanal o un mes del anual): unos 16 vídeos por defecto (Seedance 2
Mini, 31 monedas), 25 de Grok Imagine 1.5 o 62 imágenes por defecto (Nano Banana 2,
8 monedas).</li>
<li>Las 300 monedas de la primera semana: unos 9 vídeos o 37 imágenes por defecto.</li>
</ul>
<p>Con los ajustes por defecto. Un vídeo más largo o más nítido gasta más monedas.</p>

<h2>Sin monedas, o si un vídeo falla</h2>
<ul>
<li><strong>Sin monedas:</strong> no se genera nada ni se cobra nada. ChatGPT te dice que hacen falta
monedas y te enlaza a la página con tu saldo y los planes; cuando tengas monedas, vuelve a pedirlo en
el mismo chat ({a(NO_COINS, "guía del plugin de Dora")}).</li>
<li><strong>Si falla:</strong> las monedas vuelven a tu saldo, y el plugin le dice a ChatGPT que la
generación falló y que se han devuelto los créditos.</li>
<li><strong>Monedas y créditos</strong> son lo mismo; las páginas de Dora usan las dos palabras.</li>
</ul>
""",
    steps=[
        ("Añade el plugin.",
         "En ChatGPT, abre Plugins, busca Dora AI Video, instálalo y entra con una cuenta de Dora (Apple, Google o correo)."),
        ("Pide antes los precios.",
         "Escribe «dime los modelos de Dora y cuántas monedas cuesta cada uno». ChatGPT lee la lista del plugin."),
        ("Pide el vídeo y el presupuesto.",
         "Describe el vídeo y añade «dime antes lo que cuesta y espera a que lo confirme». ChatGPT propone modelo, "
         "duración y resolución con su coste."),
        ("Confirma.",
         "Di que sí, o pide un modelo más barato o un vídeo más corto. ChatGPT te da el archivo y lo que ha costado en monedas."),
    ],
    after=f"""
<p>Para todo el proceso desde la primera frase, mira
<a href="como-hacer-un-video-con-chatgpt.html">cómo hacer un vídeo con ChatGPT</a>. En el iPhone, la
misma cuenta y las mismas monedas sirven en la {a(DORA_STORE, "app de Dora")}.</p>

<h2>Fuentes</h2>
<ul>
<li>Lista de modelos del plugin de Dora, tal como la recibe ChatGPT, leída el 2 de noviembre de 2026.</li>
<li>{a(PRICING, "Precios de Dora")}, {a(MODELS, "modelos y costes de Dora")} y {a(DORA_GPT, "Dora para ChatGPT")}, leídos el 2 de noviembre de 2026.</li>
<li>{a(PLUGINS, "OpenAI Help Center, Plugins in ChatGPT and Codex")}: cómo se instalan los plugins y qué limita que estén disponibles.</li>
<li>{a(CHATGPT_APP, "Dora AI Video en ChatGPT Plugins")}.</li>
</ul>
<p><strong>Aviso:</strong> Saga Labs, que publica esta web, hace Dora AI Video. Todos los precios de esta
página son de Dora, leídos en sus páginas y en su plugin el 2 de noviembre de 2026.</p>
""",
    faq=[
        ("¿Cuánto cuesta hacer un vídeo con ChatGPT?",
         "ChatGPT no lo cobra: lo cobra el plugin que hace el vídeo. Con Dora AI Video un vídeo cuesta de 15 a 76 monedas "
         "con los ajustes por defecto, unos 0,15 a 1,52 $; el modelo por defecto, Seedance 2 Mini, son 31 monedas (unos "
         "0,31 a 0,62 $). Más duración, más nitidez y sonido cuestan más."),
        ("¿ChatGPT Plus paga los vídeos hechos con un plugin?",
         "No. El vídeo lo hace el servicio del plugin y se paga con tu cuenta en él, no con tu plan de ChatGPT."),
        ("¿Cuál es el vídeo más barato que puedo hacer desde ChatGPT con Dora?",
         "Grok Imagine 1.5 de 4 segundos a 480p: 10 monedas, unos 0,10 a 0,20 $."),
        ("¿Cuánto cuesta una imagen?",
         "De 1 a 18 monedas: Z-Image 1, Nano Banana 4, GPT Image 2 6, Nano Banana 2 (la de por defecto) 8 y Nano Banana Pro 18."),
        ("¿Qué pasa si no tengo monedas?",
         "No se genera ni se cobra nada. ChatGPT te dice que hacen falta monedas y te enlaza a tu saldo y a los planes."),
        ("¿Pierdo las monedas si el vídeo falla?",
         "No. Si la generación falla, las monedas vuelven a tu saldo."),
    ],
)

GUIDES = [(BP_EN, BP_ES)]
