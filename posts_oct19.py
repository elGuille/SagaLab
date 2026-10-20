# -*- coding: utf-8 -*-
"""Tres articulos del 19 oct 2026 (Pinku), EN y ES. Los pinta build_blog.py.

Datos comprobados el 19 oct 2026, todos enlazados en cada articulo:
- Apple Intelligence: support.apple.com/en-us/121115 (requisitos, idiomas, UE,
  China, limites diarios de las funciones con modelos en servidor),
  support.apple.com/en-us/127893 (Siri AI: beta, solo ingles, no en iPhone en la
  UE, historial por iCloud), apple.com/legal/privacy/data/en/intelligence-engine/
  (en el dispositivo o Private Cloud Compute, informe de PCC),
  support.apple.com/guide/shortcuts/tpg3vrvwmclv/ios (Use Model: On-Device sin
  red, Cloud, Cloud Pro, Extension Model), apple.com/os/ios/ (iOS 27 en iPhone 11
  y posteriores y SE de 2.a generacion), support.apple.com/en-us/102894 (Metal 3:
  iPhone 12 o posterior).
- Apps: API de lookup de iTunes (country=us y es) y la ficha web de cada app
  (compras y etiqueta de privacidad), 19 oct 2026.
- Pinku: repo Pinku (Metal 3 con supportsFamily(.metal3), modelos que no caben
  ocultos) y su ficha 1.0.9. Se evita dar el numero de modelos gratis y el precio
  de Pro porque cambian con la 1.1 (en revision a partir del 21 oct).
Sin rayas en el texto.
"""
import json

from posts import LINKEDIN, _head, _jsonld, _faq_html

DATE_ISO = "2026-10-19"
DATE = {"en": "19 October 2026", "es": "19 de octubre de 2026"}

# Nuestra app: ct.py pone el ct= de cada pagina al construir.
PINKU = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=aisagalab&amp;mt=8"

_IDS = dict(locally="6741426692", pocketpal="6502579498", privatellm="6448106860",
            enclave="6476614556", chatgpt="6448311069", gemini="6477489729",
            claude="6473753684", vibe="6740410176")


def _store(lang):
    cc = "us" if lang == "en" else "es"
    return {k: "https://apps.apple.com/%s/app/id%s" % (cc, v) for k, v in _IDS.items()}


AI_REQS = "https://support.apple.com/en-us/121115"
AI_REQS_ES = "https://support.apple.com/es-es/121115"
SIRI_AI = "https://support.apple.com/en-us/127893"
SIRI_AI_ES = "https://support.apple.com/es-es/127893"
AI_PRIVACY = "https://www.apple.com/legal/privacy/data/en/intelligence-engine/"
AI_PRIVACY_ES = "https://www.apple.com/legal/privacy/data/es/intelligence-engine/"
SHORTCUTS = "https://support.apple.com/guide/shortcuts/tpg3vrvwmclv/ios"
SHORTCUTS_ES = "https://support.apple.com/es-es/guide/shortcuts/tpg3vrvwmclv/ios"
IOS27 = "https://www.apple.com/os/ios/"
IOS27_ES = "https://www.apple.com/es/os/ios/"
METAL = "https://support.apple.com/en-us/102894"
METAL_ES = "https://support.apple.com/es-es/102894"
POCKETPAL_GH = "https://github.com/a-ghorbani/pocketpal-ai"

_X = ' target="_blank" rel="noopener"'


def _links(lang):
    d = dict(_store(lang), pinku=PINKU, x=_X, gh=POCKETPAL_GH, date=DATE[lang])
    if lang == "en":
        d.update(reqs=AI_REQS, siri=SIRI_AI, priv=AI_PRIVACY, sc=SHORTCUTS, ios=IOS27, metal=METAL)
    else:
        d.update(reqs=AI_REQS_ES, siri=SIRI_AI_ES, priv=AI_PRIVACY_ES, sc=SHORTCUTS_ES, ios=IOS27_ES,
                 metal=METAL_ES)
    return d


def _box(title, points):
    return ('\n<div class="article-note rank-box">\n<p><strong>%s</strong></p>\n<ul>\n%s\n</ul>\n</div>\n'
            % (title, "\n".join("<li>%s</li>" % p for p in points)))


# ==========================================================================
# 1. Does Apple Intelligence work offline? (guia, Pinku)
# ==========================================================================

OFF_STEPS = {
    "en": [
        ("Turn on the report.",
         "Go to Settings, Privacy &amp; Security, Apple Intelligence &amp; PCC Report, and choose a report "
         "duration. On a Mac it is in System Settings, Privacy &amp; Security."),
        ("Use the feature you are unsure about.",
         "Rewrite a paragraph, make an image, ask Siri something: whatever you want to check."),
        ("Export the report and read it.",
         "Apple says the report shows the requests sent off your device and processed by Private Cloud "
         "Compute, and, if you turned on Apple Intelligence Extensions such as ChatGPT, the requests sent "
         "to them. If your request is not there, it was handled on the iPhone."),
        ("Confirm it in airplane mode.",
         "Turn on airplane mode, with Wi-Fi and Bluetooth off, and try the same feature again. If it "
         "still works, it runs on the device."),
    ],
    "es": [
        ("Activa el informe.",
         "Ve a Ajustes, Privacidad y seguridad, Informe de Apple Intelligence, y elige cu&aacute;nto "
         "tiempo cubre. En el Mac est&aacute; en Ajustes del Sistema, Privacidad y seguridad."),
        ("Usa la funci&oacute;n que quieres comprobar.",
         "Reescribe un p&aacute;rrafo, crea una imagen, preg&uacute;ntale algo a Siri: lo que quieras mirar."),
        ("Exporta el informe y l&eacute;elo.",
         "Apple dice que el informe muestra las peticiones que salieron del dispositivo y se procesaron "
         "en Private Cloud Compute y, si activaste extensiones de Apple Intelligence como ChatGPT, las que "
         "se les enviaron. Si tu petici&oacute;n no aparece, se resolvi&oacute; en el iPhone."),
        ("Conf&iacute;rmalo en modo avi&oacute;n.",
         "Activa el modo avi&oacute;n, con la wifi y el Bluetooth apagados, y vuelve a probar. Si sigue "
         "funcionando, se ejecuta en el dispositivo."),
    ],
}

OFF_EN_BODY = """
<p><strong>Disclosure: we make Pinku, an offline AI chat app mentioned near the
end.</strong> Everything about Apple Intelligence below comes from Apple's own
support and privacy pages, linked in the text and checked on %(date)s.</p>

<h2>The short answer</h2>

<p>Partly. Apple Intelligence is not one model in one place. Apple's privacy page
says that <a href="%(priv)s"%(x)s>&ldquo;in many cases, Apple Intelligence models run
entirely on device&rdquo;</a>, and that when a task needs more computing power than
the device has, &ldquo;Apple Intelligence may send your request to Private Cloud
Compute&rdquo;, Apple's own servers. Its example is Image Playground: your description
goes to Private Cloud Compute, which makes the image.</p>

<p>Apple also lists the features that <a href="%(reqs)s"%(x)s>&ldquo;rely on
server-side models&rdquo;</a> and therefore have daily usage limits: Siri AI,
Intelligent Photo Editing Tools, Image Playground and the AFM 3 Cloud models in
Shortcuts. Those need a connection. What Apple does not publish is a
feature-by-feature list of what keeps working in airplane mode, so for everything
else you have to check on your own phone (steps below).</p>

<div class="table-scroll"><table>
<thead><tr><th>Feature</th><th>Where Apple says it runs</th><th>Without internet</th></tr></thead>
<tbody>
<tr><td>Siri AI (beta)</td><td>Listed among the features that rely on server-side models; goes to the web for up-to-date answers</td><td>Needs a connection</td></tr>
<tr><td>Image Playground</td><td>Private Cloud Compute (Apple's own example)</td><td>Needs a connection</td></tr>
<tr><td>Intelligent photo editing (Spatial Reframing, Extend, Improved Clean Up)</td><td>Listed among the features with server-side usage limits</td><td>Needs a connection</td></tr>
<tr><td>Shortcuts, Use Model: <em>On-Device</em></td><td>On the iPhone, &ldquo;without the need for a network connection&rdquo;</td><td>Works</td></tr>
<tr><td>Shortcuts, Use Model: <em>Cloud</em> and <em>Cloud Pro</em></td><td>Private Cloud Compute</td><td>Needs a connection</td></tr>
<tr><td>Shortcuts, Use Model: <em>Extension Model</em></td><td>ChatGPT</td><td>Needs a connection</td></tr>
<tr><td>Priority notifications</td><td>An on-device model (Apple's own example)</td><td>Runs on the device</td></tr>
<tr><td>Writing Tools, summaries and the rest</td><td>Apple does not say feature by feature</td><td>Check it yourself</td></tr>
</tbody>
</table></div>

<p class="article-note">Sources: Apple's <a href="%(reqs)s"%(x)s>Apple Intelligence
requirements page</a>, its <a href="%(priv)s"%(x)s>Apple Intelligence privacy
page</a> and the <a href="%(sc)s"%(x)s>Shortcuts user guide</a>, checked on
%(date)s.</p>

<h2>Is Private Cloud Compute private?</h2>

<p>It is designed to be. Apple says the data processed there &ldquo;is not stored or
made accessible to Apple&rdquo; and is used only to fulfil the request, and that the
limited information it does collect (request size, which feature, how long it took)
is not linked to your Apple Account. But it is still a request that leaves your
iPhone and is answered by a server. If what you want is a guarantee that a
conversation never leaves the device, or an assistant that works on a plane, a
server-side feature cannot give you that, however well it is protected.</p>

<p>Siri AI adds one more thing to know: Apple says its <a href="%(siri)s"%(x)s>Siri
app &ldquo;uses iCloud to privately sync your conversation history across your
devices&rdquo;</a>.</p>

<h2>Which iPhones get Apple Intelligence at all</h2>

<ul>
<li><strong>iPhone:</strong> iPhone 15 Pro and 15 Pro Max, all iPhone 16 models and
later, and iPhone Air. The iPhone 15, 15 Plus and every older iPhone do not get
it, even though <a href="%(ios)s"%(x)s>iOS 27 runs on iPhone 11 and later</a>.</li>
<li><strong>Storage:</strong> up to 8 GB on the device, and up to 14 GB on iPhone 17
Pro, 17 Pro Max and iPhone Air.</li>
<li><strong>Language:</strong> the device language and the Siri language must be
the same supported language. Siri AI itself is English only for now.</li>
<li><strong>Region:</strong> Apple Intelligence does not currently work on devices
bought in mainland China. In the EU the Apple Intelligence features across apps
are available, but <a href="%(siri)s"%(x)s>Siri AI is not available on iPhone</a>
(it is on Mac and Apple Vision Pro, in English).</li>
</ul>

<h2>How to see what left your iPhone</h2>

<p>Apple gives you a log of every request that went to its servers. This is the
most reliable way to answer the question for a specific feature.</p>
%(steps)s
<p>Apple notes that if Face ID or Touch ID are temporarily disabled, the report may
not show recent requests.</p>

<h2>An offline AI that is already on your iPhone: Shortcuts</h2>

<p>If your iPhone has Apple Intelligence, the Shortcuts app gives you a free model
that works without a connection. In a shortcut, add the <em>Use Model</em> action and
choose <em>On-Device</em>, which Apple describes as using &ldquo;the on-device Apple
Intelligence model to handle simple requests without the need for a network
connection&rdquo;. Apple calls it ideal for &ldquo;straightforward requests or simple
conversions&rdquo;: tidying a list, rewriting a sentence, pulling dates out of text.
It is a building block for automations, not a chat window, and the larger
<em>Cloud</em> and <em>Cloud Pro</em> models in the same action do need the
internet.</p>

<h2>If you want a full AI chat that works offline</h2>

<p>Apps that download an open model once and then answer on the phone, with no
server involved. They also work on iPhones without Apple Intelligence. The trade-off
is the same for all of them: a model of 1 to 5 GB is much weaker than a cloud model,
does not browse the web, and the first download needs the internet.</p>

<ul>
<li><a href="%(pinku)s">Pinku</a> (ours): iPhone and Mac, no account, chats stay
on the device. Needs iOS 18.6 and a Metal 3 iPhone, which Apple lists as
<a href="%(metal)s"%(x)s>iPhone 12 or later</a>. The default model is free; larger
models, custom instructions, dictation and read aloud need Pinku Pro, an in-app
purchase. Its App Store privacy label lists purchase history and a user ID, used
for purchases; no chat content.</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: free, iOS 18.1 or later,
label <em>Data Not Collected</em>.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: free and
<a href="%(gh)s"%(x)s>open source</a>, runs on iOS 15.1 or later, any GGUF model from
Hugging Face.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: $4.99 once, iOS 17 or later with an
A12 Bionic chip or newer, Siri and Shortcuts.</li>
</ul>

<p>We compared these in more detail, with prices and privacy labels, in
<a href="best-offline-ai-chat-apps-iphone-mac.html">the best offline AI chat apps for
iPhone and Mac</a>, and for older iPhones in
<a href="best-ai-apps-iphone-without-apple-intelligence.html">the best AI apps for
iPhones without Apple Intelligence</a>.</p>
"""

