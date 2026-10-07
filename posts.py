# -*- coding: utf-8 -*-
"""Contenido de los articulos. build_blog.py pone el chrome; aqui solo va texto.

Regla heredada de Dora (lib/mcp-facts.ts): toda cifra que se publique tiene que
salir de una fuente primaria enlazada en el propio articulo. Los motores de
respuesta degradan a la fuente que se contradice a si misma, y una politica de
retencion mal citada es ademas un problema legal.

Verificado el 5 de septiembre de 2026 contra:
  Google   support.google.com/gemini/answer/13594961  (Gemini Apps Privacy Notice)
  Anthropic privacy.anthropic.com/.../10023548        (actualizado 1 jul 2026)
  OpenAI    help.openai.com/.../8983778 y 8809935
"""

DATE_ISO = "2026-09-05"
DATE_EN = "5 September 2026"
DATE_ES = "5 de septiembre de 2026"

LINKEDIN = "https://www.linkedin.com/in/maruta/"

APP_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-blog&amp;mt=8"
KEEPER = "https://apps.apple.com/au/app/only-gallery-keeper/id1532670722"


def _jsonld(headline, desc, url, lang, section, date=None):
    return """{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": %s,
  "description": %s,
  "inLanguage": "%s",
  "articleSection": "%s",
  "datePublished": "%s",
  "dateModified": "%s",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "%s" },
  "author": {
    "@type": "Person",
    "name": "Maruta G",
    "url": "https://www.linkedin.com/in/maruta/",
    "sameAs": [
      "https://www.linkedin.com/in/maruta/",
      "https://github.com/Saga-Labs",
      "https://x.com/SagaAILab"
    ],
    "affiliation": { "@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/" }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Saga Labs",
    "url": "https://aisagalab.com/",
    "sameAs": [
      "https://aisagalab.com/",
      "https://x.com/SagaAILab",
      "https://github.com/Saga-Labs"
    ]
  }
}""" % (_q(headline), _q(desc), lang, section, date or DATE_ISO, date or DATE_ISO, url)


def _q(s):
    return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"')


def _head(kicker, h1, standfirst, byline, other_lang_label, other_lang_href):
    return """        <p class="article-kicker">%s</p>
        <h1>%s</h1>
        <p class="article-standfirst">%s</p>
        <p class="article-meta">%s
            <span class="lang-switch"> &middot; <a href="%s">%s</a></span>
        </p>""" % (kicker, h1, standfirst, byline, other_lang_href, other_lang_label)


# --------------------------------------------------------------------------
# 1 — Que hacen de verdad con tus conversaciones
# --------------------------------------------------------------------------

A1_EN_BODY = """
<p>Every mainstream AI assistant runs on someone else's computer. You type a
question, it travels to a data centre, and what happens to it next is governed
by a policy document you almost certainly have not read.</p>

<p>This article is a summary of what those documents currently say. Every number
below comes from the provider's own published policy, linked at the end. Where a
provider is vague, we say so rather than filling the gap.</p>

<h2>The short version</h2>

<div class="table-scroll">
<table>
<thead>
<tr><th>&nbsp;</th><th>ChatGPT (free/Plus)</th><th>Claude (free/Pro/Max)</th><th>Gemini Apps</th></tr>
</thead>
<tbody>
<tr><th>Trains on your chats by default</th><td>Yes, unless you turn it off in Data Controls</td><td>Only if you enable the model improvement setting</td><td>Yes, while Keep Activity is on</td></tr>
<tr><th>When you delete a chat</th><td>Gone from back-end systems within 30 days</td><td>Gone from back-end storage within 30 days</td><td>Deleted &mdash; except chats a human reviewer has seen</td></tr>
<tr><th>Kept even after you delete</th><td>Data already used in a completed training run; anything under legal hold</td><td>Up to 5 years de-identified if training was on; 2 years if flagged; 7 years for safety scores</td><td>Human-reviewed chats: up to 3 years</td></tr>
<tr><th>Humans may read it</th><td>Yes, for abuse review and safety</td><td>Yes, if flagged by trust and safety systems</td><td>Yes &mdash; a subset of chats, by Google staff and trained service providers</td></tr>
<tr><th>Default retention if you do nothing</th><td>Until you delete</td><td>Until you delete</td><td>18 months, then auto-deleted</td></tr>
</tbody>
</table>
</div>

<h2>Google says the quiet part out loud</h2>

<p>The Gemini Apps Privacy Notice is the most explicit of the three, and worth
quoting directly. On what happens when you press delete:</p>

<blockquote>Chats reviewed by human reviewers (and related data like your
language, device type, location info, or feedback) are not deleted when you
delete your activity. Instead, they are retained for up to three years.</blockquote>

<p>Read that carefully. Deleting your activity does not delete the copy a human
already looked at. That copy has its own three-year clock, and you have no
control over it.</p>

<p>Google is equally direct about what you should therefore avoid typing:</p>

<blockquote>If that setting is on, don't enter data that's confidential or that
you wouldn't want a reviewer to see or Google to use to improve its
services.</blockquote>

<p>And turning the setting off is not a full exit either. The same notice says
that even with Keep Activity off, or in a temporary chat, Google still uses your
chats to respond to you and to protect Google, its users and the public,
&ldquo;including with help from human reviewers&rdquo;.</p>

<h2>Anthropic publishes the longest clocks</h2>

<p>Anthropic's retention page, updated on 1 July 2026, is unusually specific,
which is to its credit. Deleting a conversation removes it from your history
immediately and from back-end storage within 30 days. But three other clocks run
alongside that one:</p>

<ul>
<li>If you allow your chats to be used to improve Claude, they may be kept in
de-identified form for <strong>up to five years</strong> in model training
pipelines.</li>
<li>If an automated trust and safety system flags a conversation, inputs and
outputs are kept for <strong>up to two years</strong>, and the classification
scores for <strong>up to seven years</strong>.</li>
<li>Feedback you submit &mdash; a thumbs up, a bug report &mdash; is kept for
<strong>five years</strong>.</li>
</ul>

<p>Anthropic also states plainly what no provider can undo: if a training run
already used your data, turning the setting off afterwards does not remove it
from models that have already been trained.</p>

<h2>OpenAI: the default runs the other way for consumers</h2>

<p>On consumer ChatGPT plans, your conversations may be used to improve OpenAI's
models unless you opt out in Data Controls. On Team, Enterprise and API
accounts, the default is reversed: business data is not used for training. The
difference matters, because the person most likely to paste something sensitive
into a chat is a professional using the consumer app on their own phone.</p>

<p>Deleted conversations are removed from OpenAI's systems within 30 days, with
an exception for de-identified data and legal obligations. That exception is not
theoretical: in the copyright litigation brought by The New York Times, a court
ordered OpenAI for five months to preserve output logs that would otherwise have
been deleted, and a sample of twenty million of them was later handed to the
plaintiffs' lawyers. The order itself was lifted in October 2025. We go through
the whole timeline in
<a href="i-sent-openai-and-anthropic-a-gdpr-erasure-request.html">what &ldquo;delete&rdquo;
actually means</a>.</p>

<h2>What none of this means</h2>

<p>It does not mean these companies are acting in bad faith. Retention windows
exist for real reasons: abuse investigation, incident response, legal
obligations. Human review genuinely does make models safer.</p>

<p>What it means is narrower and harder to argue with: <strong>once a
conversation leaves your device, its lifetime is governed by someone else's
policy, someone else's security, and potentially someone else's court
order</strong>. You can change a setting. You cannot change the architecture.</p>

<h2>The only category where the question does not arise</h2>

<p>There is one arrangement in which none of the rows in that table apply,
because there is nothing to retain: a model that runs on your own hardware and
never opens a network connection.</p>

<p>That is what <a href="%s">Pinku</a> does. The model file is downloaded once
and every token after that is generated by your iPhone or your Mac. There is no
account, no server, no retention window, no human reviewer, and no setting to
get wrong &mdash; the conversation is a file on your device, and deleting it is a
file deletion.</p>

<p>The honest trade-off is capability: a 1&ndash;4&nbsp;GB model on a phone is not
GPT-5, and pretending otherwise would be the same kind of marketing this article
is arguing against. We compared the apps that run a model on your
own device, ours included and where the others beat it, in
<a href="best-offline-ai-chat-apps-iphone-mac.html">Best offline AI chat apps for iPhone and Mac</a>.</p>
""" % APP_STORE

A1_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li><a href="https://support.google.com/gemini/answer/13594961" rel="nofollow noopener" target="_blank">Gemini Apps Privacy Notice</a> &mdash; Google. Retention, human review and the three-year window for reviewed chats.</li>
<li><a href="https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data" rel="nofollow noopener" target="_blank">How long do you store my data?</a> &mdash; Anthropic Privacy Center, updated 1 July 2026.</li>
<li><a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt" rel="nofollow noopener" target="_blank">Chat and file retention policies in ChatGPT</a> &mdash; OpenAI Help Center.</li>
<li><a href="https://openai.com/index/response-to-nyt-data-demands/" rel="nofollow noopener" target="_blank">How we're responding to The New York Times' data demands</a> &mdash; OpenAI.</li>
</ul>
<p>Figures checked on 5 September 2026. Policies change; if you find one of these
out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will correct
the page.</p>
"""


A1_ES_BODY = """
<p>Todos los asistentes de IA que usa la gente corren en el ordenador de otro.
Escribes una pregunta, viaja a un centro de datos, y lo que pasa despu&eacute;s
con ella lo decide un documento que casi con seguridad no has le&iacute;do.</p>

<p>Este art&iacute;culo resume lo que dicen hoy esos documentos. Cada cifra sale
de la pol&iacute;tica publicada por el propio proveedor, enlazada al final.
Cuando un proveedor es ambiguo, lo decimos en vez de rellenar el hueco.</p>

<h2>La versi&oacute;n corta</h2>

<div class="table-scroll">
<table>
<thead>
<tr><th>&nbsp;</th><th>ChatGPT (gratis/Plus)</th><th>Claude (gratis/Pro/Max)</th><th>Gemini Apps</th></tr>
</thead>
<tbody>
<tr><th>Entrena con tus chats por defecto</th><td>S&iacute;, salvo que lo desactives en Data Controls</td><td>Solo si activas la mejora del modelo</td><td>S&iacute;, mientras Keep Activity est&eacute; encendido</td></tr>
<tr><th>Al borrar un chat</th><td>Fuera de sus sistemas en 30 d&iacute;as</td><td>Fuera del almacenamiento en 30 d&iacute;as</td><td>Se borra &mdash; salvo lo que haya visto un revisor humano</td></tr>
<tr><th>Se conserva aunque borres</th><td>Lo ya usado en un entrenamiento terminado; lo que est&eacute; bajo orden judicial</td><td>Hasta 5 a&ntilde;os anonimizado si el entrenamiento estaba activo; 2 a&ntilde;os si se marc&oacute;; 7 a&ntilde;os las puntuaciones de seguridad</td><td>Chats revisados por humanos: hasta 3 a&ntilde;os</td></tr>
<tr><th>Puede leerlo una persona</th><td>S&iacute;, para revisi&oacute;n de abuso y seguridad</td><td>S&iacute;, si lo marcan los sistemas de seguridad</td><td>S&iacute; &mdash; una parte de los chats, por personal de Google y proveedores</td></tr>
<tr><th>Retenci&oacute;n si no tocas nada</th><td>Hasta que borres</td><td>Hasta que borres</td><td>18 meses y se autoborra</td></tr>
</tbody>
</table>
</div>

<h2>Google lo dice sin rodeos</h2>

<p>El aviso de privacidad de Gemini Apps es el m&aacute;s expl&iacute;cito de los
tres y merece cita literal. Sobre qu&eacute; pasa cuando pulsas borrar:</p>

<blockquote>Los chats revisados por revisores humanos (y datos asociados como tu
idioma, tipo de dispositivo, informaci&oacute;n de ubicaci&oacute;n o
comentarios) no se eliminan cuando borras tu actividad. En su lugar se conservan
hasta tres a&ntilde;os.</blockquote>

<p>L&eacute;elo despacio. Borrar tu actividad no borra la copia que ya mir&oacute;
una persona. Esa copia tiene su propio reloj de tres a&ntilde;os y t&uacute; no
tienes ning&uacute;n control sobre &eacute;l.</p>

<p>Google es igual de directo sobre lo que no deber&iacute;as escribir:</p>

<blockquote>Si ese ajuste est&aacute; activado, no introduzcas datos
confidenciales ni nada que no quieras que vea un revisor o que Google use para
mejorar sus servicios.</blockquote>

<p>Y apagar el ajuste tampoco es una salida completa. El mismo aviso dice que,
incluso con Keep Activity desactivado o en un chat temporal, Google sigue usando
tus conversaciones para responderte y para proteger a Google, a sus usuarios y al
p&uacute;blico, &laquo;incluso con ayuda de revisores humanos&raquo;.</p>

<h2>Anthropic publica los relojes m&aacute;s largos</h2>

<p>La p&aacute;gina de retenci&oacute;n de Anthropic, actualizada el 1 de julio
de 2026, es inusualmente concreta, y eso hay que reconoc&eacute;rselo. Borrar una
conversaci&oacute;n la quita del historial al momento y del almacenamiento en 30
d&iacute;as. Pero en paralelo corren otros tres relojes:</p>

<ul>
<li>Si permites que tus chats se usen para mejorar Claude, pueden conservarse de
forma anonimizada <strong>hasta cinco a&ntilde;os</strong> en las tuber&iacute;as
de entrenamiento.</li>
<li>Si un sistema autom&aacute;tico marca una conversaci&oacute;n, entradas y
salidas se guardan <strong>hasta dos a&ntilde;os</strong>, y las puntuaciones de
clasificaci&oacute;n <strong>hasta siete a&ntilde;os</strong>.</li>
<li>Los comentarios que env&iacute;as &mdash; un pulgar arriba, un informe de
error &mdash; se guardan <strong>cinco a&ntilde;os</strong>.</li>
</ul>

<p>Anthropic tambi&eacute;n dice con claridad lo que ning&uacute;n proveedor
puede deshacer: si un entrenamiento ya us&oacute; tus datos, desactivar el ajuste
despu&eacute;s no los saca de los modelos ya entrenados.</p>

<h2>OpenAI: en consumo el defecto va al rev&eacute;s</h2>

<p>En los planes de consumo de ChatGPT, tus conversaciones pueden usarse para
mejorar los modelos de OpenAI salvo que lo desactives en Data Controls. En Team,
Enterprise y API el defecto es el contrario: los datos de empresa no se usan para
entrenar. La diferencia importa, porque quien m&aacute;s probablemente pegue algo
sensible en un chat es un profesional usando la app de consumo en su
m&oacute;vil.</p>

<p>Las conversaciones borradas salen de los sistemas de OpenAI en 30 d&iacute;as,
con una excepci&oacute;n para datos anonimizados y obligaciones legales. Esa
excepci&oacute;n no es te&oacute;rica: en el pleito de derechos de autor del New
York Times, un tribunal oblig&oacute; a OpenAI durante cinco meses a conservar
registros que de otro modo se habr&iacute;an borrado, y una muestra de veinte
millones acab&oacute; en manos de los abogados de la parte contraria. La orden se
levant&oacute; en octubre de 2025. Repasamos la cronolog&iacute;a entera en
<a href="solicitud-de-borrado-rgpd-a-openai-y-anthropic.html">qu&eacute;
significa de verdad borrar un chat</a>.</p>

<h2>Lo que nada de esto significa</h2>

<p>No significa que estas empresas act&uacute;en de mala fe. Los plazos de
retenci&oacute;n existen por motivos reales: investigar abusos, responder a
incidentes, cumplir la ley. La revisi&oacute;n humana s&iacute; hace los modelos
m&aacute;s seguros.</p>

<p>Lo que significa es m&aacute;s estrecho y m&aacute;s dif&iacute;cil de
discutir: <strong>en cuanto una conversaci&oacute;n sale de tu dispositivo, su
vida la gobierna la pol&iacute;tica de otro, la seguridad de otro y,
potencialmente, la orden judicial de otro</strong>. Puedes cambiar un ajuste. No
puedes cambiar la arquitectura.</p>

<h2>La &uacute;nica categor&iacute;a donde la pregunta no existe</h2>

<p>Hay una disposici&oacute;n en la que ninguna fila de esa tabla aplica, porque
no hay nada que retener: un modelo que corre en tu propio hardware y nunca abre
una conexi&oacute;n de red.</p>

