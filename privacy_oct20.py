# -*- coding: utf-8 -*-
"""Dos articulos de privacidad del 20 oct 2026 en ingles, ruso y chino simplificado.

1. "keep": que guardan ChatGPT, Claude, Gemini y otros de tus chats y que pasa al
   borrarlos o exportarlos. Solo politicas y paginas de ayuda oficiales leidas el
   20 oct 2026 (las de OpenAI en Brave, porque help.openai.com da 403 a curl), y la
   solicitud RGPD de Marta del 15 abr 2026 (respuestas 17 abr y 16 may). Nada de
   exportaciones nuevas: Marta no pidio nada mas.
2. "net": experimento propio en un Mac (macOS 26.7.1, Apple silicon) el 20 oct
   2026 con nettop, lsof y los registros del sistema, sin root ni tcpdump: Ollama
   0.20.2 (Homebrew), LM Studio 0.4.26 (cask oficial) y Pinku para Mac 1.0.7
   compilado desde su codigo (commit 18ba3f5) con otro bundle id. Datos crudos en
   la sesion del 20 oct; resumen en ios-playbook/PLAYBOOK.md.

Idiomas por datos de Pinku (73 % ruso, 5 % chino). Pinku sale como una opcion
mas; su privacidad: los chats no salen del dispositivo y la etiqueta de Apple solo
lista historial de compras y un ID anonimo para Pro.
"""
import json
import os

from posts import LINKEDIN, _head, _jsonld, _faq_html

SITE = "https://aisagalab.com"
DATE_ISO = "2026-10-20"
MODIFIED_ISO = "2026-10-30"  # keep: ampliado el 30 oct (EN y ES nuevos) y corregido en RU y ZH
DATE = {"en": "20 October 2026", "ru": "20 октября 2026 г.", "zh": "2026年10月20日"}
DATE_KEEP = {"en": "30 October 2026", "es": "30 de octubre de 2026"}  # RU y ZH: leidas el 20, con 3 correcciones
META_KEEP = {"en": "20 October 2026, updated 30 October 2026", "es": "20 de octubre de 2026, actualizado el 30 de octubre de 2026",
             "ru": "20 октября 2026 г., обновлено 30 октября 2026 г.", "zh": "2026年10月20日，2026年10月30日更新"}
HTML_LANG = {"en": "en", "es": "es", "ru": "ru", "zh": "zh-Hans"}
LANGS = {"keep": ("en", "es", "ru", "zh"), "net": ("en", "ru", "zh")}
SPEED = {"en": "pinku/how-fast-llama-gemma-qwen-run-offline-on-iphone.html",
         "es": "pinku/es/velocidad-de-llama-gemma-y-qwen-sin-internet-en-el-iphone.html"}
PINKU = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=aisagalab&amp;mt=8"

PATHS = {
    "keep": {"en": "blog/what-ai-chatbots-keep-when-you-delete-chats.html",
             "es": "blog/es/se-borran-de-verdad-los-chats-de-ia.html",
             "ru": "blog/ru/chto-ii-chaty-hranyat-posle-udaleniya.html",
             "zh": "blog/zh/ai-chatbots-what-they-keep-delete-export.html"},
    "net": {"en": "blog/do-local-ai-apps-send-data-mac-test.html",
            "ru": "blog/ru/chto-lokalnye-ii-prilozheniya-otpravlyayut-v-internet.html",
            "zh": "blog/zh/local-ai-apps-network-test-mac.html"},
}
SWITCH = {"en": "English", "es": "Español", "ru": "Русский", "zh": "简体中文"}
FAQ_H = {"en": "Questions people ask", "es": "Preguntas frecuentes", "ru": "Частые вопросы", "zh": "常见问题"}
GDPR = "blog/i-sent-openai-and-anthropic-a-gdpr-erasure-request.html"
GDPR_ES = "blog/es/solicitud-de-borrado-rgpd-a-openai-y-anthropic.html"


def _plain(s):
    import html
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def _rel(here, there):
    return os.path.relpath(there, os.path.dirname(here))


def _ld(L, lang, path):
    art = json.loads(_jsonld(_plain(L["h1"]), _plain(L["desc"]), SITE + "/" + path, HTML_LANG[lang],
                             _plain(L["section"]), DATE_ISO))
    art.pop("@context")
    if path in PATHS["keep"].values():
        art["dateModified"] = MODIFIED_ISO
    graph = [art]
    if L.get("dataset"):
        graph.append(dict(L["dataset"], **{"@type": "Dataset", "inLanguage": HTML_LANG[lang],
                                            "url": SITE + "/" + path, "datePublished": DATE_ISO,
                                            "creator": {"@type": "Organization", "name": "Saga Labs",
                                                        "url": SITE + "/"}}))
    graph.append({
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]],
    })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def _alternates(key):
    p = PATHS[key]
    lines = ['    <link rel="alternate" hreflang="%s" href="%s/%s">' % (HTML_LANG[l], SITE, p[l])
             for l in LANGS[key]]
    lines.append('    <link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, p["en"]))
    return "\n".join(lines)


def build(render, hreflang=None):
    import privacy_en
    import privacy_es
    import privacy_ru
    import privacy_zh
    by = {"en": privacy_en.ARTICLES, "es": privacy_es.ARTICLES, "ru": privacy_ru.ARTICLES, "zh": privacy_zh.ARTICLES}
    out = []
    byline = '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN
    for key in PATHS:
        for lang in LANGS[key]:
            L = by[lang][key]
            path = PATHS[key][lang]
            others = [(SWITCH[o], _rel(path, PATHS[key][o])) for o in LANGS[key] if o != lang]
            d = dict(pinku=PINKU, x=' target="_blank" rel="noopener"', date=DATE_KEEP[lang] if key == "keep" and lang in ("en", "es") else DATE[lang],
                     gdpr=_rel(path, GDPR_ES if lang == "es" else GDPR),
                     speed=_rel(path, SPEED.get(lang, SPEED["en"])))
            d.update({"p_" + k: _rel(path, v.get(lang, v["en"])) for k, v in PATHS.items()})
            head = _head(L["kicker"], L["h1"], L["standfirst"], byline + (META_KEEP[lang] if key == "keep" else DATE[lang]),
                         others[0][0], others[0][1])
            head = head.replace('>%s</a></span>' % others[0][0],
                                '>%s</a>%s</span>' % (others[0][0], "".join(
                                    ' &middot; <a href="%s">%s</a>' % (h, n) for n, h in others[1:])))
            body = (head + '\n        <div class="article-body">' + (L["body"] % d)
                    + _faq_html(L["faq"], FAQ_H[lang])
                    + '</div>\n        <div class="article-body article-sources">' + (L["sources"] % d)
                    + '</div>')
            out.append(render(path=path, lang=HTML_LANG[lang], title=_plain(L["h1"]) + " | Saga Labs",
                              desc=_plain(L["desc"]), og_title=_plain(L["h1"]), body=body,
                              jsonld=_ld(L, lang, path), alternates=_alternates(key)))
    return out
