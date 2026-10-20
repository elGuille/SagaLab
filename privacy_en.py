# -*- coding: utf-8 -*-
"""Texto en ingles de los articulos del 20 oct 2026. Ver privacy_oct20.py."""

X = ' target="_blank" rel="noopener"'

DISCLOSE = ("<p>Transparency: Saga Labs, which publishes this site, also makes Pinku. It is described "
            "with the same kind of facts as every other app here: its App Store listing and, in the "
            "network test, what we measured.</p>")

PINKU_PRIV = ("Pinku keeps chats on the device: they never leave it. Apple's privacy label for Pinku lists "
              "only purchase history and an anonymous ID, used for Pinku Pro.")

# --------------------------------------------------------------------------
KEEP = dict(
    h1="What ChatGPT, Claude, Gemini and other AI chatbots keep, and what happens when you delete or export your chats (2026)",
    desc=("How long ChatGPT, Claude, Gemini, Copilot, Perplexity, Grok, DeepSeek, Mistral, Meta AI, Alice, Doubao "
          "and Kimi keep your conversations, what the delete button does, and how to export your data, from each "
          "company's own help pages, checked on 20 October 2026."),
    kicker="Privacy", section="Privacy",
    standfirst=("Deleting a chat removes it from your list at once. What happens on the company's side depends "
                "on the company, the setting and the kind of copy. Here is what each one says, with links."),
    body="""
<h2>The short answer</h2>

<p>Most big chatbots keep your conversations until you delete them or until an
automatic timer runs out. When you delete one, it disappears from your list at
once, and the company says it is erased from its systems within a set window,
usually <strong>30 days</strong>. Every policy below has exceptions: copies kept
for safety reviews, for legal obligations, or because they were already
de-identified or used to train a model. Exporting gives you a copy of your chat
history; it does not tell you what else the company keeps.</p>

<div class="table-scroll"><table>
<thead><tr><th>Service</th><th>Kept by default</th><th>When you delete a chat</th><th>Trains on chats by default?</th><th>Export</th></tr></thead>
<tbody>
<tr><td>ChatGPT (Free, Go, Plus, Pro)</td><td>Until you delete them</td><td>Gone from view at once; deleted within 30 days, with exceptions</td><td>Yes, unless you turn it off</td><td>Settings, Data controls, Export: a ZIP link by email or SMS, up to 7 days, link valid 24 hours</td></tr>
<tr><td>Claude (Free, Pro, Max)</td><td>Until you delete them</td><td>Gone from history at once; from back-end storage within 30 days</td><td>Only if you allow it in Privacy settings</td><td>Settings, Privacy, Export data; link valid 24 hours</td></tr>
<tr><td>Gemini Apps</td><td>Auto-deleted after 18 months (3 or 36 months, or never)</td><td>Removal starts at once; chats a human reviewed stay up to 3 years</td><td>Yes while Keep Activity is on</td><td>Google Takeout; email link active 7 days</td></tr>
<tr><td>Microsoft Copilot</td><td>18 months</td><td>You can delete one chat or all; back-end timing not stated</td><td>Yes; you can opt out at any time</td><td>Not described on the pages we read</td></tr>
<tr><td>Perplexity</td><td>While the account is active</td><td>Threads deletable one by one or all; account data removed within 30 days of deleting the account</td><td>Memory may be used; a setting turns it off</td><td>Not described on the pages we read</td></tr>
<tr><td>Grok</td><td>Not stated as a number</td><td>Deleted within 30 days, unless needed for legal, compliance or safety reasons</td><td>Training is listed among the uses of your content</td><td>Requests through x.ai's privacy portal</td></tr>
<tr><td>DeepSeek</td><td>As long as necessary to provide the service</td><td>You can delete or copy chat history in settings; no timeline given</td><td>Yes; the policy gives a right to opt out</td><td>A right to a portable copy, no button described</td></tr>
<tr><td>Vibe by Mistral (ex Le Chat)</td><td>Until you delete them</td><td>Removed on deletion; account deletion after a short grace period</td><td>Yes, users are not opted out by default</td><td>Not described on the pages we read</td></tr>
<tr><td>Meta AI</td><td>Not stated on the help page we read</td><td>Delete all chats and media in Settings; public vibes are not deleted</td><td>Meta says it uses your interactions with its AIs to improve AI at Meta</td><td>Export your information in Accounts Center</td></tr>
</tbody>
</table></div>

<p class="article-note">From each company's privacy policy and help centre, read on
%(date)s. Links and dates of each page are in the sources at the end. Where a cell
says &ldquo;not described&rdquo;, we looked and did not find it; it does not mean the
feature does not exist.</p>

<h2>ChatGPT (OpenAI)</h2>

<p>OpenAI's retention page, updated the day before we read it, says regular and
archived chats &ldquo;remain saved to your account until you delete them&rdquo;.
When you delete one, ChatGPT removes it from view immediately and OpenAI
&ldquo;schedules it for permanent deletion from its systems within 30 days&rdquo;,
unless the chat was already de-identified and disassociated from your account, or
OpenAI must keep it longer for security or legal obligations. A deleted chat cannot
be restored, not even by support. A temporary chat is not shown in your history,
but OpenAI may keep a copy for up to 30 days for safety purposes. One detail people
miss: deleting a chat does not delete a file saved in your Library.</p>

<p>On training, OpenAI says that for Free, Plus and Pro it &ldquo;may use your
content to train our models&rdquo;. You turn that off with <em>Improve the model for
everyone</em> in Settings, Data controls, or with <em>Do not train on my content</em>
in its Privacy Portal. Even after you opt out, if you press thumbs up or thumbs down
on a reply, &ldquo;the entire conversation associated with that feedback may be used
to train our models&rdquo;.</p>

<p>To export: Settings, Data controls, Export, then Confirm export. The link
arrives by email or SMS, &ldquo;can take up to 7 days&rdquo;, and expires 24 hours
after you receive it. The ZIP holds your chat history and other account data; it
cannot bring back chats you already deleted. The Privacy Portal is the other route
(Make a Privacy Request, Download my data).</p>

<p>Court orders can override all of this. In 2025 a US court ordered OpenAI to
preserve chats users had deleted, in the New York Times copyright case; that order
was later lifted for new chats. The full timeline is in
<a href="%(gdpr)s">our earlier article</a>.</p>

<h2>Claude (Anthropic)</h2>

<p>Anthropic's retention page (dated 1 July 2026) covers Free, Pro and Max. A
deleted conversation is &ldquo;removed from your chat history immediately&rdquo; and
&ldquo;deleted from our back-end storage systems within 30 days&rdquo;. The
exceptions are spelled out with numbers:</p>
<ul>
<li>If you allow your chats to be used to improve Claude, they are kept
&ldquo;in a de-identified format for up to 5 years&rdquo; in training pipelines.</li>
<li>Conversations flagged by its safety systems: inputs and outputs up to 2 years,
and the classification scores up to 7 years.</li>
<li>Feedback you send (thumbs up or down): 5 years.</li>
</ul>
<p>Training only happens if you choose to allow it, with the model improvement
switch in Settings, Privacy. Turning it off stops future use; data already in a
finished training run stays in that model. Incognito chats are not used for
training even if the setting is on. To export: Settings, Privacy, Export data; the
download link expires 24 hours after delivery.</p>

<h2>Gemini (Google)</h2>

<p>Google's Gemini Apps privacy hub (updated 19 October 2026) says your activity is
auto-deleted after <strong>18 months</strong> by default, and you can change that to 3
or 36 months, or turn auto-delete off. With Keep Activity off, and for temporary
chats, conversations are still kept with your account for <strong>72 hours</strong>
and are not used to train Google's models.</p>

<p>The exception that matters most: &ldquo;a subset of chats are reviewed by human
reviewers&rdquo;, and those reviewed chats &ldquo;are not deleted when you delete your
activity&rdquo;; they are kept for up to three years, disconnected from your account.
To export, use Google Takeout and select Gemini and My Activity, Gemini Apps; the
email download link stays active for 7 days.</p>

<h2>Microsoft Copilot</h2>

<p>Microsoft's consumer Copilot FAQ says: &ldquo;By default, we store conversation
activity for 18 months.&rdquo; You can delete single conversations or the whole
history at any time; the pages do not say how long deletion takes on Microsoft's
side. Some conversations go through automated and human review. Microsoft lists
training its models among the uses of your conversations and says you can opt out at
any time, in Privacy, with separate switches for text and voice conversations.</p>

<h2>Perplexity, Grok, DeepSeek, Mistral and Meta AI</h2>

<ul>
<li><strong>Perplexity</strong> keeps personal information &ldquo;as long as your
account is active&rdquo;. If you delete the account, it is removed from its servers
within 30 days, and signing back in before then cancels the deletion. You can
delete threads one by one or all at once; uploaded files are kept for 30 days by
default. Content from Memory may be used to improve its models; Perplexity says you can turn that off.</li>
<li><strong>Grok</strong> (xAI, now SpaceXSI; policy of 11 October 2026): Private
Chat conversations, deleted conversations and deleted accounts are erased
&ldquo;within 30 days unless it is necessary to retain the data for legal,
compliance, or safety purposes&rdquo;. Training the models is one of the listed uses
of your content. Privacy requests go through x.ai's privacy portal.</li>
<li><strong>DeepSeek</strong> (policy of 10 February 2026) keeps personal data
&ldquo;for as long as necessary to provide our Services&rdquo;, uses it to train its
technology, and says it stores data in the People's Republic of China. You can copy
or delete your chat history in settings; deleting the account cannot be undone, and
no deletion timeline is given.</li>
<li><strong>Vibe by Mistral</strong> (formerly Le Chat): conversations &ldquo;are
removed from our systems upon manual deletion&rdquo;, with possible retention for
monitoring and legal purposes. Users &ldquo;are not opted out by default&rdquo; of
training; the switch is <em>Enable data sharing</em> in the app's data settings.</li>
<li><strong>Meta AI</strong>: the help centre explains how to delete all chats and
media (Settings, Data &amp; privacy, Manage your information); public vibes are not
deleted with them. The same page says Meta uses your interactions with its AIs
&ldquo;to improve AI at Meta&rdquo;, and that when its AIs cannot answer, Meta
shares your messages and general information such as your region with select
partners. Your information can be exported from Accounts Center. We did not find a
retention period for chats.</li>
</ul>

<h2>Chatbots popular in Russian and Chinese</h2>

<ul>
<li><strong>Alice (Yandex)</strong>: without the paid option, chat history is kept
for 14 days; with Alice Plus, without a time limit. You delete a chat from the
history, and data by category from Yandex ID's data management page, which warns
that some data is kept longer &ldquo;because the law requires it&rdquo;. Yandex ID
also lets you order an archive of your data.</li>
<li><strong>GigaChat (Sber)</strong>: the user agreement for individuals (6 February
2026) does not give a retention period for conversations.</li>
<li><strong>Doubao (ByteDance)</strong>: keeps personal information only for the
period necessary to provide the service and stores data collected in China inside
China. You can delete single conversations and the account. The policy says it uses
your inputs and replies to improve its models, and a switch in privacy settings
turns that off. It lists rights to view, copy and delete, without an export
button.</li>
<li><strong>Kimi (Moonshot AI)</strong>: stores personal information in China. You
can delete conversations and the account. There is no training switch: you contact
support, and after verifying your identity they stop using your content for
training.</li>
</ul>

<h2>What a formal request got me</h2>

<p>On 15 April 2026 I sent OpenAI and Anthropic a formal GDPR request from my own
consumer accounts, asking under Article 15 for everything they held, including
safety flags and data derived from my chats, and under Article 17 for erasure, with
written confirmation of what was deleted and the legal basis for anything kept.
Anthropic acknowledged it automatically the same day. OpenAI replied on 17 April;
Anthropic's human reply arrived on 16 May, one month and one day later. The GDPR
gives one month to respond (Article 12(3)).</p>

<p>Both replies were polite and pointed to self-service tools. Neither confirmed in
writing what had been deleted, neither gave a legal basis for what was kept, and
neither answered the access request with the data itself. I did not take it to a
data protection authority, so nothing has been decided about it. The full exchange,
quoted, is in <a href="%(gdpr)s">I sent OpenAI and Anthropic a GDPR erasure request</a>.</p>

<h2>How to keep a conversation out of all of this</h2>

<ol>
<li><strong>Before typing</strong>, turn off training (ChatGPT, Copilot, Mistral,
Doubao) or leave it off (Claude). Do not press thumbs up or down on chats you
care about: on ChatGPT, Claude and Mistral, feedback has its own rules.</li>
<li><strong>Use temporary or incognito chats</strong> for sensitive questions, and
remember they are still kept for a while: up to 30 days on ChatGPT and Grok, 72
hours on Gemini.</li>
<li><strong>Delete what you do not need</strong>, and export first if you want a
copy: an export cannot bring back deleted chats.</li>
<li><strong>For conversations that should never reach a server</strong>, use a model
that runs on your own device. On a computer that means tools such as Ollama or LM
Studio; on an iPhone or Mac, apps such as Locally AI, PocketPal AI, Private LLM or
<a href="%(pinku)s">Pinku</a>. %(pinku_priv)s We tested what these apps actually send over the network on a
Mac: <a href="%(p_net)s">the results are here</a>.</li>
</ol>
""",
    faq=[
        ("When I delete a ChatGPT chat, is it really deleted?",
         "It disappears from your account at once, and OpenAI says it schedules it for permanent deletion "
         "within 30 days, unless the chat was already de-identified and disassociated from your account or "
         "OpenAI must keep it longer for security or legal obligations. It cannot be restored."),
        ("How long does Claude keep my chats after I delete them?",
         "Anthropic says a deleted chat leaves your history immediately and its back-end storage within 30 "
         "days. Chats flagged by safety systems are kept up to 2 years (scores up to 7 years), and chats used "
         "for training with your permission up to 5 years, de-identified."),
        ("Does deleting Gemini activity delete chats that a human reviewed?",
         "No. Google says reviewed chats are not deleted when you delete your activity; they are kept for up "
         "to three years, disconnected from your account."),
        ("How do I download my ChatGPT history?",
         "Settings, Data controls, Export, then Confirm export. OpenAI emails or texts a link, which can take "
         "up to 7 days to arrive and expires 24 hours after you receive it."),
        ("Is a temporary or incognito chat stored anywhere?",
         "Yes, for a while. OpenAI may keep temporary chats up to 30 days for safety, Google keeps Gemini chats "
         "72 hours with Keep Activity off, and Grok deletes Private Chat within 30 days unless it must keep it."),
        ("Which AI chat does not store my conversations at all?",
         "None of the cloud chatbots in this list promise that. A model that runs on your own device, such as "
         "Ollama or LM Studio on a computer, or Locally AI, PocketPal AI, Private LLM or Pinku on iPhone or Mac, "
         "keeps the conversation on the device."),
    ],
    sources="""
<h2>Sources</h2>
<ul>
<li>OpenAI Help Center: <a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt"%(x)s>Chat and file retention in ChatGPT</a> (updated 19 October 2026), <a href="https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data"%(x)s>Exporting your ChatGPT history and data</a> and <a href="https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance"%(x)s>How your data is used to improve model performance</a> (both updated 20 October 2026).</li>
<li>Anthropic Privacy Center: <a href="https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data"%(x)s>How long do you store my data?</a> (1 July 2026), <a href="https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training"%(x)s>Is my data used for model training?</a> (16 March 2026); Claude Help Center, <a href="https://support.claude.com/en/articles/9450526-export-your-claude-data"%(x)s>Export your Claude data</a>.</li>
<li>Google: <a href="https://support.google.com/gemini/answer/13594961?hl=en"%(x)s>Gemini Apps Privacy Hub</a> (updated 19 October 2026) and <a href="https://support.google.com/gemini/answer/16920332"%(x)s>export with Google Takeout</a>.</li>
<li>Microsoft: <a href="https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot"%(x)s>Privacy FAQ for Microsoft Copilot</a> and <a href="https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls"%(x)s>Microsoft Copilot privacy controls</a>.</li>
<li>Perplexity Help Center: <a href="https://www.perplexity.ai/help-center/en/articles/10354873-how-long-does-perplexity-retain-my-search-history-profile-data-and-personal-information"%(x)s>retention</a>, <a href="https://www.perplexity.ai/help-center/en/articles/10354879-account-deletion"%(x)s>account deletion</a>, <a href="https://www.perplexity.ai/help-center/en/articles/11564562-self-serve-data-deletion"%(x)s>self-serve data deletion</a>, <a href="https://www.perplexity.ai/help-center/en/articles/10968016-memory"%(x)s>memory</a>.</li>
<li><a href="https://x.ai/legal/privacy-policy"%(x)s>SpaceXSI (xAI) Privacy Policy</a>, last updated 11 October 2026.</li>
<li><a href="https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html"%(x)s>DeepSeek Privacy Policy</a>, last updated 10 February 2026.</li>
<li>Mistral Help Center: <a href="https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr"%(x)s>zero data retention and deletion</a> and <a href="https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training"%(x)s>training opt-out</a> (3 September 2026).</li>
<li>Meta Help Center: <a href="https://www.meta.com/help/artificial-intelligence/2457110494637611/"%(x)s>delete your Meta AI chats</a> and <a href="https://www.meta.com/help/artificial-intelligence/1771195753735844/"%(x)s>export your information</a>.</li>
<li>Yandex: <a href="https://alice.yandex.ru/support/ru/assistant/alice-app"%(x)s>Alice app help</a> and <a href="https://yandex.ru/support/yandex-app-android-alice/ru/privacy/clear-data"%(x)s>deleting your data</a>; Sber: <a href="https://developers.sber.ru/docs/ru/policies/gigachat-agreement/individuals"%(x)s>GigaChat agreement for individuals</a> (6 February 2026).</li>
<li><a href="https://www.doubao.com/legal/privacy"%(x)s>Doubao privacy policy</a> (10 September 2026) and <a href="https://www.kimi.com/user/agreement/userPrivacy?version=v2"%(x)s>Kimi privacy policy</a> (24 August 2026).</li>
<li>GDPR <a href="https://gdpr-info.eu/art-12-gdpr/"%(x)s>Article 12</a>, <a href="https://gdpr-info.eu/art-15-gdpr/"%(x)s>15</a> and <a href="https://gdpr-info.eu/art-17-gdpr/"%(x)s>17</a>.</li>
</ul>
<p>All pages read on %(date)s. Policies change; if one of these is out of date,
<a href="mailto:sagalabs@proton.me">tell us</a> and we will correct the page.</p>
""" + DISCLOSE,
)

