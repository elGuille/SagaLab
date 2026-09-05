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
theoretical, and it is the subject of
an article of its own, which we are still writing: in the
copyright litigation brought by The New York Times, a court ordered OpenAI to
preserve output logs that would otherwise have been deleted.</p>

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
excepci&oacute;n no es te&oacute;rica, y tiene
art&iacute;culo propio, que estamos escribiendo:
en el pleito de derechos de autor del New York Times, un tribunal orden&oacute; a
OpenAI conservar registros que de otro modo se habr&iacute;an borrado.</p>

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

    return out
