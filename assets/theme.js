/* FOX · PT Hub — small shared behaviours */
(function () {
  function init() {
    document.querySelectorAll('.nav').forEach(function (nav) {
      // mouse wheel scrolls tab bars sideways
      nav.addEventListener('wheel', function (e) {
        if (nav.scrollWidth <= nav.clientWidth || Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
        e.preventDefault();
        nav.scrollBy({ left: e.deltaY, behavior: 'auto' });
      }, { passive: false });
      // keep the active tab visible
      var active = nav.querySelector('.active');
      if (active && nav.scrollWidth > nav.clientWidth) active.scrollIntoView({ block: 'nearest', inline: 'center' });
      nav.addEventListener('click', function (e) {
        var b = e.target.closest('button, a');
        if (b && nav.scrollWidth > nav.clientWidth) setTimeout(function () { b.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' }); }, 0);
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