<p>Es lo que hace <a href="%s">Pinku</a>. El archivo del modelo se descarga una
vez y todo lo que viene despu&eacute;s lo genera tu iPhone o tu Mac. No hay
cuenta, ni servidor, ni ventana de retenci&oacute;n, ni revisor humano, ni ajuste
que puedas dejar mal puesto: la conversaci&oacute;n es un archivo en tu
dispositivo y borrarla es borrar un archivo.</p>

<p>El intercambio honesto es la capacidad: un modelo de 1 a 4&nbsp;GB en un
m&oacute;vil no es GPT-5, y fingir lo contrario ser&iacute;a el mismo marketing
contra el que argumenta este art&iacute;culo. Comparamos las apps que ejecutan el modelo
en tu propio dispositivo, la nuestra incluida y en qu&eacute; le ganan las
dem&aacute;s, en
<a href="mejores-apps-ia-sin-conexion-iphone-mac.html">Las mejores apps de IA sin conexi&oacute;n para iPhone y Mac</a>.</p>
""" % APP_STORE

A1_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li><a href="https://support.google.com/gemini/answer/13594961" rel="nofollow noopener" target="_blank">Aviso de privacidad de Gemini Apps</a> &mdash; Google. Retenci&oacute;n, revisi&oacute;n humana y la ventana de tres a&ntilde;os.</li>
<li><a href="https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data" rel="nofollow noopener" target="_blank">How long do you store my data?</a> &mdash; Centro de privacidad de Anthropic, actualizado el 1 de julio de 2026.</li>
<li><a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt" rel="nofollow noopener" target="_blank">Chat and file retention policies in ChatGPT</a> &mdash; Centro de ayuda de OpenAI.</li>
<li><a href="https://openai.com/index/response-to-nyt-data-demands/" rel="nofollow noopener" target="_blank">How we're responding to The New York Times' data demands</a> &mdash; OpenAI.</li>
</ul>
<p>Cifras comprobadas el 5 de septiembre de 2026. Las pol&iacute;ticas cambian; si
encuentras alguna desactualizada, <a href="mailto:sagalabs@proton.me">av&iacute;sanos</a>
y corregimos la p&aacute;gina.</p>
"""


# --------------------------------------------------------------------------
# Indices
# --------------------------------------------------------------------------

INDEX_EN = """
        <p class="article-kicker">Saga Labs</p>
        <h1>Blog</h1>
        <p class="article-standfirst">Notes on private and on-device AI. Every
        number we publish comes from a primary source, linked in the article.</p>
        <p class="article-meta">Maruta G
            <span class="lang-switch"> &middot; <a href="es/">Leer en espa&ntilde;ol</a></span>
        </p>
        <div class="article-body">
        <ul class="post-list">
            <li>
                <a href="best-ai-video-generator-apps-iphone.html">Best AI video generator apps for iPhone in 2026</a>
                <p>Runway, Kling AI, Pika, PixVerse, Luma Dream Machine, invideo,
                CapCut and our own Dora: what each one is best at, how it
                charges, and who it is for.</p>
            </li>
            <li>
                <a href="best-offline-ai-chat-apps-iphone-mac.html">Best offline AI chat apps for iPhone and Mac (2026)</a>
                <p>Locally AI, Enclave, PocketPal, Private LLM, Privacy AI and
                our own Pinku: price, models, Mac support and where each one is
                strongest. Plus how to choose, and where ChatGPT is not available.</p>
            </li>
            <li>
                <a href="best-photo-vault-apps-iphone.html">Photo vault apps for iPhone, compared</a>
                <p>Pic Safe, Keepsafe, Arca and our own Photo Vault against the
                Hidden album that comes with the phone. The real choice is whether
                your private photos should have a backup.</p>
            </li>
            <li>
                <a href="what-ai-does-with-your-conversations.html">What ChatGPT, Claude and Gemini actually do with your conversations</a>
                <p>Retention windows, human review and training defaults for the
                three main assistants, taken from their own published policies.
                Google keeps human-reviewed chats for three years after you
                delete them.</p>
            </li>
            <li>
                <a href="i-sent-openai-and-anthropic-a-gdpr-erasure-request.html">I sent OpenAI and Anthropic a GDPR erasure request. Neither told me what they kept.</a>
                <p>Five layers sit between the button and the conversation being
                gone. We asked OpenAI and Anthropic to delete our data; neither
                said it was gone, and both were being accurate.</p>
            </li>
        </ul>
        </div>
"""

INDEX_ES = """
        <p class="article-kicker">Saga Labs</p>
        <h1>Blog</h1>
        <p class="article-standfirst">Notas sobre IA privada y en el dispositivo.
        Cada cifra que publicamos sale de una fuente primaria enlazada en el
        art&iacute;culo.</p>
        <p class="article-meta">Maruta G
            <span class="lang-switch"> &middot; <a href="../">Read in English</a></span>
        </p>
        <div class="article-body">
        <ul class="post-list">
            <li>
                <a href="mejores-apps-generador-video-ia-iphone.html">Las mejores apps para generar v&iacute;deo con IA en iPhone (2026)</a>
                <p>Runway, Kling AI, Pika, PixVerse, Luma Dream Machine, invideo,
                CapCut y nuestra Dora: en qu&eacute; destaca cada una, c&oacute;mo
                cobra y para qui&eacute;n es.</p>
            </li>
            <li>
                <a href="mejores-apps-ia-sin-conexion-iphone-mac.html">Las mejores apps de IA sin conexi&oacute;n para iPhone y Mac (2026)</a>
                <p>Locally AI, Enclave, PocketPal, Private LLM, Privacy AI y
                nuestra Pinku: precio, modelos, Mac y en qu&eacute; destaca cada
                una. Con c&oacute;mo elegir y d&oacute;nde no est&aacute; ChatGPT.</p>
            </li>
            <li>
                <a href="apps-para-ocultar-fotos-iphone.html">Apps para ocultar fotos en iPhone, comparadas</a>
                <p>Pic Safe, Keepsafe, Arca y nuestra Photo Vault frente al
                &aacute;lbum Oculto que ya trae el m&oacute;vil. La decisi&oacute;n
                de verdad es si tus fotos privadas deben tener copia.</p>
            </li>
            <li>
                <a href="que-hace-la-ia-con-tus-conversaciones.html">Qu&eacute; hacen de verdad ChatGPT, Claude y Gemini con tus conversaciones</a>
                <p>Plazos de retenci&oacute;n, revisi&oacute;n humana y valores por
                defecto de entrenamiento de los tres asistentes principales, sacados
                de sus propias pol&iacute;ticas. Google conserva tres a&ntilde;os los
                chats revisados por humanos despu&eacute;s de que los borres.</p>
            </li>
            <li>
                <a href="solicitud-de-borrado-rgpd-a-openai-y-anthropic.html">Mandé a OpenAI y a Anthropic una solicitud de borrado del RGPD. Ninguno me dijo qué se quedaban.</a>
                <p>Entre el bot&oacute;n y que la conversaci&oacute;n desaparezca
                hay cinco capas. Pedimos a OpenAI y a Anthropic que borraran
                nuestros datos: ninguno dijo que estuvieran borrados, y los dos
                estaban siendo exactos.</p>
            </li>
        </ul>
        </div>
"""


def build(render, hreflang):
    out = []

    # --- indices -----------------------------------------------------------
    out.append(render(
        path="blog/index.html", lang="en",
        title="Blog — Saga Labs",
        desc="Notes on private and on-device AI from Saga Labs, the studio behind Pinku Private AI. Sourced from primary policy documents.",
        og_title="Blog — Saga Labs",
        alternates=hreflang("blog/", "blog/es/"),
        og_type="website",
        jsonld="""{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Saga Labs Blog",
  "url": "https://aisagalab.com/blog/",
  "inLanguage": "en",
  "publisher": { "@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/" }
}""",
        body=INDEX_EN,
    ))

    out.append(render(
        path="blog/es/index.html", lang="es",
        title="Blog — Saga Labs",
        desc="Notas sobre IA privada y en el dispositivo, del estudio detrás de Pinku Private AI. Con fuentes primarias.",
        og_title="Blog — Saga Labs",
        alternates=hreflang("blog/", "blog/es/"),
        og_type="website",
        jsonld="""{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Saga Labs Blog",
  "url": "https://aisagalab.com/blog/es/",
  "inLanguage": "es",
  "publisher": { "@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/" }
}""",
        body=INDEX_ES,
    ))

    # --- 1: que hacen con tus conversaciones -------------------------------
    en_path = "blog/what-ai-does-with-your-conversations.html"
    es_path = "blog/es/que-hace-la-ia-con-tus-conversaciones.html"
    alt = hreflang(en_path, es_path)

    h1_en = "What ChatGPT, Claude and Gemini actually do with your conversations"
    d_en = ("Retention windows, human review and training defaults for the three main AI "
            "assistants, quoted from their own published policies and checked in September 2026.")
    out.append(render(
        path=en_path, lang="en",
        title=h1_en + " — Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "Privacy"),
        body=_head(
            "Privacy", h1_en,
            "Three assistants, three sets of defaults, and one thing they have in "
            "common: the conversation leaves your device.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + DATE_EN,
            "Leer en espa&ntilde;ol", "es/que-hace-la-ia-con-tus-conversaciones.html",
        ) + '\n        <div class="article-body">' + A1_EN_BODY
          + '</div>\n        <div class="article-body article-sources">' + A1_EN_SOURCES + '</div>',
    ))

    h1_es = "Qué hacen de verdad ChatGPT, Claude y Gemini con tus conversaciones"
    d_es = ("Plazos de retención, revisión humana y valores por defecto de entrenamiento de los "
            "tres asistentes principales, citados de sus propias políticas y comprobados en septiembre de 2026.")
    out.append(render(
        path=es_path, lang="es",
        title=h1_es + " — Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "Privacidad"),
        body=_head(
            "Privacidad", "Qu&eacute; hacen de verdad ChatGPT, Claude y Gemini con tus conversaciones",
            "Tres asistentes, tres conjuntos de valores por defecto y una cosa en "
            "com&uacute;n: la conversaci&oacute;n sale de tu dispositivo.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + DATE_ES,
            "Read in English", "../what-ai-does-with-your-conversations.html",
        ) + '\n        <div class="article-body">' + A1_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A1_ES_SOURCES + '</div>',
    ))

    # --- 4: que significa borrar un chat ----------------------------------
    en_path = "blog/i-sent-openai-and-anthropic-a-gdpr-erasure-request.html"
    es_path = "blog/es/solicitud-de-borrado-rgpd-a-openai-y-anthropic.html"
    alt = hreflang(en_path, es_path)

    h1_en = "I sent OpenAI and Anthropic a GDPR erasure request. Neither told me what they kept."
    d_en = ("Five layers sit between the delete button and the conversation being gone: "
            "storage, model weights, the reviewer's copy, the safety flag and the court. "
            "With the OpenAI privacy team's reply, and Anthropic's.")
    out.append(render(
        path=en_path, lang="en",
        title="I sent OpenAI and Anthropic a GDPR erasure request. Neither told me what they kept. — Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "Privacy"),
        body=_head(
            "Privacy", "I sent OpenAI and Anthropic a GDPR erasure request.<br>Neither told me what they kept.",
            "Five layers sit between the delete button and a conversation actually "
            "being gone. Only the first one is under your control.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + DATE_EN,
            "Leer en espa&ntilde;ol", "es/solicitud-de-borrado-rgpd-a-openai-y-anthropic.html",
        ) + '\n        <div class="article-body">' + A4_EN_BODY
          + '</div>\n        <div class="article-body article-sources">' + A4_EN_SOURCES + '</div>',
    ))

    h1_es = "Mandé a OpenAI y a Anthropic una solicitud de borrado del RGPD. Ninguno me dijo qué se quedaban."
    d_es = ("Entre el bot\u00f3n de borrar y que la conversaci\u00f3n desaparezca hay cinco capas: "
            "almacenamiento, pesos del modelo, la copia del revisor, la marca de seguridad y el "
            "juzgado. Con la respuesta del equipo de privacidad de OpenAI, y la de Anthropic.")
    out.append(render(
        path=es_path, lang="es",
        title=h1_es + " — Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "Privacidad"),
        body=_head(
            "Privacidad", "Mand&eacute; a OpenAI y a Anthropic una solicitud de borrado del RGPD.<br>Ninguno me dijo qu&eacute; se quedaban.",
            "Entre el bot&oacute;n de borrar y que la conversaci&oacute;n desaparezca de "
            "verdad hay cinco capas. Solo la primera depende de ti.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + DATE_ES,
            "Read in English", "../i-sent-openai-and-anthropic-a-gdpr-erasure-request.html",
        ) + '\n        <div class="article-body">' + A4_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A4_ES_SOURCES + '</div>',
    ))

    # --- 5: apps para ocultar fotos ----------------------------------------
    en_path = "blog/best-photo-vault-apps-iphone.html"
    es_path = "blog/es/apps-para-ocultar-fotos-iphone.html"
    alt = hreflang(en_path, es_path)

    h1_en = "Photo vault apps for iPhone, compared"
    d_en = ("Pic Safe, Keepsafe, Arca and Photo Vault against the built-in Hidden album: "
            "cloud or no cloud, account, decoy PIN, disguised icon and ratings, from their own App Store pages.")
    out.append(render(
        path=en_path, lang="en",
        title="Photo vault apps for iPhone, compared (2026) — Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "Privacy", VAULT_DATE_ISO),
        body=_head(
            "Privacy", h1_en,
            "Four vault apps and the Hidden album that comes with the phone. "
            "The real choice is whether your private photos should have a backup.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + VAULT_DATE_EN,
            "Leer en espa&ntilde;ol", "es/apps-para-ocultar-fotos-iphone.html",
        ) + '\n        <div class="article-body">' + A5_EN_BODY
          + '</div>\n        <div class="article-body article-sources">' + A5_EN_SOURCES + '</div>',
    ))

    h1_es = "Apps para ocultar fotos en iPhone, comparadas"
    d_es = ("Pic Safe, Keepsafe, Arca y Photo Vault frente al \u00e1lbum Oculto de serie: "
            "nube o no, cuenta, PIN se\u00f1uelo, icono disfrazado y valoraciones, seg\u00fan su propia ficha del App Store.")
    out.append(render(
        path=es_path, lang="es",
        title="Apps para ocultar fotos en iPhone, comparadas (2026) — Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "Privacidad", VAULT_DATE_ISO),
        body=_head(
            "Privacidad", h1_es,
            "Cuatro apps y el &aacute;lbum Oculto que ya trae el m&oacute;vil. La "
            "decisi&oacute;n de verdad es si tus fotos privadas deben tener copia.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + VAULT_DATE_ES,
            "Read in English", "../best-photo-vault-apps-iphone.html",
        ) + '\n        <div class="article-body">' + A5_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A5_ES_SOURCES + '</div>',
    ))

    # --- 6: apps de IA sin conexion ----------------------------------------
    en_path = "blog/best-offline-ai-chat-apps-iphone-mac.html"
    es_path = "blog/es/mejores-apps-ia-sin-conexion-iphone-mac.html"
    alt = hreflang(en_path, es_path)

    h1_en = "Best offline AI chat apps for iPhone and Mac (2026)"
    d_en = ("Locally AI, Enclave, PocketPal, Private LLM, Privacy AI and Pinku compared: "
            "price, models, Mac support and real strengths, from their App Store pages. "
            "Written by Pinku's maker, disclosed.")
    out.append(render(
        path=en_path, lang="en",
        title="Best offline AI chat apps for iPhone and Mac (2026) | Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "On-device AI", OFF_DATE_ISO),
        body=_head(
            "On-device AI", h1_en,
            "Six apps that run a language model on your own device, no account and "
            "no connection needed. One of them is ours.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + OFF_DATE_EN,
            "Leer en espa&ntilde;ol", "es/mejores-apps-ia-sin-conexion-iphone-mac.html",
        ) + '\n        <div class="article-body">' + A6_EN_BODY
          + '</div>\n        <div class="article-body article-sources">' + A6_EN_SOURCES + '</div>',
    ))

    h1_es = "Las mejores apps de IA sin conexión para iPhone y Mac (2026)"
    d_es = ("Locally AI, Enclave, PocketPal, Private LLM, Privacy AI y Pinku comparadas: "
            "precio, modelos, Mac y en qu\u00e9 destaca cada una, seg\u00fan su ficha del App Store. "
            "Escrito por quien hace Pinku, y lo decimos.")
    out.append(render(
        path=es_path, lang="es",
        title="Las mejores apps de IA sin conexión para iPhone y Mac (2026) | Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "IA en el dispositivo", OFF_DATE_ISO),
        body=_head(
            "IA en el dispositivo", h1_es,
            "Seis apps que ejecutan un modelo de lenguaje en tu propio dispositivo, sin "
            "cuenta y sin conexi&oacute;n. Una de ellas es nuestra.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + OFF_DATE_ES,
            "Read in English", "../best-offline-ai-chat-apps-iphone-mac.html",
        ) + '\n        <div class="article-body">' + A6_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A6_ES_SOURCES + '</div>',
    ))

    # --- 7: apps de video con IA para iPhone --------------------------------
    en_path = "blog/best-ai-video-generator-apps-iphone.html"
    es_path = "blog/es/mejores-apps-generador-video-ia-iphone.html"
    alt = hreflang(en_path, es_path)

    h1_en = "Best AI video generator apps for iPhone in 2026"
    d_en = ("Runway, Kling AI, Pika, PixVerse, Luma Dream Machine, invideo, CapCut and Dora compared: "
            "what each is best at and how it charges, from their App Store pages. "
            "Written by Dora's maker, disclosed.")
    out.append(render(
        path=en_path, lang="en",
        title="Best AI video generator apps for iPhone in 2026 | Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld_faq(_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "AI video", AIV_DATE_ISO), AIV_FAQ_EN),
        body=_head(
            "AI video", h1_en,
            "Eight apps that turn a photo or a few words into a short video on your "
            "iPhone, and who each one is for. One of them is ours.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + AIV_DATE_EN,
            "Leer en espa&ntilde;ol", "es/mejores-apps-generador-video-ia-iphone.html",
        ) + '\n        <div class="article-body">' + A7_EN_BODY
          + _faq_html(AIV_FAQ_EN, "Questions people ask")
          + '</div>\n        <div class="article-body article-sources">' + A7_EN_SOURCES + '</div>',
    ))

    h1_es = "Las mejores apps para generar vídeo con IA en iPhone (2026)"
    d_es = ("Runway, Kling AI, Pika, PixVerse, Luma Dream Machine, invideo, CapCut y Dora comparadas: "
            "en qu\u00e9 destaca cada una y c\u00f3mo cobra, seg\u00fan su ficha del App Store. "
            "Escrito por quien hace Dora, y lo decimos.")
    out.append(render(
        path=es_path, lang="es",
        title="Las mejores apps para generar vídeo con IA en iPhone (2026) | Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld_faq(_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "Vídeo con IA", AIV_DATE_ISO), AIV_FAQ_ES),
        body=_head(
            "V&iacute;deo con IA", h1_es,
            "Ocho apps que convierten una foto o unas palabras en un v&iacute;deo corto "
            "en tu iPhone, y para qui&eacute;n es cada una. Una de ellas es nuestra.",
            '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN + AIV_DATE_ES,
            "Read in English", "../best-ai-video-generator-apps-iphone.html",
        ) + '\n        <div class="article-body">' + A7_ES_BODY
          + _faq_html(AIV_FAQ_ES, "Preguntas frecuentes")
          + '</div>\n        <div class="article-body article-sources">' + A7_ES_SOURCES + '</div>',
    ))

    return out


