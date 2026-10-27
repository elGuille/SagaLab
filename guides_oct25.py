# -*- coding: utf-8 -*-
"""Guia de Photo Vault (EN + ES), con la plantilla de guides.py: si borras la app de la boveda, ¿pierdes las fotos?

Nicho AEO (saga-growth/aeo-nichos/photo-vault.md, 25 oct 2026). Rama sin unir: se publica con el si de Marta,
y solo con la 1.3.0 a la venta (comprobarlo antes de unir).

Datos, comprobados el 25 oct 2026:
- Photo Vault 1.3.0 (37), rama release-1.3.0, confirmado por la sesion de Photo Vault con archivo y linea:
  boveda (PrivateMedia) y papelera (TrashMedia) fuera de la copia del iPhone (MediaFileManager.applyBackupExclusion);
  albumes en UserDefaults. Copia en iCloud (CloudVault): apagada por defecto, activarla es Premium
  (ICloudCopyView.swift:40), restaurar no (restoreOnly, CloudVault.swift:121-129); base privada de CloudKit del
  mismo Apple ID (CloudVault.swift:379), clave en encryptedValues (406-408); lo subido sigue en iCloud al borrar
  la app; al reinstalar la app ofrece restaurar una vez (AlbumsView.swift:266, 286-298); PIN nuevo (Llavero solo
  de este dispositivo, KeychainHelper.swift:103, 134-136); contrasenas de album vuelven (CloudVault.swift:293-306,
  351-354); senuelo nunca sube ni vuelve (CloudVault.swift:122, DecoyVault.swift). Copia en archivo: no pide
  Premium (ICloudCopyView.swift:120-135); fotos, videos, albumes, portadas y contrasenas de album, sin senuelo
  (VaultBackup.swift:82-96, 231-234); AES-256-GCM con PBKDF2 de 310.000 iteraciones y contrasena de 8 o mas
  caracteres (VaultBackup.swift:17-25, 57-61); restaurar suma sin borrar y vale en otro iPhone (151-153).
  1.3.0: Recently Deleted de 30 dias, fuera de la copia del iPhone, de iCloud y del archivo.
- Apple: support.apple.com 108770 (What does iCloud back up?, 1 may 2025: la copia incluye datos de apps) y
  developer.apple.com «Optimizing your app's data for iCloud backup» (isExcludedFromBackup).
- Competencia: descripciones del App Store de EE. UU. leidas el 25 oct 2026 (Private Photo Vault 25.8,
  Keepsafe 13.34.0, SPV 7.6.1, PV 7.7.5).
De nuestras apps: sin precios y sin la palabra «free/gratis». Sin rayas.
"""

D = {"en": "25 October 2026", "es": "25 de octubre de 2026"}
ISO = "2026-10-25"

PV_STORE = "https://apps.apple.com/app/apple-store/id1532670722?pt=118348020&amp;ct=sagalab-guide&amp;mt=8"
BACKUP = "https://support.apple.com/en-us/108770"
BACKUP_ES = "https://support.apple.com/es-es/108770"
DEV_BACKUP = "https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup"
PPV = "https://apps.apple.com/us/app/id417571834"
KEEPSAFE = "https://apps.apple.com/us/app/id510873505"
SPV = "https://apps.apple.com/us/app/id1449239240"
PVA = "https://apps.apple.com/us/app/id867586326"


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


