# -*- coding: utf-8 -*-
"""Лучшие открытые модели ИИ (2026), ruso. Mismos datos que models_en.py."""

HF = "https://huggingface.co/"
PINKU_PRIV = ("Чаты никогда не покидают устройство; в этикетке конфиденциальности Apple указаны только "
              "история покупок и анонимный идентификатор пользователя для покупки Pinku Pro.")

MODELS = dict(
    date="20 октября 2026 г.", date_iso="2026-10-20",
    h1="Лучшие открытые модели ИИ (2026)",
    desc=("Gemma 4, Qwen3.5, DeepSeek V4, Kimi K3, GLM-5.3, Mistral Small 4, gpt-oss, Llama 4 и LFM2.5: для "
          "чего лучше каждая модель с открытыми весами, размеры, лицензии, бенчмарки с источниками, нужное "
          "железо, тест маленьких моделей на 5 вопросах и как запустить их в Ollama, LM Studio, llama.cpp, Jan "
          "или на телефоне."),
    kicker="Руководство", section="Руководства",
    standfirst=("Модели, которые можно скачать и запустить у себя: от моделей на 1 ГБ для телефона до "
                "гигантов на триллионы параметров. Для чего каждая и что нужно, чтобы её запустить."),
    rank=[("Gemma 4", HF + "google/gemma-4-31B-it"), ("Qwen3.5", HF + "Qwen/Qwen3.5-9B"),
          ("DeepSeek V4", HF + "deepseek-ai/DeepSeek-V4-Pro"), ("Kimi K3", HF + "moonshotai/Kimi-K3"),
          ("GLM-5.3", HF + "zai-org/GLM-5.3"), ("Mistral Small 4", HF + "mistralai/Mistral-Small-4-119B-2603"),
          ("gpt-oss", HF + "openai/gpt-oss-120b"), ("Llama 4", HF + "meta-llama/Llama-4-Scout-17B-16E-Instruct"),
          ("LFM2.5", HF + "LiquidAI/LFM2.5-1.2B-Instruct")],
    body="""
<p>«Открытые веса» означают, что файлы обученной модели опубликованы и их можно
запустить на своём железе. Это не всегда открытый код: некоторые лицензии добавляют
условия, поэтому мы указываем каждую. Размеры, лицензии и длина контекста взяты со
страниц моделей на Hugging Face; результаты бенчмарков приводит сам разработчик.
Проверено %(date)s.</p>

<h2>Коротко</h2>

<div class="table-scroll"><table>
<thead><tr><th>Модель</th><th>Разработчик</th><th>Размеры</th><th>Лицензия</th><th>Для чего лучше</th></tr></thead>
<tbody>
<tr><td><a href=\"""" + HF + """google/gemma-4-31B-it"%(x)s>Gemma 4</a></td><td>Google DeepMind</td><td>E2B, E4B, 12B, 26B A4B (MoE), 31B</td><td>Apache 2.0</td><td>Телефоны и ноутбуки; картинки и звук; 140+ языков</td></tr>
<tr><td><a href=\"""" + HF + """Qwen/Qwen3.5-9B"%(x)s>Qwen3.5</a></td><td>Alibaba (Qwen)</td><td>от 0,8B до 397B A17B (MoE)</td><td>Apache 2.0</td><td>Самый широкий выбор размеров; сильные малые модели</td></tr>
<tr><td><a href=\"""" + HF + """deepseek-ai/DeepSeek-V4-Pro"%(x)s>DeepSeek V4</a></td><td>DeepSeek</td><td>Flash 284B (13B активных), Pro 1,6T (49B активных)</td><td>MIT</td><td>Лучшие открытые рассуждения и код; контекст 1 млн токенов</td></tr>
<tr><td><a href=\"""" + HF + """moonshotai/Kimi-K3"%(x)s>Kimi K3</a></td><td>Moonshot AI</td><td>2,8T (104B активных)</td><td>Kimi K3 License</td><td>Долгие агентные сессии программирования</td></tr>
<tr><td><a href=\"""" + HF + """zai-org/GLM-5.3"%(x)s>GLM-5.3</a></td><td>Z.ai</td><td>GLM-5.3, GLM-5.3-Flash</td><td>Своя (5.3); MIT (5.3-Flash)</td><td>Английский и китайский; агенты</td></tr>
<tr><td><a href=\"""" + HF + """mistralai/Mistral-Small-4-119B-2603"%(x)s>Mistral Small 4</a></td><td>Mistral AI</td><td>119B; Devstral Small 2 24B для кода</td><td>Apache 2.0</td><td>24 языка, включая русский; свободная лицензия</td></tr>
<tr><td><a href=\"""" + HF + """openai/gpt-oss-120b"%(x)s>gpt-oss</a></td><td>OpenAI</td><td>20B, 120B</td><td>Apache 2.0</td><td>Модель 20B, которая помещается в 16 ГБ</td></tr>
<tr><td><a href=\"""" + HF + """meta-llama/Llama-4-Scout-17B-16E-Instruct"%(x)s>Llama 4</a></td><td>Meta</td><td>Scout 109B (17B активных), Maverick</td><td>Llama 4 Community License, доступ по запросу</td><td>Готовые проекты на Llama; веса не обновлялись с мая 2025</td></tr>
<tr><td><a href=\"""" + HF + """LiquidAI/LFM2.5-1.2B-Instruct"%(x)s>LFM2.5</a></td><td>Liquid AI</td><td>230M, 1,2B, 2,6B, 8B A1B</td><td>LFM Open License v1.0</td><td>Быстрые модели с малым расходом памяти для телефонов</td></tr>
</tbody>
</table></div>

<p class="article-note">У моделей MoE (смесь экспертов) указаны все и активные
параметры. В памяти должны быть все, но на каждом токене работают только активные,
поэтому они быстрее, чем можно подумать по общему размеру.</p>

<h2>Бенчмарки по данным разработчиков</h2>

<p>Два распространённых теста: MMLU-Pro (широкие знания) и GPQA Diamond (сложные
научные вопросы). Разработчики запускают их со своими настройками, так что небольшие
различия не значат много.</p>

<div class="table-scroll"><table>
<thead><tr><th>Модель</th><th>MMLU-Pro (%%)</th><th>GPQA Diamond (%%)</th><th>Источник</th></tr></thead>
<tbody>
<tr><td>DeepSeek V4 Pro (макс. рассуждения)</td><td>87,5</td><td>90,1</td><td>карточка DeepSeek</td></tr>
<tr><td>Gemma 4 31B</td><td>85,2</td><td>84,3</td><td>карточка Google</td></tr>
<tr><td>Gemma 4 26B A4B</td><td>82,6</td><td>82,3</td><td>карточка Google</td></tr>
<tr><td>Qwen3.5 9B</td><td>82,5</td><td>81,7</td><td>карточка Qwen</td></tr>
<tr><td>gpt-oss 120B</td><td>80,8</td><td>80,1</td><td>карточка Qwen3.5-9B</td></tr>
<tr><td>Qwen3.5 4B</td><td>79,1</td><td>76,2</td><td>карточка Qwen</td></tr>
<tr><td>gpt-oss 20B</td><td>74,8</td><td>71,5</td><td>карточка Qwen3.5-9B</td></tr>
<tr><td>Gemma 4 E4B</td><td>69,4</td><td>58,6</td><td>карточка Google</td></tr>
<tr><td>Gemma 4 E2B</td><td>60,0</td><td>43,4</td><td>карточка Google</td></tr>
</tbody>
</table></div>

<h2>По моделям</h2>

<h3>Gemma 4 (Google DeepMind)</h3>
<p>Пять размеров: E2B (2,3B эффективных, 5,1B с эмбеддингами), E4B, 12B, MoE на 26B с
3,8B активных и 31B. Все понимают картинки, E2B, E4B и 12B ещё и звук. Контекст 128K
у малых и 256K у остальных; предобучение на 140+ языках. Apache 2.0. 26B A4B даёт
почти уровень 31B при скорости около 4B: хороший выбор для ноутбука.</p>

<h3>Qwen3.5 (Alibaba)</h3>
<p>Самая широкая линейка: 0,8B, 2B, 4B, 9B, 27B, 35B A3B, 122B A10B и 397B A17B, все
под Apache 2.0 и все понимают картинки. Контекст 262K токенов (9B), 201 язык и диалект
по данным Qwen. 4B и 9B на бумаге самые сильные малые модели; в нашем тесте на пять
вопросов самые маленькие версии ошибались в простых фактах.</p>

<h3>DeepSeek V4 (DeepSeek)</h3>
<p>V4-Flash (284B, 13B активных) и V4-Pro (1,6T, 49B активных), контекст миллион
токенов, лицензия MIT. По данным DeepSeek, Pro в режиме максимальных рассуждений
набирает 93,5 в LiveCodeBench и рейтинг 3206 на Codeforces. 16 октября 2026 года
вышла V4.1-Flash. Нужен серверный уровень железа. Маленькие «R1 Distill» это другие
модели, и в нашем тесте они показали себя плохо.</p>

<h3>Kimi K3 (Moonshot AI)</h3>
<p>2,8 триллиона параметров, 104B активных, текст и картинки, контекст миллион
токенов, собственная лицензия Kimi K3. Для долгих сессий программирования. Только
серверы.</p>

<h3>GLM-5.3 (Z.ai)</h3>
<p>GLM-5.3 (своя лицензия) и GLM-5.3-Flash (MIT, понимает картинки), английский и
китайский, обновлены 14 и 15 октября 2026 года. Большие модели для серверов и
агентов.</p>

<h3>Mistral Small 4 и Devstral (Mistral AI)</h3>
<p>Mistral Small 4: 119B, Apache 2.0, в карточке 24 языка, включая русский. Devstral
Small 2 (24B, Apache 2.0) для программирования помещается на мощный компьютер в
4 битах.</p>

<h3>gpt-oss (OpenAI)</h3>
<p>Две модели августа 2025 года, 20B и 120B, Apache 2.0. 20B по-прежнему частый выбор
для машины с 16 ГБ.</p>

<h3>Llama 4 (Meta)</h3>
<p>Scout (109B, 17B активных) и Maverick, лицензия Llama 4 Community License, доступ по
запросу на Hugging Face. Веса там последний раз обновлялись в мае 2025 года. Маленькие
Llama 3.2 (1B, 3B) всё ещё часто встречаются в мобильных приложениях.</p>

<h3>LFM2.5 (Liquid AI)</h3>
<p>Малые модели для устройств: 230M, 1,2B, 2,6B и 8B с 1B активных. По данным Liquid
AI, 1,2B работает меньше чем в 1 ГБ памяти, контекст 32 768 токенов, восемь языков
(русского среди них нет). Liquid рекомендует её для агентов, извлечения данных и
поиска по документам, но не для задач на знания и программирование. Лицензия своя
(LFM Open License v1.0).</p>

<h2>Какое нужно железо</h2>

<p>Грубое правило: модель в 4 битах занимает примерно 0,5–0,6 ГБ памяти на миллиард
параметров плюс место для разговора. Для MoE считайте все параметры, а не только
активные.</p>

<div class="table-scroll"><table>
<thead><tr><th>Устройство</th><th>Реальные модели (4 бита)</th></tr></thead>
<tbody>
<tr><td>iPhone или Android</td><td>До ~4B: Gemma 4 E2B (~3,6 ГБ в MLX 4 бита), Qwen3.5 2B или 4B, LFM2.5 1,2B (~0,7 ГБ), Llama 3.2 1B или 3B</td></tr>
<tr><td>Ноутбук с 16 ГБ</td><td>До ~14B: Qwen3.5 9B, Gemma 4 12B, gpt-oss 20B (впритык)</td></tr>
<tr><td>Mac или ПК с 32–64 ГБ</td><td>Gemma 4 26B A4B или 31B, Qwen3.5 27B или 35B A3B, Devstral Small 2 24B</td></tr>
<tr><td>Рабочая станция от 128 ГБ</td><td>Mistral Small 4 119B, gpt-oss 120B, Qwen3.5 122B A10B</td></tr>
<tr><td>Дата-центр</td><td>DeepSeek V4, Kimi K3, GLM-5.3, Qwen3.5 397B, Llama 4 Maverick</td></tr>
</tbody>
</table></div>

<h2>Небольшой тест: пять вопросов на Mac</h2>

<p>Разработчики Pinku прогнали маленькие модели через одни и те же пять вопросов на
факты (столица Франции, дней в високосном году, автор «Дон Кихота», химический символ
золота, самая большая планета), три на испанском и два на английском, в сборках MLX
4 бита на Mac. Вопрос засчитывался, если модель отвечала верно и не уходила в
рассуждения сверх лимита. Это пять вопросов, а не бенчмарк: тест показывает только,
знает ли модель размером с телефон базовые факты.</p>

<div class="table-scroll"><table>
<thead><tr><th>Модель</th><th>Верно</th></tr></thead>
<tbody>
<tr><td>Gemma 4 E2B</td><td>5 из 5</td></tr>
<tr><td>LFM2.5 1,2B</td><td>5 из 5</td></tr>
<tr><td>Qwen3.5 2B</td><td>4 из 5</td></tr>
<tr><td>Qwen3.5 4B</td><td>4 из 5</td></tr>
<tr><td>DeepSeek R1 Distill 7B</td><td>4 из 5</td></tr>
<tr><td>Qwen3.5 0,8B</td><td>2 из 5</td></tr>
<tr><td>DeepSeek R1 Distill 1,5B</td><td>0 из 5</td></tr>
</tbody>
</table></div>

<h2>Как ими пользоваться</h2>

<h3>На компьютере</h3>
<ul>
<li><a href="https://ollama.com/"%(x)s>Ollama</a>: бесплатно, открытый код (MIT), macOS 14+,
Windows и Linux; командная строка и с июля 2025 года приложение для чата. В библиотеке
есть Gemma 4, Qwen3.5, gpt-oss, Llama 4 и LFM2.5 для запуска у себя; гиганты (DeepSeek V4,
Kimi K3, GLM-5.3) работают в облаке Ollama за кредиты.</li>
<li><a href="https://lmstudio.ai/"%(x)s>LM Studio</a>: бесплатное приложение (код закрыт) с
каталогом моделей, работает через llama.cpp и Apple MLX; на Mac нужен Apple silicon и
macOS 14, рекомендуется 16 ГБ памяти.</li>
<li><a href="https://github.com/ggml-org/llama.cpp"%(x)s>llama.cpp</a>: открытый движок (MIT),
на котором построены многие из этих приложений; для тех, кому удобен терминал.</li>
<li><a href="https://jan.ai/"%(x)s>Jan</a>: открытое приложение для чата, версия 0.8.6,
macOS 13.6+; для локальных моделей на Mac нужен Apple silicon.</li>
<li><a href="https://github.com/ml-explore/mlx-lm"%(x)s>mlx-lm</a>: библиотека Apple (MIT) для
разработчиков на Apple silicon.</li>
</ul>

<h3>На телефоне</h3>
<ul>
<li><a href="%(pinku)s">Pinku</a> (iPhone 12+ с iOS 18.6 и Mac на Apple silicon): подборка
малых моделей (Gemma, Llama 3.2, Qwen3, SmolLM3, LFM и другие), показывает только те, на
которые хватает памяти; без аккаунта; интерфейс на русском; модель по умолчанию
бесплатна, большие входят в Pinku Pro. """ + PINKU_PRIV + """</li>
<li><a href="https://github.com/a-ghorbani/pocketpal-ai"%(x)s>PocketPal AI</a>: бесплатно и
с открытым кодом, iPhone и Android; любые GGUF-модели с Hugging Face.</li>
<li><a href="https://apps.apple.com/ru/app/id6448106860"%(x)s>Private LLM</a>: 299 ₽ один
раз, iPhone, iPad и Mac.</li>
<li><a href="https://apps.apple.com/ru/app/id6476614556"%(x)s>Enclave</a>: бесплатно, iOS 27.</li>
</ul>
<p class="article-note">Locally AI в российском App Store на %(date)s нет.</p>

<p>Подробнее (на английском, оба сайта ведёт Saga Labs): приложения для телефона по
моделям, которые они загружают, на <a href="https://reviewland.io/best-apps-run-open-source-ai-models-iphone/"%(x)s>Reviewland</a>
и программы для компьютера как <a href="https://reditor.cloud/ollama-alternatives-mac-iphone/"%(x)s>альтернативы Ollama на Reditor</a>.</p>

<p>По теме: <a href="%(p_noai)s">ИИ-приложения для iPhone без Apple Intelligence</a> и
<a href="%(p_offline)s">работает ли Apple Intelligence без интернета</a>.</p>
""",
    faq=[
        ("Какая открытая модель ИИ лучшая в 2026 году?",
         "Зависит от железа. Для серверов по данным собственной карточки выше всех здесь DeepSeek V4 Pro. "
         "Для ноутбука: Gemma 4 26B A4B или Qwen3.5 9B. Для телефона: Gemma 4 E2B, Qwen3.5 2B–4B или LFM2.5 1,2B."),
        ("Чем открытые веса отличаются от открытого кода?",
         "Открытые веса значат, что файлы модели опубликованы и их можно запустить. Лицензия может добавлять "
         "условия: у Gemma 4, Qwen3.5, Mistral Small 4 и gpt-oss Apache 2.0, у DeepSeek V4 MIT, а у Llama 4, "
         "Kimi K3, GLM-5.3 и LFM2.5 свои лицензии."),
        ("Сколько памяти нужно, чтобы запустить локальную модель?",
         "Примерно 0,5–0,6 ГБ на миллиард параметров в 4 битах плюс место для разговора. Модель 4B помещается "
         "в современный телефон, около 14B в ноутбук с 16 ГБ, а модели на триллион параметров требуют серверов."),
        ("Какая открытая модель лучше всего работает на iPhone?",
         "Модели примерно до 4B. В тесте Pinku на пять вопросов Gemma 4 E2B и LFM2.5 1,2B ответили верно на "
         "все пять, Qwen3.5 2B и 4B на четыре, DeepSeek R1 Distill 1,5B ни на один."),
        ("Какие модели лучше понимают русский?",
         "В карточках русский явно указан у Mistral Small 4; Gemma 4 предобучена на 140+ языках, Qwen3.5 "
         "заявляет 201 язык. У LFM2.5 русского нет в списке языков."),
    ],
    sources="""
<h2>Источники</h2>
<ul>
<li>Страницы и карточки моделей на Hugging Face (параметры, лицензия, контекст, бенчмарки): <a href=\"""" + HF + """google/gemma-4-31B-it"%(x)s>Gemma 4</a>, <a href=\"""" + HF + """Qwen/Qwen3.5-9B"%(x)s>Qwen3.5-9B</a> (там же данные gpt-oss), <a href=\"""" + HF + """deepseek-ai/DeepSeek-V4-Pro"%(x)s>DeepSeek V4</a>, <a href=\"""" + HF + """moonshotai/Kimi-K3"%(x)s>Kimi K3</a>, <a href=\"""" + HF + """zai-org/GLM-5.3"%(x)s>GLM-5.3</a>, <a href=\"""" + HF + """mistralai/Mistral-Small-4-119B-2603"%(x)s>Mistral Small 4</a>, <a href=\"""" + HF + """openai/gpt-oss-120b"%(x)s>gpt-oss</a>, <a href=\"""" + HF + """meta-llama/Llama-4-Scout-17B-16E-Instruct"%(x)s>Llama 4 Scout</a>, <a href=\"""" + HF + """LiquidAI/LFM2.5-1.2B-Instruct"%(x)s>LFM2.5</a>; проверено %(date)s.</li>
<li>Ollama: <a href="https://ollama.com/blog/new-app"%(x)s>приложение</a>, <a href="https://docs.ollama.com/macos"%(x)s>требования macOS</a>, <a href="https://ollama.com/pricing"%(x)s>цены</a>. LM Studio: <a href="https://lmstudio.ai/docs/app/system-requirements"%(x)s>требования</a>. Jan: <a href="https://www.jan.ai/docs/desktop/install/mac"%(x)s>установка на Mac</a>.</li>
<li>GitHub: <a href="https://github.com/ggml-org/llama.cpp"%(x)s>llama.cpp</a>, <a href="https://github.com/ml-explore/mlx-lm"%(x)s>mlx-lm</a>, <a href="https://github.com/a-ghorbani/pocketpal-ai"%(x)s>PocketPal AI</a>.</li>
<li>Тест на пять вопросов: самопроверка Pinku (5 вопросов на факты, MLX 4 бита, Mac), октябрь 2026 г.</li>
</ul>
<p>Если что-то устарело, <a href="mailto:sagalabs@proton.me">напишите нам</a>.</p>
<p>Прозрачность: Saga Labs, издатель этого сайта, также делает Pinku. Результаты теста Pinku
приведены как есть, включая модели, которых в Pinku нет.</p>
""",
)