# --------------------------------------------------------------------------
# 4 — Que significa borrar un chat
# --------------------------------------------------------------------------
#
# Cronologia NYT v. OpenAI verificada el 5 sep 2026. La orden de conservacion
# NO sigue vigente: se levanto en octubre de 2025. Lo que si ocurrio es que los
# registros conservados durante esos cinco meses se acabaron entregando.
# Contarlo mal en cualquiera de las dos direcciones es un problema.

A4_EN_BODY = """
<p>Every AI assistant has a delete button. Pressing it makes a row disappear
from a list, immediately and satisfyingly. Whether it makes anything else happen
is a different question, with a different answer for each layer of the system the
conversation passed through.</p>

<p>None of what follows is a scandal. It is mostly the ordinary consequence of
running software at scale, and some of it is legally required. But the gap
between what the button looks like it does and what it does is wide enough to be
worth writing down.</p>

<h2>Layer 1 — your view, and then the storage</h2>

<p>The row vanishing is instant and local. Behind it, both OpenAI and Anthropic
publish the same window: a deleted conversation is removed from back-end systems
<strong>within 30 days</strong>. Anthropic's wording is &ldquo;deleted from our
back-end storage systems within 30 days&rdquo;; OpenAI's is that deleted chats are
permanently removed within 30 days, unless de-identification or legal exceptions
apply.</p>

<p>Thirty days is a reasonable number. Backups have to roll over, and a system
that deleted from every replica synchronously would be a system that could not be
restored after an incident. But it does mean that &ldquo;deleted&rdquo; means
&ldquo;scheduled for deletion&rdquo; for a month.</p>

<h2>Layer 2 — the weights, which cannot be edited</h2>

<p>If your conversation was used in a training run that has already finished,
deleting the conversation does not remove its influence from the resulting model.
There is no known technique for reaching into a trained network and extracting one
conversation.</p>

<p>Anthropic states this plainly rather than hiding it: turning the setting off
means your data will not be used for <em>future</em> training, but
&ldquo;your data will still be included in model training runs that are already in
progress, or in models that have been trained.&rdquo;</p>

<p>This is the layer people underestimate. Deletion is a storage operation.
Training is not storage.</p>

<h2>Layer 3 — the copy a person read</h2>

<p>All three major providers use human reviewers on some fraction of
conversations. Google's Gemini Apps Privacy Notice is the only one that spells out
what that means for deletion, and the sentence deserves to be read twice:</p>

<blockquote>Chats reviewed by human reviewers (and related data like your
language, device type, location info, or feedback) are not deleted when you delete
your activity. Instead, they are retained for up to three years.</blockquote>

<p>Your delete does not reach that copy. It has its own three-year clock, running
independently of anything in your account settings, and there is no control
surface for it.</p>

<h2>Layer 4 — the safety flag</h2>

<p>If an automated system decides a conversation might violate a usage policy,
different rules apply. Anthropic publishes the numbers: inputs and outputs kept
for <strong>up to two years</strong>, and the trust-and-safety classification
scores for <strong>up to seven years</strong>.</p>

<p>Note the asymmetry. The classification score &mdash; a machine's judgement
about you &mdash; outlives the conversation that produced it by five years.</p>

<p>Which conversations get flagged is not published. What is published is the
policy the flag keys off, and it names four domains as
&ldquo;High-Risk Use Cases&rdquo;:</p>

<blockquote>Legal: Use cases related to legal interpretation, legal guidance, or
decisions with legal implications. Healthcare: Use cases related to healthcare
decisions, medical diagnosis, patient care, therapy, mental health, or other
medical guidance. Insurance: […] Finance: Use cases related to financial
decisions, including investment advice, loan approvals […]</blockquote>

<p>Be careful with what that does and does not say. Those requirements are
addressed to developers building products on Claude: they must put a qualified
professional in the loop and disclose that AI was involved. They are not a
statement that asking about your own health flags your chat, and we are not
claiming that they are.</p>

<p>The precise position is this. The seven-year clock starts when an automated
system decides a conversation may violate the Usage Policy. The Usage Policy is
the document that names those four domains. Whether conversations in them are
more likely to be flagged is not disclosed, and there is no mechanism for you to
find out whether any particular conversation of yours was.</p>

<p>So the categories where you would most want to know &mdash; your health, your
money, your legal exposure &mdash; are exactly the categories where you cannot.
That is not an accusation. It is the honest shape of the information available to
you, and it is the reason some conversations are worth keeping off a network
entirely.</p>

<h2>Layer 5 — the court</h2>

<p>The clearest demonstration that the delete button is not the last word came out
of the copyright litigation brought against OpenAI by The New York Times and
others. The timeline is worth stating precisely, because it is widely
misreported in both directions.</p>

<ul>
<li><strong>13 May 2025.</strong> Magistrate Judge Ona T. Wang orders OpenAI to
preserve and segregate all output log data that would otherwise be deleted &mdash;
including conversations users had deleted.</li>
<li><strong>June 2025.</strong> District Judge Sidney Stein rejects OpenAI's
objection. The order stands.</li>
<li><strong>July 2025.</strong> Plaintiffs move to compel a 120-million-log
sample. OpenAI counter-proposes 20 million de-identified conversations.</li>
<li><strong>October 2025.</strong> Judge Wang terminates the going-forward
preservation obligation. Logs already preserved stay preserved, and data tied to
accounts the plaintiffs flagged must still be retained.</li>
<li><strong>5 January 2026.</strong> The Southern District of New York upholds the
orders requiring OpenAI to produce the 20-million-log sample. The first wave is
delivered to the plaintiffs' legal team that month.</li>
</ul>

<p>So the sweeping preservation order is <em>over</em>. Anyone still saying
&ldquo;OpenAI has to keep your deleted chats forever&rdquo; is a year out of date.</p>

<p>But the part that actually matters is not over. For roughly five months, chats
that users had deleted were retained because a court said so. A sample of twenty
million of them, de-identified, has since been handed to the opposing side's
lawyers in a copyright case. Nobody in that sample was asked, and nobody in it can
tell whether they are in it.</p>

<p>OpenAI fought the order and says the preserved data sits behind a small audited
legal and security team. There is no reason to doubt that. The point is
structural, not moral: <strong>a retention policy is a promise a company makes,
and a court can suspend it for everyone at once.</strong></p>

<h2>I sent both companies a GDPR erasure request</h2>

<p>From my own personal accounts &mdash; the consumer tier this article is
about, not a business plan with different defaults &mdash; I sent OpenAI and
Anthropic a formal request under the GDPR, and kept what came back.</p>

<p>Not a support ticket. A request under Article 15, the right of access, and
Article 17, the right to erasure, asking specifically for the things this article
has been describing:</p>

<blockquote>Any conversations flagged by your trust and safety classifiers, along
with the specific reasons for flagging. Any data derived from my conversations
(classification scores, metadata, logs). Any de-identified data that originated
from my account, including any data used for model training. Information about
how long each category of my data will be retained and the legal basis for such
retention. […] Please confirm in writing what data has been deleted and, if any
data is retained, provide the specific legal basis for each category of retained
data as required under Article 17(3).</blockquote>

<p>That last sentence is the test. It is not a favour to ask: under Article 12(3)
a controller has one month to respond.</p>

<h3>The timeline</h3>

<ul>
<li><strong>15 April 2026.</strong> Request sent to both companies.</li>
<li><strong>15 April.</strong> Anthropic acknowledges automatically:
&ldquo;We're transitioning your question to a human member of our Privacy
Team.&rdquo;</li>
<li><strong>17 April.</strong> OpenAI replies. Two days, which is faster than
most companies manage.</li>
<li><strong>16 May.</strong> Anthropic's human reply arrives &mdash; one month
and one day after the request.</li>
</ul>

<h3>What OpenAI sent back</h3>

<blockquote>We acknowledge receipt of your request to delete any data associated
with you processed by OpenAI, but keep your OpenAI account. For security and
privacy reasons, the quickest way to delete <strong>data that is not necessary to
maintain your account or our services</strong>, while keeping your ChatGPT
account active, is to use our self-service tools outlined below.</blockquote>

<p>What followed were links: the Delete all chats button, the memory FAQ, the
privacy portal. Read the clause emphasised above. The self-service tools cover
data that is <em>not necessary to maintain the account or the service</em>. That
implies a second category &mdash; data that is necessary &mdash; and the reply
does not say what is in it, how long it is kept, or on what legal basis. Those
were the questions.</p>

<h3>What Anthropic sent back</h3>

<blockquote>When you delete a conversation it will be removed from your chat
history immediately, and deleted from our back-end storage systems within 30 days
<strong>in accordance with our retention periods</strong>. […] When you choose to
delete your account, your personal data connected to your account will also be
deleted <strong>in accordance with our retention periods</strong>.</blockquote>

<p>&ldquo;In accordance with our retention periods&rdquo; is not an answer to the
question; it is a pointer back to it. Those periods are the ones earlier in this
article: 30 days for ordinary storage, up to two years for a flagged
conversation, up to five years for de-identified training data, up to seven years
for a classification score. Deleting your account does not reset those clocks
&mdash; it hands you to them.</p>

<p>The same reply added something most people have never considered:</p>

<blockquote>if you are accessing Claude through a third party service (e.g.
Quora's Poe or Cursor), you will need to request account deletion through that
third party service provider.</blockquote>

<p>Deleting your account at the model provider does not delete the copies held by
whatever else you piped it through, and you are expected to know the list.</p>

<h3>What neither of them did</h3>

<p>Neither reply confirmed in writing what had been deleted. Neither gave a legal
basis for anything retained, which Article 17(3) requires when a controller keeps
data despite an erasure request. Neither engaged with the access request at all:
no list of flagged conversations, no classification scores, no retention schedule
by category. Both answered a legal request with a link to a settings page.</p>

<p>I am not claiming a proven breach. I did not escalate to a data protection
authority, so nothing here has been adjudicated, and both companies' published
policies do contain much of what I asked for. Both replied politely; one replied
very fast. But the request was specific and the answers were generic, and that
gap is the point: <strong>I asked two of the most sophisticated privacy teams in
the industry, in the most formal terms available to a European citizen, whether
my data was gone. Neither said yes.</strong></p>

<p>Not because they were hiding something. Because &ldquo;yes&rdquo; is not a
thing either of them is in a position to say.</p>

<p class="article-note">The replies are quoted verbatim except that the support
agents' names have been removed; they answered their tickets correctly and should
not be identifiable from this page. They are personal correspondence, reproduced
as received. Both companies' current published policies are linked at the end and
say the same things.</p>

<h2>What deletion means somewhere else</h2>

<p>For contrast, consider what &ldquo;delete&rdquo; means for a file on your own
machine. The operating system unlinks it. There is no thirty-day window, no
reviewer's copy, no training pipeline, and no third party who could be ordered to
produce it, because no third party ever had it.</p>

<p>That is not a claim about anyone's trustworthiness. It is a claim about how
many parties are involved. Five of the layers above exist because the conversation
travelled somewhere. A conversation that never leaves the device has one layer.</p>

<h2>Where this leaves you</h2>

<p>We are not writing this from a position of purity. We use cloud assistants
every day, by choice, and we build products on top of them. Claude and ChatGPT
are better than anything that fits on a phone, and convenience wins more often
than we would like to admit.</p>

<p>So this is not an argument for quitting them. It is an argument for knowing
which rules you are playing by, and then choosing deliberately for the
conversations where it matters &mdash; the ones you would mind someone reading,
which for most people is a small fraction of the total.</p>

<p>For that fraction, the only arrangement in which none of the five layers
exists is a model that runs on hardware you own. It is the problem we work on:
<a href="%s">Pinku</a> runs language models on an iPhone or a Mac with no account
and no network connection, and <a href="%s">Keeper</a> keeps photos and files
encrypted on the device. The rest of the time we are in the same boat as you,
typing into someone else's computer because it is easier.</p>

<p class="article-note">Every figure in this article is quoted from a provider's
own published policy or a court filing, all linked below. Check them rather than
taking our word for it &mdash; and if one is out of date,
<a href="mailto:sagalabs@proton.me">tell us</a> and we will correct the page.</p>
""" % (APP_STORE, KEEPER)

A4_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li><a href="https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data" rel="nofollow noopener" target="_blank">How long do you store my data?</a> &mdash; Anthropic Privacy Center, updated 1 July 2026. The 30-day, 2-year, 5-year and 7-year windows.</li>
<li><a href="https://gdpr-info.eu/art-15-gdpr/" rel="nofollow noopener" target="_blank">Article 15</a>, <a href="https://gdpr-info.eu/art-17-gdpr/" rel="nofollow noopener" target="_blank">Article 17</a> and <a href="https://gdpr-info.eu/art-12-gdpr/" rel="nofollow noopener" target="_blank">Article 12(3)</a> GDPR &mdash; right of access, right to erasure, and the one-month deadline to respond.</li>
<li><a href="https://www.anthropic.com/legal/aup" rel="nofollow noopener" target="_blank">Usage Policy</a> &mdash; Anthropic. The High-Risk Use Case Requirements naming legal, healthcare, insurance and finance.</li>
<li><a href="https://support.google.com/gemini/answer/13594961" rel="nofollow noopener" target="_blank">Gemini Apps Privacy Notice</a> &mdash; Google. Human review and the three-year retention of reviewed chats.</li>
<li><a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt" rel="nofollow noopener" target="_blank">Chat and file retention policies in ChatGPT</a> &mdash; OpenAI Help Center.</li>
<li><a href="https://openai.com/index/response-to-nyt-data-demands/" rel="nofollow noopener" target="_blank">How we're responding to The New York Times' data demands</a> &mdash; OpenAI, on the May 2025 preservation order.</li>
<li><a href="https://www.engadget.com/ai/openai-no-longer-has-to-preserve-all-of-its-chatgpt-data-with-some-exceptions-192422093.html" rel="nofollow noopener" target="_blank">OpenAI no longer has to preserve all of its ChatGPT data, with some exceptions</a> &mdash; Engadget, October 2025, on the order being terminated.</li>
<li><a href="https://www.dataprivacyandsecurityinsider.com/2026/01/when-chats-become-evidence-court-affirms-order-requiring-openai-to-produce-20-million-de-identified-chatgpt-logs/" rel="nofollow noopener" target="_blank">Court affirms order requiring OpenAI to produce 20 million de-identified ChatGPT logs</a> &mdash; January 2026.</li>
</ul>
<p>Checked on 5 September 2026.</p>
"""


A4_ES_BODY = """
<p>Todo asistente de IA tiene un bot&oacute;n de borrar. Pulsarlo hace desaparecer
una fila de una lista, al instante y de forma satisfactoria. Si hace algo
m&aacute;s es otra pregunta, con una respuesta distinta para cada capa del sistema
por la que pas&oacute; la conversaci&oacute;n.</p>

