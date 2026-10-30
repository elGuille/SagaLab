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
    h1="Are deleted AI chats really deleted? What ChatGPT, Claude, Gemini and other chatbots keep (2026)",
    desc=("What happens when you delete a chat in ChatGPT, Claude, Gemini, Copilot, Perplexity, Grok, DeepSeek, "
          "Mistral or Meta AI: what leaves your screen, what is erased from the servers and when, what is kept for "
          "training or safety, and what a court order kept anyway. From each company's own pages, checked on "
          "30 October 2026."),
    kicker="Privacy", section="Privacy",
    standfirst=("Deleting a chat removes it from your list at once. On the company's side, a copy can stay for 30 "
                "days, for years if it was reviewed or used for training, or for as long as a court says. Here is "
                "what each one says, with links."),
    body="""
<h2>The short answer</h2>

<p>Not right away, and not always. When you delete a chat, every service below
removes it from your list at once. Most then say they erase it from their
servers within <strong>30 days</strong>. Three kinds of copy can outlive that:
chats kept <strong>for training</strong> (up to 5 years at Anthropic if you allowed
it), chats kept <strong>for safety review</strong> (up to 3 years at Google when a
human read them, 2 years at Anthropic when flagged), and chats kept <strong>because a
court ordered it</strong>: from May to September 2025, OpenAI had to keep deleted
ChatGPT chats for a copyright case, and it still holds what it saved then.</p>

<h2>Deleted from your screen is not deleted from the servers</h2>

<div class="table-scroll"><table>
<thead><tr><th>Service</th><th>Leaves your screen</th><th>Erased from the servers</th><th>Kept for training or safety</th><th>Kept for courts or the law</th></tr></thead>
<tbody>
<tr><td>ChatGPT</td><td>At once; cannot be restored, not even by support</td><td>Within 30 days, unless already de-identified</td><td>Trains on Free, Plus and Pro chats unless you turn it off; temporary chats kept up to 30 days for safety</td><td>Court order of May 2025 kept deleted chats until 26 September 2025; OpenAI keeps what it saved then</td></tr>
<tr><td>Claude</td><td>At once</td><td>Within 30 days</td><td>Only if you allow training: up to 5 years, de-identified; flagged chats 2 years, their safety scores 7 years; feedback 5 years</td><td>Not stated on the pages we read</td></tr>
<tr><td>Gemini</td><td>When you delete the activity</td><td>Auto-deleted after 18 months by default (3 or 36, or never); 72 hours with Keep Activity off</td><td>Chats a human reviewed are not deleted with your activity: up to 3 years, disconnected from your account</td><td>Not stated on the pages we read</td></tr>
<tr><td>Microsoft Copilot</td><td>One chat or all, at any time</td><td>Older app: stored 18 months by default. The new app's privacy page gives no period</td><td>Trains on conversations unless you opt out; some get automated and human review</td><td>Not stated on the pages we read</td></tr>
<tr><td>Perplexity</td><td>One thread or all</td><td>Account data within 30 days of deleting the account; files after 30 days</td><td>Memory may be used to improve models unless you turn off AI Data Retention</td><td>Not stated on the pages we read</td></tr>
<tr><td>Grok</td><td>One chat or all</td><td>Within 30 days</td><td>Training is one of the listed uses</td><td>Longer &ldquo;for legal, compliance, or safety purposes&rdquo;</td></tr>
<tr><td>DeepSeek</td><td>Delete history in settings</td><td>&ldquo;As long as necessary&rdquo;; no timeline</td><td>Used for training; the policy gives a right to object</td><td>Stored on servers in the People's Republic of China</td></tr>
<tr><td>Vibe by Mistral</td><td>On deletion</td><td>&ldquo;Upon manual deletion&rdquo;; account after a short grace period</td><td>Users are not opted out of training by default</td><td>&ldquo;Monitoring and legal retention purposes&rdquo;</td></tr>
<tr><td>Meta AI</td><td>Delete all chats and media; public vibes stay</td><td>No period on the help pages we read</td><td>Interactions are used &ldquo;to improve AI at Meta&rdquo;</td><td>Not stated on the pages we read</td></tr>
</tbody>
</table></div>

<p class="article-note">From each company's privacy policy and help centre, read on
%(date)s. Links and the date of each page are in the sources at the end. &ldquo;Not
stated&rdquo; means we looked and did not find it on those pages, not that the company
never keeps anything for those reasons.</p>

<h2>ChatGPT (OpenAI)</h2>

<p>OpenAI's retention page (updated 29 October 2026) says regular and archived
chats &ldquo;remain saved to your account until you delete them&rdquo; or a
workspace retention policy removes them. When you delete one, ChatGPT removes it
from view immediately and OpenAI &ldquo;schedules it for permanent deletion from its
systems within 30 days&rdquo;, unless the chat was already de-identified and
disassociated from your account, or OpenAI must keep it longer for security or legal
obligations. You cannot restore a deleted chat, &ldquo;in ChatGPT or through OpenAI
Support&rdquo;. A temporary chat is not shown in your history, but OpenAI &ldquo;may
keep a copy for up to 30 days for safety purposes&rdquo;. Deleting a chat does not
delete a file you saved separately in Library or a Space.</p>

<p>On training, OpenAI says that for Free, Plus and Pro it &ldquo;may use your
content to train our models&rdquo;. Even after you opt out, if you press thumbs up or
down, &ldquo;the entire conversation associated with that feedback may be used to
train our models&rdquo;.</p>

<p><strong>Settings:</strong> turn training off in Settings, Data controls,
<em>Improve the model for everyone</em> (or <em>Do not train on my content</em> in
the Privacy Portal). Start a temporary chat by opening a new chat and selecting
<em>Temporary</em>. Delete one chat from its &bull;&bull;&bull; menu, Delete; delete
all in Settings, Data controls, <em>Delete all chats</em>. Export in Settings, Data
controls, Export: the link can take up to 7 days and expires 24 hours after you get
it, and an export cannot bring back chats you already deleted.</p>

<h2>Claude (Anthropic)</h2>

<p>Anthropic's retention page (1 July 2026) covers Free, Pro and Max. A deleted
conversation is &ldquo;removed from your chat history immediately&rdquo; and
&ldquo;deleted from our back-end storage systems within 30 days&rdquo;. The
exceptions come with numbers:</p>
<ul>
<li>If you allow your chats to be used to improve Claude, they are kept &ldquo;in a
de-identified format for up to 5 years&rdquo; in training pipelines, and data already
in a finished or running training run stays there.</li>
<li>Conversations flagged by its safety systems: inputs and outputs up to 2 years,
and the classification scores up to 7 years.</li>
<li>Feedback you send (thumbs up or down): 5 years.</li>
<li>Incognito chats are not saved to your history and not used for training, but they
are kept for 30 days by default.</li>
</ul>
<p><strong>Settings:</strong> training only happens if you switch on <em>Help improve
our AI models</em> in Settings, Privacy. Start an incognito chat with the ghost icon
at the top right. Delete a chat from its &#8942; menu, or tick several and use
<em>Select all</em>. Export from Settings, Privacy on the web or desktop app (not
from the iPhone or Android app); the link expires 24 hours after delivery.</p>

<h2>Gemini (Google)</h2>

<p>Google's Gemini Apps privacy hub (updated 26 October 2026) says your activity is
auto-deleted after <strong>18 months</strong> by default, and you can change that to 3
or 36 months, or turn auto-delete off. Temporary chats, and chats with Keep Activity
off, are still kept with your account for <strong>72 hours</strong>, and temporary
chats are not used to train Google's models.</p>

<p>The exception that matters most: &ldquo;a subset of chats are reviewed by human
reviewers&rdquo;, and those chats &ldquo;are not deleted when you delete your
activity&rdquo;; they are kept for up to three years, disconnected from your
account.</p>

<p><strong>Settings:</strong> in Settings &amp; help, Activity, choose <em>Turn
off</em> or <em>Turn off and delete activity</em>. Start a temporary chat with
<em>Temporary chat</em> next to New chat. Delete one item with <em>Delete activity
item</em>, or everything with Delete, <em>All time</em>. Export with Google Takeout
(My Activity, Gemini Apps); the email link stays active for 7 days.</p>

<h2>Microsoft Copilot</h2>

<p>Microsoft's consumer Copilot privacy FAQ says: &ldquo;By default, we store
conversation activity for 18 months. You can delete individual conversations or your
entire conversation history at any time.&rdquo; Since we first read it, Microsoft has
added a line saying that the article &ldquo;applies only to the older version of the
Microsoft Copilot app&rdquo;. The privacy page for the new app does not give a
retention period, so we cannot tell you how long the new app keeps chats. Some
conversations go through automated and human review, and you &ldquo;can opt out of use
of your conversation activity for model training at any time&rdquo;.</p>

<p><strong>Settings (older app):</strong> Privacy, <em>Training on conversation
activity</em> and <em>Training on voice conversations</em>. Delete one conversation
from the three dots next to it, or all of them with <em>Delete all activity
history</em>. We did not find a temporary chat mode on Microsoft's pages.</p>

<h2>Perplexity, Grok, DeepSeek, Mistral and Meta AI</h2>

<ul>
<li><strong>Perplexity</strong> keeps personal information &ldquo;as long as your
account is active&rdquo;. If you delete the account, it is removed from its servers
within 30 days, and signing back in before then cancels the deletion. You can delete
threads one by one or all at once (the &hellip; next to the threads tab, <em>Delete
sessions</em>); uploaded files are kept for 30 days by default. Content from Memory
may be used to improve its models unless you turn off <em>AI Data Retention</em> in
Settings, Preferences, Artificial Intelligence, and a log of cleared memories may be
kept for up to 30 days.</li>
<li><strong>Grok</strong> (xAI, now SpaceXSI; policy of 27 October 2026): Private
Chat conversations, deleted conversations and deleted accounts are erased within 30
days &ldquo;unless it is necessary to retain the data for legal, compliance, or safety
purposes&rdquo;. Training is one of the listed uses of your content. Its FAQ gives the
switches: Settings, Data Controls, <em>Improve the model</em>; the ghost icon at the top
right for a Private Chat; and Settings, Data Controls, <em>Delete All
Conversations</em>.</li>
<li><strong>DeepSeek</strong> (policy of 10 February 2026) keeps personal data for as
long as necessary, uses it to train and improve its technology, gives a right to object
to that, and stores data on servers in the People's Republic of China. You can delete
your chat history in settings; deleting the account cannot be undone, and no deletion
timeline is given. DeepSeek has no help pages with the steps.</li>
<li><strong>Vibe by Mistral</strong> (formerly Le Chat): conversations &ldquo;are
removed from our systems upon manual deletion&rdquo; or when you delete your account,
typically after a short grace period, with retention for monitoring and legal purposes.
Users &ldquo;are not opted out by default&rdquo; of training: on the phone the switch
is <em>Enable data sharing</em>; on the web, <em>Allow your interactions to be used to
train our models</em>.</li>
<li><strong>Meta AI</strong>: Settings, Data &amp; privacy, Manage your information,
<em>Delete all chats and media</em>; public vibes are not deleted with them. The same
page says Meta uses your interactions with its AIs &ldquo;to improve AI at Meta&rdquo;,
and that when its AIs cannot answer, Meta shares your messages and general information
such as your region with select partners. You can export your information from
Accounts Center. We did not find a retention period for chats.</li>
</ul>

<h2>Four times chats were kept or exposed anyway</h2>

<h3>A court ordered OpenAI to keep deleted chats (2025)</h3>
<p>In the New York Times copyright case, Magistrate Judge Ona Wang ordered OpenAI on
13 May 2025 to &ldquo;preserve and segregate all output log data that would otherwise be
deleted&rdquo;, &ldquo;whether such data might be deleted at a user's request&rdquo; or
because of privacy laws. OpenAI says this covered ChatGPT Free, Plus, Pro and Team and
the API without a zero data retention agreement, not Enterprise or Edu. A stipulated
order of 9 October 2025 ended the obligation &ldquo;as of September 26, 2025&rdquo;.
OpenAI keeps what it had already saved, except data from the European Economic Area,
Switzerland and the United Kingdom, and keeps preserving chats from accounts linked to
the domains the newspapers listed. OpenAI's own page says it &ldquo;will securely store
limited historical April&ndash;September 2025 user data&rdquo;. The case is still
open; we found no change to the preservation terms since.</p>

<h3>Italy limited ChatGPT and fined OpenAI (2023 and 2024)</h3>
<p>On 30 March 2023, Italy's data protection authority, the Garante, ordered an
immediate temporary limitation of ChatGPT's processing of data of people in Italy, and
on 11 April set the conditions for lifting it, to be met by 30 April 2023. On 20 December 2024 it fined
OpenAI fifteen million euros, for reasons that included not reporting the March 2023
breach, training without a legal basis, a lack of transparency and no age checks. The
Garante's page now says that, after the Court of Rome upheld OpenAI's appeal in a
judgment published on 18 March 2026, the decision has been temporarily taken off its
website.</p>

<h3>A ChatGPT bug showed other people's chat titles (March 2023)</h3>
<p>OpenAI wrote that a bug &ldquo;allowed some users to see titles from another active
user's chat history&rdquo;, and exposed payment-related information of 1.2%% of ChatGPT
Plus subscribers active during a nine-hour window; full card numbers were not
exposed.</p>

<h3>A DeepSeek database was open to the internet (January 2025)</h3>
<p>Wiz Research found a DeepSeek database reachable without a password, with
&ldquo;over a million lines of log streams containing chat history, secret keys, backend
details&rdquo;; DeepSeek closed it promptly after being told. The next day, 30 January
2025, the Garante ordered an urgent limitation of DeepSeek's processing of data of users
in Italy.</p>

<h2>Never paste passwords, API keys or card numbers</h2>

<p>The companies say it themselves. OpenAI: &ldquo;Please don't share any sensitive
information in your conversations.&rdquo; Google: &ldquo;Please don't enter confidential
information that you wouldn't want a reviewer to see or Google to use to improve our
services&rdquo;, and &ldquo;Don't enter login or payment information into Gemini
chats&rdquo;. Microsoft: you &ldquo;shouldn't provide any confidential or sensitive
personal data&rdquo;. xAI: &ldquo;please do not share any personal or sensitive
information in your questions to Grok.&rdquo; The UK's National Cyber Security Centre
recommends &ldquo;not to include sensitive information in queries to public
LLMs&rdquo;.</p>

<p>The reasons are in the sections above: a deleted chat can stay up to 30 days, a
reviewed one up to three years, a court can freeze deletion, and a leak exposes
whatever is in the logs. If you have already pasted a password or a key into a chatbot,
deleting the chat is not enough: change the password or revoke the key.</p>

<h2>Chatbots popular in Russian and Chinese</h2>

<ul>
<li><strong>Alice (Yandex)</strong>: without the paid option, chat history is kept
for 14 days; with Alice Plus, without a time limit. You delete a chat from the
history, and data by category from Yandex ID's data management page, which warns
that some data is kept longer &ldquo;because the law requires it&rdquo;. Yandex ID
also lets you order an archive of your data.</li>
<li><strong>GigaChat (Sber)</strong>: the agreement we read (6 February 2026) does not
give a retention period for conversations.</li>
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
<li><strong>Before typing</strong>, turn off training (ChatGPT, Copilot, Grok,
Mistral, Perplexity's Memory, Doubao) or leave it off (Claude). Do not press thumbs
up or down on chats you care about: on ChatGPT, Claude and Mistral, feedback has its
own rules.</li>
<li><strong>Use temporary or incognito chats</strong> for sensitive questions, and
remember they are still kept for a while: up to 30 days on ChatGPT, Claude and Grok,
72 hours on Gemini.</li>
<li><strong>Delete what you do not need</strong>, and export first if you want a
copy: an export cannot bring back deleted chats.</li>
<li><strong>Keep secrets out of every chat</strong>: passwords, API keys, card and ID
numbers.</li>
</ol>

<h2>When a model on your own device makes sense</h2>

<p>None of the cloud chatbots above promise to keep nothing: deletion takes time,
there are exceptions, and a court or a leak can override both. A model that runs on
your own device avoids that for the conversations where it matters (health, money,
work documents, anything you would not want a reviewer to read), because the text never
reaches a server. The trade-off is a smaller model: it knows less, makes more mistakes
and cannot search the web, so it suits private drafting, summaries and questions, not
research.</p>

<p>On a computer, tools such as Ollama or LM Studio run open models; on an iPhone or
Mac, apps such as Locally AI, PocketPal AI and Private LLM do, and so does
<a href="%(pinku)s">Pinku</a>, which we make. %(pinku_priv)s We tested what these
apps actually send over the network on a Mac (<a href="%(p_net)s">results</a>), and
how fast small models run on an iPhone (<a href="%(speed)s">speeds</a>).</p>
""",
    faq=[
        ("Are deleted ChatGPT chats really deleted?",
         "They disappear from your account at once and cannot be restored. OpenAI says it deletes them from its "
         "systems within 30 days, unless they were already de-identified or it must keep them for security or legal "
         "obligations. Deleted chats saved under the court order of May to September 2025 are still kept."),
        ("Does OpenAI still have to keep my deleted ChatGPT chats?",
         "Not new ones. The obligation ended on 26 September 2025. OpenAI keeps what it had saved before that date, "
         "except data from the European Economic Area, Switzerland and the United Kingdom, and keeps preserving chats "
         "of accounts linked to domains the New York Times listed."),
        ("How long does Claude keep my chats after I delete them?",
         "Anthropic says a deleted chat leaves your history immediately and its back-end storage within 30 days. "
         "Chats flagged by safety systems are kept up to 2 years (scores up to 7 years), and chats used for training "
         "with your permission up to 5 years, de-identified."),
        ("Does deleting Gemini activity delete chats that a human reviewed?",
         "No. Google says reviewed chats are not deleted when you delete your activity; they are kept for up to three "
         "years, disconnected from your account."),
        ("Is a temporary or incognito chat stored anywhere?",
         "Yes, for a while: up to 30 days on ChatGPT and Grok, 30 days by default on Claude, and 72 hours on Gemini."),
        ("Is it safe to paste a password or API key into ChatGPT?",
         "No. OpenAI, Google, Microsoft and xAI all ask you not to share sensitive information, and deleted chats can "
         "stay on their servers for weeks or longer. If you already did, change the password or revoke the key."),
        ("Which AI chat does not store my conversations at all?",
         "None of the cloud chatbots in this list promise that. A model that runs on your own device, such as Ollama "
         "or LM Studio on a computer, or Locally AI, PocketPal AI, Private LLM or Pinku on iPhone or Mac, keeps the "
         "conversation on the device."),
    ],
    sources="""
<h2>Sources</h2>
<ul>
<li>OpenAI Help Center: <a href="https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt"%(x)s>Chat and file retention in ChatGPT</a> (updated 29 October 2026), <a href="https://help.openai.com/en/articles/7260999-exporting-your-chatgpt-history-and-data"%(x)s>Exporting your ChatGPT history and data</a> (26 October 2026), <a href="https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance"%(x)s>How your data is used to improve model performance</a> (20 October 2026), <a href="https://help.openai.com/en/articles/8914046-temporary-chat-in-chatgpt"%(x)s>Temporary Chat</a> and <a href="https://help.openai.com/en/articles/8809935-deleting-and-archiving-chats-in-chatgpt"%(x)s>Deleting and archiving chats</a> (29 October 2026), <a href="https://help.openai.com/en/articles/6783457-what-is-chatgpt"%(x)s>What is ChatGPT?</a> (20 October 2026).</li>
<li>Anthropic: <a href="https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data"%(x)s>How long do you store my data?</a> (1 July 2026), <a href="https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training"%(x)s>Is my data used for model training?</a> (16 March 2026), <a href="https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings"%(x)s>model improvement settings</a> (3 August 2026); Claude Help Center: <a href="https://support.claude.com/en/articles/12260368-use-incognito-chats"%(x)s>incognito chats</a>, <a href="https://support.claude.com/en/articles/8230524-delete-or-rename-a-conversation"%(x)s>delete a conversation</a>, <a href="https://support.claude.com/en/articles/9450526-export-your-claude-data"%(x)s>export your data</a> (14 October 2026).</li>
<li>Google: <a href="https://support.google.com/gemini/answer/13594961?hl=en"%(x)s>Gemini Apps Privacy Hub</a> (updated 26 October 2026), <a href="https://support.google.com/gemini/answer/13278892"%(x)s>manage your Gemini Apps activity</a>, <a href="https://support.google.com/gemini/answer/13275745"%(x)s>temporary chats</a> and <a href="https://support.google.com/gemini/answer/16920332"%(x)s>export with Google Takeout</a>.</li>
<li>Microsoft: <a href="https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot"%(x)s>Privacy FAQ for Microsoft Copilot</a>, <a href="https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls"%(x)s>Copilot privacy controls</a> and <a href="https://support.microsoft.com/en-us/microsoft-copilot/conversation-history-in-microsoft-copilot"%(x)s>conversation history</a> (older app); <a href="https://support.microsoft.com/en-us/privacy/microsoft-copilot/overview"%(x)s>privacy for the new Copilot app</a>.</li>
<li>Perplexity Help Center: <a href="https://www.perplexity.ai/help-center/en/articles/10354873-how-long-does-perplexity-retain-my-search-history-profile-data-and-personal-information"%(x)s>retention</a>, <a href="https://www.perplexity.ai/help-center/en/articles/10354879-account-deletion"%(x)s>account deletion</a> (22 October 2026), <a href="https://www.perplexity.ai/help-center/en/articles/11564562-self-serve-data-deletion"%(x)s>self-serve data deletion</a> (27 October 2026), <a href="https://www.perplexity.ai/help-center/en/articles/10968016-memory"%(x)s>memory</a>.</li>
<li><a href="https://x.ai/legal/privacy-policy"%(x)s>SpaceXSI (xAI) Privacy Policy</a> (27 October 2026) and <a href="https://x.ai/legal/faq"%(x)s>Grok FAQ</a>.</li>
<li><a href="https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html"%(x)s>DeepSeek Privacy Policy</a>, last updated 10 February 2026.</li>
<li>Mistral Help Center: <a href="https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr"%(x)s>zero data retention and deletion</a> (12 August 2026) and <a href="https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training"%(x)s>training opt-out</a> (3 September 2026).</li>
<li>Meta Help Center: <a href="https://www.meta.com/help/artificial-intelligence/2457110494637611/"%(x)s>remove chats and media from Meta AI</a> and <a href="https://www.meta.com/help/artificial-intelligence/1771195753735844/"%(x)s>export your information</a>.</li>
<li>New York Times v. Microsoft and OpenAI, S.D.N.Y. 1:23-cv-11195: <a href="https://storage.courtlistener.com/recap/gov.uscourts.nysd.612697/gov.uscourts.nysd.612697.551.0.pdf"%(x)s>preservation order of 13 May 2025 (ECF 551)</a> and <a href="https://storage.courtlistener.com/recap/gov.uscourts.nysd.612697/gov.uscourts.nysd.612697.922.0.pdf"%(x)s>stipulation and order of 9 October 2025 (ECF 922)</a>; OpenAI, <a href="https://openai.com/index/response-to-nyt-data-demands/"%(x)s>How we're responding to The New York Times' data demands</a> (5 June 2025, updated 22 October 2025).</li>
<li>Garante per la protezione dei dati personali: <a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870832"%(x)s>limitation of ChatGPT, 30 March 2023</a>, <a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432"%(x)s>fine of 20 December 2024</a> (with the note on the Court of Rome judgment), <a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10097450"%(x)s>DeepSeek, 30 January 2025</a>.</li>
<li>OpenAI, <a href="https://openai.com/index/march-20-chatgpt-outage/"%(x)s>March 20 ChatGPT outage</a> (24 March 2023); Wiz Research, <a href="https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak"%(x)s>exposed DeepSeek database</a> (29 January 2025); NCSC, <a href="https://www.ncsc.gov.uk/blog-post/chatgpt-and-large-language-models-whats-the-risk"%(x)s>ChatGPT and large language models: what's the risk?</a> (14 March 2023).</li>
<li>Yandex: <a href="https://alice.yandex.ru/support/ru/assistant/alice-app"%(x)s>Alice app help</a> and <a href="https://yandex.ru/support/yandex-app-android-alice/ru/privacy/clear-data"%(x)s>deleting your data</a>; Sber: <a href="https://developers.sber.ru/docs/ru/policies/gigachat-agreement/individuals"%(x)s>GigaChat agreement</a> (6 February 2026).</li>
<li><a href="https://www.doubao.com/legal/privacy"%(x)s>Doubao privacy policy</a> (10 September 2026) and <a href="https://www.kimi.com/user/agreement/userPrivacy?version=v2"%(x)s>Kimi privacy policy</a> (24 August 2026).</li>
<li>GDPR <a href="https://gdpr-info.eu/art-12-gdpr/"%(x)s>Article 12</a>, <a href="https://gdpr-info.eu/art-15-gdpr/"%(x)s>15</a> and <a href="https://gdpr-info.eu/art-17-gdpr/"%(x)s>17</a>.</li>
</ul>
<p>First published on 20 October 2026; every page re-read on %(date)s. Policies
change; if one of these is out of date, <a href="mailto:sagalabs@proton.me">tell
us</a> and we will correct the page.</p>
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
