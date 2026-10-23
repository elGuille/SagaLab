# -*- coding: utf-8 -*-
"""Cinco guias mas (23 oct 2026, tarde), EN + ES, con la plantilla de guides.py.

Cada una lleva un dato de primera mano, comprobado el 23 oct 2026 y dicho en la pagina:
- Photo Vault (DNI/pasaporte): codigo de la app (MediaFileManager.swift: clase de
  proteccion completeUnlessOpen y isExcludedFromBackup en la boveda), 1.2.10 en venta.
- Photo Vault (album Oculto): support.apple.com 104987 (16 mar 2026), guia
  iphb4defbde9 (Oculto y Eliminado bloqueados, Use Face ID/Touch ID/Passcode) y
  102651 (Fotos de iCloud: claves en Apple salvo Proteccion de datos avanzada).
- Pinku (avion/viaje): models.json de la app (v1.1, catalogo del 19 oct): de 0,4 a
  4,7 GB, Gemma 3 1B 0,8 GB por defecto. Ficha de Traductor de Apple (modo en el
  dispositivo) y de Google Translate, Locally AI, PocketPal, Enclave, Private LLM.
- Drop (bebe): PubMed 24590753 (Hugh 2014, Pediatrics), 2405784 (Spencer 1990),
  CHOP 6 abr 2014 (mas de 200 cm), healthychildren.org (sueno seguro, 11 sep 2026);
  temporizador de Drop en el codigo (SleepTimer: 15, 30, 45, 60 min, 2 h, 8 h o sin
  fin; 30 s de fundido). 53 sonidos y 9 sin suscripcion son de la 2.10 (en revision).
- Crypton: etiquetas de privacidad de 7 apps leidas de apps.apple.com (JSON
  serialized-server-data); codigo de Crypton 2.0.7 (widgets Coin List y Portfolio,
  cuenta opcional con Apple o Google, copia de la cartera en iCloud). Sin alertas en 2.0.7.
De nuestras apps: sin precios y sin la palabra «free/gratis». Sin rayas.
"""

D = {"en": "23 October 2026", "es": "23 de octubre de 2026"}
ISO = "2026-10-23"

PV_STORE = "https://apps.apple.com/app/apple-store/id1532670722?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
PINKU_STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
DROP_STORE = "https://apps.apple.com/app/apple-store/id1462269642?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
CRYPTON_STORE = "https://apps.apple.com/app/apple-store/id1143691286?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


HIDDEN = "https://support.apple.com/en-us/104987"
HIDDEN_ES = "https://support.apple.com/es-es/104987"
HIDE_GUIDE = "https://support.apple.com/guide/iphone/hide-photos-and-videos-iphb4defbde9/ios"
HIDE_GUIDE_ES = "https://support.apple.com/es-es/guide/iphone/iphb4defbde9/ios"
ICLOUD_SEC = "https://support.apple.com/en-us/102651"
ICLOUD_SEC_ES = "https://support.apple.com/es-es/102651"
NOTES_LOCK = "https://support.apple.com/en-us/102537"
NOTES_LOCK_ES = "https://support.apple.com/es-es/102537"
PRIV_REPORT = "https://support.apple.com/en-us/102188"
PRIV_REPORT_ES = "https://support.apple.com/es-es/102188"
PV_AS = "https://apps.apple.com/us/app/id1532670722"

# --------------------------------------------------------------------------
# Photo Vault: fotos del DNI, pasaporte y tarjetas
# --------------------------------------------------------------------------

