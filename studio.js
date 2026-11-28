// Saga Lab studio pages: mobile nav and a one-time card entrance.
document.documentElement.classList.add('js');
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.nav-menu-btn');
  var links = document.getElementById('nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // App landings: the sticky screenshot follows the feature heading in view.
  var feats = document.querySelectorAll('.feat-list li');
  var phones = document.querySelectorAll('.feat-phone img');
  if (feats.length && 'IntersectionObserver' in window) {
    var fo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var i = Array.prototype.indexOf.call(feats, e.target);
        feats.forEach(function (f, k) { f.classList.toggle('on', k === i); });
        phones.forEach(function (p, k) { p.classList.toggle('on', k === i); });
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    feats.forEach(function (f) { fo.observe(f); });
  }

  var items = document.querySelectorAll('.reveal');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) { items.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  items.forEach(function (el) { io.observe(el); });
});

/* Hero background light follows the pointer (desktop, motion allowed). */
(function () {
  if (!matchMedia('(pointer: fine)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('.glow').forEach(function (g) {
    var host = g.parentElement, raf = 0;
    host.addEventListener('pointermove', function (e) {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        var r = host.getBoundingClientRect();
        g.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
        g.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
        raf = 0;
      });
    });
  });
})();