<p>Nada de lo que sigue es un esc&aacute;ndalo. Casi todo es la consecuencia
normal de operar software a escala, y parte es obligaci&oacute;n legal. Pero la
distancia entre lo que parece que hace el bot&oacute;n y lo que hace es lo bastante
grande como para merecer que se escriba.</p>

<h2>Capa 1 &mdash; tu vista, y luego el almacenamiento</h2>

<p>Que la fila desaparezca es inmediato y local. Detr&aacute;s, OpenAI y Anthropic
publican la misma ventana: una conversaci&oacute;n borrada sale de los sistemas
<strong>en 30 d&iacute;as</strong>. Anthropic dice &laquo;eliminada de nuestros
sistemas de almacenamiento en 30 d&iacute;as&raquo;; OpenAI, que los chats borrados
se eliminan definitivamente en 30 d&iacute;as, salvo anonimizaci&oacute;n u
obligaciones legales.</p>

<p>Treinta d&iacute;as es una cifra razonable. Las copias de seguridad tienen que
rotar, y un sistema que borrase de cada r&eacute;plica de forma s&iacute;ncrona
ser&iacute;a un sistema que no se puede restaurar tras un incidente. Pero implica
que &laquo;borrado&raquo; significa &laquo;programado para borrarse&raquo; durante
un mes.</p>

<h2>Capa 2 &mdash; los pesos, que no se editan</h2>

<p>Si tu conversaci&oacute;n se us&oacute; en un entrenamiento que ya
termin&oacute;, borrarla no quita su influencia del modelo resultante. No existe
t&eacute;cnica conocida para meter la mano en una red entrenada y extraer una
conversaci&oacute;n.</p>

<p>Anthropic lo dice claro en vez de esconderlo: desactivar el ajuste significa
que tus datos no se usar&aacute;n en entrenamientos <em>futuros</em>, pero
&laquo;tus datos segu&iacute;an incluidos en los entrenamientos ya en curso, o en
los modelos ya entrenados&raquo;.</p>

<p>Esta es la capa que la gente subestima. Borrar es una operaci&oacute;n de
almacenamiento. Entrenar no es almacenamiento.</p>

<h2>Capa 3 &mdash; la copia que ley&oacute; una persona</h2>

<p>Los tres grandes proveedores usan revisores humanos sobre una parte de las
conversaciones. El aviso de Gemini Apps es el &uacute;nico que deletrea qu&eacute;
significa eso para el borrado, y la frase merece leerse dos veces:</p>

<blockquote>Los chats revisados por revisores humanos (y datos asociados como tu
idioma, tipo de dispositivo, informaci&oacute;n de ubicaci&oacute;n o comentarios)
no se eliminan cuando borras tu actividad. En su lugar se conservan hasta tres
a&ntilde;os.</blockquote>

<p>Tu borrado no llega a esa copia. Tiene su propio reloj de tres a&ntilde;os, que
corre al margen de cualquier ajuste de tu cuenta, y no hay ning&uacute;n control
para &eacute;l.</p>

<h2>Capa 4 &mdash; la marca de seguridad</h2>

<p>Si un sistema autom&aacute;tico decide que una conversaci&oacute;n puede
incumplir la pol&iacute;tica de uso, se aplican otras reglas. Anthropic publica las
cifras: entradas y salidas <strong>hasta dos a&ntilde;os</strong>, y las
puntuaciones de clasificaci&oacute;n <strong>hasta siete a&ntilde;os</strong>.</p>

<p>F&iacute;jate en la asimetr&iacute;a. La puntuaci&oacute;n &mdash; el juicio de
una m&aacute;quina sobre ti &mdash; sobrevive cinco a&ntilde;os m&aacute;s que la
conversaci&oacute;n que la produjo.</p>

<p>Qu&eacute; conversaciones se marcan no se publica. Lo que s&iacute; se publica
es la pol&iacute;tica de la que depende esa marca, y nombra cuatro dominios como
&laquo;casos de uso de alto riesgo&raquo;:</p>

<blockquote>Legal: casos relacionados con interpretaci&oacute;n legal,
asesoramiento legal o decisiones con implicaciones legales. Sanidad: casos
relacionados con decisiones sanitarias, diagn&oacute;stico m&eacute;dico,
atenci&oacute;n al paciente, terapia, salud mental u otra orientaci&oacute;n
m&eacute;dica. Seguros: […] Finanzas: casos relacionados con decisiones
financieras, incluido el asesoramiento de inversi&oacute;n y la
aprobaci&oacute;n de pr&eacute;stamos […]</blockquote>

<p>Cuidado con lo que eso dice y lo que no. Esos requisitos van dirigidos a quien
construye productos sobre Claude: tiene que poner a un profesional cualificado a
revisar y avisar de que hay IA de por medio. No dicen que preguntar por tu propia
salud marque tu chat, y no estamos afirmando que lo hagan.</p>

<p>La posici&oacute;n exacta es esta. El reloj de siete a&ntilde;os arranca cuando
un sistema autom&aacute;tico decide que una conversaci&oacute;n puede incumplir la
Usage Policy. La Usage Policy es el documento que nombra esos cuatro dominios. Si
las conversaciones de esos dominios tienen m&aacute;s probabilidad de marcarse no
se dice, y no existe ning&uacute;n mecanismo para que t&uacute; averig&uuml;es si
alguna conversaci&oacute;n tuya lo est&aacute;.</p>

<p>As&iacute; que las categor&iacute;as en las que m&aacute;s te gustar&iacute;a
saberlo &mdash; tu salud, tu dinero, tu exposici&oacute;n legal &mdash; son justo
aquellas en las que no puedes. No es una acusaci&oacute;n. Es la forma honesta de
la informaci&oacute;n que tienes disponible, y es la raz&oacute;n por la que
algunas conversaciones merecen no salir a una red.</p>

<h2>Capa 5 &mdash; el juzgado</h2>

<p>La demostraci&oacute;n m&aacute;s clara de que el bot&oacute;n de borrar no
tiene la &uacute;ltima palabra sali&oacute; del pleito de derechos de autor contra
OpenAI del New York Times y otros. Conviene dar la cronolog&iacute;a exacta, porque
se cuenta mal en las dos direcciones.</p>

<ul>
<li><strong>13 de mayo de 2025.</strong> La jueza Ona T. Wang ordena a OpenAI
conservar y segregar todos los registros de salida que de otro modo se
borrar&iacute;an &mdash; incluidas conversaciones que los usuarios hab&iacute;an
borrado.</li>
<li><strong>Junio de 2025.</strong> El juez Sidney Stein rechaza la
objeci&oacute;n de OpenAI. La orden se mantiene.</li>
<li><strong>Julio de 2025.</strong> Los demandantes piden una muestra de 120
millones de registros. OpenAI contrapropone 20 millones anonimizados.</li>
<li><strong>Octubre de 2025.</strong> La jueza Wang levanta la obligaci&oacute;n de
conservaci&oacute;n hacia delante. Lo ya conservado sigue conservado, y hay que
seguir reteniendo los datos de las cuentas se&ntilde;aladas por los
demandantes.</li>
<li><strong>5 de enero de 2026.</strong> El tribunal del Distrito Sur de Nueva York
confirma las &oacute;rdenes que obligan a entregar la muestra de 20 millones. La
primera tanda llega al equipo legal de los demandantes ese mismo mes.</li>
</ul>

<p>As&iacute; que la orden general de conservaci&oacute;n <em>se acab&oacute;</em>.
Quien siga diciendo que &laquo;OpenAI tiene que guardar tus chats borrados para
siempre&raquo; lleva un a&ntilde;o de retraso.</p>

<p>Pero la parte que de verdad importa no se ha acabado. Durante unos cinco meses,
chats que los usuarios hab&iacute;an borrado se conservaron porque lo dijo un
tribunal. Una muestra de veinte millones, anonimizada, se ha entregado desde
entonces a los abogados de la parte contraria en un pleito de copyright. A nadie de
esa muestra se le pregunt&oacute;, y nadie de esa muestra puede saber si est&aacute;
dentro.</p>

<p>OpenAI pele&oacute; la orden y dice que los datos conservados est&aacute;n tras
un equipo legal y de seguridad reducido y auditado. No hay motivo para dudarlo. El
argumento es estructural, no moral: <strong>una pol&iacute;tica de
retenci&oacute;n es una promesa que hace una empresa, y un tribunal puede
suspenderla para todo el mundo a la vez.</strong></p>

<h2>Les mand&eacute; una solicitud de borrado del RGPD</h2>

<p>Desde mis propias cuentas personales &mdash; el nivel de consumo del que va
este art&iacute;culo, no un plan de empresa con otros valores por defecto &mdash;
mand&eacute; a OpenAI y a Anthropic una solicitud formal al amparo del RGPD, y
guard&eacute; lo que volvi&oacute;.</p>

<p>No un ticket de soporte. Una solicitud por el art&iacute;culo 15, derecho de
acceso, y el art&iacute;culo 17, derecho de supresi&oacute;n, pidiendo justo lo
que este art&iacute;culo lleva describiendo:</p>

<blockquote>Cualquier conversaci&oacute;n marcada por vuestros clasificadores de
trust and safety, junto con los motivos concretos del marcado. Cualquier dato
derivado de mis conversaciones (puntuaciones de clasificaci&oacute;n, metadatos,
registros). Cualquier dato anonimizado que se originara en mi cuenta, incluido el
usado para entrenar modelos. Informaci&oacute;n sobre cu&aacute;nto tiempo se
conservar&aacute; cada categor&iacute;a de mis datos y la base jur&iacute;dica de
esa conservaci&oacute;n. […] Confirmad por escrito qu&eacute; datos se han
suprimido y, si se conserva alguno, indicad la base jur&iacute;dica concreta de
cada categor&iacute;a conservada, tal como exige el art&iacute;culo
17(3).</blockquote>

<p>Esa &uacute;ltima frase es la prueba. No es un favor que se pide: el
art&iacute;culo 12(3) da al responsable un mes para contestar.</p>

<h3>La cronolog&iacute;a</h3>

<ul>
<li><strong>15 de abril de 2026.</strong> Solicitud enviada a las dos empresas.</li>
<li><strong>15 de abril.</strong> Anthropic acusa recibo autom&aacute;ticamente:
&laquo;Estamos derivando tu consulta a una persona de nuestro equipo de
privacidad&raquo;.</li>
<li><strong>17 de abril.</strong> Contesta OpenAI. Dos d&iacute;as, m&aacute;s
r&aacute;pido de lo que consigue la mayor&iacute;a.</li>
<li><strong>16 de mayo.</strong> Llega la respuesta humana de Anthropic: un mes y
un d&iacute;a despu&eacute;s de la solicitud.</li>
</ul>

<h3>Lo que contest&oacute; OpenAI</h3>

<blockquote>Acusamos recibo de tu solicitud de borrar cualquier dato asociado a ti
procesado por OpenAI, manteniendo tu cuenta. Por motivos de seguridad y
privacidad, la forma m&aacute;s r&aacute;pida de borrar <strong>los datos que no
son necesarios para mantener tu cuenta o nuestros servicios</strong>, conservando
la cuenta de ChatGPT activa, es usar nuestras herramientas de
autoservicio.</blockquote>

<p>Lo que segu&iacute;a eran enlaces: el bot&oacute;n de borrar todos los chats,
las preguntas frecuentes de la memoria, el portal de privacidad. Lee la
cl&aacute;usula destacada. Las herramientas de autoservicio cubren los datos que
<em>no son necesarios para mantener la cuenta o el servicio</em>. Eso implica una
segunda categor&iacute;a &mdash; los que s&iacute; lo son &mdash; y la respuesta
no dice qu&eacute; hay dentro, cu&aacute;nto se guarda ni con qu&eacute; base
jur&iacute;dica. Esas eran las preguntas.</p>

<h3>Lo que contest&oacute; Anthropic</h3>

<blockquote>Cuando borras una conversaci&oacute;n se elimina de tu historial de
inmediato, y de nuestros sistemas de almacenamiento en 30 d&iacute;as <strong>de
acuerdo con nuestros plazos de retenci&oacute;n</strong>. […] Cuando eliges borrar
tu cuenta, tus datos personales vinculados a ella tambi&eacute;n se borran
<strong>de acuerdo con nuestros plazos de retenci&oacute;n</strong>.</blockquote>

<p>&laquo;De acuerdo con nuestros plazos de retenci&oacute;n&raquo; no es una
respuesta a la pregunta: es un puntero de vuelta a ella. Esos plazos son los de
antes en este art&iacute;culo: 30 d&iacute;as de almacenamiento normal, hasta dos
a&ntilde;os si la conversaci&oacute;n se marc&oacute;, hasta cinco a&ntilde;os de
datos anonimizados de entrenamiento, hasta siete a&ntilde;os de puntuaci&oacute;n
de clasificaci&oacute;n. Borrar la cuenta no reinicia esos relojes: te entrega a
ellos.</p>

<p>La misma respuesta a&ntilde;ad&iacute;a algo en lo que casi nadie ha
pensado:</p>

<blockquote>si accedes a Claude a trav&eacute;s de un servicio de terceros (por
ejemplo Poe de Quora o Cursor), tendr&aacute;s que solicitar el borrado de la
cuenta a ese proveedor.</blockquote>

<p>Borrar tu cuenta en el proveedor del modelo no borra las copias que tenga
aquello por lo que lo canalizaste, y se da por hecho que t&uacute; te sabes la
lista.</p>

<h3>Lo que no hizo ninguna de las dos</h3>

<p>Ninguna respuesta confirm&oacute; por escrito qu&eacute; se hab&iacute;a
borrado. Ninguna dio una base jur&iacute;dica para lo conservado, que es lo que
exige el art&iacute;culo 17(3) cuando un responsable retiene datos pese a una
solicitud de supresi&oacute;n. Ninguna entr&oacute; en el derecho de acceso: ni
lista de conversaciones marcadas, ni puntuaciones de clasificaci&oacute;n, ni
calendario de conservaci&oacute;n por categor&iacute;a. Las dos respondieron a una
solicitud legal con un enlace a una pantalla de ajustes.</p>

<p>No estoy afirmando que haya un incumplimiento probado. No lo llev&eacute; a
una autoridad de protecci&oacute;n de datos, as&iacute; que aqu&iacute; no hay
nada dirimido, y las pol&iacute;ticas publicadas de las dos empresas s&iacute;
contienen buena parte de lo que ped&iacute;a. Las dos contestaron con
educaci&oacute;n; una, muy r&aacute;pido. Pero la solicitud era concreta y las
respuestas fueron gen&eacute;ricas, y esa distancia es el asunto:
<strong>pregunt&eacute; a dos de los equipos de privacidad m&aacute;s competentes
del sector, en los t&eacute;rminos m&aacute;s formales de que dispone una
ciudadana europea, si mis datos estaban borrados. Ninguno dijo que
s&iacute;.</strong></p>

<p>No porque escondieran nada. Porque &laquo;s&iacute;&raquo; no es algo que
ninguno de los dos est&eacute; en posici&oacute;n de decir.</p>

<p class="article-note">Las respuestas est&aacute;n citadas literalmente salvo que
se han quitado los nombres de los agentes de soporte: atendieron sus tickets
correctamente y no deber&iacute;an ser identificables desde esta p&aacute;gina. Son
correspondencia personal y se reproducen tal como se recibieron. Las
pol&iacute;ticas publicadas hoy por las dos empresas est&aacute;n enlazadas al
final y dicen lo mismo. Los textos originales est&aacute;n en ingl&eacute;s.</p>

