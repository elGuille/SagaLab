# -*- coding: utf-8 -*-
"""Pinku: herramienta «qué modelo cabe en mi iPhone/iPad/Mac» y una página por modelo (EN, RU, ZH).

Por qué existe: la gente pregunta a las IAs y a Google «can my iPhone run Llama 3B»;
la respuesta exacta está en dos sitios nuestros (el catálogo público de Pinku y la
regla de memoria del código de la app). Esto la publica, generada, sin escribirla a mano.

Volver a generar cuando cambie el catálogo:
    python3 pinku_models.py --fetch    # baja https://pinku-models.web.app/models.json a data/
    python3 build_blog.py              # escribe las páginas (llama a build() de aquí)

De dónde sale cada dato (comprobado el 23 oct 2026):
- Modelos, tamaño (sizeGB), gratis/Pro (free), razonamiento, puntos fuertes: models.json
  (el que lee Pinku 1.1; los "status": "hidden" no se ofrecen y aquí no salen).
- Regla para listar un modelo: Pinku 1.1, OnboardingInstallModelView.modelMemoryThreshold
  = 0.6 (tamaño <= 60 % de la RAM física) y ModelMemory.fits() antes de cargar.
- Gratis: solo Gemma 3 1B (Models.requiresPro en 1.1 y la ficha del App Store 1.1).
- RAM de cada iPhone: Apple no la publica; se toma de Wikipedia «List of iPhone models»
  (revisión 1380986775). Metal 3: support.apple.com/en-us/102894 (iPhone 12 o posterior).
- Licencia, parámetros y fabricante: la ficha de Hugging Face del modelo base.
- Prueba de 5 preguntas: LLMEvaluator.chatSelfTest y docs/GROWTH_LOG.md de Pinku (19 oct).
Si aparece un modelo nuevo en models.json sin entrada en ED, el build se para y dice cuál.
"""
import html as _h
import json
import math
import os
import re
import sys
import urllib.request

import ct

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://aisagalab.com"
CATALOG_URL = "https://pinku-models.web.app/models.json"
CATALOG = os.path.join(ROOT, "data", "pinku-models.json")
DATE_ISO = "2026-10-23"
DATE = {"en": "23 October 2026", "ru": "23 октября 2026 г.", "zh": "2026年10月23日"}
LINKEDIN = "https://www.linkedin.com/in/maruta/"
PT = "118348020"
STORE = "https://apps.apple.com/app/apple-store/id6754878073?pt=%s&amp;ct=%%s&amp;mt=8" % PT
SHARE = 0.6        # OnboardingInstallModelView.modelMemoryThreshold (Pinku 1.1)
EDGE = 0.93        # la RAM que informa el dispositivo queda algo por debajo de la anunciada
LANGS = ("en", "ru", "zh")
HREFLANG = {"en": "en", "ru": "ru", "zh": "zh-Hans"}
HTML_LANG = {"en": "en", "ru": "ru", "zh": "zh-Hans"}

TOOL_PATH = {"en": "pinku/which-ai-model-fits-my-iphone-mac.html",
             "ru": "pinku/ru/kakaya-model-ii-podojdet-dlya-iphone-mac.html",
             "zh": "pinku/zh/which-ai-model-fits-my-iphone-mac.html"}
MODEL_DIR = {"en": "pinku/models/", "ru": "pinku/ru/models/", "zh": "pinku/zh/models/"}

WIKI = "https://en.wikipedia.org/wiki/List_of_iPhone_models"
METAL = "https://support.apple.com/en-us/102894"

# iPhone (RAM en GB según Wikipedia; Apple no la publica). Los que no tienen Metal 3
# (iPhone 11, SE de 2.ª generación y anteriores) no ejecutan Pinku.
IPHONES = [
    ("iPhone Duo", 12), ("iPhone 18 Pro Max", 12), ("iPhone 18 Pro", 12),
    ("iPhone 17 Pro Max", 12), ("iPhone 17 Pro", 12), ("iPhone Air", 12),
    ("iPhone 17", 8), ("iPhone 17e", 8),
    ("iPhone 16 Pro Max", 8), ("iPhone 16 Pro", 8), ("iPhone 16 Plus", 8), ("iPhone 16", 8), ("iPhone 16e", 8),
    ("iPhone 15 Pro Max", 8), ("iPhone 15 Pro", 8), ("iPhone 15 Plus", 6), ("iPhone 15", 6),
    ("iPhone 14 Pro Max", 6), ("iPhone 14 Pro", 6), ("iPhone 14 Plus", 6), ("iPhone 14", 6),
    ("iPhone SE (3rd generation)", 4),
    ("iPhone 13 Pro Max", 6), ("iPhone 13 Pro", 6), ("iPhone 13", 4), ("iPhone 13 mini", 4),
    ("iPhone 12 Pro Max", 6), ("iPhone 12 Pro", 6), ("iPhone 12", 4), ("iPhone 12 mini", 4),
]
IPAD_RAM = [4, 6, 8, 12, 16]
MAC_RAM = [8, 16, 24, 32]
TIERS = [4, 6, 8, 12]   # columnas de iPhone/iPad en la tabla sin JavaScript

LIC = {
    "gemma": ("Gemma Terms of Use", "https://ai.google.dev/gemma/terms"),
    "llama3.2": ("Llama 3.2 Community License", "https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt"),
    "apache-2.0": ("Apache 2.0", "https://www.apache.org/licenses/LICENSE-2.0"),
    "lfm1.0": ("LFM Open License v1.0", "https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE"),
}

