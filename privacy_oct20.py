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
DATE = {"en": "20 October 2026", "ru": "20 октября 2026 г.", "zh": "2026年10月20日"}
HTML_LANG = {"en": "en", "ru": "ru", "zh": "zh-Hans"}
PINKU = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=aisagalab&amp;mt=8"

PATHS = {
    "keep": {"en": "blog/what-ai-chatbots-keep-when-you-delete-chats.html",
             "ru": "blog/ru/chto-ii-chaty-hranyat-posle-udaleniya.html",
             "zh": "blog/zh/ai-chatbots-what-they-keep-delete-export.html"},
    "net": {"en": "blog/do-local-ai-apps-send-data-mac-test.html",
            "ru": "blog/ru/chto-lokalnye-ii-prilozheniya-otpravlyayut-v-internet.html",
            "zh": "blog/zh/local-ai-apps-network-test-mac.html"},
}
SWITCH = {"en": "English", "ru": "Русский", "zh": "简体中文"}
FAQ_H = {"en": "Questions people ask", "ru": "Частые вопросы", "zh": "常见问题"}
GDPR = "blog/i-sent-openai-and-anthropic-a-gdpr-erasure-request.html"


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
             for l in ("en", "ru", "zh")]
    lines.append('    <link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, p["en"]))
    return "\n".join(lines)


def build(render, hreflang=None):
    import privacy_en
    import privacy_ru
    import privacy_zh
    by = {"en": privacy_en.ARTICLES, "ru": privacy_ru.ARTICLES, "zh": privacy_zh.ARTICLES}
    out = []
    byline = '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN
    for key in PATHS:
        for lang in ("en", "ru", "zh"):
            L = by[lang][key]
            path = PATHS[key][lang]
            others = [(SWITCH[o], _rel(path, PATHS[key][o])) for o in ("en", "ru", "zh") if o != lang]
            d = dict(pinku=PINKU, x=' target="_blank" rel="noopener"', date=DATE[lang],
                     gdpr=_rel(path, GDPR))
            d.update({"p_" + k: _rel(path, v[lang]) for k, v in PATHS.items()})
            head = _head(L["kicker"], L["h1"], L["standfirst"], byline + DATE[lang],
                         others[0][0], others[0][1])
            head = head.replace('>%s</a></span>' % others[0][0],
                                '>%s</a> &middot; <a href="%s">%s</a></span>'
                                % (others[0][0], others[1][1], others[1][0]))
            body = (head + '\n        <div class="article-body">' + (L["body"] % d)
                    + _faq_html(L["faq"], FAQ_H[lang])
                    + '</div>\n        <div class="article-body article-sources">' + (L["sources"] % d)
                    + '</div>')
            out.append(render(path=path, lang=HTML_LANG[lang], title=_plain(L["h1"]) + " | Saga Labs",
                              desc=_plain(L["desc"]), og_title=_plain(L["h1"]), body=body,
                              jsonld=_ld(L, lang, path), alternates=_alternates(key)))
    return out