<h2>Qu&eacute; significa borrar en otro sitio</h2>

<p>Como contraste, piensa en qu&eacute; significa &laquo;borrar&raquo; para un
archivo de tu propia m&aacute;quina. El sistema operativo lo desenlaza. No hay
ventana de treinta d&iacute;as, ni copia de un revisor, ni tuber&iacute;a de
entrenamiento, ni un tercero al que se le pueda ordenar que lo entregue, porque
ning&uacute;n tercero lo tuvo nunca.</p>

<p>Esto no es una afirmaci&oacute;n sobre la honradez de nadie. Es una
afirmaci&oacute;n sobre cu&aacute;ntas partes intervienen. Cinco de las capas de
arriba existen porque la conversaci&oacute;n viaj&oacute; a alg&uacute;n sitio. Una
conversaci&oacute;n que nunca sale del dispositivo tiene una capa.</p>

<h2>D&oacute;nde te deja esto</h2>

<p>No escribimos esto desde ninguna superioridad moral. Usamos asistentes en la
nube todos los d&iacute;as, por gusto, y adem&aacute;s hacemos productos que se
apoyan en ellos. Claude y ChatGPT son mejores que cualquier cosa que quepa en un
m&oacute;vil, y la comodidad gana m&aacute;s veces de las que nos
gustar&iacute;a reconocer.</p>

<p>As&iacute; que esto no es un argumento para dejarlos. Es un argumento para
saber a qu&eacute; reglas est&aacute;s jugando y elegir a conciencia en las
conversaciones donde importa: aquellas que te fastidiar&iacute;a que alguien
leyera, que para casi todo el mundo son una parte peque&ntilde;a del total.</p>

<p>Para esa parte, la &uacute;nica disposici&oacute;n en la que no existe ninguna
de las cinco capas es un modelo que corre en hardware tuyo. Es el problema en el
que trabajamos: <a href="%s">Pinku</a> ejecuta modelos de lenguaje en un iPhone o
un Mac sin cuenta y sin conexi&oacute;n, y <a href="%s">Keeper</a> mantiene fotos
y archivos cifrados en el dispositivo. El resto del tiempo estamos en el mismo
barco que t&uacute;, escribiendo en el ordenador de otro porque es m&aacute;s
c&oacute;modo.</p>

<p class="article-note">Toda cifra de este art&iacute;culo est&aacute; citada de la
pol&iacute;tica publicada por el proveedor o de una resoluci&oacute;n judicial,
enlazadas abajo. Compru&eacute;balas en vez de creernos &mdash; y si alguna
est&aacute; desactualizada, <a href="mailto:sagalabs@proton.me">av&iacute;sanos</a>
y corregimos la p&aacute;gina.</p>
""" % (APP_STORE, KEEPER)

A4_ES_SOURCES = A4_EN_SOURCES.replace("<h2>Sources</h2>", "<h2>Fuentes</h2>").replace(
    "<p>Checked on 5 September 2026.</p>", "<p>Comprobado el 5 de septiembre de 2026.</p>")


# --------------------------------------------------------------------------
# 5 — Apps para ocultar fotos en iPhone, comparadas
# --------------------------------------------------------------------------
#
# Photo Vault es nuestra: el aviso va arriba del todo, no al final.
# Valoraciones sacadas de la API publica de iTunes (country=us) el 4 oct 2026.
# Las funciones de la competencia salen de su propia descripcion en el App Store;
# no afirmar nada que su ficha no diga. Las de Photo Vault estan comprobadas en
# el codigo (repo onlyfansgallery): no hay cifrado propio tipo AES, asi que no
# se dice. Si cambian las cifras, cambiar la fecha.

VAULT_DATE_ISO = "2026-10-04"
VAULT_DATE_EN = "4 October 2026"
VAULT_DATE_ES = "4 de octubre de 2026"

PV = "https://apps.apple.com/app/apple-store/id1532670722?pt=118348020&amp;ct=sagalab-blog&amp;mt=8"
PICSAFE = "https://apps.apple.com/us/app/id417571834"
KEEPSAFE = "https://apps.apple.com/us/app/id510873505"
ARCA = "https://apps.apple.com/us/app/id6779157571"
HIDDEN = "https://support.apple.com/en-us/104987"

A5_EN_BODY = """
<p><strong>Disclosure: we make Photo Vault, one of the apps below.</strong> We
have tried to describe the others the way their own App Store pages describe
them, and to say plainly where they beat us.</p>

<h2>First: you may not need an app</h2>

<p>The Photos app already has a Hidden album. Since iOS 16 it is
<a href="%(hidden)s" target="_blank" rel="noopener">locked by default and opens
with Face ID or Touch ID</a>, and you can turn off <em>Show Hidden Album</em> so
it does not appear at all. It is free and it is built in.</p>

<p>Its limits: it lives inside your main photo library, so with iCloud Photos
switched on the hidden photos sync to your other devices and to iCloud, as
Apple's own page says. There is one lock for everything and the Photos app
itself stays in plain sight. If that is fine, stop here.</p>

<h2>The four vault apps most often recommended</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Cloud backup</th><th>Backup file you keep</th><th>Account</th><th>Decoy PIN</th><th>Disguised icon</th><th>Rating (US)</th></tr></thead>
<tbody>
<tr><td><a href="%(picsafe)s" target="_blank" rel="noopener">Private Photo Vault – Pic Safe</a></td><td>Yes</td><td>&mdash;</td><td>&mdash;</td><td>Yes</td><td>&mdash;</td><td>4.8 &middot; 1,016,216</td></tr>
<tr><td><a href="%(keepsafe)s" target="_blank" rel="noopener">Keepsafe</a></td><td>Yes, up to 10,000 items</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>4.7 &middot; 383,718</td></tr>
<tr><td><a href="%(arca)s" target="_blank" rel="noopener">Arca</a></td><td>No</td><td>Yes, encrypted</td><td>No</td><td>Yes</td><td>Yes</td><td>4.8 &middot; 28</td></tr>
<tr><td><a href="%(pv)s">Photo Vault</a> (ours)</td><td>No</td><td>Yes, encrypted</td><td>No</td><td>No</td><td>Yes</td><td>4.0 &middot; 5</td></tr>
</tbody>
</table></div>

<p class="article-note">A dash means the app's App Store description does not
mention it, not that it is certainly missing. Ratings checked on %(date)s.</p>

<h2>Pic Safe and Keepsafe: if you want a backup</h2>

<p>These are the two big ones, with hundreds of thousands of ratings between
them. Both offer a private cloud, so if you lose the phone the vault survives.
Pic Safe also lists a decoy password and break-in alerts. The price of the
backup is that your private photos are stored on someone's servers.</p>

<h2>Arca and Photo Vault: if you want nothing to leave the phone</h2>

<p>Both have no account, no server and no cloud. Arca's page states that every
photo, video and thumbnail is encrypted individually with AES-256, with keys
protected by the Secure Enclave, and it has a decoy vault that opens with a
second PIN. Photo Vault relies on iOS Data Protection instead: the iPhone
encrypts the files and they can't be read while it's locked, but there is no
separate per-file encryption and no decoy vault today.</p>

<p>What Photo Vault adds: a separate password for each album on top of the app
lock, a face-down lock that jumps to Safari, Messages or Calendar when you turn
the phone over, a built-in camera so new photos never touch the camera roll,
and a vault excluded from iCloud backups. The icon can pass as Calculator, Notes
or Weather.</p>

<p>Neither backs up on its own, because neither syncs to a cloud. Both let you
export an encrypted backup file and keep it where you want, in Files, on a
computer or in your own iCloud Drive. Without one, a lost phone means lost
photos.</p>

<h2>How to choose</h2>

<ul>
<li><strong>A few photos, and you trust iCloud:</strong> the built-in Hidden album.</li>
<li><strong>You need a backup:</strong> Pic Safe or Keepsafe.</li>
<li><strong>Nothing on any server, and a decoy PIN matters:</strong> Arca.</li>
<li><strong>Nothing on any server, separate album passwords, a face-down lock:</strong> <a href="%(pv)s">Photo Vault</a>.</li>
</ul>
""" % dict(hidden=HIDDEN, picsafe=PICSAFE, keepsafe=KEEPSAFE, arca=ARCA, pv=PV, date=VAULT_DATE_EN)

A5_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>Apple Support, <a href="%(hidden)s" target="_blank" rel="noopener">Hide photos with the Hidden album</a>.</li>
<li>App Store pages: <a href="%(picsafe)s" target="_blank" rel="noopener">Pic Safe</a>, <a href="%(keepsafe)s" target="_blank" rel="noopener">Keepsafe</a>, <a href="%(arca)s" target="_blank" rel="noopener">Arca</a>, <a href="%(pv)s">Photo Vault</a>. Ratings from Apple's public lookup API, US store, %(date)s.</li>
</ul>
""" % dict(hidden=HIDDEN, picsafe=PICSAFE, keepsafe=KEEPSAFE, arca=ARCA, pv=PV, date=VAULT_DATE_EN)

A5_ES_BODY = """
<p><strong>Aviso: Photo Vault, una de las apps de esta lista, es nuestra.</strong>
Hemos descrito las dem&aacute;s como las describe su propia ficha del App Store,
y decimos claramente en qu&eacute; nos ganan.</p>

<h2>Primero: puede que no necesites una app</h2>

<p>La app Fotos ya tiene un &aacute;lbum Oculto. Desde iOS 16
<a href="%(hidden)s" target="_blank" rel="noopener">viene bloqueado y se abre con
Face ID o Touch ID</a>, y puedes desactivar <em>Mostrar &aacute;lbum Oculto</em>
para que ni siquiera aparezca. Es gratis y viene de serie.</p>

<p>Sus l&iacute;mites: vive dentro de tu fototeca, as&iacute; que con Fotos en
iCloud activado las fotos ocultas se sincronizan con tus otros dispositivos y con
iCloud, como dice la propia p&aacute;gina de Apple. Hay un solo bloqueo para todo
y la app Fotos sigue a la vista. Si eso te vale, no sigas leyendo.</p>

<h2>Las cuatro apps que m&aacute;s se recomiendan</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Copia en la nube</th><th>Copia en archivo propio</th><th>Cuenta</th><th>PIN se&ntilde;uelo</th><th>Icono disfrazado</th><th>Valoraci&oacute;n (EE. UU.)</th></tr></thead>
<tbody>
<tr><td><a href="%(picsafe)s" target="_blank" rel="noopener">Private Photo Vault – Pic Safe</a></td><td>S&iacute;</td><td>&mdash;</td><td>&mdash;</td><td>S&iacute;</td><td>&mdash;</td><td>4,8 &middot; 1.016.216</td></tr>
<tr><td><a href="%(keepsafe)s" target="_blank" rel="noopener">Keepsafe</a></td><td>S&iacute;, hasta 10.000 elementos</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>4,7 &middot; 383.718</td></tr>
<tr><td><a href="%(arca)s" target="_blank" rel="noopener">Arca</a></td><td>No</td><td>S&iacute;, cifrada</td><td>No</td><td>S&iacute;</td><td>S&iacute;</td><td>4,8 &middot; 28</td></tr>
<tr><td><a href="%(pv)s">Photo Vault</a> (nuestra)</td><td>No</td><td>S&iacute;, cifrada</td><td>No</td><td>No</td><td>S&iacute;</td><td>4,0 &middot; 5</td></tr>
</tbody>
</table></div>

<p class="article-note">Un guion significa que la descripci&oacute;n de la app en
el App Store no lo menciona, no que seguro no lo tenga. Valoraciones comprobadas
el %(date)s.</p>

<h2>Pic Safe y Keepsafe: si quieres copia de seguridad</h2>

<p>Son las dos grandes, con cientos de miles de valoraciones. Las dos ofrecen una
nube privada, as&iacute; que si pierdes el m&oacute;vil la b&oacute;veda sobrevive.
Pic Safe a&ntilde;ade contrase&ntilde;a se&ntilde;uelo y alertas de intento de
acceso. El precio de la copia es que tus fotos privadas quedan en los servidores
de otra empresa.</p>

<h2>Arca y Photo Vault: si no quieres que nada salga del m&oacute;vil</h2>

<p>Ninguna de las dos tiene cuenta, servidor ni nube. La ficha de Arca dice que
cada foto, v&iacute;deo y miniatura se cifra por separado con AES-256, con las
claves protegidas por el Secure Enclave, y tiene una b&oacute;veda se&ntilde;uelo
que se abre con un segundo PIN. Photo Vault se apoya en la protecci&oacute;n de
datos de iOS: el iPhone cifra los archivos y no se pueden leer mientras est&aacute;
bloqueado, pero no hay un cifrado propio por archivo ni b&oacute;veda
se&ntilde;uelo, de momento.</p>

<p>Lo que a&ntilde;ade Photo Vault: una contrase&ntilde;a distinta para cada
&aacute;lbum, adem&aacute;s del bloqueo de la app; bloqueo boca abajo, que salta a
Safari, Mensajes o Calendario al girar el m&oacute;vil; c&aacute;mara propia para
que las fotos nuevas no pasen por el carrete; y la b&oacute;veda fuera de las
copias de iCloud. El icono puede pasar por Calculadora, Notas o Tiempo.</p>

<p>Ninguna hace copia sola, porque ninguna sincroniza con una nube. Las dos
permiten exportar una copia cifrada en un archivo y guardarla donde quieras: en
Archivos, en el ordenador o en tu propio iCloud Drive. Sin ella, perder el
m&oacute;vil es perder las fotos.</p>

<h2>C&oacute;mo elegir</h2>

<ul>
<li><strong>Pocas fotos y te f&iacute;as de iCloud:</strong> el &aacute;lbum Oculto de serie.</li>
<li><strong>Necesitas copia de seguridad:</strong> Pic Safe o Keepsafe.</li>
<li><strong>Nada en ning&uacute;n servidor, y te importa el PIN se&ntilde;uelo:</strong> Arca.</li>
<li><strong>Nada en ning&uacute;n servidor, contrase&ntilde;a por &aacute;lbum y bloqueo boca abajo:</strong> <a href="%(pv)s">Photo Vault</a>.</li>
</ul>
""" % dict(hidden=HIDDEN, picsafe=PICSAFE, keepsafe=KEEPSAFE, arca=ARCA, pv=PV, date=VAULT_DATE_ES)

A5_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Soporte de Apple, <a href="%(hidden)s" target="_blank" rel="noopener">Ocultar fotos con el &aacute;lbum Oculto</a>.</li>
<li>Fichas del App Store: <a href="%(picsafe)s" target="_blank" rel="noopener">Pic Safe</a>, <a href="%(keepsafe)s" target="_blank" rel="noopener">Keepsafe</a>, <a href="%(arca)s" target="_blank" rel="noopener">Arca</a>, <a href="%(pv)s">Photo Vault</a>. Valoraciones de la API p&uacute;blica de Apple, tienda de EE. UU., %(date)s.</li>
</ul>
""" % dict(hidden=HIDDEN, picsafe=PICSAFE, keepsafe=KEEPSAFE, arca=ARCA, pv=PV, date=VAULT_DATE_ES)


# --------------------------------------------------------------------------
# 6 — Apps de IA sin conexion para iPhone y Mac
# --------------------------------------------------------------------------
#
# Pinku es nuestra: el aviso va arriba del todo. Precios, valoraciones y
# disponibilidad por tienda sacados el 7 oct 2026 de la ficha del App Store
# (EE. UU.) y de la API publica de lookup de iTunes (country=us/ru/cn/hk).
# Privacy AI = "Privacy AI: Agent & Chatbot" (AcmeUp, id6738392421); su ficha
# de EE. UU. lista suscripcion semanal/mensual/anual, no una compra PRO unica.
# Lo de Pinku esta comprobado en su repo (docs/PRO.md, docs/MODELOS.md,
# docs/ESTADO.md 3 oct 2026). Sin rayas en el texto.

OFF_DATE_ISO = "2026-10-07"
OFF_DATE_EN = "7 October 2026"
OFF_DATE_ES = "7 de octubre de 2026"

PINKU_BLOG = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-blog&amp;mt=8"
LOCALLY = "https://apps.apple.com/us/app/id6741426692"
ENCLAVE = "https://apps.apple.com/us/app/id6476614556"
POCKETPAL = "https://apps.apple.com/us/app/id6502579498"
PRIVATELLM = "https://apps.apple.com/us/app/id6448106860"
PRIVACYAI = "https://apps.apple.com/us/app/id6738392421"
ONDEVICE = "https://apps.apple.com/us/app/id6497060890"
POCKETPAL_GH = "https://github.com/a-ghorbani/pocketpal-ai"
OPENAI_COUNTRIES = "https://help.openai.com/en/articles/7947663-chatgpt-supported-countries"

_OFF = dict(pinku=PINKU_BLOG, locally=LOCALLY, enclave=ENCLAVE, pocketpal=POCKETPAL,
            privatellm=PRIVATELLM, privacyai=PRIVACYAI, ondevice=ONDEVICE,
            gh=POCKETPAL_GH, oai=OPENAI_COUNTRIES)

A6_EN_BODY = """
<p><strong>Disclosure: we make Pinku, one of the apps below.</strong> We have
described the others the way their own App Store pages describe them, and we say
plainly where they beat us. Prices are from the US App Store on %(date)s.</p>

