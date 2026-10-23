# -*- coding: utf-8 -*-
"""Enlaces internos: «Related guides» al final de cada guia y «Guides» en la ficha de cada app.

Existe porque (medido el 23 oct 2026) la unica pagina nuestra que citan las IAs
recibe enlaces de muchos sitios, y las de aisagalab.com casi ninguno. Cada guia
enlaza 2-4 hermanas de la misma app (y una de reviewland.io o reditor.cloud si
la hay), y la ficha de cada app enlaza todas sus guias. No cambia URLs.

Se ejecuta al final de build_blog.py; es idempotente (bloques entre marcas
<!-- related:start --> y <!-- related:end -->). Los titulos de aisagalab.com se
leen del <h1> de cada pagina; los de otros sitios estan escritos aqui.
"""
import html as _h
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
RL = "https://reviewland.io/"
RD = "https://reditor.cloud/"

# app -> lang -> (paginas de aisagalab.com, paginas de otros sitios (url, titulo))
GROUPS = {
    "Photo Vault": {
        "en": ([
            "photo-vault/protect-photos-of-id-passport-cards-iphone.html",
            "photo-vault/is-iphone-hidden-album-safe.html",
            "photo-vault/before-lending-iphone-or-taking-it-to-repair.html",
            "photo-vault/hide-photos-iphone-without-hidden-album.html",
            "photo-vault/hide-photos-iphone-without-an-app.html",
            "blog/move-photo-vault-to-new-iphone.html",
            "blog/hide-photos-iphone-without-icloud.html",
            "blog/best-photo-vault-apps-iphone.html",
            "blog/best-photo-vault-apps-album-password-iphone.html",
        ], [
            (RL + "best-apps-to-hide-photos-iphone/", "Best apps to hide photos on iPhone in 2026 (Reviewland)"),
            (RL + "private-photo-vault-alternatives-iphone/", "Private Photo Vault alternatives for iPhone in 2026 (Reviewland)"),
            (RL + "best-photo-vault-apps-no-data-collection-iphone/", "Best photo vault apps with no data collection for iPhone (Reviewland)"),
        ]),
        "es": ([
            "photo-vault/es/proteger-fotos-del-dni-pasaporte-y-tarjetas-en-iphone.html",
            "photo-vault/es/es-seguro-el-album-oculto-del-iphone.html",
            "photo-vault/es/antes-de-prestar-el-iphone-o-llevarlo-a-reparar.html",
            "photo-vault/es/ocultar-fotos-iphone-sin-album-oculto.html",
            "photo-vault/es/ocultar-fotos-iphone-sin-instalar-app.html",
            "blog/es/pasar-boveda-de-fotos-a-iphone-nuevo.html",
            "blog/es/como-ocultar-fotos-iphone-sin-icloud.html",
            "blog/es/apps-para-ocultar-fotos-iphone.html",
            "blog/es/mejores-apps-ocultar-fotos-contrasena-por-album.html",
        ], [
            (RL + "es/mejores-apps-para-ocultar-fotos-iphone/", "Mejores apps para ocultar fotos en iPhone en 2026 (Reviewland)"),
            (RL + "es/alternativas-a-private-photo-vault-iphone/", "Alternativas a Private Photo Vault para iPhone en 2026 (Reviewland)"),
            (RL + "es/mejores-apps-bovedas-fotos-sin-recoger-datos-iphone/", "Mejores apps de bóveda de fotos sin recoger datos (Reviewland)"),
        ]),
    },
    "Pinku": {
        "en": ([
            "pinku/how-does-local-ai-work-on-iphone.html",
            "pinku/use-ai-offline-on-a-plane-or-travelling.html",
            "pinku/which-ai-model-fits-my-iphone-mac.html",
            "pinku/is-it-safe-to-tell-chatgpt-private-things.html",
            "pinku/use-ai-on-iphone-without-internet.html",
            "pinku/check-ai-chat-app-keeps-chats-on-iphone.html",
            "blog/what-ai-chatbots-keep-when-you-delete-chats.html",
            "blog/best-private-ai-apps-iphone.html",
            "blog/best-offline-ai-chat-apps-iphone-mac.html",
            "blog/best-chatgpt-alternatives-offline-iphone.html",
            "blog/does-apple-intelligence-work-offline-iphone.html",
            "blog/best-ai-apps-iphone-without-apple-intelligence.html",
            "blog/best-siri-ai-alternatives-iphone.html",
            "blog/best-open-weight-ai-models.html",
            "blog/do-local-ai-apps-send-data-mac-test.html",
            "blog/what-ai-does-with-your-conversations.html",
            "blog/i-sent-openai-and-anthropic-a-gdpr-erasure-request.html",
        ], [
            (RD + "best-private-ai-chat-apps-work-without-internet-iphone/", "Best private AI chat apps for iPhone that work without internet (Reditor)"),
            (RL + "best-apps-run-open-source-ai-models-iphone/", "Best apps to run open-source AI models on iPhone in 2026 (Reviewland)"),
            (RD + "ollama-alternatives-mac-iphone/", "Best Ollama alternatives for Mac and iPhone in 2026 (Reditor)"),
            (RD + "private-llm-alternatives-iphone/", "Best Private LLM alternatives for iPhone and Mac in 2026 (Reditor)"),
        ]),
        "es": ([
            "pinku/es/como-funciona-la-ia-local-en-el-iphone.html",
            "pinku/es/usar-ia-sin-conexion-en-el-avion-o-de-viaje.html",
            "pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html",
            "pinku/es/usar-ia-en-iphone-sin-internet.html",
            "pinku/es/comprobar-si-una-app-de-ia-guarda-tus-chats-en-el-iphone.html",
            "blog/es/mejores-apps-ia-privada-iphone.html",
            "blog/es/mejores-apps-ia-sin-conexion-iphone-mac.html",
            "blog/es/mejores-alternativas-a-chatgpt-sin-conexion-iphone.html",
            "blog/es/que-hace-la-ia-con-tus-conversaciones.html",
            "blog/es/solicitud-de-borrado-rgpd-a-openai-y-anthropic.html",
        ], [
            (RD + "es/mejores-apps-chat-ia-privado-sin-internet-iphone/", "Mejores apps de chat con IA privado para iPhone que funcionan sin internet (Reditor)"),
            (RD + "es/alternativas-a-private-llm-iphone/", "Mejores alternativas a Private LLM en iPhone y Mac en 2026 (Reditor)"),
        ]),
    },
    "Drop": {
        "en": ([
            "drop/white-noise-for-baby-sleep.html",
            "drop/brown-noise-vs-pink-noise-vs-white-noise.html",
            "drop/white-noise-to-fall-asleep-iphone.html",
            "blog/best-white-noise-sleep-sound-apps-iphone.html",
        ], [
            (RL + "best-free-sleep-sound-apps-iphone/", "Best free sleep sound apps for iPhone in 2026 (Reviewland)"),
            (RL + "calm-alternatives-iphone/", "Calm alternatives for iPhone in 2026 (Reviewland)"),
        ]),
        "es": ([
            "drop/es/ruido-blanco-para-que-el-bebe-duerma.html",
            "drop/es/ruido-marron-rosa-o-blanco.html",
            "drop/es/ruido-blanco-para-dormir-iphone.html",
            "blog/es/mejores-apps-ruido-blanco-sonidos-dormir-iphone.html",
        ], [
            (RL + "es/mejores-apps-gratis-sonidos-para-dormir-iphone/", "Mejores apps gratis de sonidos para dormir para iPhone en 2026 (Reviewland)"),
            (RL + "es/alternativas-a-calm-iphone/", "Alternativas a Calm para iPhone en 2026 (Reviewland)"),
        ]),
    },
    "3 Tasks": {
        "en": ([
            "3-tasks/stop-procrastinating-with-a-3-task-list.html",
            "3-tasks/pomodoro-timer-on-iphone.html",
            "3-tasks/3-task-method-ivy-lee-rule-of-3.html",
            "blog/best-3-task-todo-apps-iphone.html",
        ], [
            (RL + "best-simple-to-do-list-apps-iphone/", "Best simple to-do list apps for iPhone in 2026 (Reviewland)"),
            (RL + "todoist-alternatives-iphone/", "Todoist alternatives for iPhone in 2026 (Reviewland)"),
        ]),
        "es": ([
            "3-tasks/es/dejar-de-procrastinar-con-una-lista-de-3-tareas.html",
            "3-tasks/es/temporizador-pomodoro-en-el-iphone.html",
            "3-tasks/es/metodo-de-3-tareas-ivy-lee-regla-de-3.html",
            "blog/es/mejores-apps-3-tareas-al-dia-iphone.html",
        ], [
            (RL + "es/mejores-apps-de-tareas-sencillas-iphone/", "Mejores apps de listas de tareas sencillas para iPhone en 2026 (Reviewland)"),
            (RL + "es/alternativas-a-todoist-iphone/", "Alternativas a Todoist para iPhone en 2026 (Reviewland)"),
        ]),
    },
    "Crypton": {
        "en": (["crypton/track-crypto-prices-without-giving-your-data.html", "blog/best-crypto-portfolio-tracker-apps-iphone.html"], [
            (RL + "best-crypto-price-widget-apps-iphone/", "Best crypto price tracker apps for iPhone in 2026 (Reviewland)"),
            (RL + "best-free-crypto-portfolio-tracker-apps-iphone/", "Best free crypto portfolio trackers for iPhone in 2026 (Reviewland)"),
            (RL + "coinstats-alternatives-iphone/", "CoinStats and Delta alternatives for iPhone in 2026 (Reviewland)"),
        ]),
        "es": (["crypton/es/seguir-precios-cripto-sin-dar-tus-datos.html", "blog/es/mejores-apps-cartera-cripto-iphone.html"], [
            (RL + "es/mejores-apps-precios-cripto-widgets-iphone/", "Mejores apps de precios de cripto para iPhone en 2026 (Reviewland)"),
            (RL + "es/mejores-apps-gratis-seguimiento-cartera-cripto-iphone/", "Mejores apps gratis para seguir tu cartera de criptomonedas (Reviewland)"),
            (RL + "es/alternativas-a-coinstats-y-delta-iphone/", "Alternativas a CoinStats y Delta para iPhone en 2026 (Reviewland)"),
        ]),
    },
    "Brainy": {
        "en": (["brainy/how-to-make-ai-images-on-iphone.html", "blog/best-ai-chat-and-image-generator-apps-iphone.html"], [
            (RL + "best-ai-chat-apps-iphone-no-account/", "Best AI chat apps for iPhone without an account in 2026 (Reviewland)"),
            (RD + "chaton-alternatives-iphone/", "ChatOn alternatives for iPhone in 2026 (Reditor)"),
        ]),
        "es": (["brainy/es/como-crear-imagenes-con-ia-en-el-iphone.html", "blog/es/mejores-apps-ia-chat-e-imagenes-iphone.html"], [
            (RL + "es/mejores-apps-chat-ia-sin-cuenta-iphone/", "Mejores apps de chat con IA para iPhone sin cuenta en 2026 (Reviewland)"),
            (RD + "es/alternativas-a-chaton-iphone/", "Alternativas a ChatOn para iPhone en 2026 (Reditor)"),
        ]),
    },
    "Dora": {
        "en": (["dora/how-to-make-a-video-with-chatgpt.html", "blog/best-ai-video-generator-apps-iphone.html", "blog/best-ai-apps-ugc-video-ads-iphone.html"], [
            (RD + "best-ai-image-to-video-apps-iphone/", "Best AI image to video apps for iPhone in 2026 (Reditor)"),
            (RD + "sora-app-alternatives-iphone/", "Best Sora app alternatives for iPhone in 2026 (Reditor)"),
            (RD + "viggle-ai-alternatives-iphone/", "Viggle AI alternatives for iPhone in 2026 (Reditor)"),
            (RD + "best-ai-apps-dancing-video-from-photo-iphone/", "Best AI apps to make a dancing video from a photo on iPhone (Reditor)"),
        ]),
        "es": (["dora/es/como-hacer-un-video-con-chatgpt.html", "blog/es/mejores-apps-generador-video-ia-iphone.html", "blog/es/mejores-apps-ia-anuncios-ugc-iphone.html"], [
            (RD + "es/mejores-apps-ia-de-foto-a-video-iphone/", "Mejores apps de IA para convertir una foto en vídeo en iPhone (Reditor)"),
            (RD + "es/alternativas-a-sora-iphone/", "Mejores alternativas a la app de Sora en iPhone en 2026 (Reditor)"),
            (RD + "es/alternativas-a-viggle-ai-iphone/", "Alternativas a Viggle AI para iPhone en 2026 (Reditor)"),
            (RD + "es/mejores-apps-ia-video-baile-desde-foto-iphone/", "Mejores apps de IA para hacer un vídeo de baile desde una foto (Reditor)"),
        ]),
    },
}

