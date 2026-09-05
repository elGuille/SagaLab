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

APP_STORE = "https://apps.apple.com/us/app/pinku-private-ai/id6754878073"
KEEPER = "https://apps.apple.com/au/app/only-gallery-keeper/id1532670722"


def _jsonld(headline, desc, url, lang, section):
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
  "author": { "@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/" },
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
}""" % (_q(headline), _q(desc), lang, section, DATE_ISO, DATE_ISO, url)


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
<a href="we-asked-openai-and-anthropic-to-delete-our-data.html">what &ldquo;delete&rdquo;
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
is arguing against. We wrote up exactly what you gain and lose in
a companion piece on what actually runs on an iPhone in 2026 (coming shortly).</p>
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
<a href="pedimos-a-openai-y-anthropic-que-borraran-nuestros-datos.html">qu&eacute;
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
contra el que argumenta este art&iacute;culo. Escribimos exactamente qu&eacute;
se gana y qu&eacute; se pierde en
un art&iacute;culo hermano sobre qu&eacute; corre de verdad en un iPhone en 2026
(en camino).</p>
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
        <h1>Writing</h1>
        <p class="article-standfirst">Notes on private and on-device AI. Every
        number we publish comes from a primary source, linked in the article.</p>
        <p class="article-meta">Saga Labs
            <span class="lang-switch"> &middot; <a href="es/">Leer en espa&ntilde;ol</a></span>
        </p>
        <div class="article-body">
        <ul class="post-list">
            <li>
                <a href="what-ai-does-with-your-conversations.html">What ChatGPT, Claude and Gemini actually do with your conversations</a>
                <p>Retention windows, human review and training defaults for the
                three main assistants, taken from their own published policies.
                Google keeps human-reviewed chats for three years after you
                delete them.</p>
            </li>
            <li>
                <a href="we-asked-openai-and-anthropic-to-delete-our-data.html">We asked OpenAI and Anthropic to delete our data. Neither said it was gone.</a>
                <p>Five layers sit between the button and the conversation being
                gone. We asked OpenAI and Anthropic to delete our data; neither
                said it was gone, and both were being accurate.</p>
            </li>
        </ul>
        </div>
"""