PV4_EN = dict(
    path="photo-vault/protect-photos-of-id-passport-cards-iphone.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="How to protect photos of your ID, passport and cards on iPhone (2026)",
    desc=("Where a photo of your passport, ID or bank card ends up on an iPhone (library, iCloud, apps with photo "
          "access), and four real ways to keep it safer: Hidden album, a locked note, a vault app or a password "
          "manager. With Apple's own documentation, checked 23 October 2026."),
    section="Guides", kicker="Photo Vault guide",
    standfirst=("A photo of your passport sitting in the camera roll is in every place your camera roll goes. "
                "Decide where it should live, move it there, and delete the copies you forgot about."),
    tools=["iPhone Photos", "Notes", "a photo vault app"],
    intro=f"""
<p><strong>We make Photo Vault, one of the options on this page.</strong> The built-in options
come first, and for many people they are enough.</p>

<h2>Where that photo actually is</h2>

<p>When you take a picture of your ID to send to a landlord, a hotel or a bank, it lands in
the Photos library like any other photo. That means:</p>
<ul>
<li><strong>Anyone who opens your unlocked phone</strong> can scroll to it, and it can show up in
Memories, search and the Photos widget.</li>
<li><strong>With iCloud Photos on, it is in iCloud too.</strong> Apple's iCloud security overview
({a(ICLOUD_SEC, "Apple, 102651")}) lists Photos among the data that is end-to-end encrypted only
when you turn on Advanced Data Protection. With the default, standard data protection, the
encryption keys are kept in Apple's data centres.</li>
<li><strong>Apps you gave full photo access</strong> can read your whole library, not only the
photos you picked.</li>
</ul>

<h2>Four places it can live instead</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Option</th><th>What it does</th><th>Limits</th></tr></thead>
<tbody>
<tr><td>Hidden album (built in)</td><td>Takes the photo out of the Library, other albums and the widget; locked with Face ID, Touch ID or your passcode since iOS 16 ({a(HIDDEN, "Apple, 104987")})</td><td>Still in your library and, with iCloud Photos, in iCloud; your iPhone passcode opens it</td></tr>
<tr><td>Locked note in Notes (built in)</td><td>Notes can lock a note with your iPhone passcode or a separate notes password ({a(NOTES_LOCK, "Apple, 102537")})</td><td>Not a photo viewer; a note synced to iCloud is in iCloud</td></tr>
<tr><td>A photo vault app such as <a href="{PV_STORE}">Photo Vault</a></td><td>Keeps its own copy outside the library, behind its own lock</td><td>You must delete the original yourself; backups are your job (details below)</td></tr>
<tr><td>Your password manager, if it stores files</td><td>Keeps the document next to the logins it belongs to</td><td>Depends on the manager and plan; check what it says about attachments</td></tr>
</tbody>
</table>
</div>

<h2>What we checked in Photo Vault's code</h2>

<p>We read the storage code of the version on sale today (1.2.10). Every file in the vault gets
the iOS Data Protection class <em>completeUnlessOpen</em>, which means the file cannot be read
while the iPhone is locked, and the vault folders are marked <em>excluded from backup</em>, so
they do not go into regular iCloud or computer backups. Both settings are in
<code>MediaFileManager.swift</code> and covered by the app's tests. The flip side: without
Photo Vault's own backup, the photos are lost with the phone.</p>
""",
    steps=[
        ("Find every copy.",
         "In Photos, search for the document type (passport, ID, card) and scroll Recents around the date you sent "
         "it. Check Messages, Mail and WhatsApp threads where you sent it, and the Downloads folder in Files."),
        ("Keep only the ones you need.",
         "An expired passport or a card you cancelled does not need a photo. Delete those rather than hide them."),
        ("Choose where the rest live.",
         "Hidden album for the least effort, a locked note if you also keep notes about the document, or a vault "
         "app if you want it out of the library and out of iCloud Photos."),
        ("Move them, then delete the originals.",
         f"If you use a vault such as <a href=\"{PV_STORE}\">Photo Vault</a>, import the photos, then delete them in "
         "Photos: importing makes a copy. The same applies to a note."),
        ("Empty Recently Deleted.",
         f"Deleted photos stay in Recently Deleted for up to 30 days ({a(HIDE_GUIDE, 'Apple')}). Open it and delete "
         "them there too."),
        ("Next time, take the photo inside the vault.",
         "Photo Vault has its own camera; a photo taken there never touches the camera roll."),
        ("Mark what you send.",
         "When you must send a copy, use Markup in Photos to write who it is for and the date across it. A marked "
         "copy is less useful to anyone else who gets hold of it."),
        ("Limit photo access.",
         "In Settings, Privacy &amp; Security, Photos, set apps that do not need your whole library to Limited Access."),
    ],
    after=f"""
<h2>Where Photo Vault fits, and where it does not</h2>

<p>{a(PV_AS, "Photo Vault")} keeps photos and videos on the iPhone behind Face ID, Touch ID or a
passcode, with an optional password per album, so an ID album can stay closed when you open the
vault for someone. It can show a different, harmless set of photos with a decoy code (Premium),
change its home screen icon to Calculator, Notes or Weather, and there is no account. Backups are
either an exported file locked with a password you choose, or its optional iCloud copy (Premium),
end-to-end encrypted in your own iCloud.</p>

<p>It does not scan documents or import PDFs, it is iPhone only, and it relies on iOS Data
Protection rather than its own per-file encryption. If you already use a password manager that
keeps attachments, that may be the better home for ID scans.
<a href="../photo-vault-security.html">How Photo Vault protects your files</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(ICLOUD_SEC, "Apple, iCloud data security overview (102651)")}, read 23 October 2026.</li>
<li>{a(HIDDEN, "Apple, Hide photos with the Hidden album (104987)")}, published 16 March 2026.</li>
<li>{a(HIDE_GUIDE, "Apple, Delete or hide photos and videos on iPhone")} and {a(NOTES_LOCK, "How to lock notes (102537)")}, read 23 October 2026.</li>
<li>Photo Vault 1.2.10 source code (storage and backup), read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Is it safe to keep a photo of my passport on my iPhone?",
         "It is as safe as the places that photo reaches. In the camera roll it is visible to anyone using your "
         "unlocked phone, to apps with full photo access and, with iCloud Photos, in iCloud. Keep only what you need "
         "and move it somewhere locked."),
        ("Are iCloud Photos end-to-end encrypted?",
         "Only with Advanced Data Protection turned on. Apple's iCloud security overview says that with standard data "
         "protection, the default, the keys are kept in Apple's data centres."),
        ("Is the Hidden album enough for ID photos?",
         "It hides them from the library and locks them with Face ID, Touch ID or your passcode, but they stay in "
         "your library and in iCloud Photos, and anyone with your passcode can open them."),
        ("Does Photo Vault upload my ID photos?",
         "No, unless you turn on its optional iCloud copy (Premium), which is end-to-end encrypted in your own "
         "iCloud. The vault is excluded from regular backups and has no account or server."),
        ("Should I send a photo of my ID by WhatsApp or email?",
         "Only when you have to. Mark the copy with who it is for and the date, and delete it from the chat and "
         "your camera roll afterwards."),
    ],
)

PV4_ES = dict(
    path="photo-vault/es/proteger-fotos-del-dni-pasaporte-y-tarjetas-en-iphone.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="Cómo proteger las fotos del DNI, el pasaporte y las tarjetas en el iPhone (2026)",
    desc=("Dónde acaba en el iPhone una foto del pasaporte, el DNI o la tarjeta del banco (fototeca, iCloud, apps "
          "con acceso a fotos) y cuatro formas reales de guardarla mejor: álbum Oculto, nota bloqueada, app de "
          "bóveda o gestor de contraseñas. Con la documentación de Apple, revisada el 23 de octubre de 2026."),
    section="Guías", kicker="Guía de Photo Vault",
    standfirst=("Una foto del pasaporte en el carrete está en todos los sitios a los que va el carrete. Decide dónde "
                "debe vivir, llévala allí y borra las copias que habías olvidado."),
    tools=["Fotos del iPhone", "Notas", "una app de bóveda de fotos"],
    intro=f"""
<p><strong>Hacemos Photo Vault, una de las opciones de esta página.</strong> Las opciones que
trae el iPhone van primero, y para mucha gente bastan.</p>

<h2>Dónde está de verdad esa foto</h2>

<p>Cuando haces una foto del DNI para mandarla al casero, a un hotel o al banco, entra en la
fototeca como cualquier otra. Eso significa:</p>
<ul>
<li><strong>Quien abra tu móvil desbloqueado</strong> puede llegar a ella, y puede salir en
Recuerdos, en la búsqueda y en el widget de Fotos.</li>
<li><strong>Con Fotos en iCloud, también está en iCloud.</strong> La página de seguridad de
iCloud de Apple ({a(ICLOUD_SEC_ES, "Apple, 102651")}) pone Fotos entre los datos que solo se
cifran de extremo a extremo si activas la Protección de datos avanzada. Con la protección
estándar, que es la que viene, las claves se guardan en los centros de datos de Apple.</li>
<li><strong>Las apps a las que diste acceso completo a Fotos</strong> pueden leer toda la
fototeca, no solo las fotos que elegiste.</li>
</ul>

<h2>Cuatro sitios donde puede vivir</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Opción</th><th>Qué hace</th><th>Límites</th></tr></thead>
<tbody>
<tr><td>Álbum Oculto (de serie)</td><td>Saca la foto de la Fototeca, de los demás álbumes y del widget; bloqueado con Face ID, Touch ID o el código desde iOS 16 ({a(HIDDEN_ES, "Apple, 104987")})</td><td>Sigue en tu fototeca y, con Fotos en iCloud, en iCloud; el código del iPhone lo abre</td></tr>
<tr><td>Nota bloqueada en Notas (de serie)</td><td>Notas bloquea una nota con el código del iPhone o con una contraseña aparte ({a(NOTES_LOCK_ES, "Apple, 102537")})</td><td>No es un visor de fotos; una nota sincronizada con iCloud está en iCloud</td></tr>
<tr><td>Una app de bóveda como <a href="{PV_STORE}">Photo Vault</a></td><td>Guarda su propia copia fuera de la fototeca, con su propio bloqueo</td><td>Tienes que borrar tú el original; las copias de seguridad son cosa tuya (detalles abajo)</td></tr>
<tr><td>Tu gestor de contraseñas, si guarda archivos</td><td>Deja el documento junto a las cuentas a las que pertenece</td><td>Depende del gestor y del plan; mira qué dice de los adjuntos</td></tr>
</tbody>
</table>
</div>

<h2>Lo que comprobamos en el código de Photo Vault</h2>

<p>Leímos el código de almacenamiento de la versión que está hoy a la venta (1.2.10). Cada
archivo de la bóveda lleva la clase de Protección de datos de iOS <em>completeUnlessOpen</em>,
que hace que no se pueda leer con el iPhone bloqueado, y las carpetas de la bóveda están
marcadas como <em>excluidas de la copia de seguridad</em>, así que no entran en las copias
normales de iCloud ni del ordenador. Las dos cosas están en <code>MediaFileManager.swift</code>
y tienen sus pruebas en la app. La otra cara: sin la copia propia de Photo Vault, las fotos se
pierden con el móvil.</p>
""",
    steps=[
        ("Encuentra todas las copias.",
         "En Fotos, busca el tipo de documento (pasaporte, DNI, tarjeta) y repasa Recientes alrededor de la fecha en "
         "que lo mandaste. Mira también los chats de Mensajes, Mail y WhatsApp donde lo enviaste, y Descargas en Archivos."),
        ("Quédate solo con las que necesitas.",
         "Un pasaporte caducado o una tarjeta cancelada no necesitan foto. Bórralas en vez de ocultarlas."),
        ("Elige dónde viven las demás.",
         "Álbum Oculto si quieres lo más sencillo, una nota bloqueada si además apuntas cosas del documento, o una app "
         "de bóveda si quieres sacarlas de la fototeca y de Fotos en iCloud."),
        ("Muévelas y borra los originales.",
         f"Si usas una bóveda como <a href=\"{PV_STORE}\">Photo Vault</a>, importa las fotos y después bórralas en "
         "Fotos: importar hace una copia. Lo mismo con una nota."),
        ("Vacía Eliminado.",
         f"Las fotos borradas se quedan en Eliminado hasta 30 días ({a(HIDE_GUIDE_ES, 'Apple')}). Ábrelo y bórralas también ahí."),
        ("La próxima vez, haz la foto dentro de la bóveda.",
         "Photo Vault tiene su propia cámara; una foto hecha ahí nunca pasa por el carrete."),
        ("Marca lo que envías.",
         "Cuando tengas que mandar una copia, escribe encima con Marcación en Fotos para quién es y la fecha. Una copia "
         "marcada le sirve menos a cualquier otro que la consiga."),
        ("Limita el acceso a Fotos.",
         "En Ajustes, Privacidad y seguridad, Fotos, pon en Acceso limitado las apps que no necesitan toda tu fototeca."),
    ],
    after=f"""
<h2>Dónde encaja Photo Vault y dónde no</h2>

<p>{a(PV_AS, "Photo Vault")} guarda fotos y vídeos en el iPhone detrás de Face ID, Touch ID o un
código, con contraseña opcional por álbum, para que el álbum de documentos siga cerrado aunque
abras la bóveda delante de alguien. Puede enseñar otras fotos inofensivas con un código señuelo
(Premium), cambiar su icono por el de Calculadora, Notas o Tiempo, y no tiene cuenta. La copia de
seguridad es un archivo exportado con una contraseña que eliges tú o su copia opcional en iCloud
(Premium), cifrada de extremo a extremo en tu propio iCloud.</p>

<p>No escanea documentos ni importa PDF, es solo para iPhone y se apoya en la Protección de datos
de iOS, no en un cifrado propio por archivo. Si ya usas un gestor de contraseñas que guarda
adjuntos, quizá sea mejor sitio para los escaneos del DNI.
<a href="../../photo-vault-security.html">Cómo protege Photo Vault tus archivos</a> (en inglés).</p>

<h2>Fuentes</h2>
<ul>
<li>{a(ICLOUD_SEC_ES, "Apple, Resumen de la seguridad de los datos de iCloud (102651)")}, leído el 23 de octubre de 2026.</li>
<li>{a(HIDDEN_ES, "Apple, Ocultar fotos con el álbum Oculto (104987)")}, publicado el 16 de marzo de 2026.</li>
<li>{a(HIDE_GUIDE_ES, "Apple, Eliminar u ocultar fotos y vídeos en el iPhone")} y {a(NOTES_LOCK_ES, "Bloquear notas (102537)")}, leídos el 23 de octubre de 2026.</li>
<li>Código de Photo Vault 1.2.10 (almacenamiento y copia), leído el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Es seguro guardar una foto del pasaporte en el iPhone?",
         "Es tan seguro como los sitios a los que llega esa foto. En el carrete la ve cualquiera que use tu móvil "
         "desbloqueado, las apps con acceso completo a Fotos y, con Fotos en iCloud, está en iCloud. Guarda solo lo "
         "necesario y llévalo a un sitio bloqueado."),
        ("¿Fotos en iCloud está cifrado de extremo a extremo?",
         "Solo con la Protección de datos avanzada activada. Apple dice que con la protección estándar, la que viene, "
         "las claves se guardan en sus centros de datos."),
        ("¿Basta el álbum Oculto para las fotos del DNI?",
         "Las saca de la fototeca y las bloquea con Face ID, Touch ID o el código, pero siguen en tu fototeca y en "
         "Fotos en iCloud, y quien sepa tu código puede abrirlas."),
        ("¿Photo Vault sube las fotos de mi DNI?",
         "No, salvo que actives su copia opcional en iCloud (Premium), cifrada de extremo a extremo en tu propio "
         "iCloud. La bóveda queda fuera de las copias normales y no tiene cuenta ni servidor."),
        ("¿Mando la foto del DNI por WhatsApp o por correo?",
         "Solo si no queda otra. Marca la copia con para quién es y la fecha, y bórrala del chat y del carrete después."),
    ],
)

# --------------------------------------------------------------------------
# Photo Vault: es seguro el album Oculto
# --------------------------------------------------------------------------