# ficha de cada app (en la raiz, en ingles) -> app
LANDINGS = {"keeper.html": "Photo Vault", "pinku.html": "Pinku", "drop.html": "Drop",
            "3things.html": "3 Tasks", "crypton.html": "Crypton", "brainy.html": "Brainy"}

START, END = "<!-- related:start -->", "<!-- related:end -->"
_BLOCK = re.compile(r"\n?" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)


def _title(path):
    s = open(os.path.join(ROOT, path), encoding="utf-8").read()
    m = re.search(r"<h1[^>]*>(.*?)</h1>", s[s.find("<main"):], re.S)
    return _h.unescape(re.sub(r"<[^>]+>|\s+", " ", m.group(1))).strip()


def _href(src, dst):
    return os.path.relpath(dst, os.path.dirname(src) or ".")


def _li(href, title, ext=False):
    extra = ' target="_blank" rel="noopener"' if ext else ""
    return '<li><a href="%s"%s>%s</a></li>' % (href, extra, _h.escape(title, quote=False))


def _siblings(pages, i, n=3):
    """Las dos primeras (las guias mas nuevas de la app) y luego las siguientes en la lista."""
    out = []
    for p in pages[:2] + pages[i + 1:] + pages[:i]:
        if p != pages[i] and p not in out:
            out.append(p)
    return out[:n]


