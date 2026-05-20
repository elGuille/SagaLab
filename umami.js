/* ───────────────────────────────────────────────────────────
   Umami analytics loader (self-hosted, cookieless, no banner)
   Dashboard: https://analytics.kilmaru.com
   Site: sagalab.co
   ─────────────────────────────────────────────────────────── */
(function () {
  var WEBSITE_ID = 'eb0ef22e-f9a7-4493-8852-aeed689aa013';
  var UMAMI_SRC = 'https://analytics.kilmaru.com/script.js';

  if (!WEBSITE_ID) return;

  var s = document.createElement('script');
  s.defer = true;
  s.src = UMAMI_SRC;
  s.setAttribute('data-website-id', WEBSITE_ID);
  document.head.appendChild(s);
})();