# Datos editoriales por modelo (lo que models.json no trae). params: lo que dice la ficha.
ED = {
    "mlx-community/gemma-3-1b-it-qat-4bit": dict(
        slug="gemma-3-1b", short="Gemma 3 1B", maker="Google", base="google/gemma-3-1b-it", lic="gemma",
        params={"en": "1 billion", "ru": "1 млрд", "zh": "10 亿"},
        st={"ru": ["Разговор и повседневные вопросы", "Письмо и пересказ", "Перевод на 140+ языков"],
            "zh": ["聊天和日常问题", "写作和总结", "翻译 140 多种语言"]}),
    "mlx-community/Llama-3.2-1B-Instruct-4bit": dict(
        slug="llama-3-2-1b", short="Llama 3.2 1B", maker="Meta", base="meta-llama/Llama-3.2-1B-Instruct", lic="llama3.2",
        params={"en": "1.24 billion", "ru": "1,24 млрд", "zh": "12.4 亿"},
        st={"ru": ["Быстрые разговоры и перефразирование", "Пересказ коротких текстов", "Быстро работает на старых iPhone"],
            "zh": ["快速聊天和改写", "总结短文本", "在较旧的 iPhone 上也很快"]}),
    "mlx-community/Llama-3.2-3B-Instruct-4bit": dict(
        slug="llama-3-2-3b", short="Llama 3.2 3B", maker="Meta", base="meta-llama/Llama-3.2-3B-Instruct", lic="llama3.2",
        params={"en": "3.21 billion", "ru": "3,21 млрд", "zh": "32.1 亿"},
        st={"ru": ["Разговор и письмо", "Пересказ и выполнение инструкций", "Отвечает лучше, чем версия 1B"],
            "zh": ["聊天和写作", "总结和按指令完成任务", "回答比 1B 版本更好"]}),
    "mlx-community/Qwen3-0.6B-4bit": dict(
        slug="qwen3-0-6b", short="Qwen3 0.6B", maker="Qwen (Alibaba)", base="Qwen/Qwen3-0.6B", lic="apache-2.0",
        params={"en": "0.6 billion", "ru": "0,6 млрд", "zh": "6 亿"},
        st={"ru": ["Очень быстрая и маленькая", "Простые вопросы и перефразирование", "Может показывать ход рассуждений"],
            "zh": ["非常快，体积很小", "简单问题和改写", "可以显示推理过程"]}),
    "mlx-community/Qwen3-1.7B-4bit": dict(
        slug="qwen3-1-7b", short="Qwen3 1.7B", maker="Qwen (Alibaba)", base="Qwen/Qwen3-1.7B", lic="apache-2.0",
        params={"en": "1.7 billion", "ru": "1,7 млрд", "zh": "17 亿"},
        st={"ru": ["Пошаговые рассуждения", "Разговор и пересказ", "Сильна в китайском и 100+ языках"],
            "zh": ["一步步推理", "聊天和总结", "中文和 100 多种语言表现好"]}),
    "mlx-community/Qwen3-4B-4bit": dict(
        slug="qwen3-4b", short="Qwen3 4B", maker="Qwen (Alibaba)", base="Qwen/Qwen3-4B", lic="apache-2.0",
        params={"en": "4 billion", "ru": "4 млрд", "zh": "40 亿"},
        st={"ru": ["Рассуждения, математика и код", "Письмо и пересказ", "Перевод на 100+ языков"],
            "zh": ["推理、数学和代码", "写作和总结", "翻译 100 多种语言"]}),
    "mlx-community/Qwen3-8B-4bit": dict(
        slug="qwen3-8b", short="Qwen3 8B", maker="Qwen (Alibaba)", base="Qwen/Qwen3-8B", lic="apache-2.0",
        params={"en": "8.2 billion", "ru": "8,2 млрд", "zh": "82 亿"},
        st={"ru": ["Сложные рассуждения, математика и код", "Длинные подробные ответы", "Перевод на 100+ языков"],
            "zh": ["较难的推理、数学和代码", "详细的长回答", "翻译 100 多种语言"]}),
    "mlx-community/LFM2.5-1.2B-Instruct-4bit": dict(
        slug="lfm2-5-1-2b", short="LFM2.5 1.2B", maker="Liquid AI", base="LiquidAI/LFM2.5-1.2B-Instruct", lic="lfm1.0",
        params={"en": "1.17 billion", "ru": "1,17 млрд", "zh": "11.7 亿"}, test=5,
        st={"ru": ["Быстрый и экономный чат", "Пересказ и извлечение данных", "Мало расходует батарею"],
            "zh": ["快速、高效的聊天", "总结和提取信息", "耗电少"]}),
    "mlx-community/SmolLM3-3B-4bit": dict(
        slug="smollm3-3b", short="SmolLM3 3B", maker="Hugging Face", base="HuggingFaceTB/SmolLM3-3B", lic="apache-2.0",
        params={"en": "3 billion", "ru": "3 млрд", "zh": "30 亿"},
        st={"ru": ["Рассуждения и длинные тексты", "Разговор на 6 языках", "Пересказ"],
            "zh": ["推理和长文本", "支持 6 种语言聊天", "总结"]}),
    "mlx-community/gemma-3n-E2B-it-lm-4bit": dict(
        slug="gemma-3n-e2b", short="Gemma 3n E2B", maker="Google", base="google/gemma-3n-E2B-it", lic="gemma",
        params={"en": "about 2 billion effective (5.4 billion in the full original model, which also handles images and audio)",
                "ru": "около 2 млрд эффективных (5,4 млрд в полной исходной модели, которая работает ещё с изображениями и звуком)",
                "zh": "约 20 亿有效参数（完整原始模型为 54 亿，还能处理图片和音频）"},
        st={"ru": ["Разговор и письмо", "Перевод на 140+ языков", "Качество модели побольше при скромной памяти"],
            "zh": ["聊天和写作", "翻译 140 多种语言", "接近更大模型的质量，占用内存少"]}),
    "mlx-community/gemma-4-e2b-it-4bit": dict(
        slug="gemma-4-e2b", short="Gemma 4 E2B", maker="Google", base="google/gemma-4-E2B-it", lic="apache-2.0",
        lic_link="https://ai.google.dev/gemma/docs/gemma_4_license",
        params={"en": "2.3 billion effective (5.1 billion with embeddings)",
                "ru": "2,3 млрд эффективных (5,1 млрд вместе с эмбеддингами)",
                "zh": "23 亿有效参数（含嵌入层为 51 亿）"}, test=5,
        st={"ru": ["Разговор и письмо", "Письмо и пересказ", "Перевод на 140+ языков"],
            "zh": ["聊天和写作", "写作和总结", "翻译 140 多种语言"]}),
}

