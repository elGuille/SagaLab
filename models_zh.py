# -*- coding: utf-8 -*-
"""最好的开放权重 AI 模型（2026）, chino simplificado. Mismos datos que models_en.py."""

HF = "https://huggingface.co/"
MS = "https://modelscope.cn/models/"
PINKU_PRIV = "聊天内容不会离开你的设备；Apple 隐私标签只列出购买记录和一个用于 Pinku Pro 购买的匿名用户 ID。"

MODELS = dict(
    date="2026年10月20日", date_iso="2026-10-20",
    h1="最好的开放权重 AI 模型（2026）",
    desc=("Gemma 4、Qwen3.5、DeepSeek V4、Kimi K3、GLM-5.3、Mistral Small 4、gpt-oss、Llama 4 和 LFM2.5："
          "每个开放权重模型擅长什么、尺寸、许可证、有出处的基准成绩、所需硬件、小模型的 5 题测试，以及如何用 "
          "Ollama、LM Studio、llama.cpp、Jan 或在手机上运行。"),
    kicker="指南", section="指南",
    standfirst="可以下载并在自己设备上运行的模型，从 1 GB 的手机模型到万亿参数的大模型。每个适合做什么，运行需要什么。",
    rank=[("Gemma 4", HF + "google/gemma-4-31B-it"), ("Qwen3.5", HF + "Qwen/Qwen3.5-9B"),
          ("DeepSeek V4", HF + "deepseek-ai/DeepSeek-V4-Pro"), ("Kimi K3", HF + "moonshotai/Kimi-K3"),
          ("GLM-5.3", HF + "zai-org/GLM-5.3"), ("Mistral Small 4", HF + "mistralai/Mistral-Small-4-119B-2603"),
          ("gpt-oss", HF + "openai/gpt-oss-120b"), ("Llama 4", HF + "meta-llama/Llama-4-Scout-17B-16E-Instruct"),
          ("LFM2.5", HF + "LiquidAI/LFM2.5-1.2B-Instruct")],
    body="""
<p>“开放权重”指训练好的模型文件已经公开，可以在自己的硬件上运行。这不一定等于开源：有些许可证附带条件，
所以我们逐一列出。尺寸、许可证和上下文长度来自各模型的 Hugging Face 页面；基准成绩是各厂商自己公布的，
核对于 %(date)s。在中国大陆访问 Hugging Face 不便时，DeepSeek 等模型也发布在
<a href="https://modelscope.cn/"%(x)s>ModelScope（魔搭）</a>上。</p>

<h2>一览</h2>

<div class="table-scroll"><table>
<thead><tr><th>模型</th><th>厂商</th><th>尺寸</th><th>许可证</th><th>最适合</th></tr></thead>
<tbody>
<tr><td><a href=\"""" + HF + """google/gemma-4-31B-it"%(x)s>Gemma 4</a></td><td>Google DeepMind</td><td>E2B、E4B、12B、26B A4B（MoE）、31B</td><td>Apache 2.0</td><td>手机和笔记本；图像和音频；140 多种语言</td></tr>
<tr><td><a href=\"""" + HF + """Qwen/Qwen3.5-9B"%(x)s>Qwen3.5（通义千问）</a></td><td>阿里巴巴</td><td>0.8B 到 397B A17B（MoE）</td><td>Apache 2.0</td><td>尺寸选择最多；小模型很强；中文</td></tr>
<tr><td><a href=\"""" + HF + """deepseek-ai/DeepSeek-V4-Pro"%(x)s>DeepSeek V4</a></td><td>深度求索</td><td>Flash 284B（激活 13B）、Pro 1.6T（激活 49B）</td><td>MIT</td><td>开放模型中最强的推理和代码；100 万 token 上下文</td></tr>
<tr><td><a href=\"""" + HF + """moonshotai/Kimi-K3"%(x)s>Kimi K3</a></td><td>月之暗面</td><td>2.8T（激活 104B）</td><td>Kimi K3 许可证</td><td>长时间的智能体编程</td></tr>
<tr><td><a href=\"""" + HF + """zai-org/GLM-5.3"%(x)s>GLM-5.3</a></td><td>智谱 Z.ai</td><td>GLM-5.3、GLM-5.3-Flash</td><td>自有许可（5.3）；MIT（5.3-Flash）</td><td>中英文；智能体</td></tr>
<tr><td><a href=\"""" + HF + """mistralai/Mistral-Small-4-119B-2603"%(x)s>Mistral Small 4</a></td><td>Mistral AI</td><td>119B；代码用 Devstral Small 2 24B</td><td>Apache 2.0</td><td>24 种语言；宽松许可证</td></tr>
<tr><td><a href=\"""" + HF + """openai/gpt-oss-120b"%(x)s>gpt-oss</a></td><td>OpenAI</td><td>20B、120B</td><td>Apache 2.0</td><td>16 GB 内存能装下的 20B 模型</td></tr>
<tr><td><a href=\"""" + HF + """meta-llama/Llama-4-Scout-17B-16E-Instruct"%(x)s>Llama 4</a></td><td>Meta</td><td>Scout 109B（激活 17B）、Maverick</td><td>Llama 4 Community License，需申请</td><td>已有的 Llama 项目；2025 年 5 月后未更新</td></tr>
<tr><td><a href=\"""" + HF + """LiquidAI/LFM2.5-1.2B-Instruct"%(x)s>LFM2.5</a></td><td>Liquid AI</td><td>230M、1.2B、2.6B、8B A1B</td><td>LFM Open License v1.0</td><td>手机和边缘设备上快速、省内存</td></tr>
</tbody>
</table></div>

<p class="article-note">MoE（混合专家）模型列出总参数和激活参数。所有参数都要放进内存，但每个 token
只用激活的那部分，所以速度比总尺寸看起来快。</p>

<h2>厂商公布的基准成绩</h2>

<p>两个常见测试：MMLU-Pro（广泛知识）和 GPQA Diamond（高难度科学问题）。各厂商用自己的设置运行，
小差距不必太在意。</p>

<div class="table-scroll"><table>
<thead><tr><th>模型</th><th>MMLU-Pro（%%）</th><th>GPQA Diamond（%%）</th><th>来源</th></tr></thead>
<tbody>
<tr><td>DeepSeek V4 Pro（最大推理）</td><td>87.5</td><td>90.1</td><td>DeepSeek 模型卡</td></tr>
<tr><td>Gemma 4 31B</td><td>85.2</td><td>84.3</td><td>Google 模型卡</td></tr>
<tr><td>Gemma 4 26B A4B</td><td>82.6</td><td>82.3</td><td>Google 模型卡</td></tr>
<tr><td>Qwen3.5 9B</td><td>82.5</td><td>81.7</td><td>Qwen 模型卡</td></tr>
<tr><td>gpt-oss 120B</td><td>80.8</td><td>80.1</td><td>Qwen3.5-9B 模型卡</td></tr>
<tr><td>Qwen3.5 4B</td><td>79.1</td><td>76.2</td><td>Qwen 模型卡</td></tr>
<tr><td>gpt-oss 20B</td><td>74.8</td><td>71.5</td><td>Qwen3.5-9B 模型卡</td></tr>
<tr><td>Gemma 4 E4B</td><td>69.4</td><td>58.6</td><td>Google 模型卡</td></tr>
<tr><td>Gemma 4 E2B</td><td>60.0</td><td>43.4</td><td>Google 模型卡</td></tr>
</tbody>
</table></div>

<h2>逐个模型</h2>

<h3>Gemma 4（Google DeepMind）</h3>
<p>五个尺寸：E2B（有效 2.3B，含嵌入 5.1B）、E4B、12B、激活 3.8B 的 26B MoE 和 31B。全部支持图像，
E2B、E4B 和 12B 还支持音频。小模型上下文 128K，其余 256K；预训练覆盖 140 多种语言。Apache 2.0。
26B A4B 接近 31B 的成绩、速度接近 4B，适合笔记本。</p>

<h3>Qwen3.5（阿里巴巴通义千问）</h3>
<p>阵容最全：0.8B、2B、4B、9B、27B、35B A3B、122B A10B 和 397B A17B，全部 Apache 2.0、全部支持图像。
9B 原生上下文 262K token；Qwen 称支持 201 种语言和方言。纸面上 4B 和 9B 是最强的小模型；在我们的五题测试里，
最小的版本在简单事实上出错较多。</p>

<h3>DeepSeek V4（深度求索）</h3>
<p>V4-Flash（284B，激活 13B）和 V4-Pro（1.6T，激活 49B），100 万 token 上下文，MIT 许可。据 DeepSeek
公布，Pro 在最大推理模式下 LiveCodeBench 93.5、Codeforces 评分 3206。2026 年 10 月 16 日又发布了
V4.1-Flash。需要数据中心级硬件，多数人通过 API 使用。小型的“R1 Distill”是另一回事，在我们的测试里表现不好。</p>

<h3>Kimi K3（月之暗面）</h3>
<p>2.8 万亿参数，激活 104B，支持文本和图像，100 万 token 上下文，采用自有的 Kimi K3 许可证。
面向长时间的编程和知识工作。只适合服务器。</p>

<h3>GLM-5.3（智谱）</h3>
<p>GLM-5.3（自有许可证）和 GLM-5.3-Flash（MIT，支持图像），中英文，分别于 2026 年 10 月 14 日和 15 日更新。
面向服务器和智能体的大模型。</p>

<h3>Mistral Small 4 与 Devstral（Mistral AI）</h3>
<p>Mistral Small 4：119B，Apache 2.0，模型卡列出 24 种语言（含中文）。Devstral Small 2（24B，Apache 2.0）
是编程模型，4 位量化后可在高配台式机上运行。</p>

<h3>gpt-oss（OpenAI）</h3>
<p>2025 年 8 月发布的 20B 和 120B 两个模型，Apache 2.0。20B 仍是 16 GB 机器的常见选择。</p>

<h3>Llama 4（Meta）</h3>
<p>Scout（109B，激活 17B）和 Maverick，Llama 4 Community License，在 Hugging Face 上需申请访问；
权重最后更新于 2025 年 5 月。小型的 Llama 3.2（1B、3B）仍常见于手机 App。</p>

<h3>LFM2.5（Liquid AI）</h3>
<p>为设备设计的小模型：230M、1.2B、2.6B 和激活 1B 的 8B。据 Liquid AI，1.2B 占用内存不到 1 GB，
上下文 32,768 token，支持八种语言（含中文）。Liquid 自己推荐用于智能体、数据提取和检索，不推荐用于
知识密集型任务和编程。许可证为其自有的 LFM Open License v1.0。</p>

<h2>需要什么硬件</h2>

<p>粗略规则：4 位量化的模型每十亿参数约需 0.5 到 0.6 GB 内存，另加对话占用。MoE 模型按总参数算，
而不是激活参数。</p>

<div class="table-scroll"><table>
<thead><tr><th>设备</th><th>现实可用的模型（4 位）</th></tr></thead>
<tbody>
<tr><td>iPhone 或安卓手机</td><td>约 4B 以内：Gemma 4 E2B（MLX 4 位约 3.6 GB）、Qwen3.5 2B 或 4B、LFM2.5 1.2B（约 0.7 GB）、Llama 3.2 1B 或 3B</td></tr>
<tr><td>16 GB 笔记本</td><td>约 14B 以内：Qwen3.5 9B、Gemma 4 12B、gpt-oss 20B（勉强）</td></tr>
<tr><td>32 到 64 GB 的 Mac 或 PC</td><td>Gemma 4 26B A4B 或 31B、Qwen3.5 27B 或 35B A3B、Devstral Small 2 24B</td></tr>
<tr><td>128 GB 以上工作站</td><td>Mistral Small 4 119B、gpt-oss 120B、Qwen3.5 122B A10B</td></tr>
<tr><td>数据中心</td><td>DeepSeek V4、Kimi K3、GLM-5.3、Qwen3.5 397B、Llama 4 Maverick</td></tr>
</tbody>
</table></div>

<h2>一个小测试：在 Mac 上问五个问题</h2>

<p>Pinku 的开发者用同样五个事实问题（法国首都、闰年天数、《堂吉诃德》作者、金的化学符号、最大的行星；
三题西班牙语、两题英语）测试了几个小模型，使用 Mac 上的 MLX 4 位版本。答对且没有超出长度上限地兜圈子才算通过。
只有五个问题，不是基准测试：它只说明手机大小的模型能否答对基本事实。</p>

<div class="table-scroll"><table>
<thead><tr><th>模型</th><th>答对</th></tr></thead>
<tbody>
<tr><td>Gemma 4 E2B</td><td>5/5</td></tr>
<tr><td>LFM2.5 1.2B</td><td>5/5</td></tr>
<tr><td>Qwen3.5 2B</td><td>4/5</td></tr>
<tr><td>Qwen3.5 4B</td><td>4/5</td></tr>
<tr><td>DeepSeek R1 Distill 7B</td><td>4/5</td></tr>
<tr><td>Qwen3.5 0.8B</td><td>2/5</td></tr>
<tr><td>DeepSeek R1 Distill 1.5B</td><td>0/5</td></tr>
</tbody>
</table></div>

<h2>如何使用</h2>

<h3>在电脑上</h3>
<ul>
<li><a href="https://ollama.com/"%(x)s>Ollama</a>：免费开源（MIT），macOS 14 及以上、Windows 和 Linux；
命令行，2025 年 7 月起还有桌面聊天 App。模型库里有 Gemma 4、Qwen3.5、gpt-oss、Llama 4 和 LFM2.5 可在本机运行；
超大模型（DeepSeek V4、Kimi K3、GLM-5.3）在 Ollama 云端运行，按用量付费。</li>
<li><a href="https://lmstudio.ai/"%(x)s>LM Studio</a>：免费桌面 App（不开源），自带模型浏览器，基于 llama.cpp 和 Apple MLX；
Mac 需 Apple 芯片和 macOS 14，建议 16 GB 内存。</li>
<li><a href="https://github.com/ggml-org/llama.cpp"%(x)s>llama.cpp</a>：开源（MIT）推理引擎，很多 App 都基于它，适合习惯终端的人。</li>
<li><a href="https://jan.ai/"%(x)s>Jan</a>：开源聊天 App，0.8.6 版，macOS 13.6 及以上；Mac 上本地模型需要 Apple 芯片。</li>
<li><a href="https://github.com/ml-explore/mlx-lm"%(x)s>mlx-lm</a>：Apple 的 MIT 开源库，面向 Apple 芯片开发者。</li>
</ul>

<h3>在手机上</h3>
<ul>
<li><a href="%(pinku)s">Pinku</a>（iOS 18.6 的 iPhone 12 及以上，以及 Apple 芯片的 Mac）：精选的小模型（Gemma、Llama 3.2、
Qwen3、SmolLM3、LFM 等），只显示设备内存装得下的；无需账户；有简体中文界面；默认模型免费，更大的模型在 Pinku Pro 中。
""" + PINKU_PRIV + """ 在 Hugging Face 无法访问时，它会从 ModelScope 下载模型。</li>
<li><a href="https://github.com/a-ghorbani/pocketpal-ai"%(x)s>PocketPal AI</a>：免费开源，iPhone 和安卓；可加载 Hugging Face 上任意 GGUF 模型。</li>
<li><a href="https://apps.apple.com/cn/app/id6448106860"%(x)s>Private LLM</a>：一次性 ¥38，iPhone、iPad 和 Mac。</li>
</ul>
<p class="article-note">截至 %(date)s，Locally AI 和 Enclave 未在中国大陆 App Store 上架。</p>

<p>相关文章：<a href="%(p_noai)s">没有 Apple Intelligence 的 iPhone 适合用哪些 AI App</a>、
<a href="%(p_offline)s">Apple Intelligence 能离线使用吗</a>。</p>
""",
    faq=[
        ("2026 年最好的开放权重 AI 模型是哪个？",
         "取决于硬件。服务器上，按各自模型卡的数据，DeepSeek V4 Pro 在本文模型中成绩最高。笔记本上选 Gemma 4 26B A4B 或 Qwen3.5 9B。"
         "手机上选 Gemma 4 E2B、Qwen3.5 2B 到 4B 或 LFM2.5 1.2B。"),
        ("开放权重和开源有什么区别？",
         "开放权重指模型文件公开、可以运行。许可证可能附带条件：Gemma 4、Qwen3.5、Mistral Small 4 和 gpt-oss 用 Apache 2.0，"
         "DeepSeek V4 用 MIT，Llama 4、Kimi K3、GLM-5.3 和 LFM2.5 用各自的许可证。"),
        ("本地运行 AI 模型需要多少内存？",
         "4 位量化下每十亿参数约 0.5 到 0.6 GB，另加对话占用。4B 模型能装进较新的手机，约 14B 能装进 16 GB 笔记本，万亿参数模型需要服务器。"),
        ("在 iPhone 上哪个开放模型最好用？",
         "约 4B 以内的模型。在 Pinku 的五题测试中，Gemma 4 E2B 和 LFM2.5 1.2B 全部答对，Qwen3.5 2B 和 4B 答对四题，DeepSeek R1 Distill 1.5B 一题都没答对。"),
        ("在中国大陆怎么下载这些模型？",
         "DeepSeek 等模型同时发布在 ModelScope（魔搭）上（见其模型卡的下载表）；Pinku 在 Hugging Face 无法访问时也会从 ModelScope 下载。"),
    ],
    sources="""
<h2>来源</h2>
<ul>
<li>Hugging Face 模型页面和模型卡（参数、许可证、上下文、基准）：<a href=\"""" + HF + """google/gemma-4-31B-it"%(x)s>Gemma 4</a>、<a href=\"""" + HF + """Qwen/Qwen3.5-9B"%(x)s>Qwen3.5-9B</a>（含 gpt-oss 数据）、<a href=\"""" + HF + """deepseek-ai/DeepSeek-V4-Pro"%(x)s>DeepSeek V4</a>、<a href=\"""" + HF + """moonshotai/Kimi-K3"%(x)s>Kimi K3</a>、<a href=\"""" + HF + """zai-org/GLM-5.3"%(x)s>GLM-5.3</a>、<a href=\"""" + HF + """mistralai/Mistral-Small-4-119B-2603"%(x)s>Mistral Small 4</a>、<a href=\"""" + HF + """openai/gpt-oss-120b"%(x)s>gpt-oss</a>、<a href=\"""" + HF + """meta-llama/Llama-4-Scout-17B-16E-Instruct"%(x)s>Llama 4 Scout</a>、<a href=\"""" + HF + """LiquidAI/LFM2.5-1.2B-Instruct"%(x)s>LFM2.5</a>，核对于 %(date)s。</li>
<li>Ollama：<a href="https://ollama.com/blog/new-app"%(x)s>桌面 App</a>、<a href="https://docs.ollama.com/macos"%(x)s>macOS 要求</a>、<a href="https://ollama.com/pricing"%(x)s>价格</a>。LM Studio：<a href="https://lmstudio.ai/docs/app/system-requirements"%(x)s>系统要求</a>。Jan：<a href="https://www.jan.ai/docs/desktop/install/mac"%(x)s>Mac 安装</a>。</li>
<li>GitHub：<a href="https://github.com/ggml-org/llama.cpp"%(x)s>llama.cpp</a>、<a href="https://github.com/ml-explore/mlx-lm"%(x)s>mlx-lm</a>、<a href="https://github.com/a-ghorbani/pocketpal-ai"%(x)s>PocketPal AI</a>。</li>
<li>五题测试：Pinku 自测（5 个事实问题，MLX 4 位，Mac），2026 年 10 月。</li>
</ul>
<p>如有过时信息，请<a href="mailto:sagalabs@proton.me">告诉我们</a>。</p>
<p>说明：本站发布方 Saga Labs 也开发了 Pinku。Pinku 的测试结果按实测列出，包括它没有采用的模型。</p>
""",
)
