/**
 * Master Site Architecture & Entity Graph Data
 * Brand: Smaran Raut - SEO & Web Specialist in Itahari
 * Geographic Focus: Itahari, Sunsari, Koshi Province, Nepal
 * Verified Core Services:
 * 1. SEO-optimized business website development
 * 2. SEO services for existing websites
 * 3. Ongoing website management
 * 4. Relevant website maintenance and minor improvements
 */

const SITE_DATA = {
  brand: {
    name: "Smaran Raut",
    title: "SEO Specialist & Web Developer",
    entity: "Smaran Raut SEO & Web Development",
    tagline: "SEO-Optimized Business Websites, Search Growth & Website Maintenance",
    phone: "+977 9714539838",
    whatsapp: "+977 9714539838",
    email: "contact@smaranraut.com.np",
    website: "https://smaran-seo.netlify.app",
    address: {
      streetAddress: "Itahari Chowk, middle of Janta Galli",
      addressLocality: "Itahari",
      addressRegion: "Koshi Province",
      postalCode: "56705",
      addressCountry: "NP"
    },
    geo: {
      latitude: "26.661694",
      longitude: "87.275194"
    },
    openingHours: "Mo-Fr 09:00-18:00, Sa 10:00-15:00",
    regulators: [
      {
        name: "Office of the Company Registrar (OCR)",
        body: "Ministry of Industry, Commerce and Supplies, Nepal",
        role: "Corporate Registration & Commercial Compliance"
      },
      {
        name: "Inland Revenue Department (IRD)",
        body: "Ministry of Finance, Government of Nepal",
        role: "Income Tax (PAN/VAT Act 2058) Compliance"
      },
      {
        name: "Nepal Telecommunications Authority (NTA)",
        body: "Ministry of Communication and Information Technology",
        role: "ICT Standards & Cyber Security Directives"
      },
      {
        name: "Advertising Board of Nepal (Vigyapan Board)",
        body: "Government of Nepal",
        role: "Digital Advertisement Code of Conduct 2076"
      },
      {
        name: "Computer Association of Nepal (CAN Federation)",
        body: "National ICT Apex Body",
        role: "Professional Ethical Code & Standards"
      }
    ],
    social: {
      linkedin: "https://linkedin.com/in/smaranraut",
      twitter: "https://twitter.com/smaranraut",
      github: "https://github.com/smaranraut"
    }
  },

  services: [
    {
      slug: "seo-optimized-web-development",
      title: "SEO-Optimized Business Website Development",
      shortTitle: "SEO Web Development",
      h1: "SEO-Optimized Business Website Development in Nepal",
      metaTitle: "SEO-Optimized Business Website Development | Fast & Mobile Ready | Smaran Raut",
      metaDesc: "Custom business websites built from the ground up for search visibility, fast mobile loading, clean code, and practical inquiry generation.",
      directAnswer: "SEO-optimized business website development builds clean, mobile-ready websites designed from day one to be easily read by search engines. Instead of relying on heavy plugins, we build structured pages with fast loading speeds, simple navigation, and clear contact options for your customers.",
      calculatorId: "webdev-budget-calculator",
      calculatorName: "Website Project Estimator",
      parentSlug: null,
      faqs: [
        {
          q: "What makes an SEO-optimized website different from a regular website?",
          a: "An SEO-optimized website is built with clean HTML, fast loading speeds, proper heading structure, mobile responsiveness, and search engine tags built into every page, making it much easier for Google to index and rank."
        },
        {
          q: "Can I update content on the website myself?",
          a: "Yes. We set up straightforward content controls so you can easily update text, add new services, publish articles, or change contact details without touching code."
        },
        {
          q: "How long does it take to build a complete business website?",
          a: "Most standard business websites take between 2 to 4 weeks depending on the number of pages, custom features, and content readiness."
        }
      ]
    },
    {
      slug: "local-seo-itahari",
      title: "Local SEO & Google Business Profile Services",
      shortTitle: "Local SEO Itahari",
      h1: "Local SEO & Google Business Profile Optimization in Itahari & Eastern Nepal",
      metaTitle: "Local SEO in Itahari & Eastern Nepal | Google Maps Visibility | Smaran Raut",
      metaDesc: "Improve your business visibility on Google Maps and local search results across Itahari, Dharan, and Biratnagar with clear local SEO steps.",
      directAnswer: "Local SEO helps local businesses in Itahari, Dharan, and Biratnagar appear when nearby customers search on Google and Google Maps. We optimize your Google Business Profile, ensure your business address and phone number are consistent across online listings, and add local business schema tags to your website.",
      calculatorId: "local-seo-calculator",
      calculatorName: "Local Search Visibility Checklist",
      parentSlug: null,
      faqs: [
        {
          q: "How does Local SEO help my business in Itahari?",
          a: "When people in Itahari search for services like 'hardware shop near me' or 'dental clinic in Itahari', local SEO helps your business appear in the top Google Maps results and local search listings."
        },
        {
          q: "What is needed to verify my Google Business Profile in Nepal?",
          a: "You need a physical business address in Nepal, your registered business name, phone number, clear photos of your storefront signboard, and official registration documents if requested by Google."
        },
        {
          q: "Do you serve businesses in Dharan and Biratnagar as well?",
          a: "Yes. We work with businesses throughout Sunsari, Morang, and the broader Koshi Province region."
        }
      ]
    },
    {
      slug: "technical-seo-audit",
      title: "SEO Audits for Existing Websites",
      shortTitle: "Website SEO Audit",
      h1: "Comprehensive SEO Audits for Existing Business Websites",
      metaTitle: "SEO Audit for Existing Websites Nepal | Technical & On-Page Review | Smaran Raut",
      metaDesc: "Identify indexing issues, broken links, slow loading pages, and missing search tags with a practical, step-by-step SEO website audit.",
      directAnswer: "An SEO audit for an existing website is a thorough checkup that identifies why your site may not be ranking well on Google. We inspect crawl errors, missing page titles, broken links, slow loading pages, duplicate content, and mobile usability issues, providing a clear list of fixes.",
      calculatorId: "seo-roi-calculator",
      calculatorName: "SEO Opportunity Estimator",
      parentSlug: null,
      faqs: [
        {
          q: "Why does my existing website not show up on Google?",
          a: "Common reasons include search engine indexing blocks, missing meta titles, broken links, duplicate content, slow loading speeds, or lack of clear topic content that matches what customers are searching for."
        },
        {
          q: "What do I receive after the SEO audit?",
          a: "You receive an actionable report with prioritized recommendations: high-priority technical fixes, content improvements, and a practical step-by-step roadmap to improve rankings."
        }
      ]
    },
    {
      slug: "core-web-vitals-speed",
      title: "Website Maintenance & Speed Improvements",
      shortTitle: "Speed & Maintenance",
      h1: "Website Maintenance, Mobile Optimization & Speed Improvements",
      metaTitle: "Website Maintenance & Speed Optimization Nepal | Mobile Fast | Smaran Raut",
      metaDesc: "Fix slow page loading, resolve mobile display issues, clean up technical errors, and keep your website running smoothly and securely.",
      directAnswer: "Website maintenance and speed improvement keeps your website fast, secure, and user-friendly. We optimize oversized images, fix broken layouts on mobile screens, update outdated software, and resolve browser warnings to ensure your visitors have a smooth experience.",
      calculatorId: "cwv-speed-calculator",
      calculatorName: "Page Speed Impact Calculator",
      parentSlug: null,
      faqs: [
        {
          q: "Why is website speed important for SEO?",
          a: "Google uses page loading speed and mobile responsiveness as ranking factors. When pages load slowly on mobile devices, visitors leave quickly, resulting in lost inquiries and lower search rankings."
        },
        {
          q: "Can you fix an existing slow WordPress or custom website?",
          a: "Yes. We optimize image formats, remove unused scripts and plugins, configure browser caching, and clean up code to significantly speed up existing websites."
        }
      ]
    },
    {
      slug: "ecommerce-seo-nepal",
      title: "E-Commerce SEO & Product Optimization",
      shortTitle: "E-Commerce SEO",
      h1: "E-Commerce SEO & Product Category Search Optimization",
      metaTitle: "E-Commerce SEO Nepal | Product & Category Search Growth | Smaran Raut",
      metaDesc: "Help your online store products get discovered on Google with structured product data, optimized category pages, and clean website navigation.",
      directAnswer: "E-commerce SEO optimizes online retail stores so individual products and category pages rank when buyers search on Google. We configure structured product pricing tags, optimize category navigation, and eliminate duplicate filter links.",
      calculatorId: "ecommerce-loss-calculator",
      calculatorName: "Online Store Potential Simulator",
      parentSlug: null,
      faqs: [
        {
          q: "How does SEO help online shopping websites?",
          a: "It allows people searching for specific products, brands, or categories to land directly on your product pages rather than relying solely on paid advertisements."
        }
      ]
    },
    {
      slug: "semantic-content-strategy",
      title: "Content Planning & On-Page SEO",
      shortTitle: "Content Strategy",
      h1: "Search-Focused Content Planning & On-Page Optimization",
      metaTitle: "Content Planning & On-Page SEO Nepal | Helpful Content Guide | Smaran Raut",
      metaDesc: "Create clear, helpful content that answers your customers' questions, establishes business authority, and ranks reliably on search engines.",
      directAnswer: "Content planning and on-page SEO helps you structure your website's articles and service pages around questions your customers actually ask. We organize topics logically, write direct answers to common questions, and link related pages together.",
      calculatorId: "topical-gap-calculator",
      calculatorName: "Content Completeness Checker",
      parentSlug: null,
      faqs: [
        {
          q: "Why is helpful content important for Google ranking?",
          a: "Google actively rewards websites that provide accurate, helpful answers to search queries. Publishing clear guides that help users builds trust and long-term search visibility."
        }
      ]
    },
    {
      slug: "enterprise-link-building",
      title: "Ongoing Website Management & Search Growth",
      shortTitle: "Ongoing Management",
      h1: "Ongoing Website Management & Search Visibility Growth",
      metaTitle: "Ongoing Website Management Nepal | Search Monitoring & Growth | Smaran Raut",
      metaDesc: "Keep your website updated, monitor search ranking changes, add new service pages, and grow your digital presence month by month.",
      directAnswer: "Ongoing website management provides continuous support to ensure your website stays up to date, secure, and competitive in search results. We monitor your search performance in Google Search Console, resolve new crawl issues, and periodically update content.",
      calculatorId: "seo-roi-calculator",
      calculatorName: "Ongoing Growth Simulator",
      parentSlug: null,
      faqs: [
        {
          q: "What is included in ongoing website management?",
          a: "Routine security checks, monthly performance reports, fixing broken links, adding new service pages or blog updates, and tracking keyword visibility in Google Search Console."
        }
      ]
    }
  ],

  clusterArticles: [
    {
      slug: "website-setup-and-management",
      title: "Website Setup & Management Guide: Domains, Hosting, Launch & Maintenance",
      h1: "Website Setup & Management: Plain-English Guide to Domains, Hosting, Launch & Care",
      parentSlug: "services",
      parentName: "Services Overview",
      intent: "Educational",
      metaTitle: "Website Setup & Management Guide | Domains, Hosting & Care | Smaran Raut",
      metaDesc: "A plain-English guide to domain registration, website hosting, launch procedures, and ongoing website maintenance for business owners.",
      directAnswer: "Launching and managing a business website involves registering your digital address (domain), renting secure server space (hosting), verifying and connecting files before launch, and keeping the website fast, secure, and up to date over time.",
      readTime: "8 min read"
    },
    {
      slug: "seo-services-explained",
      title: "SEO Services Explained: Plain-English Guide to What Each Service Does",
      h1: "SEO Services Explained: What Each Service Does and How It Helps Your Business",
      parentSlug: "services",
      parentName: "Services Overview",
      intent: "Educational",
      metaTitle: "SEO Services Explained | Plain-English SEO Guide | Smaran Raut",
      metaDesc: "Understand keyword research, content optimization, site speed improvements, technical audits, search performance reviews, and local business SEO.",
      directAnswer: "Search engine optimization helps your business appear when customers search on Google. Core services include finding customer search terms (keywords), improving page text, speeding up mobile loading, and verifying technical indexing health.",
      readTime: "10 min read"
    },
    {
      slug: "social-media-and-online-advertising",
      title: "Social Media and Online Advertising: Ads, Google Profile & Google Maps",
      h1: "Social Media and Online Advertising: How Ads, Google Business Profile & Google Maps Drive Customers",
      parentSlug: "services",
      parentName: "Services Overview",
      intent: "Educational",
      metaTitle: "Social Media & Online Ads Guide | Maps & Local Growth | Smaran Raut",
      metaDesc: "Learn how Facebook and Instagram ads, Google Business Profile setup, and Google Maps visibility attract ready-to-buy customers in your area.",
      directAnswer: "Combining targeted social media ads on Facebook and Instagram with an optimized Google Business Profile and prominent Google Maps rankings enables local businesses to reach both active searchers and social media users nearby.",
      readTime: "7 min read"
    },
    {
      slug: "google-business-profile-optimization-nepal",
      title: "Google Business Profile Optimization Guide for Nepali Businesses",
      h1: "How to Optimize Your Google Business Profile for Better Local Visibility in Nepal",
      parentSlug: "local-seo-itahari",
      parentName: "Local SEO & Google Business Profile Services",
      intent: "Procedural",
      metaTitle: "Google Business Profile Optimization Nepal | Step-by-Step Guide",
      metaDesc: "Step-by-step guide to verify, set up, and optimize your Google Business Profile for better visibility in Itahari, Dharan, and across Nepal.",
      directAnswer: "Optimizing a Google Business Profile in Nepal requires selecting the right primary business category, providing an accurate physical address and phone number, completing verification, uploading clear photos of your business, and collecting honest customer reviews.",
      readTime: "7 min read"
    },
    {
      slug: "local-citations-nap-consistency-guide",
      title: "Local Citations & NAP Consistency: Keeping Business Information Accurate",
      h1: "NAP Consistency: Keeping Your Name, Address, and Phone Number Accurate Online",
      parentSlug: "local-seo-itahari",
      parentName: "Local SEO & Google Business Profile Services",
      intent: "Definitional & Procedural",
      metaTitle: "Local Citations & NAP Consistency Nepal | Local SEO Guide",
      metaDesc: "Learn why matching Name, Address, and Phone (NAP) details across directories and map listings helps Google trust your local business location.",
      directAnswer: "NAP consistency means ensuring your business Name, Address, and Phone number are written exactly the same way across every website, directory, and social media profile. When information is consistent, Google can confidently show your business to nearby customers.",
      readTime: "6 min read"
    },
    {
      slug: "multi-location-seo-eastern-nepal",
      title: "Local SEO for Multiple Branches in Eastern Nepal",
      h1: "Managing Local SEO for Businesses with Multiple Branches in Eastern Nepal",
      parentSlug: "local-seo-itahari",
      parentName: "Local SEO & Google Business Profile Services",
      intent: "Strategic",
      metaTitle: "Multi-Location SEO Eastern Nepal | Itahari Dharan Biratnagar",
      metaDesc: "Practical advice on managing Google Business Profiles and location pages for businesses with branches in Itahari, Dharan, and Biratnagar.",
      directAnswer: "Managing local SEO for multiple branches requires creating dedicated, helpful pages on your website for each physical location, verifying a separate Google Business Profile for each branch with its local phone number, and listing accurate opening hours.",
      readTime: "8 min read"
    },
    {
      slug: "local-seo-vs-organic-seo-differences",
      title: "Local SEO vs. Regular Organic SEO: What Does Your Business Need?",
      h1: "Local SEO vs. Regular SEO: Understanding the Difference for Your Business",
      parentSlug: "local-seo-itahari",
      parentName: "Local SEO & Google Business Profile Services",
      intent: "Comparative",
      metaTitle: "Local SEO vs Regular SEO Differences | Practical Guide",
      metaDesc: "Understand whether your business needs local Google Maps optimization, national search visibility, or a combination of both.",
      directAnswer: "Local SEO focuses on helping local customers find your physical business or service area in Google Maps, while regular SEO helps your website rank for general informational or national search queries regardless of physical location.",
      readTime: "5 min read"
    },

    {
      slug: "nextjs-vs-wordpress-for-seo",
      title: "Choosing Between Modern Frameworks and WordPress for Your Business Website",
      h1: "Next.js vs. WordPress: Choosing the Right Foundation for Your Website",
      parentSlug: "seo-optimized-web-development",
      parentName: "SEO-Optimized Business Website Development",
      intent: "Decision-Making",
      metaTitle: "Next.js vs WordPress for Business Websites | Practical Comparison",
      metaDesc: "A straightforward comparison of modern static web development versus WordPress for speed, maintenance, security, and search performance.",
      directAnswer: "Modern static websites load almost instantly because pages are pre-rendered into simple HTML files without database delays. WordPress offers easy editing with many templates, but requires ongoing updates, caching plugins, and maintenance to stay fast and secure.",
      readTime: "8 min read"
    },
    {
      slug: "mobile-first-responsive-design-checklist",
      title: "Mobile-Friendly Website Checklist for Business Owners",
      h1: "Mobile-Friendly Website Checklist: Ensuring Great Mobile User Experience",
      parentSlug: "seo-optimized-web-development",
      parentName: "SEO-Optimized Business Website Development",
      intent: "Checklist",
      metaTitle: "Mobile-Friendly Website Checklist | Mobile Usability Guide",
      metaDesc: "Simple checklist to make sure your website is easy to read, fast to load, and convenient to navigate on smartphones.",
      directAnswer: "A mobile-friendly website loads quickly on mobile data, fits cleanly on all screen sizes without horizontal scrolling, uses legible text without zooming, and has large, easy-to-tap buttons for calling or sending an inquiry.",
      readTime: "6 min read"
    },
    {
      slug: "static-site-generation-benefits-ranking",
      title: "Why Fast, Pre-Rendered Websites Perform Better Online",
      h1: "Why Pre-Rendered, Fast Websites Provide Better User Experience and Search Results",
      parentSlug: "seo-optimized-web-development",
      parentName: "SEO-Optimized Business Website Development",
      intent: "Definitional",
      metaTitle: "Benefits of Pre-Rendered Websites | Fast Speed & Reliability",
      metaDesc: "Learn how pre-rendered web pages deliver instant loading, reliable uptime, and better mobile search experiences.",
      directAnswer: "Pre-rendered websites generate complete HTML pages ahead of time. When a visitor or search engine crawler clicks your link, the server sends the ready-made page immediately in milliseconds without waiting for database queries.",
      readTime: "6 min read"
    },
    {
      slug: "schema-markup-implementation-guide",
      title: "Understanding Schema Markup and Rich Snippets for Local Businesses",
      h1: "How to Add Schema Structured Data to Your Business Website",
      parentSlug: "seo-optimized-web-development",
      parentName: "SEO-Optimized Business Website Development",
      intent: "Procedural",
      metaTitle: "Schema Markup Guide for Local Business Websites | Step-by-Step",
      metaDesc: "Simple guide to adding structured data tags so search engines can clearly understand your business address, phone number, and services.",
      directAnswer: "Schema markup is a standard code format (JSON-LD) placed in your website's code that tells search engines exactly what your business is, your official phone number, physical address, opening hours, and services in a language computers understand.",
      readTime: "7 min read"
    },

    {
      slug: "how-to-conduct-technical-seo-audit",
      title: "How to Check Your Website for Technical SEO Issues",
      h1: "How to Perform an SEO Checkup on an Existing Website",
      parentSlug: "technical-seo-audit",
      parentName: "SEO Audits for Existing Websites",
      intent: "Procedural",
      metaTitle: "How to Conduct a Website SEO Checkup | Practical Step-by-Step",
      metaDesc: "Learn how to find and fix common website problems like broken links, slow pages, duplicate titles, and indexing errors.",
      directAnswer: "A website SEO checkup involves checking your site in Google Search Console, testing page speed on mobile devices, finding and fixing broken 404 links, ensuring every page has a unique title and description, and confirming pages are properly indexed.",
      readTime: "8 min read"
    },
    {
      slug: "crawl-budget-optimization-large-sites",
      title: "Making Sure Search Engines Can Find All Your Important Pages",
      h1: "How to Help Google Discover and Index Your Business Pages",
      parentSlug: "technical-seo-audit",
      parentName: "SEO Audits for Existing Websites",
      intent: "Strategic",
      metaTitle: "Helping Google Index Your Pages | Search Indexing Basics",
      metaDesc: "Ensure search engine crawlers spend time reading your main service and product pages rather than broken or duplicate URLs.",
      directAnswer: "Helping search engines index your website effectively means keeping your XML sitemap clean, removing broken links, avoiding duplicate filter pages, and ensuring your main service pages are linked clearly from your navigation menus.",
      readTime: "7 min read"
    },
    {
      slug: "fixing-canonical-tag-issues-pagination",
      title: "Preventing Duplicate Content Issues on Your Website",
      h1: "How to Prevent Duplicate Content Confusion with Canonical Tags",
      parentSlug: "technical-seo-audit",
      parentName: "SEO Audits for Existing Websites",
      intent: "Technical",
      metaTitle: "Preventing Duplicate Content | Canonical Tag Basics",
      metaDesc: "Learn how canonical tags tell Google which version of a webpage is the primary one when similar URLs exist.",
      directAnswer: "Canonical tags tell search engines which URL is the main, official version of a page when duplicate or similar versions exist (such as with sorting filters or tracking parameters), preventing confusion and divided search rankings.",
      readTime: "6 min read"
    },
    {
      slug: "https-ssl-security-seo-impact",
      title: "Why HTTPS and Website Security Matter for Business Trust and Search",
      h1: "Website Security (HTTPS) and Its Importance for Business Reputation and SEO",
      parentSlug: "technical-seo-audit",
      parentName: "SEO Audits for Existing Websites",
      intent: "Security",
      metaTitle: "Website Security & HTTPS for Small Business | Security Basics",
      metaDesc: "Understand why having an active SSL certificate (HTTPS) is essential for user trust, protecting inquiries, and search rankings.",
      directAnswer: "HTTPS encrypts the communication between your visitor's browser and your website, keeping contact form details safe and preventing warning messages in modern browsers. Google also uses HTTPS as a standard security signal.",
      readTime: "5 min read"
    },

    {
      slug: "ecommerce-product-schema-rich-snippets",
      title: "Setting Up Product Schema for Online Store Items",
      h1: "How to Add Product Schema Markup to Your Online Store",
      parentSlug: "ecommerce-seo-nepal",
      parentName: "E-Commerce SEO & Product Optimization",
      intent: "Procedural",
      metaTitle: "Product Schema Markup for Online Stores | Simple Guide",
      metaDesc: "Help your products display star ratings, price tags, and in-stock badges directly in Google search results.",
      directAnswer: "Product schema markup includes structured details about your item—such as name, price in NPR, availability status, and customer reviews—so Google can display helpful shopping snippets directly in search results.",
      readTime: "7 min read"
    },
    {
      slug: "handling-faceted-navigation-duplicate-content",
      title: "Managing Product Filters on Online Stores Without Confusing Google",
      h1: "Managing Product Filter Links on E-Commerce Websites",
      parentSlug: "ecommerce-seo-nepal",
      parentName: "E-Commerce SEO & Product Optimization",
      intent: "Problem-Solving",
      metaTitle: "Managing E-Commerce Product Filters | SEO Best Practices",
      metaDesc: "Keep your online store filter navigation convenient for shoppers while avoiding thousands of duplicate search URLs.",
      directAnswer: "Managing product filters effectively means letting shoppers filter by size, color, and price while pointing canonical tags back to the main category page so search engines focus on ranking your primary categories.",
      readTime: "7 min read"
    },
    {
      slug: "optimizing-shopify-woocommerce-performance",
      title: "Simple Steps to Speed Up Shopify and WooCommerce Stores",
      h1: "How to Make Your Shopify or WooCommerce Store Load Faster",
      parentSlug: "ecommerce-seo-nepal",
      parentName: "E-Commerce SEO & Product Optimization",
      intent: "Procedural",
      metaTitle: "Speed Up Shopify & WooCommerce Stores | Practical Guide",
      metaDesc: "Practical tips to reduce store loading time, remove unused apps, optimize product photos, and improve checkout rates.",
      directAnswer: "You can speed up an online store by compressing oversized product photos, removing unused apps and plugins, avoiding excessive popup widgets, and using a clean, lightweight store theme.",
      readTime: "6 min read"
    },
    {
      slug: "ecommerce-category-page-seo-strategy",
      title: "How to Organize Online Store Category Pages for Better Discovery",
      h1: "Building Clear, User-Friendly Category Pages on Online Stores",
      parentSlug: "ecommerce-seo-nepal",
      parentName: "E-Commerce SEO & Product Optimization",
      intent: "Strategic",
      metaTitle: "E-Commerce Category Page Guide | Organization & Search",
      metaDesc: "Help customers and search engines find what they are looking for by organizing product categories with clear descriptions.",
      directAnswer: "Well-organized category pages feature helpful descriptions explaining the category, clear links to sub-categories, intuitive sorting options, and high-quality product images with clear titles and prices.",
      readTime: "6 min read"
    },

    {
      slug: "topical-authority-clustering-framework",
      title: "Organizing Website Content Logically with Pillar and Cluster Pages",
      h1: "How to Organize Your Website Content Around Core Business Topics",
      parentSlug: "semantic-content-strategy",
      parentName: "Content Planning & On-Page SEO",
      intent: "Strategic",
      metaTitle: "Organizing Website Content Around Core Topics | Planning Guide",
      metaDesc: "Learn how grouping related articles around main service pillars helps your visitors find answers and improves your search presence.",
      directAnswer: "Content grouping connects a main comprehensive service page with several focused, helpful articles answering specific questions about that service. When these pages link to each other naturally, visitors can easily explore the topic.",
      readTime: "7 min read"
    },
    {
      slug: "entity-based-seo-google-knowledge-graph",
      title: "Helping Search Engines Understand What Your Business Does",
      h1: "Helping Search Engines Accurately Understand Your Business Entity",
      parentSlug: "semantic-content-strategy",
      parentName: "Content Planning & On-Page SEO",
      intent: "Definitional",
      metaTitle: "Helping Search Engines Understand Your Business | Entity Basics",
      metaDesc: "How modern search engines connect your business name, location, owner, and services as a recognized local organization.",
      directAnswer: "Modern search engines recognize businesses as real-world entities. By providing consistent details about your business name, address, services, and official social profiles, you help Google clearly understand what you do and where you operate.",
      readTime: "6 min read"
    },
    {
      slug: "search-intent-matching-content-briefs",
      title: "Writing Website Content That Answers Customer Questions",
      h1: "How to Write Helpful Content That Matches What Customers Are Searching For",
      parentSlug: "semantic-content-strategy",
      parentName: "Content Planning & On-Page SEO",
      intent: "Procedural",
      metaTitle: "Writing Content That Answers Customer Questions | Practical Guide",
      metaDesc: "Learn how to write straightforward website content that directly answers customer questions and encourages inquiries.",
      directAnswer: "Writing for search intent means understanding what a person really wants when they search. If they are looking for a service price, provide clear pricing ranges; if they are asking a how-to question, provide direct, easy-to-follow steps.",
      readTime: "6 min read"
    },
    {
      slug: "how-to-update-decaying-content",
      title: "How to Refresh and Update Outdated Articles on Your Website",
      h1: "How to Update Old Website Articles to Keep Information Fresh and Helpful",
      parentSlug: "semantic-content-strategy",
      parentName: "Content Planning & On-Page SEO",
      intent: "Procedural",
      metaTitle: "How to Refresh Outdated Website Articles | Maintenance Guide",
      metaDesc: "Keep your website trustworthy and helpful by updating outdated prices, contact info, statistics, and advice on older pages.",
      directAnswer: "To refresh older content, review pages that have dropped in traffic, update outdated contact information or prices, add answers to new customer questions, improve clarity, and ensure all internal links work properly.",
      readTime: "6 min read"
    },

    {
      slug: "inp-interaction-to-next-paint-guide",
      title: "Understanding Interaction to Next Paint (INP) and Page Responsiveness",
      h1: "What Is INP and How to Make Your Website Feel Fast and Responsive",
      parentSlug: "core-web-vitals-speed",
      parentName: "Website Maintenance & Speed Improvements",
      intent: "Technical",
      metaTitle: "Understanding INP & Page Responsiveness | Website Speed Basics",
      metaDesc: "A straightforward guide to making sure buttons, mobile menus, and forms react instantly without annoying delays.",
      directAnswer: "Interaction to Next Paint (INP) measures how quickly a page responds on screen when a user clicks a button, opens a menu, or fills a form. Fast responsiveness ensures users never wonder whether their tap registered.",
      readTime: "7 min read"
    },
    {
      slug: "lcp-optimization-hero-images-fonts",
      title: "How to Make Your Main Page Content Load Faster on Mobile",
      h1: "How to Speed Up Above-the-Fold Loading Times on Mobile Devices",
      parentSlug: "core-web-vitals-speed",
      parentName: "Website Maintenance & Speed Improvements",
      intent: "Procedural",
      metaTitle: "Speed Up Above-the-Fold Loading on Mobile | Speed Tips",
      metaDesc: "Simple techniques to make your website's main headline and banner image appear quickly on mobile internet connections.",
      directAnswer: "Speeding up above-the-fold loading involves optimizing the main hero banner image, avoiding heavy video backgrounds, loading critical text styles immediately, and using modern image formats like WebP.",
      readTime: "6 min read"
    },
    {
      slug: "cls-cumulative-layout-shift-fixes",
      title: "Preventing Layout Shifts: Stopping Content from Jumping Around While Loading",
      h1: "How to Stop Webpage Content from Jumping While Loading",
      parentSlug: "core-web-vitals-speed",
      parentName: "Website Maintenance & Speed Improvements",
      intent: "Problem-Solving",
      metaTitle: "Fixing Webpage Layout Shifts | Simple Usability Guide",
      metaDesc: "Learn how declaring dimensions for images and reserving space for banners prevents annoying page jumps on mobile.",
      directAnswer: "Layout shifts happen when images, fonts, or notices load without reserved space, causing text to suddenly jump down as someone is reading. Declaring image dimensions and reserving container sizes eliminates this issue.",
      readTime: "5 min read"
    },
    {
      slug: "image-compression-avif-webp-delivery",
      title: "Using Modern Image Formats (WebP and AVIF) to Reduce Page Weight",
      h1: "How Modern Image Formats Help Your Website Load Faster on Mobile",
      parentSlug: "core-web-vitals-speed",
      parentName: "Website Maintenance & Speed Improvements",
      intent: "Technical",
      metaTitle: "Modern Image Formats WebP & AVIF | Image Optimization Guide",
      metaDesc: "Learn how switching from older JPEGs to WebP and AVIF formats cuts image file sizes in half while keeping photos sharp.",
      directAnswer: "Modern image formats like WebP and AVIF compress photographs into much smaller file sizes than traditional JPEG or PNG files without noticeable loss in quality, saving mobile data and dramatically speeding up page loading.",
      readTime: "6 min read"
    },

    {
      slug: "white-hat-link-building-tactics-2026",
      title: "Building Real Website Authority Through Helpful Online Resources",
      h1: "How to Earn Genuine Citations and Build Website Authority Ethically",
      parentSlug: "enterprise-link-building",
      parentName: "Ongoing Website Management & Search Growth",
      intent: "Strategic",
      metaTitle: "Building Website Authority Ethically | Sustainable Online Growth",
      metaDesc: "Discover safe, ethical ways to build website reputation through helpful guides, local community partnerships, and industry citations.",
      directAnswer: "Building genuine website authority comes from publishing helpful guides, tools, and local resources that other websites, community blogs, and local organizations naturally reference and link to.",
      readTime: "7 min read"
    },
    {
      slug: "anchor-text-distribution-best-practices",
      title: "Best Practices for Clear, Natural Link Text Across Your Website",
      h1: "How to Use Natural, Descriptive Link Text on Your Website",
      parentSlug: "enterprise-link-building",
      parentName: "Ongoing Website Management & Search Growth",
      intent: "Technical",
      metaTitle: "Natural Link Text Best Practices | Clear Navigation Guide",
      metaDesc: "Learn why using clear, natural anchor text helps both visitors and search engines understand what linked pages are about.",
      directAnswer: "Good link text describes clearly what the visitor will find on the linked page (e.g. 'read our local SEO guide') instead of repetitive keyword stuffing or generic 'click here' links.",
      readTime: "6 min read"
    },
    {
      slug: "toxic-backlink-audit-disavow-guide",
      title: "Understanding Spam Links: What Business Owners Need to Know",
      h1: "What Business Owners Should Know About Unsolicited Spam Links",
      parentSlug: "enterprise-link-building",
      parentName: "Ongoing Website Management & Search Growth",
      intent: "Decision-Making",
      metaTitle: "Understanding Spam Links & Disavow | Practical Advice",
      metaDesc: "Learn how Google handles random spam backlinks automatically, and when manual intervention is actually necessary.",
      directAnswer: "Google's automated systems automatically identify and ignore most spam scraper links without penalizing your site. Manual disavow files are only needed in rare cases where artificial paid link schemes were intentionally used in the past.",
      readTime: "5 min read"
    },
    {
      slug: "competitor-backlink-gap-analysis",
      title: "Finding Directory and Citation Opportunities in Your Local Area",
      h1: "How to Find Relevant Local Directory and Citation Opportunities",
      parentSlug: "enterprise-link-building",
      parentName: "Ongoing Website Management & Search Growth",
      intent: "Procedural",
      metaTitle: "Finding Local Directory & Citation Opportunities | Local Guide",
      metaDesc: "Step-by-step approach to identifying reputable local business directories, community portals, and industry listings.",
      directAnswer: "Finding local citation opportunities involves looking at reputable Nepali business portals, local trade associations in Koshi Province, and community directories where similar established businesses are listed, and submitting your accurate business details.",
      readTime: "7 min read"
    }
  ],

  locations: [
    { city: "Itahari", slug: "seo-expert-itahari", district: "Sunsari", h1: "No.1 SEO Expert in Itahari, Nepal - Smaran Raut", title: "SEO Expert in Itahari, Nepal - Smaran Raut" },
    { city: "Dharan", slug: "seo-expert-dharan", district: "Sunsari", h1: "No.1 SEO Expert in Dharan, Nepal - Smaran Raut", title: "SEO Expert in Dharan, Nepal - Smaran Raut" },
    { city: "Biratnagar", slug: "seo-expert-biratnagar", district: "Morang", h1: "No.1 SEO Expert in Biratnagar, Nepal - Smaran Raut", title: "SEO Expert in Biratnagar, Nepal - Smaran Raut" },
    { city: "Duhabi", slug: "seo-expert-duhabi", district: "Sunsari", h1: "No.1 SEO Expert in Duhabi, Nepal - Smaran Raut", title: "SEO Expert in Duhabi, Nepal - Smaran Raut" },
    { city: "Inaruwa", slug: "seo-expert-inaruwa", district: "Sunsari", h1: "No.1 SEO Expert in Inaruwa, Nepal - Smaran Raut", title: "SEO Expert in Inaruwa, Nepal - Smaran Raut" },
    { city: "Jhumka", slug: "seo-expert-jhumka", district: "Sunsari", h1: "No.1 SEO Expert in Jhumka, Nepal - Smaran Raut", title: "SEO Expert in Jhumka, Nepal - Smaran Raut" },
    { city: "Ramdhuni", slug: "seo-expert-ramdhuni", district: "Sunsari", h1: "No.1 SEO Expert in Ramdhuni, Nepal - Smaran Raut", title: "SEO Expert in Ramdhuni, Nepal - Smaran Raut" },
    { city: "Belbari", slug: "seo-expert-belbari", district: "Morang", h1: "No.1 SEO Expert in Belbari, Nepal - Smaran Raut", title: "SEO Expert in Belbari, Nepal - Smaran Raut" },
    { city: "Dhankuta", slug: "seo-expert-dhankuta", district: "Dhankuta", h1: "No.1 SEO Expert in Dhankuta, Nepal - Smaran Raut", title: "SEO Expert in Dhankuta, Nepal - Smaran Raut" },
    { city: "Rangeli", slug: "seo-expert-rangeli", district: "Morang", h1: "No.1 SEO Expert in Rangeli, Nepal - Smaran Raut", title: "SEO Expert in Rangeli, Nepal - Smaran Raut" },
    { city: "Urlabari", slug: "seo-expert-urlabari", district: "Morang", h1: "No.1 SEO Expert in Urlabari, Nepal - Smaran Raut", title: "SEO Expert in Urlabari, Nepal - Smaran Raut" },
    { city: "Damak", slug: "seo-expert-damak", district: "Jhapa", h1: "No.1 SEO Expert in Damak, Nepal - Smaran Raut", title: "SEO Expert in Damak, Nepal - Smaran Raut" },
    { city: "Gaighat", slug: "seo-expert-gaighat", district: "Udayapur", h1: "No.1 SEO Expert in Gaighat, Nepal - Smaran Raut", title: "SEO Expert in Gaighat, Nepal - Smaran Raut" },
    { city: "Rajbiraj", slug: "seo-expert-rajbiraj", district: "Saptari", h1: "No.1 SEO Expert in Rajbiraj, Nepal - Smaran Raut", title: "SEO Expert in Rajbiraj, Nepal - Smaran Raut" },
    { city: "Birtamod", slug: "seo-expert-birtamod", district: "Jhapa", h1: "No.1 SEO Expert in Birtamod, Nepal - Smaran Raut", title: "SEO Expert in Birtamod, Nepal - Smaran Raut" },
    { city: "Lahan", slug: "seo-expert-lahan", district: "Siraha", h1: "No.1 SEO Expert in Lahan, Nepal - Smaran Raut", title: "SEO Expert in Lahan, Nepal - Smaran Raut" },
    { city: "Ilam", slug: "seo-expert-ilam", district: "Ilam", h1: "No.1 SEO Expert in Ilam, Nepal - Smaran Raut", title: "SEO Expert in Ilam, Nepal - Smaran Raut" }
  ],

  trustPages: [
    {
      slug: "about-us",
      title: "About Smaran Raut | SEO & Web Developer in Itahari",
      h1: "About Smaran Raut: Building Search-Friendly Websites & Digital Growth",
      metaTitle: "About Smaran Raut | SEO & Web Developer in Itahari, Sunsari, Nepal",
      metaDesc: "Learn about Smaran Raut, providing practical SEO services, custom business website development, and website maintenance in Itahari, Nepal.",
      directAnswer: "Smaran Raut is an SEO specialist and web developer based on Main Road, Ward 4, Itahari, Sunsari, Nepal. Smaran helps local businesses build clean, fast, search-optimized websites and improve their visibility on Google and Google Maps through practical, honest digital techniques."
    },
    {
      slug: "contact-us",
      title: "Contact Smaran Raut | SEO & Web Inquiries",
      h1: "Contact Smaran Raut: Let's Discuss Your Website or SEO Project",
      metaTitle: "Contact Smaran Raut | SEO & Web Inquiries in Itahari | Phone & Email",
      metaDesc: "Get in touch for website development, SEO improvements for existing sites, and ongoing maintenance. Response within 24 business hours.",
      directAnswer: "You can reach Smaran Raut directly by email at contact@smaranraut.com.np, by phone or WhatsApp at +977 9714539838, or in person at our office on Main Road, Ward No. 4, Itahari, Sunsari, Koshi Province, Nepal."
    },
    {
      slug: "consultation",
      title: "Schedule a Website & SEO Consultation",
      h1: "Schedule a Consultation to Review Your Website and SEO Goals",
      metaTitle: "Schedule SEO Consultation | Review Your Website with Smaran Raut",
      metaDesc: "Book a consultation to review your current website performance, identify search opportunities, and discuss a clear plan of action.",
      directAnswer: "During a consultation, we examine your current website, discuss your target customers in Itahari, Eastern Nepal, or beyond, and provide clear recommendations on whether you need a new website, technical fixes, or ongoing local SEO management."
    },
    {
      slug: "office-location",
      title: "Office Location & Service Area | Itahari, Sunsari",
      h1: "Office Location: Main Road, Ward 4, Itahari & Eastern Nepal Service Area",
      metaTitle: "Office Location in Itahari | Smaran Raut SEO & Web Development",
      metaDesc: "Visit our office on Main Road, Ward 4, Itahari. Serving businesses in Itahari, Dharan, Biratnagar, and clients across Nepal.",
      directAnswer: "Our physical office is located at Main Road, Ward No. 4, Itahari, Sunsari District, Koshi Province, Nepal (Geo-Coordinates: 26.6646° N, 87.2798° E), open Monday through Friday from 09:00 to 18:00 and Saturday from 10:00 to 15:00."
    },
    {
      slug: "case-studies",
      title: "Client Case Studies & Practical Work Examples",
      h1: "Practical Examples of Our Website Development and SEO Work",
      metaTitle: "Client Work Examples & SEO Case Studies | Smaran Raut",
      metaDesc: "Review practical examples of websites we have built and local search visibility improvements delivered for local businesses in Eastern Nepal.",
      directAnswer: "Our work examples showcase practical results: building fast-loading websites that are easy for customers to navigate, helping local clinics and retail shops establish verified Google Maps listings, and optimizing existing online stores for smoother mobile shopping."
    },
    {
      slug: "disclaimer",
      title: "Professional Service Disclosures & Disclaimer",
      h1: "Professional Service Disclosures & Realistic Search Disclaimer",
      metaTitle: "Service Disclaimer & Disclosures | Smaran Raut SEO",
      metaDesc: "Honest disclosures regarding search engine algorithm independence, realistic expectations, and compliance under Nepalese commercial law.",
      directAnswer: "Smaran Raut operates under Nepalese law in compliance with the Office of the Company Registrar and Inland Revenue Department. Because search engines update their ranking systems independently, ethical SEO guarantees quality technical execution and best practices rather than unrealistic guaranteed ranking positions."
    },
    {
      slug: "editorial-policy",
      title: "Editorial Policy & Information Quality Standards",
      h1: "Editorial Standards: Practical Accuracy and Clear Guidance",
      metaTitle: "Editorial Policy | Smaran Raut SEO & Web Development",
      metaDesc: "Our commitment to publishing clear, accurate, and practical information based on real-world web development experience.",
      directAnswer: "All technical guides published on this website are written to provide accurate, easy-to-understand advice based on official search engine guidelines, web standards, and hands-on development experience."
    },
    {
      slug: "privacy-policy",
      title: "Privacy Policy & Client Data Protection",
      h1: "Privacy Policy: How We Respect and Protect Your Information",
      metaTitle: "Privacy Policy | Smaran Raut SEO & Web Development",
      metaDesc: "How we protect client information in compliance with Nepal's privacy and cyber security regulations.",
      directAnswer: "We treat your inquiry details, website analytics, and contact information with strict confidentiality, using your data only to deliver requested web and SEO services, and never selling or sharing your information with third parties."
    },
    {
      slug: "terms-and-conditions",
      title: "Terms and Conditions of Service",
      h1: "Terms & Conditions: Clear Service Agreements & Payment Policies",
      metaTitle: "Terms and Conditions | Smaran Raut SEO & Web Development",
      metaDesc: "Clear terms governing website projects, scope of work, support periods, and invoicing under Nepal tax compliance.",
      directAnswer: "Our service terms clearly outline the scope of work, transparent three-stage payment structure (advance, development completion balance, and 1-month SEO performance check), and ongoing maintenance under Nepal statutory guidelines."
    },
    {
      slug: "cookie-policy",
      title: "Cookie Usage Policy",
      h1: "Cookie Policy: Transparent and Minimal Website Cookies",
      metaTitle: "Cookie Policy | Smaran Raut SEO & Web Development",
      metaDesc: "Clear information on how this website uses minimal essential performance cookies without invasive tracking.",
      directAnswer: "We use only essential cookies necessary for website performance and remembering form dialog states during your visit. We do not use intrusive cross-site tracking or sell user data."
    }
  ]
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = SITE_DATA;
}
