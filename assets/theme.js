/* FOX · PT Hub — shared behaviours: tab-bar layout, study sidebar, progress memory */
(function () {
  var KEY = 'pthub:v1:' + location.pathname.replace(/index\.html$/, '');
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(st) { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  var ST = load(); ST.done = ST.done || {}; ST.q = ST.q || {};

  function txt(el) { return (el && el.textContent || '').replace(/\s+/g, ' ').trim(); }
  function secIdOf(btn) {
    var m = (btn.getAttribute('onclick') || '').match(/showSection\(\s*['"]([^'"]+)['"]/);
    if (m) return m[1];
    if (btn.id && btn.id.indexOf('btn-') === 0) return btn.id.slice(4);
    return null;
  }
  var UTIL_RE = /showAllAnswers|retest|toggleAll|resetAll|showAll|reset\(/;

  /* ---------------- 1) tab bar: [home · tools] | [شرح] | [أسئلة] ---------------- */
  function layoutNav(nav) {
    var kids = Array.prototype.slice.call(nav.children);
    var util = [], expl = [], ques = [], other = [], tabs = [];
    kids.forEach(function (el) {
      if (!/^(A|BUTTON)$/.test(el.tagName)) { other.push(el); return; }
      var oc = el.getAttribute('onclick') || '', href = el.getAttribute('href') || '';
      if (el.tagName === 'A' && /index\.html/.test(href)) { util.unshift(el); return; }
      if (UTIL_RE.test(oc)) { util.push(el); return; }
      var id = secIdOf(el), sec = id && document.getElementById(id);
      if (!sec) { other.push(el); return; }
      var t = { btn: el, id: id, sec: sec, label: txt(el), kind: kindOf(sec) };
      tabs.push(t); (t.kind === 'expl' ? expl : ques).push(el);
    });
    if (!tabs.length) return null;
    var otherHome = Array.prototype.some.call(document.querySelectorAll('a[href*="index.html"]'), function (a) { return !a.classList.contains('fx-home') && !nav.contains(a); });
    if (!otherHome && !util.some(function (e) { return e.tagName === 'A'; }) && /\/year-\d\//.test(location.pathname)) {
      var a = document.createElement('a'); a.href = '../../index.html'; a.className = 'nav-btn'; a.textContent = '🔙 الرئيسية'; util.unshift(a);
    }
    nav.classList.add('fx-nav');
    nav.innerHTML = '';
    function grp(list, cls, lbl) {
      if (!list.length) return;
      var g = document.createElement('div'); g.className = 'fx-grp ' + cls;
      if (lbl) { var s = document.createElement('span'); s.className = 'fx-grp-lbl'; s.textContent = lbl; g.appendChild(s); }
      list.forEach(function (e) { g.appendChild(e); }); nav.appendChild(g);
    }
    grp(util, 'fx-util'); grp(expl, 'fx-expl', 'الشرح'); grp(ques.concat(other), 'fx-ques', 'الأسئلة');
    return tabs;
  }
  function kindOf(sec) {
    if (sec.querySelector('.summary-box, .summary, .lec-banner')) return 'expl';
    if (!sec.querySelector('.q-card, .w-card, .flashcard, .flip-card, [class*="question"]')) return 'expl';
    return 'ques';
  }

  /* ---------------- 2) study units inside explanation tabs ---------------- */
  function unitsOf(t) {
    var cand = t.sec.querySelectorAll('.summary .card, .card, .topic-card, .info-card, .content-card');
    var out = [];
    Array.prototype.forEach.call(cand, function (c) {
      if (c.closest('.q-card')) return;
      var h = c.querySelector('h2, h3, h4');
      if (!h || (h.closest('.card') !== c && h.closest('.topic-card') !== c && h.closest('.info-card') !== c && h.closest('.content-card') !== c)) return;
      if (out.some(function (o) { return o.el.contains(c); })) return;
      out.push({ el: c, h: h, title: txt(h).replace(/✓ ذاكرت|ذاكرت ✓/g, '').trim() });
    });
    if (!out.length) out.push({ el: t.sec, h: null, title: t.label, whole: true });
    out.forEach(function (u, i) { u.key = t.id + '#' + i; });
    return out;
  }

  /* ---------------- 3) questions tracking ---------------- */
  function qCards(sec) { return sec.querySelectorAll('.q-card'); }
  function trackAnswers(tabs, refresh) {
    document.addEventListener('click', function (e) {
      var card = e.target.closest && e.target.closest('.q-card'); if (!card) return;
      var sec = card.closest('.section, [id]'); var t = null;
      tabs.forEach(function (x) { if (x.sec.contains(card)) t = x; }); if (!t) return;
      setTimeout(function () {
        if (!card.classList.contains('answered')) return;
        var i = Array.prototype.indexOf.call(qCards(t.sec), card); if (i < 0) return;
        var rec = ST.q[t.id] = ST.q[t.id] || {};
        if (!(i in rec)) { rec[i] = card.querySelector('.wrong-selected') ? 0 : 1; save(ST); refresh(); }
      }, 30);
    }, true);
  }

  /* ---------------- 4) sidebar ---------------- */
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  var NOCHIP = false;
  function buildSidebar(tabs) {
    NOCHIP = !!document.querySelector('[onclick*="toggleComplete"]');
    var expl = tabs.filter(function (t) { return t.kind === 'expl'; });
    var ques = tabs.filter(function (t) { return t.kind === 'ques' || qCards(t.sec).length; });
    expl.forEach(function (t) { t.units = unitsOf(t); });

    var fab = el('button', 'fx-fab', '<svg viewBox="0 0 36 36"><circle class="fx-ring-bg" cx="18" cy="18" r="15.5"/><circle class="fx-ring" cx="18" cy="18" r="15.5"/></svg><span class="fx-fab-ic">☰</span><span class="fx-fab-pct">0%</span>');
    fab.setAttribute('aria-label', 'فهرس المذاكرة');
    var scrim = el('div', 'fx-scrim');
    var side = el('aside', 'fx-side'); side.setAttribute('dir', 'rtl');
    var title = txt(document.querySelector('h1')) || document.title;
    side.innerHTML =
      '<div class="fx-side-head"><div class="fx-side-kick">فهرس المذاكرة</div><div class="fx-side-title">' + esc(title) + '</div>' +
      '<button class="fx-x" aria-label="إغلاق">✕</button>' +
      '<div class="fx-meters"><div class="fx-meter"><div class="fx-meter-top"><span>الشرح</span><b class="fx-m-e">0%</b></div><div class="fx-bar"><i class="fx-bar-e"></i></div><small class="fx-m-e2"></small></div>' +
      '<div class="fx-meter"><div class="fx-meter-top"><span>الأسئلة</span><b class="fx-m-q">0%</b></div><div class="fx-bar"><i class="fx-bar-q"></i></div><small class="fx-m-q2"></small></div></div></div>' +
      '<div class="fx-side-body"></div>' +
      '<div class="fx-side-foot"><button class="fx-reset">مسح التقدم في الصفحة دي</button></div>';
    var body = side.querySelector('.fx-side-body');

    function go(t, target) {
      t.btn.click();
      setTimeout(function () {
        var y = (target || t.sec).getBoundingClientRect().top + window.scrollY - 80;
        window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
      }, 60);
      if (window.innerWidth < 1100) close();
    }

    if (expl.length) {
      body.appendChild(el('div', 'fx-sec-lbl', '📖 الشرح'));
      expl.forEach(function (t) {
        var box = el('details', 'fx-item'); box.open = false;
        var sum = el('summary', 'fx-item-head');
        sum.innerHTML = '<span class="fx-dot"></span><span class="fx-item-t">' + esc(t.label) + '</span><span class="fx-item-n"></span>';
        sum.addEventListener('click', function (e) { if (e.target.closest('.fx-item-t')) { e.preventDefault(); go(t); box.open = true; } });
        box.appendChild(sum);
        var ul = el('ul', 'fx-units');
        t.units.forEach(function (u) {
          var li = el('li', 'fx-unit'); li.dataset.k = u.key;
          li.innerHTML = '<button class="fx-chk" aria-label="ذاكرت"></button><span>' + esc(u.title || '—') + '</span>';
          li.querySelector('.fx-chk').addEventListener('click', function (e) { e.stopPropagation(); toggle(u.key); });
          li.querySelector('span').addEventListener('click', function () { go(t, u.whole ? null : u.el); });
          ul.appendChild(li);
          // in-page "studied" chip (skip on pages that already have their own "done" toggles)
          if (NOCHIP) return;
          var chip = el('button', 'fx-chip', 'ذاكرت ✓'); chip.dataset.k = u.key; chip.type = 'button';
          chip.addEventListener('click', function (e) { e.stopPropagation(); toggle(u.key); });
          if (u.h) u.h.appendChild(chip); else { var w = el('div', 'fx-chip-row'); w.appendChild(chip); t.sec.appendChild(w); }
        });
        box.appendChild(ul); body.appendChild(box); t.box = box;
      });
    }
    if (ques.length) {
      body.appendChild(el('div', 'fx-sec-lbl', '🎯 الأسئلة'));
      ques.forEach(function (t) {
        var row = el('button', 'fx-qrow'); t.qrow = row;
        row.innerHTML = '<span class="fx-item-t">' + esc(t.label) + '</span><span class="fx-qbar"><i></i></span><span class="fx-qn"></span>';
        row.addEventListener('click', function () { go(t); });
        body.appendChild(row);
      });
    }

    function toggle(k) { if (ST.done[k]) delete ST.done[k]; else ST.done[k] = 1; save(ST); refresh(); }
    function refresh() {
      var tu = 0, du = 0;
      expl.forEach(function (t) {
        var d = 0; t.units.forEach(function (u) { if (ST.done[u.key]) d++; }); tu += t.units.length; du += d;
        t.box.querySelector('.fx-item-n').textContent = d + '/' + t.units.length;
        t.box.classList.toggle('is-done', d === t.units.length); t.box.classList.toggle('is-part', d > 0 && d < t.units.length);
      });
      document.querySelectorAll('.fx-unit, .fx-chip').forEach(function (e) { e.classList.toggle('on', !!ST.done[e.dataset.k]); });
      var tq = 0, aq = 0, cq = 0;
      ques.forEach(function (t) {
        var n = qCards(t.sec).length, rec = ST.q[t.id] || {}, a = 0, c = 0;
        for (var i in rec) { if (+i < n) { a++; c += rec[i]; } }
        tq += n; aq += a; cq += c;
        t.qrow.querySelector('.fx-qn').textContent = n ? a + '/' + n : '—';
        t.qrow.querySelector('.fx-qbar i').style.width = (n ? a / n * 100 : 0) + '%';
        t.qrow.classList.toggle('is-done', n > 0 && a === n);
      });
      var pe = tu ? Math.round(du / tu * 100) : null, pq = tq ? Math.round(aq / tq * 100) : null;
      side.querySelector('.fx-m-e').textContent = pe == null ? '—' : pe + '%';
      side.querySelector('.fx-bar-e').style.width = (pe || 0) + '%';
      side.querySelector('.fx-m-e2').textContent = tu ? 'ذاكرت ' + du + ' من ' + tu + ' جزء' : 'مفيش شرح في الصفحة دي';
      side.querySelector('.fx-m-q').textContent = pq == null ? '—' : pq + '%';
      side.querySelector('.fx-bar-q').style.width = (pq || 0) + '%';
      side.querySelector('.fx-m-q2').textContent = tq ? 'حليت ' + aq + ' من ' + tq + ' سؤال' + (aq ? ' · صح ' + cq + ' (' + Math.round(cq / aq * 100) + '%)' : '') : 'مفيش أسئلة تفاعلية';
      var parts = [pe, pq].filter(function (x) { return x != null; });
      var all = parts.length ? Math.round(parts.reduce(function (a, b) { return a + b; }, 0) / parts.length) : 0;
      fab.querySelector('.fx-fab-pct').textContent = all + '%';
      fab.querySelector('.fx-ring').style.strokeDashoffset = 97.4 * (1 - all / 100);
    }
    function open() { document.body.classList.add('fx-side-open'); }
    function close() { document.body.classList.remove('fx-side-open'); }
    fab.addEventListener('click', function () { document.body.classList.contains('fx-side-open') ? close() : open(); });
    scrim.addEventListener('click', close);
    side.querySelector('.fx-x').addEventListener('click', close);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    side.querySelector('.fx-reset').addEventListener('click', function () {
      if (!confirm('هيتمسح تقدمك في الصفحة دي بس. متأكد؟')) return;
      ST = { done: {}, q: {} }; save(ST); refresh();
    });
    // the page's own "retest" clears question progress for this page
    tabs.forEach(function () {});
    document.querySelectorAll('.fx-util [onclick*="retest"]').forEach(function (b) {
      b.addEventListener('click', function () { ST.q = {}; save(ST); refresh(); });
    });
    document.body.appendChild(scrim); document.body.appendChild(side); document.body.appendChild(fab);
    var pill = document.querySelector('.fx-home'); if (pill) pill.classList.add('fx-raised');
    refresh();
    return refresh;
  }

  function init() {
    var tabsAll = [];
    document.querySelectorAll('.nav').forEach(function (nav) {
      var tabs = layoutNav(nav); if (tabs) tabsAll = tabsAll.concat(tabs);
      nav.addEventListener('wheel', function (e) {
        if (nav.scrollWidth <= nav.clientWidth || Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
        e.preventDefault(); nav.scrollBy({ left: e.deltaY, behavior: 'auto' });
      }, { passive: false });
      var active = nav.querySelector('.active');
      if (active && nav.scrollWidth > nav.clientWidth) active.scrollIntoView({ block: 'nearest', inline: 'center' });
      nav.addEventListener('click', function (e) {
        var b = e.target.closest('button, a');
        if (b && nav.scrollWidth > nav.clientWidth) setTimeout(function () { b.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' }); }, 0);
      });
    });
    if (tabsAll.length >= 1) { var r = buildSidebar(tabsAll); trackAnswers(tabsAll, r); }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
