# -*- coding: utf-8 -*-
"""Texto en espanol del articulo «keep» (nuevo el 30 oct 2026, misma version que el ingles). Ver privacy_oct20.py."""

DISCLOSE = ("<p>Transparencia: Saga Labs, que publica esta web, también hace Pinku. Se describe con el mismo tipo "
            "de datos que las demás apps: su ficha del App Store y, en la prueba de red, lo que medimos.</p>")

PINKU_PRIV = ("Pinku guarda los chats en el dispositivo: no salen de él. La etiqueta de privacidad de Apple para "
              "Pinku solo lista el historial de compras y un ID anónimo, usados para Pinku Pro.")

KEEP = dict(
    h1="¿Se borran de verdad los chats de IA? Qué guardan ChatGPT, Claude, Gemini y otros (2026)",
    desc=("Qué pasa al borrar un chat en ChatGPT, Claude, Gemini, Copilot, Perplexity, Grok, DeepSeek, Mistral o Meta "
          "AI: qué desaparece de tu pantalla, qué se borra de los servidores y cuándo, qué se guarda para entrenar o "
          "por seguridad, y qué guardó una orden judicial. Según las páginas de cada empresa, comprobadas el 30 de "
          "octubre de 2026."),
    kicker="Privacidad", section="Privacidad",
    standfirst=("Al borrar un chat, desaparece de tu lista al momento. En la empresa, una copia puede quedarse 30 "
                "días, años si alguien la revisó o se usó para entrenar, o lo que diga un juez. Esto dice cada una, "
                "con enlaces."),
    body="""
<h2>La respuesta corta</h2>

<p>No enseguida, y no siempre. Al borrar un chat, todos los servicios de abajo lo quitan
de tu lista al momento. La mayoría dice que luego lo elimina de sus servidores en un
plazo de <strong>30 días</strong>. Hay tres tipos de copia que pueden durar más: los
chats guardados <strong>para entrenar</strong> (hasta 5 años en Anthropic si lo
permitiste), los guardados <strong>para revisiones de seguridad</strong> (hasta 3 años
en Google si los leyó una persona, 2 años en Anthropic si se marcaron) y los guardados
<strong>por orden judicial</strong>: de mayo a septiembre de 2025, OpenAI tuvo que
conservar los chats borrados de ChatGPT por un pleito de derechos de autor, y aún tiene
lo que guardó entonces.</p>

<h2>Borrado de tu pantalla no es borrado de los servidores</h2>

<div class="table-scroll"><table>
<thead><tr><th>Servicio</th><th>Desaparece de tu pantalla</th><th>Se borra de los servidores</th><th>Se guarda para entrenar o por seguridad</th><th>Se guarda por jueces o por ley</th></tr></thead>
<tbody>
<tr><td>ChatGPT</td><td>Al momento; no se puede recuperar, ni con soporte</td><td>En 30 días, salvo que ya estuviera desidentificado</td><td>Entrena con los chats de Free, Plus y Pro si no lo desactivas; chats temporales hasta 30 días por seguridad</td><td>La orden judicial de mayo de 2025 conservó chats borrados hasta el 26 de septiembre de 2025; OpenAI guarda lo que conservó entonces</td></tr>
<tr><td>Claude</td><td>Al momento</td><td>En 30 días</td><td>Solo si permites entrenar: hasta 5 años, desidentificado; chats marcados 2 años, sus puntuaciones de seguridad 7 años; opiniones 5 años</td><td>No consta en las páginas que leímos</td></tr>
<tr><td>Gemini</td><td>Cuando borras la actividad</td><td>Se borra sola a los 18 meses por defecto (3 o 36, o nunca); 72 horas con Keep Activity desactivado</td><td>Los chats que revisó una persona no se borran con tu actividad: hasta 3 años, desvinculados de tu cuenta</td><td>No consta en las páginas que leímos</td></tr>
<tr><td>Microsoft Copilot</td><td>Un chat o todos, cuando quieras</td><td>App antigua: 18 meses por defecto. La página de privacidad de la app nueva no da plazo</td><td>Entrena con las conversaciones si no te das de baja; algunas pasan revisión automática y humana</td><td>No consta en las páginas que leímos</td></tr>
<tr><td>Perplexity</td><td>Un hilo o todos</td><td>Datos de la cuenta en 30 días tras borrarla; archivos a los 30 días</td><td>Memory puede usarse para mejorar los modelos si no desactivas AI Data Retention</td><td>No consta en las páginas que leímos</td></tr>
<tr><td>Grok</td><td>Un chat o todos</td><td>En 30 días</td><td>Entrenar es uno de los usos que lista</td><td>Más tiempo «for legal, compliance, or safety purposes»</td></tr>
<tr><td>DeepSeek</td><td>Borra el historial en ajustes</td><td>«El tiempo necesario»; sin plazo</td><td>Se usa para entrenar; la política da derecho a oponerse</td><td>Se guarda en servidores de la República Popular China</td></tr>
<tr><td>Vibe de Mistral</td><td>Al borrarlo</td><td>«Upon manual deletion»; la cuenta, tras un breve periodo de gracia</td><td>Por defecto no estás excluido del entrenamiento</td><td>«Monitoring and legal retention purposes»</td></tr>
<tr><td>Meta AI</td><td>Borra todos los chats y medios; los vibes públicos se quedan</td><td>Sin plazo en las páginas de ayuda que leímos</td><td>Las interacciones se usan «to improve AI at Meta»</td><td>No consta en las páginas que leímos</td></tr>
</tbody>
</table></div>

<p class="article-note">De la política de privacidad y el centro de ayuda de cada empresa,
leídos el %(date)s. Los enlaces y la fecha de cada página están en las fuentes, al final.
«No consta» quiere decir que lo buscamos en esas páginas y no lo encontramos, no que la
empresa nunca guarde nada por esos motivos.</p>

<h2>ChatGPT (OpenAI)</h2>

<p>La página de conservación de OpenAI (actualizada el 29 de octubre de 2026) dice que
los chats normales y archivados «remain saved to your account until you delete them» o
hasta que los elimine una política de conservación del espacio de trabajo. Al borrar
uno, ChatGPT lo quita de la vista al momento y OpenAI «schedules it for permanent
deletion from its systems within 30 days», salvo que ya estuviera desidentificado y
desvinculado de tu cuenta, o que OpenAI deba guardarlo más tiempo por seguridad u
obligaciones legales. No puedes recuperar un chat borrado, «in ChatGPT or through OpenAI
Support». Un chat temporal no sale en tu historial, pero OpenAI «may keep a copy for up
to 30 days for safety purposes». Borrar un chat no borra un archivo que guardaste aparte
en Library o en un Space.</p>

<p>Sobre el entrenamiento, OpenAI dice que en Free, Plus y Pro «may use your content to
train our models». Aunque te des de baja, si pulsas el pulgar arriba o abajo, «the entire
conversation associated with that feedback may be used to train our models».</p>

<p><strong>Ajustes:</strong> desactiva el entrenamiento en Settings, Data controls,
<em>Improve the model for everyone</em> (o <em>Do not train on my content</em> en el
Privacy Portal). Para un chat temporal, abre un chat nuevo y elige <em>Temporary</em>.
Borra un chat desde su menú &bull;&bull;&bull;, Delete; todos, en Settings, Data controls,
<em>Delete all chats</em>. Exporta en Settings, Data controls, Export: el enlace puede
tardar hasta 7 días y caduca 24 horas después de recibirlo, y una exportación no recupera
chats ya borrados.</p>

<h2>Claude (Anthropic)</h2>

<p>La página de conservación de Anthropic (1 de julio de 2026) cubre Free, Pro y Max. Una
conversación borrada queda «removed from your chat history immediately» y «deleted from
our back-end storage systems within 30 days». Las excepciones llevan números:</p>
<ul>
<li>Si permites usar tus chats para mejorar Claude, se guardan «in a de-identified format
for up to 5 years» en los procesos de entrenamiento, y lo que ya esté en un entrenamiento
terminado o en curso se queda ahí.</li>
<li>Conversaciones marcadas por sus sistemas de seguridad: entradas y salidas hasta 2
años, y las puntuaciones de clasificación hasta 7 años.</li>
<li>Las opiniones que envías (pulgar arriba o abajo): 5 años.</li>
<li>Los chats de incógnito no se guardan en tu historial ni se usan para entrenar, pero se
conservan 30 días por defecto.</li>
</ul>
<p><strong>Ajustes:</strong> solo entrena si activas <em>Help improve our AI models</em> en
Settings, Privacy. Abre un chat de incógnito con el icono del fantasma, arriba a la
derecha. Borra un chat desde su menú &#8942;, o marca varios y usa <em>Select all</em>.
Exporta desde Settings, Privacy en la web o la app de escritorio (no desde la app de
iPhone o Android); el enlace caduca 24 horas después de la entrega.</p>

<h2>Gemini (Google)</h2>

<p>El centro de privacidad de Gemini (actualizado el 26 de octubre de 2026) dice que tu
actividad se borra sola a los <strong>18 meses</strong> por defecto, y que puedes cambiarlo
a 3 o 36 meses, o desactivar el borrado automático. Los chats temporales, y los chats con
Keep Activity desactivado, se conservan igualmente con tu cuenta <strong>72 horas</strong>,
y los temporales no se usan para entrenar los modelos de Google.</p>

<p>La excepción que más importa: «a subset of chats are reviewed by human reviewers», y esos
chats «are not deleted when you delete your activity»; se guardan hasta tres años,
desvinculados de tu cuenta.</p>

<p><strong>Ajustes:</strong> en Settings &amp; help, Activity, elige <em>Turn off</em> o
<em>Turn off and delete activity</em>. Abre un chat temporal con <em>Temporary chat</em>,
junto a New chat. Borra un elemento con <em>Delete activity item</em>, o todo con Delete,
<em>All time</em>. Exporta con Google Takeout (My Activity, Gemini Apps); el enlace del
correo funciona 7 días.</p>

<h2>Microsoft Copilot</h2>

<p>La página de preguntas sobre privacidad de Copilot dice: «By default, we store conversation
activity for 18 months. You can delete individual conversations or your entire conversation
history at any time.» Desde que la leímos por primera vez, Microsoft ha añadido que el
artículo «applies only to the older version of the Microsoft Copilot app». La página de
privacidad de la app nueva no da un plazo, así que no podemos decirte cuánto guarda los
chats la app nueva. Algunas conversaciones pasan revisión automática y humana, y puedes darte de baja: «You can opt out
of use of your conversation activity for model training at any time».</p>

<p><strong>Ajustes (app antigua):</strong> Privacy, <em>Training on conversation activity</em>
y <em>Training on voice conversations</em>. Borra una conversación desde los tres puntos que
tiene al lado, o todas con <em>Delete all activity history</em>. No encontramos un modo de
chat temporal en las páginas de Microsoft.</p>

<h2>Perplexity, Grok, DeepSeek, Mistral y Meta AI</h2>

<ul>
<li><strong>Perplexity</strong> guarda la información personal «as long as your account is
active». Si borras la cuenta, se elimina de sus servidores en 30 días, y volver a entrar antes
cancela el borrado. Puedes borrar hilos uno a uno o todos (los &hellip; junto a la pestaña de
hilos, <em>Delete sessions</em>); los archivos subidos se guardan 30 días por defecto. El
contenido de Memory puede usarse para mejorar sus modelos si no desactivas <em>AI Data
Retention</em> en Settings, Preferences, Artificial Intelligence, y puede guardar un registro
de los recuerdos borrados hasta 30 días.</li>
<li><strong>Grok</strong> (xAI, ahora SpaceXSI; política del 27 de octubre de 2026): los chats
privados, los borrados y las cuentas eliminadas se borran en 30 días «unless it is necessary
to retain the data for legal, compliance, or safety purposes». Entrenar es uno de los usos que
lista. Su FAQ da los ajustes: Settings, Data Controls, <em>Improve the model</em>; el icono del
fantasma, arriba a la derecha, para un chat privado; y Settings, Data Controls, <em>Delete All
Conversations</em>.</li>
<li><strong>DeepSeek</strong> (política del 10 de febrero de 2026) guarda los datos personales
el tiempo necesario, los usa para entrenar y mejorar su tecnología, da derecho a oponerse y los
guarda en servidores de la República Popular China. Puedes borrar tu historial en ajustes;
borrar la cuenta no tiene vuelta atrás y no da plazo de borrado. DeepSeek no tiene páginas de
ayuda con los pasos.</li>
<li><strong>Vibe de Mistral</strong> (antes Le Chat): las conversaciones «are removed from our
systems upon manual deletion» o al borrar la cuenta, normalmente tras un breve periodo de gracia,
con conservación para supervisión y fines legales. Los usuarios «are not opted out by default» del
entrenamiento: en el móvil, el ajuste es <em>Enable data sharing</em>; en la web, <em>Allow your
interactions to be used to train our models</em>.</li>
<li><strong>Meta AI</strong>: Settings, Data &amp; privacy, Manage your information, <em>Delete
all chats and media</em>; los vibes públicos no se borran con ellos. La misma página dice que
Meta usa tus interacciones con sus IA «to improve AI at Meta», y que cuando no saben contestar,
Meta comparte tus mensajes y datos generales, como tu región, con socios seleccionados. Puedes
exportar tu información desde Accounts Center. No encontramos un plazo de conservación de los
chats.</li>
</ul>

<h2>Cuatro veces en que los chats se guardaron o se expusieron igualmente</h2>

<h3>Un juez ordenó a OpenAI guardar los chats borrados (2025)</h3>
<p>En el pleito de derechos de autor del New York Times, la jueza Ona Wang ordenó a OpenAI el
13 de mayo de 2025 «preserve and segregate all output log data that would otherwise be deleted»,
«whether such data might be deleted at a user's request» o por leyes de privacidad. OpenAI dice
que afectaba a ChatGPT Free, Plus, Pro y Team y a la API sin acuerdo de conservación cero, no a
Enterprise ni a Edu. Una orden acordada del 9 de octubre de 2025 puso fin a la obligación «as of
September 26, 2025». OpenAI conserva lo que ya había guardado, salvo los datos del Espacio
Económico Europeo, Suiza y el Reino Unido, y sigue conservando los chats de las cuentas ligadas a
los dominios que listaron los periódicos. La página de OpenAI dice que «will securely store limited
historical April&ndash;September 2025 user data». El pleito sigue abierto; no hemos encontrado
cambios en esas condiciones desde entonces.</p>

<h3>Italia limitó ChatGPT y multó a OpenAI (2023 y 2024)</h3>
<p>El 30 de marzo de 2023, la autoridad italiana de protección de datos, el Garante, ordenó una
limitación temporal e inmediata del tratamiento por ChatGPT de los datos de las personas en Italia,
y el 11 de abril fijó las condiciones para levantarla, a cumplir antes del 30 de abril de 2023. El
20 de diciembre de 2024 multó a OpenAI con quince millones de euros, entre otros motivos por no
notificar la brecha de marzo de 2023, entrenar sin base jurídica, falta de transparencia y no
comprobar la edad. La página del Garante dice ahora que, tras estimar el Tribunal de Roma el recurso
de OpenAI en una sentencia publicada el 18 de marzo de 2026, la decisión se ha retirado
temporalmente de su web.</p>

<h3>Un fallo de ChatGPT mostró títulos de chats de otras personas (marzo de 2023)</h3>
<p>OpenAI escribió que un fallo «allowed some users to see titles from another active user's chat
history», y expuso datos de pago del 1,2 %% de los suscriptores de ChatGPT Plus activos durante un
periodo de nueve horas; los números completos de tarjeta no quedaron expuestos.</p>

<h3>Una base de datos de DeepSeek quedó abierta en internet (enero de 2025)</h3>
<p>Wiz Research encontró una base de datos de DeepSeek accesible sin contraseña, con «over a million
lines of log streams containing chat history, secret keys, backend details»; DeepSeek la cerró
enseguida al avisarle. Al día siguiente, el 30 de enero de 2025, el Garante ordenó con urgencia
limitar el tratamiento de los datos de los usuarios en Italia por parte de DeepSeek.</p>

<h2>Nunca pegues contraseñas, claves de API ni números de tarjeta</h2>

<p>Lo dicen las propias empresas. OpenAI: «Please don't share any sensitive information in your
conversations.» Google: «Please don't enter confidential information that you wouldn't want a
reviewer to see or Google to use to improve our services», y «Don't enter login or payment information
into Gemini chats». Microsoft: «You shouldn't provide any confidential or sensitive personal data».
xAI: «please do not share any personal or sensitive information in your questions to Grok.» El Centro
Nacional de Ciberseguridad del Reino Unido recomienda «not to include sensitive information in queries
to public LLMs».</p>

<p>Los motivos están arriba: un chat borrado puede quedarse hasta 30 días, uno revisado hasta tres
años, un juez puede congelar el borrado y una filtración expone lo que haya en los registros. Si ya
pegaste una contraseña o una clave en un chatbot, borrar el chat no basta: cambia la contraseña o
revoca la clave.</p>

<h2>Chatbots populares en ruso y en chino</h2>

<ul>
<li><strong>Alice (Yandex)</strong>: sin la opción de pago, el historial se guarda 14 días; con Alice
Plus, sin límite. Borras un chat desde el historial, y los datos por categoría desde la página de
gestión de datos de Yandex ID, que avisa de que algunos se guardan más tiempo porque lo exige la ley.
Yandex ID también permite pedir un archivo con tus datos.</li>
<li><strong>GigaChat (Sber)</strong>: el acuerdo que leímos (6 de febrero de 2026) no da un plazo de
conservación de las conversaciones.</li>
<li><strong>Doubao (ByteDance)</strong>: guarda la información personal solo el tiempo necesario para
dar el servicio y almacena en China lo recogido en China. Puedes borrar conversaciones sueltas y la
cuenta. La política dice que usa tus entradas y respuestas para mejorar sus modelos, y un ajuste de
privacidad lo desactiva. Lista derechos de consulta, copia y borrado, sin botón de exportar.</li>
<li><strong>Kimi (Moonshot AI)</strong>: guarda la información personal en China. Puedes borrar
conversaciones y la cuenta. No hay ajuste de entrenamiento: contactas con soporte y, tras verificar tu
identidad, dejan de usar tu contenido para entrenar.</li>
</ul>

<h2>Lo que conseguí con una solicitud formal</h2>

<p>El 15 de abril de 2026 envié a OpenAI y a Anthropic una solicitud formal de RGPD desde mis cuentas
personales: pedí, por el artículo 15, todo lo que tuvieran, incluidas las marcas de seguridad y los datos
derivados de mis chats, y, por el artículo 17, el borrado, con confirmación escrita de lo eliminado y la
base legal de lo conservado. Anthropic acusó recibo automáticamente el mismo día. OpenAI contestó el 17 de
abril; la respuesta humana de Anthropic llegó el 16 de mayo, un mes y un día después. El RGPD da un mes
para responder (artículo 12, apartado 3).</p>

<p>Las dos respuestas fueron educadas y remitían a herramientas de autoservicio. Ninguna confirmó por
escrito qué se había borrado, ninguna dio la base legal de lo conservado y ninguna respondió a la
solicitud de acceso con los datos. No lo llevé a una autoridad de protección de datos, así que no hay nada
decidido. El intercambio completo, con citas, está en
<a href="%(gdpr)s">Envié a OpenAI y Anthropic una solicitud de borrado RGPD</a>.</p>

<h2>Cómo dejar una conversación fuera de todo esto</h2>

<ol>
<li><strong>Antes de escribir</strong>, desactiva el entrenamiento (ChatGPT, Copilot, Grok, Mistral, Memory
de Perplexity, Doubao) o déjalo desactivado (Claude). No pulses el pulgar arriba o abajo en chats que te
importen: en ChatGPT, Claude y Mistral, las opiniones tienen sus propias reglas.</li>
<li><strong>Usa chats temporales o de incógnito</strong> para preguntas delicadas, y recuerda que se guardan
un tiempo: hasta 30 días en ChatGPT, Claude y Grok, 72 horas en Gemini.</li>
<li><strong>Borra lo que no necesites</strong>, y exporta antes si quieres una copia: una exportación no
recupera chats ya borrados.</li>
<li><strong>No metas secretos en ningún chat</strong>: contraseñas, claves de API, números de tarjeta y de
documentos.</li>
</ol>

<h2>Cuándo tiene sentido un modelo en tu propio dispositivo</h2>

<p>Ningún chatbot en la nube de los de arriba promete no guardar nada: borrar lleva tiempo, hay excepciones,
y un juez o una filtración pueden saltarse ambas cosas. Un modelo que funciona en tu dispositivo lo evita en
las conversaciones donde importa (salud, dinero, documentos de trabajo, lo que no querrías que leyera un
revisor), porque el texto nunca llega a un servidor. A cambio, el modelo es más pequeño: sabe menos, se equivoca
más y no busca en internet, así que sirve para redactar en privado, resumir y preguntar, no para investigar.</p>

<p>En un ordenador, herramientas como Ollama o LM Studio ejecutan modelos abiertos; en un iPhone o Mac, apps como
Locally AI, PocketPal AI y Private LLM, y también <a href="%(pinku)s">Pinku</a>, que hacemos nosotros.
%(pinku_priv)s Probamos qué envían realmente estas apps a internet en un Mac
(<a href="%(p_net)s">resultados, en inglés</a>) y a qué velocidad van los modelos pequeños en un iPhone
(<a href="%(speed)s">velocidades</a>).</p>
""",
    faq=[
        ("¿Se borran de verdad los chats de ChatGPT?",
         "Desaparecen de tu cuenta al momento y no se pueden recuperar. OpenAI dice que los elimina de sus sistemas en "
         "30 días, salvo que ya estuvieran desidentificados o deba guardarlos por seguridad u obligaciones legales. Los "
         "chats borrados que se guardaron por la orden judicial de mayo a septiembre de 2025 siguen guardados."),
        ("¿OpenAI sigue obligada a guardar mis chats borrados de ChatGPT?",
         "Los nuevos, no. La obligación terminó el 26 de septiembre de 2025. OpenAI conserva lo que guardó antes de esa "
         "fecha, salvo los datos del Espacio Económico Europeo, Suiza y el Reino Unido, y sigue conservando los chats de "
         "las cuentas ligadas a dominios que listó el New York Times."),
        ("¿Cuánto guarda Claude mis chats después de borrarlos?",
         "Anthropic dice que un chat borrado sale de tu historial al momento y de sus servidores en 30 días. Los chats "
         "marcados por sus sistemas de seguridad se guardan hasta 2 años (las puntuaciones, hasta 7), y los usados para "
         "entrenar con tu permiso, hasta 5 años, desidentificados."),
        ("¿Borrar la actividad de Gemini borra los chats que revisó una persona?",
         "No. Google dice que los chats revisados no se borran al borrar tu actividad; se guardan hasta tres años, "
         "desvinculados de tu cuenta."),
        ("¿Un chat temporal o de incógnito se guarda en algún sitio?",
         "Sí, un tiempo: hasta 30 días en ChatGPT y Grok, 30 días por defecto en Claude y 72 horas en Gemini."),
        ("¿Es seguro pegar una contraseña o una clave de API en ChatGPT?",
         "No. OpenAI, Google, Microsoft y xAI piden no compartir información sensible, y los chats borrados pueden seguir "
         "en sus servidores semanas o más. Si ya lo hiciste, cambia la contraseña o revoca la clave."),
        ("¿Qué chat de IA no guarda mis conversaciones?",
         "Ningún chatbot en la nube de esta lista lo promete. Un modelo que funciona en tu dispositivo, como Ollama o LM "
         "Studio en un ordenador, o Locally AI, PocketPal AI, Private LLM o Pinku en iPhone o Mac, deja la conversación en "
         "el dispositivo."),
    ],
    sources=None,  # las fuentes son las mismas que en ingles: ver abajo
)

_S = __import__("privacy_en").KEEP["sources"]
for _en, _es in [
    ("<h2>Sources</h2>", "<h2>Fuentes</h2>"),
    ("First published on 20 October 2026; every page re-read on %(date)s. Policies\nchange; if one of these is out of date, <a href=\"mailto:sagalabs@proton.me\">tell\nus</a> and we will correct the page.",
     "Publicado el 20 de octubre de 2026 en inglés; todas las páginas se releyeron el %(date)s. Las políticas\ncambian; si alguna está desfasada, <a href=\"mailto:sagalabs@proton.me\">avísanos</a> y corregiremos la página. Las fechas de la lista están en inglés, como en cada página."),
]:
    assert _en in _S, _en
    _S = _S.replace(_en, _es)
_i = _S.index("<p>Transparency:")
KEEP["sources"] = _S[:_i] + DISCLOSE

ARTICLES = {"keep": KEEP}
for _a in ARTICLES.values():
    _a["body"] = _a["body"].replace("%(pinku_priv)s", PINKU_PRIV)
