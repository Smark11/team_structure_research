/* Progressive enhancement only. The site reads fully without this file. */
(function () {
  'use strict';
  // Reading progress hairline
  var bar = document.querySelector('.progress');
  if (bar) {
    var tick = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = max > 0 ? (100 * h.scrollTop / max) + '%' : '0%';
    };
    window.addEventListener('scroll', tick, { passive: true });
    tick();
  }

  // Citation hover/focus previews: reads the entry from an inline <template id="src-index"> if present,
  // otherwise from a data attribute. No network.
  var pop = null;
  function showPop(a) {
    var id = (a.getAttribute('href') || '').split('#')[1];
    if (!id) return;
    var tpl = document.getElementById('src-index');
    var text = null;
    if (tpl) {
      var el = tpl.content.querySelector('[data-id="' + id + '"]');
      if (el) text = el.innerHTML;
    }
    if (!text) text = a.getAttribute('data-src');
    if (!text) return;
    if (!pop) {
      pop = document.createElement('div');
      pop.className = 'cite-pop';
      pop.setAttribute('role', 'tooltip');
      pop.id = 'cite-pop';
      document.body.appendChild(pop);
    }
    a.setAttribute('aria-describedby', 'cite-pop');
    pop.innerHTML = text;
    var r = a.getBoundingClientRect();
    var left = Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - 360);
    pop.style.left = Math.max(8, left) + 'px';
    pop.style.top = (r.bottom + window.scrollY + 8) + 'px';
    pop.hidden = false;
  }
  function hidePop() {
    if (pop) pop.hidden = true;
    document.querySelectorAll('sup.c a[aria-describedby]').forEach(function (el) { el.removeAttribute('aria-describedby'); });
  }
  document.querySelectorAll('sup.c a').forEach(function (a) {
    a.addEventListener('mouseenter', function () { showPop(a); });
    a.addEventListener('mouseleave', hidePop);
    a.addEventListener('focus', function () { showPop(a); });
    a.addEventListener('blur', hidePop);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hidePop(); });

  // Expand a drill-down if it is the hash target
  function openTarget() {
    var id = location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var d = el.closest('details');
    if (d) d.open = true;
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();
})();