PV6_EN = dict(
    path="photo-vault/delete-photo-vault-app-lose-photos.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="If you delete a photo vault app, do you lose the photos? (2026)",
    desc=("What happens to hidden photos when you delete a vault app on iPhone, why the iPhone's iCloud backup "
          "does not bring them back, what four popular vaults say in their App Store listings, and how to keep a copy first."),
    section="Guides", kicker="Photo Vault guide",
    standfirst=("Short answer: in most vault apps, yes. Deleting the app deletes the photos inside it, and the "
                "iPhone's iCloud backup does not have them. Export them, or turn on the app's own backup, before you delete it."),
    tools=["iPhone Settings", "Files"],
    intro=f"""
<p><strong>We make Photo Vault, a vault app, and it is one of the apps in the table.</strong> This page is
about any vault app: the rule is the same for all of them.</p>

<h2>Why the iCloud backup does not save them</h2>

<p>Apple's iCloud Backup normally includes app data ({a(BACKUP, "Apple, What does iCloud back up?")}).
But an app can mark files so they are left out of backups ({a(DEV_BACKUP, "Apple developer documentation")}).
Vault apps do this on purpose, so your private photos do not end up in an ordinary iPhone or computer backup.
The side effect: when you delete the app, iOS deletes its files, and there is no copy in the backup to restore.</p>

<p>Apple's own Hidden album is different: it is part of the Photos library and, with iCloud Photos, it is in iCloud
like any other photo.</p>

<h2>What four popular vaults say</h2>

<p>From each app's US App Store listing, read on 25 October 2026:</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Its own cloud copy</th><th>What the listing says about deleting the app</th></tr></thead>
<tbody>
<tr><td>{a(PPV, "Private Photo Vault")}</td><td>Cloud Vault, encrypted with a password only you know; the listing says the free version does not back up to Cloud Vault</td><td>Asks you to back up so a lost device does not mean lost data. If you forget the Cloud Vault password, the backup cannot be opened</td></tr>
<tr><td>{a(KEEPSAFE, "Keepsafe (Secret Photo Vault)")}</td><td>Private Cloud of up to 10,000 items, a Premium feature</td><td>Not stated</td></tr>
<tr><td>{a(SPV, "SPV - Secret Photo Vault")}</td><td>None: it keeps everything on the device</td><td>“If you delete the app, your photos &amp; data saved in the app will also be deleted”</td></tr>
<tr><td>{a(PVA, "PV - Secret Photo Album")}</td><td>Cloud sync and backup to Dropbox or Google Drive for paid members</td><td>“If you never backup the data in the app, the photos/videos will be gone”</td></tr>
<tr><td>{a(PV_STORE, "Photo Vault")} (ours)</td><td>Optional copy in your own iCloud, encrypted on the iPhone (Premium to turn on), and a password-protected backup file</td><td>Without a copy, everything is gone. With the iCloud copy or a backup file, you can restore it (details below)</td></tr>
</tbody>
</table>
</div>

<h2>Exactly what happens in Photo Vault</h2>

<p>Read from the code of Photo Vault 1.3.0 on 25 October 2026:</p>
<ul>
<li><strong>No copy:</strong> deleting the app deletes every photo, video and album in the vault, and Recently Deleted
with them. They are not in the iPhone backup.</li>
<li><strong>With the iCloud copy on</strong> (off by default; turning it on is part of Premium): photos already uploaded
stay in your private iCloud space after you delete the app. Each one is encrypted on the iPhone before it leaves,
with a key only your devices can read. Reinstall the app with the <strong>same Apple ID</strong> and, when the vault is
empty, it offers to restore from iCloud. Restoring does not need Premium. You set a new PIN; album passwords come back.</li>
<li><strong>With a backup file</strong> (Settings, iCloud &amp; Backup, Export Backup; no Premium needed): one
<code>.pvbackup</code> file with your photos, videos, albums and album passwords, encrypted with a password of at least
8 characters. Keep it in Files, iCloud Drive or on a Mac. It restores on any iPhone, even with another Apple ID,
with that password. Without the password nobody can open it, us included.</li>
<li><strong>Never restored:</strong> the decoy vault (it is never uploaded or exported), the PIN itself, and items
in Recently Deleted.</li>
</ul>
""",
    steps=[
        ("Open the vault before you delete it.",
         "Look for Export, Backup or Cloud in its settings. If there is nothing, export the photos to Photos or Files."),
        ("Make the copy.",
         "In Photo Vault: Settings, iCloud &amp; Backup. Turn on the iCloud copy, or use Export Backup and choose a password you will remember."),
        ("Check that the copy opens.",
         "Open a few photos and one video from the export, or restore the backup file on another device."),
        ("Write down the passwords.",
         "A Cloud Vault password (Private Photo Vault) or a backup file password (Photo Vault) cannot be recovered by anyone."),
        ("Cancel the subscription if you are leaving.",
         "Deleting an app does not cancel it: Settings, your name, Subscriptions."),
        ("Only then delete the app.",
         "Restore later from the app's own copy, not from the iPhone backup."),
    ],
    after=f"""
<h2>If you already deleted it</h2>

<p>Reinstall the same app and sign in to the same Apple ID or account. If it had its own cloud copy (Private Photo
Vault's Cloud Vault, Keepsafe's Private Cloud, Photo Vault's iCloud copy) it can restore from there. If it did not,
the photos are gone: restoring the whole iPhone from an iCloud backup will not bring them back, because the app left
them out of it.</p>

<p>Switching phones rather than deleting? See <a href="../blog/move-photo-vault-to-new-iphone.html">how to move a photo
vault to a new iPhone</a>.</p>

<h2>Sources</h2>
<ul>
<li>{a(BACKUP, "Apple, What does iCloud back up? (108770)")}, published 1 May 2025, read 25 October 2026.</li>
<li>{a(DEV_BACKUP, "Apple developer documentation, Optimizing your app's data for iCloud backup")}.</li>
<li>App Store listings (US) of Private Photo Vault, Keepsafe, SPV and PV, read 25 October 2026.</li>
<li>Photo Vault 1.3.0 code (backup exclusion, iCloud copy, backup file, decoy), read 25 October 2026.</li>
</ul>
""",
    faq=[
        ("If I delete a photo vault app, do I lose my photos?",
         "Usually yes. Vault apps keep their files out of the iPhone backup, so deleting the app deletes the photos unless "
         "you exported them or the app had its own cloud copy."),
        ("Can I get vault photos back from an iCloud backup?",
         "No, in most vault apps. They mark their files to be left out of iCloud and computer backups. Only the app's own "
         "copy (a cloud copy or an exported file) can bring them back."),
        ("Does reinstalling the vault bring the photos back?",
         "Only if the app had its own cloud copy. In Photo Vault, with the iCloud copy on, reinstalling with the same Apple ID "
         "offers to restore them; you set a new PIN."),
        ("Does Photo Vault's backup need the same Apple ID?",
         "The iCloud copy does. The backup file does not: it restores on any iPhone with its password."),
        ("What is never restored in Photo Vault?",
         "The decoy vault, the PIN and items in Recently Deleted."),
    ],
)

