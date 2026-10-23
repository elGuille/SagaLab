# -*- coding: utf-8 -*-
"""Cuatro guias nuevas (23 oct 2026), EN + ES, con la plantilla de guides.py.

Cada una lleva al menos un dato de primera mano o comprobable, leido el 23 oct 2026:
- Pinku: etiquetas de privacidad del App Store de ChatGPT (1.2026.286), Google
  Gemini y Pinku 1.1; aviso de Google en support.google.com/gemini/answer/13594961.
  Lo de OpenAI sale del articulo del 20 oct (help.openai.com da 403 a curl).
- Photo Vault: support.apple.com/en-us/109519 (publicado 15 sep 2026: en iOS 27
  «Ready for Repair or Trade-In» en Buscar), 111795 (Acceso guiado), guia
  iph00f208d05 (bloquear u ocultar apps), 104987 (album Oculto). No hay
  «Maintenance Mode» en iOS: no se menciona.
- Drop: PubMed 33007706, 24590753, 22726808, 28337134, 38428577; Apple 109346 y
  guia iphb2cfa052c; descripciones del App Store de myNoise, White Noise Lite,
  Rain Rain, Endel y Dark Noise. Drop NO genera ruido blanco/rosa/marron.
- 3 Tasks: jamesclear.com/ivy-lee (Ivy Lee eran SEIS tareas), chrisbailey.com/
  rule-of-three (15 abr 2025), ficha de 3 Tasks 1.3.0 y de Top 3, Three Todo,
  TickTick y Structured.
De nuestras apps, solo lo que dice su ficha actual del App Store. Sin rayas.
"""

D23 = {"en": "23 October 2026", "es": "23 de octubre de 2026"}
D23_U24 = {"en": "23 October 2026, updated 24 October 2026", "es": "23 de octubre de 2026, actualizada el 24 de octubre de 2026"}
ISO = "2026-10-23"

PV_STORE = "https://apps.apple.com/app/apple-store/id1532670722?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
PINKU_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
DROP_STORE = "https://apps.apple.com/app/apple-store/id1462269642?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
TT_STORE = "https://apps.apple.com/app/apple-store/id1553693943?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"

A = '<a href="{u}" target="_blank" rel="noopener">{t}</a>'


def a(u, t):
    return A.format(u=u, t=t)


GEMINI_HUB = "https://support.google.com/gemini/answer/13594961"
CHATGPT_AS = "https://apps.apple.com/us/app/id6448311069"
GEMINI_AS = "https://apps.apple.com/us/app/id6477489729"
PINKU_AS = "https://apps.apple.com/us/app/id6754878073"
OAI_DELETE = "https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt"
OAI_TRAIN = "https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance"
SHORTCUTS_MODEL = "https://support.apple.com/guide/shortcuts/tpg3vrvwmclv/ios"

# --------------------------------------------------------------------------
# Pinku: es seguro contarle cosas privadas a ChatGPT
# --------------------------------------------------------------------------

PK3_EN = dict(
    path="pinku/is-it-safe-to-tell-chatgpt-private-things.html",
    app_name="Pinku: Private Offline AI Chat",
    date_iso=ISO, date=D23,
    h1="Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone (2026)",
    desc=("A practical answer: what ChatGPT and Gemini say they keep and who can read it, what their App Store "
          "privacy labels list (checked 23 October 2026), what never to paste into a cloud chatbot, the settings "
          "to change, and how to keep a conversation on your iPhone with an on-device model."),
    section="Guides", kicker="Pinku guide",
    standfirst=("Short answer: safe enough for general questions, not for anything that identifies you or "
                "someone else. The companies say so themselves. Here is what to change, and what to keep "
                "off the cloud entirely."),
    tools=["ChatGPT", "Google Gemini", "Pinku"],
    intro=f"""
<p><strong>We make Pinku, an AI chat app that runs on the iPhone, and it is one of the
options below.</strong> Most of this page applies whichever app you use.</p>

<h2>The short answer</h2>

<p>A cloud chatbot is a service run on someone else's computers. What you type is
stored on your account, can be used to train models unless you switch that off,
and some of it can be read by people. Google is the most direct about it: its
Gemini privacy hub says, in so many words, <em>“Please don't enter confidential
information that you wouldn't want a reviewer to see or Google to use to improve our
services”</em> ({a(GEMINI_HUB, "Gemini Apps Privacy Hub")}, read 23 October 2026). The
same page says chats a human reviewed are kept for up to 3 years, disconnected from
your account, even if you delete them.</p>

<p>OpenAI deletes a chat you delete within 30 days, with exceptions for chats already
de-identified or kept for security or legal reasons, and on Free, Plus and Pro it may
train on your chats unless you turn off <em>Improve the model for everyone</em>. Even
then, a thumbs up or down sends the whole conversation for training. We read and
quoted every one of those policies in
<a href="../blog/what-ai-chatbots-keep-when-you-delete-chats.html">what AI chatbots keep when
you delete your chats</a>.</p>

<h2>What the App Store privacy labels say (checked 23 October 2026)</h2>

<p>Every iPhone app has to declare what it collects. These are the developers' own
declarations, which Apple shows but does not verify:</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Data linked to you, as declared</th><th>Purposes that stand out</th></tr></thead>
<tbody>
<tr><td>{a(CHATGPT_AS, "ChatGPT")} (version 1.2026.286)</td><td>Health &amp; Fitness, Location, Contact Info, User Content, Search History, Identifiers, Usage Data, Diagnostics</td><td>User Content is listed for Analytics and App Functionality; Health &amp; Fitness for Analytics and Product Personalisation; Usage and Advertising Data for Third-Party Advertising</td></tr>
<tr><td>{a(GEMINI_AS, "Google Gemini")}</td><td>Includes precise location, contacts, search and browsing history, user content and identifiers</td><td>Developer's advertising or marketing, analytics, product personalisation</td></tr>
<tr><td>{a(PINKU_AS, "Pinku")} (version 1.1)</td><td>Purchases and an identifier (user ID)</td><td>App Functionality only: recording an App Store purchase</td></tr>
</tbody>
</table>
</div>

<p>A label is not proof of anything bad; it tells you what can leave the phone. With
a cloud chatbot, your conversations are part of that by design.</p>

<h2>What not to paste into any cloud chatbot</h2>

<ul>
<li>Passwords, one-time codes, recovery keys, full card or bank numbers.</li>
<li>ID, passport, social security or health insurance numbers.</li>
<li>Medical results, legal documents or contracts with your name, address or case number still on them.</li>
<li>Other people's private details: a friend's diagnosis, a colleague's salary, screenshots of someone else's messages.</li>
<li>Work material your employer has not cleared for AI tools.</li>
</ul>

<p>Asking “what does a high LDL mean?” is fine. Pasting the lab report with your name
and date of birth is the part to avoid.</p>
""",
    steps=[
        ("Sort the question first.",
         "General knowledge, writing help and code without secrets can go to any cloud chatbot. Anything that "
         "identifies you or someone else should be rewritten, or kept on the phone."),
        ("Strip identifiers before pasting.",
         "Remove names, addresses, dates of birth, account and case numbers. Replace them with placeholders "
         "such as [NAME]; the answer will be just as useful."),
        ("Turn off training in ChatGPT.",
         f"In ChatGPT open Settings, Data controls and turn off Improve the model for everyone "
         f"({a(OAI_TRAIN, 'OpenAI help')}). Do not press thumbs up or down on a sensitive chat: that sends the "
         "whole conversation for training even with the setting off."),
        ("Use temporary chats for one-off questions.",
         "ChatGPT temporary chats are not in your history but may be kept up to 30 days. Gemini temporary chats, "
         "and chats with Keep Activity off, are kept 72 hours and are not used to improve Google AI with human reviewers."),
        ("Delete what you no longer need.",
         f"Deleted ChatGPT chats are erased within 30 days, with exceptions ({a(OAI_DELETE, 'OpenAI')}). Gemini "
         "auto-deletes after 18 months by default; you can set 3 months. Chats a reviewer already read stay up to 3 years."),
        ("Keep the truly private things on the phone.",
         f"Use an AI that runs on the device, such as <a href=\"{PINKU_STORE}\">Pinku</a>. Download a model once, "
         "then turn on airplane mode and ask: if it answers, nothing you typed left the iPhone."),
    ],
    after=f"""
<h2>Keeping it on the phone: the options</h2>

<p>An on-device model is much smaller than ChatGPT, so it is weaker at hard
questions, cannot browse the web and remembers less of the conversation. For
rewriting a private message, summarising a document you paste in or thinking aloud
about something personal, it is enough, and there is no server to trust.</p>

<ul>
<li><strong>Pinku</strong> (version 1.1, 22 October 2026). Runs 11 open models on iPhone or Mac
with Apple's MLX, from Qwen3 0.6B (0.4 GB) to Qwen3 8B (4.7 GB); works in airplane mode once a model is
downloaded; no account; chats saved only on the device. Free with Gemma 3 1B; Pinku Pro (yearly or a
one-time purchase) lets you choose any model and adds custom instructions, on-device dictation and read
aloud. Requires iOS 18.6. It is weaker than a cloud model, and only lists the models your device has
the memory for.</li>
<li><strong>Locally AI by LM Studio</strong> (free, 1.66.0): runs Llama, Gemma, Qwen and others on iPhone and iPad with MLX, no login.</li>
<li><strong>Private LLM</strong> ($4.99 one-time, 1.9.16): local models on iPhone and iPad.</li>
<li><strong>PocketPal AI</strong> (free, 1.20.1): runs models on the device for offline chat.</li>
<li><strong>Enclave</strong> (free, 1.77.0): local assistant; its current version requires iOS 27.</li>
<li><strong>Apple's own model</strong>: on iPhones with Apple Intelligence, the Shortcuts action Use Model set to
On-Device works {a(SHORTCUTS_MODEL, "without a network connection")}.</li>
</ul>

<p>Versions and prices from the US App Store on 23 October 2026. We compared these apps in
detail, including where they beat Pinku, in <a href="../blog/best-private-ai-apps-iphone.html">the best
private AI apps that keep your chats on your iPhone</a>. To check any app yourself, see
<a href="check-ai-chat-app-keeps-chats-on-iphone.html">how to check whether an AI chat app really keeps
your chats on your iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(GEMINI_HUB, "Google, Gemini Apps Privacy Hub")}, read 23 October 2026.</li>
<li>App Store privacy labels of {a(CHATGPT_AS, "ChatGPT")}, {a(GEMINI_AS, "Google Gemini")} and {a(PINKU_AS, "Pinku")}, US store, read 23 October 2026.</li>
<li>OpenAI help centre on {a(OAI_DELETE, "chat retention")} and {a(OAI_TRAIN, "model training")}, quoted in <a href="../blog/what-ai-chatbots-keep-when-you-delete-chats.html">our 20 October 2026 article</a>.</li>
<li>{a(SHORTCUTS_MODEL, "Apple, Shortcuts User Guide: Use Model")}.</li>
</ul>
""",
    faq=[
        ("Is it safe to tell ChatGPT private things?",
         "For general questions, yes. For anything that identifies you or someone else, no: chats are stored on your "
         "account, may be used for training unless you turn it off, and the companies' own pages tell you not to share "
         "confidential information. Remove names and numbers first, or use an AI that runs on your phone."),
        ("Can people at OpenAI or Google read my chats?",
         "Google says human reviewers read some Gemini chats and keeps those for up to 3 years, disconnected from your "
         "account. OpenAI keeps chats until you delete them and may review them for safety. Neither is a private diary."),
        ("Does deleting a ChatGPT chat delete it for good?",
         "It disappears at once and OpenAI says it is erased within 30 days, unless it was already de-identified or must "
         "be kept for security or legal reasons."),
        ("Does a temporary chat keep my data private?",
         "Partly. ChatGPT temporary chats are not in your history but may be kept up to 30 days. Gemini temporary chats are "
         "kept 72 hours. Both still go to the company's servers."),
        ("How can I use AI without my chats leaving my phone?",
         "Use an app that runs the model on the device, such as Pinku, Locally AI, Private LLM or PocketPal AI. Test it in "
         "airplane mode: if it still answers, the conversation stays on the phone."),
    ],
)