PV5_EN = dict(
    path="photo-vault/is-iphone-hidden-album-safe.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="Is the iPhone Hidden album safe? What its lock protects, and what it does not (2026)",
    desc=("What Apple's Hidden and Recently Deleted lock actually protects, according to support.apple.com "
          "(checked 23 October 2026): who can open it, what happens with iCloud Photos, and when you need more "
          "than the Hidden album."),
    section="Guides", kicker="Photo Vault guide",
    standfirst=("Short answer: safe against someone scrolling your camera roll, not against someone who knows "
                "your passcode, and not out of iCloud. Here is exactly what Apple says it does."),
    tools=["iPhone Photos", "Settings"],
    intro=f"""
<p><strong>We make Photo Vault, a vault app, and it is one of the alternatives mentioned at
the end.</strong> For many people the Hidden album is the right answer, and this page says
when.</p>

<h2>What Apple says the Hidden album does</h2>

<p>We read Apple's own pages on 23 October 2026. In short:</p>
<ul>
<li><strong>It takes photos out of view.</strong> Hidden photos “don't appear anywhere else in
Photos, like the Library, other albums, or even the Photos widget on your Home Screen”
({a(HIDDEN, "Apple, 104987")}).</li>
<li><strong>It is locked by default.</strong> Since iOS 16 the Hidden album “is locked by default
and requires authentication to unlock”. Apple's iPhone guide says the Recently Deleted and
Hidden collections are both locked by default and unlock with “Face ID, Touch ID, or your
passcode” ({a(HIDE_GUIDE, "iPhone User Guide")}).</li>
<li><strong>You can hide the album itself.</strong> Settings, Apps, Photos, turn off Show Hidden
Album.</li>
<li><strong>It follows iCloud Photos.</strong> “If you use iCloud Photos, the photos that you hide
on one device are hidden on your other devices too.”</li>
</ul>

<h2>The limits, from the same pages</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Situation</th><th>Protected by the Hidden album?</th></tr></thead>
<tbody>
<tr><td>Someone scrolls your Library while you show a photo</td><td>Yes: hidden photos are not there, and the album asks for Face ID or Touch ID</td></tr>
<tr><td>Someone who knows your iPhone passcode</td><td>No: Apple lists the passcode as a way to unlock it</td></tr>
<tr><td>The lock was switched off</td><td>No: Settings, Apps, Photos, Use Face ID (or Touch ID or Passcode) turns it off, and anyone in your Settings can do that</td></tr>
<tr><td>Your other devices with iCloud Photos</td><td>Hidden there too, behind each device's own lock (on a Mac, Touch ID or the login password)</td></tr>
<tr><td>The copy in iCloud</td><td>It is a normal iCloud Photos item; see below</td></tr>
<tr><td>Photos you deleted instead of hiding</td><td>Kept up to 30 days in Recently Deleted, which is locked the same way</td></tr>
</tbody>
</table>
</div>

<h2>The data point most people miss: who holds the keys in iCloud</h2>

<p>Hiding does not change how a photo is stored in iCloud. Apple's iCloud security overview
({a(ICLOUD_SEC, "102651")}) puts Photos in the list of data that becomes end-to-end encrypted only
when you turn on <strong>Advanced Data Protection</strong>. With standard data protection, the
default, the data is encrypted but the keys are kept in Apple's data centres so Apple can help
with recovery. If you want hidden photos in iCloud that only your devices can decrypt, turn on
Advanced Data Protection (Settings, your name, iCloud) and read Apple's warning about recovery
first.</p>
""",
    steps=[
        ("Hide the photo.",
         f"Open it, tap the More button and choose Hide ({a(HIDDEN, 'Apple')})."),
        ("Make sure the lock is on.",
         "Settings, Apps, Photos: Use Face ID (or Use Touch ID, or Use Passcode) should be on. It covers Hidden and Recently Deleted."),
        ("Hide the album itself.",
         "In the same screen turn off Show Hidden Album, so it does not appear under Utilities."),
        ("Empty Recently Deleted.",
         "If you deleted copies or edited versions, delete them again in Recently Deleted."),
        ("Decide about iCloud.",
         "If the photos must not be readable by anyone but you in iCloud, turn on Advanced Data Protection, or keep "
         "them out of iCloud Photos altogether."),
        ("Change your passcode if others know it.",
         "The Hidden album is only as private as your iPhone passcode. A partner or child who knows it can open the album."),
        ("If that is not enough, move them out of the library.",
         f"A locked note ({a(NOTES_LOCK, 'Apple')}) can use a separate password. A vault app keeps photos in its own "
         "storage with its own lock."),
    ],
    after=f"""
<h2>When the Hidden album is enough, and when it is not</h2>

<p>It is enough when the worry is a friend scrolling your photos, a child playing with your
phone, or a photo popping up in Memories. It is not enough when someone close to you knows your
passcode, when you share an iCloud account or Mac, or when you do not want the photos in iCloud
under Apple's keys.</p>

<p>For those cases there are three common routes: a locked note with a separate notes password;
moving the photos to a computer or drive and deleting them from the phone; or a vault app. Vault
apps include Private Photo Vault, Keepsafe (Secret Photo Vault) and our {a(PV_AS, "Photo Vault")}, which keeps
photos outside the library behind its own passcode or Face ID, with an optional password per album
and a decoy code (Premium), no account, and its own optional end-to-end encrypted iCloud copy
(Premium). A vault only helps if you then delete the originals from Photos and Recently Deleted.
We compared these apps in <a href="../blog/best-photo-vault-apps-iphone.html">the best photo vault apps
for iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(HIDDEN, "Apple, Hide photos with the Hidden album (104987)")}, published 16 March 2026, read 23 October 2026.</li>
<li>{a(HIDE_GUIDE, "Apple, Delete or hide photos and videos on iPhone")}, read 23 October 2026.</li>
<li>{a(ICLOUD_SEC, "Apple, iCloud data security overview (102651)")}, read 23 October 2026.</li>
<li>{a(NOTES_LOCK, "Apple, How to lock notes (102537)")}.</li>
</ul>
""",
    faq=[
        ("Is the iPhone Hidden album safe?",
         "It hides photos from the library and, since iOS 16, locks them with Face ID, Touch ID or your passcode. It "
         "does not protect them from someone who knows your passcode, and with iCloud Photos they are in iCloud like any other photo."),
        ("Can someone open my Hidden album with my passcode?",
         "Yes. Apple lists Face ID, Touch ID or your passcode as ways to unlock the Hidden and Recently Deleted albums."),
        ("Are hidden photos uploaded to iCloud?",
         "If iCloud Photos is on, yes. Apple says photos you hide on one device are hidden on your other devices too, "
         "so they are in your iCloud library."),
        ("Are hidden photos end-to-end encrypted in iCloud?",
         "Only with Advanced Data Protection on. With standard data protection, the default, Apple keeps the keys."),
        ("Can I hide the Hidden album itself?",
         "Yes. Settings, Apps, Photos, turn off Show Hidden Album."),
        ("Is a vault app safer than the Hidden album?",
         "It can be, because the photo leaves your library and iCloud Photos and has its own lock, but only if you "
         "delete the originals and keep a backup of the vault."),
    ],
)

PV5_ES = dict(
    path="photo-vault/es/es-seguro-el-album-oculto-del-iphone.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="¿Es seguro el álbum Oculto del iPhone? Qué protege su bloqueo y qué no (2026)",
    desc=("Qué protege de verdad el bloqueo de Oculto y Eliminado de Apple, según support.apple.com (revisado el "
          "23 de octubre de 2026): quién puede abrirlo, qué pasa con Fotos en iCloud y cuándo hace falta algo más."),
    section="Guías", kicker="Guía de Photo Vault",
    standfirst=("Respuesta corta: seguro frente a alguien que repasa tu carrete, no frente a quien sabe tu código, "
                "y no fuera de iCloud. Esto es exactamente lo que Apple dice que hace."),
    tools=["Fotos del iPhone", "Ajustes"],
    intro=f"""
<p><strong>Hacemos Photo Vault, una app de bóveda, y es una de las alternativas que salen al
final.</strong> Para mucha gente el álbum Oculto es la respuesta correcta, y esta página dice
cuándo.</p>

<h2>Lo que Apple dice que hace el álbum Oculto</h2>

<p>Leímos las páginas de Apple el 23 de octubre de 2026. En resumen:</p>
<ul>
<li><strong>Quita las fotos de la vista.</strong> Las fotos ocultas no aparecen en ningún otro
sitio de Fotos, ni en la Fototeca, ni en otros álbumes, ni en el widget de Fotos
({a(HIDDEN_ES, "Apple, 104987")}).</li>
<li><strong>Está bloqueado de serie.</strong> Desde iOS 16 el álbum Oculto está bloqueado y pide
identificarse. La guía del iPhone dice que Eliminado y Oculto están bloqueados de serie y se
abren con Face ID, Touch ID o el código ({a(HIDE_GUIDE_ES, "Manual del iPhone")}).</li>
<li><strong>Se puede ocultar el propio álbum.</strong> Ajustes, Apps, Fotos, desactiva Mostrar
álbum Oculto.</li>
<li><strong>Sigue a Fotos en iCloud.</strong> Si usas Fotos en iCloud, lo que ocultas en un
dispositivo queda oculto también en los demás.</li>
</ul>

<h2>Los límites, según esas mismas páginas</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Situación</th><th>¿Lo protege el álbum Oculto?</th></tr></thead>
<tbody>
<tr><td>Alguien repasa tu Fototeca mientras enseñas una foto</td><td>Sí: las ocultas no están ahí y el álbum pide Face ID o Touch ID</td></tr>
<tr><td>Alguien que sabe el código de tu iPhone</td><td>No: Apple pone el código como forma de abrirlo</td></tr>
<tr><td>Alguien quitó el bloqueo</td><td>No: Ajustes, Apps, Fotos, Usar Face ID (o Touch ID o Código) lo desactiva, y lo puede hacer quien entre en tus Ajustes</td></tr>
<tr><td>Tus otros dispositivos con Fotos en iCloud</td><td>Ocultas también allí, con el bloqueo de cada uno (en un Mac, Touch ID o la contraseña de inicio)</td></tr>
<tr><td>La copia en iCloud</td><td>Es una foto normal de Fotos en iCloud; mira abajo</td></tr>
<tr><td>Fotos que borraste en vez de ocultarlas</td><td>Se quedan hasta 30 días en Eliminado, bloqueado igual</td></tr>
</tbody>
</table>
</div>

<h2>El dato que casi nadie mira: quién tiene las claves en iCloud</h2>

<p>Ocultar no cambia cómo se guarda una foto en iCloud. La página de seguridad de iCloud de Apple
({a(ICLOUD_SEC_ES, "102651")}) pone Fotos en la lista de datos que solo pasan a cifrarse de
extremo a extremo si activas la <strong>Protección de datos avanzada</strong>. Con la protección
estándar, la que viene, los datos van cifrados pero las claves se guardan en los centros de
datos de Apple para poder ayudarte a recuperarlos. Si quieres que en iCloud solo tus
dispositivos puedan descifrar las fotos ocultas, activa la Protección de datos avanzada
(Ajustes, tu nombre, iCloud) y lee antes el aviso de Apple sobre la recuperación.</p>
""",
    steps=[
        ("Oculta la foto.",
         f"Ábrela, toca el botón Más y elige Ocultar ({a(HIDDEN_ES, 'Apple')})."),
        ("Comprueba que el bloqueo está activado.",
         "Ajustes, Apps, Fotos: Usar Face ID (o Usar Touch ID, o Usar código) debe estar activado. Vale para Oculto y Eliminado."),
        ("Oculta el propio álbum.",
         "En la misma pantalla desactiva Mostrar álbum Oculto, para que no salga en Utilidades."),
        ("Vacía Eliminado.",
         "Si borraste copias o versiones editadas, bórralas otra vez en Eliminado."),
        ("Decide qué hacer con iCloud.",
         "Si en iCloud nadie más que tú debe poder leerlas, activa la Protección de datos avanzada o déjalas fuera de Fotos en iCloud."),
        ("Cambia el código si otros lo saben.",
         "El álbum Oculto es tan privado como el código de tu iPhone. Una pareja o un hijo que lo sepa puede abrirlo."),
        ("Si no basta, sácalas de la fototeca.",
         f"Una nota bloqueada ({a(NOTES_LOCK_ES, 'Apple')}) puede llevar una contraseña aparte. Una app de bóveda guarda "
         "las fotos en su propio espacio con su propio bloqueo."),
    ],
    after=f"""
<h2>Cuándo basta el álbum Oculto y cuándo no</h2>

<p>Basta si lo que te preocupa es un amigo que repasa tus fotos, un niño que juega con el móvil
o una foto que sale en Recuerdos. No basta si alguien cercano sabe tu código, si compartes cuenta
de iCloud o Mac, o si no quieres las fotos en iCloud con las claves en manos de Apple.</p>

<p>Para esos casos hay tres caminos habituales: una nota bloqueada con contraseña de notas aparte;
pasar las fotos a un ordenador o un disco y borrarlas del móvil; o una app de bóveda. Entre ellas
están Private Photo Vault, Keepsafe (Secret Photo Vault) y nuestra {a(PV_AS, "Photo Vault")}, que guarda las
fotos fuera de la fototeca con su propio código o Face ID, contraseña opcional por álbum y código
señuelo (Premium), sin cuenta, y con su propia copia opcional en iCloud cifrada de extremo a
extremo (Premium). Una bóveda solo sirve si después borras los originales de Fotos y de
Eliminado. Las comparamos en <a href="../../blog/es/apps-para-ocultar-fotos-iphone.html">las
mejores apps para ocultar fotos en iPhone</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(HIDDEN_ES, "Apple, Ocultar fotos con el álbum Oculto (104987)")}, publicado el 16 de marzo de 2026, leído el 23 de octubre de 2026.</li>
<li>{a(HIDE_GUIDE_ES, "Apple, Eliminar u ocultar fotos y vídeos en el iPhone")}, leído el 23 de octubre de 2026.</li>
<li>{a(ICLOUD_SEC_ES, "Apple, Resumen de la seguridad de los datos de iCloud (102651)")}, leído el 23 de octubre de 2026.</li>
<li>{a(NOTES_LOCK_ES, "Apple, Bloquear notas (102537)")}.</li>
</ul>
""",
    faq=[
        ("¿Es seguro el álbum Oculto del iPhone?",
         "Saca las fotos de la fototeca y, desde iOS 16, las bloquea con Face ID, Touch ID o el código. No las protege "
         "de quien sepa tu código, y con Fotos en iCloud están en iCloud como cualquier otra foto."),
        ("¿Alguien puede abrir mi álbum Oculto con mi código?",
         "Sí. Apple pone Face ID, Touch ID o el código como formas de abrir Oculto y Eliminado."),
        ("¿Las fotos ocultas se suben a iCloud?",
         "Si tienes Fotos en iCloud, sí. Apple dice que lo que ocultas en un dispositivo se oculta en los demás, así "
         "que están en tu fototeca de iCloud."),
        ("¿Las fotos ocultas van cifradas de extremo a extremo en iCloud?",
         "Solo con la Protección de datos avanzada. Con la protección estándar, la que viene, Apple guarda las claves."),
        ("¿Se puede ocultar el propio álbum Oculto?",
         "Sí. Ajustes, Apps, Fotos, desactiva Mostrar álbum Oculto."),
        ("¿Una app de bóveda es más segura que el álbum Oculto?",
         "Puede serlo, porque la foto sale de la fototeca y de Fotos en iCloud y tiene su propio bloqueo, pero solo si "
         "borras los originales y guardas una copia de la bóveda."),
    ],
)