# --------------------------------------------------------------------------
NET = dict(
    h1="Do local AI apps send your data to the internet? We watched Ollama, LM Studio and Pinku on a Mac",
    desc=("A network test of three local AI apps on a Mac on 20 October 2026: what Ollama, LM Studio and Pinku "
          "connect to when you open them, download a model, chat and leave them idle, measured with nettop and "
          "macOS logs. Methodology and raw numbers."),
    kicker="Experiment", section="Experiments",
    standfirst=("While chatting, none of the three opened a single connection to the internet. Around the chat "
                "it is different: each one talks to its servers when you open it or download a model, and one "
                "keeps doing so while idle. What we saw, how we measured it, and what we could not see."),
    dataset=dict(
        name="Network connections of Ollama, LM Studio and Pinku on macOS, 20 October 2026",
        description=("Per-process connections (remote address, bytes in and out) recorded with nettop once per "
                     "second while opening, downloading a model, chatting and idling, on macOS 26.7.1."),
        measurementTechnique="nettop (per-process, 1-second samples), lsof, macOS unified log, app caches",
        variableMeasured=["remote host", "bytes received", "bytes sent", "phase"],
    ),
    body="""
<h2>The short answer</h2>

<p><strong>Chatting sent nothing.</strong> In all three apps, typing a question and
getting an answer opened no connection outside the Mac. The internet traffic
happened around the chat:</p>
<ul>
<li><strong>Downloading a model</strong> always goes online, as expected: to
Ollama's registry, to Hugging Face, or, for LM Studio, through LM Studio's own
servers.</li>
<li><strong>Opening the app</strong>: Ollama made no outside connection. LM Studio
fetched about 172 MB of engines on its first launch and about 1 MB on later ones.
Pinku made four small requests to huggingface.co when it loaded a model it already
had.</li>
<li><strong>Idle</strong>: Ollama and Pinku sent nothing in five minutes. LM Studio
opened about 30 connections to its own servers once, a few seconds after a
chat.</li>
</ul>

<h2>Results</h2>

<div class="table-scroll"><table>
<thead><tr><th>App</th><th>Opening</th><th>Downloading a model</th><th>Chatting</th><th>Idle, 5 minutes</th></tr></thead>
<tbody>
<tr><td>Ollama 0.20.2 (Homebrew)</td><td>Nothing outside the Mac; the server listens only on 127.0.0.1</td><td>registry.ollama.ai and Cloudflare storage: 524 MB in, 125 KB out</td><td>Nothing outside the Mac</td><td>Nothing outside the Mac</td></tr>
<tr><td>LM Studio 0.4.26</td><td>First launch: about 172 MB from extensions.lmstudio.ai (engines), without any click. Later launches: about 1 MB from lmstudio.ai</td><td>Through search.lmstudio.ai/v1/hf-proxy: 352 MB in, 84 KB out</td><td>Nothing about the chat itself; with the default command, LM Studio also fetched its model catalogue (about 150 KB in, 12 KB out)</td><td>One burst of about 30 connections to lmstudio.ai addresses, 3 MB in, 31 KB out, then nothing</td></tr>
<tr><td>Pinku for Mac 1.0.7</td><td>No model yet: nothing. With a model installed: 4 requests to huggingface.co, about 35 KB in and 23 KB out</td><td>huggingface.co and Hugging Face's storage on Amazon: about 350 MB for a 0.4 GB model</td><td>Nothing</td><td>Nothing</td></tr>
</tbody>
</table></div>

<p class="article-note">Measured on one Mac on %(date)s. &ldquo;Nothing&rdquo; means
nettop showed no connection from the app's processes to any address outside the
Mac during the whole phase; connections to 127.0.0.1 (the app talking to itself)
are not counted.</p>

<h2>Ollama</h2>

<p>We used the Homebrew build, which runs as a background service. When it starts,
it opens a server on 127.0.0.1:11434 and a helper process that talks to it, both
local. <code>ollama pull qwen3:0.6b</code> went to registry.ollama.ai and then
downloaded 524 MB from Cloudflare storage. <code>ollama run</code> with a question
only talked to the local server, and so did the following five minutes. This
covers the command-line build only: the Ollama app you download from ollama.com
has its own window and updater, which we did not test.</p>

<h2>LM Studio</h2>

<p>On its first launch, before we touched anything, LM Studio downloaded about 172
MB from extensions.lmstudio.ai. Its own download log lists what: the llama.cpp
engine, a Python runtime and a tool called harmony. Later launches fetched about 1
MB from lmstudio.ai addresses.</p>

<p>Model downloads do not go straight to Hugging Face. We asked for
<em>mlx-community/Qwen3-0.6B-4bit</em> and LM Studio's log shows every file coming
from <code>search.lmstudio.ai/v1/hf-proxy/&hellip;</code>, a proxy run by LM
Studio. Its settings file, untouched, had <code>"useHFProxy": true</code>. That
means LM Studio's servers see which models you download. It does not mean they see
your chats.</p>

<p>We could not drive LM Studio's chat window with our tools, so we chatted through
<code>lms chat</code>, LM Studio's own command, which uses the same engine. With
the default command, LM Studio fetched its model catalogue from lmstudio.ai while
answering: about 150 KB down and 12 KB up. With the
<code>--dont-fetch-catalog</code> option, the same kind of question produced no
outside connection at all. During the five idle minutes that followed, LM Studio
opened about 30 connections to lmstudio.ai addresses once, between 45 and 60
seconds in (3 MB down, 31 KB up, under 3 KB up per connection), and nothing after
that. The local server listened only on 127.0.0.1.</p>

<h2>Pinku</h2>

<p>Pinku is an iPhone and Mac app that runs open models on the device. %(pinku_priv)s
The Mac App Store version is 1.0.7. Pinku was not installed on our test Mac, so we
built 1.0.7 from its source and ran it under a separate app identifier, so it
started like a fresh install.</p>

<ul>
<li><strong>First launch, no model</strong>: no connection in 60 seconds.</li>
<li><strong>Downloading the smallest model</strong> (Qwen3 0.6B, 0.4 GB): requests to
huggingface.co for the model's files, and the weights from Hugging Face's storage
on Amazon servers. Our recording started 22 seconds after the download began, so it
caught about 347 MB; the app's network cache lists only huggingface.co
addresses.</li>
<li><strong>Opening with a model installed</strong>: four HTTPS requests to
huggingface.co within seven seconds, about 35 KB down and 23 KB up. The answers
were &ldquo;304 Not Modified&rdquo;: Pinku was checking that the model files on the
Mac were still the current version. The requests name the model, and Hugging Face
sees the Mac's IP address. They contain no chat.</li>
<li><strong>Chatting</strong> (one question, answer in about 85 seconds): no
connection.</li>
<li><strong>Idle, 5 minutes</strong>: no connection.</li>
</ul>

<p>Pinku's App Store description does not mention this check at launch; we
found it in this test. Purchases of
Pinku Pro go through Apple's own system process, which talks to Apple; we could
not attribute that traffic to one app with these tools, so purchases are not part
of the results.</p>

<h2>How we measured</h2>

<ol>
<li>One Mac with Apple silicon, macOS 26.7.1, on Wi-Fi, on 20 October 2026.
No changes to security settings, no administrator password, no new
permissions.</li>
<li><strong>nettop</strong>, the network monitor built into macOS, recorded every
socket of every process once per second, with remote address and bytes in and
out. We kept only the processes of each app.</li>
<li><strong>lsof</strong> to see which ports each app listened on.</li>
<li>Host names: from each app's own records (Pinku's network cache, LM Studio's
download log), from macOS logs and from DNS lookups of the addresses.</li>
<li>Four phases per app: opening (60 to 90 seconds), downloading the smallest
model, one question (<em>Write three short sentences about the sea</em>), and five
minutes idle with the app open.</li>
<li>Afterwards we removed LM Studio, the models we downloaded and our Pinku
build.</li>
</ol>

<h2>What we could not see</h2>

<ul>
<li><strong>Inside the connections.</strong> They are encrypted. Without capturing
packets (which needs an administrator password) we see where data went and how
much, not what it said.</li>
<li><strong>Very short connections</strong> that open and close within one second
can be missed by nettop. For Pinku and LM Studio the apps' own logs and caches
agreed with what nettop showed.</li>
<li><strong>The iPhone.</strong> All of this is on a Mac. Apps on iOS cannot be
inspected this way without other tools.</li>
<li><strong>Longer periods.</strong> Five minutes of idle is not a day. An app that
checks for updates once a day would not show up.</li>
<li><strong>Other apps.</strong> We tested three. Jan, GPT4All, Msty and others were
not part of this test.</li>
</ul>

<h2>How to check an app yourself</h2>

<p>Open Terminal and run <code>nettop -P -L 0 -s 1 -n</code> while you use the app;
each line shows a process and its bytes in and out. For a single app, run
<code>nettop -p</code> followed by its process name. To see where it is listening,
run <code>lsof -nP -iTCP -sTCP:LISTEN</code>. Do it once while you chat and once
while you download a model, and you will see the difference this article is
about.</p>

<p>For what the cloud chatbots keep once your question reaches them, see
<a href="%(p_keep)s">what ChatGPT, Claude, Gemini and others keep, and what deleting
does</a>.</p>
""",
    faq=[
        ("Does Ollama send my chats to the internet?",
         "In our test on a Mac (Ollama 0.20.2 from Homebrew, 20 October 2026), no. Chatting and five minutes idle "
         "produced only local connections on 127.0.0.1. Downloading a model connects to registry.ollama.ai."),
        ("Does LM Studio connect to the internet when I am not downloading anything?",
         "Yes. In our test it downloaded about 172 MB of engines on first launch, about 1 MB on later launches, "
         "fetched its model catalogue when chatting through the lms command, and opened about 30 connections to "
         "its servers once while idle. We saw no connection carrying the chat itself."),
        ("Does LM Studio see which models I download?",
         "With its default settings, yes: downloads from Hugging Face went through search.lmstudio.ai/v1/hf-proxy, "
         "and the settings file had useHFProxy set to true."),
        ("Does Pinku send anything when I chat?",
         "No. Pinku for Mac 1.0.7 made no connection while chatting or idle. It connects to Hugging Face to "
         "download a model, and in version 1.0.7 also when it loads an installed model, to check its files."),
        ("How can I see what an app sends on my Mac?",
         "Run nettop -P -L 0 -s 1 -n in Terminal while you use the app. It lists every process with the bytes it "
         "sends and receives, without an administrator password."),
    ],
    sources="""
<h2>Sources and tools</h2>
<ul>
<li>Apple, nettop and lsof manual pages (<code>man nettop</code>, <code>man lsof</code>) in macOS 26.7.1.</li>
<li><a href="https://ollama.com/"%(x)s>Ollama</a> 0.20.2, installed with Homebrew (<code>brew install ollama</code>).</li>
<li><a href="https://lmstudio.ai/"%(x)s>LM Studio</a> 0.4.26, Homebrew cask that downloads the official installer from lmstudio.ai.</li>
<li><a href="%(pinku)s">Pinku</a> for Mac 1.0.7, built from its source code; App Store privacy label as shown on %(date)s.</li>
<li>Models: <a href="https://ollama.com/library/qwen3"%(x)s>qwen3:0.6b</a> (Ollama) and <a href="https://huggingface.co/mlx-community/Qwen3-0.6B-4bit"%(x)s>mlx-community/Qwen3-0.6B-4bit</a> (LM Studio and Pinku).</li>
</ul>
<p>If you repeat the test and get different results,
<a href="mailto:sagalabs@proton.me">tell us</a>; we will add them.</p>
""" + DISCLOSE,
)

ARTICLES = {"keep": KEEP, "net": NET}
for _a in ARTICLES.values():
    _a["body"] = _a["body"].replace("%(pinku_priv)s", PINKU_PRIV)
