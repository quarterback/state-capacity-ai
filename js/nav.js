document.addEventListener('DOMContentLoaded', function () {
  // Sidebar toggle (mobile)
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('.sidebar');
  var overlay = document.querySelector('.sidebar-overlay');

  if (toggle && sidebar) {
    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      if (overlay) overlay.classList.toggle('visible');
    });
  }

  if (overlay) {
    overlay.addEventListener('click', function () {
      sidebar.classList.remove('open');
      overlay.classList.remove('visible');
    });
  }

  // Theme toggle
  var themeBtn = document.querySelector('.theme-toggle');
  var html = document.documentElement;

  function getPreferred() {
    var stored = localStorage.getItem('theme');
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      html.setAttribute('data-theme', 'dark');
    } else {
      html.removeAttribute('data-theme');
    }
    if (themeBtn) {
      themeBtn.textContent = theme === 'dark' ? 'Light' : 'Dark';
      themeBtn.setAttribute('aria-label', 'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' theme');
    }
  }

  applyTheme(getPreferred());

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = html.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      var next = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem('theme', next);
      applyTheme(next);
    });
  }

  var searchInput = document.getElementById('guide-search');
  var noResults = document.getElementById('no-results');

  if (searchInput) {
    var allCards = document.querySelectorAll('.guide-card');
    var sections = document.querySelectorAll('.landing-section');

    searchInput.addEventListener('input', function () {
      var query = this.value.toLowerCase().trim();
      var visibleCount = 0;

      allCards.forEach(function (card) {
        var title = card.querySelector('.guide-card-title');
        var desc = card.querySelector('.guide-card-desc');
        var tags = card.getAttribute('data-tags') || '';
        var text = (title ? title.textContent : '') + ' ' + (desc ? desc.textContent : '') + ' ' + tags;

        if (!query || text.toLowerCase().indexOf(query) !== -1) {
          card.classList.remove('hidden');
          visibleCount++;
        } else {
          card.classList.add('hidden');
        }
      });

      if (noResults) {
        noResults.hidden = visibleCount > 0;
      }

      sections.forEach(function (section) {
        var sectionCards = section.querySelectorAll('.guide-card');
        var sectionVisible = 0;
        sectionCards.forEach(function (c) {
          if (!c.classList.contains('hidden')) sectionVisible++;
        });
        var heading = section.querySelector('h2');
        var grid = section.querySelector('.guide-grid');
        var extBtn = section.querySelector('.ext-btn');
        if (heading) heading.style.display = sectionVisible > 0 || !query ? '' : 'none';
        if (grid) grid.style.display = sectionVisible > 0 ? '' : 'none';
        if (extBtn) extBtn.style.display = sectionVisible > 0 || !query ? '' : 'none';
      });
    });
  }
});