T = {
    "en": dict(
        kicker="Pinku tool", model_kicker="Pinku model",
        tool_h1="Which AI model fits my iPhone, iPad or Mac?",
        tool_title="Which AI model fits my iPhone, iPad or Mac? (Pinku)",
        tool_stand="Pick your device and see which of Pinku's %d on-device models it can run, with the download size and the memory each one needs.",
        tool_desc="Pick an iPhone (12 to iPhone Duo), iPad or Mac and see which of Pinku's %d offline AI models fit its memory: size, minimum RAM, test results and licence.",
        disc="<strong>Disclosure: we make Pinku.</strong> This tool uses Pinku's public model catalog (updated %s) and the rule the app itself uses to decide which models to list.",
        disc_model="<strong>Disclosure: we make Pinku, the app this page is about.</strong> The figures come from Pinku's public model catalog (updated %s) and the model's Hugging Face card.",
        pick="Your device", choose="Choose a device", g_iphone="iPhone", g_ipad="iPad (by memory)", g_mac="Mac with Apple silicon (by memory)",
        ipad_opt="iPad with %d GB", mac_opt="Mac with %d GB", mac_opt_more="Mac with %d GB or more",
        res_head="%s: %d of %d models", res_none="No models fit this device.",
        st_yes="Fits", st_edge="At the limit", st_no="Too big", free="free", pro="Pro",
        edge_note="At the limit: Pinku compares the model with the memory the device reports, which is a little below the advertised figure, so the model may or may not be listed.",
        noscript="Without JavaScript, use the table: each column is a memory size.",
        t_model="Model", t_size="Download", t_min="Memory needed", t_test="5-question test", t_plan="In Pinku",
        tier="%d GB", mac_col="Mac 8 GB+",
        h_table="All models at a glance", h_rule="How Pinku decides what your device can run",
        rule=["Pinku lists a model only if its download is at most 60% of the device's memory. That is why the table says, for example, that Qwen3 8B (4.7 GB) needs 7.9 GB.",
              "Before loading a model, the iPhone and iPad app also checks how much memory is free at that moment, so a listed model can still be refused if other apps are using memory. Closing them helps.",
              "Pinku needs iOS or iPadOS 18.6 or later and a device with Metal 3, which Apple lists for iPhone 12 or later, iPad Pro 11-inch (3rd generation), iPad Pro 12.9-inch (5th generation), iPad Air (4th generation), iPad mini (6th generation), iPad (9th generation) or later. On a Mac it needs Apple silicon and macOS 14 or later. The iPhone 11 and the iPhone SE (2nd generation) cannot run it."],
        h_ram="Memory of each iPhone", ram_note="Apple does not publish how much memory an iPhone has. These figures come from Wikipedia's list of iPhone models, which cites teardowns and regulatory filings, read on %s. iPad and Mac memory is on Apple's tech specs page for each model.",
        t_iphone="iPhone", t_ram="Memory",
        h_free="Which models are free", free_txt="Downloading Pinku and chatting with the default model, Gemma 3 1B, is free. Pinku Pro, a yearly subscription or a one-time purchase, lets you choose any other model.",
        get="Get Pinku on the App Store",
        h_models="The models", h_sources="Sources", h_faq="Questions people ask",
        test_none="Not in the test", test_val="%d of 5",
        test_expl="Pinku's developers ask new candidate models five factual questions on a Mac (capital of France, days in a leap year, author of Don Quixote, chemical symbol for gold, largest planet). It is five questions, not a benchmark.",
        faq_tool=[
            ("Can my iPhone run Qwen3 8B?", "Pinku lists Qwen3 8B (4.7 GB) when the device has at least 7.9 GB of memory. That means 12 GB iPhones (iPhone 17 Pro, iPhone Air, iPhone 18 Pro, iPhone Duo). On 8 GB iPhones it is right at the limit and may not be listed."),
            ("What is the best model for an iPhone with 4 GB of memory?", "On 4 GB iPhones (iPhone 12, 12 mini, 13, 13 mini, SE 3rd generation) Pinku lists models up to about 2.2 GB: Gemma 3 1B, Llama 3.2 1B and 3B, Qwen3 0.6B and 1.7B, LFM2.5 1.2B and SmolLM3 3B. Qwen3 4B is at the limit."),
            ("Do these models work without internet?", "Yes. You download a model once inside Pinku; after that every answer is generated on the device, in airplane mode too."),
            ("Why does my iPhone not show a model this tool says fits?", "The device reports slightly less memory than its advertised size, and Pinku also checks free memory before loading. Models marked at the limit can go either way."),
        ],
        m_h1="%s on iPhone, iPad and Mac: size, memory and devices",
        m_title="%s on iPhone and Mac: size, RAM needed, devices | Pinku",
        m_stand="%s by %s, as it runs offline in Pinku: a %s GB download that needs %s GB of memory. Which iPhones, iPads and Macs can run it, and how to try it.",
        m_desc="%s by %s offline on iPhone, iPad and Mac with Pinku: %s GB download, needs %s GB of memory, licence %s. Which devices run it.",
        f_maker="Made by", f_params="Parameters", f_size="Download size in Pinku", f_min="Memory needed to be listed", f_reason="Shows its reasoning",
        f_lic="Licence", f_card="Model card", f_build="Build Pinku downloads", f_test="5-question test", yes="Yes", no="No",
        h_good="What it is good at", good_src="As described in Pinku's catalog.",
        h_dev="Devices that run it", dev_iphone="iPhones", dev_edge="At the limit (may not be listed)", dev_ipad="iPad", dev_mac="Mac",
        dev_ipad_txt="An iPad with Metal 3 and at least %s GB of memory.", dev_mac_txt="Any Mac with Apple silicon and %s GB of memory or more, on macOS 14 or later.",
        dev_mac_all="Any Mac with Apple silicon and macOS 14 or later (they all have at least 8 GB).",
        dev_none="No iPhone has enough memory for it.",
        h_try="How to try it in Pinku",
        try_free=["Install Pinku from the App Store (iPhone, iPad or Mac).", "Open it: %s is the default model, so the first download is this one.", "When it finishes, start a chat. It works offline from then on, and it is free."],
        try_pro=["Install Pinku from the App Store (iPhone, iPad or Mac).", "Open the model list; Pinku only shows models your device has memory for.", "Choose %s. It needs Pinku Pro (yearly subscription or one-time purchase); chatting with Gemma 3 1B is free.", "Download it once. After that it works offline."],
        h_other="Other models in Pinku", tool_link="Which model fits my device? (tool)",
        faq_model=[
            ("Can my iPhone run %(m)s?", "%(dev)s"),
            ("Is %(m)s free in Pinku?", "%(plan)s"),
            ("Does %(m)s work offline?", "Yes. In Pinku you download it once (%(size)s GB) and every answer is then generated on the device, with no connection."),
        ],
        plan_free="Yes. It is Pinku's default model, and chatting with it is free.",
        plan_pro="It is one of the models that come with Pinku Pro, a yearly subscription or a one-time purchase. Chatting with Gemma 3 1B is free.",
        dev_ans="Pinku lists it on devices with at least %s GB of memory. iPhones: %s.",
        edge_ans=" At the limit, so it may not be listed: %s.", edge_only="Pinku lists it on devices with at least %s GB of memory. No iPhone is clearly above that; at the limit, so it may not be listed: %s.",
        dev_ans_none="No: it needs %s GB of memory, more than any iPhone has. It runs on a Mac with Apple silicon.",
        lang_names={"en": "English", "ru": "Русский", "zh": "中文"},
        src=[("Pinku model catalog (models.json)", "https://pinku-models.web.app/models.json"),
             ("Pinku on the App Store", "https://apps.apple.com/app/id6754878073"),
             ("Wikipedia, List of iPhone models", WIKI),
             ("Apple, Support for Metal on Apple devices", METAL)],
    ),
    "ru": dict(
        kicker="Инструмент Pinku", model_kicker="Модель в Pinku",
        tool_h1="Какая модель ИИ подойдёт для моего iPhone, iPad или Mac?",
        tool_title="Какая модель ИИ подойдёт для iPhone, iPad или Mac? (Pinku)",
        tool_stand="Выберите устройство и посмотрите, какие из %d локальных моделей Pinku оно потянет: размер загрузки и сколько памяти нужно каждой.",
        tool_desc="Выберите iPhone (от 12 до iPhone Duo), iPad или Mac и узнайте, какие из %d офлайн-моделей ИИ в Pinku поместятся в его память: размер, минимум ОЗУ, тест и лицензия.",
        disc="<strong>Важно: Pinku делаем мы.</strong> Инструмент берёт данные из открытого каталога моделей Pinku (обновлён %s) и правило, по которому само приложение решает, какие модели показать.",
        disc_model="<strong>Важно: Pinku, о котором эта страница, делаем мы.</strong> Цифры взяты из открытого каталога моделей Pinku (обновлён %s) и карточки модели на Hugging Face.",
        pick="Ваше устройство", choose="Выберите устройство", g_iphone="iPhone", g_ipad="iPad (по объёму памяти)", g_mac="Mac на Apple silicon (по объёму памяти)",
        ipad_opt="iPad с %d ГБ", mac_opt="Mac с %d ГБ", mac_opt_more="Mac с %d ГБ и больше",
        res_head="%s: %d из %d моделей", res_none="Ни одна модель не помещается.",
        st_yes="Подходит", st_edge="На пределе", st_no="Слишком большая", free="бесплатно", pro="Pro",
        edge_note="На пределе: Pinku сравнивает модель с памятью, которую сообщает устройство, а она чуть меньше заявленной, поэтому модель может появиться в списке, а может и нет.",
        noscript="Без JavaScript смотрите таблицу: каждый столбец — объём памяти.",
        t_model="Модель", t_size="Загрузка", t_min="Нужно памяти", t_test="Тест из 5 вопросов", t_plan="В Pinku",
        tier="%d ГБ", mac_col="Mac 8 ГБ+",
        h_table="Все модели в одной таблице", h_rule="Как Pinku решает, что потянет ваше устройство",
        rule=["Pinku показывает модель, только если её загрузка занимает не больше 60 % памяти устройства. Поэтому, например, для Qwen3 8B (4,7 ГБ) в таблице указано 7,9 ГБ.",
              "Перед загрузкой модели приложение на iPhone и iPad ещё проверяет, сколько памяти свободно в этот момент, так что модель из списка может не запуститься, если память заняли другие приложения. Помогает их закрыть.",
              "Pinku нужен iOS или iPadOS 18.6 и новее и устройство с Metal 3: по данным Apple, это iPhone 12 и новее, iPad Pro 11 дюймов (3-го поколения), iPad Pro 12,9 дюйма (5-го поколения), iPad Air (4-го поколения), iPad mini (6-го поколения), iPad (9-го поколения) и новее. На Mac нужен Apple silicon и macOS 14 и новее. На iPhone 11 и iPhone SE (2-го поколения) Pinku не работает."],
        h_ram="Память каждого iPhone", ram_note="Apple не публикует объём памяти iPhone. Эти цифры взяты из списка моделей iPhone в английской Википедии, который ссылается на разборы и регистрационные документы; проверено %s. Память iPad и Mac указана в технических характеристиках каждой модели на сайте Apple.",
        t_iphone="iPhone", t_ram="Память",
        h_free="Какие модели бесплатны", free_txt="Скачать Pinku и общаться с моделью по умолчанию, Gemma 3 1B, можно бесплатно. Pinku Pro — годовая подписка или разовая покупка — позволяет выбрать любую другую модель.",
        get="Скачать Pinku в App Store",
        h_models="Модели", h_sources="Источники", h_faq="Частые вопросы",
        test_none="Не участвовала", test_val="%d из 5",
        test_expl="Разработчики Pinku задают новым моделям-кандидатам пять вопросов на знание фактов на Mac (столица Франции, дней в високосном году, автор «Дон Кихота», химический символ золота, крупнейшая планета). Это пять вопросов, а не бенчмарк.",
        faq_tool=[
            ("Потянет ли мой iPhone Qwen3 8B?", "Pinku показывает Qwen3 8B (4,7 ГБ), если у устройства не меньше 7,9 ГБ памяти. Это iPhone с 12 ГБ (iPhone 17 Pro, iPhone Air, iPhone 18 Pro, iPhone Duo). На iPhone с 8 ГБ модель на пределе и может не появиться в списке."),
            ("Какая модель лучше для iPhone с 4 ГБ памяти?", "На iPhone с 4 ГБ (iPhone 12, 12 mini, 13, 13 mini, SE 3-го поколения) Pinku показывает модели примерно до 2,2 ГБ: Gemma 3 1B, Llama 3.2 1B и 3B, Qwen3 0.6B и 1.7B, LFM2.5 1.2B и SmolLM3 3B. Qwen3 4B — на пределе."),
            ("Работают ли эти модели без интернета?", "Да. Модель скачивается в Pinku один раз, после этого каждый ответ создаётся на устройстве, в том числе в авиарежиме."),
            ("Почему мой iPhone не показывает модель, которая здесь подходит?", "Устройство сообщает чуть меньше памяти, чем заявлено, а Pinku ещё проверяет свободную память перед загрузкой. Модели с пометкой «на пределе» могут не появиться."),
        ],
        m_h1="%s на iPhone, iPad и Mac: размер, память и устройства",
        m_title="%s на iPhone и Mac: размер, сколько нужно ОЗУ, устройства | Pinku",
        m_stand="%s от %s в офлайн-режиме в Pinku: загрузка %s ГБ, нужно %s ГБ памяти. На каких iPhone, iPad и Mac она работает и как её попробовать.",
        m_desc="%s от %s офлайн на iPhone, iPad и Mac в Pinku: загрузка %s ГБ, нужно %s ГБ памяти, лицензия %s. На каких устройствах работает.",
        f_maker="Разработчик", f_params="Параметры", f_size="Размер загрузки в Pinku", f_min="Память, чтобы модель появилась в списке", f_reason="Показывает рассуждения",
        f_lic="Лицензия", f_card="Карточка модели", f_build="Версия, которую скачивает Pinku", f_test="Тест из 5 вопросов", yes="Да", no="Нет",
        h_good="В чём она сильна", good_src="По описанию в каталоге Pinku.",
        h_dev="На каких устройствах работает", dev_iphone="iPhone", dev_edge="На пределе (может не появиться)", dev_ipad="iPad", dev_mac="Mac",
        dev_ipad_txt="iPad с Metal 3 и не меньше %s ГБ памяти.", dev_mac_txt="Любой Mac на Apple silicon с %s ГБ памяти и больше, macOS 14 и новее.",
        dev_mac_all="Любой Mac на Apple silicon с macOS 14 и новее (у всех не меньше 8 ГБ).",
        dev_none="Ни у одного iPhone не хватает для неё памяти.",
        h_try="Как попробовать в Pinku",
        try_free=["Установите Pinku из App Store (iPhone, iPad или Mac).", "Откройте его: %s — модель по умолчанию, поэтому первой скачается она.", "Когда загрузка закончится, начните чат. Дальше всё работает без интернета и бесплатно."],
        try_pro=["Установите Pinku из App Store (iPhone, iPad или Mac).", "Откройте список моделей: Pinku показывает только те, на которые хватает памяти.", "Выберите %s. Для неё нужен Pinku Pro (годовая подписка или разовая покупка); общение с Gemma 3 1B бесплатно.", "Скачайте её один раз. Дальше она работает без интернета."],
        h_other="Другие модели в Pinku", tool_link="Какая модель подойдёт для моего устройства? (инструмент)",
        faq_model=[
            ("Потянет ли мой iPhone %(m)s?", "%(dev)s"),
            ("%(m)s в Pinku бесплатна?", "%(plan)s"),
            ("Работает ли %(m)s без интернета?", "Да. В Pinku модель скачивается один раз (%(size)s ГБ), после этого каждый ответ создаётся на устройстве без подключения."),
        ],
        plan_free="Да. Это модель Pinku по умолчанию, общаться с ней бесплатно.",
        plan_pro="Она входит в Pinku Pro — годовую подписку или разовую покупку. Общение с Gemma 3 1B бесплатно.",
        dev_ans="Pinku показывает её на устройствах, где не меньше %s ГБ памяти. iPhone: %s.",
        edge_ans=" На пределе, может не появиться: %s.", edge_only="Pinku показывает её на устройствах, где не меньше %s ГБ памяти. Ни один iPhone не проходит с запасом; на пределе, может не появиться: %s.",
        dev_ans_none="Нет: ей нужно %s ГБ памяти, больше, чем есть у любого iPhone. Она работает на Mac с Apple silicon.",
        lang_names={"en": "English", "ru": "Русский", "zh": "中文"},
        src=[("Каталог моделей Pinku (models.json)", "https://pinku-models.web.app/models.json"),
             ("Pinku в App Store", "https://apps.apple.com/ru/app/id6754878073"),
             ("Wikipedia, List of iPhone models", WIKI),
             ("Apple, Support for Metal on Apple devices", METAL)],
    ),
    "zh": dict(
        kicker="Pinku 工具", model_kicker="Pinku 模型",
        tool_h1="我的 iPhone、iPad 或 Mac 能运行哪个 AI 模型？",
        tool_title="我的 iPhone、iPad 或 Mac 能运行哪个 AI 模型？(Pinku)",
        tool_stand="选择你的设备，看看 Pinku 的 %d 个本机模型中它能运行哪些，以及每个模型的下载大小和所需内存。",
        tool_desc="选择 iPhone（iPhone 12 到 iPhone Duo）、iPad 或 Mac，查看 Pinku 的 %d 个离线 AI 模型中哪些装得下：大小、最低内存、测试结果和许可证。",
        disc="<strong>说明：Pinku 是我们开发的。</strong>本工具使用 Pinku 公开的模型目录（更新于 %s），以及应用本身决定显示哪些模型的规则。",
        disc_model="<strong>说明：本页介绍的 Pinku 是我们开发的。</strong>数据来自 Pinku 公开的模型目录（更新于 %s）和该模型在 Hugging Face 上的模型卡。",
        pick="你的设备", choose="选择设备", g_iphone="iPhone", g_ipad="iPad（按内存）", g_mac="Apple 芯片 Mac（按内存）",
        ipad_opt="%d GB 内存的 iPad", mac_opt="%d GB 内存的 Mac", mac_opt_more="%d GB 或以上内存的 Mac",
        res_head="%s：%d / %d 个模型", res_none="没有模型能装得下。",
        st_yes="可以", st_edge="刚好在边界", st_no="太大", free="免费", pro="Pro",
        edge_note="刚好在边界：Pinku 用设备报告的内存来比较，而这个数字比标称内存略低，所以这个模型可能显示，也可能不显示。",
        noscript="没有 JavaScript 时请看表格：每一列是一种内存大小。",
        t_model="模型", t_size="下载大小", t_min="所需内存", t_test="5 题测试", t_plan="在 Pinku 中",
        tier="%d GB", mac_col="Mac 8 GB+",
        h_table="所有模型一览", h_rule="Pinku 如何判断你的设备能运行什么",
        rule=["只有当模型的下载大小不超过设备内存的 60% 时，Pinku 才会显示它。所以表中写着，例如 Qwen3 8B（4.7 GB）需要 7.9 GB。",
              "在 iPhone 和 iPad 上，加载模型之前应用还会检查当时还有多少空闲内存，所以如果其他 App 占用了内存，列表中的模型也可能无法加载。关掉它们会有帮助。",
              "Pinku 需要 iOS 或 iPadOS 18.6 及以上，并且设备支持 Metal 3。Apple 列出的是 iPhone 12 及以后、iPad Pro 11 英寸（第三代）、iPad Pro 12.9 英寸（第五代）、iPad Air（第四代）、iPad mini（第六代）、iPad（第九代）及以后。在 Mac 上需要 Apple 芯片和 macOS 14 及以上。iPhone 11 和 iPhone SE（第二代）无法运行。"],
        h_ram="每款 iPhone 的内存", ram_note="Apple 不公布 iPhone 的内存大小。这些数字来自英文维基百科的 iPhone 机型列表，该列表引用拆机报告和监管文件，查阅于 %s。iPad 和 Mac 的内存可在 Apple 网站上各机型的技术规格页查到。",
        t_iphone="iPhone", t_ram="内存",
        h_free="哪些模型免费", free_txt="下载 Pinku 并使用默认模型 Gemma 3 1B 聊天是免费的。Pinku Pro（按年订阅或一次性购买）可以选择任何其他模型。",
        get="在 App Store 获取 Pinku",
        h_models="模型", h_sources="来源", h_faq="常见问题",
        test_none="未参加测试", test_val="5 题答对 %d 题",
        test_expl="Pinku 的开发者会在 Mac 上用五个事实问题测试候选模型（法国首都、闰年天数、《堂吉诃德》作者、金的化学符号、最大的行星）。这只是五个问题，不是基准测试。",
        faq_tool=[
            ("我的 iPhone 能运行 Qwen3 8B 吗？", "设备至少有 7.9 GB 内存时，Pinku 才会显示 Qwen3 8B（4.7 GB）。也就是 12 GB 内存的 iPhone（iPhone 17 Pro、iPhone Air、iPhone 18 Pro、iPhone Duo）。在 8 GB 的 iPhone 上它刚好在边界，可能不会显示。"),
            ("4 GB 内存的 iPhone 适合哪个模型？", "在 4 GB 的 iPhone（iPhone 12、12 mini、13、13 mini、SE 第三代）上，Pinku 显示约 2.2 GB 以内的模型：Gemma 3 1B、Llama 3.2 1B 和 3B、Qwen3 0.6B 和 1.7B、LFM2.5 1.2B 以及 SmolLM3 3B。Qwen3 4B 刚好在边界。"),
            ("这些模型不联网也能用吗？", "能。在 Pinku 里下载一次模型后，每个回答都在设备上生成，飞行模式下也可以。"),
            ("为什么我的 iPhone 没有显示这里说能运行的模型？", "设备报告的内存比标称略少，而且 Pinku 在加载前还会检查空闲内存。标为“刚好在边界”的模型可能显示，也可能不显示。"),
        ],
        m_h1="%s 在 iPhone、iPad 和 Mac 上：大小、内存和设备",
        m_title="%s 在 iPhone 和 Mac 上：大小、所需内存、设备 | Pinku",
        m_stand="%s（%s）在 Pinku 中离线运行：下载 %s GB，需要 %s GB 内存。哪些 iPhone、iPad 和 Mac 能运行，以及怎么试用。",
        m_desc="在 Pinku 中离线运行 %s（%s）：下载 %s GB，需要 %s GB 内存，许可证 %s。哪些 iPhone、iPad 和 Mac 能运行。",
        f_maker="开发者", f_params="参数", f_size="在 Pinku 中的下载大小", f_min="显示所需内存", f_reason="显示推理过程",
        f_lic="许可证", f_card="模型卡", f_build="Pinku 下载的版本", f_test="5 题测试", yes="是", no="否",
        h_good="擅长什么", good_src="根据 Pinku 模型目录中的描述。",
        h_dev="能运行的设备", dev_iphone="iPhone", dev_edge="刚好在边界（可能不显示）", dev_ipad="iPad", dev_mac="Mac",
        dev_ipad_txt="支持 Metal 3、至少 %s GB 内存的 iPad。", dev_mac_txt="任何 %s GB 或以上内存、运行 macOS 14 及以上的 Apple 芯片 Mac。",
        dev_mac_all="任何运行 macOS 14 及以上的 Apple 芯片 Mac（内存都至少 8 GB）。",
        dev_none="没有哪款 iPhone 的内存够用。",
        h_try="如何在 Pinku 中试用",
        try_free=["从 App Store 安装 Pinku（iPhone、iPad 或 Mac）。", "打开应用：%s 是默认模型，所以第一个下载的就是它。", "下载完成后开始聊天。之后离线也能用，而且免费。"],
        try_pro=["从 App Store 安装 Pinku（iPhone、iPad 或 Mac）。", "打开模型列表；Pinku 只显示你的设备内存够用的模型。", "选择 %s。它需要 Pinku Pro（按年订阅或一次性购买）；使用 Gemma 3 1B 聊天是免费的。", "下载一次，之后离线可用。"],
        h_other="Pinku 中的其他模型", tool_link="我的设备适合哪个模型？（工具）",
        faq_model=[
            ("我的 iPhone 能运行 %(m)s 吗？", "%(dev)s"),
            ("%(m)s 在 Pinku 中免费吗？", "%(plan)s"),
            ("%(m)s 不联网能用吗？", "能。在 Pinku 中下载一次（%(size)s GB）后，每个回答都在设备上生成，不需要网络。"),
        ],
        plan_free="是的。它是 Pinku 的默认模型，用它聊天免费。",
        plan_pro="它属于 Pinku Pro（按年订阅或一次性购买）包含的模型。使用 Gemma 3 1B 聊天是免费的。",
        dev_ans="在至少有 %s GB 内存的设备上，Pinku 会显示它。iPhone：%s。",
        edge_ans="刚好在边界、可能不显示的：%s。", edge_only="在至少有 %s GB 内存的设备上，Pinku 会显示它。没有哪款 iPhone 明显高于这个数；刚好在边界、可能不显示的：%s。",
        dev_ans_none="不能：它需要 %s GB 内存，超过所有 iPhone。它可以在 Apple 芯片 Mac 上运行。",
        lang_names={"en": "English", "ru": "Русский", "zh": "中文"},
        src=[("Pinku 模型目录（models.json）", "https://pinku-models.web.app/models.json"),
             ("App Store 上的 Pinku", "https://apps.apple.com/cn/app/id6754878073"),
             ("Wikipedia, List of iPhone models", WIKI),
             ("Apple, Support for Metal on Apple devices", METAL)],
    ),
}