OFF_ES_BODY = """
<p><strong>Aviso: hacemos Pinku, una app de chat con IA sin conexi&oacute;n que sale
al final.</strong> Todo lo que decimos de Apple Intelligence sale de las p&aacute;ginas
de soporte y privacidad de Apple, enlazadas en el texto y comprobadas el
%(date)s.</p>

<h2>La respuesta corta</h2>

<p>En parte. Apple Intelligence no es un solo modelo en un solo sitio. La
p&aacute;gina de privacidad de Apple dice que <a href="%(priv)s"%(x)s>&laquo;en muchos
casos, los modelos de Apple Intelligence se ejecutan por completo en el
dispositivo&raquo;</a> y que, cuando una tarea necesita m&aacute;s potencia de la que
tiene el dispositivo, &laquo;Apple Intelligence puede enviar tu petici&oacute;n a Private
Cloud Compute&raquo;, los servidores de Apple. Su ejemplo es Image Playground: la
descripci&oacute;n va a Private Cloud Compute, que crea la imagen.</p>

<p>Apple tambi&eacute;n nombra las funciones que <a href="%(reqs)s"%(x)s>&laquo;dependen
de modelos en servidor&raquo;</a> y por eso tienen l&iacute;mites de uso diarios: Siri AI,
las herramientas inteligentes de edici&oacute;n de fotos, Image Playground y los
modelos AFM 3 en la nube de Atajos. Esas necesitan conexi&oacute;n. Lo que Apple no
publica es una lista, funci&oacute;n por funci&oacute;n, de lo que sigue funcionando en
modo avi&oacute;n; para lo dem&aacute;s hay que comprobarlo en tu propio iPhone (pasos
m&aacute;s abajo).</p>

<div class="table-scroll"><table>
<thead><tr><th>Funci&oacute;n</th><th>D&oacute;nde dice Apple que se ejecuta</th><th>Sin internet</th></tr></thead>
<tbody>
<tr><td>Siri AI (beta)</td><td>Entre las funciones que dependen de modelos en servidor; sale a la web para respuestas actuales</td><td>Necesita conexi&oacute;n</td></tr>
<tr><td>Image Playground</td><td>Private Cloud Compute (el ejemplo de Apple)</td><td>Necesita conexi&oacute;n</td></tr>
<tr><td>Edici&oacute;n inteligente de fotos (Spatial Reframing, Extend, Clean Up mejorado)</td><td>Entre las funciones con l&iacute;mites de uso en servidor</td><td>Necesita conexi&oacute;n</td></tr>
<tr><td>Atajos, acci&oacute;n Use Model: <em>On-Device</em></td><td>En el iPhone, &laquo;sin necesidad de conexi&oacute;n a la red&raquo;</td><td>Funciona</td></tr>
<tr><td>Atajos, Use Model: <em>Cloud</em> y <em>Cloud Pro</em></td><td>Private Cloud Compute</td><td>Necesita conexi&oacute;n</td></tr>
<tr><td>Atajos, Use Model: <em>Extension Model</em></td><td>ChatGPT</td><td>Necesita conexi&oacute;n</td></tr>
<tr><td>Notificaciones prioritarias</td><td>Un modelo en el dispositivo (el ejemplo de Apple)</td><td>En el dispositivo</td></tr>
<tr><td>Herramientas de escritura, res&uacute;menes y lo dem&aacute;s</td><td>Apple no lo detalla funci&oacute;n por funci&oacute;n</td><td>Compru&eacute;balo t&uacute;</td></tr>
</tbody>
</table></div>

<p class="article-note">Fuentes: la <a href="%(reqs)s"%(x)s>p&aacute;gina de
requisitos de Apple Intelligence</a>, la <a href="%(priv)s"%(x)s>p&aacute;gina de
privacidad de Apple Intelligence</a> y el <a href="%(sc)s"%(x)s>manual de
Atajos</a>, comprobadas el %(date)s. Las citas de Apple est&aacute;n traducidas del
ingl&eacute;s, y los nombres de las opciones de Atajos son los de su gu&iacute;a en ingl&eacute;s:
en un iPhone en espa&ntilde;ol pueden aparecer traducidos.</p>

<h2>&iquest;Es privado Private Cloud Compute?</h2>

<p>Est&aacute; pensado para serlo. Apple dice que los datos que se procesan ah&iacute;
&laquo;no se almacenan ni son accesibles para Apple&raquo; y que solo se usan para
resolver la petici&oacute;n, y que lo poco que recoge (tama&ntilde;o de la petici&oacute;n,
qu&eacute; funci&oacute;n, cu&aacute;nto tard&oacute;) no va unido a tu cuenta de Apple. Pero
sigue siendo una petici&oacute;n que sale del iPhone y la contesta un servidor. Si lo
que quieres es la garant&iacute;a de que una conversaci&oacute;n no sale nunca del
dispositivo, o un asistente que funcione en un avi&oacute;n, una funci&oacute;n en servidor
no te lo puede dar, por bien protegida que est&eacute;.</p>

<p>Con Siri AI hay algo m&aacute;s: Apple dice que su <a href="%(siri)s"%(x)s>app de
Siri &laquo;usa iCloud para sincronizar de forma privada tu historial de
conversaciones entre tus dispositivos&raquo;</a>.</p>

<h2>Qu&eacute; iPhone tienen Apple Intelligence</h2>

<ul>
<li><strong>iPhone:</strong> iPhone 15 Pro y 15 Pro Max, todos los iPhone 16 y
posteriores, y el iPhone Air. El iPhone 15, el 15 Plus y todos los anteriores no
lo tienen, aunque <a href="%(ios)s"%(x)s>iOS 27 funciona desde el iPhone 11</a>.</li>
<li><strong>Espacio:</strong> hasta 8 GB en el dispositivo, y hasta 14 GB en el
iPhone 17 Pro, el 17 Pro Max y el iPhone Air.</li>
<li><strong>Idioma:</strong> el idioma del dispositivo y el de Siri tienen que ser
el mismo, y uno de los admitidos (el espa&ntilde;ol lo es). Siri AI, por ahora, solo en
ingl&eacute;s.</li>
<li><strong>Regi&oacute;n:</strong> Apple Intelligence no funciona de momento en
dispositivos comprados en China continental. En la UE est&aacute;n las funciones de
Apple Intelligence en las apps, pero <a href="%(siri)s"%(x)s>Siri AI no est&aacute;
disponible en el iPhone</a> (s&iacute; en el Mac y en Apple Vision Pro, en ingl&eacute;s).
Si vives en Espa&ntilde;a, mira <a href="mejores-alternativas-siri-ai-iphone-ue.html">las
alternativas a Siri AI en el iPhone</a>.</li>
</ul>

<h2>C&oacute;mo ver qu&eacute; ha salido de tu iPhone</h2>

<p>Apple te da un registro de cada petici&oacute;n que fue a sus servidores. Es la
forma m&aacute;s fiable de saberlo para una funci&oacute;n concreta.</p>
%(steps)s
<p>Apple avisa de que, si Face ID o Touch ID est&aacute;n desactivados temporalmente,
el informe puede no mostrar las peticiones recientes.</p>

<h2>Una IA sin conexi&oacute;n que ya tienes en el iPhone: Atajos</h2>

<p>Si tu iPhone tiene Apple Intelligence, la app Atajos trae un modelo gratis que
funciona sin conexi&oacute;n. En un atajo, a&ntilde;ade la acci&oacute;n de usar un modelo
(<em>Use Model</em> en la gu&iacute;a de Apple) y elige el modelo del dispositivo
(<em>On-Device</em>), que seg&uacute;n Apple usa &laquo;el modelo de Apple
Intelligence del dispositivo para peticiones sencillas sin necesidad de conexi&oacute;n
a la red&raquo;. Apple lo recomienda para peticiones directas o conversiones
sencillas: ordenar una lista, reescribir una frase, sacar fechas de un texto. Es una
pieza para automatizar, no una ventana de chat, y los modelos m&aacute;s grandes de la
misma acci&oacute;n (<em>Cloud</em> y <em>Cloud Pro</em>) s&iacute; necesitan internet.</p>

<h2>Si quieres un chat de IA completo sin conexi&oacute;n</h2>

<p>Apps que descargan un modelo abierto una vez y despu&eacute;s contestan en el
m&oacute;vil, sin servidor. Tambi&eacute;n funcionan en iPhone sin Apple Intelligence. El
precio es el mismo en todas: un modelo de 1 a 5 GB es mucho m&aacute;s flojo que uno en
la nube, no busca en internet y la primera descarga necesita conexi&oacute;n.</p>

<ul>
<li><a href="%(pinku)s">Pinku</a> (nuestra): iPhone y Mac, sin cuenta, los chats se
quedan en el dispositivo. Pide iOS 18.6 y un iPhone con Metal 3, que Apple
lista como <a href="%(metal)s"%(x)s>iPhone 12 o posterior</a>. El modelo por defecto
es gratis; los modelos grandes, las instrucciones personalizadas, el dictado y la
lectura en voz alta van con Pinku Pro, una compra dentro de la app. Su etiqueta
de privacidad del App Store indica historial de compras e identificador de
usuario, para las compras; ning&uacute;n contenido de los chats.</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: gratis, iOS 18.1 o
posterior, etiqueta <em>Datos no recopilados</em>.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: gratis y de
<a href="%(gh)s"%(x)s>c&oacute;digo abierto</a>, desde iOS 15.1, cualquier modelo GGUF de
Hugging Face.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: 5,99 &euro; una vez, iOS 17 o
posterior con chip A12 Bionic o m&aacute;s nuevo, Siri y Atajos.</li>
</ul>

<p>Las comparamos con m&aacute;s detalle, con precios y etiquetas de privacidad, en
<a href="mejores-apps-ia-sin-conexion-iphone-mac.html">las mejores apps de IA sin
conexi&oacute;n para iPhone y Mac</a>, y para iPhone antiguos en
<a href="mejores-apps-ia-iphone-sin-apple-intelligence.html">las mejores apps de IA
para iPhone sin Apple Intelligence</a>.</p>
"""

