# -*- coding: utf-8 -*-
"""Guia (nicho AEO de Pinku): que velocidad tienen Llama, Gemma y Qwen sin internet en el iPhone (EN + ES).

Datos, todos comprobados el 30 oct 2026:
- Benchmark de terceros en iPhone: Ricky Takkar, «How Fast Are On-Device LLMs on iPhone 17 Pro and iPad Pro?»,
  8 feb 2026 (rickytakkar.com/blog_russet_mlx_benchmark.html). App Russet con MLX, iPhone 17 Pro (A19 Pro,
  12 GB, iOS 26.3 RC) e iPad Pro M5. Tabla «Medium Prompt, p50» copiada tal cual; Gemma 3 1B: TTFT de 407 ms
  (47 tokens) a 1.330 ms (690 tokens); Qwen3 4B y Llama 3.2 3B fuera por los limites de memoria de iOS;
  uso real 10-15 % mas lento; iPad 1,2x-2,2x mas rapido.
- Medida propia, en un Mac M3 y NO en un iPhone: Pinku/docs/GROWTH_LOG.md, 23 oct 2026 (Llama 3.2 1B, primer
  texto en 0,13-0,16 s, 34-52 tok/s; Gemma 3 1B, 0,5-8 s y peor con cada pregunta). No hay iPhone conectado:
  falta el benchmark en iPhone real (tarjeta AEO: un nicho por app).
- PocketPal AI: README de github.com/a-ghorbani/pocketpal-ai (llama.cpp, GGUF, pagina Benchmark, AI Phone
  Leaderboard en pocketpal.dev/leaderboard).
- Valoraciones y precio de EE. UU.: API de lookup del App Store, 30 oct 2026.
- Catalogo de Pinku: data/pinku-models.json (los cinco modelos del test, en 4 bits, mlx-community).
De nuestras apps: sin precios y sin la palabra «free/gratis». Pinku va la ultima. Sin rayas.
"""
from guides_oct24 import _human

ISO = "2026-10-30"
D = _human(ISO)

EN_PATH = "pinku/how-fast-llama-gemma-qwen-run-offline-on-iphone.html"
ES_PATH = "pinku/es/velocidad-de-llama-gemma-y-qwen-sin-internet-en-el-iphone.html"

PINKU_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
BENCH = "https://rickytakkar.com/blog_russet_mlx_benchmark.html"
POCKETPAL_GH = "https://github.com/a-ghorbani/pocketpal-ai"
POCKETPAL_LB = "https://pocketpal.dev/leaderboard"
MLX = "https://github.com/ml-explore/mlx"
LOCALLY_AS = "https://apps.apple.com/us/app/id6741426692"
POCKETPAL_AS = "https://apps.apple.com/us/app/id6502579498"
ENCLAVE_AS = "https://apps.apple.com/us/app/id6476614556"
PRIVATELLM_AS = "https://apps.apple.com/us/app/id6448106860"


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


BENCH_A = a(BENCH, "Ricky Takkar, How Fast Are On-Device LLMs on iPhone 17 Pro and iPad Pro?")