# ---------------------------------------------------------------- datos

def fetch():
    data = urllib.request.urlopen(CATALOG_URL, timeout=20).read()
    json.loads(data)
    os.makedirs(os.path.dirname(CATALOG), exist_ok=True)
    open(CATALOG, "wb").write(data)
    print("models.json guardado en", CATALOG)


def models():
    cat = json.load(open(CATALOG, encoding="utf-8"))
    out = []
    for m in cat["models"]:
        if m.get("status") == "hidden":
            continue
        if m["id"] not in ED:
            raise SystemExit("pinku_models: modelo nuevo en models.json sin datos en ED: %s" % m["id"])
        e = dict(ED[m["id"]])
        e.update(id=m["id"], size=m["sizeGB"], free=bool(m.get("free")), reasoning=bool(m.get("reasoning")),
                 strengths_en=m.get("strengths", []), quality=m.get("quality", 0))
        e["min"] = math.ceil(m["sizeGB"] / SHARE * 10) / 10
        out.append(e)
    out.sort(key=lambda e: (e["size"], e["short"]))
    return cat.get("updated", ""), out


def status(size, ram, ios=True):
    limit = SHARE * ram + 1e-9
    if size > limit:
        return "no"
    if ios and size > limit * EDGE:
        return "edge"
    return "yes"