OFF_FAQ = {
    "en": [
        ("Does Apple Intelligence work in airplane mode?",
         "Some of it. Apple says many requests run entirely on the device, and the On-Device model in "
         "Shortcuts works without a network connection. Features that rely on server-side models, which "
         "Apple lists as Siri AI, Intelligent Photo Editing Tools, Image Playground and the AFM 3 Cloud "
         "models in Shortcuts, need a connection."),
        ("Does Siri AI work offline?",
         "Expect it to need a connection. Apple lists Siri AI among the features that rely on server-side "
         "models and have daily usage limits, and says it goes out to the web for up-to-date information."),
        ("How can I tell if Apple Intelligence sent my request to a server?",
         "Turn on Settings, Privacy & Security, Apple Intelligence & PCC Report. Apple says it logs the "
         "requests processed by Private Cloud Compute and those sent to extensions such as ChatGPT. You "
         "can export it and look for your request."),
        ("Is Private Cloud Compute the same as the cloud?",
         "It is Apple's own servers. Apple says the data is not stored or made accessible to Apple and is "
         "only used to answer the request, but the request does leave your device."),
        ("Which iPhones have Apple Intelligence?",
         "iPhone 15 Pro, iPhone 15 Pro Max, all iPhone 16 models and later, and iPhone Air. The iPhone 15, "
         "15 Plus and older models do not, even on iOS 27."),
        ("Can I use an AI chat offline on an iPhone without Apple Intelligence?",
         "Yes, with an app that runs an open model on the phone, such as Pinku (iPhone 12 or later), "
         "Locally AI, PocketPal AI or Private LLM. You need the internet once to download the model."),
    ],
    "es": [
        ("¿Funciona Apple Intelligence en modo avión?",
         "En parte. Apple dice que muchas peticiones se ejecutan por completo en el dispositivo, y el "
         "modelo del dispositivo (On-Device) de la acción Use Model de Atajos funciona sin conexión. Las funciones que dependen de modelos "
         "en servidor, que Apple nombra como Siri AI, la edición inteligente de fotos, Image Playground y "
         "los modelos AFM 3 en la nube de Atajos, necesitan conexión."),
        ("¿Funciona Siri AI sin internet?",
         "Cuenta con que necesita conexión. Apple la incluye entre las funciones que dependen de modelos "
         "en servidor y tienen límites diarios, y dice que sale a la web para buscar información actual. "
         "Además, en la UE Siri AI no está disponible en el iPhone."),
        ("¿Cómo sé si Apple Intelligence ha mandado mi petición a un servidor?",
         "Activa en Ajustes, Privacidad y seguridad, el Informe de Apple Intelligence. Apple dice "
         "que registra las peticiones procesadas en Private Cloud Compute y las enviadas a extensiones "
         "como ChatGPT. Puedes exportarlo y buscar tu petición."),
        ("¿Private Cloud Compute es la nube?",
         "Son servidores de Apple. Apple dice que los datos no se guardan ni son accesibles para Apple y "
         "solo se usan para contestar, pero la petición sale de tu dispositivo."),
        ("¿Qué iPhone tienen Apple Intelligence?",
         "iPhone 15 Pro, iPhone 15 Pro Max, todos los iPhone 16 y posteriores, y el iPhone Air. El iPhone "
         "15, el 15 Plus y los anteriores no, ni siquiera con iOS 27."),
        ("¿Puedo usar un chat de IA sin conexión en un iPhone sin Apple Intelligence?",
         "Sí, con una app que ejecute un modelo abierto en el móvil, como Pinku (iPhone 12 o posterior), "
         "Locally AI, PocketPal AI o Private LLM. Solo necesitas internet una vez, para descargar el "
         "modelo."),
    ],
}

OFF_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (device and storage requirements, languages, EU and China, server-side features with daily limits), published 14 September 2026.</li>
<li>Apple, <a href="%(siri)s"%(x)s>How to get Siri AI</a> (beta, English only, not on iPhone in the EU, iCloud sync of conversation history), published 22 September 2026.</li>
<li>Apple, <a href="%(priv)s"%(x)s>Apple Intelligence &amp; Privacy</a> (on device or Private Cloud Compute, the Apple Intelligence &amp; PCC Report).</li>
<li>Apple, <a href="%(sc)s"%(x)s>Use Apple Intelligence in Shortcuts on iPhone or iPad</a> (Use Model: On-Device, Cloud, Cloud Pro, Extension Model).</li>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (compatible iPhones) and <a href="%(metal)s"%(x)s>Support for Metal on Apple devices</a> (Metal 3 on iPhone 12 or later).</li>
<li>App Store pages (US) of Pinku, Locally AI, PocketPal AI and Private LLM, as shown on %(date)s.</li>
</ul>
<p>All checked on %(date)s. If anything here is out of date,
<a href="mailto:sagalabs@proton.me">tell us</a> and we will correct the page.</p>
"""

OFF_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Apple, <a href="%(reqs)s"%(x)s>C&oacute;mo obtener la nueva generaci&oacute;n de Apple Intelligence</a> (dispositivos y espacio, idiomas, UE y China, funciones en servidor con l&iacute;mites diarios), publicada el 14 de septiembre de 2026.</li>
<li>Apple, <a href="%(siri)s"%(x)s>C&oacute;mo obtener Siri AI</a> (beta, solo en ingl&eacute;s, no en el iPhone en la UE, historial sincronizado por iCloud), publicada el 22 de septiembre de 2026.</li>
<li>Apple, <a href="%(priv)s"%(x)s>Apple Intelligence y privacidad</a> (en el dispositivo o en Private Cloud Compute, el Informe de Apple Intelligence).</li>
<li>Apple, <a href="%(sc)s"%(x)s>Usar Apple Intelligence en Atajos en el iPhone o el iPad</a> (Use Model: On-Device, Cloud, Cloud Pro, Extension Model).</li>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (iPhone compatibles) y <a href="%(metal)s"%(x)s>Compatibilidad con Metal en dispositivos Apple</a> (Metal 3 desde el iPhone 12).</li>
<li>Fichas del App Store (Espa&ntilde;a) de Pinku, Locally AI, PocketPal AI y Private LLM, tal como se ve&iacute;an el %(date)s.</li>
</ul>
<p>Todo comprobado el %(date)s. Si algo ha cambiado,
<a href="mailto:sagalabs@proton.me">escr&iacute;benos</a> y lo corregimos.</p>
"""


# ==========================================================================
# 2. Best AI apps for iPhones without Apple Intelligence (ranking, Pinku 1.a)
# ==========================================================================

def _rank_items(lang):
    s = _store(lang)
    return [("Pinku: Private Offline AI Chat", "https://apps.apple.com/app/id6754878073"),
            ("Locally AI by LM Studio", s["locally"]),
            ("PocketPal AI", s["pocketpal"]),
            ("Private LLM - Local AI Chat", s["privatellm"]),
            ("ChatGPT", s["chatgpt"]),
            ("Google Gemini", s["gemini"]),
            ("Claude by Anthropic", s["claude"]),
            ("Vibe by Mistral (ex-Le Chat)", s["vibe"])]


NOAI_WHY_EN = _box("Why Pinku is #1 for these iPhones", [
    "It needs no Apple Intelligence: it runs on any iPhone with Metal 3, which Apple lists as iPhone 12 or later, on iOS 18.6 or later.",
    "After one model download it works with no connection at all, on a plane or with no signal.",
    "No account, and chats are stored only on the iPhone. There is no cloud mode to switch on by mistake.",
    "It only lists the models your iPhone has enough memory for, and checks free memory before loading one, so older phones get small models instead of a crash.",
    "Free to download and use with the default model (Gemma 3 1B); Pinku Pro, an in-app purchase, adds larger models, custom instructions, dictation and read aloud.",
])

