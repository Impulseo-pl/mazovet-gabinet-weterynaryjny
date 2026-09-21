/* Mazovet — demo Impulseo */
(function () {
  document.documentElement.classList.add('js');

  // menu mobilne
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.mainnav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // nagłówek nad hero -> po scrollu pełna biel
  var head = document.querySelector('.site-head.over');
  if (head) {
    var onScroll = function () {
      head.classList.toggle('solid', window.scrollY > 40);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // pojawianie się sekcji
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // dzisiejszy dzień w tabeli godzin
  var todayRow = document.querySelector('.hours tr[data-day="' + new Date().getDay() + '"]');
  if (todayRow) todayRow.classList.add('today');

  // status otwarcia (pn–pt 8–18, sob 9–13)
  var statusEl = document.querySelector('[data-open-status]');
  if (statusEl) {
    var now = new Date(), d = now.getDay(), m = now.getHours() * 60 + now.getMinutes();
    var open = (d >= 1 && d <= 5 && m >= 480 && m < 1080) || (d === 6 && m >= 540 && m < 780);
    statusEl.textContent = open ? 'Teraz otwarte' : 'Teraz zamknięte';
  }

  // filtry galerii
  var filterBtns = document.querySelectorAll('.filters button');
  if (filterBtns.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.dataset.filter;
        filterBtns.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        document.querySelectorAll('.gal figure').forEach(function (fig) {
          fig.style.display = (f === 'all' || fig.dataset.cat === f) ? '' : 'none';
        });
      });
    });
  }

  // formularz — w demie nie wysyła
  var form = document.querySelector('form[data-demo-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form-result');
      if (note) {
        note.hidden = false;
        note.textContent = 'To wersja demonstracyjna — formularz uruchamiamy przy wdrożeniu strony. W pilnej sprawie prosimy o telefon: 794 206 306.';
      }
    });
  }
})();