def num(x, lang):
    s = ("%.1f" % x).rstrip("0").rstrip(".") if x != int(x) else "%d" % x
    return s.replace(".", ",") if lang == "ru" else s


def fdate(iso, lang):
    y, mo, d = (int(x) for x in iso.split("-"))
    if lang == "ru":
        ms = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
        return "%d %s %d г." % (d, ms[mo - 1], y)
    if lang == "zh":
        return "%d年%d月%d日" % (y, mo, d)
    ms = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return "%d %s %d" % (d, ms[mo - 1], y)


def esc(s):
    return _h.escape(s, quote=True)


def model_path(e, lang):
    return MODEL_DIR[lang] + e["slug"] + ".html"


def rel(src, dst):
    return os.path.relpath(dst, os.path.dirname(src))


def store(ctv):
    return STORE % ctv


def lic(e):
    name, link = LIC[e["lic"]]
    return name, e.get("lic_link", link)


def iphone_name(n, lang):
    if lang == "ru":
        return n.replace("(3rd generation)", "(3-го поколения)")
    if lang == "zh":
        return n.replace("(3rd generation)", "（第三代）")
    return n


# ---------------------------------------------------------------- piezas

def alternates(paths):
    out = ['    <link rel="alternate" hreflang="%s" href="%s/%s">' % (HREFLANG[l], SITE, paths[l]) for l in LANGS]
    out.append('    <link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, paths["en"]))
    return "\n".join(out)


def header(lang, kicker, h1, stand, path, paths):
    t = T[lang]
    others = " &middot; ".join('<a href="%s" hreflang="%s">%s</a>' % (rel(path, paths[l]), HREFLANG[l], t["lang_names"][l])
                               for l in LANGS if l != lang)
    return ('        <p class="article-kicker">%s</p>\n        <h1>%s</h1>\n        <p class="article-standfirst">%s</p>\n'
            '        <p class="article-meta"><a href="%s" rel="author me noopener" target="_blank">Maruta G</a> &middot; %s\n'
            '            <span class="lang-switch"> &middot; %s</span>\n        </p>\n'
            % (esc(kicker), esc(h1), esc(stand), LINKEDIN, DATE[lang], others))


def faq_html(lang, faq):
    t = T[lang]
    return "<h2>%s</h2>\n" % t["h_faq"] + "".join("<h3>%s</h3>\n<p>%s</p>\n" % (esc(q), esc(a)) for q, a in faq)


def sources_html(lang, extra=()):
    t = T[lang]
    items = list(t["src"]) + list(extra)
    return ('<div class="article-sources">\n<h2>%s</h2>\n<ul>\n%s\n</ul>\n<p>%s</p>\n</div>\n'
            % (t["h_sources"], "\n".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, esc(n)) for n, u in items),
               {"en": "Checked on ", "ru": "Проверено ", "zh": "核对于 "}[lang] + DATE[lang] + ("." if lang != "zh" else "。")))


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def ld(graph):
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def plan_cell(e, lang):
    t = T[lang]
    return t["free"] if e["free"] else t["pro"]


