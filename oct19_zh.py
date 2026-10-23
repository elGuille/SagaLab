# -*- coding: utf-8 -*-
"""简体中文 (19 oct 2026). Datos del App Store de China continental (country=cn)."""

PINKU_ID = "https://apps.apple.com/app/id6754878073"
CN = "https://apps.apple.com/cn/app/id"

PINKU_PRIV = "聊天内容不会离开你的设备；Apple 隐私标签只列出购买记录和一个用于 Pinku Pro 购买的匿名用户 ID。"

DISCLOSE = ('<h2>来自 Saga Labs 团队</h2>\n<p>Pinku 是我们开发的，也是本页提到的 App 之一。我们做它，是因为 Ollama、LM Studio 等运行开放模型的优秀工具需要一定的技术知识：选择模型文件和量化方式，有时还要用终端。Pinku 面向其他所有人：从 App Store 安装，点一下模型，就能在 iPhone 或 Mac 上私密聊天，不用终端，也不用任何设置。代价是只有一份为每台设备挑选的小模型清单，所以对想运行任意模型的人来说，它替代不了那些工具。本页关于 Pinku 的信息和其他 App 一样，来自 App Store 页面。</p>')

NOT_IN_CN = ("截至 %(date)s，中国大陆 App Store 没有上架 ChatGPT、Gemini、Claude、Locally AI 和 Enclave，"
             "所以本文不列入：用中国大陆的 Apple 账户无法下载。")

