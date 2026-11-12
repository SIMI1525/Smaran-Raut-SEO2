/**
 * blog-search.js — Live Blog Search & Tag Filter
 * Smaran Raut SEO Website | v2026_v1
 *
 * Features:
 *  - Instant client-side search (title + tags, no API call)
 *  - Tag/category chip filters
 *  - Zero-layout-shift: visibility toggled via CSS class
 *  - Debounced input for smooth typing
 *  - Accessible: ARIA live region announces result count
 */

(function () {
  'use strict';

  // ── Blog post index (embedded for instant search) ────────────────────────
  // Each entry mirrors the blog directory. Update when adding new posts.
  const POSTS = [
    {
      slug:     'what-is-seo',
      title:    'What Is SEO? A Complete Beginner\'s Guide (2026)',
      excerpt:  'Learn what Search Engine Optimisation is, how it works, and why every Nepal business needs it.',
      tags:     ['seo-basics', 'beginner', 'nepal'],
      category: 'seo-basics',
    },
    {
      slug:     'how-seo-works',
      title:    'How Does SEO Work? Crawling, Indexing & Ranking Explained',
      excerpt:  'A step-by-step breakdown of how Google discovers, evaluates, and ranks web pages in Nepal.',
      tags:     ['seo-basics', 'google', 'ranking'],
      category: 'seo-basics',
    },
    {
      slug:     'on-page-seo-guide',
      title:    'On-Page SEO Guide: Optimise Every Page for Google',
      excerpt:  'Master title tags, meta descriptions, heading hierarchy, and internal linking for top rankings.',
      tags:     ['on-page-seo', 'content', 'technical'],
      category: 'on-page-seo',
    },
    {
      slug:     'off-page-seo-guide',
      title:    'Off-Page SEO Guide: Build Authority Beyond Your Website',
      excerpt:  'Backlinks, brand mentions, digital PR — the complete off-page strategy for Nepal businesses.',
      tags:     ['off-page-seo', 'backlinks', 'authority'],
      category: 'off-page-seo',
    },
    {
      slug:     'technical-seo-checklist',
      title:    'Technical SEO Checklist 2026: 50 Checks You Can\'t Ignore',
      excerpt:  'Site speed, Core Web Vitals, crawl budget, schema markup — the definitive technical audit checklist.',
      tags:     ['technical-seo', 'checklist', 'core-web-vitals'],
      category: 'technical-seo',
    },
    {
      slug:     'local-seo-guide-nepal',
      title:    'Local SEO Guide for Nepal: Rank in Your City\'s Map Pack',
      excerpt:  'How businesses in Itahari, Biratnagar, and across Nepal dominate local Google searches.',
      tags:     ['local-seo', 'nepal', 'google-maps', 'itahari'],
      category: 'local-seo',
    },
    {
      slug:     'keyword-research-guide',
      title:    'Keyword Research Guide: Find What Nepal Searches in 2026',
      excerpt:  'Tools, techniques, and Nepal-specific tips to discover high-intent keywords that convert.',
      tags:     ['keyword-research', 'tools', 'nepal'],
      category: 'seo-basics',
    },
    {
      slug:     'seo-vs-ppc',
      title:    'SEO vs PPC: Which Is Better for Nepal Businesses?',
      excerpt:  'Compare organic search and paid advertising — cost, timeline, ROI, and when to use each.',
      tags:     ['seo-basics', 'ppc', 'digital-marketing', 'nepal'],
      category: 'digital-marketing',
    },
    {
      slug:     'google-search-console-guide',
      title:    'Google Search Console Guide: Monitor & Fix Your SEO',
      excerpt:  'Set up GSC, interpret performance reports, fix coverage errors, and submit sitemaps.',
      tags:     ['tools', 'google', 'technical-seo'],
      category: 'tools',
    },
    {
      slug:     'google-analytics-seo',
      title:    'Google Analytics 4 for SEO: Track What Actually Matters',
      excerpt:  'Configure GA4 to measure organic traffic, conversions, and user behaviour for SEO decisions.',
      tags:     ['tools', 'google', 'analytics'],
      category: 'tools',
    },
    {
      slug:     'backlink-building-nepal',
      title:    'Backlink Building in Nepal: Earn Links That Move Rankings',
      excerpt:  'White-hat link acquisition strategies tailored to the Nepal digital landscape in 2026.',
      tags:     ['off-page-seo', 'backlinks', 'nepal'],
      category: 'off-page-seo',
    },
    {
      slug:     'website-speed-optimization',
      title:    'Website Speed Optimisation: Score 95+ on PageSpeed Insights',
      excerpt:  'Images, caching, minification, CDN — every technique to make your Nepal website lightning fast.',
      tags:     ['technical-seo', 'core-web-vitals', 'performance'],
      category: 'technical-seo',
    },
    {
      slug:     'mobile-seo-guide',
      title:    'Mobile SEO Guide: Rank on the Device Nepal Uses Most',
      excerpt:  'Responsive design, mobile-first indexing, tap targets, and AMP considerations for Nepal sites.',
      tags:     ['technical-seo', 'mobile', 'core-web-vitals'],
      category: 'technical-seo',
    },
    {
      slug:     'ecommerce-seo-nepal',
      title:    'E-commerce SEO Nepal: Drive Organic Sales Without Ads',
      excerpt:  'Product page optimisation, category SEO, schema markup, and site architecture for Nepal stores.',
      tags:     ['ecommerce', 'nepal', 'on-page-seo'],
      category: 'ecommerce',
    },
    {
      slug:     'wordpress-seo-guide',
      title:    'WordPress SEO Guide: Rank Higher With the World\'s Top CMS',
      excerpt:  'Yoast vs Rank Math, permalink settings, speed plugins, and schema setup for WordPress Nepal.',
      tags:     ['wordpress', 'cms', 'on-page-seo', 'tools'],
      category: 'tools',
    },
    {
      slug:     'schema-markup-guide',
      title:    'Schema Markup Guide: Get Rich Results on Google Search',
      excerpt:  'JSON-LD implementation for LocalBusiness, FAQPage, Article, and Product schema in Nepal.',
      tags:     ['technical-seo', 'schema', 'structured-data'],
      category: 'technical-seo',
    },
    {
      slug:     'seo-audit-checklist',
      title:    'SEO Audit Checklist 2026: 80-Point Website Health Check',
      excerpt:  'The exact audit framework used by Smaran Raut to identify and fix ranking blockers.',
      tags:     ['technical-seo', 'checklist', 'audit'],
      category: 'technical-seo',
    },
    {
      slug:     'content-writing-seo',
      title:    'SEO Content Writing Guide: Write for Humans, Rank on Google',
      excerpt:  'E-E-A-T, semantic keywords, content structure, and publishing cadence for Nepal audiences.',
      tags:     ['content', 'on-page-seo', 'eeat'],
      category: 'content',
    },
    {
      slug:     'seo-tools-nepal',
      title:    'Best SEO Tools for Nepal in 2026 (Free & Paid)',
      excerpt:  'Semrush, Ahrefs, Ubersuggest — which tools give the best ROI for Nepal SEO professionals?',
      tags:     ['tools', 'nepal', 'keyword-research'],
      category: 'tools',
    },
    {
      slug:     'google-algorithm-updates',
      title:    'Google Algorithm Updates 2026: What Changed & How to Adapt',
      excerpt:  'Helpful Content, Core Updates, spam policies — stay ahead of Google\'s ranking changes.',
      tags:     ['google', 'algorithm', 'seo-basics'],
      category: 'seo-basics',
    },
    {
      slug:     'nepal-digital-marketing-guide',
      title:    'Nepal Digital Marketing Guide 2026: SEO, Social & Beyond',
      excerpt:  'The complete digital marketing roadmap for Nepali businesses: SEO, social media, email, PPC.',
      tags:     ['digital-marketing', 'nepal', 'social-media'],
      category: 'digital-marketing',
    },
    {
      slug:     'how-to-rank-on-google-nepal',
      title:    'How to Rank on Google in Nepal: Step-by-Step (2026)',
      excerpt:  'From domain registration to first-page rankings — the actionable Nepal SEO roadmap.',
      tags:     ['seo-basics', 'nepal', 'ranking', 'beginner'],
      category: 'seo-basics',
    },
    {
      slug:     'seo-pricing-nepal',
      title:    'SEO Pricing in Nepal 2026: What Does SEO Really Cost?',
      excerpt:  'Monthly retainer, project-based, hourly — transparent SEO pricing for Nepal businesses.',
      tags:     ['nepal', 'pricing', 'seo-basics'],
      category: 'local-seo',
    },
    {
      slug:     'website-development-cost-nepal',
      title:    'Website Development Cost in Nepal 2026: Full Price Guide',
      excerpt:  'Static sites, WordPress, e-commerce — realistic cost estimates from a Nepal developer.',
      tags:     ['nepal', 'pricing', 'web-development'],
      category: 'web-development',
    },
    {
      slug:     'best-cms-for-seo',
      title:    'Best CMS for SEO in 2026: WordPress vs Others Compared',
      excerpt:  'WordPress, Webflow, Ghost, Joomla — ranked by SEO capability for Nepal websites.',
      tags:     ['cms', 'wordpress', 'technical-seo'],
      category: 'technical-seo',
    },
    {
      slug:     'social-media-seo',
      title:    'Social Media SEO: How Social Signals Impact Your Rankings',
      excerpt:  'Facebook, Instagram, TikTok — how Nepal businesses use social media to amplify SEO.',
      tags:     ['social-media', 'off-page-seo', 'digital-marketing'],
      category: 'digital-marketing',
    },
    {
      slug:     'youtube-seo-guide',
      title:    'YouTube SEO Guide: Rank Your Videos on Google & YouTube',
      excerpt:  'Titles, descriptions, tags, thumbnails — the YouTube SEO playbook for Nepal content creators.',
      tags:     ['youtube', 'video-seo', 'digital-marketing'],
      category: 'digital-marketing',
    },
    {
      slug:     'nepal-ecommerce-guide',
      title:    'Nepal E-commerce Guide 2026: Start, Grow & Scale Online',
      excerpt:  'Platform selection, payment gateways, logistics, and SEO for Nepal online stores.',
      tags:     ['ecommerce', 'nepal', 'digital-marketing'],
      category: 'ecommerce',
    },
    {
      slug:     'google-my-business-guide',
      title:    'Google My Business Guide 2026: Complete Profile Optimisation',
      excerpt:  'Setup, NAP consistency, reviews, posts, Q&A — maximise your GMB profile for Nepal searches.',
      tags:     ['local-seo', 'google-maps', 'gmb', 'nepal'],
      category: 'local-seo',
    },
    {
      slug:     'seo-for-small-business-nepal',
      title:    'SEO for Small Business Nepal: Compete Without a Big Budget',
      excerpt:  'Practical, low-cost SEO tactics that give Nepali SMEs a fighting chance against bigger brands.',
      tags:     ['local-seo', 'small-business', 'nepal', 'beginner'],
      category: 'local-seo',
    },
    {
      slug:     'itahari-business-directory',
      title:    'Itahari Business Directory 2026: Top Local Businesses Listed',
      excerpt:  'Comprehensive directory of Itahari businesses with addresses, contacts, and categories.',
      tags:     ['itahari', 'local-seo', 'nepal', 'directory'],
      category: 'local-seo',
    },
  ];

  // ── Utility: debounce ─────────────────────────────────────────────────────
  function debounce(fn, wait) {
    var timer;
    return function () {
      var ctx  = this;
      var args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () { fn.apply(ctx, args); }, wait);
    };
  }

  // ── Core filter logic ─────────────────────────────────────────────────────
  var activeTag   = 'all';
  var searchQuery = '';

  function filterCards() {
    var blogGrid  = document.getElementById('blog-grid');
    var noResults = document.getElementById('no-results');
    var liveRegion = document.getElementById('blog-search-status');

    if (!blogGrid) return;

    var cards        = blogGrid.querySelectorAll('.blog-card');
    var visibleCount = 0;

    cards.forEach(function (card) {
      var title    = (card.dataset.title    || '').toLowerCase();
      var tags     = (card.dataset.tags     || '').toLowerCase();
      var category = (card.dataset.category || '').toLowerCase();
      var excerpt  = (card.dataset.excerpt  || '').toLowerCase();

      var matchesSearch =
        !searchQuery ||
        title.includes(searchQuery)    ||
        tags.includes(searchQuery)     ||
        excerpt.includes(searchQuery);

      var matchesTag =
        activeTag === 'all' ||
        tags.includes(activeTag)     ||
        category.includes(activeTag);

      if (matchesSearch && matchesTag) {
        card.classList.remove('blog-card--hidden');
        card.removeAttribute('aria-hidden');
        visibleCount++;
      } else {
        card.classList.add('blog-card--hidden');
        card.setAttribute('aria-hidden', 'true');
      }
    });

    // Show/hide empty state
    if (noResults) {
      noResults.hidden = visibleCount > 0;
    }

    // Announce result count to screen readers
    if (liveRegion) {
      liveRegion.textContent =
        visibleCount === 0
          ? 'No blog posts found. Try a different search term.'
          : visibleCount + ' blog post' + (visibleCount === 1 ? '' : 's') + ' found.';
    }
  }

  // ── Initialise ────────────────────────────────────────────────────────────
  function init() {
    var searchInput = document.getElementById('blog-search-input');
    var tagFilters  = document.querySelectorAll('.tag-filter-chip');
    var blogGrid    = document.getElementById('blog-grid');

    // Inject ARIA live region if not present
    if (!document.getElementById('blog-search-status')) {
      var liveRegion = document.createElement('div');
      liveRegion.id              = 'blog-search-status';
      liveRegion.setAttribute('role', 'status');
      liveRegion.setAttribute('aria-live', 'polite');
      liveRegion.setAttribute('aria-atomic', 'true');
      liveRegion.className       = 'sr-only';
      document.body.appendChild(liveRegion);
    }

    // Populate data attributes from POSTS index if cards lack them
    if (blogGrid) {
      blogGrid.querySelectorAll('.blog-card').forEach(function (card) {
        var slug = card.dataset.slug;
        if (!slug) return;
        var post = POSTS.find(function (p) { return p.slug === slug; });
        if (!post) return;
        if (!card.dataset.title)    card.dataset.title    = post.title;
        if (!card.dataset.tags)     card.dataset.tags     = post.tags.join(' ');
        if (!card.dataset.category) card.dataset.category = post.category;
        if (!card.dataset.excerpt)  card.dataset.excerpt  = post.excerpt;
      });
    }

    // Search input handler (debounced 200 ms)
    if (searchInput) {
      searchInput.addEventListener(
        'input',
        debounce(function () {
          searchQuery = this.value.toLowerCase().trim();
          filterCards();
        }, 200)
      );

      // Clear on Escape
      searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
          this.value = '';
          searchQuery = '';
          filterCards();
        }
      });
    }

    // Tag chip handler
    tagFilters.forEach(function (chip) {
      chip.addEventListener('click', function () {
        tagFilters.forEach(function (c) {
          c.classList.remove('active');
          c.setAttribute('aria-pressed', 'false');
        });
        this.classList.add('active');
        this.setAttribute('aria-pressed', 'true');
        activeTag = this.dataset.tag || 'all';
        filterCards();
      });

      // Keyboard activation (Space / Enter already fire click on buttons)
      chip.setAttribute('role', 'button');
      chip.setAttribute('aria-pressed', chip.classList.contains('active') ? 'true' : 'false');
      if (!chip.getAttribute('tabindex')) {
        chip.setAttribute('tabindex', '0');
      }
    });

    // Run initial filter (respects any default active chip)
    var defaultChip = document.querySelector('.tag-filter-chip.active');
    if (defaultChip) {
      activeTag = defaultChip.dataset.tag || 'all';
    }
    filterCards();
  }

  // ── Boot ──────────────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