def test_cell(e, lang):
    t = T[lang]
    return t["test_val"] % e["test"] if e.get("test") is not None else t["test_none"]


# ---------------------------------------------------------------- herramienta

TOOL_CSS = """<style>
.fit-tool { margin: 8px 0 32px; padding: 18px 20px; border: 1px solid rgba(128,128,128,.28); border-radius: 10px; }
.fit-tool label { display: block; font-weight: 600; margin-bottom: 8px; }
.fit-tool select { font: inherit; padding: 8px 10px; border-radius: 8px; max-width: 100%; }
.fit-out h3 { margin: 20px 0 10px; font-size: 1.05rem; }
.fit-out ul { list-style: none; padding: 0; margin: 0; }
.fit-out li { margin: 0 0 8px; }
.fit-tag { display: inline-block; font-size: .8rem; padding: 1px 8px; border-radius: 999px; border: 1px solid currentColor; margin-left: 6px; opacity: .8; }
.fit-yes { font-weight: 600; }
.fit-edge { opacity: .75; }
.fit-no { opacity: .4; }
</style>
"""

TOOL_JS = """<script>
(function () {
  var D = JSON.parse(document.getElementById('fit-data').textContent);
  var sel = document.getElementById('fit-device'), out = document.getElementById('fit-out');
  function status(size, ram, ios) {
    var lim = D.share * ram + 1e-9;
    if (size > lim) return 'no';
    if (ios && size > lim * D.edge) return 'edge';
    return 'yes';
  }
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function show() {
    var v = sel.value; out.innerHTML = '';
    if (!v) return;
    var p = v.split('|'), ram = parseFloat(p[1]), ios = p[0] !== 'mac', name = sel.options[sel.selectedIndex].text;
    var rows = D.models.map(function (m) { return [m, status(m.size, ram, ios)]; });
    var ok = rows.filter(function (r) { return r[1] !== 'no'; });
    var h = '<h3>' + esc(D.t.head.replace('%s', name).replace('%d', ok.length).replace('%d', D.models.length)) + '</h3>';
    if (!ok.length) h += '<p>' + esc(D.t.none) + '</p>';
    h += '<ul>';
    rows.forEach(function (r) {
      var m = r[0], s = r[1];
      h += '<li class="fit-' + s + '"><a href="' + m.href + '">' + esc(m.name) + '</a> &middot; ' + esc(m.sizeTxt) + ' &middot; ' + esc(m.plan) +
           '<span class="fit-tag">' + esc(D.t[s]) + '</span></li>';
    });
    h += '</ul>';
    if (rows.some(function (r) { return r[1] === 'edge'; })) h += '<p class="fit-edge">' + esc(D.t.edgeNote) + '</p>';
    out.innerHTML = h;
    try { history.replaceState(null, '', '#' + encodeURIComponent(v)); } catch (e) {}
  }
  sel.addEventListener('change', show);
  if (location.hash) { var v = decodeURIComponent(location.hash.slice(1)); for (var i = 0; i < sel.options.length; i++) if (sel.options[i].value === v) { sel.value = v; } }
  show();
})();
</script>
"""