# --------------------------------------------------------------------------
OFFLINE = dict(
    h1="Apple Intelligence 能离线使用吗？iPhone 断网时还能用什么（2026）",
    desc=("Apple Intelligence 有的请求在 iPhone 上处理，有的发到 Apple 服务器，而且目前在中国大陆购买的设备上"
          "不能使用。Apple 官方说明了哪些功能需要联网、如何查看哪些请求离开了手机，以及哪些 AI 聊天 App 可以完全离线。"),
    kicker="指南", section="指南",
    standfirst="部分可以。简单请求在设备上完成，复杂请求交给 Apple 的私密云计算（Private Cloud Compute）。在中国大陆，Apple Intelligence 目前根本无法启用。",
    steps_h="如何确认某个功能是在 iPhone 上运行的",
    steps=[
        ("打开报告。",
         "前往设置、隐私与安全性、Apple 智能报告（英文说明里叫 Apple Intelligence &amp; PCC Report），选择时间范围。Mac 上在系统设置的同一位置。"),
        ("使用你想确认的功能。", "改写一段文字、生成一张图片，或者问 Siri 一个问题。"),
        ("导出报告并查看。",
         "Apple 表示，报告会显示离开设备、由私密云计算处理的请求；如果开启了 ChatGPT 等 Apple Intelligence 扩展，也会显示发给它们的请求。报告里没有你的请求，就说明它是在 iPhone 上完成的。"),
        ("用飞行模式再确认一次。", "打开飞行模式并关闭 Wi-Fi 和蓝牙，再试一次。仍然可用，就说明它在设备上运行。"),
    ],
    body="""
<h2>简短回答</h2>

<p>部分可以。Apple Intelligence 不是一个模型放在一个地方。Apple 的隐私页面写道：
<a href="%(priv)s"%(x)s>“在许多情况下，Apple Intelligence 模型完全在设备上运行”</a>；
当任务需要的算力超过设备本身时，“Apple Intelligence 可能会把你的请求发送到私密云计算”，
也就是 Apple 自己的服务器。Apple 举的例子是 Image Playground：图片描述会发到私密云计算生成图片。</p>

<p>Apple 还列出了<a href="%(reqs)s"%(x)s>“依赖服务器端模型”</a>、因此有每日使用上限的功能：
Siri AI、智能照片编辑工具、Image Playground，以及快捷指令中的 AFM 3 云端模型。这些需要联网。
Apple 没有公布哪些功能在飞行模式下仍可使用，其余功能需要你自己检查（步骤见下文）。</p>

<div class="table-scroll"><table>
<thead><tr><th>功能</th><th>Apple 说明的运行位置</th><th>断网时</th></tr></thead>
<tbody>
<tr><td>Siri AI（测试版）</td><td>属于依赖服务器端模型的功能；会联网获取最新信息</td><td>需要联网</td></tr>
<tr><td>Image Playground</td><td>私密云计算（Apple 自己的例子）</td><td>需要联网</td></tr>
<tr><td>智能照片编辑（Spatial Reframing、Extend、改进的清除）</td><td>属于有服务器端使用上限的功能</td><td>需要联网</td></tr>
<tr><td>快捷指令 Use Model：<em>On-Device</em></td><td>在 iPhone 上，“无需网络连接”</td><td>可用</td></tr>
<tr><td>快捷指令 Use Model：<em>Cloud</em> 和 <em>Cloud Pro</em></td><td>私密云计算</td><td>需要联网</td></tr>
<tr><td>快捷指令 Use Model：<em>Extension Model</em></td><td>ChatGPT</td><td>需要联网</td></tr>
<tr><td>优先通知</td><td>设备端模型（Apple 的例子）</td><td>在设备上</td></tr>
<tr><td>写作工具、摘要等</td><td>Apple 没有逐项说明</td><td>请自行检查</td></tr>
</tbody>
</table></div>

<p class="article-note">来源：Apple 的 <a href="%(reqs)s"%(x)s>Apple Intelligence 要求页面</a>、
<a href="%(priv)s"%(x)s>Apple Intelligence 隐私页面</a>和<a href="%(sc)s"%(x)s>快捷指令使用手册</a>（英文），
核对于 %(date)s。引文由英文翻译；Use Model 的选项名称沿用英文手册。</p>

<h2>在中国大陆：目前无法使用</h2>

<p>Apple 的说明很明确：<a href="%(reqs)s"%(x)s>在中国大陆购买的设备目前无法使用 Apple Intelligence 功能</a>；
在中国大陆以外购买的设备，如果人在中国大陆、且 Apple 账户地区也是中国大陆，同样无法使用。
Apple 表示等功能在中国大陆推出后，已购买的支持设备可以启用一组核心功能，而新功能要等监管要求完成后才会提供。
<a href="%(siri)s"%(x)s>Siri AI</a> 也明确不支持 Apple 账户地区为中国大陆的用户。</p>

<h2>哪些 iPhone 支持 Apple Intelligence</h2>

<ul>
<li><strong>iPhone：</strong>iPhone 15 Pro、15 Pro Max、所有 iPhone 16 及更新机型、iPhone Air。
iPhone 15、15 Plus 和更早的机型都不支持，尽管 <a href="%(ios)s"%(x)s>iOS 27 支持 iPhone 11 及更新机型</a>。</li>
<li><strong>存储：</strong>设备上最多占用 8 GB，iPhone 17 Pro、17 Pro Max 和 iPhone Air 最多 14 GB。</li>
<li><strong>语言：</strong>设备语言和 Siri 语言必须一致且受支持，简体中文和繁体中文都在列表中。Siri AI 目前只支持英语。</li>
</ul>

<h2>私密云计算真的私密吗？</h2>

<p>设计上是。Apple 表示在那里处理的数据“不会被存储，也不会让 Apple 访问”，只用于完成请求；
收集的少量信息（请求大小、功能、耗时）不与 Apple 账户关联。但请求仍然离开了 iPhone，由服务器作答。
如果你需要对话永远不离开设备，或者在飞机上也能用，服务器端功能做不到。另外，Apple 说 Siri AI 的 App
会通过 iCloud 同步对话记录。</p>

<h2>如何查看哪些请求离开了 iPhone</h2>

<p>Apple 会记录每一个发往其服务器的请求。这是判断某个功能最可靠的方法。</p>
%(steps)s
<p>Apple 提醒：如果面容 ID 或触控 ID 暂时停用，报告可能不会显示最近的请求。</p>

<h2>需要完全离线的 AI 聊天</h2>

<p>下面这些 App 只需下载一次开源模型，之后在手机上直接回答，不经过任何服务器。它们不需要 Apple Intelligence，
在中国大陆也能下载。共同的代价是：1 到 5 GB 的模型明显弱于云端模型，不能联网搜索，首次下载需要网络。</p>

<ul>
<li><a href="%(pinku)s">Pinku</a>：iPhone 和 Mac，无需账户，界面有简体中文。需要 iOS 18.6 以及支持 Metal 3 的
iPhone，Apple 列出的是 <a href="%(metal)s"%(x)s>iPhone 12 及更新机型</a>。默认模型免费；更大的模型、自定义指令、
听写和朗读需要 Pinku Pro（App 内购买）。""" + PINKU_PRIV + """</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>：免费、<a href="%(gh)s"%(x)s>开源</a>，iOS 15.1 及以上，可加载
Hugging Face 上任意 GGUF 模型；界面为英文。</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>：一次性 ¥38，iOS 17 及 A12 仿生芯片或更新，支持 Siri 和快捷指令；
界面为英文。</li>
</ul>

<p>""" + NOT_IN_CN + """ 旧款 iPhone 请看<a href="%(p_noai)s">没有 Apple Intelligence 的 iPhone 适合用哪些 AI App</a>。</p>
""",
    faq=[
        ("在中国大陆能用 Apple Intelligence 吗？",
         "目前不能。Apple 表示，在中国大陆购买的设备目前无法使用 Apple Intelligence；在其他地区购买的设备，如果人在中国大陆且 Apple 账户地区也是中国大陆，同样无法使用。"),
        ("Apple Intelligence 在飞行模式下能用吗？",
         "部分可以。很多请求在设备上完成，快捷指令里的 On-Device 模型无需网络。Siri AI、智能照片编辑、Image Playground 和快捷指令中的 AFM 3 云端模型需要联网。"),
        ("怎么知道请求有没有被发到服务器？",
         "在设置、隐私与安全性中打开 Apple 智能报告。Apple 表示报告会记录发往私密云计算以及 ChatGPT 等扩展的请求。"),
        ("哪些 iPhone 支持 Apple Intelligence？",
         "iPhone 15 Pro、15 Pro Max、所有 iPhone 16 及更新机型和 iPhone Air。iPhone 15、15 Plus 和更早机型即使升级到 iOS 27 也不支持。"),
        ("在中国大陆有可以离线使用的 AI 聊天 App 吗？",
         "有。中国大陆 App Store 上的 Pinku（简体中文界面，iPhone 12 及以上）、PocketPal AI 和 Private LLM 都在 iPhone 上运行模型，只需联网下载一次模型。"),
    ],
    sources="""
<h2>来源</h2>
<ul>
<li>Apple，<a href="%(reqs)s"%(x)s>如何获取新一代 Apple Intelligence</a>（设备、存储、语言、欧盟和中国大陆、服务器端功能上限），发布于 2026 年 9 月 14 日。</li>
<li>Apple，<a href="%(siri)s"%(x)s>如何获取 Siri AI</a>（测试版、仅英语、欧盟、中国大陆、iCloud 同步），发布于 2026 年 9 月 22 日。</li>
<li>Apple，<a href="%(priv)s"%(x)s>Apple Intelligence 与隐私</a>（设备端或私密云计算、报告）。</li>
<li>Apple，<a href="%(sc)s"%(x)s>Use Apple Intelligence in Shortcuts</a>（Use Model：On-Device、Cloud、Cloud Pro、Extension Model）。</li>
<li>Apple，<a href="%(ios)s"%(x)s>iOS 27</a> 和 <a href="%(metal)s"%(x)s>Apple 设备对 Metal 的支持</a>（iPhone 12 起支持 Metal 3）。</li>
<li>中国大陆 App Store 页面：Pinku、PocketPal AI、Private LLM，查看于 %(date)s。</li>
</ul>
<p>以上均核对于 %(date)s。如有过时信息，请<a href="mailto:sagalabs@proton.me">告诉我们</a>。</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
NOAI = dict(
    h1="没有 Apple Intelligence 的 iPhone 适合用哪些 AI App（2026）",
    desc=("iOS 27 支持 iPhone 11 起的机型，Apple Intelligence 只支持 iPhone 15 Pro 起，而且在中国大陆暂不可用。"
          "PocketPal、Private LLM、Pinku、豆包、DeepSeek、Kimi、千问和 Vibe：中国大陆 App Store 能下载什么、离线还是云端、要求和价格。"),
    kicker="排行", section="排行",
    standfirst="你的 iPhone 已经是 iOS 27，却没有 Apple Intelligence；在中国大陆，新机型也一样。中国大陆 App Store 里这八个 App 可以补上 AI 助手。",
    rank=[("PocketPal AI", CN + "6502579498"), ("Private LLM - 本地AI聊天", CN + "6448106860"),
          ("Pinku: Private Offline AI Chat", PINKU_ID), ("豆包 - 生活工作 AI 助手", CN + "6459478672"),
          ("Kimi", CN + "6474233312"), ("千问 - 阿里AI助手", CN + "6466733523"),
          ("DeepSeek - AI 智能助手", CN + "6737597349"), ("Vibe by Mistral (ex-Le Chat)", CN + "6740410176")],
    body="""
<p>各 App 的信息来自中国大陆 App Store，核对于 %(date)s。</p>

<p><strong>说明：本榜第 3 名的 Pinku 是我们开发的。</strong></p>

<p><a href="%(ios)s"%(x)s>iOS 27 支持 iPhone 11 及更新机型</a>以及 iPhone SE（第二代及以后）。
<a href="%(reqs)s"%(x)s>Apple Intelligence</a> 则需要 iPhone 15 Pro、15 Pro Max、任何 iPhone 16 及更新机型或 iPhone Air，
而且在中国大陆购买的设备目前无法使用。所以 iPhone 11 到 15 根本没有 Apple Intelligence，在中国大陆的新机型也用不了。
下面的 App 用两种方式补上：一种在手机上直接运行模型，无需联网；另一种是云端助手。</p>

<p class="article-note">""" + NOT_IN_CN + """</p>

<h2>排行</h2>

<ol>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>：最旧的 iPhone 也能用，代码开源。</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>：一次性付费，支持 iPhone 11 和 SE。</li>
<li><a href="%(pinku)s">Pinku</a>：离线、私密，简体中文界面，适合 iPhone 12 到 15。</li>
<li><a href="%(doubao)s"%(x)s>豆包</a>：评分人数最多的云端助手（字节跳动）。</li>
<li><a href="%(kimi)s"%(x)s>Kimi</a>：评分最高的云端助手（月之暗面）。</li>
<li><a href="%(qwen)s"%(x)s>千问</a>：阿里巴巴的云端助手，系统要求最低。</li>
<li><a href="%(deepseek)s"%(x)s>DeepSeek</a>：DeepSeek 官方 App。</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>：欧洲公司，界面无中文。</li>
</ol>

<h2>一览</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>AI 在哪里运行</th><th>要求</th><th>价格</th><th>评分（中国大陆）</th><th>中文界面</th></tr></thead>
<tbody>
<tr><td>1. <a href="%(pocketpal)s"%(x)s>PocketPal AI</a></td><td>iPhone 本机</td><td>iOS 15.1</td><td>免费</td><td>3.2（89）</td><td>无</td></tr>
<tr><td>2. <a href="%(privatellm)s"%(x)s>Private LLM</a></td><td>iPhone 本机</td><td>iOS 17，A12 仿生及以上</td><td>¥38</td><td>3.4（45）</td><td>无</td></tr>
<tr><td>3. <a href="%(pinku)s">Pinku</a></td><td>iPhone 本机</td><td>iOS 18.6，iPhone 12 及以上</td><td>免费；Pinku Pro 为 App 内购买</td><td>3.2（6）</td><td>有</td></tr>
<tr><td>4. <a href="%(doubao)s"%(x)s>豆包</a></td><td>云端</td><td>iOS 15.0，联网</td><td>免费</td><td>4.7（4,947,221）</td><td>有</td></tr>
<tr><td>5. <a href="%(kimi)s"%(x)s>Kimi</a></td><td>云端</td><td>iOS 15.0，联网</td><td>免费</td><td>4.9（194,948）</td><td>有</td></tr>
<tr><td>6. <a href="%(qwen)s"%(x)s>千问</a></td><td>云端</td><td>iOS 14.0，联网</td><td>免费</td><td>4.3（337,233）</td><td>有</td></tr>
<tr><td>7. <a href="%(deepseek)s"%(x)s>DeepSeek</a></td><td>云端</td><td>iOS 15.0，联网</td><td>免费</td><td>3.9（90,935）</td><td>有</td></tr>
<tr><td>8. <a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>云端</td><td>iOS 16.4，联网</td><td>免费</td><td>4.8（118）</td><td>无</td></tr>
</tbody>
</table></div>

<p class="article-note">要求、价格和评分来自 %(date)s 的中国大陆 App Store 页面；“中文界面”依据 App Store 列出的语言。
Pinku 需要 iPhone 12 是因为它需要 Metal 3，Apple 列出的是 <a href="%(metal)s"%(x)s>iPhone 12 及更新机型</a>。</p>

<h2>本机还是云端？</h2>

<p>在 iPhone 上运行模型，在哪里都能用，对话留在设备上，每条消息不花钱。但能装进手机的模型只有 0.4 到 5 GB，
明显弱于云端模型：事实更容易出错，不能联网搜索，能处理的文本也更短。旧款 iPhone 内存更少，只能运行小模型。
云端 App 更聪明，但每条消息都会发到公司的服务器，没网就不能用。</p>

<h2>1. PocketPal AI</h2>

<p>系统要求最低（iOS 15.1），也是唯一<a href="%(gh)s"%(x)s>开源</a>的。可以加载 Hugging Face 上任何 GGUF 模型：
选择更多，但也更容易选到手机跑不动的模型。免费，隐私标签为“未收集数据”；界面为英文。</p>

<h2>2. Private LLM</h2>

<p>一次性 ¥38，支持家人共享、Siri 和快捷指令，隐私标签为“未收集数据”。支持 iPhone 11 和 SE（第二代）：
需要 A12 仿生芯片或更新。界面为英文。</p>

<h2>3. Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> 通过 Apple MLX 在 iPhone 上运行开源模型（Gemma 3、Llama 3.2、Qwen3 等）。
模型只需下载一次，之后每个回答都在手机上生成，飞行模式也能用。无需账户，聊天只保存在设备上。""" + PINKU_PRIV + """
它只显示内存够用的模型，加载前会检查可用内存。默认模型（Gemma 3 1B）免费；Pinku Pro（App 内购买）增加更大的模型、
自定义指令、听写和朗读。这里唯一有中文界面的离线 App，也能在 Apple 芯片的 Mac 上运行。不足：iPhone 11 和 SE（第二代）
没有 Metal 3，无法运行；代码不开源；不能读取图片和文档；在中国大陆的评分人数还很少（3.2，6 个评分）。</p>

<h2>4. 豆包</h2>

<p>字节跳动的 AI 助手，免费，iOS 15 起，这份列表里评分人数最多（4.7，约 495 万个评分）。
云端服务：你输入的内容会发到其服务器。</p>

<h2>5. Kimi</h2>

<p>月之暗面的助手，免费，iOS 15 起，这份列表里评分最高（4.9，194,948 个评分）。云端。</p>

<h2>6. 千问</h2>

<p>阿里巴巴的助手，免费，iOS 14 即可运行，是这里系统要求最低的云端 App。云端。</p>

<h2>7. DeepSeek</h2>

<p>DeepSeek 官方 App，免费，iOS 15 起，评分 3.9（90,935 个评分）。云端。</p>

<h2>8. Vibe by Mistral</h2>

<p>原名 Le Chat，来自巴黎的 Mistral AI。免费，iOS 16.4 起，界面没有中文。云端。</p>

<p>没有 Apple Intelligence、也没有网络时 iPhone 还能做什么，请看
<a href="%(p_offline)s">Apple Intelligence 能离线使用吗</a>。</p>
""",
    faq=[
        ("iPhone 13、14 或 15 能用 Apple Intelligence 吗？",
         "不能。需要 iPhone 15 Pro、15 Pro Max、iPhone 16 及更新机型或 iPhone Air。在中国大陆购买的设备目前也无法使用。"),
        ("在中国大陆，没有 Apple Intelligence 的 iPhone 用什么 AI App 好？",
         "想离线使用、聊天只留在手机上：Pinku（简体中文界面，iPhone 12 及以上）、PocketPal AI 或 Private LLM。想要最强的回答：豆包、Kimi、千问或 DeepSeek 等云端助手。"),
        ("中国大陆 App Store 有 ChatGPT 吗？",
         "截至 2026 年 10 月 19 日没有。ChatGPT、Gemini、Claude、Locally AI 和 Enclave 都不在中国大陆 App Store 上架。"),
        ("iPhone 12 能离线运行 AI 模型吗？",
         "能，可以运行约 0.4 到 2 GB 的小型开源模型。旧款 iPhone 内存较少，最大的模型不会提供。"),
        ("离线 AI 和云端 AI 一样好吗？",
         "不一样。手机能装下的模型更容易出错，不能联网搜索，能处理的文本也更短。它的优点是隐私、断网可用、每条消息不花钱。"),
    ],
    sources="""
<h2>来源</h2>
<ul>
<li>Apple，<a href="%(ios)s"%(x)s>iOS 27</a> 和<a href="%(reqs)s"%(x)s>如何获取新一代 Apple Intelligence</a>（设备、中国大陆）。</li>
<li>Apple，<a href="%(metal)s"%(x)s>Apple 设备对 Metal 的支持</a>（iPhone 12 起支持 Metal 3）。</li>
<li>中国大陆 App Store 页面（要求、价格、评分、语言）：<a href="%(pinku)s">Pinku</a>、<a href="%(pocketpal)s"%(x)s>PocketPal AI</a>、<a href="%(privatellm)s"%(x)s>Private LLM</a>、<a href="%(doubao)s"%(x)s>豆包</a>、<a href="%(kimi)s"%(x)s>Kimi</a>、<a href="%(qwen)s"%(x)s>千问</a>、<a href="%(deepseek)s"%(x)s>DeepSeek</a>、<a href="%(vibe)s"%(x)s>Vibe by Mistral</a>，查看于 %(date)s；同日用中国大陆 App Store 查询确认 ChatGPT、Gemini、Claude、Locally AI 和 Enclave 未上架。</li>
<li>PocketPal AI 源代码：<a href="%(gh)s"%(x)s>github.com/a-ghorbani/pocketpal-ai</a>。</li>
</ul>
<p>如有过时信息，请<a href="mailto:sagalabs@proton.me">告诉我们</a>。</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
SIRI = dict(
    h1="iPhone 上最好的 Siri AI 替代品（2026）",
    desc=("Siri AI 是只支持英语的测试版，欧盟的 iPhone 不提供，中国大陆也不可用。它能做什么、哪里用不了，"
          "以及每项功能可以用什么代替：豆包、Kimi、千问、DeepSeek、Pinku 等中国大陆 App Store 可下载的 App。"),
    kicker="比较", section="比较",
    standfirst="Apple 的新 Siri 只说英语，而且 Apple 账户地区为中国大陆时无法使用。它能做什么，以及在中国大陆该用什么代替。",
    rank=[("豆包 - 生活工作 AI 助手", CN + "6459478672"), ("Kimi", CN + "6474233312"),
          ("千问 - 阿里AI助手", CN + "6466733523"), ("DeepSeek - AI 智能助手", CN + "6737597349"),
          ("Pinku: Private Offline AI Chat", PINKU_ID), ("PocketPal AI", CN + "6502579498")],
    body="""
<p>关于 Siri AI 的信息来自 Apple 支持页面，各 App 的信息来自中国大陆 App Store，核对于 %(date)s。</p>

<h2>谁能用 Siri AI</h2>

<p><a href="%(siri)s"%(x)s>Siri AI</a> 是基于新一代 Apple Intelligence 的新版 Siri。Apple 给出的限制：</p>

<ul>
<li><strong>需要排队的测试版。</strong>在设置、Siri 中选择 Try Siri AI (Beta) 后等待。</li>
<li><strong>仅英语。</strong>“Siri AI 目前提供英语版本”，设备语言和 Siri 语言必须一致。</li>
<li><strong>中国大陆不可用：</strong>Apple 账户地区为中国大陆时 Siri AI 目前无法使用；在中国大陆购买的设备目前也无法使用 Apple Intelligence。</li>
<li><strong>欧盟的 iPhone 不提供。</strong></li>
<li><strong>只支持新设备：</strong>iPhone 15 Pro 及以上、iPhone 16 及以上、iPhone Air，以及 M1 及以上的 Mac 和 iPad。</li>
</ul>

<h2>Siri AI 能做什么，可以用什么代替</h2>

<div class="table-scroll"><table>
<thead><tr><th>Siri AI 功能（Apple 列表）</th><th>在中国大陆最接近的替代</th></tr></thead>
<tbody>
<tr><td>广泛知识：几乎任何问题都能回答</td><td>豆包、Kimi、千问或 DeepSeek</td></tr>
<tr><td>Write with Siri：随处起草和修改文字</td><td>上述任一 App；Apple 写作工具在中国大陆暂不可用</td></tr>
<tr><td>个人情境：信息、邮件、日历、备忘录</td><td>iPhone 上没有 App 能像 Siri AI 那样读取这些内容</td></tr>
<tr><td>屏幕感知和跨 App 操作</td><td>iPhone 上没有完整替代</td></tr>
<tr><td>通过 iCloud 同步对话记录的 Siri App</td><td>各 App 各自保存记录，云端 App 存在其服务器上</td></tr>
<tr><td>断网可用</td><td>Siri AI 依赖服务器端模型；离线可用 Pinku 或 PocketPal AI</td></tr>
</tbody>
</table></div>

<h2>按需求选择</h2>

<ol>
<li><a href="%(doubao)s"%(x)s>豆包</a>：日常问答，这份列表里评分人数最多。</li>
<li><a href="%(kimi)s"%(x)s>Kimi</a>：这份列表里评分最高。</li>
<li><a href="%(qwen)s"%(x)s>千问</a>：阿里巴巴，系统要求最低。</li>
<li><a href="%(deepseek)s"%(x)s>DeepSeek</a>：DeepSeek 官方 App。</li>
<li><a href="%(pinku)s">Pinku</a>：内容不能离开手机，或者没有网络时。</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>：免费开源的离线聊天。</li>
</ol>

<div class="table-scroll"><table>
<thead><tr><th></th><th>运行位置</th><th>价格</th><th>评分（中国大陆）</th><th>iOS</th></tr></thead>
<tbody>
<tr><td><a href="%(doubao)s"%(x)s>豆包</a></td><td>云端（字节跳动）</td><td>免费</td><td>4.7（4,947,221）</td><td>15.0</td></tr>
<tr><td><a href="%(kimi)s"%(x)s>Kimi</a></td><td>云端（月之暗面）</td><td>免费</td><td>4.9（194,948）</td><td>15.0</td></tr>
<tr><td><a href="%(qwen)s"%(x)s>千问</a></td><td>云端（阿里巴巴）</td><td>免费</td><td>4.3（337,233）</td><td>14.0</td></tr>
<tr><td><a href="%(deepseek)s"%(x)s>DeepSeek</a></td><td>云端</td><td>免费</td><td>3.9（90,935）</td><td>15.0</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a></td><td>iPhone 本机</td><td>免费；Pinku Pro 为 App 内购买</td><td>3.2（6）</td><td>18.6</td></tr>
<tr><td><a href="%(pocketpal)s"%(x)s>PocketPal AI</a></td><td>iPhone 本机</td><td>免费</td><td>3.2（89）</td><td>15.1</td></tr>
</tbody>
</table></div>

<p class="article-note">""" + NOT_IN_CN + """</p>

<h2>豆包、Kimi、千问、DeepSeek</h2>

<p>这四个都是免费的云端助手，有中文界面，最接近“问 Siri 任何问题”。区别主要在评分和公司：豆包（字节跳动）评分人数最多，
Kimi（月之暗面）评分最高，千问（阿里巴巴）iOS 14 就能用，DeepSeek 是 DeepSeek 官方 App。它们都会把你输入的内容发到各自的服务器。</p>

<h2>Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> 不能代替 Siri：它不读取信息、看不到屏幕，也不能操作其他 App。它直接在 iPhone 上用你下载一次的开源模型回答，
对话不会发到任何服务器，飞行模式也能用。无需账户，有简体中文界面。""" + PINKU_PRIV + """
支持 iOS 18.6 的 iPhone 12 及以上机型，有没有 Apple Intelligence 都可以。默认模型免费；Pinku Pro 增加更大的模型、自定义指令、听写和朗读。
手机大小的模型明显弱于上面的云端 App。</p>

<h2>PocketPal AI</h2>

<p>免费、开源的离线聊天，iOS 15.1 及以上，可加载任意 GGUF 模型；界面为英文。</p>

<p>相关文章：<a href="%(p_offline)s">Apple Intelligence 能离线使用吗</a>、
<a href="%(p_noai)s">没有 Apple Intelligence 的 iPhone 适合用哪些 AI App</a>。</p>
""",
    faq=[
        ("Siri AI 支持中文吗？", "目前不支持。Apple 表示 Siri AI 目前提供英语版本。"),
        ("在中国大陆能用 Siri AI 吗？",
         "目前不能。Apple 表示 Apple 账户地区为中国大陆时 Siri AI 无法使用，在中国大陆购买的设备目前也无法使用 Apple Intelligence。"),
        ("在中国大陆，用什么代替 Siri AI？",
         "日常问答可以用中国大陆 App Store 里的豆包、Kimi、千问或 DeepSeek。它们都不会像 Siri AI 那样读取你的信息或在 App 之间操作。想要私密、断网可用的助手，可以用 Pinku 或 PocketPal AI。"),
        ("中国大陆 App Store 有 ChatGPT、Gemini 或 Claude 吗？", "截至 2026 年 10 月 19 日都没有。"),
        ("有没有聊天只保存在 iPhone 上的 AI 助手？",
         "有。Pinku 和 PocketPal AI 在 iPhone 上运行模型，对话不会发送到服务器，但能力弱于云端助手。"),
    ],
    sources="""
<h2>来源</h2>
<ul>
<li>Apple，<a href="%(siri)s"%(x)s>如何获取 Siri AI</a>（测试版、语言、欧盟、中国大陆、功能、设备），发布于 2026 年 9 月 22 日。</li>
<li>Apple，<a href="%(reqs)s"%(x)s>如何获取新一代 Apple Intelligence</a>（中国大陆、语言、设备），发布于 2026 年 9 月 14 日。</li>
<li>中国大陆 App Store 页面：<a href="%(doubao)s"%(x)s>豆包</a>、<a href="%(kimi)s"%(x)s>Kimi</a>、<a href="%(qwen)s"%(x)s>千问</a>、<a href="%(deepseek)s"%(x)s>DeepSeek</a>、<a href="%(pinku)s">Pinku</a>、<a href="%(pocketpal)s"%(x)s>PocketPal AI</a>，查看于 %(date)s。</li>
</ul>
<p>如有过时信息，请<a href="mailto:sagalabs@proton.me">告诉我们</a>。</p>
""" + DISCLOSE,
)

from models_zh import MODELS  # noqa: E402

ARTICLES = {"offline": OFFLINE, "noai": NOAI, "siri": SIRI, "models": MODELS}