# --------------------------------------------------------------------------
# Pinku: IA sin conexion en el avion o de viaje
# --------------------------------------------------------------------------

TRANSLATE_AS = "https://apps.apple.com/us/app/translate/id1514844618"
GTRANSLATE_AS = "https://apps.apple.com/us/app/google-translate/id414706506"
LOCALLY_AS = "https://apps.apple.com/us/app/id6741426692"
POCKETPAL_AS = "https://apps.apple.com/us/app/id6502579498"
ENCLAVE_AS = "https://apps.apple.com/us/app/id6476614556"
PRIVATELLM_AS = "https://apps.apple.com/us/app/id6448106860"
PINKU_AS = "https://apps.apple.com/us/app/id6754878073"
SHORTCUTS_MODEL = "https://support.apple.com/guide/shortcuts/tpg3vrvwmclv/ios"

PK4_EN = dict(
    path="pinku/use-ai-offline-on-a-plane-or-travelling.html",
    app_name="Pinku: Private Offline AI Chat",
    date_iso=ISO, date=D,
    h1="How to use AI offline on a plane or while travelling (iPhone, 2026)",
    desc=("A pre-trip checklist for AI with no signal: which on-device AI chat apps and offline translators work in "
          "airplane mode, how much to download before you leave (model sizes from 0.4 to 4.7 GB, read from Pinku's "
          "model list), and what offline AI cannot do."),
    section="Guides", kicker="Pinku guide",
    standfirst=("ChatGPT, Gemini and Claude need a connection for every message. On a plane, in a roaming dead zone "
                "or abroad without data, what works is whatever you downloaded before you left."),
    tools=["an on-device AI chat app", "Apple Translate", "Google Translate"],
    intro=f"""
<p><strong>We make Pinku, an on-device AI chat app, and it is one of the options below.</strong>
The checklist works whichever app you choose.</p>

<h2>What works with no connection</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Need</th><th>Works offline if you prepare</th><th>Prepare before you leave</th></tr></thead>
<tbody>
<tr><td>Translate signs, menus, a conversation</td><td>{a(TRANSLATE_AS, "Apple Translate")} (its listing: “On-device mode, a fully offline experience… for downloaded languages”), {a(GTRANSLATE_AS, "Google Translate")} (“Offline: translate with no internet connection”)</td><td>Download the languages of the trip</td></tr>
<tr><td>Draft an email, rewrite, summarise text you paste, brainstorm, explain something</td><td>An on-device AI chat app: Locally AI, PocketPal AI, Enclave, Pinku, Private LLM</td><td>Install the app and download a model on Wi-Fi</td></tr>
<tr><td>Quick automations</td><td>Shortcuts' Use Model action with On-Device works “without the need for a network connection” on iPhones with Apple Intelligence ({a(SHORTCUTS_MODEL, "Apple")})</td><td>Build and test the shortcut at home</td></tr>
<tr><td>Look up current facts, prices, opening hours</td><td>Nothing offline does this: models have no web access</td><td>Save the pages or screenshots you will need</td></tr>
</tbody>
</table>
</div>

<h2>How much to download: sizes from Pinku's model list</h2>

<p>The size of the download is the thing that catches people out on hotel Wi-Fi. We read the
model catalogue that ships with Pinku 1.1 (<code>models.json</code>, updated 19 October 2026):
the smallest model, Qwen 3 0.6B, is 0.4 GB; the default, Gemma 3 1B, is 0.8 GB; Llama 3.2 3B
and SmolLM3 3B are 1.8 GB; Qwen 3 4B is 2.3 GB; Gemma 4 E2B is 3.6 GB; the largest, Qwen 3 8B,
is 4.7 GB. Other on-device apps use similar open models, so the sizes are a fair guide for them
too. One model of 1 to 2 GB covers most travel needs; download it at home, not at the gate.</p>

<h2>On-device AI apps for a trip (App Store, 23 October 2026)</h2>
<ul>
<li><strong>{a(LOCALLY_AS, "Locally AI by LM Studio")}</strong>: “Run AI models like Llama, Gemma, Qwen… Offline. Private. No login.” iPhone and iPad.</li>
<li><strong>{a(POCKETPAL_AS, "PocketPal AI")}</strong>: open source, offline chatting with models you download, including any compatible model from Hugging Face.</li>
<li><strong>{a(PINKU_AS, "Pinku")}</strong>: on-device chat on iPhone, iPad and Mac (Apple silicon), needs Metal 3 (iPhone 12 or later); a Siri and Shortcuts action to start a chat; dictation recognised on the device and read aloud with Pinku Pro. No account.</li>
<li><strong>{a(ENCLAVE_AS, "Enclave")}</strong>: “chat offline — no account, no cloud”, many open models; its Pro adds cloud models, which of course need a connection.</li>
<li><strong>{a(PRIVATELLM_AS, "Private LLM")}</strong>: paid upfront, works “even without internet access”, with Siri and Shortcuts.</li>
</ul>
""",
    steps=[
        ("A day before: install and download on Wi-Fi.",
         f"Install an on-device AI app such as <a href=\"{PINKU_STORE}\">Pinku</a> or one of the others above and download "
         "one model. Check that the app lists it as downloaded, not streaming."),
        ("Download your translation languages.",
         "In Apple Translate or Google Translate, download every language of the trip, including the one you speak."),
        ("Test everything in airplane mode at home.",
         "Turn on airplane mode, open each app and ask one real question. Whatever fails here will fail on the plane."),
        ("Pick a model that suits the phone.",
         "Smaller models answer faster and use less battery; larger ones answer better. Many apps only offer the models "
         "that fit your device's memory."),
        ("Paste what you will need into a note.",
         "Booking confirmations, addresses and the text you want summarised or translated. The model can only work with what you give it."),
        ("Charge, and bring a cable or battery.",
         "Running a model is heavy work for a phone. Long sessions drain the battery faster than reading."),
        ("On board, turn on airplane mode and ask.",
         "If the app answers in airplane mode, the answer was generated on the iPhone and nothing you typed left it."),
    ],
    after=f"""
<h2>What offline AI cannot do</h2>

<p>A 1 to 5 GB model on a phone is much smaller than the cloud models behind ChatGPT, Gemini or
Claude. It is good for drafting, rewriting, summarising text you paste in, explaining and
brainstorming. It has no web access, so it does not know today's news, prices or opening hours,
and it can state wrong facts with confidence: check anything that matters, such as visa rules or
medication, against an official source you saved before leaving. Translators are better than chat
models at translation; use both.</p>

<p>About Pinku in particular: chats stay on the device that wrote them (no sync), so a
conversation on your iPhone is not on your Mac. Its App Store privacy label lists purchases and a
user ID, for App Functionality. More in
<a href="use-ai-on-iphone-without-internet.html">how to use AI on iPhone without internet</a> and
<a href="../blog/best-offline-ai-chat-apps-iphone-mac.html">the best offline AI chat apps for iPhone and Mac</a>.</p>

<h2>Sources</h2>
<ul>
<li>Pinku 1.1 model catalogue (<code>models.json</code>, 19 October 2026), read in the app's source code on 23 October 2026.</li>
<li>App Store listings of Apple Translate, Google Translate, Locally AI, PocketPal AI, Enclave and Private LLM, US store, read 23 October 2026.</li>
<li>{a(SHORTCUTS_MODEL, "Apple, Use Model action in Shortcuts")}.</li>
</ul>
""",
    faq=[
        ("Does ChatGPT work on a plane without Wi-Fi?",
         "No. ChatGPT, Gemini and Claude send every message to their servers. With in-flight Wi-Fi they may work; in "
         "airplane mode without Wi-Fi only an on-device model can answer."),
        ("Which AI apps work offline on iPhone?",
         "On-device AI chat apps such as Locally AI, PocketPal AI, Enclave, Pinku and Private LLM, once a model is "
         "downloaded. Apple Translate and Google Translate translate offline with downloaded languages."),
        ("How big is an offline AI model?",
         "In Pinku's catalogue they range from 0.4 GB (Qwen 3 0.6B) to 4.7 GB (Qwen 3 8B); the default Gemma 3 1B is 0.8 GB."),
        ("Can offline AI translate?",
         "Many small models can, but a dedicated translator with downloaded languages is usually more reliable for travel."),
        ("Does offline AI drain the battery?",
         "Generating text is heavy work for the phone, so long sessions use more battery than reading. Smaller models use less."),
        ("How do I know the AI really runs offline?",
         "Turn on airplane mode and ask a question. If it answers, the answer was generated on the device."),
    ],
)