PK3_ES = dict(
    path="pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html",
    app_name="Pinku: Private Offline AI Chat",
    date_iso=ISO, date=D23,
    h1="¿Es seguro contarle cosas privadas a ChatGPT? Qué guardan las apps de IA y cómo dejarlo en tu móvil (2026)",
    desc=("Respuesta práctica: qué dicen ChatGPT y Gemini que guardan y quién puede leerlo, qué declaran sus etiquetas de "
          "privacidad del App Store (comprobado el 23 de octubre de 2026), qué no pegar nunca en un chatbot en la nube, "
          "qué ajustes cambiar y cómo dejar una conversación en el iPhone con un modelo local."),
    section="Guías", kicker="Guía de Pinku",
    standfirst=("Respuesta corta: vale para preguntas generales, no para nada que te identifique a ti o a otra "
                "persona. Lo dicen las propias empresas. Esto es lo que conviene cambiar y lo que mejor no subir a la nube."),
    tools=["ChatGPT", "Google Gemini", "Pinku"],
    intro=f"""
<p><strong>Hacemos Pinku, una app de chat con IA que funciona dentro del iPhone, y es una
de las opciones de abajo.</strong> Casi todo lo que sigue vale uses la app que uses.</p>

<h2>La respuesta corta</h2>

<p>Un chatbot en la nube es un servicio que corre en ordenadores de otra empresa. Lo que
escribes se guarda en tu cuenta, puede usarse para entrenar modelos si no lo desactivas
y una parte la pueden leer personas. Google lo dice sin rodeos en su centro de privacidad
de Gemini: <em>«No incluyas información confidencial que no quieras que vea un revisor o
que Google utilice para mejorar sus servicios»</em> ({a(GEMINI_HUB + "?hl=es", "Centro de privacidad de Gemini")},
leído el 23 de octubre de 2026). La misma página dice que los chats que ha revisado una
persona se guardan hasta 3 años, desvinculados de tu cuenta, aunque los borres.</p>

<p>OpenAI elimina en 30 días un chat que borras, salvo los ya anonimizados o los que deba
conservar por seguridad o por ley, y en Free, Plus y Pro puede entrenar con tus chats si
no desactivas <em>Mejorar el modelo para todos</em>. Aun así, un pulgar arriba o abajo
envía la conversación entera para entrenar. Leímos y citamos cada política en
<a href="../../blog/what-ai-chatbots-keep-when-you-delete-chats.html">qué guardan los chatbots
de IA cuando borras tus chats</a> (en inglés).</p>

<h2>Qué dicen las etiquetas de privacidad del App Store (23 de octubre de 2026)</h2>

<p>Cada app de iPhone tiene que declarar qué recoge. Son declaraciones del propio
desarrollador, que Apple muestra pero no verifica:</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Datos vinculados a ti, según declara</th><th>Fines que llaman la atención</th></tr></thead>
<tbody>
<tr><td>{a(CHATGPT_AS, "ChatGPT")} (versión 1.2026.286)</td><td>Salud y forma física, ubicación, datos de contacto, contenido del usuario, historial de búsqueda, identificadores, datos de uso, diagnóstico</td><td>Contenido del usuario figura para analítica y funcionalidad de la app; salud y forma física, para analítica y personalización; datos de uso y de publicidad, para publicidad de terceros</td></tr>
<tr><td>{a(GEMINI_AS, "Google Gemini")}</td><td>Incluye ubicación precisa, contactos, historial de búsqueda y de navegación, contenido del usuario e identificadores</td><td>Publicidad o marketing del desarrollador, analítica, personalización</td></tr>
<tr><td>{a(PINKU_AS, "Pinku")} (versión 1.1)</td><td>Compras y un identificador (ID de usuario)</td><td>Solo funcionalidad de la app: registrar una compra del App Store</td></tr>
</tbody>
</table>
</div>

<p>Una etiqueta no prueba nada malo; dice qué puede salir del móvil. Con un chatbot en la
nube, tus conversaciones salen por diseño.</p>

<h2>Lo que no conviene pegar en ningún chatbot en la nube</h2>

<ul>
<li>Contraseñas, códigos de un solo uso, claves de recuperación, números completos de tarjeta o de cuenta.</li>
<li>DNI, pasaporte, número de la Seguridad Social o de la tarjeta sanitaria.</li>
<li>Análisis médicos, documentos legales o contratos con tu nombre, dirección o número de expediente.</li>
<li>Datos privados de otras personas: el diagnóstico de un amigo, el sueldo de un compañero, capturas de mensajes ajenos.</li>
<li>Material del trabajo que tu empresa no haya autorizado para herramientas de IA.</li>
</ul>

<p>Preguntar «¿qué significa tener el LDL alto?» está bien. Pegar el análisis con tu nombre
y tu fecha de nacimiento es lo que hay que evitar.</p>
""",
    steps=[
        ("Clasifica la pregunta.",
         "Cultura general, ayuda para escribir y código sin secretos pueden ir a cualquier chatbot en la nube. Lo que te "
         "identifique a ti o a otra persona, reescríbelo o déjalo en el móvil."),
        ("Quita los datos que identifican antes de pegar.",
         "Borra nombres, direcciones, fechas de nacimiento y números de cuenta o de expediente. Pon marcadores como "
         "[NOMBRE]; la respuesta será igual de útil."),
        ("Desactiva el entrenamiento en ChatGPT.",
         f"En ChatGPT abre Ajustes, Controles de datos y desactiva Mejorar el modelo para todos "
         f"({a(OAI_TRAIN, 'ayuda de OpenAI')}). No pulses el pulgar arriba o abajo en un chat delicado: envía la "
         "conversación entera para entrenar aunque el ajuste esté desactivado."),
        ("Usa chats temporales para preguntas sueltas.",
         "Los chats temporales de ChatGPT no salen en tu historial pero pueden guardarse hasta 30 días. Los de Gemini, y "
         "los chats con Guardar actividad desactivado, se guardan 72 horas y no se usan para mejorar la IA de Google con revisores."),
        ("Borra lo que ya no necesites.",
         f"Los chats borrados de ChatGPT se eliminan en 30 días, con excepciones ({a(OAI_DELETE, 'OpenAI')}). Gemini los "
         "borra solo a los 18 meses por defecto; puedes elegir 3 meses. Los que ya leyó un revisor quedan hasta 3 años."),
        ("Lo privado de verdad, déjalo en el móvil.",
         f"Usa una IA que funcione en el dispositivo, como <a href=\"{PINKU_STORE}\">Pinku</a>. Descarga un modelo una vez, "
         "activa el modo avión y pregunta: si responde, nada de lo que escribiste salió del iPhone."),
    ],
    after=f"""
<h2>Dejarlo en el móvil: las opciones</h2>

<p>Un modelo local es mucho más pequeño que ChatGPT: flojea en preguntas difíciles, no
busca en internet y recuerda menos de la conversación. Para reescribir un mensaje
privado, resumir un documento que pegas o pensar en voz alta sobre algo personal basta,
y no hay ningún servidor del que fiarse.</p>

<ul>
<li><strong>Pinku</strong> (versión 1.1, 22 de octubre de 2026). Ejecuta 11 modelos abiertos en
iPhone o Mac con MLX de Apple, de Qwen3 0.6B (0,4 GB) a Qwen3 8B (4,7 GB); funciona en modo avión una vez
descargado el modelo; sin cuenta; los chats se guardan solo en el dispositivo. Gratis con Gemma 3 1B;
Pinku Pro (anual o compra única) deja elegir cualquier modelo y añade instrucciones personalizadas,
dictado en el dispositivo y lectura en voz alta. Requiere iOS 18.6. Es más flojo que un modelo en la
nube y solo muestra los modelos para los que tu aparato tiene memoria.</li>
<li><strong>Locally AI by LM Studio</strong> (gratis, 1.66.0): Llama, Gemma, Qwen y otros en iPhone y iPad con MLX, sin registro.</li>
<li><strong>Private LLM</strong> (4,99 $ en pago único en EE. UU., 1.9.16): modelos locales en iPhone y iPad.</li>
<li><strong>PocketPal AI</strong> (gratis, 1.20.1): ejecuta modelos en el dispositivo para chatear sin conexión.</li>
<li><strong>Enclave</strong> (gratis, 1.77.0): asistente local; su versión actual pide iOS 27.</li>
<li><strong>El modelo de Apple</strong>: en iPhone con Apple Intelligence, la acción Usar modelo de Atajos en modo En el
dispositivo funciona {a(SHORTCUTS_MODEL, "sin conexión a la red")}.</li>
</ul>

<p>Versiones y precios del App Store de EE. UU. el 23 de octubre de 2026. Las comparamos a
fondo, también donde ganan a Pinku, en <a href="../../blog/es/mejores-apps-ia-privada-iphone.html">las
mejores apps de IA privada que guardan tus chats en el iPhone</a>. Para comprobarlo tú con
cualquier app: <a href="comprobar-si-una-app-de-ia-guarda-tus-chats-en-el-iphone.html">cómo comprobar
si una app de chat con IA guarda de verdad tus chats en el iPhone</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(GEMINI_HUB + "?hl=es", "Google, Centro de privacidad de las Apps de Gemini")}, leído el 23 de octubre de 2026.</li>
<li>Etiquetas de privacidad del App Store de {a(CHATGPT_AS, "ChatGPT")}, {a(GEMINI_AS, "Google Gemini")} y {a(PINKU_AS, "Pinku")}, tienda de EE. UU., leídas el 23 de octubre de 2026.</li>
<li>Centro de ayuda de OpenAI sobre {a(OAI_DELETE, "conservación de chats")} y {a(OAI_TRAIN, "entrenamiento")}, citado en <a href="../../blog/what-ai-chatbots-keep-when-you-delete-chats.html">nuestro artículo del 20 de octubre de 2026</a>.</li>
<li>{a(SHORTCUTS_MODEL, "Apple, Manual de Atajos: Usar modelo")}.</li>
</ul>
""",
    faq=[
        ("¿Es seguro contarle cosas privadas a ChatGPT?",
         "Para preguntas generales, sí. Para lo que te identifique a ti o a otra persona, no: los chats se guardan en tu "
         "cuenta, pueden usarse para entrenar si no lo desactivas y las propias empresas piden no compartir información "
         "confidencial. Quita nombres y números antes, o usa una IA que funcione en el móvil."),
        ("¿Pueden leer mis chats en OpenAI o en Google?",
         "Google dice que revisores humanos leen algunos chats de Gemini y que los guarda hasta 3 años, desvinculados de tu "
         "cuenta. OpenAI guarda los chats hasta que los borras y puede revisarlos por seguridad. Ninguno es un diario privado."),
        ("¿Borrar un chat de ChatGPT lo elimina del todo?",
         "Desaparece al momento y OpenAI dice que lo elimina en 30 días, salvo que ya estuviera anonimizado o deba "
         "conservarlo por seguridad o por obligación legal."),
        ("¿Un chat temporal protege mis datos?",
         "En parte. Los chats temporales de ChatGPT no salen en tu historial pero pueden guardarse hasta 30 días. Los de "
         "Gemini, 72 horas. Los dos pasan por los servidores de la empresa."),
        ("¿Cómo uso IA sin que mis chats salgan del móvil?",
         "Con una app que ejecute el modelo en el dispositivo, como Pinku, Locally AI, Private LLM o PocketPal AI. Pruébala "
         "en modo avión: si sigue respondiendo, la conversación se queda en el móvil."),
    ],
)