<p>Every app here does the same basic thing: it downloads an open language model
to your iPhone or Mac and runs it there. Once the model is on the device, your
questions are answered without a network connection and without an account. What
differs is which models you can run, what you pay, and how much else the app
does.</p>

<h2>The six apps at a glance</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Price (US)</th><th>Mac App Store</th><th>Models</th><th>Rating (US)</th></tr></thead>
<tbody>
<tr><td><a href="%(locally)s" target="_blank" rel="noopener">Locally AI by LM Studio</a></td><td>Free</td><td>Yes</td><td>Llama, Gemma, Qwen, DeepSeek and more, on Apple MLX</td><td>4.7 &middot; 1,742</td></tr>
<tr><td><a href="%(enclave)s" target="_blank" rel="noopener">Enclave</a></td><td>Free; Pro $9.99</td><td>Not listed</td><td>Hundreds of open models; Pro adds cloud models</td><td>4.7 &middot; 1,087</td></tr>
<tr><td><a href="%(pocketpal)s" target="_blank" rel="noopener">PocketPal AI</a></td><td>Free, open source</td><td>Not listed</td><td>Any GGUF model from Hugging Face</td><td>4.1 &middot; 160</td></tr>
<tr><td><a href="%(privatellm)s" target="_blank" rel="noopener">Private LLM</a></td><td>$4.99 upfront</td><td>Yes</td><td>Llama, Gemma, Qwen, Phi, Mistral and more, up to 14B</td><td>4.2 &middot; 734</td></tr>
<tr><td><a href="%(privacyai)s" target="_blank" rel="noopener">Privacy AI</a></td><td>Free; subscription for cloud features</td><td>Not listed</td><td>GGUF and MLX models, Apple's models, optional cloud providers</td><td>4.8 &middot; 20</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a> (ours)</td><td>Free; Pinku Pro $9.99 one-time</td><td>Yes</td><td>12 curated models on Apple MLX, 0.34 to 4.7 GB</td><td>4.7 &middot; 12</td></tr>
</tbody>
</table></div>

<p class="article-note">&ldquo;Not listed&rdquo; means we found no Mac App Store
listing; iPhone and iPad apps can still run on many Apple silicon Macs. Ratings
are from Apple's public lookup API on %(date)s.</p>

<h2>Locally AI by LM Studio: the safe free pick</h2>

<p>Made by the team behind LM Studio, the desktop app many people already use to
run models on a computer. It is free, needs no login, runs models with Apple's MLX
framework, and its page says it can analyse images as well as text. It has the
most ratings of any app here, and it is on iPhone, iPad and Mac. If you want one
free app and do not want to think about it, start here.</p>

<h2>Enclave: local first, cloud if you want it</h2>

<p>Enclave lets you try hundreds of open models, chat with PDFs and other
documents, talk to it by voice using Apple's on-device speech, build custom
assistants and call it from Siri and Shortcuts. Local use is free. Pro is listed
at $9.99, and the app's description now presents Pro as a subscription that adds
cloud models from Anthropic, OpenAI, Google and xAI. Good if you want one app for
both private local chats and the occasional cloud model.</p>

<h2>PocketPal AI: for people who want any model</h2>

<p>PocketPal is free and <a href="%(gh)s" target="_blank" rel="noopener">open
source</a> (MIT licence). You search Hugging Face from inside the app and run any
GGUF model you find, with no curated list in between. That makes it the most
flexible option and the one for tinkerers. The flip side is that choosing a model
that fits your phone's memory is up to you.</p>

<h2>Private LLM: pay once, use Siri</h2>

<p>The only app here you pay for before downloading: $4.99, once, with Family
Sharing, on iPhone, iPad and Mac. It uses its own quantisation (OmniQuant), offers
larger models than most, up to 14B parameters, and integrates with Siri and
Shortcuts. A good fit if you dislike in-app purchases and want bigger models on a
Mac.</p>

<h2>Privacy AI: the most features</h2>

<p>Privacy AI is a chatbot and an agent: it plans, calls tools (its page lists
more than 60), supports MCP, has an AI keyboard for other apps, and runs both GGUF
and MLX models plus Apple's own models. Its page says local model features are
free and that cloud models and the MCP marketplace need a subscription; on the US
store the plans are $3.99 a week, $9.99 a month or $99.99 a year. It has few
ratings so far. Choose it if you want an agent, not just a chat.</p>

<h2>Pinku: ours, and narrower on purpose</h2>

<p><a href="%(pinku)s">Pinku</a> runs twelve curated open models (Gemma 3,
Gemma 3n, Llama 3.2, Qwen3, DeepSeek-R1 distills, SmolLM3 and LFM2) on iPhone,
iPad and Mac with Apple MLX. There is no account and no server. Before loading a
model it checks the memory actually free on the device; if the model does not fit,
it warns you and keeps the current one loaded instead of crashing. You can
regenerate an answer, edit a message and rerun from it, and share a message or a
whole conversation. The interface is in English, Spanish, German, French,
Japanese, Korean, Simplified Chinese and Russian.</p>

<p>It is free to download, and the six models up to 1 GB, including the default
Gemma 3 1B, work without paying. Pinku Pro is an optional one-time purchase
($9.99) that adds the six larger models, custom instructions, voice dictation
recognised on the device and read aloud. There is no subscription.</p>

<p>Where others beat it: Pinku does not read images or documents, does not browse
Hugging Face for arbitrary models, has no cloud option and no agent tools, and
does not sync chats between your devices. It also has far fewer ratings than
Locally AI, Enclave or Private LLM.</p>

<p class="article-note">Also worth knowing: <a href="%(ondevice)s" target="_blank"
rel="noopener">On-Device AI</a> sells Pro as a subscription ($3.99 or $34.99,
depending on the plan) or as a lifetime purchase.</p>

<h2>How to choose</h2>

<p>Three complaints come up again and again in the reviews of apps in this
category, ours included. They make better criteria than any feature list:</p>

<ul>
<li><strong>Crashes when loading a model.</strong> A model too big for your
device's memory will close the app. Prefer an app that tells you a model will not
fit, and start with a small one (under 1 GB) on an iPhone.</li>
<li><strong>Lost chat history.</strong> Everything lives on the device, so an
update gone wrong or a deleted app can take your chats with it. Check whether the
app lets you export or share conversations, and use it for anything you want to
keep.</li>
<li><strong>Paywalls that move.</strong> A feature that is free today can move
behind a subscription tomorrow. Read the most recent reviews, and if that worries
you, prefer a clear free tier or a one-time purchase.</li>
</ul>

<p>Then, by what you need:</p>

<ul>
<li><strong>One free app, iPhone and Mac:</strong> Locally AI.</li>
<li><strong>Any model you can find:</strong> PocketPal AI.</li>
<li><strong>Pay once, Siri, bigger models on a Mac:</strong> Private LLM.</li>
<li><strong>Local plus an optional cloud model in the same app:</strong> Enclave.</li>
<li><strong>An agent with tools:</strong> Privacy AI.</li>
<li><strong>The interface in your language, a memory check before loading, a one-time upgrade:</strong> <a href="%(pinku)s">Pinku</a>.</li>
</ul>

<h2>Where ChatGPT is not available</h2>

<p>OpenAI does not offer ChatGPT in every country. Russia, mainland China and Hong
Kong are among those missing from its <a href="%(oai)s" target="_blank"
rel="noopener">list of supported countries</a>. There, an assistant that runs on
the device is often the practical option, not just the private one, provided the
app is in your App Store. On %(date)s Apple's lookup API showed:</p>

<ul>
<li><strong>Russia:</strong> Pinku, Enclave, PocketPal AI, Private LLM and Privacy AI. Not Locally AI.</li>
<li><strong>Mainland China:</strong> Pinku, PocketPal AI and Private LLM.</li>
<li><strong>Hong Kong:</strong> all six.</li>
</ul>

<p>Models are downloaded from Hugging Face, which can be slow or unreachable in
some places. Pinku has an &ldquo;alternative download source&rdquo; setting that
uses a mirror for that case.</p>
""" % dict(_OFF, date=OFF_DATE_EN)

A6_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>App Store pages (US): <a href="%(locally)s" target="_blank" rel="noopener">Locally AI by LM Studio</a>, <a href="%(enclave)s" target="_blank" rel="noopener">Enclave</a>, <a href="%(pocketpal)s" target="_blank" rel="noopener">PocketPal AI</a>, <a href="%(privatellm)s" target="_blank" rel="noopener">Private LLM</a>, <a href="%(privacyai)s" target="_blank" rel="noopener">Privacy AI</a>, <a href="%(ondevice)s" target="_blank" rel="noopener">On-Device AI</a>, <a href="%(pinku)s">Pinku</a>. Prices, in-app purchases and descriptions as shown on %(date)s.</li>
<li>Ratings and store availability in Russia, mainland China and Hong Kong: Apple's public iTunes lookup API, %(date)s.</li>
<li>PocketPal AI source code and licence: <a href="%(gh)s" target="_blank" rel="noopener">github.com/a-ghorbani/pocketpal-ai</a>.</li>
<li>OpenAI, <a href="%(oai)s" target="_blank" rel="noopener">ChatGPT supported countries</a>.</li>
<li>Pinku's features and prices: <a href="../pinku.html">its product page</a>.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
""" % dict(_OFF, date=OFF_DATE_EN)

A6_ES_BODY = """
<p><strong>Aviso: Pinku, una de las apps de esta lista, es nuestra.</strong>
Hemos descrito las demás como las describe su propia ficha del App Store, y
decimos claramente en qué nos ganan. Precios de la App Store de EE. UU. a
%(date)s.</p>

<p>Todas hacen lo mismo en lo básico: descargan un modelo de lenguaje abierto a
tu iPhone o tu Mac y lo ejecutan ahí. Con el modelo ya en el dispositivo, tus
preguntas se responden sin conexión y sin cuenta. Lo que cambia es qué modelos
puedes usar, cuánto pagas y qué más hace la app.</p>

<h2>Las seis apps de un vistazo</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Precio (EE. UU.)</th><th>Mac App Store</th><th>Modelos</th><th>Valoración (EE. UU.)</th></tr></thead>
<tbody>
<tr><td><a href="%(locally)s" target="_blank" rel="noopener">Locally AI by LM Studio</a></td><td>Gratis</td><td>Sí</td><td>Llama, Gemma, Qwen, DeepSeek y más, con Apple MLX</td><td>4,7 &middot; 1.742</td></tr>
<tr><td><a href="%(enclave)s" target="_blank" rel="noopener">Enclave</a></td><td>Gratis; Pro 9,99 $</td><td>No aparece</td><td>Cientos de modelos abiertos; Pro añade modelos en la nube</td><td>4,7 &middot; 1.087</td></tr>
<tr><td><a href="%(pocketpal)s" target="_blank" rel="noopener">PocketPal AI</a></td><td>Gratis, código abierto</td><td>No aparece</td><td>Cualquier modelo GGUF de Hugging Face</td><td>4,1 &middot; 160</td></tr>
<tr><td><a href="%(privatellm)s" target="_blank" rel="noopener">Private LLM</a></td><td>4,99 $ por adelantado</td><td>Sí</td><td>Llama, Gemma, Qwen, Phi, Mistral y más, hasta 14B</td><td>4,2 &middot; 734</td></tr>
<tr><td><a href="%(privacyai)s" target="_blank" rel="noopener">Privacy AI</a></td><td>Gratis; suscripción para la nube</td><td>No aparece</td><td>Modelos GGUF y MLX, los de Apple y proveedores en la nube opcionales</td><td>4,8 &middot; 20</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a> (nuestra)</td><td>Gratis; Pinku Pro 9,99 $, pago único</td><td>Sí</td><td>12 modelos seleccionados con Apple MLX, de 0,34 a 4,7 GB</td><td>4,7 &middot; 12</td></tr>
</tbody>
</table></div>

<p class="article-note">&laquo;No aparece&raquo; significa que no encontramos ficha
en la Mac App Store; muchas apps de iPhone y iPad funcionan igualmente en Macs con
Apple silicon. Valoraciones de la API pública de Apple a %(date)s.</p>

<h2>Locally AI by LM Studio: la opción gratuita segura</h2>

<p>La hace el equipo de LM Studio, la app de escritorio que mucha gente ya usa
para correr modelos en el ordenador. Es gratis, no pide registro, ejecuta los
modelos con MLX de Apple y su ficha dice que también analiza imágenes. Es la que
más valoraciones tiene de todas, y está en iPhone, iPad y Mac. Si quieres una sola
app gratuita sin complicarte, empieza por aquí.</p>

<h2>Enclave: local primero, nube si la quieres</h2>

<p>Enclave te deja probar cientos de modelos abiertos, chatear con PDF y otros
documentos, hablarle por voz con el reconocimiento de Apple en el dispositivo,
crear asistentes propios y usarla desde Siri y Atajos. El uso local es gratis. Pro
aparece a 9,99 $, y la descripción de la app presenta ahora Pro como una
suscripción que añade modelos en la nube de Anthropic, OpenAI, Google y xAI. Buena
si quieres una sola app para chats privados en local y, de vez en cuando, un
modelo en la nube.</p>

<h2>PocketPal AI: para quien quiere cualquier modelo</h2>

<p>PocketPal es gratis y de <a href="%(gh)s" target="_blank" rel="noopener">código
abierto</a> (licencia MIT). Buscas en Hugging Face desde la propia app y ejecutas
cualquier modelo GGUF que encuentres, sin lista cerrada de por medio. Es la opción
más flexible y la de quien disfruta trasteando. La otra cara es que elegir un
modelo que quepa en la memoria del móvil queda de tu parte.</p>

<h2>Private LLM: pagas una vez y usas Siri</h2>

<p>La única de la lista que se paga antes de descargarla: 4,99 $, una vez, con En
Familia, en iPhone, iPad y Mac. Usa su propia cuantización (OmniQuant), ofrece
modelos más grandes que la mayoría, de hasta 14B parámetros, y se integra con
Siri y Atajos. Encaja si no te gustan las compras dentro de la app y quieres
modelos grandes en el Mac.</p>

<h2>Privacy AI: la que más hace</h2>

<p>Privacy AI es chatbot y agente: planifica, usa herramientas (su ficha habla de
más de 60), admite MCP, trae un teclado con IA para otras apps y ejecuta modelos
GGUF y MLX además de los de Apple. Su ficha dice que las funciones con modelos
locales son gratis y que los modelos en la nube y el marketplace de MCP necesitan
suscripción; en la tienda de EE. UU. cuesta 3,99 $ a la semana, 9,99 $ al mes o
99,99 $ al año. Todavía tiene pocas valoraciones. Elígela si quieres un agente, no
solo un chat.</p>

<h2>Pinku: la nuestra, y más acotada a propósito</h2>

<p><a href="%(pinku)s">Pinku</a> ejecuta doce modelos abiertos seleccionados
(Gemma 3, Gemma 3n, Llama 3.2, Qwen3, destilados de DeepSeek-R1, SmolLM3 y LFM2)
en iPhone, iPad y Mac con Apple MLX. No hay cuenta ni servidor. Antes de cargar un
modelo mira la memoria que de verdad queda libre; si no cabe, avisa y mantiene el
modelo actual en lugar de cerrarse. Puedes regenerar una respuesta, editar un
mensaje y volver a generar desde ahí, y compartir un mensaje o la conversación
entera. La interfaz está en inglés, español, alemán, francés, japonés, coreano,
chino simplificado y ruso.</p>

<p>Se descarga gratis, y los seis modelos de hasta 1 GB, incluido el que viene
por defecto (Gemma 3 1B), funcionan sin pagar. Pinku Pro es una compra única
opcional (9,99 $) que añade los seis modelos más grandes, instrucciones
personalizadas, dictado por voz reconocido en el dispositivo y lectura en voz
alta. No hay suscripción.</p>

<p>En qué le ganan las demás: Pinku no lee imágenes ni documentos, no busca en
Hugging Face cualquier modelo, no tiene opción en la nube ni herramientas de
agente, y no sincroniza los chats entre tus dispositivos. Además tiene muchas menos
valoraciones que Locally AI, Enclave o Private LLM.</p>

<p class="article-note">Conviene saberlo también: <a href="%(ondevice)s"
target="_blank" rel="noopener">On-Device AI</a> vende Pro como suscripción (3,99 $
o 34,99 $, según el plan) o como compra de por vida.</p>

<h2>Cómo elegir</h2>

<p>Hay tres quejas que se repiten en las reseñas de las apps de esta categoría,
la nuestra incluida. Sirven más como criterio que cualquier lista de
funciones:</p>

<ul>
<li><strong>Se cierra al cargar un modelo.</strong> Un modelo que no cabe en la
memoria del dispositivo tumba la app. Mejor una app que te avise de que no cabe, y
en un iPhone empieza por uno pequeño (de menos de 1 GB).</li>
<li><strong>Historial de chats perdido.</strong> Todo vive en el dispositivo, así
que una actualización que sale mal o una app borrada pueden llevarse tus chats.
Mira si la app deja exportar o compartir conversaciones y hazlo con lo que
quieras conservar.</li>
<li><strong>Muros de pago que se mueven.</strong> Lo que hoy es gratis puede
pasar mañana a una suscripción. Lee las reseñas más recientes y, si te preocupa,
prefiere un nivel gratuito claro o una compra única.</li>
</ul>

<p>Y después, según lo que necesites:</p>

<ul>
<li><strong>Una sola app gratis, en iPhone y Mac:</strong> Locally AI.</li>
<li><strong>Cualquier modelo que encuentres:</strong> PocketPal AI.</li>
<li><strong>Pagar una vez, Siri y modelos grandes en el Mac:</strong> Private LLM.</li>
<li><strong>Local y, si quieres, un modelo en la nube en la misma app:</strong> Enclave.</li>
<li><strong>Un agente con herramientas:</strong> Privacy AI.</li>
<li><strong>La interfaz en tu idioma, comprobación de memoria antes de cargar y una mejora de pago único:</strong> <a href="%(pinku)s">Pinku</a>.</li>
</ul>

<h2>Donde ChatGPT no está disponible</h2>

<p>OpenAI no ofrece ChatGPT en todos los países. Rusia, China continental y Hong
Kong no están en su <a href="%(oai)s" target="_blank" rel="noopener">lista de
países admitidos</a>. Allí un asistente que corre en el dispositivo suele ser la
opción práctica, no solo la privada, siempre que la app esté en tu App Store. A
%(date)s, la API de Apple mostraba:</p>

<ul>
<li><strong>Rusia:</strong> Pinku, Enclave, PocketPal AI, Private LLM y Privacy AI. Locally AI no.</li>
<li><strong>China continental:</strong> Pinku, PocketPal AI y Private LLM.</li>
<li><strong>Hong Kong:</strong> las seis.</li>
</ul>

<p>Los modelos se descargan de Hugging Face, que en algunos sitios va lento o no
responde. Pinku tiene un ajuste de &laquo;fuente de descarga alternativa&raquo; que
usa un espejo para ese caso.</p>
""" % dict(_OFF, date=OFF_DATE_ES)

