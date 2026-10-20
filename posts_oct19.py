# -*- coding: utf-8 -*-
"""Tres articulos del 19 oct 2026 (Pinku) en ingles, ruso y chino simplificado.

Idiomas elegidos con datos (ventas de App Store Connect, 60 dias hasta el 18 oct
2026): Pinku tuvo 1.300 descargas; ruso (RU, KZ, UA...) 944 (73 %), ingles 164
(13 %, y las 2 unicas compras de Pro, US y CA), chino 65 (5 %, CN 46), espanol
8 (0,6 %). Por eso no hay version en espanol.

El texto de cada idioma esta en oct19_en.py, oct19_ru.py y oct19_zh.py. Pinku sale
como una opcion mas (sin "ours" ni cuadro "por que es la 1.a"); la transparencia
va en una linea al final, en fuentes. Privacidad de Pinku: los chats no salen del
dispositivo; la etiqueta de Apple solo lista historial de compras y un ID de
usuario anonimo (RevenueCat sin appUserID) para las compras de Pro.

Datos comprobados el 19 oct 2026: support.apple.com 121115 y 127893, privacidad
de Apple Intelligence, guia de Atajos (Use Model), apple.com/os/ios, Metal 3
(102894), API de lookup de iTunes (us, ru, cn) y fichas web del App Store.
Sin rayas en el texto.
"""
import json

from posts import LINKEDIN, _head, _jsonld, _faq_html

SITE = "https://aisagalab.com"
DATE_ISO = "2026-10-19"
DATE = {"en": "19 October 2026", "ru": "19 октября 2026 г.", "zh": "2026年10月19日"}
HTML_LANG = {"en": "en", "ru": "ru", "zh": "zh-Hans"}
CC = {"en": "us", "ru": "ru", "zh": "cn"}

PINKU = "https://apps.apple.com/app/apple-store/id6754878073?pt=118348020&amp;ct=aisagalab&amp;mt=8"
PINKU_ID = "https://apps.apple.com/app/id6754878073"

IDS = dict(locally="6741426692", pocketpal="6502579498", privatellm="6448106860",
           enclave="6476614556", chatgpt="6448311069", gemini="6477489729",
           claude="6473753684", vibe="6740410176", alice="6621272550",
           deepseek="6737597349", perplexity="1668000334", doubao="6459478672",
           kimi="6474233312", qwen="6466733523")

_SUP = {"en": "en-us", "ru": "ru-ru", "zh": "zh-cn"}
_PRIV = {"en": "en", "ru": "ru", "zh": "zh-cn"}


def links(lang):
    cc = CC[lang]
    d = {k: "https://apps.apple.com/%s/app/id%s" % (cc, v) for k, v in IDS.items()}
    sup = _SUP[lang]
    d.update(
        **{k + "_id": v for k, v in IDS.items()},
        pinku=PINKU, x=' target="_blank" rel="noopener"', date=DATE[lang],
        gh="https://github.com/a-ghorbani/pocketpal-ai",
        reqs="https://support.apple.com/%s/121115" % sup,
        siri="https://support.apple.com/%s/127893" % sup,
        metal="https://support.apple.com/%s/102894" % sup,
        priv="https://www.apple.com/legal/privacy/data/%s/intelligence-engine/" % _PRIV[lang],
        sc="https://support.apple.com/guide/shortcuts/tpg3vrvwmclv/ios",
        ios="https://www.apple.com.cn/os/ios/" if lang == "zh" else "https://www.apple.com/os/ios/",
    )
    return d


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


def _ld(L, lang, path):
    art = json.loads(_jsonld(_plain(L["h1"]), _plain(L["desc"]), SITE + "/" + path, HTML_LANG[lang],
                             _plain(L["section"]), DATE_ISO))
    art.pop("@context")
    graph = [art]
    if L.get("rank"):
        graph.append({
            "@type": "ItemList", "name": _plain(L["h1"]),
            "itemListOrder": "https://schema.org/ItemListOrderAscending",
            "numberOfItems": len(L["rank"]),
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": u}
                                for i, (n, u) in enumerate(L["rank"])],
        })
    if L.get("steps"):
        graph.append({
            "@type": "HowTo", "name": _plain(L["steps_h"]), "inLanguage": HTML_LANG[lang],
            "step": [{"@type": "HowToStep", "position": i + 1, "name": _plain(n), "text": _plain(t)}
                     for i, (n, t) in enumerate(L["steps"])],
        })
    graph.append({
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]],
    })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def _articles():
    import oct19_en
    import oct19_ru
    import oct19_zh
    by = {"en": oct19_en.ARTICLES, "ru": oct19_ru.ARTICLES, "zh": oct19_zh.ARTICLES}
    keys = list(oct19_en.ARTICLES)
    return [{lang: by[lang][k] for lang in ("en", "ru", "zh")} for k in keys]


PATHS = {
    "offline": {"en": "blog/does-apple-intelligence-work-offline-iphone.html",
                "ru": "blog/ru/rabotaet-li-apple-intelligence-bez-interneta.html",
                "zh": "blog/zh/apple-intelligence-offline-iphone.html"},
    "noai": {"en": "blog/best-ai-apps-iphone-without-apple-intelligence.html",
             "ru": "blog/ru/luchshie-prilozheniya-ii-iphone-bez-apple-intelligence.html",
             "zh": "blog/zh/best-ai-apps-iphone-without-apple-intelligence.html"},
    "siri": {"en": "blog/best-siri-ai-alternatives-iphone.html",
             "ru": "blog/ru/luchshie-alternativy-siri-ai-iphone.html",
             "zh": "blog/zh/best-siri-ai-alternatives-iphone.html"},
}
SWITCH = {"en": "English", "ru": "Русский", "zh": "简体中文"}
FAQ_H = {"en": "Questions people ask", "ru": "Частые вопросы", "zh": "常见问题"}


def _alternates(key):
    p = PATHS[key]
    lines = ['    <link rel="alternate" hreflang="%s" href="%s/%s">' % (HTML_LANG[l], SITE, p[l])
             for l in ("en", "ru", "zh")]
    lines.append('    <link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, p["en"]))
    return "\n".join(lines)


def _rel(here, there):
    import os
    return os.path.relpath(there, os.path.dirname(here))


def build(render, hreflang=None):
    out = []
    byline = '<a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; ' % LINKEDIN
    for key, spec in zip(PATHS, _articles()):
        for lang in ("en", "ru", "zh"):
            L = spec[lang]
            path = PATHS[key][lang]
            others = [(SWITCH[o], _rel(path, PATHS[key][o])) for o in ("en", "ru", "zh") if o != lang]
            d = links(lang)
            d.update({"p_" + k: _rel(path, v[lang]) for k, v in PATHS.items()})
            if L.get("steps"):
                d["steps"] = _steps_html(L["steps"], L["steps_h"])
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