# --------------------------------------------------------------------------
# Photo Vault: antes de prestar el iPhone o llevarlo a reparar
# --------------------------------------------------------------------------

SERVICE = "https://support.apple.com/en-us/109519"
SERVICE_ES = "https://support.apple.com/es-es/109519"
GUIDED = "https://support.apple.com/en-us/111795"
GUIDED_ES = "https://support.apple.com/es-es/111795"
LOCKAPP = "https://support.apple.com/guide/iphone/lock-or-hide-an-app-iph00f208d05/ios"
LOCKAPP_ES = "https://support.apple.com/es-es/guide/iphone/iph00f208d05/ios"
HIDDEN = "https://support.apple.com/en-us/104987"
HIDDEN_ES = "https://support.apple.com/es-es/104987"
PV_AS = "https://apps.apple.com/us/app/id1532670722"

PV3_EN = dict(
    path="photo-vault/before-lending-iphone-or-taking-it-to-repair.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D23,
    h1="What to do before lending your iPhone or taking it to repair (2026)",
    desc=("Checklist with the exact iOS menus: Guided Access and locked apps before you lend your iPhone; backup, "
          "Wallet, and Find My's Ready for Repair or Trade-In (iOS 27) before a repair, from Apple's support page "
          "published 15 September 2026; and how to keep private photos safe through both."),
    section="Guides", kicker="Photo Vault guide",
    standfirst=("Lending your phone for five minutes and leaving it at a repair shop for three days are different "
                "risks. Here is what iOS already gives you for each, and where a photo vault fits."),
    tools=["iPhone Settings", "Find My", "Photo Vault: Hide Pics Video"],
    intro=f"""
<p><strong>We make Photo Vault, which appears in this guide.</strong> Most steps use
only what is built into iOS.</p>

<h2>Lending your iPhone for a few minutes</h2>

<p>The safest way to lend a phone is to lend <em>one app</em>. iOS calls this
{a(GUIDED, "Guided Access")}: Settings, Accessibility, Guided Access, turn it on and set a
Guided Access passcode in Passcode Settings. Then open the app you want to lend (Safari,
Camera, a game), triple-click the side button and tap Start. The other person cannot
leave that app; you end the session with another triple-click and your passcode or Face
ID. Apple notes it is useful “when you let a child use your device”.</p>

<p>For apps you never want opened, iOS 18 and later let you
{a(LOCKAPP, "lock or hide an app")}: touch and hold its icon, tap Require Face ID (or Touch
ID or Passcode). Apple says information inside a locked app does not appear in
notification previews, search, Siri suggestions or your call history. Hide and Require
Face ID also moves it to a locked Hidden folder; built-in apps can be locked but not hidden.</p>

<p>Photos is where most accidents happen: someone swipes one photo too far. The
{a(HIDDEN, "Hidden album")} is locked by default since iOS 16, and in Settings, Apps,
Photos you can turn off Show Hidden Album so it does not appear at all. With iCloud
Photos on, a photo you hide is hidden on your other devices too, but it is still part
of your library.</p>

<h2>Taking it to repair</h2>

<p>Apple's checklist, {a(SERVICE, "Prepare your iPhone or iPad for a service appointment")}
(published 15 September 2026), changed with iOS 27. You no longer turn off Find My. Instead,
in the Find My app, select your iPhone, tap More, tap Repair or Trade In, then Enable: this is
<em>Ready for Repair or Trade-In</em>. On iOS 26 or earlier you still turn off Find My in Settings,
your name, Find My. iOS has no separate “maintenance mode” that hides your data from a
technician, so the backup and what you leave on the phone matter.</p>

<p>Two lines on that page are worth reading twice: <em>“Never give your Apple Account password,
device passcode, or account security details to anyone else. Neither Apple nor Apple Authorized
Service Providers will ask for this information.”</em> If a software test needs your passcode,
Apple says to type it yourself and stay present while the technician has the device. And when
you get it back, it “might have been erased”.</p>
""",
    steps=[
        ("Back up the iPhone.",
         f"iCloud or a computer. Apple also asks you to check that iCloud has finished syncing: Settings, your name, "
         f"iCloud, and the Saved to iCloud status should be green ({a(SERVICE, 'Apple')})."),
        ("Back up anything that is not in that backup.",
         f"Some apps keep data out of iCloud backups on purpose. <a href=\"{PV_STORE}\">Photo Vault</a>, for one, excludes "
         "its vault from regular iCloud backups: before a repair that may erase the phone, export its encrypted backup "
         "(Settings, Backup) to Files or a computer, or turn on its optional iCloud copy."),
        ("Lock or hide the apps you never lend.",
         "Touch and hold the icon, Require Face ID. Banking, messages, notes, photos and your vault are the usual ones."),
        ("To lend it, start Guided Access.",
         "Settings, Accessibility, Guided Access on, set its passcode. Open the app you are lending, triple-click the side "
         "button, tap Start. Triple-click again to end it."),
        ("Before a repair, remove Wallet cards and Apple Cash.",
         "Wallet, choose a card, More, Card Details, Remove Card. Turn off Apple Cash in Settings, Wallet &amp; Apple Pay."),
        ("Turn on Ready for Repair or Trade-In.",
         "On iOS 27: Find My app, your iPhone, More, Repair or Trade In, Enable. On iOS 26 or earlier: Settings, your name, "
         "Find My, turn off Find My iPhone."),
        ("Do not hand over your passcode.",
         "Type it yourself if a test needs it and stay with the phone. Apple and its authorised providers will not ask for it."),
        ("When it comes back, restore and switch things back on.",
         "Restore from your backup if it was erased, turn Find My back on if you turned it off, and restore your vault from "
         "its exported file or iCloud copy."),
    ],
    after=f"""
<h2>Where a photo vault fits</h2>

<p>Guided Access protects you for five minutes. A locked app protects one app. A vault
keeps private photos out of the Photos library altogether, so they do not appear in
Recents, Memories, search or a slideshow someone starts by accident. What
{a(PV_AS, "Photo Vault's App Store listing")} says (version 1.2.9, read 23 October 2026):
Face ID, Touch ID or a passcode to open it; a separate password per album; a disguised
icon (Calculator, Notes or Weather); a face-down exit to Safari, Calendar or Messages; a
private camera; an encrypted, password-locked backup file; an optional iCloud copy,
encrypted so only you can open it; no account and no server. It is free to try; Premium,
with 7 days free and then yearly, unlocks unlimited photos and videos.</p>

<p>What it does not do: it does not protect anything outside the vault, and because the
vault is excluded from regular iCloud backups, a phone erased during a repair loses it
unless you exported a backup or turned on the iCloud copy. If you only need to hide a
few photos, the free Hidden album may be enough.</p>

<h2>Alternatives</h2>
<ul>
<li><strong>Nothing to install:</strong> the Hidden album, locked apps and Guided Access, above. Step by step in
<a href="hide-photos-iphone-without-an-app.html">how to hide photos on iPhone without installing an app</a>.</li>
<li><strong>Private Photo Vault - Pic Safe</strong> (Legendary Software Labs, free, 25.8, 4.82 from about 1,018,000 ratings).</li>
<li><strong>Secret Photo Vault: Keepsafe</strong> (free, 13.34.0, 4.75 from about 385,000 ratings).</li>
<li><strong>Private Photo Vault - Arca</strong> (Pacifiq, free, 1.37): no server, no account.</li>
</ul>
<p>US App Store, 23 October 2026. Compared in detail in <a href="../blog/best-photo-vault-apps-iphone.html">the best
photo vault apps for iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(SERVICE, "Apple, Prepare your iPhone or iPad for a service appointment (109519)")}, published 15 September 2026, read 23 October 2026.</li>
<li>{a(GUIDED, "Apple, Use Guided Access on iPhone or iPad (111795)")}.</li>
<li>{a(LOCKAPP, "Apple, iPhone User Guide: Lock or hide an app")}.</li>
<li>{a(HIDDEN, "Apple, Hide photos with the Hidden album (104987)")}.</li>
<li>{a(PV_AS, "Photo Vault on the App Store")}, version 1.2.9, read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("How do I lend my iPhone without someone seeing my photos?",
         "Use Guided Access: Settings, Accessibility, Guided Access. Open the one app you want to lend, triple-click the side "
         "button and tap Start. The other person cannot leave that app until you triple-click and enter your passcode."),
        ("Do I have to turn off Find My before a repair?",
         "Not on iOS 27. Apple now asks you to turn on Ready for Repair or Trade-In in the Find My app (your device, More, "
         "Repair or Trade In, Enable). On iOS 26 or earlier you turn off Find My."),
        ("Does iPhone have a maintenance mode for repairs?",
         "Not as of iOS 27. Apple's service checklist does not include one. Back up, remove Wallet cards, turn on Ready for "
         "Repair or Trade-In and do not share your passcode."),
        ("Should I give the repair shop my passcode?",
         "No. Apple says neither Apple nor its authorised service providers will ask for it. If a test needs it, type it "
         "yourself and stay with the phone."),
        ("Will my hidden photos survive a repair?",
         "Photos in the Hidden album are part of your library, so they are in your iCloud or computer backup. A vault app may "
         "not be: Photo Vault is excluded from regular iCloud backups, so export its backup or turn on its iCloud copy first."),
    ],
)

PV3_ES = dict(
    path="photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D23,
    h1="Qué hacer antes de prestar el iPhone o llevarlo a reparar (2026)",
    desc=("Lista con los menús exactos de iOS: Acceso guiado y apps bloqueadas antes de prestar el iPhone; copia, Cartera y "
          "«Listo para la reparación o renovación» de Buscar (iOS 27) antes de una reparación, según la página de Apple "
          "publicada el 15 de septiembre de 2026; y cómo proteger las fotos privadas en los dos casos."),
    section="Guías", kicker="Guía de Photo Vault",
    standfirst=("Prestar el móvil cinco minutos y dejarlo tres días en un taller son riesgos distintos. Esto es lo que "
                "iOS ya trae para cada uno, y dónde encaja una bóveda de fotos."),
    tools=["Ajustes del iPhone", "Buscar", "Photo Vault: Hide Pics Video"],
    intro=f"""
<p><strong>Hacemos Photo Vault, que aparece en esta guía.</strong> Casi todos los pasos
usan solo lo que trae iOS.</p>

<h2>Prestar el iPhone unos minutos</h2>

<p>Lo más seguro es prestar <em>una sola app</em>. iOS lo llama
{a(GUIDED_ES, "Acceso guiado")}: Ajustes, Accesibilidad, Acceso guiado, actívalo y define
un código en Ajustes del código. Luego abre la app que vas a prestar (Safari, Cámara, un
juego), haz triple clic en el botón lateral y toca Iniciar. La otra persona no puede salir
de esa app; terminas la sesión con otro triple clic y tu código o Face ID. Apple dice que es
útil «cuando dejas que un niño use tu dispositivo».</p>

<p>Para las apps que no quieres que nadie abra, desde iOS 18 puedes
{a(LOCKAPP_ES, "bloquear u ocultar una app")}: mantén pulsado su icono y toca «Requerir Face ID»
(o Touch ID o código). Según Apple, lo que hay dentro de una app bloqueada no aparece en las
previsualizaciones de notificaciones, la búsqueda, las sugerencias de Siri ni el historial de
llamadas. «Ocultar y requerir Face ID» la lleva además a una carpeta Oculto bloqueada; las apps
que vienen con el iPhone se pueden bloquear pero no ocultar.</p>

<p>En Fotos es donde pasan los accidentes: alguien desliza una foto de más. El
{a(HIDDEN_ES, "álbum Oculto")} está bloqueado por defecto desde iOS 16, y en Ajustes, Apps,
Fotos puedes desactivar Mostrar el Álbum Oculto para que ni aparezca. Con Fotos en iCloud,
una foto que ocultas se oculta también en tus otros dispositivos, pero sigue en tu fototeca.</p>

<h2>Llevarlo a reparar</h2>

<p>La lista de Apple, {a(SERVICE_ES, "Preparar tu iPhone o iPad para una cita de servicio")}
(publicada el 15 de septiembre de 2026), cambió con iOS 27. Ya no se desactiva Buscar: en la
app Buscar seleccionas el iPhone, tocas Más, Reparación o Renovación y Activar. Es
<em>Listo para la reparación o renovación</em>. En iOS 26 o anterior se sigue desactivando
Buscar en Ajustes, tu nombre, Buscar. iOS no tiene un «modo mantenimiento» aparte que oculte
tus datos al técnico, así que importan la copia y lo que dejas en el móvil.</p>

<p>Dos frases de esa página merecen releerse: <em>«Nunca des a nadie la contraseña de tu cuenta
de Apple, el código del dispositivo o los detalles de seguridad de tu cuenta. Ni Apple ni ningún
proveedor de servicio autorizado Apple solicitarán esta información.»</em> Si una prueba de
software necesita tu código, Apple dice que lo introduzcas tú y te quedes presente. Y al
devolvértelo, puede que el dispositivo «se haya borrado».</p>
""",
    steps=[
        ("Haz una copia de seguridad del iPhone.",
         f"En iCloud o en un ordenador. Apple pide además comprobar que iCloud terminó de sincronizar: Ajustes, tu nombre, "
         f"iCloud, y el estado de Guardado en iCloud debe estar en verde ({a(SERVICE_ES, 'Apple')})."),
        ("Guarda aparte lo que no entra en esa copia.",
         f"Algunas apps dejan sus datos fuera de las copias de iCloud a propósito. <a href=\"{PV_STORE}\">Photo Vault</a>, por "
         "ejemplo, excluye la bóveda de las copias normales de iCloud: antes de una reparación que puede borrar el móvil, "
         "exporta su copia cifrada (Ajustes, Copia de seguridad) a Archivos o a un ordenador, o activa su copia opcional en iCloud."),
        ("Bloquea u oculta las apps que nunca prestas.",
         "Mantén pulsado el icono y toca Requerir Face ID. Banco, mensajes, notas, fotos y la bóveda son las habituales."),
        ("Para prestarlo, inicia Acceso guiado.",
         "Ajustes, Accesibilidad, Acceso guiado activado y con código. Abre la app que prestas, triple clic en el botón "
         "lateral, Iniciar. Otro triple clic para terminar."),
        ("Antes de reparar, quita las tarjetas de Cartera y Apple Cash.",
         "Cartera, elige una tarjeta, Más, Detalles de la tarjeta, Eliminar tarjeta. Desactiva Apple Cash en Ajustes, Cartera y Apple Pay."),
        ("Activa Listo para la reparación o renovación.",
         "En iOS 27: app Buscar, tu iPhone, Más, Reparación o Renovación, Activar. En iOS 26 o anterior: Ajustes, tu nombre, "
         "Buscar, desactiva Buscar mi iPhone."),
        ("No entregues tu código.",
         "Introdúcelo tú si una prueba lo necesita y quédate con el móvil. Apple y sus proveedores autorizados no te lo pedirán."),
        ("Cuando vuelva, restaura y reactiva.",
         "Restaura la copia si lo borraron, vuelve a activar Buscar si lo desactivaste y recupera la bóveda desde su archivo "
         "exportado o su copia en iCloud."),
    ],
    after=f"""
<h2>Dónde encaja una bóveda de fotos</h2>

<p>El Acceso guiado te protege cinco minutos. Una app bloqueada protege esa app. Una bóveda
saca las fotos privadas de la fototeca, así que no salen en Recientes, Recuerdos, la búsqueda
ni un pase de diapositivas que alguien inicia sin querer. Lo que dice
{a(PV_AS, "la ficha de Photo Vault en el App Store")} (versión 1.2.9, leída el 23 de octubre de 2026):
Face ID, Touch ID o código para abrirla; contraseña distinta por álbum; icono disfrazado
(Calculadora, Notas o Tiempo); al poner el móvil boca abajo salta a Safari, Calendario o
Mensajes; cámara privada; copia de seguridad cifrada con contraseña; copia opcional en tu
iCloud, cifrada para que solo tú la abras; sin cuenta y sin servidor. Se puede probar gratis;
Premium, con 7 días gratis y luego anual, desbloquea fotos y vídeos ilimitados.</p>

<p>Lo que no hace: no protege nada fuera de la bóveda y, como la bóveda está fuera de las copias
normales de iCloud, un móvil borrado en una reparación la pierde si no exportaste una copia o
activaste la copia en iCloud. Si solo quieres esconder unas pocas fotos, el álbum Oculto, gratis,
puede bastar.</p>

<h2>Alternativas</h2>
<ul>
<li><strong>Sin instalar nada:</strong> álbum Oculto, apps bloqueadas y Acceso guiado, arriba. Paso a paso en
<a href="ocultar-fotos-iphone-sin-instalar-app.html">cómo ocultar fotos en el iPhone sin instalar ninguna app</a>.</li>
<li><strong>Private Photo Vault - Pic Safe</strong> (Legendary Software Labs, gratis, 25.8, 4,82 con unas 1.018.000 valoraciones en EE. UU.).</li>
<li><strong>Secret Photo Vault: Keepsafe</strong> (gratis, 13.34.0, 4,75 con unas 385.000 valoraciones).</li>
<li><strong>Private Photo Vault - Arca</strong> (Pacifiq, gratis, 1.37): sin servidor y sin cuenta.</li>
</ul>
<p>App Store de EE. UU., 23 de octubre de 2026. Comparadas a fondo en
<a href="../../blog/es/apps-para-ocultar-fotos-iphone.html">las mejores apps para ocultar fotos en iPhone</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(SERVICE_ES, "Apple, Preparar tu iPhone o iPad para una cita de servicio (109519)")}, publicada el 15 de septiembre de 2026, leída el 23 de octubre de 2026.</li>
<li>{a(GUIDED_ES, "Apple, Utilizar el acceso guiado en el iPhone o iPad (111795)")}.</li>
<li>{a(LOCKAPP_ES, "Apple, Manual del iPhone: bloquear u ocultar una app")}.</li>
<li>{a(HIDDEN_ES, "Apple, Ocultar fotos con el álbum Oculto (104987)")}.</li>
<li>{a(PV_AS, "Photo Vault en el App Store")}, versión 1.2.9, leída el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Cómo presto el iPhone sin que vean mis fotos?",
         "Con Acceso guiado: Ajustes, Accesibilidad, Acceso guiado. Abre la única app que quieres prestar, haz triple clic en "
         "el botón lateral y toca Iniciar. La otra persona no sale de esa app hasta que hagas triple clic y pongas tu código."),
        ("¿Tengo que desactivar Buscar antes de una reparación?",
         "En iOS 27, no. Apple pide activar Listo para la reparación o renovación en la app Buscar (tu dispositivo, Más, "
         "Reparación o Renovación, Activar). En iOS 26 o anterior se desactiva Buscar."),
        ("¿El iPhone tiene un modo mantenimiento para reparaciones?",
         "No a fecha de iOS 27; la lista de Apple no lo incluye. Haz copia, quita las tarjetas de Cartera, activa Listo para "
         "la reparación o renovación y no compartas tu código."),
        ("¿Debo dar mi código al taller?",
         "No. Apple dice que ni Apple ni sus proveedores autorizados lo pedirán. Si una prueba lo necesita, introdúcelo tú y "
         "quédate con el móvil."),
        ("¿Mis fotos ocultas sobreviven a una reparación?",
         "Las del álbum Oculto forman parte de tu fototeca, así que van en tu copia de iCloud o del ordenador. Las de una "
         "bóveda puede que no: Photo Vault está fuera de las copias normales de iCloud, así que exporta su copia o activa su "
         "copia en iCloud antes."),
    ],
)

