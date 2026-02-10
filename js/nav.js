document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('.sidebar');
  var overlay = document.querySelector('.sidebar-overlay');
  var menuToggle = document.querySelector('.mobile-menu-toggle');
  var mobileNav = document.getElementById('mobile-nav');

  function closeMobileNav() {
    if (mobileNav && menuToggle) {
      mobileNav.hidden = true;
      menuToggle.setAttribute('aria-expanded', 'false');
      menuToggle.setAttribute('aria-label', 'Open menu');
    }
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (overlay) overlay.classList.remove('visible');
  }

  if (toggle && sidebar) {
    toggle.addEventListener('click', function () {
      closeMobileNav();
      sidebar.classList.toggle('open');
      if (overlay) overlay.classList.toggle('visible');
    });
  }

  if (overlay) {
    overlay.addEventListener('click', function () {
      closeSidebar();
      closeMobileNav();
    });
  }

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', function () {
      var isOpen = !mobileNav.hidden;
      if (!isOpen) closeSidebar();
      mobileNav.hidden = isOpen;
      menuToggle.setAttribute('aria-expanded', String(!isOpen));
      menuToggle.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');
    });

    document.addEventListener('click', function (e) {
      if (!mobileNav.hidden && !mobileNav.contains(e.target) && !menuToggle.contains(e.target)) {
        closeMobileNav();
      }
    });
  }

  // Navigation dropdown toggles
  var dropdownToggles = document.querySelectorAll('.nav-dropdown-toggle');
  var allDropdowns = document.querySelectorAll('.nav-dropdown');

  function closeAllDropdowns() {
    allDropdowns.forEach(function(dropdown) {
      dropdown.hidden = true;
    });
    dropdownToggles.forEach(function(toggle) {
      toggle.setAttribute('aria-expanded', 'false');
    });
  }

  dropdownToggles.forEach(function(toggle) {
    toggle.addEventListener('click', function(e) {
      e.stopPropagation();
      var targetId = this.getAttribute('aria-controls');
      var targetDropdown = document.getElementById(targetId);
      var isOpen = this.getAttribute('aria-expanded') === 'true';

      // Close all dropdowns first
      closeAllDropdowns();

      // If this one wasn't open, open it
      if (!isOpen && targetDropdown) {
        targetDropdown.hidden = false;
        this.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', function(e) {
    var clickedInside = false;
    allDropdowns.forEach(function(dropdown) {
      if (dropdown.contains(e.target)) {
        clickedInside = true;
      }
    });
    if (!clickedInside) {
      closeAllDropdowns();
    }
  });

  var themeBtn = document.querySelector('.theme-toggle');
  var html = document.documentElement;

  function getPreferred() {
    var stored = localStorage.getItem('theme');
    if (stored) return stored;
    return 'dark';
  }

  function applyTheme(theme) {
    if (theme === 'light') {
      html.setAttribute('data-theme', 'light');
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
      var current = html.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
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
