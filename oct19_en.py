# -*- coding: utf-8 -*-
"""Texto en ingles de los articulos del 19 oct 2026. Ver posts_oct19.py."""

PINKU_ID = "https://apps.apple.com/app/id6754878073"
US = "https://apps.apple.com/us/app/id"

PINKU_PRIV = ("Chats never leave your device; Apple's privacy label lists only purchase history and an "
              "anonymous user ID, used for Pinku Pro purchases.")

DISCLOSE = ("<p>Transparency: Saga Labs, which publishes this site, also makes Pinku. Facts about every app, "
            "Pinku included, come from its App Store page.</p>")

# --------------------------------------------------------------------------
OFFLINE = dict(
    h1="Does Apple Intelligence work offline? What works without internet on iPhone (2026)",
    desc=("Apple Intelligence runs some requests on the iPhone and sends others to Apple's servers. What "
          "Apple's own pages say needs a connection, how to see what left your phone, and which AI chat "
          "apps work fully offline."),
    kicker="Guide", section="Guides",
    standfirst=("Partly. Some requests run on the device and heavier ones go to Apple's Private Cloud "
                "Compute servers. What Apple's documentation says, and how to check on your own phone."),
    steps_h="How to check whether a feature ran on your iPhone",
    steps=[
        ("Turn on the report.",
         "Go to Settings, Privacy &amp; Security, Apple Intelligence &amp; PCC Report, and choose a report "
         "duration. On a Mac it is in System Settings, Privacy &amp; Security."),
        ("Use the feature you are unsure about.",
         "Rewrite a paragraph, make an image, ask Siri something: whatever you want to check."),
        ("Export the report and read it.",
         "Apple says the report shows the requests sent off your device and processed by Private Cloud "
         "Compute, and, if you turned on Apple Intelligence Extensions such as ChatGPT, the requests sent "
         "to them. If your request is not there, it was handled on the iPhone."),
        ("Confirm it in airplane mode.",
         "Turn on airplane mode, with Wi-Fi and Bluetooth off, and try the same feature again. If it "
         "still works, it runs on the device."),
    ],
    body="""
<h2>The short answer</h2>

<p>Partly. Apple Intelligence is not one model in one place. Apple's privacy page
says that <a href="%(priv)s"%(x)s>&ldquo;in many cases, Apple Intelligence models run
entirely on device&rdquo;</a>, and that when a task needs more computing power than
the device has, &ldquo;Apple Intelligence may send your request to Private Cloud
Compute&rdquo;, Apple's own servers. Its example is Image Playground: your description
goes to Private Cloud Compute, which makes the image.</p>

<p>Apple also lists the features that <a href="%(reqs)s"%(x)s>&ldquo;rely on
server-side models&rdquo;</a> and therefore have daily usage limits: Siri AI,
Intelligent Photo Editing Tools, Image Playground and the AFM 3 Cloud models in
Shortcuts. Those need a connection. What Apple does not publish is a
feature-by-feature list of what keeps working in airplane mode, so for everything
else you have to check on your own phone (steps below).</p>

<div class="table-scroll"><table>
<thead><tr><th>Feature</th><th>Where Apple says it runs</th><th>Without internet</th></tr></thead>
<tbody>
<tr><td>Siri AI (beta)</td><td>Listed among the features that rely on server-side models; goes to the web for up-to-date answers</td><td>Needs a connection</td></tr>
<tr><td>Image Playground</td><td>Private Cloud Compute (Apple's own example)</td><td>Needs a connection</td></tr>
<tr><td>Intelligent photo editing (Spatial Reframing, Extend, Improved Clean Up)</td><td>Listed among the features with server-side usage limits</td><td>Needs a connection</td></tr>
<tr><td>Shortcuts, Use Model: <em>On-Device</em></td><td>On the iPhone, &ldquo;without the need for a network connection&rdquo;</td><td>Works</td></tr>
<tr><td>Shortcuts, Use Model: <em>Cloud</em> and <em>Cloud Pro</em></td><td>Private Cloud Compute</td><td>Needs a connection</td></tr>
<tr><td>Shortcuts, Use Model: <em>Extension Model</em></td><td>ChatGPT</td><td>Needs a connection</td></tr>
<tr><td>Priority notifications</td><td>An on-device model (Apple's own example)</td><td>Runs on the device</td></tr>
<tr><td>Writing Tools, summaries and the rest</td><td>Apple does not say feature by feature</td><td>Check it yourself</td></tr>
</tbody>
</table></div>

<p class="article-note">Sources: Apple's <a href="%(reqs)s"%(x)s>Apple Intelligence
requirements page</a>, its <a href="%(priv)s"%(x)s>Apple Intelligence privacy
page</a> and the <a href="%(sc)s"%(x)s>Shortcuts user guide</a>, checked on
%(date)s.</p>

<h2>Is Private Cloud Compute private?</h2>

<p>It is designed to be. Apple says the data processed there &ldquo;is not stored or
made accessible to Apple&rdquo; and is used only to fulfil the request, and that the
limited information it does collect (request size, which feature, how long it took)
is not linked to your Apple Account. But it is still a request that leaves your
iPhone and is answered by a server. If you want a conversation that never leaves the
device, or an assistant that works on a plane, a server-side feature cannot give you
that, however well it is protected.</p>

<p>Siri AI adds one more thing to know: Apple says its <a href="%(siri)s"%(x)s>Siri
app &ldquo;uses iCloud to privately sync your conversation history across your
devices&rdquo;</a>.</p>

<h2>Which iPhones get Apple Intelligence at all</h2>

<ul>
<li><strong>iPhone:</strong> iPhone 15 Pro and 15 Pro Max, all iPhone 16 models and
later, and iPhone Air. The iPhone 15, 15 Plus and every older iPhone do not get
it, even though <a href="%(ios)s"%(x)s>iOS 27 runs on iPhone 11 and later</a>.</li>
<li><strong>Storage:</strong> up to 8 GB on the device, and up to 14 GB on iPhone 17
Pro, 17 Pro Max and iPhone Air.</li>
<li><strong>Language:</strong> the device and Siri language must be the same
supported language: English, Danish, Dutch, French, German, Italian, Norwegian,
Portuguese, Spanish, Swedish, Turkish, Vietnamese, Chinese, Japanese or Korean.
Russian, Arabic and Hindi are not on the list. Siri AI itself is English only for
now.</li>
<li><strong>Region:</strong> Apple Intelligence does not currently work on devices
bought in mainland China. In the EU the Apple Intelligence features across apps
are available, but <a href="%(siri)s"%(x)s>Siri AI is not available on iPhone</a>.
See <a href="%(p_siri)s">the Siri AI alternatives</a> for what to use instead.</li>
</ul>

<h2>How to see what left your iPhone</h2>

<p>Apple gives you a log of every request that went to its servers. This is the
most reliable way to answer the question for a specific feature.</p>
%(steps)s
<p>Apple notes that if Face ID or Touch ID are temporarily disabled, the report may
not show recent requests.</p>

<h2>An offline AI that is already on your iPhone: Shortcuts</h2>

<p>If your iPhone has Apple Intelligence, the Shortcuts app gives you a free model
that works without a connection. In a shortcut, add the <em>Use Model</em> action and
choose <em>On-Device</em>, which Apple describes as using &ldquo;the on-device Apple
Intelligence model to handle simple requests without the need for a network
connection&rdquo;. Apple calls it ideal for &ldquo;straightforward requests or simple
conversions&rdquo;: tidying a list, rewriting a sentence, pulling dates out of text.
It is a building block for automations, not a chat window, and the larger
<em>Cloud</em> and <em>Cloud Pro</em> models in the same action do need the
internet.</p>

<h2>If you want a full AI chat that works offline</h2>

<p>These apps download an open model once and then answer on the phone, with no
server involved. They also work on iPhones without Apple Intelligence and in any
language the model understands. The trade-off is the same for all of them: a model
of 1 to 5 GB is much weaker than a cloud model, does not browse the web, and the
first download needs the internet.</p>

<ul>
<li><a href="%(pinku)s">Pinku</a>: iPhone and Mac, no account. Needs iOS 18.6 and a
Metal 3 iPhone, which Apple lists as <a href="%(metal)s"%(x)s>iPhone 12 or
later</a>. The default model is free; larger models, custom instructions, dictation
and read aloud need Pinku Pro, an in-app purchase. """ + PINKU_PRIV + """</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: free, iOS 18.1 or later,
label <em>Data Not Collected</em>.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: free and
<a href="%(gh)s"%(x)s>open source</a>, runs on iOS 15.1 or later, any GGUF model from
Hugging Face.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: $4.99 once, iOS 17 or later with an
A12 Bionic chip or newer, Siri and Shortcuts.</li>
</ul>

<p>For older iPhones, see <a href="%(p_noai)s">the best AI apps for iPhones without
Apple Intelligence</a>.</p>
""",
    faq=[
        ("Does Apple Intelligence work in airplane mode?",
         "Some of it. Apple says many requests run entirely on the device, and the On-Device model in "
         "Shortcuts works without a network connection. Features that rely on server-side models, which "
         "Apple lists as Siri AI, Intelligent Photo Editing Tools, Image Playground and the AFM 3 Cloud "
         "models in Shortcuts, need a connection."),
        ("Does Siri AI work offline?",
         "Expect it to need a connection. Apple lists Siri AI among the features that rely on server-side "
         "models and have daily usage limits, and says it goes out to the web for up-to-date information."),
        ("How can I tell if Apple Intelligence sent my request to a server?",
         "Turn on Settings, Privacy & Security, Apple Intelligence & PCC Report. Apple says it logs the "
         "requests processed by Private Cloud Compute and those sent to extensions such as ChatGPT. You "
         "can export it and look for your request."),
        ("Is Private Cloud Compute the same as the cloud?",
         "It is Apple's own servers. Apple says the data is not stored or made accessible to Apple and is "
         "only used to answer the request, but the request does leave your device."),
        ("Which iPhones have Apple Intelligence?",
         "iPhone 15 Pro, iPhone 15 Pro Max, all iPhone 16 models and later, and iPhone Air. The iPhone 15, "
         "15 Plus and older models do not, even on iOS 27."),
        ("Can I use an AI chat offline on an iPhone without Apple Intelligence?",
         "Yes, with an app that runs an open model on the phone, such as Pinku (iPhone 12 or later), "
         "Locally AI, PocketPal AI or Private LLM. You need the internet once to download the model."),
    ],
    sources="""
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (device and storage requirements, languages, EU and China, server-side features with daily limits), published 14 September 2026.</li>
<li>Apple, <a href="%(siri)s"%(x)s>How to get Siri AI</a> (beta, English only, not on iPhone in the EU, iCloud sync of conversation history), published 22 September 2026.</li>
<li>Apple, <a href="%(priv)s"%(x)s>Apple Intelligence &amp; Privacy</a> (on device or Private Cloud Compute, the Apple Intelligence &amp; PCC Report).</li>
<li>Apple, <a href="%(sc)s"%(x)s>Use Apple Intelligence in Shortcuts on iPhone or iPad</a> (Use Model: On-Device, Cloud, Cloud Pro, Extension Model).</li>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (compatible iPhones) and <a href="%(metal)s"%(x)s>Support for Metal on Apple devices</a> (Metal 3 on iPhone 12 or later).</li>
<li>App Store pages (US) of Pinku, Locally AI, PocketPal AI and Private LLM, as shown on %(date)s.</li>
</ul>
<p>All checked on %(date)s. If anything here is out of date,
<a href="mailto:sagalabs@proton.me">tell us</a> and we will correct the page.</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
NOAI = dict(
    h1="Best AI apps for iPhones without Apple Intelligence (2026)",
    desc=("iOS 27 runs on iPhone 11 and later, Apple Intelligence only on iPhone 15 Pro and newer. Pinku, "
          "Locally AI, PocketPal, Private LLM, ChatGPT, Gemini, Claude and Vibe ranked for the iPhones in "
          "between: offline or cloud, requirements, price and privacy label."),
    kicker="Rankings", section="Rankings",
    standfirst=("Your iPhone runs iOS 27 but has no Apple Intelligence. Eight apps that give it an AI "
                "assistant, on the phone or in the cloud."),
    rank=[("Pinku: Private Offline AI Chat", PINKU_ID), ("Locally AI by LM Studio", US + "6741426692"),
          ("PocketPal AI", US + "6502579498"), ("Private LLM - Local AI Chat", US + "6448106860"),
          ("ChatGPT", US + "6448311069"), ("Google Gemini", US + "6477489729"),
          ("Claude by Anthropic", US + "6473753684"), ("Vibe by Mistral (ex-Le Chat)", US + "6740410176")],
    body="""
<p>Facts about each app come from its App Store page (US), checked on %(date)s.</p>

<p><a href="%(ios)s"%(x)s>iOS 27 runs on iPhone 11 and later</a>, including the
iPhone SE (2nd generation and later). <a href="%(reqs)s"%(x)s>Apple Intelligence
does not</a>: it needs an iPhone 15 Pro, 15 Pro Max, any iPhone 16 or later, or
iPhone Air. So the iPhone 11, 12, 13, 14, 15 and 15 Plus, and the SE, are on the
latest iOS without Writing Tools, Image Playground or Siri AI. These apps fill the
gap in two ways: some run an AI model on the phone itself, offline; the others are
cloud assistants that need the internet but are far more capable.</p>

<h2>The ranking</h2>

<ol>
<li><a href="%(pinku)s">Pinku</a>: offline and private, for iPhone 12 to 15.</li>
<li><a href="%(locally)s"%(x)s>Locally AI by LM Studio</a>: free offline chat.</li>
<li><a href="%(pocketpal)s"%(x)s>PocketPal AI</a>: runs on the oldest iPhones, and its code is public.</li>
<li><a href="%(privatellm)s"%(x)s>Private LLM</a>: pay once, works on iPhone 11 and SE.</li>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: cloud all-rounder.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: if you live in Google's apps.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: long writing and documents.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: the European option.</li>
</ol>

<h2>At a glance</h2>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Where the AI runs</th><th>Needs</th><th>Price (US)</th><th>Rating (US)</th></tr></thead>
<tbody>
<tr><td>1. <a href="%(pinku)s">Pinku</a></td><td>On the iPhone</td><td>iOS 18.6, iPhone 12 or later</td><td>Free; Pinku Pro in-app purchase</td><td>4.7 (12)</td></tr>
<tr><td>2. <a href="%(locally)s"%(x)s>Locally AI</a></td><td>On the iPhone</td><td>iOS 18.1</td><td>Free</td><td>4.7 (1,805)</td></tr>
<tr><td>3. <a href="%(pocketpal)s"%(x)s>PocketPal AI</a></td><td>On the iPhone</td><td>iOS 15.1</td><td>Free; optional paid &ldquo;Pals&rdquo; from $0.99</td><td>4.1 (162)</td></tr>
<tr><td>4. <a href="%(privatellm)s"%(x)s>Private LLM</a></td><td>On the iPhone</td><td>iOS 17, A12 Bionic or later</td><td>$4.99 upfront</td><td>4.2 (736)</td></tr>
<tr><td>5. <a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Cloud</td><td>iOS 18.0, internet</td><td>Free; Go $8, Plus $19.99 a month</td><td>4.8 (11.4 million)</td></tr>
<tr><td>6. <a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Cloud</td><td>iOS 17.4, internet</td><td>Free; Google AI Plus $4.99, Pro $19.99</td><td>4.7 (2.36 million)</td></tr>
<tr><td>7. <a href="%(claude)s"%(x)s>Claude</a></td><td>Cloud</td><td>iOS 18.0, internet</td><td>Free; Pro $20 a month</td><td>4.7 (282,163)</td></tr>
<tr><td>8. <a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Cloud</td><td>iOS 16.4, internet</td><td>Free; Vibe Pro $14.99</td><td>4.8 (1,318)</td></tr>
</tbody>
</table></div>

<p class="article-note">Requirements, in-app purchase prices and ratings as shown on
each app's US App Store page on %(date)s. The iPhone 12 limit for Pinku comes from its
need for Metal 3, which Apple lists on iPhone 12 or later. Not every app is sold in
every country: in Russia and mainland China, for example, ChatGPT, Gemini, Claude and
Locally AI are not in the App Store.</p>

<h2>On the phone or in the cloud?</h2>

<p>An app that runs the model on your iPhone works anywhere, keeps the conversation
on the device and costs nothing per message. But the models that fit in a phone
weigh 0.4 to 5 GB, and they are clearly weaker than ChatGPT, Gemini or Claude: they
make more mistakes on facts, do not browse the web and handle shorter texts. Older
iPhones also have less memory, so they run only the smaller models. The cloud apps
are the opposite: much smarter, but every message goes to the company's servers and
nothing works without a connection. Many people end up with one of each.</p>

<h2>1. Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> runs open models (Gemma 3, Llama 3.2, Qwen3 and
others) on the iPhone with Apple's MLX framework. You download a model once, and
from then on every answer is generated on the phone, in airplane mode too. No
account; chats are saved only on the device. """ + PINKU_PRIV + """ It only lists the
models your iPhone has enough memory for, and checks free memory before loading one.
The default model (Gemma 3 1B) is free; Pinku Pro, an in-app purchase, adds larger
models, custom instructions, dictation and read aloud. Its interface is in eight
languages, Russian and Chinese among them, and it also runs on Macs with Apple
silicon. Limits: it does not run on the iPhone 11 or the SE (2nd generation), which
lack Metal 3; its code is not public; and it reads no images or documents.</p>

<h2>2. Locally AI by LM Studio</h2>

<p>Free, no login, made by the company behind LM Studio for the Mac, with <em>Data
Not Collected</em> on its privacy label and by far the most ratings of the offline
apps here. It also analyses images. It needs iOS 18.1.</p>

<h2>3. PocketPal AI</h2>

<p>The offline app with the lowest requirement here, iOS 15.1, and the only one with
<a href="%(gh)s"%(x)s>public source code</a>. It loads any GGUF model from Hugging
Face, which gives you more choice and more ways to pick a model your iPhone cannot
handle. Free, <em>Data Not Collected</em>; it sells optional character presets
(&ldquo;Pals&rdquo;).</p>

<h2>4. Private LLM</h2>

<p>$4.99 once, with Family Sharing, Siri and Shortcuts, and <em>Data Not
Collected</em>. It is the paid option that supports the iPhone 11 and iPhone SE (2nd
generation): it asks for an A12 Bionic chip or later.</p>

<h2>5. ChatGPT</h2>

<p>The most rated AI app on the App Store by far. Free to start, with paid plans
listed in the app (Go, Plus, Pro). It is the closest thing to a full assistant on an
iPhone without Apple Intelligence, but it is a cloud service that keeps your
conversations on its servers: its privacy label lists contact info, usage data and
user content as data linked to you.</p>

<h2>6. Google Gemini</h2>

<p>Free, works from iOS 17.4, and its paid tiers come bundled with Google storage
(Google AI Plus with 400 GB, Pro with 5 TB). The natural choice if your mail,
calendar and photos are already at Google. Cloud only.</p>

<h2>7. Claude</h2>

<p>From Anthropic. Free to start, Pro at $20 a month. Strong at long writing,
summaries and working through documents. Cloud only, and its privacy label lists
contact info, identifiers and user content as data linked to you.</p>

<h2>8. Vibe by Mistral</h2>

<p>The app formerly called Le Chat, from Mistral AI, based in Paris: the only
European company here. Free, Vibe Pro at $14.99, and the lowest requirement of the
cloud apps (iOS 16.4). Cloud only.</p>

<h2>What about Enclave?</h2>

<p><a href="%(enclave)s"%(x)s>Enclave</a> is another good offline app, with optional
cloud models in its Pro tier, but it now requires iOS 27. If your iPhone is on iOS 27
(iPhone 11 or later), it is worth a look; on iOS 18 or 26 it will not install.</p>

<p>Not sure what your iPhone does without Apple Intelligence? We explained
<a href="%(p_offline)s">what Apple Intelligence does offline and what goes to Apple's
servers</a>.</p>
""",
    faq=[
        ("Can I get Apple Intelligence on an iPhone 13, 14 or 15?",
         "No. Apple Intelligence needs an iPhone 15 Pro, 15 Pro Max, an iPhone 16 or later, or iPhone Air. "
         "The iPhone 15, 15 Plus and older models can update to iOS 27 but do not get Apple Intelligence."),
        ("What is the best AI app for an iPhone without Apple Intelligence?",
         "For an assistant that works offline and keeps chats on the phone, an on-device app such as Pinku "
         "(iPhone 12 or later), Locally AI, PocketPal AI or Private LLM. For the most capable answers, a "
         "cloud app such as ChatGPT, Gemini or Claude, which needs the internet."),
        ("Can an iPhone 12 run an AI model offline?",
         "Yes. Apps like Pinku run small open models (around 0.4 to 2 GB) on an iPhone 12. Older iPhones "
         "have less memory, so the biggest models are not offered on them."),
        ("Do offline AI apps work on the iPhone 11?",
         "Some do. Private LLM supports iPhones with an A12 Bionic chip or later, and PocketPal AI needs "
         "iOS 15.1. Pinku needs Metal 3, which Apple lists on iPhone 12 or later."),
        ("Is an offline AI app as good as ChatGPT?",
         "No. A model small enough for a phone makes more mistakes, does not browse the web and handles "
         "shorter texts. Its advantages are privacy, working with no connection and no cost per message."),
    ],
    sources="""
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(ios)s"%(x)s>iOS 27</a> (compatible iPhones) and <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (devices with Apple Intelligence).</li>
<li>Apple, <a href="%(metal)s"%(x)s>Support for Metal on Apple devices</a> (Metal 3 on iPhone 12 or later).</li>
<li>App Store pages (US), including requirements, in-app purchases, ratings and App Privacy: <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, <a href="%(pocketpal)s"%(x)s>PocketPal AI</a>, <a href="%(privatellm)s"%(x)s>Private LLM</a>, <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(enclave)s"%(x)s>Enclave</a>, as shown on %(date)s. Availability in Russia and China from the App Store lookup for those countries, same day.</li>
<li>PocketPal AI source code: <a href="%(gh)s"%(x)s>github.com/a-ghorbani/pocketpal-ai</a>.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
SIRI = dict(
    h1="Best Siri AI alternatives for iPhone (2026)",
    desc=("Siri AI is a beta, in English only, not on iPhone in the EU and not in mainland China. What it "
          "does, where you cannot get it, and the apps that cover each part: ChatGPT, Gemini, Claude, Vibe "
          "by Mistral, Pinku and Locally AI, plus local options in Russia and China."),
    kicker="Comparisons", section="Comparisons",
    standfirst=("Apple's new Siri is English only, waitlisted, and missing on iPhone in the EU and China. "
                "What it does, and what to use where you cannot get it."),
    rank=[("ChatGPT", US + "6448311069"), ("Google Gemini", US + "6477489729"),
          ("Claude by Anthropic", US + "6473753684"), ("Vibe by Mistral (ex-Le Chat)", US + "6740410176"),
          ("Pinku: Private Offline AI Chat", PINKU_ID), ("Locally AI by LM Studio", US + "6741426692")],
    body="""
<p>What we say about Siri AI comes from Apple's support pages, and about each app from
its App Store page (US unless we say otherwise), checked on %(date)s.</p>

<h2>Who can use Siri AI today</h2>

<p><a href="%(siri)s"%(x)s>Siri AI</a> is the new Siri built on the next generation of
Apple Intelligence. Apple's own page sets the limits:</p>

<ul>
<li><strong>It is a beta with a waitlist.</strong> You turn it on in Settings, Siri,
Try Siri AI (Beta), and wait.</li>
<li><strong>English only.</strong> &ldquo;Siri AI is currently available in
English&rdquo;, and the device and Siri language must match.</li>
<li><strong>Recent devices only:</strong> iPhone 15 Pro and later, iPhone 16 and
later, iPhone Air, Macs and iPads with M1 or later.</li>
<li><strong>Not on iPhone in the EU:</strong> &ldquo;Siri AI is not available for iOS,
iPadOS, or watchOS in the EU.&rdquo; It is on macOS 27 and visionOS 27, in
English.</li>
<li><strong>Not in mainland China:</strong> it &ldquo;will not currently work if your
Apple Account region is in mainland China&rdquo;, and Apple Intelligence as a whole
does not work on devices bought there.</li>
</ul>

<p>In practice that leaves out most iPhone owners in the world: anyone with an older
iPhone, anyone who uses their phone in a language other than English, and everyone
in the EU and China. In Russia there is a second wall: Russian is not one of
<a href="%(reqs)s"%(x)s>the languages Apple Intelligence supports</a> at all.</p>

<h2>What Siri AI does, and what replaces each part</h2>

<div class="table-scroll"><table>
<thead><tr><th>Siri AI feature (Apple's list)</th><th>Closest option on any iPhone</th></tr></thead>
<tbody>
<tr><td>Broad world knowledge: answers to almost any question</td><td>ChatGPT, Gemini, Claude or Vibe by Mistral</td></tr>
<tr><td>Write with Siri: drafts and edits wherever you type</td><td>Apple's Writing Tools on iPhones with Apple Intelligence (Apple lists them for users without Siri AI), or any of the chat apps</td></tr>
<tr><td>Personal context across Messages, Mail, Calendar and Notes</td><td>No app on the iPhone reads all of these the way Siri AI does</td></tr>
<tr><td>Onscreen awareness and app actions</td><td>No full replacement on iPhone</td></tr>
<tr><td>Siri app with conversation history synced by iCloud</td><td>Each chat app keeps its own history, most of them on their servers</td></tr>
<tr><td>Works without a connection</td><td>Siri AI relies on server-side models; offline, Pinku or Locally AI</td></tr>
</tbody>
</table></div>

<h2>The options, by what you need</h2>

<ol>
<li><a href="%(chatgpt)s"%(x)s>ChatGPT</a>: general replacement for asking anything.</li>
<li><a href="%(gemini)s"%(x)s>Google Gemini</a>: if your mail and calendar are at Google.</li>
<li><a href="%(claude)s"%(x)s>Claude</a>: writing and long documents.</li>
<li><a href="%(vibe)s"%(x)s>Vibe by Mistral</a>: a European company.</li>
<li><a href="%(pinku)s">Pinku</a>: nothing may leave the phone, or there is no connection.</li>
<li><a href="%(locally)s"%(x)s>Locally AI</a>: free offline chat.</li>
</ol>

<div class="table-scroll"><table>
<thead><tr><th></th><th>Where it runs</th><th>Price (US)</th><th>Rating (US)</th><th>Privacy label</th></tr></thead>
<tbody>
<tr><td><a href="%(chatgpt)s"%(x)s>ChatGPT</a></td><td>Cloud (OpenAI, US)</td><td>Free; Go $8, Plus $19.99 a month</td><td>4.8 (11.4 million)</td><td>Data linked to you, incl. contact info and user content</td></tr>
<tr><td><a href="%(gemini)s"%(x)s>Google Gemini</a></td><td>Cloud (Google, US)</td><td>Free; Google AI Plus $4.99, Pro $19.99</td><td>4.7 (2.36 million)</td><td>Data linked to you, incl. location, contact info and identifiers</td></tr>
<tr><td><a href="%(claude)s"%(x)s>Claude</a></td><td>Cloud (Anthropic, US)</td><td>Free; Pro $20 a month</td><td>4.7 (282,163)</td><td>Data linked to you, incl. contact info and user content</td></tr>
<tr><td><a href="%(vibe)s"%(x)s>Vibe by Mistral</a></td><td>Cloud (Mistral AI, France)</td><td>Free; Vibe Pro $14.99</td><td>4.8 (1,318)</td><td>Contact info linked to you; usage and user content not linked</td></tr>
<tr><td><a href="%(pinku)s">Pinku</a></td><td>On the iPhone</td><td>Free; Pinku Pro in-app purchase</td><td>4.7 (12)</td><td>Purchase history and an anonymous user ID (for Pro); chats stay on the device</td></tr>
<tr><td><a href="%(locally)s"%(x)s>Locally AI</a></td><td>On the iPhone</td><td>Free</td><td>4.7 (1,805)</td><td>Data Not Collected</td></tr>
</tbody>
</table></div>

<p class="article-note">Prices and ratings from each app's US App Store page on
%(date)s. Privacy labels are what each developer declares to Apple; Apple does not
verify them.</p>

<h2>ChatGPT</h2>

<p>The most rated AI app on the App Store, and the most direct replacement for
&ldquo;ask Siri anything&rdquo;. Free to start, with Go, Plus and Pro plans in the app.
A cloud service: its privacy label lists contact info, usage data and user content
as linked to you.</p>

<h2>Google Gemini</h2>

<p>Free, from iOS 17.4, with paid tiers bundled with Google storage. If your mail,
calendar and photos are at Google, it is the closest thing to the personal context
Siri AI promises, inside Google's apps. Cloud only.</p>

<h2>Claude</h2>

<p>From Anthropic. Free to start, Pro at $20 a month. The best of these for writing,
editing and working through long documents. Cloud only.</p>

<h2>Vibe by Mistral</h2>

<p>Formerly Le Chat, made by Mistral AI in Paris. Its privacy label separates contact
info, which is linked to you, from usage data and user content, which it declares as
not linked. Free, Vibe Pro at $14.99, iOS 16.4 or later. It is also sold in Russia
and mainland China.</p>

<h2>Pinku</h2>

<p><a href="%(pinku)s">Pinku</a> does not replace Siri: it cannot read your
messages, see your screen or act in other apps. It answers on the iPhone itself, with
an open model you download once, so the conversation goes to no server and it works
in airplane mode. No account. """ + PINKU_PRIV + """ Its interface is in eight
languages, including Russian, Chinese, Japanese and Korean, and it runs on any iPhone
12 or later with iOS 18.6, with or without Apple Intelligence. The default model is
free; Pinku Pro, an in-app purchase, adds larger models, custom instructions,
dictation and read aloud. A phone-sized model is much weaker than the cloud apps
above.</p>

<h2>Locally AI by LM Studio</h2>

<p>Free private offline chat: no login, <em>Data Not Collected</em>, iOS 18.1 or
later, and it can also look at images. It is not sold in Russia or mainland China.</p>

<h2>If you are in the EU</h2>

<p>Everything above is available in the EU App Store. On an iPhone 15 Pro or later you
keep the rest of Apple Intelligence: Apple says the new features across apps
(advanced photo editing, the reimagined Image Playground, Safari's intelligent
features) are available to EU users on iOS 27. On a Mac with macOS 27 Golden Gate,
Siri AI is available in the EU if your device and Siri language are English.</p>

<h2>If you are in Russia</h2>

<p>On 19 October 2026 the Russian App Store does not sell ChatGPT, Gemini, Claude or
Locally AI. What it does have: <a href="https://apps.apple.com/ru/app/id%(alice_id)s"%(x)s>Alice
AI</a> from Yandex (free, 4.8 from 53,071 ratings), <a href="https://apps.apple.com/ru/app/id%(deepseek_id)s"%(x)s>DeepSeek</a>
(free, 3.9 from 9,770), <a href="https://apps.apple.com/ru/app/id%(perplexity_id)s"%(x)s>Perplexity</a>
(free, 4.9 from 37,853) and Vibe by Mistral in the cloud; Pinku, PocketPal AI, Private
LLM and Enclave offline. Of the offline apps, only Pinku has a Russian interface.</p>

<h2>If you are in mainland China</h2>

<p>Apple Intelligence does not work on iPhones bought in mainland China, and the
Chinese App Store does not sell ChatGPT, Gemini, Claude, Locally AI or Enclave. The
big local assistants are <a href="https://apps.apple.com/cn/app/id%(doubao_id)s"%(x)s>Doubao</a>
(ByteDance), <a href="https://apps.apple.com/cn/app/id%(deepseek_id)s"%(x)s>DeepSeek</a>,
<a href="https://apps.apple.com/cn/app/id%(kimi_id)s"%(x)s>Kimi</a> and
<a href="https://apps.apple.com/cn/app/id%(qwen_id)s"%(x)s>Qwen</a> (Alibaba), all free
and all in the cloud. Offline, Pinku (with a Chinese interface), PocketPal AI and
Private LLM are sold there.</p>

<p>Related: <a href="%(p_offline)s">what Apple Intelligence does offline</a> and
<a href="%(p_noai)s">the best AI apps for iPhones without Apple Intelligence</a>.</p>
""",
    faq=[
        ("Is Siri AI available everywhere?",
         "No. Apple says Siri AI is a beta, currently available in English only, not available on iPhone, "
         "iPad or Apple Watch in the EU, and not working for Apple Accounts in mainland China."),
        ("Is Siri AI available in the EU?",
         "Not on iPhone. It is available on macOS 27 and visionOS 27 for EU accounts with the device and "
         "Siri language set to English. The other new Apple Intelligence features are available in the EU."),
        ("Does Siri AI work in Russian or Chinese?",
         "Not yet. Apple says Siri AI is currently available in English. Russian is not among the languages "
         "Apple Intelligence supports at all; Chinese is, but Apple Intelligence does not work in mainland "
         "China."),
        ("What is the best Siri AI alternative on iPhone?",
         "For asking anything, ChatGPT, Gemini or Claude; Vibe by Mistral for a European company. None of "
         "them reads your messages and acts across apps the way Siri AI does. For a private assistant that "
         "works offline, Pinku or Locally AI."),
        ("Is there an AI assistant that keeps my chats on my iPhone?",
         "Yes. On-device apps such as Pinku and Locally AI run the model on the iPhone, so the conversation "
         "is not sent to a server. They are less capable than cloud assistants."),
    ],
    sources="""
<h2>Sources</h2>
<ul>
<li>Apple, <a href="%(siri)s"%(x)s>How to get Siri AI</a> (beta, languages, EU, China, features, requirements), published 22 September 2026.</li>
<li>Apple, <a href="%(reqs)s"%(x)s>How to get the next generation of Apple Intelligence</a> (supported languages, features available in the EU, China, devices), published 14 September 2026.</li>
<li>App Store pages (US), including prices, ratings and App Privacy: <a href="%(chatgpt)s"%(x)s>ChatGPT</a>, <a href="%(gemini)s"%(x)s>Google Gemini</a>, <a href="%(claude)s"%(x)s>Claude</a>, <a href="%(vibe)s"%(x)s>Vibe by Mistral</a>, <a href="%(pinku)s">Pinku</a>, <a href="%(locally)s"%(x)s>Locally AI</a>, as shown on %(date)s. Russian and Chinese availability, prices and ratings from the App Store in those countries, same day.</li>
</ul>
<p>If anything here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a>
and we will correct the page.</p>
""" + DISCLOSE,
)

ARTICLES = {"offline": OFFLINE, "noai": NOAI, "siri": SIRI}