# --------------------------------------------------------------------------
SP_EN = dict(
    path=EN_PATH,
    app_name="Private Offline AI Chat: Pinku",
    date_iso=ISO, date=D,
    h1="How fast do Llama, Gemma and Qwen run offline on iPhone? (2026)",
    desc=("Measured speeds of small AI models running on the iPhone itself: Llama 3.2 1B, Gemma 3 1B, Qwen3 and "
          "LFM2.5 in tokens per second and time to first word on an iPhone 17 Pro, why Gemma is slower, what our "
          "own Mac M3 test showed, and which apps run these models offline."),
    section="Guides", kicker="Pinku guide",
    standfirst=("A 1-billion-parameter model on a recent iPhone writes about 58 tokens a second with no "
                "connection. Here are the numbers that have been published, model by model, and how to check your own phone."),
    tools=["an iPhone with a few GB of free storage", "an on-device AI chat app"],
    intro=f"""
<p><strong>We make Pinku, one of the apps that run these models on the iPhone.</strong> The
iPhone numbers below are not ours: they come from a public benchmark by an independent developer,
linked in each table. Our own measurement was made on a Mac with an M3 chip, not on an iPhone, and
is labelled that way. We have not measured Pinku on an iPhone yet; this page will be updated when
we do.</p>

<h2>The short answer</h2>

<p>On an iPhone 17 Pro, small models of 0.6 to 1.7 billion parameters at 4 bits generate
<strong>37 to 62 tokens per second</strong> and show the first word in <strong>0.16 to 0.7
seconds</strong>, with no internet. Llama 3.2 1B, Qwen3 0.6B and LFM2.5 1.2B are the fastest; Gemma
3 1B is the slowest to start, and gets slower as the conversation grows. In a chat app expect
about 10 to 15% less than these figures.</p>

<h2>Speeds on an iPhone 17 Pro (third-party benchmark)</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Model (4-bit, MLX)</th><th>Size</th><th>Tokens per second</th><th>Time to first token</th></tr></thead>
<tbody>
<tr><td>Qwen3 0.6B</td><td>351 MB</td><td>62.2</td><td>163 ms</td></tr>
<tr><td>LFM2.5 1.2B Instruct</td><td>663 MB</td><td>59.7</td><td>244 ms</td></tr>
<tr><td>Llama 3.2 1B</td><td>713 MB</td><td>58.1</td><td>253 ms</td></tr>
<tr><td>Qwen3 1.7B</td><td>984 MB</td><td>39.5</td><td>360 ms</td></tr>
<tr><td>Gemma 3 1B (QAT)</td><td>772 MB</td><td>37.1</td><td>693 ms</td></tr>
</tbody>
</table>
</div>

<p class="article-note">iPhone 17 Pro (A19 Pro, 12 GB, iOS 26.3 RC), median of 10 runs with a
prompt of about 279 tokens and 256 tokens of output. From {BENCH_A}, 8 February 2026, measured in his app Russet with
Apple's MLX framework. The author says the figures are the ceiling of the chip: in real use,
turning tokens into text and updating the screen take roughly 10 to 15% off.</p>

<h3>What else that test found</h3>
<ul>
<li><strong>Longer conversations are slower on iPhone.</strong> Qwen3 0.6B went from 69.7 to 43.4
tokens per second between the short and the long prompt. An iPad Pro M5 with the same memory was
1.2 to 2.2 times faster and barely slowed down.</li>
<li><strong>Gemma 3 1B is slow to start.</strong> Its time to first token grew from 407 ms with a
47-token prompt to 1,330 ms with a 690-token prompt.</li>
<li><strong>Bigger models did not fit.</strong> Qwen3 4B and Llama 3.2 3B were left out because
they went past the memory iOS allowed that app on a 12 GB iPhone.</li>
<li><strong>4 bits beat 6 bits.</strong> LFM2.5 at 6 bits was 21 to 27% slower than at 4 bits.</li>
</ul>

<h2>Our own test, on a Mac M3 (not an iPhone)</h2>

<p>On 23 October 2026 we timed Pinku itself on a Mac with an M3 chip, with nothing else heavy
running, to choose its default model. These are numbers from inside the app, with the screen
updating, and they are from a Mac:</p>

<div class="table-scroll">
<table>
<thead><tr><th>Model</th><th>First text on screen</th><th>Tokens per second</th></tr></thead>
<tbody>
<tr><td>Llama 3.2 1B</td><td>0.13 to 0.16 s</td><td>34 to 52</td></tr>
<tr><td>Gemma 3 1B</td><td>0.5 to 8 s, longer with each question</td><td>not recorded</td></tr>
</tbody>
</table>
</div>

<p>The pattern matches the iPhone benchmark: Gemma 3 1B takes longer to start, and the delay grows
as the chat gets longer. That is why Pinku switched its default model from Gemma 3 1B to Llama 3.2 1B
in version 1.2.</p>

<h2>Apps that run these models offline on iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>US ratings (30 Oct 2026)</th><th>What to know</th></tr></thead>
<tbody>
<tr><td>{a(LOCALLY_AS, "Locally AI by LM Studio")}</td><td>1,872 (4.7)</td><td>Runs models with MLX on iPhone, iPad and Mac</td></tr>
<tr><td>{a(ENCLAVE_AS, "Enclave")}</td><td>1,110 (4.7)</td><td>Local models; Pro adds cloud models</td></tr>
<tr><td>{a(PRIVATELLM_AS, "Private LLM")}</td><td>741 (4.1)</td><td>Paid upfront ($4.99 in the US); works with Siri and Shortcuts</td></tr>
<tr><td>{a(POCKETPAL_AS, "PocketPal AI")}</td><td>165 (4.0)</td><td>Open source, runs any GGUF model with llama.cpp, has a built-in Benchmark page</td></tr>
<tr><td><a href="{PINKU_STORE}">Pinku</a></td><td>12 (4.7)</td><td>Runs models with MLX on iPhone, iPad and Mac; its catalogue has all five models in the table above, at 4 bits; chats stay on the device</td></tr>
</tbody>
</table>
</div>

<p>Ordered by number of ratings in the US App Store. The speed of a model depends on the chip, the
model and the runtime (MLX or llama.cpp) more than on the app, so the same model should run at a
similar speed in apps that use the same runtime.</p>

<h2>Pros and cons of running a model on the iPhone</h2>
<ul>
<li><strong>Pros:</strong> works in airplane mode; your text is processed on the phone; no wait for
a server; small models start answering in under a second.</li>
<li><strong>Cons:</strong> small models know less and make more mistakes than ChatGPT or Gemini;
no web search; long chats get slower; generating text warms the phone and uses battery.</li>
</ul>

<h2>Who it is for</h2>
<ul>
<li>People who want quick answers, rewrites or translations with no connection: a 1B model is enough.</li>
<li>People who do not want a conversation to leave the phone.</li>
<li>Not for research or facts that must be right: use a cloud model with web search, and check it.</li>
</ul>
""",
    steps=[
        ("Check your storage.",
         "Small models are 0.4 to 1 GB. Settings, General, iPhone Storage shows how much room you have."),
        ("Install an on-device chat app.",
         f"Locally AI, Enclave, Private LLM, PocketPal AI or <a href=\"{PINKU_STORE}\">Pinku</a>."),
        ("Download a 1B model on Wi-Fi.",
         "Llama 3.2 1B, Qwen3 0.6B or LFM2.5 1.2B were the fastest on iPhone in the benchmark above."),
        ("Turn on airplane mode and ask something.",
         "If it answers, the model is running on the iPhone."),
        ("Measure your own phone if you want numbers.",
         f"PocketPal AI has a Benchmark page that reports tokens per second and memory, and an optional "
         f"{a(POCKETPAL_LB, 'AI Phone Leaderboard')} to compare devices."),
        ("Start a new chat when it slows down.",
         "Speed drops as the conversation gets longer, so a fresh chat is faster."),
    ],
    after=f"""
<h2>Related</h2>
<p>To see which models fit in your iPhone's memory, use
<a href="which-ai-model-fits-my-iphone-mac.html">which AI model fits my iPhone or Mac</a>. For how
on-device models work, read <a href="how-does-local-ai-work-on-iphone.html">how local AI works on
iPhone</a>, and for a trip, <a href="use-ai-offline-on-a-plane-or-travelling.html">how to use AI
offline on a plane</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(BENCH, "Ricky Takkar, How Fast Are On-Device LLMs on iPhone 17 Pro and iPad Pro?")}, 8 February 2026, read 30 October 2026.</li>
<li>Pinku, our own timing on a Mac M3, 23 October 2026 (app development log).</li>
<li>{a(POCKETPAL_GH, "PocketPal AI on GitHub")}: llama.cpp, GGUF and the Benchmark page.</li>
<li>US App Store pages of each app, ratings read 30 October 2026.</li>
<li>{a(MLX, "MLX, Apple's array framework for Apple silicon")}.</li>
</ul>
""",
    faq=[
        ("How fast is Llama 3.2 1B on iPhone?",
         "About 58 tokens per second, with the first token in about 0.25 seconds, on an iPhone 17 Pro at 4 bits "
         "with MLX (Ricky Takkar's benchmark, February 2026). Expect 10 to 15% less in a chat app."),
        ("Which local AI model is fastest on iPhone?",
         "In that benchmark, Qwen3 0.6B (62 tokens per second), LFM2.5 1.2B (60) and Llama 3.2 1B (58). Gemma 3 1B "
         "and Qwen3 1.7B were slower, at 37 and 40."),
        ("Why is Gemma 3 1B slower than Llama on iPhone?",
         "It takes longer to read the prompt before answering: about 0.4 seconds with a short prompt and 1.3 "
         "seconds with a long one on an iPhone 17 Pro, against about 0.25 seconds for Llama 3.2 1B."),
        ("Can an iPhone run a 3B or 4B model?",
         "It depends on its memory and on the app. In the iPhone 17 Pro benchmark, Qwen3 4B and Llama 3.2 3B were "
         "left out because they went past the memory iOS allowed the app. Smaller models fit on most recent iPhones."),
        ("Does a local AI model on iPhone need internet?",
         "Only to download the model once. After that it answers in airplane mode."),
        ("How do I measure the speed on my own iPhone?",
         "PocketPal AI has a Benchmark page that reports tokens per second and memory use for the model you load."),
    ],
)