A6_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Fichas del App Store (EE. UU.): <a href="%(locally)s" target="_blank" rel="noopener">Locally AI by LM Studio</a>, <a href="%(enclave)s" target="_blank" rel="noopener">Enclave</a>, <a href="%(pocketpal)s" target="_blank" rel="noopener">PocketPal AI</a>, <a href="%(privatellm)s" target="_blank" rel="noopener">Private LLM</a>, <a href="%(privacyai)s" target="_blank" rel="noopener">Privacy AI</a>, <a href="%(ondevice)s" target="_blank" rel="noopener">On-Device AI</a>, <a href="%(pinku)s">Pinku</a>. Precios, compras dentro de la app y descripciones a %(date)s.</li>
<li>Valoraciones y disponibilidad en Rusia, China continental y Hong Kong: API pública de búsqueda de iTunes de Apple, %(date)s.</li>
<li>Código y licencia de PocketPal AI: <a href="%(gh)s" target="_blank" rel="noopener">github.com/a-ghorbani/pocketpal-ai</a>.</li>
<li>OpenAI, <a href="%(oai)s" target="_blank" rel="noopener">ChatGPT supported countries</a>.</li>
<li>Funciones y precios de Pinku: <a href="../../pinku.html">su página</a>.</li>
</ul>
<p>Si algo está desactualizado, <a href="mailto:sagalabs@proton.me">avísanos</a> y
corregimos la página.</p>
""" % dict(_OFF, date=OFF_DATE_ES)


# --------------------------------------------------------------------------
# 7 — Apps de video con IA para iPhone (comparativa, Dora es nuestra)
# --------------------------------------------------------------------------
# Dora es nuestra: el aviso va arriba del todo. Datos de las demas sacados el
# 7 oct 2026 de su ficha del App Store (EE. UU.), sus compras dentro de la app
# y la API publica de lookup de iTunes. Sin precios: solo como cobran.
# Fuera: Hailuo (la app oficial id6741675037 ya no esta en la tienda) e
# Higgsfield (sin app oficial; hay imitaciones con su nombre). CapCut: su ficha
# no habla de generar video; lo de Seedance sale de capcut.com y dice
# "subscriber accounts" en Europa, Asia, Oriente Medio y Sudamerica.
# Dora: solo los hechos verificados (docs/README.md del repo Dora): medianas
# 115 s video y 48 s imagen, 22 modelos, sin generaciones gratis, sin precios.
# Sin rayas en el texto.

AIV_DATE_ISO = "2026-10-07"
AIV_DATE_EN = "7 October 2026"
AIV_DATE_ES = "7 de octubre de 2026"

DORA_WEB = "https://doravideo.com/?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=dora_blog_compare"
DORA_IOS = "https://apps.apple.com/app/id6754180384"
DORA_CONNECTORS = "https://doravideo.com/connectors?utm_source=aisagalab&amp;utm_medium=referral&amp;utm_campaign=dora_blog_compare"
CAPCUT = "https://apps.apple.com/us/app/id1500855883"
CAPCUT_SEEDANCE = "https://www.capcut.com/features/seedance-2-5-for-video-editor"
RUNWAY = "https://apps.apple.com/us/app/id1665024375"
PIKA = "https://apps.apple.com/us/app/id6680155400"
LUMA = "https://apps.apple.com/us/app/id6478852867"
KLING = "https://apps.apple.com/us/app/id6738049229"
PIXVERSE = "https://apps.apple.com/us/app/id6767802142"
INVIDEO = "https://apps.apple.com/us/app/id6471394316"

_AIV = dict(dora=DORA_WEB, dora_ios=DORA_IOS, connectors=DORA_CONNECTORS,
            capcut=CAPCUT, seedance=CAPCUT_SEEDANCE, runway=RUNWAY, pika=PIKA,
            luma=LUMA, kling=KLING, pixverse=PIXVERSE, invideo=INVIDEO)

# Preguntas frecuentes: el mismo texto va visible y en el FAQPage.
AIV_FAQ_EN = [
    ("What is the best AI video generator app for iPhone?",
     "It depends on the job. Runway and Kling AI are strong all-rounders for cinematic clips. "
     "Pika and PixVerse are built around effects and templates. invideo and CapCut are the ones "
     "with a full timeline editor. Dora fits people who want many short vertical clips from "
     "photos, or who work inside Claude or ChatGPT. It is made by Saga Labs, who wrote this page."),
    ("Can I turn a photo into a video on iPhone?",
     "Yes. Runway, Pika, Kling AI, PixVerse Lite, invideo and Dora all say on their App Store "
     "pages that they turn a still photo into a moving video. Luma Dream Machine works from "
     "reference images, up to four at a time."),
    ("How long does an AI video take to generate?",
     "Usually minutes, not seconds. Runway's App Store page says a first generation takes about "
     "two minutes. In Dora the measured median is 115 seconds for a video and 48 seconds for an "
     "image. Longer, higher resolution clips take longer in every app."),
    ("Which apps can copy a dance onto the person in my photo?",
     "PixVerse Lite and Dora both have a feature called Motion Control: you give it a photo of a "
     "person and a reference video, and the person in the photo makes the moves from the video."),
    ("Can I make AI videos from inside ChatGPT or Claude?",
     "Dora works inside Claude and ChatGPT through an MCP connector, using the same account and "
     "balance as the app; the setup steps are at doravideo.com/connectors. We did not check "
     "whether the other apps here offer the same, so look at their own sites."),
    ("Are these apps free?",
     "All of them are free to download, and all of them charge through in-app purchases: "
     "subscriptions, credit packs or both. Runway says it is free to start. Dora has paid plans "
     "only and no free generations."),
]

AIV_FAQ_ES = [
    ("¿Cuál es la mejor app para generar vídeo con IA en iPhone?",
     "Depende de para qué. Runway y Kling AI son buenas para casi todo y dan clips de aire "
     "cinematográfico. Pika y PixVerse giran en torno a efectos y plantillas. invideo y CapCut son "
     "las que tienen un editor completo con línea de tiempo. Dora encaja con quien quiere muchos "
     "clips verticales cortos a partir de fotos, o trabaja dentro de Claude o ChatGPT. La hace "
     "Saga Labs, que es quien escribe esta página."),
    ("¿Puedo convertir una foto en vídeo en el iPhone?",
     "Sí. Runway, Pika, Kling AI, PixVerse Lite, invideo y Dora dicen en su ficha del App Store "
     "que convierten una foto fija en un vídeo con movimiento. Luma Dream Machine trabaja con "
     "imágenes de referencia, hasta cuatro a la vez."),
    ("¿Cuánto tarda en generarse un vídeo con IA?",
     "Minutos, no segundos. La ficha de Runway dice que la primera generación tarda unos dos "
     "minutos. En Dora la mediana medida es de 115 segundos para un vídeo y 48 segundos para una "
     "imagen. En todas las apps, los clips más largos o de más resolución tardan más."),
    ("¿Qué apps copian un baile en la persona de mi foto?",
     "PixVerse Lite y Dora tienen una función llamada Motion Control: le das la foto de una "
     "persona y un vídeo de referencia, y la persona de la foto hace los movimientos del vídeo."),
    ("¿Se pueden hacer vídeos con IA desde ChatGPT o Claude?",
     "Dora funciona dentro de Claude y ChatGPT con un conector MCP, con la misma cuenta y el mismo "
     "saldo que la app; los pasos están en doravideo.com/connectors. No hemos comprobado si las "
     "demás apps de esta lista ofrecen lo mismo, así que mira sus propias webs."),
    ("¿Son gratis estas apps?",
     "Todas se descargan gratis y todas cobran con compras dentro de la app: suscripciones, packs "
     "de créditos o las dos cosas. Runway dice que se puede empezar gratis. Dora solo tiene planes "
     "de pago y no da generaciones gratis."),
]


def _faq_html(faq, heading):
    import html as _h
    parts = ["\n<h2>%s</h2>\n" % heading]
    for q, a in faq:
        parts.append("<h3>%s</h3>\n<p>%s</p>\n" % (_h.escape(q, quote=False), _h.escape(a, quote=False)))
    return "".join(parts)


def _jsonld_faq(article_jsonld, faq):
    """BlogPosting + FAQPage en un @graph. Sale de _jsonld para no duplicar autor."""
    import json
    art = json.loads(article_jsonld)
    art.pop("@context")
    page = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }
    return json.dumps({"@context": "https://schema.org", "@graph": [art, page]},
                      ensure_ascii=False, indent=2)


A7_EN_BODY = """
<p><strong>Disclosure: we make Dora, one of the apps below.</strong> Saga Labs,
the studio that runs this site, builds and sells it. We have described the other
apps the way their own App Store pages describe them, and we say plainly where
they beat us. Ratings and in-app purchases are from the US App Store on
%(date)s. We list how each app charges, not prices, because prices change by
country and by week.</p>

<p>Every app here does some version of the same thing: you give it a photo or a
few words, and a few minutes later you get back a short video clip. They differ
in which models they run, how much editing they let you do afterwards, and how
they charge.</p>

<h2>The eight apps at a glance</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Strongest at</th><th>How it charges</th><th>Rating (US)</th></tr></thead>
<tbody>
<tr><td><a href="%(runway)s" target="_blank" rel="noopener">Runway</a></td><td>Many top models in one app, an agent that builds a whole video</td><td>Free to start; subscriptions and credit packs</td><td>4.5 &middot; 16,768</td></tr>
<tr><td><a href="%(kling)s" target="_blank" rel="noopener">Kling AI</a></td><td>Longer clips, 1080p or 4K, extension up to 3 minutes</td><td>Credit packs and plans, weekly or monthly</td><td>4.7 &middot; 31,559</td></tr>
<tr><td><a href="%(pika)s" target="_blank" rel="noopener">Pika</a></td><td>Playful effects: swap, add or melt things in your clips</td><td>Subscriptions, weekly, monthly or yearly</td><td>4.7 &middot; 4,185</td></tr>
<tr><td><a href="%(pixverse)s" target="_blank" rel="noopener">PixVerse Lite</a></td><td>Trending templates, AI dance, lip sync, Motion Control</td><td>Plans, weekly or yearly, and credit packs</td><td>4.3 &middot; 1,228</td></tr>
<tr><td><a href="%(luma)s" target="_blank" rel="noopener">Luma Dream Machine</a></td><td>Consistent characters from one face photo; edit by describing</td><td>Subscriptions, plus credit packs</td><td>4.5 &middot; 1,795</td></tr>
<tr><td><a href="%(invideo)s" target="_blank" rel="noopener">invideo</a></td><td>A full multitrack editor plus 200+ models, team editing</td><td>Plans and add-on packs</td><td>4.5 &middot; 27,821</td></tr>
<tr><td><a href="%(capcut)s" target="_blank" rel="noopener">CapCut</a></td><td>Editing: timeline, captions, effects, 4K export</td><td>Free editor; monthly or yearly subscriptions</td><td>4.6 &middot; 1,123,165</td></tr>
<tr><td><a href="%(dora_ios)s" target="_blank" rel="noopener">Dora</a> (ours)</td><td>Many short vertical clips from photos; works inside Claude and ChatGPT</td><td>Paid plans only, no free generations</td><td>4.3 &middot; 15</td></tr>
</tbody>
</table></div>

<p class="article-note">All eight are free to download from the App Store and
charge through in-app purchases. Ratings are from Apple's public lookup API on
%(date)s.</p>

<h2>Runway: the most models in one place</h2>

<p>Runway's app puts several of the best known video and image models side by
side (its page lists Seedance 2.5, Kling 3 Pro, its own Gen-4.5, Nano Banana Pro
and Nano Banana 2) and does text to video, image to video and video to video.
Its Runway Agent takes a plain description, plans the shots, generates them and
assembles the finished video. Characters, objects and places can be kept the
same across shots, and work syncs with Runway on a computer. It is free to
start, with subscriptions and credit packs for more. Best for people who want to
pick the model for each job and may finish the work on a laptop.</p>

<h2>Kling AI: longer, sharper clips</h2>

<p>Kling AI runs its own Kling models. Its page says it generates up to 15
seconds in native 1080p or 4K, and that Video Extension takes a clip up to three
minutes. It also generates images in 4K, and has a community feed where you can
clone a piece you like and try the idea yourself. It charges with credit
packs and plans, including a weekly one. Best for people who care most about
motion and image quality, or who need a clip longer than a few seconds.</p>

<h2>Pika: effects first</h2>

<p>Pika is built for fun, shareable clips. Pikaffects melt, squish, explode or
levitate a photo; Pikaswaps replace anything in a video with something from your
photos or a prompt; Pikadditions drop new objects or people into a video you
already have while keeping its sound. It also does plain image to video and text
to video. It charges with subscriptions, weekly, monthly or yearly. Best for
social posts and memes where the effect is the point.</p>

<h2>PixVerse Lite: templates and trends</h2>

<p>PixVerse Lite is the current iPhone app from PixVerse, running its own V6
model and several outside models. Its strength is the template library: AI dance,
transformations, beauty and miniature styles, ready to apply to a photo. It also
has Motion Control (a character photo plus a reference motion video), lip sync
for talking avatars, video upscaling to 4K and a video extension tool. It charges
with weekly or yearly plans and credit packs. Best for people who follow trends
and want a result in a couple of taps.</p>

<h2>Luma Dream Machine: talk to it like a creative partner</h2>

