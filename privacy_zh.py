# -*- coding: utf-8 -*-
"""Texto en chino simplificado de los articulos del 20 oct 2026. Ver privacy_oct20.py.
Las politicas en ingles van parafraseadas; las de Doubao y Kimi, segun su texto chino.
Locally AI no se vende en la App Store de China (lookup cn, 20 oct): no se cita."""

DISCLOSE = ("<p>说明：运营本网站的 Saga Labs 也开发了 Pinku。本文对 Pinku 的描述和对其他应用一样，"
            "依据的是它的 App Store 页面，以及网络测试中我们实际测到的数据。</p>")

PINKU_PRIV = ("Pinku 把聊天记录保存在设备上，不会离开设备。Apple 隐私标签中，Pinku 只列出了购买记录和一个"
              "用于 Pinku Pro 的匿名 ID。")

# --------------------------------------------------------------------------
KEEP = dict(
    h1="ChatGPT、Claude、Gemini 等 AI 聊天会保存你的哪些对话？删除或导出聊天记录后会发生什么（2026）",
    desc=("ChatGPT、Claude、Gemini、Copilot、Perplexity、Grok、DeepSeek、Mistral、豆包和 Kimi "
          "会把对话保存多久，删除按钮实际做了什么，以及如何导出数据。依据各公司官方帮助页面，2026年10月20日核对。"),
    kicker="隐私", section="隐私",
    standfirst="删除的聊天会立刻从列表中消失。公司那边怎么处理，取决于公司、设置和副本的类型。以下是每家公司自己的说法，附链接。",
    body="""
<h2>简短回答</h2>

<p>大多数主流聊天机器人会一直保存你的对话，直到你删除，或者自动删除的期限到了。删除后，
对话会立刻从列表中消失，公司表示会在一定期限内从系统中清除，通常是 <strong>30 天</strong>。
每一份政策都有例外：为安全审查保留的副本、法律要求保留的数据，以及已经去标识化或已用于训练模型的数据。
导出能拿到一份聊天记录副本，但不会告诉你公司还保留了什么。</p>

<div class="table-scroll"><table>
<thead><tr><th>服务</th><th>默认保存多久</th><th>删除聊天后</th><th>默认用聊天训练吗</th><th>导出</th></tr></thead>
<tbody>
<tr><td>ChatGPT（Free、Go、Plus、Pro）</td><td>直到你删除</td><td>立刻从列表消失；30 天内删除，有例外</td><td>是，除非你关闭</td><td>设置、数据控制、导出：通过邮件或短信发送 ZIP 链接，最长 7 天，链接 24 小时有效</td></tr>
<tr><td>Claude（Free、Pro、Max）</td><td>直到你删除</td><td>立刻从历史中消失；30 天内从后台存储删除</td><td>只有你在隐私设置中允许才会</td><td>设置、隐私、导出数据；链接 24 小时有效</td></tr>
<tr><td>Gemini</td><td>18 个月后自动删除（可选 3 个月、36 个月或不删除）</td><td>经人工审核的对话不会随活动记录一起删除，最多保留 3 年</td><td>开启“保留活动记录”时会</td><td>Google Takeout；邮件链接 7 天有效</td></tr>
<tr><td>Microsoft Copilot</td><td>18 个月（旧版应用；新版未说明期限）</td><td>可删除单个或全部对话；后台删除时间未说明</td><td>是；可随时退出</td><td>所读页面未说明</td></tr>
<tr><td>Perplexity</td><td>账号存续期间</td><td>可逐个或全部删除对话；删除账号后 30 天内删除数据</td><td>“记忆”内容可能被使用；有开关</td><td>所读页面未说明</td></tr>
<tr><td>Grok</td><td>未给出具体期限</td><td>30 天内删除，除非出于法律、合规或安全原因需要保留</td><td>训练模型列在用途之中</td><td>通过 x.ai 隐私门户申请</td></tr>
<tr><td>DeepSeek</td><td>提供服务所必需的期间</td><td>可在设置中删除聊天记录；未给出期限</td><td>是；政策写明有权拒绝</td><td>有权获得数据副本，未描述按钮</td></tr>
<tr><td>豆包（字节跳动）</td><td>提供服务所必需的期间</td><td>可删除单个对话和账号</td><td>是，可在隐私设置中关闭</td><td>政策列出查阅、复制、删除等权利，没有导出按钮</td></tr>
<tr><td>Kimi（月之暗面）</td><td>实现服务目的所必需的时间</td><td>可删除会话和账号</td><td>没有开关，需联系客服</td><td>只能复制对话，没有导出功能</td></tr>
</tbody>
</table></div>

<p class="article-note">依据各公司的隐私政策和帮助中心，于%(date)s阅读。每个页面的链接和日期见文末来源。
表中写“未说明”表示我们查找过但没有找到，并不代表该功能不存在。</p>

<h2>ChatGPT（OpenAI）</h2>

<p>OpenAI 关于保存期限的页面（在我们阅读前一天更新）写道，普通和已归档的聊天会一直保存在账号中，直到你删除。
删除后，ChatGPT 会立刻从列表中移除，OpenAI 会安排在 30 天内从系统中永久删除，除非该聊天已经去标识化并与账号解除关联，
或 OpenAI 因安全或法律义务必须保留更久。删除的聊天无法恢复，客服也不行。临时聊天不会出现在历史中，
但 OpenAI 可能出于安全目的保留最多 30 天的副本。一个容易忽略的细节：删除聊天不会删除保存在“资料库”中的文件。</p>

<p>关于训练：对 Free、Plus 和 Pro 用户，OpenAI 可能使用你的内容训练模型。可以在设置的“数据控制”中关闭
<em>Improve the model for everyone</em>，或在隐私门户选择 <em>Do not train on my content</em>。
即使已经关闭，如果你对回答点了赞或踩，相关的整段对话仍可能被用于训练。</p>

<p>导出：设置、数据控制、导出，然后确认。链接通过邮件或短信发送，最长可能需要 7 天，收到后 24 小时失效。
ZIP 中包含聊天记录和其他账号数据，但无法找回已删除的聊天。另一个途径是隐私门户（Make a Privacy Request，Download my data）。</p>

<p>法院命令可以凌驾于这一切之上。2025 年，美国法院在《纽约时报》版权案中要求 OpenAI 保留用户已删除的聊天，
后来对新聊天取消了这一要求。完整时间线见<a href="%(gdpr)s">我们之前的文章（英文）</a>。</p>

<h2>Claude（Anthropic）</h2>

<p>Anthropic 的保存期限页面（2026年7月1日）适用于 Free、Pro 和 Max。删除的对话会立刻从聊天历史中移除，
并在 30 天内从后台存储中删除。例外情况写明了数字：</p>
<ul>
<li>如果你允许用聊天改进 Claude，这些聊天会以去标识化形式在训练流程中保存最多 5 年。</li>
<li>被安全系统标记的对话：输入和输出最多 2 年，分类评分最多 7 年。</li>
<li>你提交的反馈（赞或踩）：5 年。</li>
</ul>
<p>只有你选择允许才会用于训练，开关在设置的“隐私”中。关闭后不再用于今后的训练；已经完成的训练中用到的数据会留在模型里。
无痕聊天即使开着该设置也不会用于训练。导出：设置、隐私、导出数据；下载链接在发送后 24 小时失效。</p>

<h2>Gemini（Google）</h2>

<p>Google 的 Gemini 隐私中心（2026年10月19日更新）写道，默认情况下活动记录会在 <strong>18 个月</strong>后自动删除，
可以改为 3 个月或 36 个月，也可以关闭自动删除。关闭“保留活动记录”时以及临时聊天中，对话仍会随账号保存
<strong>72 小时</strong>，并且不会用于训练 Google 的模型。</p>

<p>最重要的例外：部分对话会由人工审核员阅读，这些经过审核的对话在你删除活动记录时不会被删除，
而是与账号断开关联后保存最多三年。导出请使用 Google Takeout，勾选 Gemini 和“我的活动”中的 Gemini 应用；邮件下载链接 7 天内有效。</p>

<h2>Microsoft Copilot</h2>

<p>根据 Microsoft 的说明，Copilot 默认保存对话活动 18 个月。Microsoft 现在注明该页面只适用于旧版应用，新版应用的隐私页面没有给出期限（2026年10月30日核对）。你可以随时删除单个对话或全部历史；
页面没有说明 Microsoft 那边删除需要多久。部分对话会经过自动和人工审核。Microsoft 把训练模型列为对话的用途之一，
并表示你可以随时在隐私设置中退出，文字和语音对话分开设置。</p>

<h2>Perplexity、Grok、DeepSeek 与 Mistral</h2>

<ul>
<li><strong>Perplexity</strong> 在账号存续期间保存个人信息。删除账号后 30 天内从服务器删除，期间重新登录会取消删除。
对话可以逐个或全部删除；上传的文件默认保存 30 天。“记忆”中的内容可能被用于改进模型，Perplexity 表示可以关闭。</li>
<li><strong>Grok</strong>（xAI，现为 SpaceXSI；2026年10月11日的政策）：Private Chat 中的对话、已删除的对话和已删除的账号
会在 30 天内清除，除非出于法律、合规或安全原因需要保留。训练模型是所列的内容用途之一。</li>
<li><strong>DeepSeek</strong>（2026年2月10日的政策）在提供服务所必需的期间内保存个人数据，用于训练其技术，
并写明数据在中华人民共和国境内收集、处理和存储。可以在设置中删除聊天记录；注销账号不可恢复，未给出删除期限。</li>
<li><strong>Vibe by Mistral</strong>（原 Le Chat）：你手动删除后，对话会从系统中移除，但可能出于监控和法律目的保留。
默认情况下用户没有退出训练；开关是应用数据设置中的 <em>Enable data sharing</em>。</li>
</ul>

<h2>豆包与 Kimi</h2>

<ul>
<li><strong>豆包</strong>（隐私政策 2026年9月10日更新）：仅在为提供豆包服务之目的所必需的期间内保留个人信息，
在中国境内运营中收集的信息存储在中国境内。可以删除单个对话，也可以在“设置-豆包账号管理”中注销账号。
政策写明会使用输入和回复等内容数据改进模型，可在“设置-隐私与权限-帮助模型改进效果”中关闭。
政策列出了查阅、复制、更正、删除等权利，没有导出功能。</li>
<li><strong>Kimi</strong>（隐私政策 2026年8月24日更新）：个人信息存储于中华人民共和国境内，保存期限为实现服务目的所必需的时间。
可以在“历史会话”中删除会话，也可以注销账号。没有关闭训练的开关：需要联系客服，核实身份后停止将你的内容用于模型训练。
导出只能用“复制”按钮复制对话。</li>
</ul>

<h2>一次正式申请的结果</h2>

<p>2026年4月15日，我用自己的个人账号向 OpenAI 和 Anthropic 发出了正式的 GDPR 申请：依据第 15 条，
要求提供他们保存的全部数据，包括安全系统的标记和从我的聊天中派生的数据；依据第 17 条，要求删除，
并书面确认删除了什么、保留的数据依据什么法律基础。Anthropic 当天自动回复确认收到。OpenAI 于 4 月 17 日回复；
Anthropic 的人工回复在 5 月 16 日送达，也就是一个月零一天之后。GDPR 规定的答复期限是一个月（第 12 条第 3 款）。</p>

<p>两家的回复都很礼貌，都指向自助设置。两家都没有书面确认删除了什么，没有说明保留数据的法律基础，
也没有针对访问请求提供数据本身。我没有向数据保护机构投诉，因此这件事没有任何裁定。
完整往来和原文引用见<a href="%(gdpr)s">英文文章</a>。</p>

<h2>如何让对话不留在别人的服务器上</h2>

<ol>
<li><strong>开始输入之前</strong>，关闭训练（ChatGPT、Copilot、Mistral、豆包），或保持关闭（Claude）。
重要的对话不要点赞或踩：ChatGPT、Claude 和 Mistral 对反馈有单独的规则。</li>
<li><strong>敏感问题使用临时或无痕聊天</strong>，但要记住它们也会保存一段时间：ChatGPT 和 Grok 最多 30 天，Gemini 72 小时。</li>
<li><strong>删除不需要的内容</strong>，如需副本请先导出：导出无法找回已删除的聊天。</li>
<li><strong>对于绝不能到达任何服务器的对话</strong>，请使用在自己设备上运行的模型。电脑上可以用 Ollama 或 LM Studio；
iPhone 或 Mac 上有 PocketPal AI、Private LLM 或 <a href="%(pinku)s">Pinku</a> 等应用。%(pinku_priv)s
我们在 Mac 上测试了这类应用实际向网络发送了什么：<a href="%(p_net)s">结果见这里</a>。</li>
</ol>
""",
    faq=[
        ("删除 ChatGPT 的聊天后，真的删除了吗？",
         "聊天会立刻从账号中消失，OpenAI 表示会安排在 30 天内永久删除，除非该聊天已去标识化并与账号解除关联，"
         "或因安全或法律义务需要保留更久。删除后无法恢复。"),
        ("Claude 删除的聊天会保留多久？",
         "Anthropic 表示删除的聊天会立刻从历史中消失，30 天内从后台存储删除。被安全系统标记的聊天最多保留 2 年"
         "（评分最多 7 年），经你允许用于训练的聊天以去标识化形式最多保留 5 年。"),
        ("删除 Gemini 活动记录会删除人工审核过的对话吗？",
         "不会。Google 表示经过审核的对话不会随活动记录一起删除，而是与账号断开关联后最多保留三年。"),
        ("豆包会用我的对话训练模型吗？",
         "豆包隐私政策写明会使用输入和回复等内容数据改进模型，可以在“设置-隐私与权限-帮助模型改进效果”中关闭。"),
        ("临时聊天或无痕聊天会被保存吗？",
         "会保存一段时间。OpenAI 可能出于安全目的保留临时聊天最多 30 天；关闭活动记录时 Google 保留 Gemini 对话 72 小时；"
         "Grok 的 Private Chat 在 30 天内删除，除非必须保留。"),
        ("哪个 AI 聊天完全不保存我的对话？",
         "本文列出的云端聊天机器人都没有这样承诺。在自己设备上运行的模型，例如电脑上的 Ollama 或 LM Studio，"
         "或 iPhone 和 Mac 上的 PocketPal AI、Private LLM、Pinku，会把对话留在设备上。"),
    ],
    sources="""
<h2>来源</h2>
<ul>
<li>OpenAI 帮助中心：<a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt"%(x)s>Chat and file retention in ChatGPT</a>（2026年10月19日更新）、<a href="https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data"%(x)s>Exporting your ChatGPT history and data</a> 和 <a href="https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance"%(x)s>How your data is used to improve model performance</a>（均为2026年10月20日更新）。</li>
<li>Anthropic：<a href="https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data"%(x)s>How long do you store my data?</a>（2026年7月1日）、<a href="https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training"%(x)s>Is my data used for model training?</a>（2026年3月16日）、<a href="https://support.claude.com/en/articles/9450526-export-your-claude-data"%(x)s>Export your Claude data</a>。</li>
<li>Google：<a href="https://support.google.com/gemini/answer/13594961?hl=zh-Hans"%(x)s>Gemini 隐私中心</a>（2026年10月19日更新）和 <a href="https://support.google.com/gemini/answer/16920332"%(x)s>使用 Google Takeout 导出</a>。</li>
<li>Microsoft：<a href="https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot"%(x)s>Privacy FAQ for Microsoft Copilot</a> 和 <a href="https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls"%(x)s>Microsoft Copilot privacy controls</a>。</li>
<li>Perplexity：<a href="https://www.perplexity.ai/help-center/en/articles/10354873-how-long-does-perplexity-retain-my-search-history-profile-data-and-personal-information"%(x)s>保存期限</a>、<a href="https://www.perplexity.ai/help-center/en/articles/10354879-account-deletion"%(x)s>删除账号</a>、<a href="https://www.perplexity.ai/help-center/en/articles/11564562-self-serve-data-deletion"%(x)s>自助删除数据</a>、<a href="https://www.perplexity.ai/help-center/en/articles/10968016-memory"%(x)s>记忆</a>。</li>
<li><a href="https://x.ai/legal/privacy-policy"%(x)s>SpaceXSI（xAI）隐私政策</a>，2026年10月11日。</li>
<li><a href="https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html"%(x)s>DeepSeek 隐私政策</a>，2026年2月10日。</li>
<li>Mistral：<a href="https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr"%(x)s>删除与保存</a> 和 <a href="https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training"%(x)s>退出训练</a>（2026年9月3日）。</li>
<li><a href="https://www.doubao.com/legal/privacy"%(x)s>豆包隐私政策</a>（2026年9月10日更新，9月17日生效）和 <a href="https://www.kimi.com/user/agreement/userPrivacy?version=v2"%(x)s>Kimi 隐私政策</a>（2026年8月24日更新，8月31日生效）。</li>
<li>GDPR <a href="https://gdpr-info.eu/art-12-gdpr/"%(x)s>第 12 条</a>、<a href="https://gdpr-info.eu/art-15-gdpr/"%(x)s>第 15 条</a>和<a href="https://gdpr-info.eu/art-17-gdpr/"%(x)s>第 17 条</a>。</li>
</ul>
<p>所有页面均于%(date)s阅读。政策会变化；如有过时内容，请<a href="mailto:sagalabs@proton.me">告诉我们</a>，我们会更正。</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
NET = dict(
    h1="本地 AI 应用会把你的数据发到网上吗？我们在 Mac 上监测了 Ollama、LM Studio 和 Pinku",
    desc=("2026年10月20日在 Mac 上对三款本地 AI 应用做的网络测试：Ollama、LM Studio 和 Pinku 在打开、下载模型、"
          "聊天和闲置时连接了哪里。使用 nettop 和 macOS 日志测量，公开方法和原始数据。"),
    kicker="实验", section="实验",
    standfirst=("聊天过程中，三款应用都没有建立任何互联网连接。聊天之外就不一样了：每款应用在打开或下载模型时"
                "都会连接自己的服务器，其中一款闲置时也会。以下是我们看到的、测量方法，以及我们看不到的部分。"),
    dataset=dict(
        name="Ollama、LM Studio 和 Pinku 在 macOS 上的网络连接，2026年10月20日",
        description="在 macOS 26.7.1 上，用 nettop 每秒记录各进程的连接（远程地址、收发字节），覆盖打开、下载模型、聊天和闲置。",
        measurementTechnique="nettop（按进程，每秒采样）、lsof、macOS 统一日志、应用缓存",
        variableMeasured=["远程主机", "接收字节", "发送字节", "阶段"],
    ),
    body="""
<h2>简短回答</h2>

<p><strong>聊天时什么都没有发送。</strong>三款应用在提问和回答期间都没有建立任何到 Mac 之外的连接。网络流量发生在聊天之外：</p>
<ul>
<li><strong>下载模型</strong>一定要联网，这在意料之中：连接 Ollama 的模型仓库、Hugging Face，或者 LM Studio 自己的服务器。</li>
<li><strong>打开应用</strong>：Ollama 没有对外连接。LM Studio 首次启动下载了约 172 MB 的推理引擎，之后每次约 1 MB。
Pinku 在加载已安装的模型时向 huggingface.co 发出了四个小请求。</li>
<li><strong>闲置</strong>：Ollama 和 Pinku 五分钟内什么都没发送。LM Studio 在一次聊天后不久，向自己的服务器建立了约 30 个连接。</li>
</ul>

<h2>结果</h2>

<div class="table-scroll"><table>
<thead><tr><th>应用</th><th>打开</th><th>下载模型</th><th>聊天</th><th>闲置 5 分钟</th></tr></thead>
<tbody>
<tr><td>Ollama 0.20.2（Homebrew）</td><td>没有对外连接；服务只监听 127.0.0.1</td><td>registry.ollama.ai 和 Cloudflare 存储：接收 524 MB，发送 125 KB</td><td>没有对外连接</td><td>没有对外连接</td></tr>
<tr><td>LM Studio 0.4.26</td><td>首次启动：未做任何操作，从 extensions.lmstudio.ai 下载约 172 MB（推理引擎）。之后：从 lmstudio.ai 约 1 MB</td><td>经由 search.lmstudio.ai/v1/hf-proxy：接收 352 MB，发送 84 KB</td><td>聊天本身没有；用默认命令时，LM Studio 同时获取了模型目录（接收约 150 KB，发送 12 KB）</td><td>一次约 30 个到 lmstudio.ai 地址的连接，接收 3 MB，发送 31 KB，之后没有</td></tr>
<tr><td>Pinku Mac 版 1.0.7</td><td>还没有模型：没有。已安装模型：向 huggingface.co 发出 4 个请求，接收约 35 KB，发送 23 KB</td><td>huggingface.co 以及 Hugging Face 在亚马逊服务器上的存储：0.4 GB 的模型约 350 MB</td><td>没有</td><td>没有</td></tr>
</tbody>
</table></div>

<p class="article-note">%(date)s在一台 Mac 上测得。“没有”表示在整个阶段中，nettop 没有显示该应用的进程连接到 Mac 之外的任何地址；
到 127.0.0.1 的连接（应用与自身通信）不计算在内。</p>

<h2>Ollama</h2>

<p>我们使用的是 Homebrew 版本，以后台服务运行。启动时，它在 127.0.0.1:11434 上开启服务，并启动一个与之通信的辅助进程，都是本地的。
<code>ollama pull qwen3:0.6b</code> 连接了 registry.ollama.ai，然后从 Cloudflare 存储下载了 524 MB。
用 <code>ollama run</code> 提问时只与本地服务通信，之后五分钟也是如此。这只适用于命令行版本：
从 ollama.com 下载的 Ollama 应用有自己的窗口和更新程序，我们没有测试。</p>

<h2>LM Studio</h2>

<p>首次启动时，在我们还没做任何操作之前，LM Studio 就从 extensions.lmstudio.ai 下载了约 172 MB。
它自己的下载记录列出了内容：llama.cpp 引擎、一个 Python 运行环境和一个名为 harmony 的工具。之后每次启动从 lmstudio.ai 地址获取约 1 MB。</p>

<p>模型下载并不是直接连接 Hugging Face。我们请求了 <em>mlx-community/Qwen3-0.6B-4bit</em>，LM Studio 的记录显示所有文件都来自
<code>search.lmstudio.ai/v1/hf-proxy/&hellip;</code>，这是 LM Studio 运营的代理。未改动的设置文件中是
<code>"useHFProxy": true</code>。也就是说，LM Studio 的服务器能看到你下载了哪些模型。但这并不意味着它们能看到你的聊天。</p>

<p>我们无法用工具操作 LM Studio 的聊天窗口，所以通过 LM Studio 自带、使用同一引擎的 <code>lms chat</code> 命令聊天。
用默认命令时，LM Studio 在回答期间从 lmstudio.ai 获取了模型目录：接收约 150 KB，发送 12 KB。加上
<code>--dont-fetch-catalog</code> 选项后，同样的问题没有产生任何对外连接。随后闲置的五分钟里，LM Studio 在第 45 到 60 秒之间
向 lmstudio.ai 地址建立了约 30 个连接（接收 3 MB，发送 31 KB，每个连接发送不到 3 KB），之后再无连接。本地服务只监听 127.0.0.1。</p>

<h2>Pinku</h2>

<p>Pinku 是一款在设备上运行开放模型的 iPhone 和 Mac 应用。%(pinku_priv)s Mac App Store 上的版本是 1.0.7。
测试用的 Mac 上没有安装 Pinku，因此我们从源代码编译了 1.0.7，并用单独的应用标识运行，让它像全新安装一样启动。</p>

<ul>
<li><strong>首次启动、没有模型</strong>：60 秒内没有任何连接。</li>
<li><strong>下载最小的模型</strong>（Qwen3 0.6B，0.4 GB）：向 huggingface.co 请求模型文件，权重来自 Hugging Face 在亚马逊服务器上的存储。
我们的记录在下载开始 22 秒后才启动，捕获了约 347 MB；应用的网络缓存中只有 huggingface.co 的地址。</li>
<li><strong>已安装模型后打开</strong>：七秒内向 huggingface.co 发出四个 HTTPS 请求，接收约 35 KB，发送 23 KB。
响应是“304 Not Modified”：Pinku 在检查 Mac 上的模型文件是否仍是最新版本。请求中包含模型名称，Hugging Face 能看到这台 Mac 的 IP 地址。请求中没有聊天内容。</li>
<li><strong>聊天</strong>（一个问题，约 85 秒得到回答）：没有连接。</li>
<li><strong>闲置 5 分钟</strong>：没有连接。</li>
</ul>

<p>Pinku 的 App Store 描述没有提到启动时的这项检查；这是我们在本次测试中发现的。购买 Pinku Pro 通过 Apple 自己的系统进程与 Apple 通信；
用这些工具无法把这部分流量归属到某一个应用，所以购买不在结果之内。</p>

<h2>测量方法</h2>

<ol>
<li>一台 Apple 芯片的 Mac，macOS 26.7.1，Wi-Fi，2026年10月20日。没有更改安全设置，没有使用管理员密码，没有授予新权限。</li>
<li>用 macOS 自带的网络监视工具 <strong>nettop</strong>，每秒记录所有进程的所有套接字，包括远程地址和收发字节，只保留各应用的进程。</li>
<li>用 <strong>lsof</strong> 查看每个应用监听的端口。</li>
<li>主机名来自应用自己的记录（Pinku 的网络缓存、LM Studio 的下载记录）、macOS 日志，以及对地址的 DNS 查询。</li>
<li>每个应用四个阶段：打开（60 到 90 秒）、下载最小的模型、一个问题（<em>Write three short sentences about the sea</em>）、打开应用闲置五分钟。</li>
<li>测试结束后，我们删除了 LM Studio、下载的模型和我们编译的 Pinku。</li>
</ol>

<h2>我们看不到的部分</h2>

<ul>
<li><strong>连接的内容。</strong>连接是加密的。不抓包（需要管理员密码）只能看到数据去了哪里、有多少，看不到具体内容。</li>
<li><strong>极短的连接</strong>，在一秒内打开又关闭，nettop 可能漏掉。对 Pinku 和 LM Studio，应用自己的日志和缓存与 nettop 的结果一致。</li>
<li><strong>iPhone。</strong>以上都是在 Mac 上测的。iOS 上的应用无法用这种方式检查。</li>
<li><strong>更长的时间。</strong>五分钟闲置不等于一天。每天检查一次更新的应用不会在测试中出现。</li>
<li><strong>其他应用。</strong>我们只测了三款。Jan、GPT4All、Msty 等不在本次测试中。</li>
</ul>

<h2>自己如何检查一个应用</h2>

<p>打开“终端”，在使用应用时运行 <code>nettop -P -L 0 -s 1 -n</code>；每一行显示一个进程及其收发字节。
只看一个应用，可以用 <code>nettop -p</code> 加进程名。查看监听端口用 <code>lsof -nP -iTCP -sTCP:LISTEN</code>。
在聊天时和下载模型时各做一次，就能看到本文所说的区别。</p>

<p>问题到达云端聊天机器人之后会被保存多久，请看
<a href="%(p_keep)s">ChatGPT、Claude、Gemini 等会保存什么，删除有什么用</a>。</p>
""",
    faq=[
        ("Ollama 会把我的聊天发到网上吗？",
         "在我们的 Mac 测试中（Homebrew 版 Ollama 0.20.2，2026年10月20日）不会。聊天和闲置五分钟只有到 127.0.0.1 的本地连接。"
         "下载模型时会连接 registry.ollama.ai。"),
        ("不下载东西时 LM Studio 会联网吗？",
         "会。在我们的测试中，它首次启动下载了约 172 MB 的引擎，之后每次启动约 1 MB，用 lms 命令聊天时获取了模型目录，"
         "闲置时还向自己的服务器建立过约 30 个连接。我们没有看到传送聊天内容的连接。"),
        ("LM Studio 能看到我下载了哪些模型吗？",
         "默认设置下能：从 Hugging Face 的下载经由 search.lmstudio.ai/v1/hf-proxy，设置文件中 useHFProxy 为 true。"),
        ("Pinku 聊天时会发送什么吗？",
         "不会。Pinku Mac 版 1.0.7 在聊天和闲置时都没有连接。它会连接 Hugging Face 下载模型，1.0.7 版在加载已安装的模型时也会连接，用于检查模型文件。"),
        ("怎样查看 Mac 上的应用发送了什么？",
         "使用应用时在“终端”中运行 nettop -P -L 0 -s 1 -n。它会列出每个进程收发的字节，不需要管理员密码。"),
    ],
    sources="""
<h2>来源与工具</h2>
<ul>
<li>Apple，macOS 26.7.1 中 nettop 和 lsof 的手册（<code>man nettop</code>、<code>man lsof</code>）。</li>
<li><a href="https://ollama.com/"%(x)s>Ollama</a> 0.20.2，通过 Homebrew 安装（<code>brew install ollama</code>）。</li>
<li><a href="https://lmstudio.ai/"%(x)s>LM Studio</a> 0.4.26，Homebrew cask，从 lmstudio.ai 下载官方安装包。</li>
<li><a href="%(pinku)s">Pinku</a> Mac 版 1.0.7，由源代码编译；App Store 隐私标签为%(date)s所见。</li>
<li>模型：<a href="https://ollama.com/library/qwen3"%(x)s>qwen3:0.6b</a>（Ollama）和 <a href="https://huggingface.co/mlx-community/Qwen3-0.6B-4bit"%(x)s>mlx-community/Qwen3-0.6B-4bit</a>（LM Studio 和 Pinku）。</li>
</ul>
<p>如果你重复测试得到了不同结果，请<a href="mailto:sagalabs@proton.me">告诉我们</a>，我们会补充。</p>
""" + DISCLOSE,
)

ARTICLES = {"keep": KEEP, "net": NET}
for _a in ARTICLES.values():
    _a["body"] = _a["body"].replace("%(pinku_priv)s", PINKU_PRIV)