PK4_ES = dict(
    path="pinku/es/usar-ia-sin-conexion-en-el-avion-o-de-viaje.html",
    app_name="Pinku: Private Offline AI Chat",
    date_iso=ISO, date=D,
    h1="Cómo usar la IA sin conexión en el avión o de viaje (iPhone, 2026)",
    desc=("Lista para antes del viaje: qué apps de chat con IA en el dispositivo y qué traductores funcionan en modo "
          "avión, cuánto descargar antes de salir (modelos de 0,4 a 4,7 GB, según la lista de modelos de Pinku) y qué "
          "no puede hacer la IA sin conexión."),
    section="Guías", kicker="Guía de Pinku",
    standfirst=("ChatGPT, Gemini y Claude necesitan conexión para cada mensaje. En el avión, sin roaming o en el "
                "extranjero sin datos, funciona lo que descargaste antes de salir."),
    tools=["una app de chat con IA en el dispositivo", "Traducir de Apple", "Google Translate"],
    intro=f"""
<p><strong>Hacemos Pinku, una app de chat con IA en el dispositivo, y es una de las opciones de
abajo.</strong> La lista sirve elijas la app que elijas.</p>

<h2>Qué funciona sin conexión</h2>

<div class="table-scroll">
<table>
<thead><tr><th>Para qué</th><th>Funciona sin conexión si lo preparas</th><th>Antes de salir</th></tr></thead>
<tbody>
<tr><td>Traducir carteles, cartas, una conversación</td><td>{a(TRANSLATE_AS, "Traducir de Apple")} (su ficha: modo en el dispositivo, sin conexión para los idiomas descargados), {a(GTRANSLATE_AS, "Google Translate")} (traduce sin conexión a internet)</td><td>Descarga los idiomas del viaje</td></tr>
<tr><td>Escribir un correo, reescribir, resumir un texto que pegas, pensar ideas, que te expliquen algo</td><td>Una app de chat con IA en el dispositivo: Locally AI, PocketPal AI, Enclave, Pinku, Private LLM</td><td>Instala la app y descarga un modelo con wifi</td></tr>
<tr><td>Automatizaciones rápidas</td><td>La acción Usar modelo de Atajos con En el dispositivo funciona sin conexión de red en iPhone con Apple Intelligence ({a(SHORTCUTS_MODEL, "Apple")})</td><td>Haz y prueba el atajo en casa</td></tr>
<tr><td>Consultar datos del día, precios, horarios</td><td>Nada sin conexión lo hace: los modelos no tienen acceso a la web</td><td>Guarda las páginas o capturas que vayas a necesitar</td></tr>
</tbody>
</table>
</div>

<h2>Cuánto descargar: tamaños de la lista de modelos de Pinku</h2>

<p>El tamaño de la descarga es lo que pilla a la gente con el wifi del hotel. Leímos el catálogo
de modelos que lleva Pinku 1.1 (<code>models.json</code>, actualizado el 19 de octubre de 2026):
el más pequeño, Qwen 3 0.6B, ocupa 0,4 GB; el de serie, Gemma 3 1B, 0,8 GB; Llama 3.2 3B y
SmolLM3 3B, 1,8 GB; Qwen 3 4B, 2,3 GB; Gemma 4 E2B, 3,6 GB; el mayor, Qwen 3 8B, 4,7 GB. Las
demás apps usan modelos abiertos parecidos, así que los tamaños sirven de guía también para
ellas. Con un modelo de 1 a 2 GB cubres casi todo lo del viaje; descárgalo en casa, no en la
puerta de embarque.</p>

<h2>Apps de IA en el dispositivo para un viaje (App Store, 23 de octubre de 2026)</h2>
<ul>
<li><strong>{a(LOCALLY_AS, "Locally AI by LM Studio")}</strong>: ejecuta modelos como Llama, Gemma o Qwen sin conexión y sin iniciar sesión. iPhone y iPad.</li>
<li><strong>{a(POCKETPAL_AS, "PocketPal AI")}</strong>: de código abierto, chat sin conexión con los modelos que descargues, también cualquiera compatible de Hugging Face.</li>
<li><strong>{a(PINKU_AS, "Pinku")}</strong>: chat en el dispositivo en iPhone, iPad y Mac (Apple silicon), necesita Metal 3 (iPhone 12 o posterior); acción de Siri y Atajos para empezar un chat; dictado reconocido en el dispositivo y lectura en voz alta con Pinku Pro. Sin cuenta.</li>
<li><strong>{a(ENCLAVE_AS, "Enclave")}</strong>: chat sin conexión, sin cuenta ni nube, con muchos modelos abiertos; su Pro añade modelos en la nube, que sí necesitan conexión.</li>
<li><strong>{a(PRIVATELLM_AS, "Private LLM")}</strong>: de pago único, funciona incluso sin acceso a internet, con Siri y Atajos.</li>
</ul>
""",
    steps=[
        ("Un día antes: instala y descarga con wifi.",
         f"Instala una app de IA en el dispositivo como <a href=\"{PINKU_STORE}\">Pinku</a> u otra de las de arriba y descarga "
         "un modelo. Comprueba que la app lo da por descargado."),
        ("Descarga los idiomas para traducir.",
         "En Traducir de Apple o en Google Translate, descarga todos los idiomas del viaje, también el tuyo."),
        ("Prueba todo en modo avión en casa.",
         "Activa el modo avión, abre cada app y haz una pregunta real. Lo que falle aquí fallará en el avión."),
        ("Elige un modelo que vaya con tu móvil.",
         "Los pequeños contestan antes y gastan menos batería; los grandes contestan mejor. Muchas apps solo ofrecen los "
         "modelos que caben en la memoria del aparato."),
        ("Pega en una nota lo que vayas a necesitar.",
         "Reservas, direcciones y los textos que quieras resumir o traducir. El modelo solo trabaja con lo que le das."),
        ("Carga el móvil y lleva cable o batería.",
         "Ejecutar un modelo es trabajo duro para el teléfono. Las sesiones largas gastan más batería que leer."),
        ("A bordo, modo avión y pregunta.",
         "Si la app contesta en modo avión, la respuesta se generó en el iPhone y nada de lo que escribiste salió de él."),
    ],
    after=f"""
<h2>Lo que la IA sin conexión no puede hacer</h2>

<p>Un modelo de 1 a 5 GB en un móvil es mucho más pequeño que los de ChatGPT, Gemini o Claude
en la nube. Sirve para redactar, reescribir, resumir lo que pegas, explicar y pensar ideas. No
tiene acceso a la web, así que no sabe noticias, precios ni horarios de hoy, y puede decir datos
falsos con seguridad: comprueba lo importante, como visados o medicamentos, en una fuente oficial
guardada antes de salir. Para traducir, los traductores son más fiables que los modelos de chat;
usa los dos.</p>

<p>Sobre Pinku en concreto: los chats se quedan en el aparato en que se escribieron (no hay
sincronización), así que una conversación del iPhone no está en el Mac. Su etiqueta de privacidad
del App Store declara compras y un identificador de usuario, para el funcionamiento de la app.
Más en <a href="usar-ia-en-iphone-sin-internet.html">cómo usar IA en el iPhone sin internet</a> y
<a href="../../blog/es/mejores-apps-ia-sin-conexion-iphone-mac.html">las mejores apps de IA sin conexión para iPhone y Mac</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>Catálogo de modelos de Pinku 1.1 (<code>models.json</code>, 19 de octubre de 2026), leído en el código de la app el 23 de octubre de 2026.</li>
<li>Fichas del App Store de Traducir de Apple, Google Translate, Locally AI, PocketPal AI, Enclave y Private LLM, tienda de EE. UU., leídas el 23 de octubre de 2026.</li>
<li>{a(SHORTCUTS_MODEL, "Apple, acción Usar modelo de Atajos")}.</li>
</ul>
""",
    faq=[
        ("¿Funciona ChatGPT en el avión sin wifi?",
         "No. ChatGPT, Gemini y Claude mandan cada mensaje a sus servidores. Con el wifi del avión pueden funcionar; en "
         "modo avión sin wifi solo contesta un modelo en el dispositivo."),
        ("¿Qué apps de IA funcionan sin conexión en el iPhone?",
         "Las de chat con IA en el dispositivo, como Locally AI, PocketPal AI, Enclave, Pinku y Private LLM, una vez "
         "descargado un modelo. Traducir de Apple y Google Translate traducen sin conexión con los idiomas descargados."),
        ("¿Cuánto ocupa un modelo de IA sin conexión?",
         "En el catálogo de Pinku van de 0,4 GB (Qwen 3 0.6B) a 4,7 GB (Qwen 3 8B); el de serie, Gemma 3 1B, ocupa 0,8 GB."),
        ("¿La IA sin conexión puede traducir?",
         "Muchos modelos pequeños sí, pero para viajar suele ser más fiable un traductor con los idiomas descargados."),
        ("¿La IA sin conexión gasta mucha batería?",
         "Generar texto es trabajo duro para el móvil, así que las sesiones largas gastan más que leer. Los modelos pequeños gastan menos."),
        ("¿Cómo sé que la IA funciona de verdad sin conexión?",
         "Activa el modo avión y haz una pregunta. Si contesta, la respuesta se generó en el aparato."),
    ],
)

# --------------------------------------------------------------------------
# Drop: ruido blanco para que el bebe duerma
# --------------------------------------------------------------------------

HUGH = "https://pubmed.ncbi.nlm.nih.gov/24590753/"
SPENCER = "https://pubmed.ncbi.nlm.nih.gov/2405784/"
RIEDY = "https://pubmed.ncbi.nlm.nih.gov/33007706/"
CHOP = "https://www.chop.edu/news/white-noise-not-right-noise"
AAP_SAFE = "https://www.healthychildren.org/English/ages-stages/baby/sleep/Pages/a-parents-guide-to-safe-sleep.aspx"
BGS_GUIDE = "https://support.apple.com/guide/iphone/play-background-sounds-iphb2cfa052c/ios"
BGS_GUIDE_ES = "https://support.apple.com/es-es/guide/iphone/iphb2cfa052c/ios"
DROP_AS = "https://apps.apple.com/us/app/id1462269642"
WNL_AS = "https://apps.apple.com/us/app/id292987597"
WNDS_AS = "https://apps.apple.com/us/app/id1083248251"
BABYSLEEP_AS = "https://apps.apple.com/us/app/id6451003361"