NOAI_WHY_ES = _box("Por qu&eacute; Pinku es la n.&ordm; 1 para estos iPhone", [
    "No necesita Apple Intelligence: funciona en cualquier iPhone con Metal 3, que Apple lista como iPhone 12 o posterior, con iOS 18.6 o posterior.",
    "Tras descargar un modelo una vez, funciona sin ninguna conexi&oacute;n, en un avi&oacute;n o sin cobertura.",
    "Sin cuenta, y los chats se guardan solo en el iPhone. No hay modo nube que se pueda activar sin querer.",
    "Solo muestra los modelos para los que tu iPhone tiene memoria, y la comprueba antes de cargar uno: en un m&oacute;vil antiguo salen modelos peque&ntilde;os en vez de un cierre.",
    "Gratis para descargar y usar con el modelo por defecto (Gemma 3 1B); Pinku Pro, una compra dentro de la app, a&ntilde;ade modelos grandes, instrucciones personalizadas, dictado y lectura en voz alta.",
])

NOAI_EN_BODY = ("""
<p><strong>Disclosure: we make Pinku, the app ranked first here.</strong> What we say
about the other apps comes from their App Store pages (US), checked on %(date)s.</p>

<p><a href="%(ios)s"%(x)s>iOS 27 runs on iPhone 11 and later</a>, including the
iPhone SE (2nd generation and later). <a href="%(reqs)s"%(x)s>Apple Intelligence
does not</a>: it needs an iPhone 15 Pro, 15 Pro Max, any iPhone 16 or later, or
iPhone Air. So the iPhone 11, 12, 13, 14, 15 and 15 Plus, and the SE, are on the
latest iOS without Writing Tools, Image Playground or Siri AI. These apps fill the
gap, in two different ways: some run an AI model on the phone itself, offline; the
others are cloud assistants that need the internet but are far more capable.</p>

<h2>The ranking</h2>

<ol>
<li><a href="%(pinku)s">Pinku</a>: best offline and private AI for iPhone 12 to 15.</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: best free offline chat.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: runs on the oldest iPhones, and its code is public.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: pay once, works on iPhone 11 and SE.</li>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: best cloud all-rounder.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: best if you live in Google's apps.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: best for long writing and documents.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: the European option.</li>
</ol>
""" + NOAI_WHY_EN + """
<h2>At a glance</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Where the AI runs</th><th>Needs</th><th>Price (US)</th><th>Rating (US)</th></tr></thead>
<tbody>
<tr><td>1. <a href="%(pinku)s">Pinku</a> (ours)</td><td>On the iPhone</td><td>iOS 18.6, iPhone 12 or later</td><td>Free; Pinku Pro in-app purchase</td><td>4.7 (12)</td></tr>
<tr><td>2. <a href="%(locally)s"%(x)s>Locally AI</a></td><td>On the iPhone</td><td>iOS 18.1</td><td>Free</td><td>4.7 (1,805)</td></tr>
<tr><td>3. <a href="%(pocketpal)s"%(x)s>PocketPal AI</a></td><td>On the iPhone</td><td>iOS 15.1</td><td>Free; optional paid &ldquo;Pals&rdquo; from $0.99</td><td>4.1 (162)</td></tr>
<tr><td>4. <a href="%(privatellm)s"%(x)s>Private LLM</a></td><td>On the iPhone</td><td>iOS 17, A12 Bionic or later</td><td>$4.99 upfront</td><td>4.2 (736)</td></tr>
<tr><td>5. <a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Cloud</td><td>iOS 18.0, internet</td><td>Free; Go $8, Plus $19.99 a month</td><td>4.8 (11.4 million)</td></tr>
<tr><td>6. <a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Cloud</td><td>iOS 17.4, internet</td><td>Free; Google AI Plus $4.99, Pro $19.99</td><td>4.7 (2.36 million)</td></tr>
<tr><td>7. <a href="%(claude)s"%(x)s>Claude</a></td><td>Cloud</td><td>iOS 18.0, internet</td><td>Free; Pro $20 a month</td><td>4.7 (282,163)</td></tr>
<tr><td>8. <a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Cloud</td><td>iOS 16.4, internet</td><td>Free; Vibe Pro $14.99</td><td>4.8 (1,318)</td></tr>
</tbody>
</table></div>

<p class="article-note">Requirements, in-app purchase prices and ratings as shown on
each app's US App Store page on %(date)s. Prices are the ones Apple lists for the
in-app purchases; plans may have other periods. The iPhone 12 limit for Pinku comes
from its need for Metal 3, which Apple lists on iPhone 12 or later.</p>

<h2>On the phone or in the cloud?</h2>

<p>An app that runs the model on your iPhone works anywhere, keeps the conversation
on the device and costs nothing per message. But the models that fit in a phone
weigh 0.4 to 5 GB, and they are clearly weaker than ChatGPT, Gemini or Claude: they
make more mistakes on facts, do not browse the web and handle shorter texts. Older
iPhones also have less memory, so they run only the smaller models. The cloud apps
are the opposite: much smarter, but every message goes to the company's servers and
nothing works without a connection. Many people end up with one of each.</p>

<h2>1. Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> runs open models (Gemma 3, Llama 3.2, Qwen3 and
others) on the iPhone with Apple's MLX framework. You download a model once, and
from then on every answer is generated on the phone, in airplane mode too. There
is no account, chats are saved only on the device, and you can delete any of them.
On an older iPhone it hides the models that would not fit in memory. It also runs on
Macs with Apple silicon. Its App Store privacy label lists purchase history and a
user ID linked to you, used for purchases; it lists no chat content. Where others
beat it: it does not run on the iPhone 11 or the SE (2nd generation), which lack
Metal 3 (Private LLM and PocketPal do), its code is not public, and it reads no
images or documents.</p>

<h2>2. Locally AI by LM Studio</h2>

<p>Free, no login, made by the company behind LM Studio for the Mac, with
<em>Data Not Collected</em> on its privacy label and by far the most ratings of the
offline apps here. It also analyses images. It needs iOS 18.1.</p>

<h2>3. PocketPal AI</h2>

<p>The offline app with the lowest requirement here, iOS 15.1, and the only one with
<a href="%(gh)s"%(x)s>public source code</a>. It loads any GGUF model from Hugging
Face, which gives you more choice and more ways to pick a model your iPhone cannot
handle. Free, <em>Data Not Collected</em>; it sells optional character presets
(&ldquo;Pals&rdquo;).</p>

<h2>4. Private LLM</h2>

<p>$4.99 once, with Family Sharing, Siri and Shortcuts, and <em>Data Not
Collected</em>. It is the paid option that explicitly supports the iPhone 11 and
iPhone SE (2nd generation): it asks for an A12 Bionic chip or later.</p>

<h2>5. ChatGPT</h2>

<p>The most rated AI app on the App Store by far. Free to start, with paid plans
listed in the app (Go, Plus, Pro). It is the closest thing to a full assistant on an
iPhone without Apple Intelligence, but it is a cloud service: its privacy label lists
contact info, usage data and user content as data linked to you.</p>

<h2>6. Google Gemini</h2>

<p>Free, works from iOS 17.4, and its paid tiers come bundled with Google storage
(Google AI Plus with 400 GB, Pro with 5 TB). The natural choice if your mail,
calendar and photos are already at Google. Cloud only.</p>

<h2>7. Claude</h2>

<p>From Anthropic. Free to start, Pro at $20 a month. Strong at long writing,
summaries and working through documents. Cloud only, and its privacy label lists
contact info, identifiers and user content as data linked to you.</p>

<h2>8. Vibe by Mistral</h2>

<p>The app formerly called Le Chat, from Mistral AI, based in Paris: the only
European company here. Free, Vibe Pro at $14.99, and the lowest requirement of the
cloud apps (iOS 16.4). Cloud only.</p>

<h2>What about Enclave?</h2>

<p><a href="%(enclave)s"%(x)s>Enclave</a> is another good offline app, with optional
cloud models in its Pro tier, but it now requires iOS 27. If your iPhone is on iOS 27
(iPhone 11 or later), it is worth a look; on iOS 18 or 26 it will not install.</p>

<p>Not sure what your iPhone does without Apple Intelligence? We explained
<a href="does-apple-intelligence-work-offline-iphone.html">what Apple Intelligence
does offline and what goes to Apple's servers</a>.</p>
""")