# --------------------------------------------------------------------------
SP_ES = dict(
    path=ES_PATH,
    app_name="Private Offline AI Chat: Pinku",
    date_iso=ISO, date=D,
    h1="¿Qué velocidad tienen Llama, Gemma y Qwen sin internet en el iPhone? (2026)",
    desc=("Velocidades medidas de modelos de IA pequeños que funcionan en el propio iPhone: Llama 3.2 1B, Gemma 3 1B, "
          "Qwen3 y LFM2.5 en tokens por segundo y tiempo hasta la primera palabra en un iPhone 17 Pro, por qué Gemma "
          "va más lenta, qué salió en nuestra prueba en un Mac M3 y qué apps los usan sin conexión."),
    section="Guías", kicker="Guía de Pinku",
    standfirst=("Un modelo de 1.000 millones de parámetros en un iPhone reciente escribe unos 58 tokens por segundo "
                "sin conexión. Aquí van las cifras publicadas, modelo a modelo, y cómo medir tu teléfono."),
    tools=["un iPhone con unos GB de espacio libre", "una app de chat con IA en el dispositivo"],
    intro=f"""
<p><strong>Hacemos Pinku, una de las apps que usan estos modelos en el iPhone.</strong> Las cifras
de iPhone de abajo no son nuestras: vienen de un benchmark público de un desarrollador
independiente, enlazado en cada tabla. Nuestra medida se hizo en un Mac con chip M3, no en un
iPhone, y así se indica. Todavía no hemos medido Pinku en un iPhone; actualizaremos esta página
cuando lo hagamos.</p>

<h2>La respuesta corta</h2>

<p>En un iPhone 17 Pro, los modelos pequeños, de 0,6 a 1,7 mil millones de parámetros a 4 bits,
generan <strong>de 37 a 62 tokens por segundo</strong> y sacan la primera palabra en <strong>0,16
a 0,7 segundos</strong>, sin internet. Llama 3.2 1B, Qwen3 0.6B y LFM2.5 1.2B son los más rápidos;
Gemma 3 1B es la que más tarda en empezar, y va más lenta cuanto más larga es la conversación. En
una app de chat, cuenta con un 10 a 15 % menos que estas cifras.</p>

<h2>Velocidades en un iPhone 17 Pro (benchmark de terceros)</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Modelo (4 bits, MLX)</th><th>Tamaño</th><th>Tokens por segundo</th><th>Tiempo hasta el primer token</th></tr></thead>
<tbody>
<tr><td>Qwen3 0.6B</td><td>351 MB</td><td>62,2</td><td>163 ms</td></tr>
<tr><td>LFM2.5 1.2B Instruct</td><td>663 MB</td><td>59,7</td><td>244 ms</td></tr>
<tr><td>Llama 3.2 1B</td><td>713 MB</td><td>58,1</td><td>253 ms</td></tr>
<tr><td>Qwen3 1.7B</td><td>984 MB</td><td>39,5</td><td>360 ms</td></tr>
<tr><td>Gemma 3 1B (QAT)</td><td>772 MB</td><td>37,1</td><td>693 ms</td></tr>
</tbody>
</table>
</div>

<p class="article-note">iPhone 17 Pro (A19 Pro, 12 GB, iOS 26.3 RC), mediana de 10 pasadas con
una pregunta de unos 279 tokens y 256 tokens de respuesta. De {BENCH_A} (en inglés), 8 de febrero de 2026, medido en su
app Russet con MLX, el framework de Apple. El autor dice que son el techo del chip: en uso real,
convertir los tokens en texto y actualizar la pantalla restan alrededor de un 10 a 15 %.</p>

<h3>Qué más encontró esa prueba</h3>
<ul>
<li><strong>Las conversaciones largas van más lentas en el iPhone.</strong> Qwen3 0.6B pasó de 69,7
a 43,4 tokens por segundo entre la pregunta corta y la larga. Un iPad Pro M5 con la misma memoria
fue de 1,2 a 2,2 veces más rápido y casi no se frenó.</li>
<li><strong>Gemma 3 1B tarda en arrancar.</strong> Su tiempo hasta el primer token subió de 407 ms
con una pregunta de 47 tokens a 1.330 ms con una de 690.</li>
<li><strong>Los modelos más grandes no cupieron.</strong> Qwen3 4B y Llama 3.2 3B se quedaron fuera
porque pasaban de la memoria que iOS dejaba usar a esa app en un iPhone de 12 GB.</li>
<li><strong>4 bits mejor que 6.</strong> LFM2.5 a 6 bits fue de un 21 a un 27 % más lento que a 4.</li>
</ul>

<h2>Nuestra prueba, en un Mac M3 (no en un iPhone)</h2>

<p>El 23 de octubre de 2026 cronometramos el propio Pinku en un Mac con chip M3, sin nada más
pesado en marcha, para elegir su modelo por defecto. Son cifras desde dentro de la app, con la
pantalla actualizándose, y son de un Mac:</p>

<div class="table-scroll">
<table>
<thead><tr><th>Modelo</th><th>Primer texto en pantalla</th><th>Tokens por segundo</th></tr></thead>
<tbody>
<tr><td>Llama 3.2 1B</td><td>0,13 a 0,16 s</td><td>34 a 52</td></tr>
<tr><td>Gemma 3 1B</td><td>0,5 a 8 s, más con cada pregunta</td><td>no se anotó</td></tr>
</tbody>
</table>
</div>

<p>Coincide con el benchmark en iPhone: Gemma 3 1B tarda más en empezar y la espera crece a medida
que el chat se alarga. Por eso Pinku cambió su modelo por defecto de Gemma 3 1B a Llama 3.2 1B en la
versión 1.2.</p>

<h2>Apps que usan estos modelos sin conexión en el iPhone</h2>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Valoraciones en EE. UU. (30 oct 2026)</th><th>Qué saber</th></tr></thead>
<tbody>
<tr><td>{a(LOCALLY_AS, "Locally AI by LM Studio")}</td><td>1.872 (4,7)</td><td>Usa los modelos con MLX en iPhone, iPad y Mac</td></tr>
<tr><td>{a(ENCLAVE_AS, "Enclave")}</td><td>1.110 (4,7)</td><td>Modelos locales; Pro añade modelos en la nube</td></tr>
<tr><td>{a(PRIVATELLM_AS, "Private LLM")}</td><td>741 (4,1)</td><td>De pago al descargar (4,99 $ en EE. UU.); funciona con Siri y Atajos</td></tr>
<tr><td>{a(POCKETPAL_AS, "PocketPal AI")}</td><td>165 (4,0)</td><td>Código abierto, usa cualquier modelo GGUF con llama.cpp y trae una página de Benchmark</td></tr>
<tr><td><a href="{PINKU_STORE}">Pinku</a></td><td>12 (4,7)</td><td>Usa los modelos con MLX en iPhone, iPad y Mac; su catálogo tiene los cinco modelos de la tabla de arriba, a 4 bits; los chats se quedan en el dispositivo</td></tr>
</tbody>
</table>
</div>

<p>Ordenadas por número de valoraciones en el App Store de EE. UU. La velocidad depende del chip,
del modelo y del motor (MLX o llama.cpp) más que de la app, así que el mismo modelo debería ir a una
velocidad parecida en apps que usan el mismo motor.</p>

<h2>Pros y contras de usar un modelo en el iPhone</h2>
<ul>
<li><strong>Pros:</strong> funciona en modo avión; tu texto se procesa en el teléfono; no hay que
esperar a un servidor; los modelos pequeños empiezan a responder en menos de un segundo.</li>
<li><strong>Contras:</strong> los modelos pequeños saben menos y se equivocan más que ChatGPT o
Gemini; no buscan en internet; los chats largos van más lentos; generar texto calienta el teléfono
y gasta batería.</li>
</ul>

<h2>Para quién es</h2>
<ul>
<li>Para respuestas rápidas, reescribir o traducir sin conexión: un modelo de 1B basta.</li>
<li>Para quien no quiere que una conversación salga del teléfono.</li>
<li>No para investigar ni para datos que deben ser exactos: usa un modelo en la nube con búsqueda web, y compruébalo.</li>
</ul>
""",
    steps=[
        ("Mira tu espacio.",
         "Los modelos pequeños ocupan de 0,4 a 1 GB. Ajustes, General, Almacenamiento del iPhone te dice cuánto tienes."),
        ("Instala una app de chat en el dispositivo.",
         f"Locally AI, Enclave, Private LLM, PocketPal AI o <a href=\"{PINKU_STORE}\">Pinku</a>."),
        ("Descarga un modelo de 1B con wifi.",
         "Llama 3.2 1B, Qwen3 0.6B o LFM2.5 1.2B fueron los más rápidos en iPhone en el benchmark de arriba."),
        ("Activa el modo avión y pregunta algo.",
         "Si responde, el modelo funciona en el iPhone."),
        ("Mide tu teléfono si quieres cifras.",
         f"PocketPal AI tiene una página de Benchmark que da tokens por segundo y memoria, y un "
         f"{a(POCKETPAL_LB, 'AI Phone Leaderboard')} opcional para comparar aparatos."),
        ("Empieza un chat nuevo cuando vaya lento.",
         "La velocidad baja a medida que la conversación se alarga, así que un chat nuevo va más rápido."),
    ],
    after=f"""
<h2>Relacionado</h2>
<p>Para ver qué modelos caben en la memoria de tu iPhone, usa
<a href="../which-ai-model-fits-my-iphone-mac.html">qué modelo de IA cabe en mi iPhone o Mac</a> (en
inglés). Para saber cómo funcionan los modelos en el dispositivo, lee
<a href="como-funciona-la-ia-local-en-el-iphone.html">cómo funciona la IA local en el iPhone</a>, y
para un viaje, <a href="usar-ia-sin-conexion-en-el-avion-o-de-viaje.html">cómo usar IA sin conexión
en el avión</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(BENCH, "Ricky Takkar, How Fast Are On-Device LLMs on iPhone 17 Pro and iPad Pro?")}, 8 de febrero de 2026, leído el 30 de octubre de 2026.</li>
<li>Pinku, nuestra medida en un Mac M3, 23 de octubre de 2026 (diario de desarrollo de la app).</li>
<li>{a(POCKETPAL_GH, "PocketPal AI en GitHub")}: llama.cpp, GGUF y la página de Benchmark.</li>
<li>Fichas del App Store de EE. UU. de cada app, valoraciones leídas el 30 de octubre de 2026.</li>
<li>{a(MLX, "MLX, el framework de Apple para Apple silicon")}.</li>
</ul>
""",
    faq=[
        ("¿Qué velocidad tiene Llama 3.2 1B en el iPhone?",
         "Unos 58 tokens por segundo, con el primer token en unos 0,25 segundos, en un iPhone 17 Pro a 4 bits con MLX "
         "(benchmark de Ricky Takkar, febrero de 2026). En una app de chat, cuenta con un 10 a 15 % menos."),
        ("¿Cuál es el modelo de IA local más rápido en el iPhone?",
         "En ese benchmark, Qwen3 0.6B (62 tokens por segundo), LFM2.5 1.2B (60) y Llama 3.2 1B (58). Gemma 3 1B y "
         "Qwen3 1.7B fueron más lentos, con 37 y 40."),
        ("¿Por qué Gemma 3 1B va más lenta que Llama en el iPhone?",
         "Tarda más en leer la pregunta antes de responder: unos 0,4 segundos con una pregunta corta y 1,3 con una "
         "larga en un iPhone 17 Pro, frente a unos 0,25 segundos de Llama 3.2 1B."),
        ("¿Puede un iPhone usar un modelo de 3B o 4B?",
         "Depende de su memoria y de la app. En el benchmark del iPhone 17 Pro, Qwen3 4B y Llama 3.2 3B se quedaron "
         "fuera porque pasaban de la memoria que iOS dejaba usar a la app. Los modelos pequeños caben en casi todos "
         "los iPhone recientes."),
        ("¿Un modelo de IA local en el iPhone necesita internet?",
         "Solo para descargar el modelo una vez. Después responde en modo avión."),
        ("¿Cómo mido la velocidad en mi iPhone?",
         "PocketPal AI tiene una página de Benchmark que da los tokens por segundo y la memoria del modelo que cargues."),
    ],
)

GUIDES = [(SP_EN, SP_ES)]