DR3_EN = dict(
    path="drop/white-noise-for-baby-sleep.html",
    app_name="Sleep Sounds & Focus: Drop",
    date_iso=ISO, date=D,
    h1="How to help a baby sleep with white noise: volume, distance and timer (2026)",
    desc=("What the published guidance says about white noise for babies: a 1990 trial in newborns, the 2014 "
          "Pediatrics study of 14 infant sleep machines (all above 50 dBA at 30 cm), advice to keep the device more "
          "than 200 cm from the cot, and AAP safe sleep rules. Then how to set it up on an iPhone."),
    section="Guides", kicker="Drop guide",
    standfirst=("A steady sound can help some babies settle. The published advice is about doing it quietly, far "
                "from the cot and not all night by default. Ask your paediatrician about anything specific to your baby."),
    tools=["iPhone Background Sounds", "a sleep sound app"],
    intro=f"""
<p><strong>We make Drop, a sleep sounds app, and it is one of the options below.</strong> This
page repeats published guidance and does not add medical advice of its own.</p>

<h2>What the research found</h2>

<ul>
<li><strong>It can help some newborns settle.</strong> In a small randomised trial in London
({a(SPENCER, "Spencer et al., Archives of Disease in Childhood, 1990")}), 16 of 20 newborns
(80%) fell asleep within five minutes with white noise, against 5 of 20 (25%) without it. The
authors' conclusion is cautious: white noise “may help mothers settle difficult babies”.</li>
<li><strong>Machines can be too loud.</strong> Researchers in Toronto measured 14 infant sleep
machines at maximum volume, adjusting for a 6-month-old's ear canal
({a(HUGH, "Hugh et al., Pediatrics, 2014")}). At 30 cm all of them were above 50 dBA, the
recommended noise limit for hospital nurseries, and three were above 85 dBA, which over 8 hours
exceeds adult workplace limits.</li>
<li><strong>Distance and volume matter most.</strong> Writing about that study, a paediatrician
at the Children's Hospital of Philadelphia advises to “place them more than 200 centimeters from
the crib” and “keep the volume low” ({a(CHOP, "CHOP, 6 April 2014")}).</li>
<li><strong>For adults the evidence is weak.</strong> A 2021 review of 38 studies rated the
evidence that continuous noise improves sleep as very low quality ({a(RIEDY, "Riedy et al., 2021")}).</li>
</ul>

<h2>Safe sleep comes first</h2>

<p>The American Academy of Pediatrics' safe sleep advice ({a(AAP_SAFE, "HealthyChildren.org, updated 11 September 2026")})
says to place a baby on their back for every sleep, on a firm, flat surface, with “a fitted sheet
only — nothing else should be in the crib”, sharing the room but not the bed for at least the first
6 months. That rules out a phone, speaker or sound machine in the cot or tied to its rails.</p>

<h2>What we checked in Drop's code</h2>

<p>We read Drop's sleep timer in the app's source code (<code>SleepTimer</code>): the options are
15, 30, 45 and 60 minutes, 2 hours, 8 hours, or no end, and in the last 30 seconds the volume falls
gradually to silence instead of cutting off. Playback is set to continue with the screen locked.</p>
""",
    steps=[
        ("Choose one steady sound.",
         "White noise, a fan, rain or a heartbeat. Pick one that is even and without sudden peaks, so it does not startle."),
        ("Put the phone or speaker far from the cot.",
         "More than 200 cm away, never in the cot or on its rails, per the guidance above."),
        ("Start low.",
         "Set the volume at the lowest level that covers the household noise. Listen from where the baby's head is: "
         "it should sound quieter than a normal conversation."),
        ("Set a timer.",
         f"Let the sound stop after the baby is asleep unless you have decided otherwise. On iPhone, Background Sounds "
         f"has Stop Sound with a Timer ({a(BGS_GUIDE, 'Apple')}); apps such as <a href=\"{DROP_STORE}\">Drop</a> have their own timer."),
        ("Use Do Not Disturb or airplane mode.",
         "So a call or notification does not play through the same speaker at full volume. Sounds already downloaded keep playing."),
        ("Check with your paediatrician.",
         "Especially for premature babies, or if your baby has hearing or ear problems."),
    ],
    after=f"""
<h2>Ways to play it on iPhone (App Store, 23 October 2026)</h2>
<ul>
<li><strong>Background Sounds</strong>, built into iOS (Settings, Accessibility, Audio &amp; Visual): Balanced, Bright and
Dark Noise, Ocean, Rain and Stream, with a stop timer ({a(BGS_GUIDE, "Apple")}).</li>
<li><strong>{a(WNL_AS, "White Noise Lite")}</strong> (TMSOFT): many sounds including Heartbeat and Oscillating Fan, a mix
pad and a timer that fades audio out.</li>
<li><strong>{a(WNDS_AS, "White Noise Deep Sleep Sounds")}</strong> (Slumber Studios): 250+ sounds including Shush and Baby
Shusher, sleep timer and mixing.</li>
<li><strong>{a(DROP_AS, "Drop")}</strong>: 53 sounds in version 2.10 (sent to Apple on 23 October 2026), including White,
Pink and Brown Noise, Gentle Breeze (a fan) and Mother's Heartbeat; 9 of them play without a subscription, White Noise and
Mother's Heartbeat among them. One sound at a time (it does not mix sounds), timer from 15 minutes to 8 hours with a
30-second fade, plays with the screen locked, works offline, no account.</li>
<li><strong>{a(BABYSLEEP_AS, "Baby Sleep - White noise")}</strong> (AppCode): nature sounds, three kinds of white noise,
a timer from 1 minute to 8 hours with a gentle fade-out.</li>
</ul>

<p>Whichever you use, the volume and the distance are what the studies are about, not the app.
More on sound colours in <a href="brown-noise-vs-pink-noise-vs-white-noise.html">brown vs pink vs white noise</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(SPENCER, "Spencer JA et al. White noise and sleep induction. Arch Dis Child 1990;65(1):135-7")}.</li>
<li>{a(HUGH, "Hugh SC et al. Infant sleep machines and hazardous sound pressure levels. Pediatrics 2014;133(4):677-81")}.</li>
<li>{a(CHOP, "Pasquariello PS. White noise: not the right noise. Children's Hospital of Philadelphia, 6 April 2014")}.</li>
<li>{a(AAP_SAFE, "American Academy of Pediatrics, How to keep your sleeping baby safe (HealthyChildren.org)")}, read 23 October 2026.</li>
<li>{a(RIEDY, "Riedy SM et al. Noise as a sleep aid: a systematic review. Sleep Med Rev 2021;55:101385")}.</li>
<li>Drop source code (sleep timer and playback), App Store listings of the apps above, read 23 October 2026.</li>
</ul>
""",
    faq=[
        ("Is white noise safe for babies?",
         "The published concern is volume and distance. A 2014 Pediatrics study found 14 infant sleep machines were all "
         "above 50 dBA at 30 cm at full volume. Keep the device more than 200 cm from the cot, at low volume, and ask your paediatrician."),
        ("Does white noise help babies sleep?",
         "In a small 1990 trial, 80% of newborns fell asleep within five minutes with white noise versus 25% without. "
         "It is one small study; it may help some babies settle."),
        ("How loud should white noise be for a baby?",
         "Low. The 2014 study used 50 dBA, the hospital nursery limit, as the reference. In practice, quieter than normal "
         "conversation where the baby's head is."),
        ("How far should a sound machine be from the crib?",
         "More than 200 cm, according to the Children's Hospital of Philadelphia, and never in the crib or on its rails."),
        ("Should white noise play all night?",
         "The guidance is to keep exposure low; a timer that stops the sound after the baby falls asleep is the cautious default."),
        ("Can I use my iPhone as a white noise machine?",
         "Yes: Background Sounds in iOS or a sleep sound app. Put the phone far from the cot, use Do Not Disturb, and set a timer."),
    ],
)