NOAI_ES_BODY = ("""
<p><strong>Aviso: hacemos Pinku, la app que ponemos primera.</strong> Lo que decimos
de las dem&aacute;s sale de su ficha del App Store en Espa&ntilde;a, comprobada el
%(date)s.</p>

<p><a href="%(ios)s"%(x)s>iOS 27 funciona desde el iPhone 11</a>, tambi&eacute;n en el
iPhone SE de 2.&ordf; generaci&oacute;n y posteriores. <a href="%(reqs)s"%(x)s>Apple
Intelligence no</a>: pide un iPhone 15 Pro, 15 Pro Max, cualquier iPhone 16 o
posterior, o el iPhone Air. As&iacute; que el iPhone 11, 12, 13, 14, 15 y 15 Plus, y el SE,
tienen el iOS m&aacute;s nuevo sin herramientas de escritura, Image Playground ni Siri
AI. Estas apps cubren el hueco de dos formas: unas ejecutan un modelo de IA en el
propio m&oacute;vil, sin conexi&oacute;n; las otras son asistentes en la nube que necesitan
internet pero son mucho m&aacute;s capaces.</p>

<h2>El ranking</h2>

<ol>
<li><a href="%(pinku)s">Pinku</a>: la mejor IA privada y sin conexi&oacute;n para iPhone 12 a 15.</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: el mejor chat sin conexi&oacute;n gratis.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: funciona en los iPhone m&aacute;s antiguos y su c&oacute;digo es p&uacute;blico.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: pago &uacute;nico, funciona en iPhone 11 y SE.</li>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: el asistente en la nube m&aacute;s completo.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: si vives en las apps de Google.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: para textos largos y documentos.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: la opci&oacute;n europea.</li>
</ol>
""" + NOAI_WHY_ES + """
<h2>De un vistazo</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>D&oacute;nde funciona la IA</th><th>Necesita</th><th>Precio (Espa&ntilde;a)</th><th>Valoraci&oacute;n (Espa&ntilde;a)</th></tr></thead>
<tbody>
<tr><td>1. <a href="%(pinku)s">Pinku</a> (nuestra)</td><td>En el iPhone</td><td>iOS 18.6, iPhone 12 o posterior</td><td>Gratis; Pinku Pro, compra dentro de la app</td><td>5,0 (1)</td></tr>
<tr><td>2. <a href="%(locally)s"%(x)s>Locally AI</a></td><td>En el iPhone</td><td>iOS 18.1</td><td>Gratis</td><td>4,5 (149)</td></tr>
<tr><td>3. <a href="%(pocketpal)s"%(x)s>PocketPal AI</a></td><td>En el iPhone</td><td>iOS 15.1</td><td>Gratis; &laquo;Pals&raquo; opcionales desde 1,49 &euro;</td><td>4,5 (8)</td></tr>
<tr><td>4. <a href="%(privatellm)s"%(x)s>Private LLM</a></td><td>En el iPhone</td><td>iOS 17, A12 Bionic o posterior</td><td>5,99 &euro; de entrada</td><td>3,4 (24)</td></tr>
<tr><td>5. <a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Nube</td><td>iOS 18.0, internet</td><td>Gratis; Go 7,99 &euro;, Plus 22,99 &euro; al mes</td><td>4,8 (933.001)</td></tr>
<tr><td>6. <a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Nube</td><td>iOS 17.4, internet</td><td>Gratis; Google AI Plus 4,99 &euro;, Pro 21,99 &euro;</td><td>4,7 (211.082)</td></tr>
<tr><td>7. <a href="%(claude)s"%(x)s>Claude</a></td><td>Nube</td><td>iOS 18.0, internet</td><td>Gratis; Pro 22 &euro; al mes</td><td>4,7 (15.123)</td></tr>
<tr><td>8. <a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Nube</td><td>iOS 16.4, internet</td><td>Gratis; Vibe Pro 17,99 &euro;</td><td>4,7 (432)</td></tr>
</tbody>
</table></div>

<p class="article-note">Requisitos, precios de las compras dentro de la app y
valoraciones tal como aparec&iacute;an en la ficha del App Store de Espa&ntilde;a el
%(date)s. Son los precios que Apple muestra para cada compra; los planes pueden
tener otros periodos. El l&iacute;mite del iPhone 12 en Pinku viene de que necesita
Metal 3, que Apple lista desde el iPhone 12.</p>

<h2>&iquest;En el m&oacute;vil o en la nube?</h2>

<p>Una app que ejecuta el modelo en el iPhone funciona en cualquier sitio, deja la
conversaci&oacute;n en el dispositivo y no cuesta nada por mensaje. Pero los modelos
que caben en un m&oacute;vil pesan de 0,4 a 5 GB y son claramente m&aacute;s flojos que
ChatGPT, Gemini o Claude: se equivocan m&aacute;s en datos, no buscan en internet y
admiten textos m&aacute;s cortos. Los iPhone antiguos, adem&aacute;s, tienen menos memoria y
solo mueven los modelos peque&ntilde;os. Las apps en la nube son lo contrario: mucho
m&aacute;s listas, pero cada mensaje va a los servidores de la empresa y sin conexi&oacute;n
no funcionan. Mucha gente acaba con una de cada.</p>

<h2>1. Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> ejecuta modelos abiertos (Gemma 3, Llama 3.2, Qwen3 y
otros) en el iPhone con MLX, el motor de Apple. Descargas un modelo una vez y a partir
de ah&iacute; cada respuesta se genera en el m&oacute;vil, tambi&eacute;n en modo avi&oacute;n. No hay
cuenta, los chats se guardan solo en el dispositivo y puedes borrar cualquiera. En
un iPhone antiguo oculta los modelos que no cabr&iacute;an en memoria. La app est&aacute; en
espa&ntilde;ol y tambi&eacute;n funciona en Mac con Apple silicon. Su etiqueta de privacidad
indica historial de compras e identificador de usuario vinculados a ti, para las
compras; ning&uacute;n contenido de los chats. En qu&eacute; pierde: no funciona en el iPhone
11 ni en el SE de 2.&ordf; generaci&oacute;n, que no tienen Metal 3 (Private LLM y PocketPal
s&iacute;), su c&oacute;digo no es p&uacute;blico y no lee im&aacute;genes ni documentos.</p>

<h2>2. Locally AI by LM Studio</h2>

<p>Gratis, sin registro, de la empresa que hace LM Studio para Mac, con <em>Datos no
recopilados</em> en su etiqueta y muchas m&aacute;s valoraciones que el resto de apps sin
conexi&oacute;n. Tambi&eacute;n analiza im&aacute;genes. Pide iOS 18.1.</p>

<h2>3. PocketPal AI</h2>

<p>La app sin conexi&oacute;n que menos pide, iOS 15.1, y la &uacute;nica con
<a href="%(gh)s"%(x)s>c&oacute;digo p&uacute;blico</a>. Carga cualquier modelo GGUF de Hugging
Face, lo que da m&aacute;s donde elegir y m&aacute;s formas de elegir uno que tu iPhone no
puede mover. Gratis, <em>Datos no recopilados</em>; vende personajes predefinidos
opcionales (&laquo;Pals&raquo;).</p>

<h2>4. Private LLM</h2>

<p>5,99 &euro; una vez, con En familia, Siri y Atajos, y <em>Datos no recopilados</em>.
Es la opci&oacute;n de pago que admite el iPhone 11 y el SE de 2.&ordf; generaci&oacute;n: pide
chip A12 Bionic o posterior. En Espa&ntilde;a tiene pocas valoraciones y m&aacute;s bajas
que en EE.&nbsp;UU. (3,4 frente a 4,2).</p>

<h2>5. ChatGPT</h2>

<p>La app de IA con m&aacute;s valoraciones del App Store con diferencia. Gratis para
empezar, con planes de pago en la app (Go, Plus, Pro). Es lo m&aacute;s parecido a un
asistente completo en un iPhone sin Apple Intelligence, pero es un servicio en la
nube: su etiqueta de privacidad indica datos de contacto, de uso y contenido del
usuario vinculados a ti.</p>

<h2>6. Google Gemini</h2>

<p>Gratis, desde iOS 17.4, y sus planes de pago vienen con almacenamiento de Google
(Google AI Plus con 400 GB, Pro con 5 TB). Lo natural si tu correo, calendario y
fotos ya est&aacute;n en Google. Solo en la nube.</p>

<h2>7. Claude</h2>

<p>De Anthropic. Gratis para empezar, Pro a 22 &euro; al mes. Bueno en textos largos,
res&uacute;menes y trabajo con documentos. Solo en la nube, y su etiqueta indica datos de
contacto, identificadores y contenido del usuario vinculados a ti.</p>

<h2>8. Vibe by Mistral</h2>

<p>La app que antes se llamaba Le Chat, de Mistral AI, con sede en Par&iacute;s: la
&uacute;nica empresa europea de la lista. Gratis, Vibe Pro a 17,99 &euro;, y la que menos pide
de las apps en la nube (iOS 16.4). Solo en la nube.</p>

<h2>&iquest;Y Enclave?</h2>

<p><a href="%(enclave)s"%(x)s>Enclave</a> es otra buena app sin conexi&oacute;n, con modelos
en la nube opcionales en su plan Pro, pero ahora pide iOS 27. Si tu iPhone ya tiene
iOS 27 (desde el iPhone 11), vale la pena mirarla; con iOS 18 o 26 no se instala.</p>

<p>&iquest;No sabes qu&eacute; hace tu iPhone sin Apple Intelligence? Lo explicamos en
<a href="apple-intelligence-funciona-sin-internet-iphone.html">qu&eacute; hace Apple
Intelligence sin conexi&oacute;n y qu&eacute; va a los servidores de Apple</a>.</p>
""")

NOAI_FAQ = {
    "en": [
        ("Can I get Apple Intelligence on an iPhone 13, 14 or 15?",
         "No. Apple Intelligence needs an iPhone 15 Pro, 15 Pro Max, an iPhone 16 or later, or iPhone Air. "
         "The iPhone 15, 15 Plus and older models can update to iOS 27 but do not get Apple Intelligence."),
        ("What is the best AI app for an iPhone without Apple Intelligence?",
         "For an assistant that works offline and keeps chats on the phone, an on-device app such as Pinku "
         "(iPhone 12 or later), Locally AI, PocketPal AI or Private LLM. For the most capable answers, a "
         "cloud app such as ChatGPT, Gemini or Claude, which needs the internet."),
        ("Can an iPhone 12 run an AI model offline?",
         "Yes. Apps like Pinku run small open models (around 0.4 to 2 GB) on an iPhone 12. Older iPhones "
         "have less memory, so the biggest models are not offered on them."),
        ("Do offline AI apps work on the iPhone 11?",
         "Some do. Private LLM supports iPhones with an A12 Bionic chip or later, and PocketPal AI needs "
         "iOS 15.1. Pinku needs Metal 3, which Apple lists on iPhone 12 or later."),
        ("Is an offline AI app as good as ChatGPT?",
         "No. A model small enough for a phone makes more mistakes, does not browse the web and handles "
         "shorter texts. Its advantages are privacy, working with no connection and no cost per message."),
    ],
    "es": [
        ("¿Puedo tener Apple Intelligence en un iPhone 13, 14 o 15?",
         "No. Apple Intelligence pide un iPhone 15 Pro, 15 Pro Max, un iPhone 16 o posterior, o el iPhone "
         "Air. El iPhone 15, el 15 Plus y los anteriores se actualizan a iOS 27 pero sin Apple "
         "Intelligence."),
        ("¿Cuál es la mejor app de IA para un iPhone sin Apple Intelligence?",
         "Para un asistente que funcione sin conexión y deje los chats en el móvil, una app en el "
         "dispositivo como Pinku (iPhone 12 o posterior), Locally AI, PocketPal AI o Private LLM. Para las "
         "respuestas más capaces, una app en la nube como ChatGPT, Gemini o Claude, que necesita internet."),
        ("¿Puede un iPhone 12 ejecutar un modelo de IA sin conexión?",
         "Sí. Apps como Pinku ejecutan modelos abiertos pequeños (de unos 0,4 a 2 GB) en un iPhone 12. Los "
         "iPhone antiguos tienen menos memoria, así que no se les ofrecen los modelos más grandes."),
        ("¿Funcionan las apps de IA sin conexión en el iPhone 11?",
         "Algunas sí. Private LLM admite iPhone con chip A12 Bionic o posterior, y PocketPal AI pide iOS "
         "15.1. Pinku necesita Metal 3, que Apple lista desde el iPhone 12."),
        ("¿Una app de IA sin conexión es tan buena como ChatGPT?",
         "No. Un modelo que cabe en un móvil se equivoca más, no busca en internet y admite textos más "
         "cortos. Sus ventajas son la privacidad, que funciona sin conexión y que no cuesta nada por "
         "mensaje."),
    ],
}