def tool_page(lang, updated, ms):
    t = T[lang]
    path = TOOL_PATH[lang]
    n = len(ms)
    ctv = "tool-fit" + ("" if lang == "en" else "-" + lang)
    sz = lambda x: num(x, lang) + (" ГБ" if lang == "ru" else " GB")
    # selector
    opts = ['<option value="">%s</option>' % esc(t["choose"]), '<optgroup label="%s">' % esc(t["g_iphone"])]
    opts += ['<option value="iphone|%d">%s</option>' % (r, esc(iphone_name(nm, lang))) for nm, r in IPHONES]
    opts += ['</optgroup>', '<optgroup label="%s">' % esc(t["g_ipad"])]
    opts += ['<option value="ipad|%d">%s</option>' % (r, esc(t["ipad_opt"] % r)) for r in IPAD_RAM]
    opts += ['</optgroup>', '<optgroup label="%s">' % esc(t["g_mac"])]
    opts += ['<option value="mac|%d">%s</option>' % (r, esc((t["mac_opt_more"] if r == MAC_RAM[-1] else t["mac_opt"]) % r)) for r in MAC_RAM]
    opts.append('</optgroup>')
    data = {"share": SHARE, "edge": EDGE,
            "t": {"head": t["res_head"], "none": t["res_none"], "yes": t["st_yes"], "edge": t["st_edge"], "no": t["st_no"], "edgeNote": t["edge_note"]},
            "models": [{"name": e["short"], "size": e["size"], "sizeTxt": sz(e["size"]), "plan": plan_cell(e, lang),
                        "href": rel(path, model_path(e, lang))} for e in ms]}
    tool = ('<div class="fit-tool">\n<form onsubmit="return false"><label for="fit-device">%s</label>\n<select id="fit-device">\n%s\n</select></form>\n'
            '<div id="fit-out" class="fit-out" aria-live="polite"></div>\n<noscript><p>%s</p></noscript>\n</div>\n'
            % (t["pick"], "\n".join(opts), t["noscript"]))
    # tabla completa (funciona sin JavaScript)
    mark = {"yes": "&#10003;", "edge": "&#8776;", "no": "&ndash;"}
    head = "".join("<th>%s</th>" % (t["tier"] % r) for r in TIERS) + "<th>%s</th>" % t["mac_col"]
    rows = []
    for e in ms:
        cells = "".join('<td title="%s">%s</td>' % (t["st_" + status(e["size"], r)], mark[status(e["size"], r)]) for r in TIERS)
        cells += "<td>%s</td>" % mark[status(e["size"], 8, ios=False)]
        rows.append('<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td>%s<td>%s</td><td>%s</td></tr>'
                    % (rel(path, model_path(e, lang)), esc(e["short"]), sz(e["size"]), sz(e["min"]), cells, plan_cell(e, lang), test_cell(e, lang)))
    legend = "&#10003; %s &middot; &#8776; %s &middot; &ndash; %s" % (t["st_yes"], t["st_edge"], t["st_no"])
    table = ('<h2>%s</h2>\n<div class="table-scroll"><table>\n<thead><tr><th>%s</th><th>%s</th><th>%s</th>%s<th>%s</th><th>%s</th></tr></thead>\n<tbody>\n%s\n</tbody>\n</table></div>\n'
             '<p class="article-note">%s. %s %s</p>\n'
             % (t["h_table"], t["t_model"], t["t_size"], t["t_min"], head, t["t_plan"], t["t_test"], "\n".join(rows), legend, t["edge_note"], t["test_expl"]))
    rule = "<h2>%s</h2>\n" % t["h_rule"] + "".join("<p>%s</p>\n" % esc(p) for p in t["rule"])
    ram = ('<h2>%s</h2>\n<div class="table-scroll"><table>\n<thead><tr><th>%s</th><th>%s</th></tr></thead>\n<tbody>\n%s\n</tbody>\n</table></div>\n<p>%s</p>\n'
           % (t["h_ram"], t["t_iphone"], t["t_ram"],
              "\n".join("<tr><td>%s</td><td>%s</td></tr>" % (esc(iphone_name(nm, lang)), t["tier"] % r) for nm, r in IPHONES),
              t["ram_note"] % DATE[lang]))
    free = '<h2>%s</h2>\n<p>%s</p>\n<p><a href="%s">%s</a></p>\n' % (t["h_free"], t["free_txt"], store(ctv), t["get"])
    faq = t["faq_tool"]
    body = (header(lang, t["kicker"], t["tool_h1"], t["tool_stand"] % n, path, TOOL_PATH)
            + '        <div class="article-body">\n' + TOOL_CSS
            + "<p>%s</p>\n" % (t["disc"] % fdate(updated, lang))
            + tool
            + '<script type="application/json" id="fit-data">%s</script>\n' % json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
            + table + rule + ram + free + faq_html(lang, faq) + sources_html(lang) + TOOL_JS
            + "</div>")
    url = "%s/%s" % (SITE, path)
    graph = [{"@type": "WebApplication", "name": t["tool_h1"], "url": url, "inLanguage": HREFLANG[lang],
              "description": t["tool_desc"] % n, "applicationCategory": "UtilitiesApplication",
              "operatingSystem": "Any (web browser)", "isAccessibleForFree": True,
              "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
              "dateModified": DATE_ISO,
              "publisher": {"@type": "Organization", "name": "Saga Labs", "url": SITE},
              "about": {"@type": "SoftwareApplication", "name": "Pinku", "operatingSystem": "iOS, iPadOS, macOS",
                        "applicationCategory": "UtilitiesApplication", "url": "https://apps.apple.com/app/id6754878073"}},
             faq_ld(faq)]
    return dict(path=path, lang=HTML_LANG[lang], title=t["tool_title"], desc=t["tool_desc"] % n, og_title=t["tool_h1"],
                body=body, jsonld=ld(graph), alternates=alternates(TOOL_PATH), ct=ctv)


# ---------------------------------------------------------------- páginas de modelo