# --------------------------------------------------------------------------
# Drop: ruido marron, rosa o blanco
# --------------------------------------------------------------------------

RIEDY = "https://pubmed.ncbi.nlm.nih.gov/33007706/"
HUGH = "https://pubmed.ncbi.nlm.nih.gov/24590753/"
ZHOU = "https://pubmed.ncbi.nlm.nih.gov/22726808/"
PAPA = "https://pubmed.ncbi.nlm.nih.gov/28337134/"
NIGG = "https://pubmed.ncbi.nlm.nih.gov/38428577/"
BGS = "https://support.apple.com/en-us/109346"
BGS_ES = "https://support.apple.com/es-es/109346"
BGS_GUIDE = "https://support.apple.com/guide/iphone/play-background-sounds-iphb2cfa052c/ios"
BGS_GUIDE_ES = "https://support.apple.com/es-es/guide/iphone/iphb2cfa052c/ios"
AINSIDER = "https://appleinsider.com/articles/21/07/23/how-to-use-rain-dark-noise-and-more-background-sounds-in-ios-15"
DROP_AS = "https://apps.apple.com/us/app/id1462269642"

DR2_EN = dict(
    path="drop/brown-noise-vs-pink-noise-vs-white-noise.html",
    app_name="Sleep Sounds & Focus: Drop",
    date_iso=ISO, date=D23_U24, modified_iso="2026-10-24",
    h1="Brown noise vs pink noise vs white noise: which one for sleep, focus or a baby (2026)",
    desc=("What white, pink and brown noise are, what the studies actually found for sleep (a 2021 review of 38 studies), "
          "focus (a 2024 meta-analysis on ADHD) and babies (a 2014 Pediatrics study of 14 sleep machines), and how to play "
          "each on iPhone. Sources with dates; no health claims beyond them."),
    section="Guides", kicker="Drop guide",
    standfirst=("Pick the one you find least annoying, keep it quiet, and do not expect a miracle: that is roughly what "
                "the research supports. The details, with the studies linked."),
    tools=["iPhone Background Sounds", "a sleep sound app"],
    intro=f"""
<p><strong>We make Drop, a sleep and calm sounds app that plays white, pink and brown noise.</strong> It is one option among several: the iPhone's built-in sounds and the other apps listed below also do it. We say where Drop fits at the end.</p>

<h2>The difference in one table</h2>

<div class="table-scroll">
<table>
<thead><tr><th></th><th>White noise</th><th>Pink noise</th><th>Brown noise</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>Equal energy at every frequency</td><td>Energy falls as pitch rises (equal per octave)</td><td>Energy falls faster still; mostly low frequencies</td></tr>
<tr><td>Sounds like</td><td>Static, a hiss, a TV between channels</td><td>Steady rain</td><td>A waterfall, a deep rumble</td></tr>
<tr><td>Sleep</td><td colspan="3">Evidence for continuous noise of any colour is very low quality (Riedy 2021). One small study found more stable sleep with pink noise (Zhou 2012).</td></tr>
<tr><td>Focus</td><td colspan="2">Small benefit in people with ADHD; slightly worse performance in people without it (Nigg 2024)</td><td>No studies found (Nigg 2024)</td></tr>
<tr><td>Baby</td><td colspan="3">Volume and distance matter more than colour: all 14 machines tested at full volume were above the hospital nursery limit at 30 cm (Hugh 2014)</td></tr>
</tbody>
</table>
</div>

<p>The “sounds like” row follows the 2024 meta-analysis by Nigg and colleagues, which
describes white noise as sounding “like static” and pink or brown noise as having
“more power in the lower frequencies” and sounding “like rain or a waterfall”.</p>

<h2>For sleep</h2>

<p>The most complete look at the question is a systematic review by Riedy, Smith, Rocha and
Basner at the University of Pennsylvania ({a(RIEDY, "Sleep Medicine Reviews, 2021")}). It
covered 38 studies of continuous white or similar broadband noise and sleep. Results ranged
from noise improving sleep to noise disrupting it, and under the GRADE criteria the quality of
evidence that continuous noise improves sleep was <em>very low</em>. The authors warn it “may
also negatively affect sleep and hearing”.</p>

<p>Pink noise has some extra interest. In a small study ({a(ZHOU, "Zhou et al., Journal of Theoretical Biology, 2012")}), 40 people slept a night with steady pink noise and a night in
quiet, and the noise nights showed a higher share of stable sleep. A different line of
research plays short <em>pulses</em> of pink noise timed to deep-sleep brain waves: in 13 older
adults ({a(PAPA, "Papalambros et al., 2017")}) it increased slow-wave activity and next-day word
recall. That needs EEG equipment in a lab; a pink noise track on your phone does not do it.</p>

<p>We found no controlled study of brown noise for sleep. Brown noise is popular on social
media; the research has not caught up.</p>

<p>In practice: if a steady sound masks the traffic or the neighbours, use the colour you find
least irritating, at the lowest volume that works, and use a timer.</p>

<h2>For focus</h2>

<p>A 2024 meta-analysis ({a(NIGG, "Nigg et al., Journal of the American Academy of Child and Adolescent Psychiatry")}) pooled 13 studies with 335 children and young adults with ADHD or
ADHD symptoms. White and pink noise gave a small improvement on lab attention tasks. In people
without ADHD (11 studies, 335 people), they made performance slightly <em>worse</em>. The
authors found no studies of brown noise at all.</p>

<h2>For a baby</h2>

<p>Researchers in Toronto measured 14 infant sleep machines at maximum volume
({a(HUGH, "Hugh et al., Pediatrics, 2014")}). At 30 cm every one was louder than 50 dBA, the
recommended limit for hospital nurseries, and three exceeded 85 dBA, the level that over 8
hours breaks adult workplace limits. The colour of the noise did not come into it. Put the
phone or machine well away from the cot, keep the volume low, and use a timer; ask your
paediatrician if you are unsure.</p>
""",
    steps=[
        ("Try the noise built into your iPhone.",
         f"Settings, Accessibility, Audio &amp; Visual, Background Sounds, turn it on ({a(BGS_GUIDE, 'Apple')}). The sounds "
         f"include Balanced Noise, Bright Noise and Dark Noise, plus Ocean, Rain and Stream ({a(AINSIDER, 'AppleInsider')}). "
         "Apple does not say which colour of noise each one is."),
        ("Shape it with the Equalizer.",
         "On iOS 26 or later, Background Sounds has an Equalizer: tap it and drag across the grid to cut the high or low "
         "frequencies until it sounds right to you."),
        ("Set a timer.",
         "In the same screen, Stop Sound with a Timer. You can also start and stop Background Sounds from Control Center."),
        ("Keep the volume low.",
         "Use the lowest level that covers the noise you want to mask. For a baby, put the phone well away from the cot."),
        ("If you want true brown or pink noise, use an app that names it.",
         "White Noise Lite, myNoise, Rain Rain, Endel and Drop list it on the App Store (details below)."),
        ("If noise is not for you, try nature sounds or slow breathing.",
         f"Rain or ocean is easier on the ear for many people. <a href=\"{DROP_STORE}\">Drop</a> has rain, ocean and other nature sounds and a guided "
         "breathing timer."),
    ],
    after=f"""
<h2>Apps that play pink or brown noise (App Store, 23 October 2026)</h2>
<ul>
<li><strong>White Noise Lite</strong> (TMSoft, free with ads, 8.7.3, 4.82 from about 278,000 ratings): its sound list
includes Brown Noise, Pink Noise, White Noise, Blue Noise and Violet Noise, with a mixer and fading timer.</li>
<li><strong>myNoise</strong> (free, 3.21.77): its “White Noise &amp; Co” soundscape covers white, brown, green, grey and pink
noise, each with its own sliders.</li>
<li><strong>Rain Rain Sleep Sounds</strong> (free, 6.9.10): lists Pink Noise among 50+ sounds, with a free mixer and fade-out timer.</li>
<li><strong>Endel</strong> (free, Premium for Colored Noise): “choose one of 9 colors of noise”.</li>
<li><strong>Dark Noise</strong> (free, 3.6.1): 50+ ambient sounds, custom mixes and a fade-out timer.</li>
<li><strong>Drop</strong> (free, 2.10, 24 October 2026): White Noise free; Pink Noise, Brown Noise and Deep Brown Noise with Drop Pro, among 53 sounds. One sound at a time, no mixer or equaliser, sleep timer with fade-out.</li>
</ul>

<h2>Where Drop fits</h2>

<p>{a(DROP_AS, "Drop's App Store listing")} (version 2.10, 24 October 2026) describes nature sounds (gentle rain, crystal dewdrops, crackling campfire, mystical forest, ocean waves), guided breathing sessions of 2, 5, 10 and 20 minutes, widgets, a plant that grows as you practise, offline use and no ads. Version 2.10 has 53 sounds, 9 of them free. White noise is free; pink, brown and deep brown noise come with Drop Pro. They are fixed looped tracks, one at a time, so if you want to shape the colour or layer it with rain, myNoise or White Noise Lite do more. If you tried brown or pink noise and found it grating, rain or ocean with a few minutes of slow breathing is the other route it offers.
More on <a href="../drop.html">Drop's page</a>, and the step by step in
<a href="white-noise-to-fall-asleep-iphone.html">how to use white noise to fall asleep on iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(RIEDY, "Riedy SM et al. Noise as a sleep aid: a systematic review. Sleep Med Rev 2021;55:101385")}.</li>
<li>{a(HUGH, "Hugh SC et al. Infant sleep machines and hazardous sound pressure levels. Pediatrics 2014;133(4):677-81")}.</li>
<li>{a(ZHOU, "Zhou J et al. Pink noise: effect on complexity synchronization of brain activity and sleep consolidation. J Theor Biol 2012;306:68-72")}.</li>
<li>{a(PAPA, "Papalambros NA et al. Acoustic enhancement of sleep slow oscillations and concomitant memory improvement in older adults. Front Hum Neurosci 2017;11:109")}.</li>
<li>{a(NIGG, "Nigg JT et al. Do white noise or pink noise help with task performance in youth with ADHD? J Am Acad Child Adolesc Psychiatry 2024;63(8):778-788")}.</li>
<li>{a(BGS, "Apple, Use Background Sounds to help with sleep, focus, and more (109346)")} and {a(BGS_GUIDE, "Play background sounds on iPhone")}, read 23 October 2026.</li>
<li>App Store listings of the apps above, US store, read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Is brown noise better than white noise for sleep?",
         "There is no study showing that. A 2021 review of 38 studies rated the evidence that any continuous noise improves "
         "sleep as very low quality, and we found no controlled study of brown noise and sleep. Use whichever you find least "
         "irritating, quietly."),
        ("Is pink noise good for sleep?",
         "One small 2012 study found more stable sleep with steady pink noise. Lab studies that play pink noise pulses timed "
         "to deep-sleep brain waves improved memory in older adults, but that is not the same as a pink noise track."),
        ("Which noise is best for focus or ADHD?",
         "A 2024 meta-analysis found a small benefit of white and pink noise for people with ADHD and a small negative effect "
         "for people without it. It found no studies of brown noise."),
        ("Is white noise safe for a baby?",
         "The concern is volume. A 2014 study found all 14 infant sleep machines exceeded 50 dBA at 30 cm at full volume. Keep "
         "the device far from the cot, at low volume, with a timer, and ask your paediatrician."),
        ("Can I play brown noise on iPhone without an app?",
         "iPhone's Background Sounds (Settings, Accessibility, Audio & Visual) has Balanced, Bright and Dark Noise. Apple does "
         "not label them by colour."),
        ("Does Drop have brown or pink noise?",
         "Yes, since version 2.10 (24 October 2026). White noise is free; pink, brown and deep brown noise come with Drop Pro. "
         "For free coloured noise, use the iPhone's Background Sounds or White Noise Lite."),
    ],
)

DR2_ES = dict(
    path="drop/es/ruido-marron-rosa-o-blanco.html",
    app_name="Sleep Sounds & Focus: Drop",
    date_iso=ISO, date=D23_U24, modified_iso="2026-10-24",
    h1="Ruido marrón, rosa o blanco: cuál para dormir, concentrarse o para un bebé (2026)",
    desc=("Qué son el ruido blanco, rosa y marrón, qué encontraron de verdad los estudios para dormir (una revisión de 38 "
          "estudios de 2021), concentrarse (un metaanálisis de 2024 sobre TDAH) y bebés (un estudio de Pediatrics de 2014 con "
          "14 máquinas) y cómo poner cada uno en el iPhone. Fuentes con fecha, sin afirmaciones de salud más allá de ellas."),
    section="Guías", kicker="Guía de Drop",
    standfirst=("Elige el que menos te moleste, ponlo bajo y no esperes milagros: eso es, más o menos, lo que respalda "
                "la investigación. Los detalles, con los estudios enlazados."),
    tools=["Sonidos de fondo del iPhone", "una app de sonidos para dormir"],
    intro=f"""
<p><strong>Hacemos Drop, una app de sonidos para dormir y relajarse que tiene ruido blanco, rosa y marrón.</strong> Es una opción más: los sonidos del propio iPhone y las otras apps de la lista también lo hacen. Al final decimos dónde encaja Drop.</p>

<h2>La diferencia en una tabla</h2>

<div class="table-scroll">
<table>
<thead><tr><th></th><th>Ruido blanco</th><th>Ruido rosa</th><th>Ruido marrón</th></tr></thead>
<tbody>
<tr><td>Qué es</td><td>La misma energía en todas las frecuencias</td><td>La energía baja al subir el tono (igual por octava)</td><td>Baja todavía más deprisa; sobre todo graves</td></tr>
<tr><td>Suena como</td><td>Estática, un siseo, una tele sin señal</td><td>Lluvia constante</td><td>Una cascada, un retumbar grave</td></tr>
<tr><td>Dormir</td><td colspan="3">La evidencia de que un ruido continuo de cualquier color mejore el sueño es de calidad muy baja (Riedy 2021). Un estudio pequeño vio un sueño más estable con ruido rosa (Zhou 2012).</td></tr>
<tr><td>Concentración</td><td colspan="2">Pequeña mejora en personas con TDAH; algo peor en personas sin TDAH (Nigg 2024)</td><td>Sin estudios (Nigg 2024)</td></tr>
<tr><td>Bebé</td><td colspan="3">Importan más el volumen y la distancia que el color: las 14 máquinas medidas a volumen máximo superaban a 30 cm el límite de las salas de neonatos (Hugh 2014)</td></tr>
</tbody>
</table>
</div>

<p>La fila «suena como» sigue el metaanálisis de Nigg y colaboradores de 2024, que describe
el ruido blanco como «estática» y el rosa o el marrón como ruidos con «más potencia en las
frecuencias bajas» que suenan «como lluvia o una cascada».</p>

<h2>Para dormir</h2>

<p>La revisión más completa es la de Riedy, Smith, Rocha y Basner, de la Universidad de
Pensilvania ({a(RIEDY, "Sleep Medicine Reviews, 2021")}). Reunió 38 estudios sobre ruido blanco
continuo u otro ruido de banda ancha y sueño. Los resultados iban de que el ruido mejora el
sueño a que lo empeora, y con los criterios GRADE la calidad de la evidencia de que lo mejore
era <em>muy baja</em>. Los autores avisan de que «también puede afectar negativamente al sueño
y al oído».</p>

<p>El ruido rosa tiene algo más. En un estudio pequeño ({a(ZHOU, "Zhou y otros, Journal of Theoretical Biology, 2012")}), 40 personas durmieron una noche con ruido rosa constante y otra
en silencio, y las noches con ruido tuvieron más proporción de sueño estable. Otra línea de
investigación emite <em>pulsos</em> cortos de ruido rosa sincronizados con las ondas del sueño
profundo: en 13 adultos mayores ({a(PAPA, "Papalambros y otros, 2017")}) aumentó la actividad de
ondas lentas y el recuerdo de palabras al día siguiente. Eso exige un electroencefalograma en un
laboratorio; una pista de ruido rosa en el móvil no lo hace.</p>

<p>No encontramos ningún estudio controlado sobre ruido marrón y sueño. Es muy popular en redes;
la investigación no ha llegado todavía.</p>

<p>En la práctica: si un sonido constante tapa el tráfico o a los vecinos, usa el color que menos
te moleste, al volumen más bajo que funcione, y con temporizador.</p>

<h2>Para concentrarse</h2>

<p>Un metaanálisis de 2024 ({a(NIGG, "Nigg y otros, Journal of the American Academy of Child and Adolescent Psychiatry")}) juntó 13 estudios con 335 niños y jóvenes con TDAH o síntomas de TDAH.
El ruido blanco y el rosa dieron una mejora pequeña en tareas de atención de laboratorio. En
personas sin TDAH (11 estudios, 335 personas) empeoraron un poco el rendimiento. No encontraron
ningún estudio con ruido marrón.</p>

<h2>Para un bebé</h2>

<p>Investigadores de Toronto midieron 14 máquinas de ruido para bebés a volumen máximo
({a(HUGH, "Hugh y otros, Pediatrics, 2014")}). A 30 cm todas superaban los 50 dBA, el límite
recomendado en las salas de neonatos, y tres pasaban de 85 dBA, el nivel que durante 8 horas
supera los límites laborales para adultos. El color del ruido no influía. Pon el móvil o la
máquina lejos de la cuna, a volumen bajo y con temporizador; ante la duda, pregunta al pediatra.</p>
""",
    steps=[
        ("Prueba el ruido que trae el iPhone.",
         f"Ajustes, Accesibilidad, Audio y efectos visuales, Sonidos de fondo, y actívalo ({a(BGS_GUIDE_ES, 'Apple')}). Los sonidos "
         f"incluyen ruido equilibrado, brillante y oscuro (Balanced, Bright y Dark Noise), además de océano, lluvia y arroyo "
         f"({a(AINSIDER, 'AppleInsider')}). Apple no dice qué color es cada uno."),
        ("Ajústalo con el ecualizador.",
         "En iOS 26 o posterior, Sonidos de fondo tiene Ecualizador: actívalo y arrastra por la cuadrícula para quitar agudos o "
         "graves hasta que te suene bien."),
        ("Pon un temporizador.",
         "En la misma pantalla, la opción de detener el sonido con temporizador. También puedes activarlo desde el centro de control."),
        ("Mantén el volumen bajo.",
         "El más bajo que tape el ruido que quieres ocultar. Para un bebé, el móvil lejos de la cuna."),
        ("Si quieres ruido marrón o rosa de verdad, usa una app que lo nombre.",
         "White Noise Lite, myNoise, Rain Rain, Endel y Drop lo indican en el App Store (detalles abajo)."),
        ("Si el ruido no es lo tuyo, prueba sonidos de la naturaleza o respiración lenta.",
         f"La lluvia o el mar resultan más agradables a mucha gente. <a href=\"{DROP_STORE}\">Drop</a> tiene lluvia, mar y otros sonidos de la "
         "naturaleza y un temporizador de respiración guiada."),
    ],
    after=f"""
<h2>Apps con ruido rosa o marrón (App Store, 23 de octubre de 2026)</h2>
<ul>
<li><strong>White Noise Lite</strong> (TMSoft, gratis con anuncios, 8.7.3, 4,82 con unas 278.000 valoraciones en EE. UU.):
su lista incluye Brown Noise, Pink Noise, White Noise, Blue Noise y Violet Noise, con mezclador y temporizador con fundido.</li>
<li><strong>myNoise</strong> (gratis, 3.21.77): su paisaje «White Noise &amp; Co» cubre ruido blanco, marrón, verde, gris y rosa,
cada uno con sus controles.</li>
<li><strong>Rain Rain Sleep Sounds</strong> (gratis, 6.9.10): incluye Pink Noise entre más de 50 sonidos, con mezclador gratis.</li>
<li><strong>Endel</strong> (gratis; Colored Noise es Premium): «elige uno de 9 colores de ruido».</li>
<li><strong>Dark Noise</strong> (gratis, 3.6.1): más de 50 sonidos ambientales, mezclas y temporizador con fundido.</li>
<li><strong>Drop</strong> (gratis, 2.10, 24 de octubre de 2026): ruido blanco gratis; ruido rosa, marrón y marrón profundo con Drop Pro, entre 53 sonidos. Un sonido cada vez, sin mezclador ni ecualizador, temporizador con fundido.</li>
</ul>

<h2>Dónde encaja Drop</h2>

<p>{a(DROP_AS, "La ficha de Drop en el App Store")} (versión 2.10, 24 de octubre de 2026) describe sonidos de la naturaleza (lluvia suave, gotas de rocío, hoguera, bosque, olas del mar), sesiones de respiración guiada de 2, 5, 10 y 20 minutos, widgets, una planta que crece con la práctica, uso sin conexión y sin anuncios. La 2.10 tiene 53 sonidos, 9 gratis. El ruido blanco es gratis; el rosa, el marrón y el marrón profundo van con Drop Pro. Son pistas fijas en bucle, una cada vez, así que si quieres ajustar el color o mezclarlo con lluvia, myNoise o White Noise Lite hacen más. Si probaste el marrón o el rosa y se te hizo pesado, lluvia u océano con unos minutos de respiración lenta es la otra vía que ofrece.
Más en <a href="../../drop.html">la página de Drop</a> y el paso a paso en
<a href="ruido-blanco-para-dormir-iphone.html">cómo usar ruido blanco para dormirte con el iPhone</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(RIEDY, "Riedy SM y otros. Noise as a sleep aid: a systematic review. Sleep Med Rev 2021;55:101385")}.</li>
<li>{a(HUGH, "Hugh SC y otros. Infant sleep machines and hazardous sound pressure levels. Pediatrics 2014;133(4):677-81")}.</li>
<li>{a(ZHOU, "Zhou J y otros. Pink noise: effect on complexity synchronization of brain activity and sleep consolidation. J Theor Biol 2012;306:68-72")}.</li>
<li>{a(PAPA, "Papalambros NA y otros. Acoustic enhancement of sleep slow oscillations and concomitant memory improvement in older adults. Front Hum Neurosci 2017;11:109")}.</li>
<li>{a(NIGG, "Nigg JT y otros. Do white noise or pink noise help with task performance in youth with ADHD? J Am Acad Child Adolesc Psychiatry 2024;63(8):778-788")}.</li>
<li>{a(BGS_ES, "Apple, Utilizar Sonidos de fondo (109346)")} y {a(BGS_GUIDE_ES, "Reproducir sonidos de fondo en el iPhone")}, leídos el 23 de octubre de 2026.</li>
<li>Fichas del App Store de las apps citadas, tienda de EE. UU., leídas el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Es mejor el ruido marrón que el blanco para dormir?",
         "No hay estudios que lo demuestren. Una revisión de 2021 de 38 estudios calificó de muy baja la calidad de la evidencia "
         "de que cualquier ruido continuo mejore el sueño, y no encontramos estudios controlados sobre ruido marrón y sueño. Usa "
         "el que menos te moleste, bajo."),
        ("¿El ruido rosa ayuda a dormir?",
         "Un estudio pequeño de 2012 vio un sueño más estable con ruido rosa constante. Los estudios de laboratorio con pulsos de "
         "ruido rosa sincronizados con el sueño profundo mejoraron la memoria en adultos mayores, pero eso no es lo mismo que una pista de ruido rosa."),
        ("¿Qué ruido va mejor para concentrarse o para el TDAH?",
         "Un metaanálisis de 2024 vio una mejora pequeña con ruido blanco y rosa en personas con TDAH y un pequeño efecto negativo "
         "en personas sin TDAH. No encontró estudios con ruido marrón."),
        ("¿Es seguro el ruido blanco para un bebé?",
         "Lo que preocupa es el volumen. Un estudio de 2014 vio que las 14 máquinas para bebés superaban 50 dBA a 30 cm a volumen "
         "máximo. Aparato lejos de la cuna, volumen bajo, temporizador, y consulta al pediatra."),
        ("¿Puedo poner ruido marrón en el iPhone sin instalar nada?",
         "Sonidos de fondo (Ajustes, Accesibilidad, Audio y efectos visuales) tiene ruido equilibrado, brillante y oscuro. Apple no "
         "los etiqueta por color."),
        ("¿Drop tiene ruido marrón o rosa?",
         "Sí, desde la versión 2.10 (24 de octubre de 2026). El ruido blanco es gratis; el rosa, el marrón y el marrón profundo van "
         "con Drop Pro. Para ruido de colores gratis, usa Sonidos de fondo del iPhone o White Noise Lite."),
    ],
)