INDEX_ES = """
        <p class="article-kicker">Saga Labs</p>
        <h1>Art&iacute;culos</h1>
        <p class="article-standfirst">Notas sobre IA privada y en el dispositivo.
        Cada cifra que publicamos sale de una fuente primaria enlazada en el
        art&iacute;culo.</p>
        <p class="article-meta">Saga Labs
            <span class="lang-switch"> &middot; <a href="../">Read in English</a></span>
        </p>
        <div class="article-body">
        <ul class="post-list">
            <li>
                <a href="que-hace-la-ia-con-tus-conversaciones.html">Qu&eacute; hacen de verdad ChatGPT, Claude y Gemini con tus conversaciones</a>
                <p>Plazos de retenci&oacute;n, revisi&oacute;n humana y valores por
                defecto de entrenamiento de los tres asistentes principales, sacados
                de sus propias pol&iacute;ticas. Google conserva tres a&ntilde;os los
                chats revisados por humanos despu&eacute;s de que los borres.</p>
            </li>
            <li>
                <a href="pedimos-a-openai-y-anthropic-que-borraran-nuestros-datos.html">Pedimos a OpenAI y a Anthropic que borraran nuestros datos. Ninguno dijo que estuvieran borrados.</a>
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
        title="Writing — Saga Labs",
        desc="Notes on private and on-device AI from Saga Labs, the studio behind Pinku Private AI. Sourced from primary policy documents.",
        og_title="Writing — Saga Labs",
        alternates=hreflang("blog/", "blog/es/"),
        og_type="website",
        jsonld="""{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Saga Labs Writing",
  "url": "https://aisagalab.com/blog/",
  "inLanguage": "en",
  "publisher": { "@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/" }
}""",
        body=INDEX_EN,
    ))

    out.append(render(
        path="blog/es/index.html", lang="es",
        title="Artículos — Saga Labs",
        desc="Notas sobre IA privada y en el dispositivo, del estudio detrás de Pinku Private AI. Con fuentes primarias.",
        og_title="Artículos — Saga Labs",
        alternates=hreflang("blog/", "blog/es/"),
        og_type="website",
        jsonld="""{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Saga Labs Artículos",
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
            "Saga Labs &middot; " + DATE_EN,
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
            "Saga Labs &middot; " + DATE_ES,
            "Read in English", "../what-ai-does-with-your-conversations.html",
        ) + '\n        <div class="article-body">' + A1_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A1_ES_SOURCES + '</div>',
    ))

    # --- 4: que significa borrar un chat ----------------------------------
    en_path = "blog/we-asked-openai-and-anthropic-to-delete-our-data.html"
    es_path = "blog/es/pedimos-a-openai-y-anthropic-que-borraran-nuestros-datos.html"
    alt = hreflang(en_path, es_path)

    h1_en = "We asked OpenAI and Anthropic to delete our data. Neither said it was gone."
    d_en = ("Five layers sit between the delete button and the conversation being gone: "
            "storage, model weights, the reviewer's copy, the safety flag and the court. "
            "With the OpenAI privacy team's reply, and Anthropic's.")
    out.append(render(
        path=en_path, lang="en",
        title="We asked OpenAI and Anthropic to delete our data. Neither said it was gone. — Saga Labs",
        desc=d_en, og_title=h1_en, alternates=alt,
        jsonld=_jsonld(h1_en, d_en, "https://aisagalab.com/" + en_path, "en", "Privacy"),
        body=_head(
            "Privacy", "We asked OpenAI and Anthropic to delete our data.<br>Neither said it was gone.",
            "Five layers sit between the delete button and a conversation actually "
            "being gone. Only the first one is under your control.",
            "Saga Labs &middot; " + DATE_EN,
            "Leer en espa&ntilde;ol", "es/pedimos-a-openai-y-anthropic-que-borraran-nuestros-datos.html",
        ) + '\n        <div class="article-body">' + A4_EN_BODY
          + '</div>\n        <div class="article-body article-sources">' + A4_EN_SOURCES + '</div>',
    ))

    h1_es = "Pedimos a OpenAI y a Anthropic que borraran nuestros datos. Ninguno dijo que estuvieran borrados."
    d_es = ("Entre el bot\u00f3n de borrar y que la conversaci\u00f3n desaparezca hay cinco capas: "
            "almacenamiento, pesos del modelo, la copia del revisor, la marca de seguridad y el "
            "juzgado. Con la respuesta del equipo de privacidad de OpenAI, y la de Anthropic.")
    out.append(render(
        path=es_path, lang="es",
        title=h1_es + " — Saga Labs",
        desc=d_es, og_title=h1_es, alternates=alt,
        jsonld=_jsonld(h1_es, d_es, "https://aisagalab.com/" + es_path, "es", "Privacidad"),
        body=_head(
            "Privacidad", "Pedimos a OpenAI y a Anthropic que borraran nuestros datos.<br>Ninguno dijo que estuvieran borrados.",
            "Entre el bot&oacute;n de borrar y que la conversaci&oacute;n desaparezca de "
            "verdad hay cinco capas. Solo la primera depende de ti.",
            "Saga Labs &middot; " + DATE_ES,
            "Read in English", "../we-asked-openai-and-anthropic-to-delete-our-data.html",
        ) + '\n        <div class="article-body">' + A4_ES_BODY
          + '</div>\n        <div class="article-body article-sources">' + A4_ES_SOURCES + '</div>',
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

<h2>We asked both companies directly</h2>

<p>In September 2026 we did the obvious experiment. Using our own accounts, we
asked OpenAI and Anthropic to delete the data associated with us, and we kept the
replies. Both answered within a day, both were polite, and neither did anything
wrong. That is what makes the answers useful.</p>

<p>OpenAI's privacy team replied with instructions rather than a confirmation,
and with one qualifier worth isolating:</p>

<blockquote>We acknowledge receipt of your request to delete any data associated
with you processed by OpenAI, but keep your OpenAI account. For security and
privacy reasons, the quickest way to delete <strong>data that is not necessary to
maintain your account or our services</strong>, while keeping your ChatGPT account
active, is to use our self-service tools outlined below.</blockquote>

<p>Read the clause we emphasised. The self-service tools cover data that is
<em>not necessary to maintain the account or the service</em>. That phrasing
implies a second category &mdash; data that is necessary &mdash; and the reply
does not say what is in it, how large it is, or how long it lasts. The answer to
&ldquo;delete everything about me&rdquo; was a link to a Delete all chats
button.</p>

<p>Anthropic's reply was more specific, and lands on a qualifier of its own:</p>

<blockquote>When you delete a conversation it will be removed from your chat
history immediately, and deleted from our back-end storage systems within 30 days
<strong>in accordance with our retention periods</strong>. […] When you choose to
delete your account, your personal data connected to your account will also be
deleted <strong>in accordance with our retention periods</strong>.</blockquote>

<p>&ldquo;In accordance with our retention periods&rdquo; is not an answer to the
question; it is a pointer back to the question. Those periods are the ones earlier
in this article: 30 days for ordinary storage, up to two years for a flagged
conversation, up to five years for de-identified training data, up to seven years
for a safety classification score. Deleting your account does not reset those
clocks &mdash; it hands you to them.</p>

<p>The same reply added something most people have never considered:</p>

<blockquote>if you are accessing Claude through a third party service (e.g.
Quora's Poe or Cursor), you will need to request account deletion through that
third party service provider.</blockquote>

<p>Which means that deleting your account at the model provider does not delete
the copies held by whatever else you piped it through, and you are expected to
know the list.</p>

<p>Neither company was evasive. Both replied faster than most companies would.
The point is narrower: <strong>we asked two of the most sophisticated privacy
teams in the industry whether our data was gone, and neither said yes.</strong>
Not because they were hiding something, but because &ldquo;yes&rdquo; is not a
thing either of them is in a position to say.</p>

<p class="article-note">The two replies are quoted verbatim except that we removed
the support agents' names. They answered their tickets correctly and should not be
identifiable from this page.</p>

<h2>What deletion means somewhere else</h2>

<p>For contrast, consider what &ldquo;delete&rdquo; means for a file on your own
machine. The operating system unlinks it. There is no thirty-day window, no
reviewer's copy, no training pipeline, and no third party who could be ordered to
produce it, because no third party ever had it.</p>

<p>That is not a claim about anyone's trustworthiness. It is a claim about how
many parties are involved. Five of the layers above exist because the conversation
travelled somewhere. A conversation that never leaves the device has one layer.</p>

<h2>Where this leaves you</h2>

<p>None of this is an argument for abandoning cloud assistants. They are better
at almost everything, and for most of what people use them for, the retention
question is not worth the trade. It is an argument for one narrower habit:
knowing which of your conversations you would mind someone reading, and treating
those differently from the rest.</p>

<p>For those, the only arrangement in which none of the five layers exists is a
model that runs on hardware you own. That is the problem we work on:
<a href="%s">Pinku</a> runs language models on an iPhone or a Mac without an
account or a network connection, and <a href="%s">Keeper</a> keeps photos and
files encrypted on the device.</p>

<p class="article-note">Every figure in this article is quoted from a provider's
own published policy or a court filing, all linked below. Check them rather than
taking our word for it &mdash; and if one is out of date,
<a href="mailto:sagalabs@proton.me">tell us</a> and we will correct the page.</p>
""" % (APP_STORE, KEEPER)

A4_EN_SOURCES = """
<h2>Sources</h2>
<ul>
<li><a href="https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data" rel="nofollow noopener" target="_blank">How long do you store my data?</a> &mdash; Anthropic Privacy Center, updated 1 July 2026. The 30-day, 2-year, 5-year and 7-year windows.</li>
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

<h2>Se lo preguntamos a las dos empresas</h2>

<p>En septiembre de 2026 hicimos el experimento obvio. Desde nuestras propias
cuentas, pedimos a OpenAI y a Anthropic que borraran los datos asociados a
nosotros, y guardamos las respuestas. Las dos contestaron en menos de un
d&iacute;a, las dos fueron correctas, y ninguna hizo nada mal. Eso es justo lo que
hace &uacute;tiles las respuestas.</p>

<p>El equipo de privacidad de OpenAI respondi&oacute; con instrucciones en vez de
con una confirmaci&oacute;n, y con una coletilla que merece aislarse:</p>

<blockquote>Acusamos recibo de tu solicitud de borrar cualquier dato asociado a ti
procesado por OpenAI, manteniendo tu cuenta. Por motivos de seguridad y
privacidad, la forma m&aacute;s r&aacute;pida de borrar <strong>los datos que no
son necesarios para mantener tu cuenta o nuestros servicios</strong>, conservando
la cuenta de ChatGPT activa, es usar nuestras herramientas de
autoservicio.</blockquote>

<p>Lee la cl&aacute;usula que hemos destacado. Las herramientas de autoservicio
cubren los datos que <em>no son necesarios para mantener la cuenta o el
servicio</em>. Esa formulaci&oacute;n implica una segunda categor&iacute;a &mdash;
los que s&iacute; lo son &mdash; y la respuesta no dice qu&eacute; hay dentro,
cu&aacute;nto ocupa ni cu&aacute;nto dura. La respuesta a &laquo;borrad todo lo
m&iacute;o&raquo; fue un enlace a un bot&oacute;n de borrar todos los chats.</p>

<p>La de Anthropic fue m&aacute;s concreta, y aterriza en una coletilla
propia:</p>

<blockquote>Cuando borras una conversaci&oacute;n se elimina de tu historial de
inmediato, y de nuestros sistemas de almacenamiento en 30 d&iacute;as
<strong>de acuerdo con nuestros plazos de retenci&oacute;n</strong>. […] Cuando
eliges borrar tu cuenta, tus datos personales vinculados a ella tambi&eacute;n se
borran <strong>de acuerdo con nuestros plazos de retenci&oacute;n</strong>.</blockquote>

<p>&laquo;De acuerdo con nuestros plazos de retenci&oacute;n&raquo; no es una
respuesta a la pregunta: es un puntero de vuelta a la pregunta. Esos plazos son
los de antes en este art&iacute;culo: 30 d&iacute;as de almacenamiento normal,
hasta dos a&ntilde;os si la conversaci&oacute;n se marc&oacute;, hasta cinco
a&ntilde;os de datos anonimizados de entrenamiento, hasta siete a&ntilde;os de
puntuaci&oacute;n de seguridad. Borrar la cuenta no reinicia esos relojes: te
entrega a ellos.</p>

<p>La misma respuesta a&ntilde;ad&iacute;a algo en lo que casi nadie ha
pensado:</p>

<blockquote>si accedes a Claude a trav&eacute;s de un servicio de terceros (por
ejemplo Poe de Quora o Cursor), tendr&aacute;s que solicitar el borrado de la
cuenta a ese proveedor.</blockquote>

<p>Es decir: borrar tu cuenta en el proveedor del modelo no borra las copias que
tenga aquello por lo que lo canalizaste, y se da por hecho que t&uacute; te sabes
la lista.</p>

<p>Ninguna de las dos empresas fue evasiva. Contestaron m&aacute;s r&aacute;pido
de lo que contesta la mayor&iacute;a. El punto es m&aacute;s estrecho:
<strong>preguntamos a dos de los equipos de privacidad m&aacute;s competentes del
sector si nuestros datos estaban borrados, y ninguno dijo que s&iacute;.</strong>
No porque escondieran nada, sino porque &laquo;s&iacute;&raquo; no es algo que
ninguno de los dos est&eacute; en posici&oacute;n de decir.</p>

<p class="article-note">Las dos respuestas est&aacute;n citadas literalmente salvo
que hemos quitado los nombres de los agentes de soporte. Atendieron sus tickets
correctamente y no deber&iacute;an ser identificables desde esta p&aacute;gina.
La de OpenAI est&aacute; traducida del ingl&eacute;s.</p>

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

<p>Nada de esto es un argumento para dejar los asistentes en la nube. Son mejores
en casi todo, y para la mayor parte de lo que la gente hace con ellos, la
cuesti&oacute;n de la retenci&oacute;n no compensa el cambio. Es un argumento
para una costumbre m&aacute;s estrecha: saber cu&aacute;les de tus conversaciones
te importar&iacute;a que alguien leyera, y tratarlas distinto que al resto.</p>

<p>Para esas, la &uacute;nica disposici&oacute;n en la que no existe ninguna de
las cinco capas es un modelo que corre en hardware tuyo. Es el problema en el que
trabajamos: <a href="%s">Pinku</a> ejecuta modelos de lenguaje en un iPhone o un
Mac sin cuenta y sin conexi&oacute;n, y <a href="%s">Keeper</a> mantiene fotos y
archivos cifrados en el dispositivo.</p>

<p class="article-note">Toda cifra de este art&iacute;culo est&aacute; citada de la
pol&iacute;tica publicada por el proveedor o de una resoluci&oacute;n judicial,
enlazadas abajo. Compru&eacute;balas en vez de creernos &mdash; y si alguna
est&aacute; desactualizada, <a href="mailto:sagalabs@proton.me">av&iacute;sanos</a>
y corregimos la p&aacute;gina.</p>
""" % (APP_STORE, KEEPER)

A4_ES_SOURCES = A4_EN_SOURCES.replace("<h2>Sources</h2>", "<h2>Fuentes</h2>").replace(
    "<p>Checked on 5 September 2026.</p>", "<p>Comprobado el 5 de septiembre de 2026.</p>")