def model_page(lang, updated, ms, e):
    t = T[lang]
    path = model_path(e, lang)
    paths = {l: model_path(e, l) for l in LANGS}
    ctv = "model-" + e["slug"] + ("" if lang == "en" else "-" + lang)
    sz = lambda x: num(x, lang) + (" ГБ" if lang == "ru" else " GB")
    lname, llink = lic(e)
    card = "https://huggingface.co/" + e["base"]
    build = "https://huggingface.co/" + e["id"]
    facts = [
        (t["f_maker"], esc(e["maker"])),
        (t["f_params"], esc(e["params"][lang])),
        (t["f_size"], sz(e["size"])),
        (t["f_min"], sz(e["min"])),
        (t["f_reason"], t["yes"] if e["reasoning"] else t["no"]),
        (t["f_lic"], '<a href="%s" target="_blank" rel="noopener">%s</a>' % (llink, esc(lname))),
        (t["f_card"], '<a href="%s" target="_blank" rel="noopener">%s</a>' % (card, esc(e["base"]))),
        (t["f_build"], '<a href="%s" target="_blank" rel="noopener">%s</a>' % (build, esc(e["id"]))),
        (t["f_test"], test_cell(e, lang)),
        (t["t_plan"], plan_cell(e, lang)),
    ]
    ftable = ('<div class="table-scroll"><table>\n<tbody>\n%s\n</tbody>\n</table></div>\n'
              % "\n".join("<tr><th>%s</th><td>%s</td></tr>" % (k, v) for k, v in facts))
    strengths = e["strengths_en"] if lang == "en" else e["st"][lang]
    good = "<h2>%s</h2>\n<ul>\n%s\n</ul>\n<p>%s</p>\n" % (t["h_good"], "\n".join("<li>%s</li>" % esc(s) for s in strengths), t["good_src"])
    if e.get("test") is not None:
        good += "<p>%s %s</p>\n" % (esc(t["test_expl"]), esc(test_cell(e, lang)) + ("." if lang != "zh" else "。"))
    yes = [iphone_name(n, lang) for n, r in IPHONES if status(e["size"], r) == "yes"]
    edge = [iphone_name(n, lang) for n, r in IPHONES if status(e["size"], r) == "edge"]
    sep = "、" if lang == "zh" else ", "
    colon = "：" if lang == "zh" else ":"
    dev = "<h2>%s</h2>\n" % t["h_dev"]
    if yes:
        dev += "<p><strong>%s%s</strong> %s</p>\n" % (t["dev_iphone"], colon, esc(sep.join(yes)))
    if edge:
        dev += "<p><strong>%s%s</strong> %s</p>\n" % (t["dev_edge"], colon, esc(sep.join(edge)))
    if not yes and not edge:
        dev += "<p><strong>%s%s</strong> %s</p>\n" % (t["dev_iphone"], colon, t["dev_none"])
    dev += "<p><strong>%s%s</strong> %s</p>\n" % (t["dev_ipad"], colon, t["dev_ipad_txt"] % num(e["min"], lang))
    mac = t["dev_mac_all"] if e["min"] <= 8 else t["dev_mac_txt"] % num(e["min"], lang)
    dev += "<p><strong>%s%s</strong> %s</p>\n" % (t["dev_mac"], colon, mac)
    if edge:
        dev += '<p class="article-note">%s</p>\n' % t["edge_note"]
    dev += '<p><a href="%s">%s</a></p>\n' % (rel(path, TOOL_PATH[lang]), t["tool_link"])
    steps = [s % e["short"] if "%s" in s else s for s in (t["try_free"] if e["free"] else t["try_pro"])]
    tr = '<h2>%s</h2>\n<ol>\n%s\n</ol>\n<p><a href="%s">%s</a></p>\n' % (
        t["h_try"], "\n".join("<li>%s</li>" % esc(s) for s in steps), store(ctv), t["get"])
    other = "<h2>%s</h2>\n<ul>\n%s\n</ul>\n" % (t["h_other"], "\n".join(
        '<li><a href="%s">%s</a> &middot; %s</li>' % (rel(path, model_path(o, lang)), esc(o["short"]), sz(o["size"]))
        for o in ms if o is not e))
    if yes:
        dev_ans = t["dev_ans"] % (num(e["min"], lang), sep.join(yes)) + (t["edge_ans"] % sep.join(edge) if edge else "")
    elif edge:
        dev_ans = t["edge_only"] % (num(e["min"], lang), sep.join(edge))
    else:
        dev_ans = t["dev_ans_none"] % num(e["min"], lang)
    vals = {"m": e["short"], "dev": dev_ans, "plan": t["plan_free"] if e["free"] else t["plan_pro"], "size": num(e["size"], lang)}
    faq = [(q % vals, a % vals) for q, a in t["faq_model"]]
    h1 = t["m_h1"] % e["short"]
    stand = t["m_stand"] % (e["short"], e["maker"], num(e["size"], lang), num(e["min"], lang))
    desc = t["m_desc"] % (e["short"], e["maker"], num(e["size"], lang), num(e["min"], lang), lname)
    body = (header(lang, t["model_kicker"], h1, stand, path, paths)
            + '        <div class="article-body">\n'
            + "<p>%s</p>\n" % (t["disc_model"] % fdate(updated, lang))
            + ftable + good + dev + tr + other + faq_html(lang, faq)
            + sources_html(lang, [(e["base"] + " (Hugging Face)", card)])
            + "</div>")
    url = "%s/%s" % (SITE, path)
    graph = [{"@type": "TechArticle", "headline": h1, "description": desc, "inLanguage": HREFLANG[lang], "url": url,
              "mainEntityOfPage": url, "datePublished": DATE_ISO, "dateModified": DATE_ISO,
              "author": {"@type": "Person", "name": "Maruta G", "url": LINKEDIN},
              "publisher": {"@type": "Organization", "name": "Saga Labs", "url": SITE},
              "about": {"@type": "SoftwareSourceCode", "name": e["short"], "codeRepository": card,
                        "license": llink, "author": {"@type": "Organization", "name": e["maker"]}}},
             faq_ld(faq)]
    return dict(path=path, lang=HTML_LANG[lang], title=t["m_title"] % e["short"], desc=desc, og_title=h1,
                body=body, jsonld=ld(graph), alternates=alternates(paths), ct=ctv)


def pages():
    updated, ms = models()
    out = []
    for lang in LANGS:
        out.append(tool_page(lang, updated, ms))
        for e in ms:
            out.append(model_page(lang, updated, ms, e))
    return out


def _retag(html, ctv):
    parts = ct._LD.split(html)
    return "".join(c if i % 2 else ct._URL.sub(lambda m: ct._fix(m.group(0), ctv), c) for i, c in enumerate(parts))


def build(render):
    res = []
    for p in pages():
        ctv = p.pop("ct")
        path, _ = render(**p)
        full = os.path.join(ROOT, path)
        s = _retag(open(full, encoding="utf-8").read(), ctv)
        open(full, "w", encoding="utf-8").write(s)
        res.append((path, len(s)))
    return res


def all_paths():
    _, ms = models()
    return [TOOL_PATH[l] for l in LANGS] + [model_path(e, l) for l in LANGS for e in ms]


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    _, ms = models()
    for e in ms:
        print("%-14s %4.1f GB  min %4.1f GB  %s" % (e["short"], e["size"], e["min"], "free" if e["free"] else "Pro"))
