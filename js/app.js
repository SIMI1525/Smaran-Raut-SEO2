/**
 * Core Application Script & Universal Event Architecture
 * - Universal Event Delegation for Modals, CTAs, Mobile Drawers & Accordions
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

    // 4. Mobile Menu Open
    if (e.target.closest('#mobile-menu-toggle')) {
      e.preventDefault();
      const drawer = document.getElementById('mobile-nav-drawer');
      if (drawer) {
        drawer.classList.add('active');
        document.body.classList.add('modal-open');
      }
      return;
    }

    // 4b. Mobile Dropdown Toggle (Tap-to-expand)
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

    // 4c. Desktop Dropdown Click Toggle & Outside Click
    const deskToggle = e.target.closest('.dropdown-toggle');
    if (deskToggle) {
      e.preventDefault();
      const dropdown = deskToggle.closest('.nav-dropdown');
      if (dropdown) {
        const isCurrentActive = dropdown.classList.contains('active');
        document.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('active'));
        if (!isCurrentActive) {
          dropdown.classList.add('active');
        }
      }
      return;
    } else if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('active'));
    }

    // 5. Mobile Menu Close
    if (e.target.closest('#mobile-menu-close, .mobile-nav-links a:not(.mobile-dropdown-toggle)')) {
      const drawer = document.getElementById('mobile-nav-drawer');
      if (drawer) {
        drawer.classList.remove('active');
        document.body.classList.remove('modal-open');
      }
      return;
    }

    // 6. Accordion Header Toggle
    const accHeader = e.target.closest('.accordion-header');
    if (accHeader) {
      e.preventDefault();
      const item = accHeader.closest('.accordion-item');
      if (item) {
        const isActive = item.classList.contains('active');
        // Close siblings in same accordion if desired
        const parentAcc = item.closest('.faq-accordion');
        if (parentAcc) {
          parentAcc.querySelectorAll('.accordion-item').forEach(sibling => {
            sibling.classList.remove('active');
          });
        }
        if (!isActive) {
          item.classList.add('active');
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
      const drawer = document.getElementById('mobile-nav-drawer');
      if (drawer && drawer.classList.contains('active')) {
        drawer.classList.remove('active');
        document.body.classList.remove('modal-open');
      }
    }
  });

  // Universal Form Validation & Submission Interceptor
  document.addEventListener('submit', function (e) {
    const form = e.target;
    if (!form || !form.matches('form')) return;

    e.preventDefault();

    // Check validity
    if (!form.checkValidity()) {
      window.showToast("Please complete all required fields correctly.", "error");
      return;
    }

    // Collect data summary
    const nameInput = form.querySelector('[name="name"], [name="client_name"]');
    const clientName = nameInput ? nameInput.value.trim() : "Valued Client";

    // Simulate instant secure submission
    window.showToast(`Thank you, ${clientName}! Your inquiry has been securely dispatched to Smaran Raut. We will contact you within 24 business hours.`, "success");

    // Reset and close modal
    form.reset();
    closeModal();
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

  // Live Search Input Listener for Blog
  document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('blog-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', function () {
        const activeTagPill = document.querySelector('.tag-pill.active');
        const activeTag = activeTagPill ? activeTagPill.getAttribute('data-filter') : 'all';
        filterBlogArticles(activeTag);
      });
    }
  });

})();
