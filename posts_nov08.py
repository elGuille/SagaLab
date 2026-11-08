# -*- coding: utf-8 -*-
"""Noticia (8 nov 2026): la investigacion de los Democratas a las criptos de la familia Trump tras las
elecciones de mitad de mandato, y como se movieron WLFI, TRUMP y USD1 (EN + ES). Lo pidio Marta, con Crypton.

Datos comprobados el 8 nov 2026:
- crypto.news, 4 nov 2026 (Rony Roy): Camara para los Democratas segun NBC News y MS NOW; Robert Garcia,
  «Lawyer up.»; investigaciones desde febrero de 2027; WLFI, USD1, World Liberty Trust, TRUMP, indulto de
  Changpeng Zhao (lo niega); 49 % y 500 M$ de Tahnoon; Reuters, 2.300 M$; mas de 1.000 M$ y ~635 M$ de TRUMP;
  Lauren Bis a Newsweek (parafraseada, la cita va en la de Garcia).
- Reuters en The Star, 15 ago 2026: OCC, aprobacion preliminar y condicional el 14 ago 2026, no final.
- CNBC, 5 nov 2026 (Tanaya Macheel): CLARITY fallo la votacion de cloture del Senado en septiembre; unos
  esperan una version mas dura el ano que viene, otros nada hasta 2028.
- FT, 8 nov 2026: solo el titular (de pago).
- Precios: API de CoinGecko, cierre diario UTC del 1 nov y valor del 8 nov ~10:20 UTC; USD1 y BTC del fichero
  de hechos de Crecimiento (CoinGecko, 8 nov).
- Crypton: ficha de EE. UU. de la 2.0.8 (buscador de cualquier moneda de CoinGecko), 4,7 con 186 valoraciones
  (API de lookup, 8 nov). Sin alertas en la version a la venta. Sin opinion politica ni predicciones. Sin rayas.
"""
import json
import re

ISO = "2026-11-08"
EN = "blog/trump-crypto-midterms-investigation-wlfi-trump-usd1.html"
ES = "blog/es/criptos-de-trump-tras-las-elecciones-investigacion-wlfi-trump-usd1.html"

CRYPTON = "https://apps.apple.com/app/id1143691286"
COINGECKO_APP = "https://apps.apple.com/us/app/id1390323960"
CMC_APP = "https://apps.apple.com/us/app/id1282107098"
CN = "https://crypto.news/democrats-prepare-to-investigate-world-liberty-financial-after-house-win/"
CNBC = "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"
OCC = "https://www.thestar.com.my/tech/tech-news/2026/08/15/us-regulator-approves-bank-charter-for-trump-backed-crypto-company-world-liberty-financial"
CG = {"TRUMP": "https://www.coingecko.com/en/coins/official-trump",
      "WLFI": "https://www.coingecko.com/en/coins/world-liberty-financial",
      "USD1": "https://www.coingecko.com/en/coins/usd1-wlfi",
      "BTC": "https://www.coingecko.com/en/coins/bitcoin"}


def a(u, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)