# --------------------------------------------------------------------------
# 3 Tasks: el metodo de 3 tareas
# --------------------------------------------------------------------------

IVY = "https://jamesclear.com/ivy-lee"
BAILEY = "https://chrisbailey.com/rule-of-three/"
COWAN = "https://pubmed.ncbi.nlm.nih.gov/11515286/"
TT_AS = "https://apps.apple.com/us/app/id1553693943"

TT_EN = dict(
    path="3-tasks/3-task-method-ivy-lee-rule-of-3.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D23,
    h1="The 3-task method (Ivy Lee and the Rule of 3): how to plan your day with only 3 tasks",
    desc=("Where the 3-task idea comes from (Ivy Lee's 1918 method actually used six tasks; the Rule of 3 is J.D. Meier's, "
          "popularised by Chris Bailey), how to plan a day with three tasks step by step, and the apps and paper setups "
          "that make it stick. App data checked on the App Store on 23 October 2026."),
    section="Guides", kicker="3 Tasks guide",
    standfirst=("Write down the three things that would make today a good day, do the first one first, and carry the "
                "rest over. That is the whole method; here is how to make it work."),
    tools=["paper or a to-do app", "3 Tasks"],
    intro=f"""
<p><strong>We make 3 Tasks, a to-do app that holds three tasks a day, and it is one of the
options below.</strong> The method works just as well on paper.</p>

<h2>Where the idea comes from</h2>

<p><strong>Ivy Lee, 1918.</strong> The story, as James Clear tells it from Scott Cutlip's history of
public relations, is that Charles Schwab, president of Bethlehem Steel, asked the consultant Ivy Lee
how to get more done, tried his answer for three months and paid him $25,000
({a(IVY, "jamesclear.com/ivy-lee")}). The method was: at the end of each day, write down the
<em>six</em> most important things for tomorrow, no more; put them in order of importance; next day
work only on the first until it is finished; at the end of the day move what is left to a new list of
six; repeat. So the famous method is six tasks, not three, and the story is told second-hand.</p>

<p><strong>The Rule of 3.</strong> The three comes from J.D. Meier's book <em>Getting Results the Agile
Way</em> (2010), and was popularised by Chris Bailey: write down three things you want to accomplish
today, three this week and three this year ({a(BAILEY, "chrisbailey.com, 15 April 2025")}). Bailey's
reasons: it shows you your real daily capacity, forces you to choose what not to do, and three things
are easy to remember.</p>

<p>Why three rather than six? Neither source proves a magic number. A widely cited review of memory
research puts what people can hold in mind at once at about four items
({a(COWAN, "Cowan, Behavioral and Brain Sciences, 2001")}), which is one reason a list of three is easy
to keep in your head all day. Six gives more room on days of small tasks; three forces harder choices.</p>
""",
    steps=[
        ("Write tomorrow's candidates the evening before.",
         "Dump everything that could be done tomorrow. This list can be long; it is not your plan."),
        ("Pick three that would make the day a success.",
         "Choose outcomes, not activities: “send the proposal” rather than “work on the proposal”. If one is too big to finish "
         "in a day, cut it down until it fits."),
        ("Put them in order.",
         "Number one is the task you would do if you could only do one. Ivy Lee's rule: nothing else until it is finished."),
        ("Start with number one before email and messages.",
         "Give it the first block of the day. A timer helps you notice how long it really takes."),
        ("Treat everything else as extra.",
         "Meetings, replies and small chores still happen, but only around the three, and nothing new joins the list today."),
        ("At the end of the day, carry over and choose again.",
         "Unfinished tasks go back into tomorrow's candidates, not automatically onto tomorrow's three. Choose again."),
        ("Once a week, check the three for the week.",
         "Bailey's version: three goals for the week and three for the year, so the daily three point somewhere."),
    ],
    after=f"""
<h2>Tools that work for it (App Store, 23 October 2026)</h2>

<ul>
<li><strong>Paper or a sticky note.</strong> Three lines on a card on your desk is the original version, and it cannot
grow into a 40-item list.</li>
<li><strong><a href="{TT_STORE}">3 Tasks</a></strong> (version 1.3.0, 21 October 2026). From {a(TT_AS, "its listing")}: three
daily priorities on one screen; a start and pause timer on every task that keeps counting with the screen locked; Repeat
Daily for a task that comes back each morning; a home screen widget with your three tasks; dark mode. Free, with no ads
and no account. 3 Tasks Pro, a one-time purchase with no subscription, adds history with the time each task took, a streak,
CSV export and four colour themes. It uses Firebase Analytics to count how timers and tasks are used. It has no backlog
or project lists: it is only the three.</li>
<li><strong>Top 3: Daily Focus Tasks</strong> (free, 1.2.0): “built around one rule: focus on only three important tasks per day”.</li>
<li><strong>Three Todo</strong> ($0.99, 2.9.5): keeps a backlog and shows three at a time.</li>
<li><strong>TickTick</strong> (free, 8.2.30, 4.86 from about 46,600 ratings): a full to-do app; use its four priority levels and
show only today's top priority.</li>
<li><strong>Structured</strong> (free, 4.6.6, 4.79 from about 168,000 ratings): a day planner on a timeline, if you prefer
to give each of the three a time slot.</li>
</ul>

<p>Compared in detail in <a href="../blog/best-3-task-todo-apps-iphone.html">the best to-do apps that limit you to 3
tasks a day</a>. More about the app on <a href="../3things.html">the 3 Tasks page</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(IVY, "James Clear, The Ivy Lee Method")}, read 23 October 2026 (cites Scott M. Cutlip, <em>The Unseen Power</em>, pp. 118-119).</li>
<li>{a(BAILEY, "Chris Bailey, The Rule of 3")}, published 15 April 2025.</li>
<li>J.D. Meier, <em>Getting Results the Agile Way</em>, 2010.</li>
<li>{a(COWAN, "Cowan N. The magical number 4 in short-term memory. Behav Brain Sci 2001;24(1):87-114")}.</li>
<li>App Store listings of 3 Tasks, Top 3, Three Todo, TickTick and Structured, US store, read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("What is the Ivy Lee method?",
         "A 1918 productivity method: each evening write the six most important tasks for tomorrow, rank them, work on the first "
         "until it is done, then the next, and move unfinished ones to the next day's list of six."),
        ("Is the Ivy Lee method three tasks or six?",
         "Six. The three-task version is the Rule of 3, from J.D. Meier's Getting Results the Agile Way, popularised by Chris Bailey."),
        ("What is the Rule of 3 for productivity?",
         "Write down three things you want to accomplish today, three this week and three this year, and set new daily ones each day."),
        ("What if I finish my three tasks early?",
         "Pick the next most important item from your candidates, or stop. The point is that the day already counts as a good one."),
        ("What happens to tasks I did not finish?",
         "They go back into tomorrow's candidate list, and you choose the three again. In Ivy Lee's version they move to the next "
         "day's list."),
        ("Is there an app that only allows 3 tasks a day?",
         "Yes: 3 Tasks and Top 3 are built around three tasks a day; Three Todo shows three at a time from a backlog."),
    ],
)

TT_ES = dict(
    path="3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html",
    app_name="To Do List & Focus: 3 Tasks",
    date_iso=ISO, date=D23,
    h1="El método de las 3 tareas (Ivy Lee y la regla de 3): cómo planificar el día con solo 3 tareas",
    desc=("De dónde sale la idea de las 3 tareas (el método de Ivy Lee de 1918 eran en realidad seis; la regla de 3 es de "
          "J.D. Meier y la popularizó Chris Bailey), cómo planificar un día con tres tareas paso a paso y qué apps o qué papel "
          "ayudan a mantenerlo. Datos de apps comprobados en el App Store el 23 de octubre de 2026."),
    section="Guías", kicker="Guía de 3 Tasks",
    standfirst=("Apunta las tres cosas que harían de hoy un buen día, haz primero la primera y pasa el resto al día "
                "siguiente. Ese es todo el método; así se consigue que funcione."),
    tools=["papel o una app de tareas", "3 Tasks"],
    intro=f"""
<p><strong>Hacemos 3 Tasks, una app de tareas que admite tres al día, y es una de las
opciones de abajo.</strong> El método funciona igual de bien en papel.</p>

<h2>De dónde sale la idea</h2>

<p><strong>Ivy Lee, 1918.</strong> La historia, tal como la cuenta James Clear a partir de la historia de
las relaciones públicas de Scott Cutlip, es que Charles Schwab, presidente de Bethlehem Steel, preguntó
al consultor Ivy Lee cómo hacer más, probó su respuesta tres meses y le pagó 25.000 dólares
({a(IVY, "jamesclear.com/ivy-lee")}). El método: al final de cada día, apunta las <em>seis</em> cosas más
importantes para mañana, ni una más; ordénalas por importancia; al día siguiente trabaja solo en la
primera hasta acabarla; al final del día pasa lo pendiente a una nueva lista de seis; repite. O sea, el
método famoso son seis tareas, no tres, y la historia nos llega de segunda mano.</p>

<p><strong>La regla de 3.</strong> El tres viene del libro de J.D. Meier <em>Getting Results the Agile
Way</em> (2010), y lo popularizó Chris Bailey: apunta tres cosas que quieres conseguir hoy, tres esta
semana y tres este año ({a(BAILEY, "chrisbailey.com, 15 de abril de 2025")}). Sus razones: te enseña tu
capacidad real de cada día, te obliga a elegir qué no hacer y tres cosas se recuerdan fácil.</p>

<p>¿Por qué tres y no seis? Ninguna de las dos fuentes demuestra un número mágico. Una revisión muy
citada sobre la memoria sitúa en unos cuatro elementos lo que podemos tener en mente a la vez
({a(COWAN, "Cowan, Behavioral and Brain Sciences, 2001")}), una razón de que una lista de tres se lleve
en la cabeza todo el día. Seis dan más margen en días de tareas pequeñas; tres obligan a elegir más.</p>
""",
    steps=[
        ("Apunta la víspera las candidatas de mañana.",
         "Vuelca todo lo que podrías hacer mañana. Esta lista puede ser larga; no es tu plan."),
        ("Elige tres que harían del día un éxito.",
         "Resultados, no actividades: «enviar la propuesta» y no «trabajar en la propuesta». Si una es demasiado grande para un "
         "día, recórtala hasta que quepa."),
        ("Ponlas en orden.",
         "La número uno es la que harías si solo pudieras hacer una. Regla de Ivy Lee: nada más hasta terminarla."),
        ("Empieza por la número uno antes del correo y los mensajes.",
         "Dale el primer bloque del día. Un temporizador ayuda a ver cuánto tarda de verdad."),
        ("Todo lo demás es extra.",
         "Las reuniones, respuestas y recados siguen ahí, pero alrededor de las tres, y hoy no entra nada nuevo en la lista."),
        ("Al acabar el día, pasa lo pendiente y vuelve a elegir.",
         "Lo que no terminaste vuelve a las candidatas de mañana, no directamente a las tres de mañana. Elige otra vez."),
        ("Una vez por semana, repasa las tres de la semana.",
         "La versión de Bailey: tres objetivos para la semana y tres para el año, para que las tres de cada día apunten a algo."),
    ],
    after=f"""
<h2>Herramientas que sirven (App Store, 23 de octubre de 2026)</h2>

<ul>
<li><strong>Papel o una nota adhesiva.</strong> Tres líneas en una tarjeta sobre la mesa es la versión original, y no puede
crecer hasta 40 tareas.</li>
<li><strong><a href="{TT_STORE}">3 Tasks</a></strong> (versión 1.3.0, 21 de octubre de 2026). Según {a(TT_AS, "su ficha")}:
tres prioridades diarias en una sola pantalla; un temporizador de inicio y pausa en cada tarea que sigue contando con la
pantalla bloqueada; Repeat Daily para una tarea que vuelve cada mañana; widget con tus tres tareas; modo oscuro. Gratis, sin
anuncios y sin cuenta. 3 Tasks Pro, pago único sin suscripción, añade historial con el tiempo de cada tarea, racha, exportación
a CSV y cuatro temas de color. Usa Firebase Analytics para contar cómo se usan los temporizadores y las tareas. No tiene
bandeja de pendientes ni proyectos: solo las tres.</li>
<li><strong>Top 3: Daily Focus Tasks</strong> (gratis, 1.2.0): «construida alrededor de una regla: centrarse solo en tres tareas importantes al día».</li>
<li><strong>Three Todo</strong> (0,99 $ en EE. UU., 2.9.5): guarda una lista de pendientes y enseña tres cada vez.</li>
<li><strong>TickTick</strong> (gratis, 8.2.30, 4,86 con unas 46.600 valoraciones en EE. UU.): app de tareas completa; usa sus cuatro
niveles de prioridad y muestra solo la máxima de hoy.</li>
<li><strong>Structured</strong> (gratis, 4.6.6, 4,79 con unas 168.000 valoraciones): agenda del día en línea de tiempo, si prefieres
dar a cada una de las tres su hueco.</li>
</ul>

<p>Comparadas a fondo en <a href="../../blog/es/mejores-apps-3-tareas-al-dia-iphone.html">las mejores apps de tareas que te
limitan a 3 al día</a>. Más sobre la app en <a href="../../3things.html">la página de 3 Tasks</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(IVY, "James Clear, The Ivy Lee Method")}, leído el 23 de octubre de 2026 (cita a Scott M. Cutlip, <em>The Unseen Power</em>, pp. 118-119).</li>
<li>{a(BAILEY, "Chris Bailey, The Rule of 3")}, publicado el 15 de abril de 2025.</li>
<li>J.D. Meier, <em>Getting Results the Agile Way</em>, 2010.</li>
<li>{a(COWAN, "Cowan N. The magical number 4 in short-term memory. Behav Brain Sci 2001;24(1):87-114")}.</li>
<li>Fichas del App Store de 3 Tasks, Top 3, Three Todo, TickTick y Structured, tienda de EE. UU., leídas el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Qué es el método Ivy Lee?",
         "Un método de productividad de 1918: cada tarde apunta las seis tareas más importantes de mañana, ordénalas, trabaja en la "
         "primera hasta acabarla, luego en la siguiente, y pasa las pendientes a la lista de seis del día siguiente."),
        ("¿El método Ivy Lee son tres tareas o seis?",
         "Seis. La versión de tres es la regla de 3, del libro de J.D. Meier Getting Results the Agile Way, que popularizó Chris Bailey."),
        ("¿Qué es la regla de 3 de productividad?",
         "Apuntar tres cosas que quieres conseguir hoy, tres esta semana y tres este año, y fijar las del día cada día."),
        ("¿Y si termino las tres tareas pronto?",
         "Coge la siguiente más importante de tus candidatas, o para. La idea es que el día ya cuenta como bueno."),
        ("¿Qué pasa con las tareas que no terminé?",
         "Vuelven a las candidatas de mañana y eliges las tres otra vez. En la versión de Ivy Lee pasan a la lista del día siguiente."),
        ("¿Hay alguna app que solo deje 3 tareas al día?",
         "Sí: 3 Tasks y Top 3 están pensadas para tres tareas al día; Three Todo enseña tres cada vez de una lista de pendientes."),
    ],
)

GUIDES = [(PK3_EN, PK3_ES), (PV3_EN, PV3_ES), (DR2_EN, DR2_ES), (TT_EN, TT_ES)]