PV6_ES = dict(
    path="photo-vault/es/borrar-app-de-boveda-pierdo-las-fotos.html",
    app_name="Photo Vault: Hide Pics Video",
    date_iso=ISO, date=D,
    h1="Si borro la app de la bóveda de fotos, ¿pierdo las fotos? (2026)",
    desc=("Qué pasa con las fotos ocultas al borrar una app de bóveda en el iPhone, por qué la copia de iCloud del "
          "iPhone no las devuelve, qué dicen cuatro bóvedas populares en su ficha y cómo guardar una copia antes."),
    section="Guías", kicker="Guía de Photo Vault",
    standfirst=("Respuesta corta: en casi todas las bóvedas, sí. Borrar la app borra las fotos de dentro, y la copia de "
                "iCloud del iPhone no las tiene. Expórtalas o activa la copia de la propia app antes de borrarla."),
    tools=["Ajustes del iPhone", "Archivos"],
    intro=f"""
<p><strong>Hacemos Photo Vault, una app de bóveda, y sale en la tabla.</strong> Esta página vale para cualquier
bóveda: la regla es la misma en todas.</p>

<h2>Por qué la copia de iCloud no las salva</h2>

<p>La copia de iCloud normalmente incluye los datos de las apps ({a(BACKUP_ES, "Apple, ¿Qué incluye la copia de seguridad de iCloud?")}).
Pero una app puede marcar archivos para dejarlos fuera de las copias ({a(DEV_BACKUP, "documentación para desarrolladores de Apple")}).
Las bóvedas lo hacen a propósito, para que tus fotos privadas no acaben en una copia normal del iPhone o del ordenador.
El efecto: al borrar la app, iOS borra sus archivos y no hay copia que restaurar.</p>

<p>El álbum Oculto de Apple es distinto: forma parte de la fototeca y, con Fotos de iCloud, está en iCloud como
cualquier otra foto.</p>

<h2>Qué dicen cuatro bóvedas populares</h2>

<p>De la ficha de cada app en el App Store de EE. UU., leída el 25 de octubre de 2026:</p>

<div class="table-scroll">
<table>
<thead><tr><th>App</th><th>Copia propia en la nube</th><th>Qué dice la ficha sobre borrar la app</th></tr></thead>
<tbody>
<tr><td>{a(PPV, "Private Photo Vault")}</td><td>Cloud Vault, cifrada con una contraseña que solo sabes tú; la ficha dice que la versión gratuita no copia en Cloud Vault</td><td>Pide hacer copias para no perder datos si pierdes el móvil. Si olvidas la contraseña de Cloud Vault, la copia no se puede abrir</td></tr>
<tr><td>{a(KEEPSAFE, "Keepsafe (Secret Photo Vault)")}</td><td>Private Cloud de hasta 10.000 elementos, función Premium</td><td>No lo dice</td></tr>
<tr><td>{a(SPV, "SPV - Secret Photo Vault")}</td><td>Ninguna: lo guarda todo en el aparato</td><td>«Si borras la app, tus fotos y datos guardados en la app también se borran»</td></tr>
<tr><td>{a(PVA, "PV - Secret Photo Album")}</td><td>Sincronización y copia en Dropbox o Google Drive para miembros de pago</td><td>«Si nunca hiciste copia de los datos de la app, las fotos y vídeos desaparecen»</td></tr>
<tr><td>{a(PV_STORE, "Photo Vault")} (nuestra)</td><td>Copia opcional en tu propio iCloud, cifrada en el iPhone (activarla es Premium), y archivo de copia con contraseña</td><td>Sin copia, se pierde todo. Con la copia en iCloud o un archivo, se puede restaurar (detalle abajo)</td></tr>
</tbody>
</table>
</div>

<h2>Qué pasa exactamente en Photo Vault</h2>

<p>Leído del código de Photo Vault 1.3.0 el 25 de octubre de 2026:</p>
<ul>
<li><strong>Sin copia:</strong> borrar la app borra todas las fotos, vídeos y álbumes de la bóveda, y también
Eliminado recientemente. No están en la copia del iPhone.</li>
<li><strong>Con la copia en iCloud</strong> (viene apagada; activarla es parte de Premium): lo ya subido sigue en tu
espacio privado de iCloud aunque borres la app. Cada foto se cifra en el iPhone antes de salir, con una clave que
solo leen tus dispositivos. Reinstala la app con el <strong>mismo Apple ID</strong> y, con la bóveda vacía, te ofrece
restaurar desde iCloud. Restaurar no necesita Premium. Pones un PIN nuevo; las contraseñas de los álbumes vuelven.</li>
<li><strong>Con un archivo de copia</strong> (Configuración, iCloud y copia de seguridad, Exportar copia; no necesita Premium): un archivo
<code>.pvbackup</code> con fotos, vídeos, álbumes y sus contraseñas, cifrado con una contraseña de al menos 8 caracteres.
Guárdalo en Archivos, iCloud Drive o un Mac. Se restaura en cualquier iPhone, aunque tenga otro Apple ID, con esa
contraseña. Sin ella nadie puede abrirlo, tampoco nosotros.</li>
<li><strong>No vuelve nunca:</strong> la bóveda señuelo (no se sube ni se exporta), el PIN y lo que esté en
Eliminado recientemente.</li>
</ul>
""",
    steps=[
        ("Abre la bóveda antes de borrarla.",
         "Busca Exportar, Copia o Nube en sus ajustes. Si no hay nada, exporta las fotos a Fotos o a Archivos."),
        ("Haz la copia.",
         "En Photo Vault: Configuración, iCloud y copia de seguridad. Activa la copia en iCloud o usa Exportar copia con una contraseña que recuerdes."),
        ("Comprueba que la copia se abre.",
         "Abre algunas fotos y un vídeo de lo exportado, o restaura el archivo en otro aparato."),
        ("Apunta las contraseñas.",
         "La contraseña de Cloud Vault (Private Photo Vault) o la del archivo de copia (Photo Vault) no la puede recuperar nadie."),
        ("Cancela la suscripción si te vas.",
         "Borrar una app no la cancela: Ajustes, tu nombre, Suscripciones."),
        ("Solo entonces borra la app.",
         "Para recuperar, usa la copia de la propia app, no la copia del iPhone."),
    ],
    after=f"""
<h2>Si ya la borraste</h2>

<p>Reinstala la misma app y entra con el mismo Apple ID o cuenta. Si tenía copia propia en la nube (Cloud Vault de
Private Photo Vault, Private Cloud de Keepsafe, la copia en iCloud de Photo Vault) puede restaurar desde ahí. Si no la
tenía, las fotos se han perdido: restaurar el iPhone entero desde una copia de iCloud no las devuelve, porque la app las
dejó fuera.</p>

<p>¿Cambias de móvil en vez de borrar? Mira <a href="../../blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html">cómo pasar
la bóveda de fotos a un iPhone nuevo</a>.</p>

<h2>Fuentes</h2>
<ul>
<li>{a(BACKUP_ES, "Apple, ¿Qué incluye la copia de seguridad de iCloud? (108770)")}, publicado el 1 de mayo de 2025, leído el 25 de octubre de 2026.</li>
<li>{a(DEV_BACKUP, "Documentación para desarrolladores de Apple, Optimizing your app's data for iCloud backup")}.</li>
<li>Fichas del App Store (EE. UU.) de Private Photo Vault, Keepsafe, SPV y PV, leídas el 25 de octubre de 2026.</li>
<li>Código de Photo Vault 1.3.0 (exclusión de copias, copia en iCloud, archivo de copia, señuelo), leído el 25 de octubre de 2026.</li>
</ul>
""",
    faq=[
        ("Si borro una app de bóveda de fotos, ¿pierdo las fotos?",
         "Casi siempre, sí. Las bóvedas dejan sus archivos fuera de la copia del iPhone, así que borrar la app borra las fotos "
         "salvo que las hayas exportado o la app tuviera su propia copia en la nube."),
        ("¿Puedo recuperar las fotos de la bóveda desde una copia de iCloud?",
         "No, en casi todas las bóvedas. Marcan sus archivos para quedar fuera de las copias de iCloud y del ordenador. Solo la "
         "copia de la propia app (en la nube o en un archivo) las devuelve."),
        ("¿Reinstalar la bóveda devuelve las fotos?",
         "Solo si la app tenía copia propia en la nube. En Photo Vault, con la copia en iCloud activada, al reinstalar con el mismo "
         "Apple ID te ofrece restaurarlas; pones un PIN nuevo."),
        ("¿La copia de Photo Vault necesita el mismo Apple ID?",
         "La copia en iCloud, sí. El archivo de copia, no: se restaura en cualquier iPhone con su contraseña."),
        ("¿Qué no se recupera nunca en Photo Vault?",
         "La bóveda señuelo, el PIN y lo que esté en Eliminado recientemente."),
    ],
)

GUIDES = [(PV6_EN, PV6_ES)]