T = {
"en": dict(
 path=EN, kicker="Crypto news", date="8 November 2026",
 h1="Trump family crypto after the midterms: what Democrats plan to investigate, and how WLFI, TRUMP and USD1 moved",
 desc=("After Democrats won the House on 3 November 2026, reports say they plan to investigate World Liberty "
       "Financial (WLFI, USD1) and the TRUMP meme coin. A dated timeline, CoinGecko prices from 1 to 8 November, "
       "what to watch next and how to follow these tokens on iPhone."),
 stand="What has been reported, with dates and sources, and what the prices did in the week after the vote.",
 switch='<a href="es/criptos-de-trump-tras-las-elecciones-investigacion-wlfi-trump-usd1.html" hreflang="es">Leer en espa&ntilde;ol</a>',
 answer=("<p><strong>After Democrats won the House in the 3 November 2026 midterms, Rep. Robert Garcia, expected to chair "
         "the House Oversight Committee, signalled investigations into the Trump family's crypto businesses, which "
         "according to " + a(CN, "crypto.news") + " could begin as early as February 2027.</strong> In the week after "
         "the vote, CoinGecko data show the TRUMP meme coin down about 32%, World Liberty Financial's WLFI token down "
         "about 8%, and the USD1 stablecoin holding close to $1.</p>"),
 what_h="What has been reported",
 what=("<p>According to " + a(CN, "crypto.news") + ", which cited NBC News and MS NOW projections, Democrats won "
       "control of the House. It reported that Garcia answered the result with two words, &ldquo;Lawyer up,&rdquo; "
       "and that committees could seek documents and testimony by subpoena.</p>\n"
       "<p>The targets named in that reporting are:</p>\n<ul>\n"
       "<li><strong>World Liberty Financial</strong>, its WLFI token and its USD1 stablecoin, including its foreign "
       "ownership. crypto.news reported that an investment vehicle of the UAE's Sheikh Tahnoon bin Zayed took a 49% "
       "stake, for a reported $500 million, shortly before the January 2025 inauguration.</li>\n"
       "<li><strong>World Liberty Trust Company</strong>, the planned trust bank for USD1. Reuters reported that the "
       "Office of the Comptroller of the Currency gave it preliminary conditional approval on 14 August 2026, and that "
       "it is not final (" + a(OCC, "Reuters, via The Star") + ").</li>\n"
       "<li><strong>The TRUMP meme coin.</strong> According to crypto.news, Trump reported more than $1 billion of "
       "crypto-related income for 2025, about $635 million of it in royalties tied to the coin, and Reuters estimated "
       "that the family's crypto ventures earned at least $2.3 billion.</li>\n"
       "<li><strong>The pardon of Binance founder Changpeng Zhao.</strong> crypto.news reported that Zhao denies business "
       "ties to the family and says he never discussed any clemency arrangement.</li>\n"
       "<li>Business dealings of other family members.</li>\n</ul>\n"
       "<p>White House spokeswoman Lauren Bis told Newsweek, as cited by crypto.news, that the Democrats' plans are a "
       "continuation of what she described as a long-running witch hunt against the president. On 8 November the "
       "Financial Times carried the story on its front page under the headline <em>Crypto industry braces for reckoning "
       "over Trump ties</em>.</p>"),
 tl_h="Timeline",
 tl=[("Before January 2025", "A vehicle of Sheikh Tahnoon bin Zayed reportedly takes 49% of World Liberty Financial (crypto.news)."),
     ("14 August 2026", "The OCC gives World Liberty Trust Company preliminary conditional approval (Reuters)."),
     ("September 2026", "The CLARITY Act fails a Senate cloture vote (CNBC)."),
     ("3 November 2026", "Midterm elections; Democrats win the House, according to NBC News and MS NOW projections."),
     ("4 November 2026", "TRUMP has its largest daily fall of the week on CoinGecko, from $1.59 to $1.27. crypto.news reports the planned investigations."),
     ("5 November 2026", "CNBC reports that the result puts the crypto industry on the defensive in Washington."),
     ("8 November 2026", "The Financial Times runs the story on its front page."),
     ("From February 2027", "Investigations could begin, according to crypto.news.")],
 px_h="How the tokens moved, 1 to 8 November",
 th=("Token", "1 Nov (daily close)", "8 Nov", "Change", "Market cap, 8 Nov"),
 rows=[("TRUMP (Official Trump)", "$1.71", "$1.16", "&minus;32%", "~$328 million"),
       ("WLFI (World Liberty Financial)", "$0.050", "$0.046", "&minus;8%", "~$1.47 billion"),
       ("USD1 (stablecoin)", "$0.998", "$0.998", "0%", "~$3.44 billion (from ~$3.87 billion)"),
       ("Bitcoin, for comparison", "$78,294", "$75,806", "&minus;3%", "")],
 px_note=("Source: CoinGecko, daily close in UTC for 1 November and the price on the morning of 8 November (UTC). "
          "Rounded. USD1 kept its price, while its market cap on CoinGecko fell by about $430 million over the week. Bitcoin also fell over the same week, so not every move can be put down to the news."),
 next_h="What to watch next",
 nxt=["<strong>When the committees start.</strong> crypto.news reported that investigations could begin as early as "
      "February 2027, once the new House is in place.",
      "<strong>The CLARITY Act.</strong> " + a(CNBC, "CNBC") + " reported that the market-structure bill had already failed "
      "a Senate cloture vote in September; analysts it quoted expect either a tougher Democratic version next year or no "
      "movement until 2028.",
      "<strong>The trust bank.</strong> World Liberty Trust Company's approval is preliminary and conditional; the OCC "
      "still has to give final approval (Reuters)."],
 track_h="How to track WLFI, TRUMP and USD1 on iPhone",
 track=("<p>Any crypto tracker that uses CoinGecko or CoinMarketCap data lists all three. Three options:</p>\n<ul>\n"
        "<li><strong>Crypton</strong>, our app (" + a(CRYPTON, "App Store") + ", 4.7 stars from 186 US ratings). Search "
        "for WLFI, TRUMP or USD1 by name or symbol, add them to your favourites and pick them for the Coin List widget on "
        "your Home Screen. If you hold any, add the amount and your average buy price to see profit and loss. It works "
        "without an account. It does not have price alerts in the version on sale.</li>\n"
        "<li><strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), the source of the prices in this article, "
        "with alerts and widgets.</li>\n"
        "<li><strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), with alerts and widgets.</li>\n</ul>\n"
        "<p>For more, see <a href=\"best-crypto-portfolio-tracker-apps-iphone.html\">the best crypto portfolio tracker "
        "apps for iPhone</a> and <a href=\"../crypton/track-crypto-prices-without-giving-your-data.html\">how to track "
        "crypto prices without giving your data</a>.</p>"),
 nfa="Not financial advice. This article reports what others have published and what prices did; it does not recommend buying or selling anything.",
 src_h="Sources",
 src=[a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 November 2026.",
      a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 November 2026.",
      a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15 August 2026.",
      "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 November 2026 (paywalled; headline only).",
      "Prices: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", read on 8 November 2026.",
      "Crypton: its US App Store page and Apple's public lookup API, 8 November 2026."],
 own="Disclosure: we make Crypton.",
 fix='If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
 faq_h="Questions people ask",
 faq=[("Are Democrats investigating Trump's crypto?", "According to crypto.news, after winning the House on 3 November 2026, Democrats plan to look at World Liberty Financial, USD1, the TRUMP meme coin and related deals, and investigations could begin as early as February 2027."),
      ("How did the TRUMP coin react to the midterms?", "On CoinGecko it went from $1.71 at the 1 November close to about $1.16 on 8 November, a fall of about 32%, with the largest daily drop on 4 November."),
      ("Did USD1 lose its peg?", "No. On CoinGecko it stayed close to $1 in the week after the vote, at about $0.998 on 8 November."),
      ("How can I follow WLFI and TRUMP on iPhone?", "Search for them in a tracker that uses CoinGecko or CoinMarketCap data, such as Crypton (ours), CoinGecko or CoinMarketCap, add them to a watchlist and put them on a Home Screen widget.")],
),
"es": dict(
 path=ES, kicker="Noticias cripto", date="8 de noviembre de 2026",
 h1="Las criptos de la familia Trump tras las elecciones: qué quieren investigar los demócratas y cómo se han movido WLFI, TRUMP y USD1",
 desc=("Tras ganar los demócratas la Cámara de Representantes el 3 de noviembre de 2026, varios medios cuentan que "
       "investigarán World Liberty Financial (WLFI, USD1) y la memecoin TRUMP. Cronología, precios de CoinGecko del 1 "
       "al 8 de noviembre, qué vigilar y cómo seguir estos tokens en el iPhone."),
 stand="Lo publicado hasta ahora, con fecha y fuente, y qué hicieron los precios la semana siguiente a la votación.",
 switch='<a href="../trump-crypto-midterms-investigation-wlfi-trump-usd1.html" hreflang="en">Read in English</a>',
 answer=("<p><strong>Los demócratas ganaron la Cámara de Representantes en las elecciones del 3 de noviembre de 2026, y "
         "el congresista Robert Garcia, que previsiblemente presidirá el Comité de Supervisión, ha dado a entender que "
         "habrá investigaciones sobre los negocios cripto de la familia Trump; según " + a(CN, "crypto.news") + ", "
         "podrían empezar en febrero de 2027.</strong> En la semana posterior, según CoinGecko, la memecoin TRUMP bajó "
         "un 32 %, el token WLFI de World Liberty Financial un 8 % y la stablecoin USD1 se mantuvo cerca de 1 dólar.</p>"),
 what_h="Qué se ha publicado",
 what=("<p>Según " + a(CN, "crypto.news") + ", que cita las proyecciones de NBC News y MS NOW, los demócratas se quedan "
       "con la Cámara. El medio cuenta que Garcia respondió al resultado con un aviso de dos palabras, «Lawyer up» "
       "(«búsquense abogado»), y que los comités podrán pedir documentos y declaraciones por citación.</p>\n"
       "<p>Lo que esa información señala como objetivo:</p>\n<ul>\n"
       "<li><strong>World Liberty Financial</strong>, con su token WLFI y su stablecoin USD1, y quién es dueño de qué. "
       "crypto.news publica que un vehículo de inversión del jeque emiratí Tahnoon bin Zayed se quedó con el 49 %, por "
       "unos 500 millones de dólares, poco antes de la toma de posesión de enero de 2025.</li>\n"
       "<li><strong>World Liberty Trust Company</strong>, el banco fiduciario previsto para USD1. Según Reuters, la "
       "Oficina del Contralor de la Moneda (OCC) le dio una aprobación preliminar y condicional el 14 de agosto de 2026, "
       "que todavía no es definitiva (" + a(OCC, "Reuters, en The Star") + ").</li>\n"
       "<li><strong>La memecoin TRUMP.</strong> Según crypto.news, Trump declaró más de 1.000 millones de dólares de "
       "ingresos ligados a las cripto en 2025, unos 635 millones por derechos vinculados a esta moneda; Reuters calcula "
       "que los negocios cripto de la familia han ganado al menos 2.300 millones.</li>\n"
       "<li><strong>El indulto a Changpeng Zhao</strong>, fundador de Binance. crypto.news recoge que Zhao niega tener "
       "negocios con la familia y haber hablado nunca de un indulto.</li>\n"
       "<li>Negocios de otros miembros de la familia.</li>\n</ul>\n"
       "<p>La portavoz de la Casa Blanca Lauren Bis dijo a Newsweek, según crypto.news, que lo que buscan los demócratas "
       "es seguir con lo que ella llama una caza de brujas contra el presidente que dura ya años. El 8 de noviembre el "
       "Financial Times lo llevó a portada con el titular <em>Crypto industry braces for reckoning over Trump ties</em>.</p>"),
 tl_h="Cronología",
 tl=[("Antes de enero de 2025", "Un vehículo del jeque Tahnoon bin Zayed se queda, según la prensa, con el 49 % de World Liberty Financial (crypto.news)."),
     ("14 de agosto de 2026", "La OCC da a World Liberty Trust Company una aprobación preliminar y condicional (Reuters)."),
     ("Septiembre de 2026", "La ley CLARITY no supera una votación de cloture en el Senado (CNBC)."),
     ("3 de noviembre de 2026", "Elecciones de mitad de mandato; los demócratas ganan la Cámara, según las proyecciones de NBC News y MS NOW."),
     ("4 de noviembre de 2026", "TRUMP tiene en CoinGecko su mayor caída diaria de la semana, de 1,59 a 1,27 dólares. crypto.news informa de las investigaciones."),
     ("5 de noviembre de 2026", "CNBC publica que el resultado deja al sector cripto a la defensiva en Washington."),
     ("8 de noviembre de 2026", "El Financial Times lo lleva a portada."),
     ("Desde febrero de 2027", "Podrían empezar las investigaciones, según crypto.news.")],
 px_h="Cómo se movieron los tokens del 1 al 8 de noviembre",
 th=("Token", "1 nov (cierre)", "8 nov", "Cambio", "Capitalización, 8 nov"),
 rows=[("TRUMP (Official Trump)", "1,71 $", "1,16 $", "&minus;32 %", "~328 millones $"),
       ("WLFI (World Liberty Financial)", "0,050 $", "0,046 $", "&minus;8 %", "~1.470 millones $"),
       ("USD1 (stablecoin)", "0,998 $", "0,998 $", "0 %", "~3.440 millones $ (desde ~3.870 millones)"),
       ("Bitcoin, para comparar", "78.294 $", "75.806 $", "&minus;3 %", "")],
 px_note=("Fuente: CoinGecko, cierre diario en UTC del 1 de noviembre y precio de la mañana del 8 de noviembre (UTC), "
          "redondeado. USD1 mantuvo el precio, pero su capitalización en CoinGecko bajó unos 430 millones de dólares en la semana. El bitcoin también bajó esa semana, así que no todo movimiento se puede atribuir a la noticia."),
 next_h="Qué vigilar a partir de ahora",
 nxt=["<strong>Cuándo arrancan los comités.</strong> crypto.news apunta a febrero de 2027 como pronto, ya con la nueva Cámara.",
      "<strong>La ley CLARITY.</strong> Según " + a(CNBC, "CNBC") + ", la ley sobre la estructura del mercado cripto ya se "
      "atascó en el Senado en septiembre; los analistas que cita esperan o una versión más dura de los demócratas el año que "
      "viene o nada hasta 2028.",
      "<strong>El banco fiduciario.</strong> La aprobación de World Liberty Trust Company es preliminar y condicional: la OCC "
      "aún tiene que dar la definitiva (Reuters)."],
 track_h="Cómo seguir WLFI, TRUMP y USD1 en el iPhone",
 track=("<p>Cualquier app que use datos de CoinGecko o CoinMarketCap tiene los tres. Tres opciones:</p>\n<ul>\n"
        "<li><strong>Crypton</strong>, nuestra app (" + a(CRYPTON, "App Store") + ", 4,7 estrellas con 186 valoraciones en "
        "EE. UU.). Busca WLFI, TRUMP o USD1 por nombre o símbolo, añádelos a favoritos y elígelos en el widget de lista de "
        "monedas de la pantalla de inicio. Si tienes alguno, pon la cantidad y tu precio medio de compra y verás cuánto "
        "ganas o pierdes. No hace falta cuenta. La versión a la venta no tiene alertas de precio.</li>\n"
        "<li><strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), de donde salen los precios de este artículo, "
        "con alertas y widgets.</li>\n"
        "<li><strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), con alertas y widgets.</li>\n</ul>\n"
        "<p>Más en <a href=\"mejores-apps-cartera-cripto-iphone.html\">las mejores apps para seguir tu cartera de "
        "criptomonedas en iPhone</a> y en <a href=\"../../crypton/es/seguir-precios-cripto-sin-dar-tus-datos.html\">cómo "
        "seguir los precios cripto sin dar tus datos</a>.</p>"),
 nfa="Esto no es asesoramiento financiero. Contamos lo que otros han publicado y lo que hicieron los precios; no recomendamos comprar ni vender nada.",
 src_h="Fuentes",
 src=[a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 de noviembre de 2026.",
      a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 de noviembre de 2026.",
      a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters en The Star, 15 de agosto de 2026.",
      "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 de noviembre de 2026 (de pago; solo el titular).",
      "Precios: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", consultado el 8 de noviembre de 2026.",
      "Crypton: su ficha del App Store de EE. UU. y la API pública de Apple, 8 de noviembre de 2026."],
 own="Aviso: Crypton es nuestra.",
 fix='Si algo está desactualizado, <a href="mailto:sagalabs@proton.me">avísanos</a> y lo corregimos.',
 faq_h="Preguntas frecuentes",
 faq=[("¿Van a investigar los demócratas las criptos de Trump?", "Según crypto.news, tras ganar la Cámara el 3 de noviembre de 2026 quieren examinar World Liberty Financial, USD1, la memecoin TRUMP y otros negocios, y las investigaciones podrían empezar en febrero de 2027."),
      ("¿Cómo reaccionó la moneda TRUMP a las elecciones?", "En CoinGecko pasó de 1,71 dólares al cierre del 1 de noviembre a unos 1,16 el 8 de noviembre, un 32 % menos, con la mayor caída diaria el 4 de noviembre."),
      ("¿Ha perdido USD1 su paridad con el dólar?", "No. En CoinGecko se mantuvo cerca de 1 dólar la semana siguiente a la votación, en unos 0,998 el 8 de noviembre."),
      ("¿Cómo sigo WLFI y TRUMP en el iPhone?", "Búscalos en una app que use datos de CoinGecko o CoinMarketCap, como Crypton (nuestra), CoinGecko o CoinMarketCap, añádelos a favoritos y ponlos en un widget de la pantalla de inicio.")],
)}