<p>Dream Machine is Luma's app for images and video. Instead of prompt syntax,
you ask for what you want and use Modify to change an image or video by
describing the change. Reference lets you guide it with up to four images, and a
single photo of a face is enough to keep a person consistent across many images
and videos. It charges with subscriptions plus credit packs. Best for people
exploring an idea or a look across many variations.</p>

<h2>invideo: when you also need to edit</h2>

<p>invideo combines generation and editing. Its agent, Agent Two, turns a plain
description into a video and keeps changing it as you direct; every AI edit stays
editable on a professional multitrack timeline. It offers more than 200 models
for image, video, voice, sound and music, and real time collaboration with a team.
It charges with plans and add-on packs. Best for ads, explainers and YouTube
videos that need more than one clip.</p>

<h2>CapCut: the editor most people already have</h2>

<p>CapCut is first of all a video editor, and an excellent free one: multitrack
timeline, keyframes, auto captions, text to speech, background removal, millions
of music clips and 4K export at 60 fps. Its App Store page does not describe
generating video from a prompt. CapCut's own site says ByteDance's Seedance 2.5
video model is <a href="%(seedance)s" target="_blank" rel="noopener">rolling out
to CapCut</a> for subscriber accounts in Europe, Asia, the Middle East and South
America. The editor is free, with monthly or yearly subscriptions for more. Best
for finishing clips made anywhere, including in every other app on this list.</p>

<h2>Dora: ours, and narrower on purpose</h2>

<p><a href="%(dora)s">Dora</a> turns a photo or a text description into a short
video or an image, vertical, horizontal or square. It is an iPhone app,
<a href="%(dora_ios)s" target="_blank" rel="noopener">DORA &middot; AI Video
Generator</a>, and a website, <a href="%(dora)s">doravideo.com</a>, with the same
account and balance on both. A video takes about two minutes and an image about a
minute (measured medians: 115 seconds and 48 seconds). There are 22 models in the
app to choose from. Motion Control copies the moves of a dance video onto the
person in a photo.</p>

<p>Dora also works inside Claude and ChatGPT through an MCP connector, so you can
ask the assistant for a video in the middle of a conversation and it uses your
Dora account; the <a href="%(connectors)s">setup steps are here</a>. Dora has paid
plans only, with no free generations.</p>

<p>Where others beat it: Dora is not an editor. It has no timeline, does not cut
clips together and does not publish to social networks; you get the file and take
it to CapCut, invideo or wherever you edit. It has no community feed or agent that
assembles a whole video, and it has far fewer ratings than any other app here.</p>

<h2>Left out, and why</h2>

<p>Hailuo, from MiniMax, and Higgsfield are both popular for AI video. On
%(date)s we could not find an official app from either in the US App Store, while
several apps with similar names were listed by other developers. If you want
either one, start from the company's own website rather than an App Store
search.</p>

<h2>How to choose</h2>

<ul>
<li><strong>Pick the model yourself, finish on a computer:</strong> Runway.</li>
<li><strong>Quality and longer clips:</strong> Kling AI.</li>
<li><strong>Effects for social posts and memes:</strong> Pika.</li>
<li><strong>Trends and ready templates:</strong> PixVerse Lite.</li>
<li><strong>Explore a character or a look across many versions:</strong> Luma Dream Machine.</li>
<li><strong>A finished ad or explainer with editing and a team:</strong> invideo.</li>
<li><strong>Editing what you already made:</strong> CapCut.</li>
<li><strong>Many short vertical clips from photos, or video from inside Claude or ChatGPT:</strong> <a href="%(dora)s">Dora</a>.</li>
</ul>
""" % dict(_AIV, date=AIV_DATE_EN)

A7_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li>App Store pages (US): <a href="%(runway)s" target="_blank" rel="noopener">Runway</a>, <a href="%(kling)s" target="_blank" rel="noopener">Kling AI</a>, <a href="%(pika)s" target="_blank" rel="noopener">Pika</a>, <a href="%(pixverse)s" target="_blank" rel="noopener">PixVerse Lite</a>, <a href="%(luma)s" target="_blank" rel="noopener">Luma Dream Machine</a>, <a href="%(invideo)s" target="_blank" rel="noopener">invideo</a>, <a href="%(capcut)s" target="_blank" rel="noopener">CapCut</a>, <a href="%(dora_ios)s" target="_blank" rel="noopener">Dora</a>. Descriptions and in-app purchases as shown on %(date)s.</li>
<li>Ratings: Apple's public iTunes lookup API, %(date)s.</li>
<li>CapCut, <a href="%(seedance)s" target="_blank" rel="noopener">Seedance 2.5 for Video Editor</a>.</li>
<li>Dora's connectors for Claude and ChatGPT: <a href="%(connectors)s">doravideo.com/connectors</a>. Dora's generation times are medians we measured on our own production jobs.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
""" % dict(_AIV, date=AIV_DATE_EN)

A7_ES_BODY = """
<p><strong>Aviso: Dora, una de las apps de esta lista, es nuestra.</strong> La
hace y la vende Saga Labs, el estudio que publica esta web. Hemos descrito las
demás como las describe su propia ficha del App Store, y decimos claramente en
qué nos ganan. Valoraciones y compras dentro de la app de la App Store de EE. UU.
a %(date)s. Contamos cómo cobra cada app, no los precios, porque cambian según el
país y la semana.</p>

<p>Todas hacen, a su manera, lo mismo: les das una foto o unas palabras y unos
minutos después te devuelven un clip de vídeo corto. Cambian los modelos que usan,
cuánto te dejan editar después y cómo cobran.</p>

<h2>Las ocho apps de un vistazo</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>En qué destaca</th><th>Cómo cobra</th><th>Valoración (EE. UU.)</th></tr></thead>
<tbody>
<tr><td><a href="%(runway)s" target="_blank" rel="noopener">Runway</a></td><td>Muchos de los mejores modelos en una app, un agente que monta el vídeo entero</td><td>Se empieza gratis; suscripciones y packs de créditos</td><td>4,5 &middot; 16.768</td></tr>
<tr><td><a href="%(kling)s" target="_blank" rel="noopener">Kling AI</a></td><td>Clips más largos, 1080p o 4K, extensión hasta 3 minutos</td><td>Packs de créditos y planes, semanales o mensuales</td><td>4,7 &middot; 31.559</td></tr>
<tr><td><a href="%(pika)s" target="_blank" rel="noopener">Pika</a></td><td>Efectos divertidos: cambiar, añadir o derretir cosas en tus clips</td><td>Suscripciones semanales, mensuales o anuales</td><td>4,7 &middot; 4.185</td></tr>
<tr><td><a href="%(pixverse)s" target="_blank" rel="noopener">PixVerse Lite</a></td><td>Plantillas de tendencia, baile con IA, lip sync, Motion Control</td><td>Planes semanales o anuales y packs de créditos</td><td>4,3 &middot; 1.228</td></tr>
<tr><td><a href="%(luma)s" target="_blank" rel="noopener">Luma Dream Machine</a></td><td>Personajes coherentes a partir de una foto de la cara; editar describiendo</td><td>Suscripciones y packs de créditos</td><td>4,5 &middot; 1.795</td></tr>
<tr><td><a href="%(invideo)s" target="_blank" rel="noopener">invideo</a></td><td>Editor multipista completo, más de 200 modelos, edición en equipo</td><td>Planes y packs adicionales</td><td>4,5 &middot; 27.821</td></tr>
<tr><td><a href="%(capcut)s" target="_blank" rel="noopener">CapCut</a></td><td>Editar: línea de tiempo, subtítulos, efectos, exportar en 4K</td><td>Editor gratis; suscripciones mensuales o anuales</td><td>4,6 &middot; 1.123.165</td></tr>
<tr><td><a href="%(dora_ios)s" target="_blank" rel="noopener">Dora</a> (nuestra)</td><td>Muchos clips verticales cortos a partir de fotos; funciona dentro de Claude y ChatGPT</td><td>Solo planes de pago, sin generaciones gratis</td><td>4,3 &middot; 15</td></tr>
</tbody>
</table></div>

<p class="article-note">Las ocho se descargan gratis del App Store y cobran con
compras dentro de la app. Valoraciones de la API pública de Apple a %(date)s.</p>

<h2>Runway: la que más modelos reúne</h2>

<p>La app de Runway pone lado a lado varios de los modelos de vídeo e imagen más
conocidos (su ficha cita Seedance 2.5, Kling 3 Pro, su propio Gen-4.5, Nano Banana
Pro y Nano Banana 2) y hace texto a vídeo, imagen a vídeo y vídeo a vídeo. Su
Runway Agent recibe una descripción normal, planifica los planos, los genera y
monta el vídeo terminado. Puede mantener iguales personajes, objetos y lugares de
un plano a otro, y el trabajo se sincroniza con Runway en el ordenador. Se empieza
gratis, con suscripciones y packs de créditos para más. Para quien quiere elegir
el modelo de cada encargo y quizá terminar en el portátil.</p>

<h2>Kling AI: clips más largos y más nítidos</h2>

<p>Kling AI usa sus propios modelos Kling. Su ficha dice que genera hasta 15
segundos en 1080p nativo o en 4K, y que Video Extension alarga un clip hasta tres
minutos. También genera imágenes en 4K y tiene un muro de la comunidad donde
puedes clonar una obra que te guste y probar la idea tú. Cobra con packs de
créditos y planes, uno de ellos semanal. Para quien prioriza la calidad del
movimiento y de la imagen, o necesita un clip de más de unos segundos.</p>

<h2>Pika: primero, los efectos</h2>

<p>Pika está hecha para clips divertidos y para compartir. Pikaffects derrite,
aplasta, hace explotar o hace levitar una foto; Pikaswaps cambia cualquier cosa de un
vídeo por algo de tus fotos o de una descripción; Pikadditions mete objetos o
personas nuevas en un vídeo que ya tienes sin tocar su sonido. También hace imagen
a vídeo y texto a vídeo sin más. Cobra con suscripciones semanales, mensuales o
anuales. Para publicaciones y memes en los que el efecto es lo importante.</p>

<h2>PixVerse Lite: plantillas y tendencias</h2>

<p>PixVerse Lite es la app de iPhone actual de PixVerse, con su propio modelo V6 y
varios modelos externos. Su fuerte es la biblioteca de plantillas: baile con IA,
transformaciones, estilos de belleza y de miniatura, listos para aplicar a una
foto. Tiene además Motion Control (foto de un personaje más un vídeo de movimiento
de referencia), lip sync para avatares que hablan, escalado de vídeo a 4K y una
herramienta para alargar vídeos. Cobra con planes semanales o anuales y packs de
créditos. Para quien sigue las tendencias y quiere el resultado en dos toques.</p>

<h2>Luma Dream Machine: le hablas como a un compañero creativo</h2>

<p>Dream Machine es la app de Luma para imágenes y vídeo. En vez de aprender a
escribir prompts, pides lo que quieres y usas Modify para cambiar una imagen o un
vídeo describiendo el cambio. Reference te deja guiarla con hasta cuatro imágenes,
y basta una foto de una cara para mantener a una persona igual en muchas imágenes
y vídeos. Cobra con suscripciones y packs de créditos. Para quien explora una idea
o un estilo con muchas variaciones.</p>

<h2>invideo: cuando también hay que editar</h2>

<p>invideo junta generación y edición. Su agente, Agent Two, convierte una
descripción normal en un vídeo y lo sigue cambiando según le indicas; cada edición
de la IA se puede retocar en una línea de tiempo multipista profesional. Ofrece
más de 200 modelos de imagen, vídeo, voz, sonido y música, y edición en tiempo real
con un equipo. Cobra con planes y packs adicionales. Para anuncios, vídeos
explicativos y de YouTube que necesitan más de un clip.</p>

<h2>CapCut: el editor que casi todo el mundo ya tiene</h2>

<p>CapCut es ante todo un editor de vídeo, y uno muy bueno y gratis: línea de
tiempo multipista, fotogramas clave, subtítulos automáticos, texto a voz, quitar
fondos, millones de clips de música y exportación en 4K a 60 fps. Su ficha del App
Store no habla de generar vídeo a partir de una descripción. La web de CapCut dice
que Seedance 2.5, el modelo de vídeo de ByteDance, <a href="%(seedance)s"
target="_blank" rel="noopener">está llegando a CapCut</a> para cuentas de
suscriptor en Europa, Asia, Oriente Medio y Sudamérica. El editor es gratis, con
suscripciones mensuales o anuales para más. Para terminar clips hechos en
cualquier sitio, incluidas todas las demás apps de esta lista.</p>

<h2>Dora: la nuestra, y más acotada a propósito</h2>

<p><a href="%(dora)s">Dora</a> convierte una foto o una descripción en texto en un
vídeo corto o una imagen, en vertical, horizontal o cuadrado. Es una app de
iPhone, <a href="%(dora_ios)s" target="_blank" rel="noopener">DORA &middot; AI Video
Generator</a>, y una web, <a href="%(dora)s">doravideo.com</a>, con la misma cuenta
y el mismo saldo en las dos. Un vídeo tarda unos dos minutos y una imagen, más o
menos uno (medianas medidas: 115 segundos y 48 segundos). En la app hay 22 modelos
para elegir. Motion Control copia los movimientos de un vídeo de baile en la
persona de una foto.</p>

<p>Dora funciona también dentro de Claude y ChatGPT con un conector MCP: le pides
un vídeo al asistente en mitad de la conversación y lo hace con tu cuenta de Dora;
<a href="%(connectors)s">aquí están los pasos</a>. Dora solo tiene planes de pago,
sin generaciones gratis.</p>

<p>En qué le ganan las demás: Dora no es un editor. No tiene línea de tiempo, no
une clips y no publica en redes; te da el archivo y lo llevas a CapCut, a invideo
o a donde edites. No tiene muro de la comunidad ni un agente que monte un vídeo
entero, y tiene muchas menos valoraciones que cualquier otra app de la lista.</p>

<h2>Las que faltan, y por qué</h2>

<p>Hailuo, de MiniMax, y Higgsfield son populares para vídeo con IA. A %(date)s no
encontramos una app oficial de ninguna de las dos en la App Store de EE. UU., y sí
varias apps con nombres parecidos de otros desarrolladores. Si quieres una de
ellas, entra desde la web de la propia empresa y no desde una búsqueda en el App
Store.</p>

<h2>Cómo elegir</h2>

<ul>
<li><strong>Elegir tú el modelo y terminar en el ordenador:</strong> Runway.</li>
<li><strong>Calidad y clips más largos:</strong> Kling AI.</li>
<li><strong>Efectos para redes y memes:</strong> Pika.</li>
<li><strong>Tendencias y plantillas listas:</strong> PixVerse Lite.</li>
<li><strong>Explorar un personaje o un estilo en muchas versiones:</strong> Luma Dream Machine.</li>
<li><strong>Un anuncio o vídeo explicativo terminado, con edición y en equipo:</strong> invideo.</li>
<li><strong>Editar lo que ya tienes:</strong> CapCut.</li>
<li><strong>Muchos clips verticales cortos a partir de fotos, o vídeo desde dentro de Claude o ChatGPT:</strong> <a href="%(dora)s">Dora</a>.</li>
</ul>
""" % dict(_AIV, date=AIV_DATE_ES)

A7_ES_SOURCES = """
<h2>Fuentes</h2>
<ul>
<li>Fichas del App Store (EE. UU.): <a href="%(runway)s" target="_blank" rel="noopener">Runway</a>, <a href="%(kling)s" target="_blank" rel="noopener">Kling AI</a>, <a href="%(pika)s" target="_blank" rel="noopener">Pika</a>, <a href="%(pixverse)s" target="_blank" rel="noopener">PixVerse Lite</a>, <a href="%(luma)s" target="_blank" rel="noopener">Luma Dream Machine</a>, <a href="%(invideo)s" target="_blank" rel="noopener">invideo</a>, <a href="%(capcut)s" target="_blank" rel="noopener">CapCut</a>, <a href="%(dora_ios)s" target="_blank" rel="noopener">Dora</a>. Descripciones y compras dentro de la app a %(date)s.</li>
<li>Valoraciones: API pública de búsqueda de iTunes de Apple, %(date)s.</li>
<li>CapCut, <a href="%(seedance)s" target="_blank" rel="noopener">Seedance 2.5 for Video Editor</a>.</li>
<li>Conectores de Dora para Claude y ChatGPT: <a href="%(connectors)s">doravideo.com/connectors</a>. Los tiempos de Dora son medianas que medimos en nuestros propios trabajos de producción.</li>
</ul>
<p>Si algo está desactualizado, <a href="mailto:sagalabs@proton.me">avísanos</a> y
corregimos la página.</p>
""" % dict(_AIV, date=AIV_DATE_ES)
