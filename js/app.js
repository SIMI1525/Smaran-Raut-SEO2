/**
 * Core Application Script & Universal Event Architecture
 * - Universal Event Delegation for Modals, CTAs, Mobile Drawers & Accordions
 * - Robust Header Dropdown State Management (Auto-Close & BFCache Resilient)
 * - Universal Form Interception with Toast Feedback
 * - Knowledge Hub Live Search & Tag Filtering
 * - Clean Scroll-Locking & Escape Handlers
 */

(function () {
  'use strict';

  // Floating Toast Notification System
  window.showToast = function (message, type = 'success') {
    let container = document.getElementById('toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toast-container';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    // Icon
    const iconSvg = type === 'success' 
      ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>'
      : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>';

    toast.innerHTML = `${iconSvg}<span>${message}</span>`;
    container.appendChild(toast);

    // Trigger animation
    setTimeout(() => {
      toast.classList.add('show');
    }, 10);

    // Auto remove after 4.5 seconds
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
        if (toast.parentNode) {
          toast.parentNode.removeChild(toast);
        }
      }, 300);
    }, 4500);
  };

  // Modal Controllers
  function openConsultationModal(servicePrefill) {
    const modal = document.getElementById('consultation-modal');
    if (!modal) return;

    if (servicePrefill) {
      const select = modal.querySelector('#modal-service-select');
      if (select) {
        select.value = servicePrefill;
      }
    }

    modal.classList.add('active');
    document.body.classList.add('modal-open');
  }

  function closeModal() {
    const modals = document.querySelectorAll('.modal-backdrop');
    modals.forEach(m => m.classList.remove('active'));
    document.body.classList.remove('modal-open');
  }

  // Central Dropdown & Navigation State Manager
  function closeAllDropdowns() {
    // 1. Reset all desktop dropdowns
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
      dropdown.classList.remove('active');
      const toggle = dropdown.querySelector('.dropdown-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    });

    // 2. Reset all mobile dropdown items
    document.querySelectorAll('.mobile-dropdown-item').forEach(item => {
      item.classList.remove('active');
      const toggle = item.querySelector('.mobile-dropdown-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
      const submenu = item.querySelector('.mobile-submenu');
      if (submenu) submenu.style.display = 'none';
    });

    // 3. Remove lingering focus so :focus-within doesn't keep dropdowns visible
    if (document.activeElement && (document.activeElement.closest('.nav-dropdown') || document.activeElement.closest('.mobile-nav-drawer'))) {
      document.activeElement.blur();
    }
  }

  function closeMobileDrawer() {
    document.querySelectorAll('.mobile-nav-drawer').forEach(drawer => {
      drawer.classList.remove('active');
    });
    document.body.classList.remove('modal-open');
  }

  // Bind mouseleave / mouseenter on desktop dropdowns to cleanly reset hover suppression
  function initDropdownHoverListeners() {
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
      dropdown.addEventListener('mouseleave', function () {
        this.classList.remove('is-closed');
        this.classList.remove('active');
        const toggle = this.querySelector('.dropdown-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      });
      dropdown.addEventListener('mouseenter', function () {
        this.classList.remove('is-closed');
      });
    });
  }

  // Universal Event Delegation
  document.addEventListener('click', function (e) {
    // 1. Consultation Modal Triggers
    const trigger = e.target.closest('[data-modal="consultation"], .btn-consultation, #book-consultation-btn, [href*="#consultation"]');
    if (trigger) {
      e.preventDefault();
      const service = trigger.getAttribute('data-service') || '';
      openConsultationModal(service);
      return;
    }

    // 2. Modal Close Buttons
    if (e.target.closest('.modal-close-btn, [data-modal-close]')) {
      e.preventDefault();
      closeModal();
      return;
    }

    // 3. Modal Backdrop Click Close
    if (e.target.classList.contains('modal-backdrop')) {
      closeModal();
      return;
    }

    // 4a. Dropdown Menu Item Click (Services & Knowledge Hub)
    // Instantly close the dropdown and blur the link so it never remains open after navigation
    const dropdownLink = e.target.closest('.dropdown-menu a, .dropdown-item');
    if (dropdownLink) {
      const parentDropdown = dropdownLink.closest('.nav-dropdown');
      if (parentDropdown) {
        parentDropdown.classList.add('is-closed');
        parentDropdown.classList.remove('active');
        const toggle = parentDropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      }
      closeAllDropdowns();
      return; // Allow standard link navigation to continue
    }

    // 4b. Mobile Navigation Link Click
    const mobileLink = e.target.closest('.mobile-nav-drawer a, .mobile-submenu a');
    if (mobileLink && !mobileLink.classList.contains('mobile-dropdown-toggle')) {
      closeAllDropdowns();
      closeMobileDrawer();
      return; // Allow standard link navigation to continue
    }

    // 4c. Mobile Menu Open
    if (e.target.closest('#mobile-menu-toggle, #mobile-menu-open-btn, .mobile-menu-btn')) {
      e.preventDefault();
      document.querySelectorAll('.mobile-nav-drawer').forEach(drawer => {
        drawer.classList.add('active');
      });
      document.body.classList.add('modal-open');
      return;
    }

    // 4d. Mobile Dropdown Toggle (Tap-to-expand)
    const mobileToggle = e.target.closest('.mobile-dropdown-toggle');
    if (mobileToggle) {
      e.preventDefault();
      const item = mobileToggle.closest('.mobile-dropdown-item');
      if (item) {
        const submenu = item.querySelector('.mobile-submenu');
        const isExpanded = item.classList.contains('active');
        if (submenu) {
          if (isExpanded) {
            item.classList.remove('active');
            submenu.style.display = 'none';
            mobileToggle.setAttribute('aria-expanded', 'false');
          } else {
            item.classList.add('active');
            submenu.style.display = 'flex';
            mobileToggle.setAttribute('aria-expanded', 'true');
          }
        }
      }
      return;
    }

    // 4e. Desktop Dropdown Click Toggle & Outside Click
    const deskToggle = e.target.closest('.dropdown-toggle');
    if (deskToggle) {
      const dropdown = deskToggle.closest('.nav-dropdown');
      const isNavAnchor = deskToggle.tagName === 'A' && deskToggle.getAttribute('href') && deskToggle.getAttribute('href') !== '#';

      if (isNavAnchor) {
        // Services tab is a direct navigation link to Services Overview
        closeAllDropdowns();
        if (dropdown) dropdown.classList.add('is-closed');
        return; // Allow direct navigation to proceed
      } else {
        // Button toggle (e.g. Knowledge Hub)
        e.preventDefault();
        if (dropdown) {
          const isCurrentActive = dropdown.classList.contains('active');
          closeAllDropdowns();
          if (!isCurrentActive) {
            dropdown.classList.remove('is-closed');
            dropdown.classList.add('active');
            deskToggle.setAttribute('aria-expanded', 'true');
          }
        }
        return;
      }
    } else if (!e.target.closest('.nav-dropdown')) {
      closeAllDropdowns();
    }

    // 5. Mobile Menu Close Button
    if (e.target.closest('#mobile-menu-close, #mobile-drawer-close-btn, .mobile-drawer-close')) {
      e.preventDefault();
      closeMobileDrawer();
      return;
    }

    // 6. Accordion Header Toggle
    const accHeader = e.target.closest('.accordion-header');
    if (accHeader) {
      e.preventDefault();
      const item = accHeader.closest('.accordion-item');
      if (item) {
        const isActive = item.classList.contains('active');
        const parentAcc = item.closest('.faq-accordion');
        if (parentAcc) {
          parentAcc.querySelectorAll('.accordion-item').forEach(sibling => {
            sibling.classList.remove('active');
            const btn = sibling.querySelector('.accordion-header');
            if (btn) btn.setAttribute('aria-expanded', 'false');
          });
        }
        if (!isActive) {
          item.classList.add('active');
          accHeader.setAttribute('aria-expanded', 'true');
        } else {
          accHeader.setAttribute('aria-expanded', 'false');
        }
      }
      return;
    }

    // 7. Knowledge Hub Tag Filter Pills
    const tagPill = e.target.closest('.tag-pill');
    if (tagPill) {
      e.preventDefault();
      const parentWrap = tagPill.closest('.tag-pills-wrap');
      if (parentWrap) {
        parentWrap.querySelectorAll('.tag-pill').forEach(p => p.classList.remove('active'));
      }
      tagPill.classList.add('active');

      const filterTag = tagPill.getAttribute('data-filter') || 'all';
      filterBlogArticles(filterTag);
    }
  });

  // Global Keyboard Escape Listener
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' || e.keyCode === 27) {
      closeModal();
      closeAllDropdowns();
      closeMobileDrawer();
    }
  });

  // Universal Form Validation & Submission Interceptor (Cloudflare Pages Function /api/submit & D1 integration)
  document.addEventListener('submit', function (e) {
    const form = e.target;
    if (!form || !form.matches('form')) return;

    e.preventDefault();

    if (!form.checkValidity()) {
      window.showToast("Please complete all required fields correctly.", "error");
      return;
    }

    const nameInput = form.querySelector('[name="name"], [name="client_name"]');
    const clientName = nameInput ? nameInput.value.trim() : "Valued Client";

    // Submit button loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnContent = submitBtn ? submitBtn.innerHTML : '';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.setAttribute('aria-busy', 'true');
      submitBtn.textContent = 'Submitting...';
    }

    // Build structured payload for /api/submit
    const formData = new FormData(form);
    const payload = {};
    for (const [key, value] of formData.entries()) {
      payload[key] = typeof value === 'string' ? value.trim() : value;
    }

    // Ensure form identifier is explicitly present
    if (!payload['form-name'] && !payload['form_type']) {
      const formName = form.getAttribute('name') || form.id || 'consultation-modal';
      payload['form-name'] = formName;
    }

    // Attach originating page URL
    payload['page_url'] = window.location.href;

    const postEndpoint = (form.getAttribute('action') && form.getAttribute('action') !== '/')
      ? form.getAttribute('action')
      : '/api/submit';

    fetch(postEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    .then(function (response) {
      return response.json().then(function (data) {
        if (response.ok && data.success) {
          const successMsg = data.message || `Thank you, ${clientName}! Your inquiry has been securely received by Smaran Raut. We will contact you within 24 business hours.`;
          window.showToast(successMsg, "success");
          form.reset();
          closeModal();
        } else {
          const errorMsg = (data && data.error) ? data.error : ("Server returned status " + response.status);
          throw new Error(errorMsg);
        }
      });
    })
    .catch(function (error) {
      console.warn('Form submission notice:', error);
      // In local static development (file:// or python static server without Pages Functions),
      // inform developer gracefully that validation passed; in production, show exact server error or fallback.
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:') {
        window.showToast(`[Local Preview] Thank you, ${clientName}! Form validated. (On Cloudflare Pages production, this saves to D1 and dispatches email).`, "success");
        form.reset();
        closeModal();
      } else {
        const userNotice = (error && error.message && !error.message.includes('fetch'))
          ? error.message
          : "There was an issue dispatching your request online. Please contact us directly at +977 9714539838 or contact@smaranraut.com.np.";
        window.showToast(userNotice, "error");
      }
    })
    .finally(function () {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.removeAttribute('aria-busy');
        submitBtn.innerHTML = originalBtnContent;
      }
    });
  });

  // Knowledge Hub Filtering Logic
  function filterBlogArticles(tag) {
    const articles = document.querySelectorAll('.blog-article-item');
    const searchInput = document.getElementById('blog-search-input');
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    let matchCount = 0;

    articles.forEach(article => {
      const artTag = article.getAttribute('data-tag') || '';
      const text = article.textContent.toLowerCase();

      const matchesTag = (tag === 'all' || artTag === tag);
      const matchesQuery = (!query || text.includes(query));

      if (matchesTag && matchesQuery) {
        article.style.display = '';
        matchCount++;
      } else {
        article.style.display = 'none';
      }
    });

    const countEl = document.getElementById('blog-results-count');
    if (countEl) {
      countEl.textContent = `Showing ${matchCount} guides`;
    }
  }

  // Handle Lifecycle, BFCache, and Initial DOM Load
  window.addEventListener('pageshow', function () {
    closeAllDropdowns();
    closeMobileDrawer();
  });

  function initApp() {
    closeAllDropdowns();
    closeMobileDrawer();
    initDropdownHoverListeners();

    const searchInput = document.getElementById('blog-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', function () {
        const activeTagPill = document.querySelector('.tag-pill.active');
        const activeTag = activeTagPill ? activeTagPill.getAttribute('data-filter') : 'all';
        filterBlogArticles(activeTag);
      });
    }

    // Services Overview Package Toggle (Show More / Show Less)
    const toggleBtn = document.getElementById('toggle-packages-btn');
    const moreContainer = document.getElementById('more-packages');
    if (toggleBtn && moreContainer) {
      toggleBtn.addEventListener('click', function () {
        const isExpanded = moreContainer.classList.contains('is-expanded');
        if (isExpanded) {
          moreContainer.classList.remove('is-expanded');
          toggleBtn.setAttribute('aria-expanded', 'false');
          toggleBtn.innerHTML = 'Show More Packages &darr;';
          toggleBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          moreContainer.classList.add('is-expanded');
          toggleBtn.setAttribute('aria-expanded', 'true');
          toggleBtn.innerHTML = 'Show Less Packages &uarr;';
        }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
