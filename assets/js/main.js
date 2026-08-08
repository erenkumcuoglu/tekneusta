// Tekne Usta — interactions
(function () {
  // Nav scroll state
  var nav = document.getElementById('main-nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  // Mobile menu
  var toggle = document.getElementById('nav-toggle');
  var links = document.getElementById('nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () { links.classList.toggle('open'); });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  // Parallax bands (home)
  var pBands = [
    { el: document.getElementById('par-1'), bg: document.getElementById('pb1') },
    { el: document.getElementById('par-2'), bg: document.getElementById('pb2') },
    { el: document.getElementById('par-3'), bg: document.getElementById('pb3') }
  ].filter(function (x) { return x.el && x.bg; });
  function doParallax() {
    pBands.forEach(function (b) {
      var rect = b.el.getBoundingClientRect();
      var vh = window.innerHeight;
      if (rect.bottom < 0 || rect.top > vh) return;
      var progress = (vh - rect.top) / (vh + rect.height);
      b.bg.style.transform = 'translateY(' + ((progress - 0.5) * 30) + '%)';
    });
  }
  if (pBands.length) {
    window.addEventListener('scroll', doParallax, { passive: true });
    doParallax();
  }

  // Scroll reveal
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } });
    }, { threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) { ro.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var open = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
        var q = i.querySelector('.faq-q'); if (q) q.setAttribute('aria-expanded', 'false');
      });
      if (!open) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    });
  });

  // Quote form — Netlify submit + WhatsApp handoff
  var form = document.getElementById('f-fields');
  if (form) {
    var WA = form.getAttribute('data-wa') || '905321738978';
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var req = ['ad', 'tel', 'tip', 'hizmet'];
      var missing = req.find(function (id) {
        var el = document.getElementById(id);
        return el && !el.value.trim();
      });
      if (missing) { document.getElementById(missing).focus(); return; }

      var data = new FormData(form);
      fetch('/', { method: 'POST', body: data }).catch(function () {});

      var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
      var lead = form.getAttribute('data-lead') || 'Merhaba, tekneusta.com üzerinden teklif talebi:';
      var msg = lead + '%0A%0A' +
        'Ad: ' + encodeURIComponent(v('ad')) + '%0A' +
        'Telefon: ' + encodeURIComponent(v('tel')) + '%0A' +
        (v('email') ? 'E-posta: ' + encodeURIComponent(v('email')) + '%0A' : '') +
        'Tekne Tipi: ' + encodeURIComponent(v('tip')) + '%0A' +
        'Hizmet: ' + encodeURIComponent(v('hizmet')) +
        (v('not') ? '%0ANot: ' + encodeURIComponent(v('not')) : '');

      form.style.display = 'none';
      var ok = document.getElementById('f-success');
      if (ok) ok.style.display = 'block';
      setTimeout(function () { window.open('https://wa.me/' + WA + '?text=' + msg, '_blank'); }, 400);
    });
  }
})();