NOAI_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (compatible iPhones) and <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (devices with Apple Intelligence).</li>
<li>Apple, <a href="%(metal)s"%(x)s>Support for Metal on Apple devices</a> (Metal 3 on iPhone 12 or later).</li>
<li>App Store pages (US), including requirements, in-app purchases, ratings and App Privacy: <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, <a href="%(pocketpal)s"%(x)s>PocketPal AI</a>, <a href="%(privatellm)s"%(x)s>Private LLM</a>, <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(enclave)s"%(x)s>Enclave</a>, as shown on %(date)s.</li>
<li>PocketPal AI source code: <a href="%(gh)s"%(x)s>github.com/a-ghorbani/pocketpal-ai</a>.</li>
<li>Pinku's features: <a href="../pinku.html">its product page</a>.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
"""

NOAI_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (iPhone compatibles) y <a href="%(reqs)s"%(x)s>C&oacute;mo obtener la nueva generaci&oacute;n de Apple Intelligence</a> (dispositivos con Apple Intelligence).</li>
<li>Apple, <a href="%(metal)s"%(x)s>Compatibilidad con Metal en dispositivos Apple</a> (Metal 3 desde el iPhone 12).</li>
<li>Fichas del App Store (Espa&ntilde;a), con requisitos, compras dentro de la app, valoraciones y privacidad: <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, <a href="%(pocketpal)s"%(x)s>PocketPal AI</a>, <a href="%(privatellm)s"%(x)s>Private LLM</a>, <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(enclave)s"%(x)s>Enclave</a>, tal como se ve&iacute;an el %(date)s.</li>
<li>C&oacute;digo de PocketPal AI: <a href="%(gh)s"%(x)s>github.com/a-ghorbani/pocketpal-ai</a>.</li>
<li>Funciones de Pinku: <a href="../../pinku.html">su p&aacute;gina</a>.</li>
</ul>
<p>Si algo ha cambiado, <a href="mailto:sagalabs@proton.me">escr&iacute;benos</a> y lo
corregimos.</p>
"""


# ==========================================================================
# 3. Best Siri AI alternatives for iPhone in the EU (por situacion)
# ==========================================================================
#
# Formato distinto a proposito: Siri AI hace cosas (contexto personal, acciones
# en apps) que Pinku no hace, asi que no la ponemos primera. Es la prueba de
# "comparativa neutral" que pide PLAYBOOK.md (Formato en uso desde el 7 oct).

def _siri_items(lang):
    s = _store(lang)
    return [("ChatGPT", s["chatgpt"]), ("Google Gemini", s["gemini"]),
            ("Claude by Anthropic", s["claude"]), ("Vibe by Mistral (ex-Le Chat)", s["vibe"]),
            ("Pinku: Private Offline AI Chat", "https://apps.apple.com/app/id6754878073"),
            ("Locally AI by LM Studio", s["locally"])]


SIRI_EN_BODY = """
<p><strong>Disclosure: we make Pinku, one of the apps below.</strong> We do not rank
it first, because it does not do most of what Siri AI does. What we say about each
app comes from its App Store page, and about Siri AI from Apple's own support pages,
checked on %(date)s.</p>

<h2>What is and is not available in the EU</h2>

<p>Apple's page on Siri AI is explicit: <a href="%(siri)s"%(x)s>&ldquo;Siri AI is not
available for iOS, iPadOS, or watchOS in the EU.&rdquo;</a> It is available on macOS 27
and visionOS 27 for people whose Apple Account region is in the EU, with the device
and Siri language set to English. It is also English only everywhere for now, and a
beta with a waitlist.</p>

<p>That does not mean the EU gets no Apple Intelligence. Apple says the new features
across apps, such as advanced photo editing, the reimagined Image Playground and
the intelligent features in Safari, <a href="%(reqs)s"%(x)s>are available to users in
the EU</a> on iOS 27, on an iPhone that supports Apple Intelligence (iPhone 15 Pro
or later). On the same page Apple lists Writing Tools as &ldquo;available for users
without Siri AI writing support&rdquo;, and the only feature it rules out on EU
iPhones is Siri AI. What is missing on an EU iPhone is the new
Siri: the one that answers questions about almost anything, understands your
messages and emails, sees what is on screen and acts across apps.</p>

<h2>What Siri AI does, and what replaces each part</h2>

<div class="table-scroll"><table>
<thead><tr><th>Siri AI feature (Apple's list)</th><th>Closest option on an EU iPhone</th></tr></thead>
<tbody>
<tr><td>Broad world knowledge: answers to almost any question</td><td>ChatGPT, Gemini, Claude or Vibe by Mistral</td></tr>
<tr><td>Write with Siri: drafts and edits wherever you type</td><td>Apple's Writing Tools (Apple lists them for users without Siri AI), or any of the chat apps</td></tr>
<tr><td>Personal context across Messages, Mail, Calendar and Notes</td><td>No app on the iPhone reads all of these the way Siri AI does</td></tr>
<tr><td>Onscreen awareness and app actions</td><td>No full replacement on iPhone</td></tr>
<tr><td>Siri app with conversation history synced by iCloud</td><td>Each chat app keeps its own history, on its servers</td></tr>
<tr><td>Works without a connection</td><td>Siri AI relies on server-side models; for offline use, Pinku or Locally AI</td></tr>
</tbody>
</table></div>

<h2>The options, by what you need</h2>

<ol>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: best general replacement for asking anything.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: best if your mail and calendar are at Google.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: best for writing and long documents.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: best if you want a European company.</li>
<li><a href="%(pinku)s">Pinku</a> (ours): best if nothing may leave the phone.</li>
<li><a href="%(locally)s"%(x)s>Locally AI</a>: free offline chat, also private.</li>
</ol>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Where it runs</th><th>Price (Spain)</th><th>Rating (Spain)</th><th>Privacy label</th></tr></thead>
<tbody>
<tr><td><a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Cloud (OpenAI, US)</td><td>Free; Go &euro;7.99, Plus &euro;22.99 a month</td><td>4.8 (933,001)</td><td>Data linked to you, incl. contact info and user content</td></tr>
<tr><td><a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Cloud (Google, US)</td><td>Free; Google AI Plus &euro;4.99, Pro &euro;21.99</td><td>4.7 (211,082)</td><td>Data linked to you, incl. location, contact info and identifiers</td></tr>
<tr><td><a href="%(claude)s"%(x)s>Claude</a></td><td>Cloud (Anthropic, US)</td><td>Free; Pro &euro;22 a month</td><td>4.7 (15,123)</td><td>Data linked to you, incl. contact info and user content</td></tr>
<tr><td><a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Cloud (Mistral AI, France)</td><td>Free; Vibe Pro &euro;17.99</td><td>4.7 (432)</td><td>Contact info linked to you; usage and user content not linked</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a> (ours)</td><td>On the iPhone</td><td>Free; Pinku Pro in-app purchase</td><td>5.0 (1)</td><td>Purchase history and user ID, for purchases</td></tr>
<tr><td><a href="%(locally)s"%(x)s>Locally AI</a></td><td>On the iPhone</td><td>Free</td><td>4.5 (149)</td><td>Data Not Collected</td></tr>
</tbody>
</table></div>

<p class="article-note">Prices and ratings from each app's Spanish App Store page on
%(date)s; we use Spain because it is the largest EU market we checked. Privacy labels
are what each developer declares to Apple; Apple does not verify them.</p>

<h2>ChatGPT</h2>

<p>The most rated AI app on the App Store, and the most direct replacement for
&ldquo;ask Siri anything&rdquo;. Free to start, with Go, Plus and Pro plans in the app.
It is a cloud service from a US company: its privacy label lists contact info, usage
data and user content as linked to you.</p>

<h2>Google Gemini</h2>

<p>Free, from iOS 17.4, with paid tiers bundled with Google storage. If your mail,
calendar and photos are at Google, it is the closest thing to the personal context
Siri AI promises, inside Google's apps. Cloud only.</p>

<h2>Claude</h2>

<p>From Anthropic. Free to start, Pro at &euro;22 a month. The best of these for
writing, editing and working through long documents. Cloud only.</p>

<h2>Vibe by Mistral</h2>

<p>Formerly Le Chat, made by Mistral AI in Paris, the only EU company here. Its
privacy label separates contact info, which is linked to you, from usage data and
user content, which it declares as not linked. Free, Vibe Pro at &euro;17.99, iOS 16.4
or later.</p>

<h2>Pinku (ours)</h2>

<p><a href="%(pinku)s">Pinku</a> is not a Siri replacement: it cannot read your
messages, see your screen or act in other apps. What it does is answer on the
iPhone itself, with an open model you download once, so the conversation never goes
to any server, in the EU or anywhere else, and it works in airplane mode. No account.
Its interface is in Spanish, German, French and other languages, and it runs on any
iPhone 12 or later with iOS 18.6, with or without Apple Intelligence. The default
model is free; Pinku Pro, an in-app purchase, adds larger models, custom
instructions, dictation and read aloud. A phone-sized model is much weaker than the
cloud apps above.</p>

<h2>Locally AI by LM Studio</h2>

<p>The free alternative to Pinku for private, offline chat: no login, <em>Data Not
Collected</em>, iOS 18.1 or later, and it can also look at images.</p>

<h2>Have a Mac?</h2>

<p>On a Mac with macOS 27 Golden Gate, Siri AI is available in the EU if your device
and Siri language are both English. Apple Intelligence itself needs a Mac with M1 or
later.</p>

<p>Related: <a href="does-apple-intelligence-work-offline-iphone.html">what Apple
Intelligence does offline</a> and <a href="best-ai-apps-iphone-without-apple-intelligence.html">the
best AI apps for iPhones without Apple Intelligence</a>.</p>
"""