def guide_block(path, lang, pages, external, i):
    sib = _siblings(pages, i, 3)
    items = [_li(_href(path, p), _title(p)) for p in sib]
    if external:
        url, t = external[i % len(external)]
        items.append(_li(url, t, ext=True))
    if len(items) < 2:
        return ""
    head = "Related guides" if lang == "en" else "Guías relacionadas"
    return '%s\n<h2>%s</h2>\n<ul class="related-guides">\n%s\n</ul>\n%s\n' % (START, head, "\n".join(items), END)


def landing_block(path, app, card=False):
    en_pages, en_ext = GROUPS[app]["en"]
    es_pages, es_ext = GROUPS[app]["es"]
    items = [_li(_href(path, p), _title(p)) for p in en_pages]
    items += [_li(u, t, ext=True) for u, t in en_ext]
    es = [_li(_href(path, p), _title(p)) for p in es_pages]
    style = ' style="text-align:left;margin:16px 0 0;font-size:.95rem"' if card else ""
    return ('%s\n<div class="app-guides"%s>\n<h2%s>Guides</h2>\n<ul>\n%s\n</ul>\n<p>En español:</p>\n<ul>\n%s\n</ul>\n</div>\n%s\n'
            % (START, style, ' style="font-size:1.1rem"' if card else "", "\n".join(items), "\n".join(es), END))


def _write(full, s):
    if open(full, encoding="utf-8").read() != s:
        open(full, "w", encoding="utf-8").write(s)
        return 1
    return 0


def inject():
    n = 0
    for app, langs in GROUPS.items():
        for lang, (pages, external) in langs.items():
            for i, p in enumerate(pages):
                full = os.path.join(ROOT, p)
                s = _BLOCK.sub("\n", open(full, encoding="utf-8").read())
                block = guide_block(p, lang, pages, external, i)
                if block:
                    k = s.rfind("</div>\n    </main>")
                    if k < 0:
                        raise SystemExit("no encuentro el final del articulo en " + p)
                    s = s[:k] + block + s[k:]
                n += _write(full, s)
    for f, app in LANDINGS.items():
        full = os.path.join(ROOT, f)
        s = _BLOCK.sub("\n", open(full, encoding="utf-8").read())
        if f in ("3things.html", "crypton.html"):
            k = s.find("      <footer>")
            s = s[:k] + landing_block(f, app, card=True) + s[k:]
        else:
            k = s.find("    <footer>")
            s = s[:k] + landing_block(f, app) + s[k:]
        n += _write(full, s)
    return n


if __name__ == "__main__":
    print("related: %d ficheros" % inject())