DR3_ES = dict(
    path="drop/es/ruido-blanco-para-que-el-bebe-duerma.html",
    app_name="Sleep Sounds & Focus: Drop",
    date_iso=ISO, date=D,
    h1="Cómo ayudar a dormir a un bebé con ruido blanco: volumen, distancia y temporizador (2026)",
    desc=("Lo que dicen las guías publicadas sobre el ruido blanco para bebés: un ensayo de 1990 con recién nacidos, "
          "el estudio de Pediatrics de 2014 con 14 máquinas (todas por encima de 50 dBA a 30 cm), el consejo de poner "
          "el aparato a más de 200 cm de la cuna y las normas de sueño seguro de la AAP. Y cómo prepararlo en el iPhone."),
    section="Guías", kicker="Guía de Drop",
    standfirst=("Un sonido constante puede ayudar a algunos bebés a calmarse. Las guías publicadas hablan de hacerlo "
                "flojo, lejos de la cuna y no toda la noche por defecto. Lo concreto de tu bebé, pregúntalo al pediatra."),
    tools=["Sonidos de fondo del iPhone", "una app de sonidos para dormir"],
    intro=f"""
<p><strong>Hacemos Drop, una app de sonidos para dormir, y es una de las opciones de abajo.</strong>
Esta página repite lo que dicen las guías publicadas y no añade consejos médicos propios.</p>

<h2>Lo que encontraron los estudios</h2>

<ul>
<li><strong>Puede ayudar a algunos recién nacidos a dormirse.</strong> En un ensayo pequeño en
Londres ({a(SPENCER, "Spencer et al., Archives of Disease in Childhood, 1990")}), 16 de 20 recién
nacidos (80 %) se durmieron en cinco minutos con ruido blanco, frente a 5 de 20 (25 %) sin él. La
conclusión de los autores es prudente: el ruido blanco puede ayudar a calmar a los bebés difíciles.</li>
<li><strong>Las máquinas pueden sonar demasiado.</strong> Investigadores de Toronto midieron 14
máquinas de sueño infantil al máximo, corrigiendo para el oído de un bebé de 6 meses
({a(HUGH, "Hugh et al., Pediatrics, 2014")}). A 30 cm todas pasaban de 50 dBA, el límite
recomendado en las salas de recién nacidos de los hospitales, y tres pasaban de 85 dBA, que en 8
horas supera los límites laborales para adultos.</li>
<li><strong>Lo que más cuenta es la distancia y el volumen.</strong> Sobre ese estudio, un pediatra
del Children's Hospital of Philadelphia aconseja ponerlas a más de 200 centímetros de la cuna y
con el volumen bajo ({a(CHOP, "CHOP, 6 de abril de 2014")}).</li>
<li><strong>En adultos la evidencia es débil.</strong> Una revisión de 2021 de 38 estudios calificó
de muy baja calidad la evidencia de que el ruido continuo mejore el sueño ({a(RIEDY, "Riedy et al., 2021")}).</li>
</ul>

<h2>Primero, el sueño seguro</h2>

<p>Los consejos de sueño seguro de la Academia Americana de Pediatría
({a(AAP_SAFE, "HealthyChildren.org, actualizado el 11 de septiembre de 2026")}) dicen que el bebé
duerma siempre boca arriba, en una superficie firme y plana, solo con una sábana ajustable y nada
más en la cuna, compartiendo habitación pero no cama al menos los 6 primeros meses. Eso descarta
poner un móvil, un altavoz o una máquina de sonido dentro de la cuna o atada a los barrotes.</p>

<h2>Lo que comprobamos en el código de Drop</h2>

<p>Leímos el temporizador de Drop en el código de la app (<code>SleepTimer</code>): las opciones
son 15, 30, 45 y 60 minutos, 2 horas, 8 horas o sin fin, y en los últimos 30 segundos el volumen
baja poco a poco hasta el silencio en lugar de cortarse. El sonido sigue con la pantalla bloqueada.</p>
""",
    steps=[
        ("Elige un sonido constante.",
         "Ruido blanco, un ventilador, lluvia o un latido. Uno uniforme y sin picos repentinos, para que no sobresalte."),
        ("Pon el móvil o el altavoz lejos de la cuna.",
         "A más de 200 cm, nunca dentro de la cuna ni en los barrotes, según las guías de arriba."),
        ("Empieza bajo.",
         "Pon el volumen más bajo que tape el ruido de casa. Escucha desde donde está la cabeza del bebé: debe sonar más "
         "flojo que una conversación normal."),
        ("Pon un temporizador.",
         f"Que el sonido pare cuando el bebé ya duerma, salvo que hayas decidido otra cosa. En el iPhone, Sonidos de fondo "
         f"tiene Detener sonido con temporizador ({a(BGS_GUIDE_ES, 'Apple')}); apps como <a href=\"{DROP_STORE}\">Drop</a> tienen el suyo."),
        ("Usa No molestar o el modo avión.",
         "Para que una llamada o un aviso no suene por el mismo altavoz a todo volumen. Los sonidos descargados siguen sonando."),
        ("Consúltalo con el pediatra.",
         "Sobre todo con bebés prematuros o si tu bebé tiene problemas de oído."),
    ],
    after=f"""
<h2>Formas de ponerlo en el iPhone (App Store, 23 de octubre de 2026)</h2>
<ul>
<li><strong>Sonidos de fondo</strong>, de serie en iOS (Ajustes, Accesibilidad, Audio y visualización): ruido equilibrado,
brillante y oscuro, océano, lluvia y arroyo, con temporizador ({a(BGS_GUIDE_ES, "Apple")}).</li>
<li><strong>{a(WNL_AS, "White Noise Lite")}</strong> (TMSOFT): muchos sonidos, entre ellos latido y ventilador, mezclador
y un temporizador que baja el sonido poco a poco.</li>
<li><strong>{a(WNDS_AS, "White Noise Deep Sleep Sounds")}</strong> (Slumber Studios): más de 250 sonidos, con «shush» y
sonidos para bebés, temporizador y mezcla.</li>
<li><strong>{a(DROP_AS, "Drop")}</strong>: 53 sonidos en la versión 2.10 (enviada a Apple el 23 de octubre de 2026), entre
ellos ruido blanco, rosa y marrón, una brisa de ventilador y un latido materno; 9 suenan sin suscripción, entre ellos el
ruido blanco y el latido. Un sonido cada vez (no mezcla sonidos), temporizador de 15 minutos a 8 horas con 30 segundos de
fundido, suena con la pantalla bloqueada, funciona sin conexión y sin cuenta.</li>
<li><strong>{a(BABYSLEEP_AS, "Baby Sleep - White noise")}</strong> (AppCode): sonidos de naturaleza, tres tipos de ruido
blanco y temporizador de 1 minuto a 8 horas con fundido suave.</li>
</ul>

<p>Uses la que uses, los estudios hablan del volumen y la distancia, no de la app. Más sobre
colores de ruido en <a href="ruido-marron-rosa-o-blanco.html">ruido marrón, rosa o blanco</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(SPENCER, "Spencer JA et al. White noise and sleep induction. Arch Dis Child 1990;65(1):135-7")}.</li>
<li>{a(HUGH, "Hugh SC et al. Infant sleep machines and hazardous sound pressure levels. Pediatrics 2014;133(4):677-81")}.</li>
<li>{a(CHOP, "Pasquariello PS. White noise: not the right noise. Children's Hospital of Philadelphia, 6 de abril de 2014")}.</li>
<li>{a(AAP_SAFE, "Academia Americana de Pediatría, How to keep your sleeping baby safe (HealthyChildren.org)")}, leído el 23 de octubre de 2026.</li>
<li>{a(RIEDY, "Riedy SM et al. Noise as a sleep aid: a systematic review. Sleep Med Rev 2021;55:101385")}.</li>
<li>Código de Drop (temporizador y reproducción) y fichas del App Store de las apps de arriba, leídos el 23 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("¿Es seguro el ruido blanco para los bebés?",
         "Lo que preocupa en los estudios es el volumen y la distancia. Un estudio de Pediatrics de 2014 vio que 14 "
         "máquinas para bebés pasaban todas de 50 dBA a 30 cm al máximo. Pon el aparato a más de 200 cm de la cuna, "
         "con volumen bajo, y pregunta al pediatra."),
        ("¿El ruido blanco ayuda a dormir a los bebés?",
         "En un ensayo pequeño de 1990, el 80 % de los recién nacidos se durmió en cinco minutos con ruido blanco "
         "frente al 25 % sin él. Es un solo estudio pequeño; puede ayudar a calmar a algunos bebés."),
        ("¿A qué volumen debe sonar el ruido blanco para un bebé?",
         "Bajo. El estudio de 2014 usa como referencia 50 dBA, el límite de las salas de recién nacidos. En la práctica, "
         "más flojo que una conversación normal donde está la cabeza del bebé."),
        ("¿A qué distancia de la cuna pongo la máquina de ruido?",
         "A más de 200 cm, según el Children's Hospital of Philadelphia, y nunca dentro de la cuna ni en los barrotes."),
        ("¿Debe sonar toda la noche?",
         "Las guías piden poca exposición; un temporizador que pare el sonido cuando el bebé se duerma es lo prudente."),
        ("¿Puedo usar el iPhone como máquina de ruido blanco?",
         "Sí: Sonidos de fondo de iOS o una app de sonidos para dormir. Pon el móvil lejos de la cuna, activa No molestar y usa un temporizador."),
    ],
)

# --------------------------------------------------------------------------
# Crypton: seguir precios cripto sin dar tus datos
# --------------------------------------------------------------------------

CRYPTON_AS = "https://apps.apple.com/us/app/id1143691286"
CRYPTOPRO_AS = "https://apps.apple.com/us/app/id980888073"
COINGECKO_AS = "https://apps.apple.com/us/app/id1390323960"
CMC_AS = "https://apps.apple.com/us/app/id1282107098"
COINSTATS_AS = "https://apps.apple.com/us/app/id1247849330"
DELTA_AS = "https://apps.apple.com/us/app/id1288676542"
HODL_AS = "https://apps.apple.com/us/app/id1253668876"
LABELS_STORY = "https://apps.apple.com/us/iphone/story/id1539235847"

CR_EN = dict(
    path="crypton/track-crypto-prices-without-giving-your-data.html",
    app_name="Crypto Tracker: Crypton",
    date_iso=ISO, date=D,
    h1="How to track crypto prices without giving your data: no-account trackers, widgets and alerts (2026)",
    desc=("The App Store privacy labels of 7 crypto trackers, read on 23 October 2026 (CoinGecko, CoinMarketCap, "
          "CoinStats, Delta, HODL, Crypto Pro, Crypton), what connecting a wallet or exchange gives away, and how to "
          "follow prices with a widget and alerts while sharing as little as possible."),
    section="Guides", kicker="Crypton guide",
    standfirst=("A price is public; your holdings are not. Most of what a tracker learns about you comes from the "
                "account, the exchange or wallet you connect and the analytics in the app. You can skip most of it."),
    tools=["a crypto price tracker app", "iPhone App Privacy Report"],
    intro=f"""
<p><strong>We make Crypton, a crypto price tracker, and it is one of the seven apps below.</strong>
The others are real alternatives with features Crypton does not have.</p>

<h2>What 7 trackers declare on the App Store (read 23 October 2026)</h2>

<p>We read the privacy label of each app from its public App Store page (US store). These are
the developers' own declarations; Apple shows them but does not verify them
({a(LABELS_STORY, "Apple's definitions")}).</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Data used to track you</th><th>Data linked to you</th><th>Data not linked to you</th></tr></thead>
<tbody>
<tr><td>{a(CRYPTOPRO_AS, "Crypto Pro")}</td><td>None</td><td>None</td><td>Identifiers</td></tr>
<tr><td>{a(CRYPTON_AS, "Crypton")}</td><td>None</td><td>None</td><td>Usage Data, Diagnostics</td></tr>
<tr><td>{a(COINSTATS_AS, "CoinStats")}</td><td>None</td><td>None</td><td>Contact Info, Identifiers, Usage Data, Diagnostics</td></tr>
<tr><td>{a(COINGECKO_AS, "CoinGecko")}</td><td>None</td><td>Contact Info</td><td>Identifiers, Usage Data, Diagnostics</td></tr>
<tr><td>{a(CMC_AS, "CoinMarketCap")}</td><td>Usage Data</td><td>Identifiers</td><td>Identifiers, Usage Data, Diagnostics</td></tr>
<tr><td>{a(DELTA_AS, "Delta by eToro")}</td><td>Identifiers, Usage Data</td><td>None</td><td>User Content, Search History, Identifiers, Usage Data, Diagnostics</td></tr>
<tr><td>{a(HODL_AS, "HODL")}</td><td>Usage Data</td><td>Purchases, Financial Info, Contact Info, User Content, Identifiers, Usage Data</td><td>User Content, Usage Data, Diagnostics</td></tr>
</tbody>
</table>
</div>

<p>Labels describe what the app may collect across all its features. An app with portfolio
sync, news and exchange connections will declare more than a plain price list, and that is not
by itself a sign of bad faith.</p>

<h2>The three things that give your data away</h2>
<ol>
<li><strong>An account.</strong> An email or sign-in links what you watch and hold to you.
CoinMarketCap's listing says you can “go incognito without logging in”, saving data locally;
Crypton and Crypto Pro work without one.</li>
<li><strong>Connecting an exchange or wallet.</strong> CoinStats and Delta sync with hundreds of
exchanges and wallets, which is their strength, but the service then knows your real balances
and, for a wallet address, your on-chain history. Typing holdings in by hand gives away nothing
about where they are.</li>
<li><strong>Server-side alerts.</strong> An alert that reaches you while the app is closed is
usually sent by the developer's server, which therefore stores the coin and price you are
watching. That is often fine; just know it.</li>
</ol>
""",
    steps=[
        ("Pick a tracker that works without an account.",
         f"Crypto Pro, CoinMarketCap in incognito mode, or <a href=\"{CRYPTON_STORE}\">Crypton</a> all show prices without "
         "signing in. Read the privacy label on the App Store page before installing."),
        ("Add holdings by hand.",
         "Enter the coin, the amount and the buy price yourself instead of connecting an exchange or pasting a wallet "
         "address. You still get profit and loss."),
        ("Put the prices on a widget.",
         "A Home Screen widget shows the coins you follow without opening the app. Most trackers above have one."),
        ("Decide whether you need alerts.",
         "If you do, choose an app whose alerts you are comfortable with, and set only the ones you will act on."),
        ("Say no to tracking.",
         "If an app asks to track you across other companies' apps and websites, tap Ask App Not to Track."),
        ("Check what it contacts.",
         f"Turn on App Privacy Report (Settings, Privacy &amp; Security, App Privacy Report) and after a few days look at "
         f"which domains the app contacted ({a(PRIV_REPORT, 'Apple')})."),
        ("Keep a backup of a manual portfolio.",
         "Without an account, check how the app keeps your holdings if you delete it or change phones."),
    ],
    after=f"""
<h2>Who each app suits</h2>
<ul>
<li><strong>Crypto Pro</strong>: no ads, price notifications, widgets, Apple Watch, optional iCloud sync, keys kept in the
keychain; the smallest label of the seven.</li>
<li><strong>Crypton</strong>: prices of the top 250 coins, favourites, a manual portfolio with profit and loss on every
coin, two widgets (Coin List, where you pick the coins, in small, medium and large; Portfolio, with value, today's change
and biggest holdings), and an optional account with Sign in with Apple or Google to sync. Without an account, holdings,
buy prices and favourites are also copied to iCloud's key-value store under your Apple ID, so they survive a new phone
(we read this in the code of version 2.0.7). It has no price alerts in the version on sale today and no exchange or
wallet connections.</li>
<li><strong>CoinStats</strong>: for people who want every exchange and wallet synced in one place, with alerts, widgets and
Apple Watch.</li>
<li><strong>CoinGecko</strong> and <strong>CoinMarketCap</strong>: the broadest market data, alerts and widgets; an account
for sync.</li>
<li><strong>Delta</strong>: crypto plus stocks, ETFs and forex in one portfolio, synced with brokers and exchanges.</li>
<li><strong>HODL</strong>: crypto and stocks with news, social posts and an AI agent; the longest label.</li>
</ul>

<p>Full rankings: <a href="../blog/best-crypto-portfolio-tracker-apps-iphone.html">the best crypto portfolio tracker apps
for iPhone</a>. More on <a href="../crypton.html">Crypton's page</a>.</p>

<h2>Sources</h2>
<ul>
<li>App Store pages (privacy labels and descriptions) of Crypto Pro, Crypton, CoinStats, CoinGecko, CoinMarketCap, Delta by eToro and HODL, US store, read 23 October 2026.</li>
<li>Crypton 2.0.7 source code (widgets, account, portfolio copy in iCloud), read 23 October 2026.</li>
<li>{a(PRIV_REPORT, "Apple, About App Privacy Report (102188)")} and {a(LABELS_STORY, "App Store privacy definitions")}.</li>
</ul>
""",
    faq=[
        ("Can I track crypto prices without an account?",
         "Yes. Crypto Pro, Crypton and CoinMarketCap's incognito mode show prices and let you keep a portfolio without signing in."),
        ("Which crypto tracker collects the least data?",
         "Of seven we checked on 23 October 2026, Crypto Pro declares only identifiers not linked to you, and Crypton "
         "only usage and diagnostics not linked to you. Neither declares data used to track you."),
        ("Is it safe to connect my exchange to a portfolio app?",
         "Read-only API keys cannot move funds, but the app then knows your real balances and trades. Entering holdings "
         "by hand shares nothing about where they are."),
        ("Do crypto price alerts share my data?",
         "Alerts that arrive while the app is closed are usually sent from the developer's server, which stores the coin "
         "and price you watch. Local alerts checked on the phone do not need that."),
        ("Does Crypton have a widget?",
         "Yes, two: Coin List (choose the coins; small, medium, large) and Portfolio (value, today's change, biggest holdings)."),
        ("Does Crypton have price alerts?",
         "Not in the version on sale on 23 October 2026."),
    ],
)

CR_ES = dict(
    path="crypton/es/seguir-precios-cripto-sin-dar-tus-datos.html",
    app_name="Crypto Tracker: Crypton",
    date_iso=ISO, date=D,
    h1="Cómo seguir los precios de las criptomonedas sin dar tus datos: apps sin cuenta, widgets y alertas (2026)",
    desc=("Las etiquetas de privacidad del App Store de 7 apps de cripto, leídas el 23 de octubre de 2026 (CoinGecko, "
          "CoinMarketCap, CoinStats, Delta, HODL, Crypto Pro, Crypton), qué regalas al conectar un monedero o un "
          "exchange, y cómo seguir precios con widget y alertas compartiendo lo mínimo."),
    section="Guías", kicker="Guía de Crypton",
    standfirst=("Un precio es público; lo que tienes, no. Casi todo lo que una app de cripto sabe de ti sale de la "
                "cuenta, del exchange o monedero que conectas y de la analítica de la app. Puedes saltarte casi todo."),
    tools=["una app de precios de cripto", "Informe de privacidad de apps del iPhone"],
    intro=f"""
<p><strong>Hacemos Crypton, una app de precios de criptomonedas, y es una de las siete de abajo.</strong>
Las demás son alternativas reales con funciones que Crypton no tiene.</p>

<h2>Lo que declaran 7 apps en el App Store (leído el 23 de octubre de 2026)</h2>

<p>Leímos la etiqueta de privacidad de cada app en su página pública del App Store (tienda de
EE. UU.). Son declaraciones de los propios desarrolladores; Apple las enseña pero no las comprueba
({a(LABELS_STORY, "definiciones de Apple")}).</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Datos para rastrearte</th><th>Datos vinculados a ti</th><th>Datos no vinculados a ti</th></tr></thead>
<tbody>
<tr><td>{a(CRYPTOPRO_AS, "Crypto Pro")}</td><td>Ninguno</td><td>Ninguno</td><td>Identificadores</td></tr>
<tr><td>{a(CRYPTON_AS, "Crypton")}</td><td>Ninguno</td><td>Ninguno</td><td>Datos de uso, Diagnóstico</td></tr>
<tr><td>{a(COINSTATS_AS, "CoinStats")}</td><td>Ninguno</td><td>Ninguno</td><td>Información de contacto, Identificadores, Datos de uso, Diagnóstico</td></tr>
<tr><td>{a(COINGECKO_AS, "CoinGecko")}</td><td>Ninguno</td><td>Información de contacto</td><td>Identificadores, Datos de uso, Diagnóstico</td></tr>
<tr><td>{a(CMC_AS, "CoinMarketCap")}</td><td>Datos de uso</td><td>Identificadores</td><td>Identificadores, Datos de uso, Diagnóstico</td></tr>
<tr><td>{a(DELTA_AS, "Delta by eToro")}</td><td>Identificadores, Datos de uso</td><td>Ninguno</td><td>Contenido del usuario, Historial de búsqueda, Identificadores, Datos de uso, Diagnóstico</td></tr>
<tr><td>{a(HODL_AS, "HODL")}</td><td>Datos de uso</td><td>Compras, Información financiera, Información de contacto, Contenido del usuario, Identificadores, Datos de uso</td><td>Contenido del usuario, Datos de uso, Diagnóstico</td></tr>
</tbody>
</table>
</div>

<p>La etiqueta cubre lo que la app puede recoger con todas sus funciones. Una app con
sincronización de cartera, noticias y conexión a exchanges declara más que una simple lista de
precios, y eso por sí solo no es mala fe.</p>

<h2>Las tres cosas que regalan tus datos</h2>
<ol>
<li><strong>Una cuenta.</strong> Un correo o un inicio de sesión une a tu nombre lo que sigues y
lo que tienes. La ficha de CoinMarketCap dice que puedes usarla en modo incógnito sin iniciar
sesión, con los datos guardados en el móvil; Crypton y Crypto Pro funcionan sin cuenta.</li>
<li><strong>Conectar un exchange o un monedero.</strong> CoinStats y Delta se sincronizan con
cientos de exchanges y monederos, que es su punto fuerte, pero entonces el servicio sabe tus
saldos reales y, con una dirección de monedero, tu historial en la cadena. Si metes las cantidades
a mano no dices nada de dónde están.</li>
<li><strong>Alertas en el servidor.</strong> Una alerta que te llega con la app cerrada suele
mandarla el servidor del desarrollador, que por tanto guarda la moneda y el precio que vigilas.
Muchas veces no importa; solo conviene saberlo.</li>
</ol>
""",
    steps=[
        ("Elige una app que funcione sin cuenta.",
         f"Crypto Pro, CoinMarketCap en modo incógnito o <a href=\"{CRYPTON_STORE}\">Crypton</a> enseñan precios sin "
         "iniciar sesión. Lee la etiqueta de privacidad en el App Store antes de instalar."),
        ("Mete tus monedas a mano.",
         "Escribe la moneda, la cantidad y el precio de compra en lugar de conectar un exchange o pegar una dirección de "
         "monedero. Sigues viendo ganancias y pérdidas."),
        ("Pon los precios en un widget.",
         "Un widget en la pantalla de inicio enseña tus monedas sin abrir la app. Casi todas las de arriba tienen."),
        ("Decide si necesitas alertas.",
         "Si las quieres, elige una app cuyas alertas te parezcan bien y pon solo las que vayas a usar."),
        ("Di que no al rastreo.",
         "Si una app pide rastrearte en apps y webs de otras empresas, toca Pedir a la app que no me rastree."),
        ("Mira con quién se conecta.",
         f"Activa el Informe de privacidad de apps (Ajustes, Privacidad y seguridad) y al cabo de unos días mira qué "
         f"dominios ha contactado la app ({a(PRIV_REPORT_ES, 'Apple')})."),
        ("Guarda una copia de la cartera manual.",
         "Sin cuenta, mira cómo guarda la app tus monedas si la borras o cambias de móvil."),
    ],
    after=f"""
<h2>Para quién es cada una</h2>
<ul>
<li><strong>Crypto Pro</strong>: sin anuncios, avisos de precio, widgets, Apple Watch, sincronización opcional con iCloud y
claves en el llavero; la etiqueta más corta de las siete.</li>
<li><strong>Crypton</strong>: precios de las 250 primeras monedas, favoritas, cartera manual con ganancias y pérdidas por
moneda, dos widgets (Lista de monedas, en la que eliges las monedas, pequeño, mediano y grande; Cartera, con el valor, el
cambio del día y lo que más pesa) y cuenta opcional con Iniciar sesión con Apple o Google para sincronizar. Sin cuenta, las
monedas, precios de compra y favoritas se copian además en el almacén clave-valor de iCloud con tu Apple ID, así que
vuelven en un móvil nuevo (lo leímos en el código de la versión 2.0.7). La versión a la venta hoy no tiene alertas de
precio ni conexión con exchanges o monederos.</li>
<li><strong>CoinStats</strong>: para quien quiere todos sus exchanges y monederos sincronizados en un sitio, con alertas,
widgets y Apple Watch.</li>
<li><strong>CoinGecko</strong> y <strong>CoinMarketCap</strong>: los datos de mercado más amplios, alertas y widgets; cuenta
para sincronizar.</li>
<li><strong>Delta</strong>: cripto más acciones, ETF y divisas en una cartera, sincronizada con brókeres y exchanges.</li>
<li><strong>HODL</strong>: cripto y acciones con noticias, redes y un agente de IA; la etiqueta más larga.</li>
</ul>

<p>Comparativa completa: <a href="../../blog/es/mejores-apps-cartera-cripto-iphone.html">las mejores apps para seguir tu
cartera de criptomonedas en iPhone</a>. Más en <a href="../../crypton.html">la página de Crypton</a> (en inglés).</p>

<h2>Fuentes</h2>
<ul>
<li>Páginas del App Store (etiquetas de privacidad y descripciones) de Crypto Pro, Crypton, CoinStats, CoinGecko, CoinMarketCap, Delta by eToro y HODL, tienda de EE. UU., leídas el 23 de octubre de 2026.</li>
<li>Código de Crypton 2.0.7 (widgets, cuenta, copia de la cartera en iCloud), leído el 23 de octubre de 2026.</li>
<li>{a(PRIV_REPORT_ES, "Apple, Acerca del Informe de privacidad de apps (102188)")} y {a(LABELS_STORY, "definiciones de privacidad del App Store")}.</li>
</ul>
""",
    faq=[
        ("¿Puedo seguir los precios de cripto sin crear una cuenta?",
         "Sí. Crypto Pro, Crypton y el modo incógnito de CoinMarketCap enseñan precios y dejan llevar una cartera sin iniciar sesión."),
        ("¿Qué app de cripto recoge menos datos?",
         "De las siete que miramos el 23 de octubre de 2026, Crypto Pro solo declara identificadores no vinculados a ti, y "
         "Crypton solo datos de uso y diagnóstico no vinculados a ti. Ninguna declara datos para rastrearte."),
        ("¿Es seguro conectar mi exchange a una app de cartera?",
         "Las claves API de solo lectura no pueden mover fondos, pero la app sabe entonces tus saldos y operaciones reales. "
         "Si metes las cantidades a mano no compartes dónde están."),
        ("¿Las alertas de precio comparten mis datos?",
         "Las que llegan con la app cerrada suelen salir del servidor del desarrollador, que guarda la moneda y el precio "
         "que vigilas. Las alertas que comprueba el propio móvil no lo necesitan."),
        ("¿Crypton tiene widget?",
         "Sí, dos: Lista de monedas (eliges las monedas; pequeño, mediano, grande) y Cartera (valor, cambio del día y lo que más pesa)."),
        ("¿Crypton tiene alertas de precio?",
         "No en la versión a la venta el 23 de octubre de 2026."),
    ],
)

GUIDES = [(PV4_EN, PV4_ES), (PV5_EN, PV5_ES), (PK4_EN, PK4_ES), (DR3_EN, DR3_ES), (CR_EN, CR_ES)]