SIRI_ES_BODY = """
<p><strong>Aviso: hacemos Pinku, una de las apps de la lista.</strong> No la ponemos
primera, porque no hace casi nada de lo que hace Siri AI. Lo que decimos de cada app
sale de su ficha del App Store en Espa&ntilde;a, y lo de Siri AI, de las p&aacute;ginas de
soporte de Apple, comprobadas el %(date)s.</p>

<h2>Qu&eacute; hay y qu&eacute; no hay en la UE</h2>

<p>La p&aacute;gina de Apple sobre Siri AI lo dice claro: <a href="%(siri)s"%(x)s>&laquo;Siri
AI no est&aacute; disponible para iOS, iPadOS ni watchOS en la UE&raquo;</a>. S&iacute; lo est&aacute;
en macOS 27 y visionOS 27 para quien tenga la cuenta de Apple en la UE y el idioma
del dispositivo y de Siri en ingl&eacute;s. Adem&aacute;s, de momento es solo en ingl&eacute;s en
todas partes, y es una beta con lista de espera.</p>

<p>Eso no quiere decir que en la UE no haya Apple Intelligence. Apple dice que las
funciones nuevas en las apps, como la edici&oacute;n avanzada de fotos, el nuevo Image
Playground y las funciones inteligentes de Safari, <a href="%(reqs)s"%(x)s>est&aacute;n
disponibles en la UE</a> con iOS 27, en un iPhone compatible con Apple
Intelligence (iPhone 15 Pro o posterior). En la misma p&aacute;gina, Apple dice que las
herramientas de escritura est&aacute;n &laquo;disponibles para quien no tenga la escritura
de Siri AI&raquo;, y la &uacute;nica funci&oacute;n que descarta en los iPhone de la UE es Siri
AI. Lo que falta en un iPhone de la UE es la Siri nueva: la que
responde a casi cualquier pregunta, entiende tus mensajes y correos, ve lo que hay
en pantalla y act&uacute;a en las apps.</p>

<h2>Qu&eacute; hace Siri AI y qu&eacute; sustituye cada parte</h2>

<div class="table-scroll"><table>
<thead><tr><th>Funci&oacute;n de Siri AI (lista de Apple)</th><th>Lo m&aacute;s parecido en un iPhone de la UE</th></tr></thead>
<tbody>
<tr><td>Conocimiento general: respuestas a casi cualquier pregunta</td><td>ChatGPT, Gemini, Claude o Vibe by Mistral</td></tr>
<tr><td>Escribir con Siri: borradores y correcciones donde escribas</td><td>Las herramientas de escritura de Apple (Apple las ofrece a quien no tiene Siri AI) o cualquiera de las apps de chat</td></tr>
<tr><td>Contexto personal en Mensajes, Mail, Calendario y Notas</td><td>Ninguna app del iPhone lee todo eso como Siri AI</td></tr>
<tr><td>Lo que hay en pantalla y acciones en apps</td><td>Sin sustituto completo en el iPhone</td></tr>
<tr><td>App de Siri con el historial sincronizado por iCloud</td><td>Cada app de chat guarda su historial, en sus servidores</td></tr>
<tr><td>Funcionar sin conexi&oacute;n</td><td>Siri AI depende de modelos en servidor; sin conexi&oacute;n, Pinku o Locally AI</td></tr>
</tbody>
</table></div>

<h2>Las opciones, seg&uacute;n lo que necesites</h2>

<ol>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: el mejor sustituto general para preguntar de todo.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: si tu correo y tu calendario est&aacute;n en Google.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: para escribir y documentos largos.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: si prefieres una empresa europea.</li>
<li><a href="%(pinku)s">Pinku</a> (nuestra): si nada puede salir del m&oacute;vil.</li>
<li><a href="%(locally)s"%(x)s>Locally AI</a>: chat sin conexi&oacute;n gratis, tambi&eacute;n privado.</li>
</ol>

<div class="table-scroll"><table>
<thead><tr><th></th><th>D&oacute;nde funciona</th><th>Precio (Espa&ntilde;a)</th><th>Valoraci&oacute;n (Espa&ntilde;a)</th><th>Etiqueta de privacidad</th></tr></thead>
<tbody>
<tr><td><a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Nube (OpenAI, EE.&nbsp;UU.)</td><td>Gratis; Go 7,99 &euro;, Plus 22,99 &euro; al mes</td><td>4,8 (933.001)</td><td>Datos vinculados a ti, entre ellos contacto y contenido del usuario</td></tr>
<tr><td><a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Nube (Google, EE.&nbsp;UU.)</td><td>Gratis; Google AI Plus 4,99 &euro;, Pro 21,99 &euro;</td><td>4,7 (211.082)</td><td>Datos vinculados a ti, entre ellos ubicaci&oacute;n, contacto e identificadores</td></tr>
<tr><td><a href="%(claude)s"%(x)s>Claude</a></td><td>Nube (Anthropic, EE.&nbsp;UU.)</td><td>Gratis; Pro 22 &euro; al mes</td><td>4,7 (15.123)</td><td>Datos vinculados a ti, entre ellos contacto y contenido del usuario</td></tr>
<tr><td><a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Nube (Mistral AI, Francia)</td><td>Gratis; Vibe Pro 17,99 &euro;</td><td>4,7 (432)</td><td>Contacto vinculado a ti; uso y contenido del usuario, no vinculados</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a> (nuestra)</td><td>En el iPhone</td><td>Gratis; Pinku Pro, compra dentro de la app</td><td>5,0 (1)</td><td>Historial de compras e identificador de usuario, para las compras</td></tr>
<tr><td><a href="%(locally)s"%(x)s>Locally AI</a></td><td>En el iPhone</td><td>Gratis</td><td>4,5 (149)</td><td>Datos no recopilados</td></tr>
</tbody>
</table></div>

<p class="article-note">Precios y valoraciones de la ficha del App Store de
Espa&ntilde;a de cada app el %(date)s. Las etiquetas de privacidad son lo que cada
desarrollador declara a Apple; Apple no las verifica.</p>

<h2>ChatGPT</h2>

<p>La app de IA con m&aacute;s valoraciones del App Store y el sustituto m&aacute;s directo de
&laquo;preg&uacute;ntale a Siri cualquier cosa&raquo;. Gratis para empezar, con planes Go, Plus y
Pro en la app. Es un servicio en la nube de una empresa de EE.&nbsp;UU.: su etiqueta
indica datos de contacto, de uso y contenido del usuario vinculados a ti.</p>

<h2>Google Gemini</h2>

<p>Gratis, desde iOS 17.4, con planes de pago que incluyen almacenamiento de Google.
Si tu correo, calendario y fotos est&aacute;n en Google, es lo m&aacute;s parecido al contexto
personal que promete Siri AI, dentro de las apps de Google. Solo en la nube.</p>

<h2>Claude</h2>

<p>De Anthropic. Gratis para empezar, Pro a 22 &euro; al mes. La mejor de estas para
escribir, corregir y trabajar con documentos largos. Solo en la nube.</p>

<h2>Vibe by Mistral</h2>

<p>Antes Le Chat, de Mistral AI, en Par&iacute;s: la &uacute;nica empresa de la UE de la
lista. Su etiqueta separa los datos de contacto, vinculados a ti, de los datos de uso
y el contenido del usuario, que declara como no vinculados. Gratis, Vibe Pro a
17,99 &euro;, desde iOS 16.4.</p>

<h2>Pinku (nuestra)</h2>

<p><a href="%(pinku)s">Pinku</a> no sustituye a Siri: no lee tus mensajes, no ve tu
pantalla y no act&uacute;a en otras apps. Lo que hace es contestar en el propio iPhone,
con un modelo abierto que descargas una vez, as&iacute; que la conversaci&oacute;n no va a
ning&uacute;n servidor, ni en la UE ni fuera, y funciona en modo avi&oacute;n. Sin cuenta. La
app est&aacute; en espa&ntilde;ol y funciona en cualquier iPhone 12 o posterior con iOS 18.6,
tenga o no Apple Intelligence. El modelo por defecto es gratis; Pinku Pro, una compra
dentro de la app, a&ntilde;ade modelos grandes, instrucciones personalizadas, dictado y
lectura en voz alta. Un modelo del tama&ntilde;o de un m&oacute;vil es mucho m&aacute;s flojo que
las apps en la nube de arriba.</p>

<h2>Locally AI by LM Studio</h2>

<p>La alternativa gratis a Pinku para chatear en privado y sin conexi&oacute;n: sin
registro, <em>Datos no recopilados</em>, desde iOS 18.1, y tambi&eacute;n mira
im&aacute;genes.</p>

<h2>&iquest;Tienes Mac?</h2>

<p>En un Mac con macOS 27 Golden Gate, Siri AI s&iacute; est&aacute; disponible en la UE si el
idioma del dispositivo y el de Siri son el ingl&eacute;s. Apple Intelligence pide un Mac
con M1 o posterior.</p>

<p>Relacionado: <a href="apple-intelligence-funciona-sin-internet-iphone.html">qu&eacute; hace
Apple Intelligence sin conexi&oacute;n</a> y <a href="mejores-apps-ia-iphone-sin-apple-intelligence.html">las
mejores apps de IA para iPhone sin Apple Intelligence</a>.</p>
"""

SIRI_FAQ = {
    "en": [
        ("Is Siri AI available in the EU?",
         "Not on iPhone. Apple says Siri AI is not available for iOS, iPadOS or watchOS in the EU. It is "
         "available on macOS 27 and visionOS 27 for EU accounts with the device and Siri language set to "
         "English."),
        ("Is Apple Intelligence available in the EU?",
         "Yes. Apple says the Apple Intelligence features across apps, such as advanced photo editing, "
         "Image Playground and Safari's intelligent features, are available to users in the EU on iOS 27, "
         "on a supported iPhone (iPhone 15 Pro or later). Only Siri AI is missing on iPhone."),
        ("What is the best Siri AI alternative on iPhone in Europe?",
         "For asking anything, ChatGPT, Gemini or Claude; Vibe by Mistral if you prefer a European "
         "company. None of them reads your messages and acts across apps the way Siri AI does. For a "
         "private assistant that works offline, Pinku or Locally AI."),
        ("Does Siri AI work in Spanish?",
         "Not yet. Apple says Siri AI is currently available in English."),
        ("Is there an AI assistant that keeps my chats on my iPhone?",
         "Yes. On-device apps such as Pinku and Locally AI run the model on the iPhone, so the "
         "conversation is not sent to a server. They are less capable than cloud assistants."),
    ],
    "es": [
        ("¿Está Siri AI disponible en España y la UE?",
         "No en el iPhone. Apple dice que Siri AI no está disponible para iOS, iPadOS ni watchOS en la UE. "
         "Sí en macOS 27 y visionOS 27 para cuentas de la UE con el idioma del dispositivo y de Siri en "
         "inglés."),
        ("¿Está Apple Intelligence disponible en la UE?",
         "Sí. Apple dice que las funciones de Apple Intelligence en las apps, como la edición avanzada de "
         "fotos, Image Playground y las funciones inteligentes de Safari, están disponibles en la UE con "
         "iOS 27, en un iPhone compatible (iPhone 15 Pro o posterior). Solo falta Siri AI en el iPhone."),
        ("¿Cuál es la mejor alternativa a Siri AI en el iPhone en Europa?",
         "Para preguntar de todo, ChatGPT, Gemini o Claude; Vibe by Mistral si prefieres una empresa "
         "europea. Ninguna lee tus mensajes ni actúa en las apps como Siri AI. Para un asistente privado "
         "que funcione sin conexión, Pinku o Locally AI."),
        ("¿Siri AI funciona en español?",
         "Todavía no. Apple dice que, por ahora, Siri AI está disponible en inglés."),
        ("¿Hay un asistente de IA que deje mis chats en el iPhone?",
         "Sí. Apps en el dispositivo como Pinku y Locally AI ejecutan el modelo en el iPhone, así que la "
         "conversación no se envía a ningún servidor. Son menos capaces que los asistentes en la nube."),
    ],
}