def build(render):
    alts = ('    <link rel="alternate" hreflang="en" href="https://aisagalab.com/%s">\n'
            '    <link rel="alternate" hreflang="es" href="https://aisagalab.com/%s">\n'
            '    <link rel="alternate" hreflang="x-default" href="https://aisagalab.com/%s">' % (EN, ES, EN))
    out = []
    for lang, c in T.items():
        tl = "".join("<li><strong>%s.</strong> %s</li>\n" % x for x in c["tl"])
        rows = "".join("<tr>%s</tr>\n" % "".join("<td>%s</td>" % v for v in r) for r in c["rows"])
        nxt = "".join("<li>%s</li>\n" % x for x in c["nxt"])
        faq = "".join("<h3>%s</h3>\n<p>%s</p>\n" % q for q in c["faq"])
        body = ('<p class="article-kicker">%s</p>\n<h1>%s</h1>\n<p class="article-standfirst">%s</p>\n'
                '<p class="article-meta"><a href="https://www.linkedin.com/in/maruta/" rel="author me noopener" target="_blank">Maruta G</a> &middot; %s <span class="lang-switch"> &middot; %s</span></p>\n'
                '<div class="article-body">\n%s\n<h2>%s</h2>\n%s\n<h2>%s</h2>\n<ul>\n%s</ul>\n'
                '<h2>%s</h2>\n<div class="table-scroll"><table><thead><tr>%s</tr></thead><tbody>\n%s</tbody></table></div>\n<p class="article-note">%s</p>\n'
                '<h2>%s</h2>\n<ul>\n%s</ul>\n<h2>%s</h2>\n%s\n<p class="article-note">%s</p>\n<h2>%s</h2>\n%s</div>\n'
                '<div class="article-body article-sources">\n<h2>%s</h2>\n<ul>\n%s</ul>\n<p>%s</p>\n<p>%s</p>\n</div>') % (
            c["kicker"], c["h1"], c["stand"], c["date"], c["switch"], c["answer"], c["what_h"], c["what"], c["tl_h"], tl,
            c["px_h"], "".join("<th>%s</th>" % h for h in c["th"]), rows, c["px_note"], c["next_h"], nxt,
            c["track_h"], c["track"], c["nfa"], c["faq_h"], faq, c["src_h"],
            "".join("<li>%s</li>\n" % s for s in c["src"]), c["own"], c["fix"])
        art = {"@type": "NewsArticle", "headline": c["h1"], "description": c["desc"], "inLanguage": lang,
               "datePublished": ISO, "dateModified": ISO,
               "mainEntityOfPage": {"@type": "WebPage", "@id": "https://aisagalab.com/" + c["path"]},
               "image": "https://aisagalab.com/images/preview.jpg",
               "author": {"@type": "Person", "name": "Maruta G", "url": "https://www.linkedin.com/in/maruta/"},
               "publisher": {"@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/"}}
        faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", r)}} for q, r in c["faq"]]}
        out.append(render(path=c["path"], lang=lang, title=c["h1"] + " | Saga Labs", desc=c["desc"], og_title=c["h1"], body=body,
                          jsonld=json.dumps({"@context": "https://schema.org", "@graph": [art, faqld]}, ensure_ascii=False, indent=2), alternates=alts))
    return out