SIRI_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(siri)s"%(x)s>How to get Siri AI</a> (EU, languages, features, requirements), published 22 September 2026.</li>
<li>Apple, <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (features available in the EU, devices), published 14 September 2026.</li>
<li>App Store pages (Spain), including prices, ratings and App Privacy: <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, as shown on %(date)s.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
"""

SIRI_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Apple, <a href="%(siri)s"%(x)s>C&oacute;mo obtener Siri AI</a> (UE, idiomas, funciones, requisitos), publicada el 22 de septiembre de 2026.</li>
<li>Apple, <a href="%(reqs)s"%(x)s>C&oacute;mo obtener la nueva generaci&oacute;n de Apple Intelligence</a> (funciones disponibles en la UE, dispositivos), publicada el 14 de septiembre de 2026.</li>
<li>Fichas del App Store (Espa&ntilde;a), con precios, valoraciones y privacidad: <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, tal como se ve&iacute;an el %(date)s.</li>
</ul>
<p>Si algo ha cambiado, <a href="mailto:sagalabs@proton.me">escr&iacute;benos</a> y lo
corregimos.</p>
"""


# ==========================================================================
# Lista y build
# ==========================================================================

ARTICLES = [
    dict(
        en_path="blog/does-apple-intelligence-work-offline-iphone.html",
        es_path="blog/es/apple-intelligence-funciona-sin-internet-iphone.html",
        steps=OFF_STEPS, faq=OFF_FAQ,
        en=dict(h1="Does Apple Intelligence work offline? What works without internet on iPhone (2026)",
                desc=("Apple Intelligence runs some requests on the iPhone and sends others to Apple's "
                      "servers. What Apple's own pages say needs a connection, how to see what left your "
                      "phone, and how to get an AI chat that works fully offline. Written by Pinku's "
                      "maker, disclosed."),
                kicker="Guide", section="Guides",
                standfirst=("Partly. Some requests run on the device and heavier ones go to Apple's "
                            "Private Cloud Compute servers. What Apple's documentation says, and how to "
                            "check on your own phone."),
                body=OFF_EN_BODY, sources=OFF_EN_SOURCES,
                steps_h="How to check whether a feature ran on your iPhone"),
        es=dict(h1="¿Funciona Apple Intelligence sin internet? Lo que va sin conexión en el iPhone (2026)",
                desc=("Apple Intelligence resuelve unas peticiones en el iPhone y manda otras a los "
                      "servidores de Apple. Qué dicen las páginas de Apple que necesita conexión, cómo ver "
                      "qué ha salido del móvil y cómo tener un chat de IA que funcione sin internet. "
                      "Escrito por quien hace Pinku, y lo decimos."),
                kicker="Gu&iacute;a", section="Guías",
                standfirst=("En parte. Unas peticiones se resuelven en el dispositivo y las pesadas van a "
                            "Private Cloud Compute, los servidores de Apple. Qu&eacute; dice la "
                            "documentaci&oacute;n de Apple y c&oacute;mo comprobarlo en tu m&oacute;vil."),
                body=OFF_ES_BODY, sources=OFF_ES_SOURCES,
                steps_h="C&oacute;mo comprobar si una funci&oacute;n se ejecut&oacute; en tu iPhone"),
    ),
    dict(
        en_path="blog/best-ai-apps-iphone-without-apple-intelligence.html",
        es_path="blog/es/mejores-apps-ia-iphone-sin-apple-intelligence.html",
        rank=_rank_items, faq=NOAI_FAQ,
        en=dict(h1="Best AI apps for iPhones without Apple Intelligence (2026)",
                desc=("iOS 27 runs on iPhone 11 and later, Apple Intelligence only on iPhone 15 Pro and "
                      "newer. Pinku, Locally AI, PocketPal, Private LLM, ChatGPT, Gemini, Claude and Vibe "
                      "ranked for the iPhones in between: offline or cloud, requirements and price. "
                      "Ours is first, disclosed."),
                kicker="Rankings", section="Rankings",
                standfirst=("Your iPhone runs iOS 27 but has no Apple Intelligence. Eight apps that give "
                            "it an AI assistant, on the phone or in the cloud."),
                body=NOAI_EN_BODY, sources=NOAI_EN_SOURCES),
        es=dict(h1="Las mejores apps de IA para iPhone sin Apple Intelligence (2026)",
                desc=("iOS 27 funciona desde el iPhone 11 y Apple Intelligence solo desde el iPhone 15 Pro. "
                      "Pinku, Locally AI, PocketPal, Private LLM, ChatGPT, Gemini, Claude y Vibe ordenadas "
                      "para los iPhone de en medio: sin conexión o en la nube, requisitos y precio. La "
                      "primera es nuestra, y lo decimos."),
                kicker="Rankings", section="Rankings",
                standfirst=("Tu iPhone tiene iOS 27 pero no Apple Intelligence. Ocho apps que le dan un "
                            "asistente de IA, en el m&oacute;vil o en la nube."),
                body=NOAI_ES_BODY, sources=NOAI_ES_SOURCES),
    ),
    dict(
        en_path="blog/best-siri-ai-alternatives-iphone-eu.html",
        es_path="blog/es/mejores-alternativas-siri-ai-iphone-ue.html",
        rank=_siri_items, faq=SIRI_FAQ,
        en=dict(h1="Best Siri AI alternatives for iPhone in the EU (2026)",
                desc=("Apple says Siri AI is not available on iPhone in the EU. What Siri AI does, which "
                      "Apple Intelligence features EU iPhones still get, and the apps that cover each part: "
                      "ChatGPT, Gemini, Claude, Vibe by Mistral, Pinku and Locally AI. Pinku is ours, "
                      "disclosed."),
                kicker="Comparisons", section="Comparisons",
                standfirst=("The new Siri is not coming to iPhones in the EU for now. What you lose, what "
                            "you keep, and what to use instead."),
                body=SIRI_EN_BODY, sources=SIRI_EN_SOURCES),
        es=dict(h1="Las mejores alternativas a Siri AI en el iPhone en la UE (2026)",
                desc=("Apple dice que Siri AI no está disponible en el iPhone en la UE. Qué hace Siri AI, "
                      "qué funciones de Apple Intelligence siguen teniendo los iPhone de la UE y qué apps "
                      "cubren cada parte: ChatGPT, Gemini, Claude, Vibe by Mistral, Pinku y Locally AI. "
                      "Pinku es nuestra, y lo decimos."),
                kicker="Comparativas", section="Comparativas",
                standfirst=("La Siri nueva no llega de momento a los iPhone de la UE. Qu&eacute; pierdes, "
                            "qu&eacute; conservas y qu&eacute; usar en su lugar."),
                body=SIRI_ES_BODY, sources=SIRI_ES_SOURCES),
    ),
]


def _plain(s):
    import html
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def _steps_html(steps, heading):
    out = ['\n<h3>%s</h3>\n<ol class="howto-steps">\n' % heading]
    for name, text in steps:
        out.append("<li><strong>%s</strong> %s</li>\n" % (name, text))
    out.append("</ol>\n")
    return "".join(out)


def _ld(spec, lang, L, path):
    art = json.loads(_jsonld(_plain(L["h1"]), _plain(L["desc"]), "https://aisagalab.com/" + path, lang,
                             _plain(L["section"]), DATE_ISO))
    art.pop("@context")
    graph = [art]
    if spec.get("rank"):
        items = spec["rank"](lang)
        graph.append({
            "@type": "ItemList", "name": _plain(L["h1"]),
            "itemListOrder": "https://schema.org/ItemListOrderAscending",
            "numberOfItems": len(items),
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": u}
                                for i, (n, u) in enumerate(items)],
        })
    if spec.get("steps"):
        graph.append({
            "@type": "HowTo", "name": _plain(L["steps_h"]), "inLanguage": lang,
            "step": [{"@type": "HowToStep", "position": i + 1, "name": _plain(n), "text": _plain(t)}
                     for i, (n, t) in enumerate(spec["steps"][lang])],
        })
    graph.append({
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in spec["faq"][lang]],
    })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def build(render, hreflang):
    out = []
    byline = '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN
    for spec in ARTICLES:
        alt = hreflang(spec["en_path"], spec["es_path"])
        for lang in ("en", "es"):
            L = spec[lang]
            path = spec[lang + "_path"]
            if lang == "en":
                other = ("Leer en espa&ntilde;ol", "es/" + spec["es_path"].split("/")[-1])
            else:
                other = ("Read in English", "../" + spec["en_path"].split("/")[-1])
            d = _links(lang)
            if spec.get("steps"):
                d["steps"] = _steps_html(spec["steps"][lang], L["steps_h"])
            body = (_head(L["kicker"], L["h1"], L["standfirst"], byline + DATE[lang], other[0], other[1])
                    + '\n        <div class="article-body">' + (L["body"] % d)
                    + _faq_html(spec["faq"][lang],
                                "Questions people ask" if lang == "en" else "Preguntas frecuentes")
                    + '</div>\n        <div class="article-body article-sources">' + (L["sources"] % d)
                    + '</div>')
            out.append(render(path=path, lang=lang, title=_plain(L["h1"]) + " | Saga Labs",
                              desc=_plain(L["desc"]), og_title=_plain(L["h1"]), body=body,
                              jsonld=_ld(spec, lang, L, path), alternates=alt))
    return out
