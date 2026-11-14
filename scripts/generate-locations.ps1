# Location Landing Pages Generator for Smaran Raut SEO Website
$ErrorActionPreference = "Stop"

$rootDir = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

$cities = @(
    @{
        Name = "Itahari"
        Slug = "seo-expert-itahari"
        District = "Sunsari"
        Tagline = "Transport Hub & Commercial Epicenter of Sunsari"
        EcoContext = "As the primary commercial junction of Eastern Nepal connecting the Mahendra and Koshi Highways, Itahari's business landscape is dominated by busy wholesale centers, retail showrooms, private colleges, transport services, and hospitality establishments. Standing out on Google ensures that local shoppers, travelers, and regional clients find your business first."
        IndustryFocus = "Retail showrooms, transport services, educational consultancies, local clinics, and hospitality enterprises"
    },
    @{
        Name = "Dharan"
        Slug = "seo-expert-dharan"
        District = "Sunsari"
        Tagline = "Educational & Healthcare Capital of Eastern Nepal"
        EcoContext = "Famous for BP Koirala Institute of Health Sciences (BPKIHS), dental and medical academies, and its status as the gateway to Bhedetar tourism, Dharan hosts a dense concentration of healthcare clinics, educational consultancies, boutique hotels, cafes, and specialized services that rely heavily on local and regional search discovery."
        IndustryFocus = "Private healthcare clinics, dental practices, educational consultancies, tourism lodges, cafes, and consumer services"
    },
    @{
        Name = "Biratnagar"
        Slug = "seo-expert-biratnagar"
        District = "Morang"
        Tagline = "Provincial Capital & Industrial Metropolis of Koshi"
        EcoContext = "As the capital of Koshi Province and Nepal's second-largest industrial metropolis, Biratnagar is a hub for major manufacturing units, import-export trading houses, large multi-specialty hospitals, corporate offices, and competitive retail markets demanding top-tier search visibility and professional web infrastructure."
        IndustryFocus = "Manufacturing firms, corporate enterprises, multi-specialty hospitals, logistics providers, and B2B commercial suppliers"
    },
    @{
        Name = "Duhabi"
        Slug = "seo-expert-duhabi"
        District = "Sunsari"
        Tagline = "Strategic Industrial & Manufacturing Corridor"
        EcoContext = "Situated along the high-traffic highway corridor between Itahari and Biratnagar, Duhabi is home to prominent industrial manufacturing plants, agro-processing units, heavy machinery workshops, and transport logistics firms that require clean B2B web presences and regional search visibility."
        IndustryFocus = "Manufacturing plants, transport logistics, industrial equipment suppliers, agro-mills, and wholesale distribution"
    },
    @{
        Name = "Inaruwa"
        Slug = "seo-expert-inaruwa"
        District = "Sunsari"
        Tagline = "District Administrative & Agricultural Center"
        EcoContext = "As the administrative headquarters of Sunsari district, Inaruwa is a vital center for government-related professional services, legal consultancies, agricultural commodity trade, and regional retail businesses serving the southern Sunsari rural and semi-urban communities."
        IndustryFocus = "Legal consultancies, agricultural commodity dealers, retail stores, local financial services, and administrative firms"
    },
    @{
        Name = "Jhumka"
        Slug = "seo-expert-jhumka"
        District = "Sunsari"
        Tagline = "Emerging Highway Commercial Market"
        EcoContext = "Positioned centrally along the East-West Highway between Itahari and Inaruwa, Jhumka is an energetic and rapidly growing trading town with expanding agro-vet supplies, hardware stores, community healthcare, and consumer retail businesses benefiting from local search discovery."
        IndustryFocus = "Hardware suppliers, agro-vet stores, local medical clinics, educational centers, and regional retail shops"
    },
    @{
        Name = "Ramdhuni"
        Slug = "seo-expert-ramdhuni"
        District = "Sunsari"
        Tagline = "Historic Cultural Heritage & Emerging Commerce"
        EcoContext = "Encompassing the historic Ramdhuni temple pilgrimage circuit and expanding residential areas, Ramdhuni features growing local commercial retail, hospitality for regional visitors, construction supplies, and agricultural enterprises expanding their digital reach."
        IndustryFocus = "Cultural tourism hospitality, local retail, agro-farming businesses, building materials, and local services"
    },
    @{
        Name = "Belbari"
        Slug = "seo-expert-belbari"
        District = "Morang"
        Tagline = "Northern Morang Highway Commerce Hub"
        EcoContext = "Located on the Mahendra Highway between Itahari and Pathari, Belbari is a thriving municipality centered on agro-enterprises, timber trade, cooperatives, healthcare clinics, and community educational centers seeking greater search discoverability across Morang."
        IndustryFocus = "Community enterprises, timber and hardware supplies, local clinics, agro-processing, and consumer retail"
    },
    @{
        Name = "Dhankuta"
        Slug = "seo-expert-dhankuta"
        District = "Dhankuta"
        Tagline = "Koshi Hill Regional Trade & Agro-Tourism Center"
        EcoContext = "Serving as the historic administrative capital of the eastern hills, Dhankuta is renowned for commercial horticulture (avocado, orange, tea), higher educational institutions, regional hospitals, and eco-tourism that benefit from clean, search-optimized web presences."
        IndustryFocus = "Agro-export enterprises, tea and horticulture businesses, hill tourism lodges, polyclinics, and educational institutions"
    },
    @{
        Name = "Rangeli"
        Slug = "seo-expert-rangeli"
        District = "Morang"
        Tagline = "Historic Agricultural Trade & Border Commerce Town"
        EcoContext = "One of Morang's oldest trading towns, Rangeli anchors southern Morang's agricultural output with prominent rice mills, agricultural machinery dealers, local healthcare, and cross-border commercial trading firms looking to establish digital credibility."
        IndustryFocus = "Rice and flour mills, agricultural equipment dealers, border trading firms, pharmacies, and local retail"
    },
    @{
        Name = "Urlabari"
        Slug = "seo-expert-urlabari"
        District = "Morang"
        Tagline = "Eastern Morang Highway & Medical Junction"
        EcoContext = "Urlabari connects eastern Morang with Jhapa, hosting prominent private hospitals, shopping complexes, educational institutes, and vibrant local retail businesses that draw daily foot traffic and online search queries from surrounding rural municipalities."
        IndustryFocus = "Private community hospitals, diagnostic centers, retail shopping stores, boarding schools, and vehicle services"
    },
    @{
        Name = "Damak"
        Slug = "seo-expert-damak"
        District = "Jhapa"
        Tagline = "Western Jhapa Commercial & Healthcare Metropolis"
        EcoContext = "Damak is a major commercial powerhouse in Western Jhapa featuring sprawling shopping centers, multi-specialty private medical facilities, colleges, real estate consultancies, and vibrant hospitality businesses competing intensely for customer attention in search engines."
        IndustryFocus = "Specialty medical centers, retail malls, business consultancies, private schools and colleges, and modern cafes"
    },
    @{
        Name = "Gaighat"
        Slug = "seo-expert-gaighat"
        District = "Udayapur"
        Tagline = "Inner Terai Gateway & Udayapur District Headquarters"
        EcoContext = "As the headquarter city of Udayapur (Triyuga Municipality), Gaighat bridges the eastern hills with the Terai plains. Its economy is powered by cement and construction logistics, regional healthcare, hotel services, and wholesale trade requiring authoritative search representation."
        IndustryFocus = "Construction material suppliers, regional hotels, transport agencies, healthcare clinics, and consumer retail"
    },
    @{
        Name = "Rajbiraj"
        Slug = "seo-expert-rajbiraj"
        District = "Saptari"
        Tagline = "Historic Planned City & District Headquarters of Saptari"
        EcoContext = "Nepal's earliest planned township, Rajbiraj is a cultural and administrative beacon hosting judicial law chambers, medical training institutions, border logistics, and traditional agro-commercial trade that increasingly rely on professional web assets and Google Maps verification."
        IndustryFocus = "Legal consultancies, private diagnostic clinics, educational academies, agricultural distributors, and retail centers"
    },
    @{
        Name = "Birtamod"
        Slug = "seo-expert-birtamod"
        District = "Jhapa"
        Tagline = "Premier Economic & Tea Capital of Eastern Nepal"
        EcoContext = "Birtamod is the pulsating economic heart of Jhapa, commanding massive tea processing and trading, premier super-specialty hospitals, high-volume retail malls, automobile showrooms, and financial institutions where prominent Google ranking is an essential competitive advantage."
        IndustryFocus = "Super-specialty hospitals, tea export houses, automobile dealerships, modern retail complexes, and financial consultancies"
    },
    @{
        Name = "Lahan"
        Slug = "seo-expert-lahan"
        District = "Siraha"
        Tagline = "Highway Commercial Hub & Renowned Healthcare Center"
        EcoContext = "Prominently positioned in eastern Siraha along the East-West Highway, Lahan is celebrated for world-class eye hospitals attracting cross-border patients, along with active wholesale retail markets, agricultural transport, and regional hospitality requiring strong local search placement."
        IndustryFocus = "Eye clinics and healthcare centers, regional hotels, pharmaceutical distributors, wholesale retail, and agro-trade"
    },
    @{
        Name = "Ilam"
        Slug = "seo-expert-ilam"
        District = "Ilam"
        Tagline = "Orthodox Tea Capital & Boutique Tourism Haven"
        EcoContext = "Ilam's world-famous picturesque tea estates, agro-tourism homestays, organic horticulture export (cardamom, ginger, dairy), and specialty hospitality require modern, fast-loading websites and international/national search visibility to convert travelers and buyers."
        IndustryFocus = "Boutique tea estates, tourism resorts and homestays, horticulture export enterprises, and local artisanal businesses"
    }
)

Write-Host "Starting generation of 17 location-specific landing pages..." -ForegroundColor Cyan

# Helper to render the mini-tabs HTML for any page (excluding the current page)
function Get-MiniTabsHtml([string]$currentSlug, [bool]$isHome = $false) {
    $chipsHtml = ""
    foreach ($c in $cities) {
        # Do not link to self
        if ($c.Slug -eq $currentSlug) { continue }
        
        $href = if ($isHome) {
            "$($c.Slug)/index.html"
        } else {
            "../$($c.Slug)/index.html"
        }
        
        $chipsHtml += @"
        <a href="$href" class="geo-tab-chip">
          <span class="geo-pin">&#128205;</span>
          <span class="geo-label">SEO Expert in $($c.Name)</span>
          <span class="geo-arrow">&rarr;</span>
        </a>

"@
    }

    return @"
    <!-- Regional Geographical Internal Linking Section -->
    <section class="geo-locations-section" aria-label="Explore SEO Services in Nearby Areas">
      <div class="container">
        <div class="geo-locations-card">
          <div class="geo-header">
            <div class="geo-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              <span>Regional Service Coverage &middot; Eastern Nepal</span>
            </div>
            <h2 class="geo-title">Explore SEO Services in Nearby Areas</h2>
            <p class="geo-subtitle">
              Based in Itahari, Sunsari, Smaran Raut provides hands-on search engine optimization, website speed enhancement, and technical web development to businesses across Eastern Nepal.
            </p>
          </div>
          <div class="geo-tabs-grid">
$chipsHtml          </div>
        </div>
      </div>
    </section>
"@
}

# Generate each location page
$count = 0
foreach ($city in $cities) {
    $count++
    $cName = $city.Name
    $cSlug = $city.Slug
    $cDist = $city.District
    $cTagline = $city.Tagline
    $cEco = $city.EcoContext
    $cInd = $city.IndustryFocus

    $targetDir = Join-Path $rootDir $cSlug
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }

    $miniTabs = Get-MiniTabsHtml -currentSlug $cSlug -isHome $false

    $pageHtml = @"
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEO Expert in $cName, Nepal - Smaran Raut</title>
  <meta name="description" content="Looking for an SEO expert in $cName, Nepal? Smaran Raut provides search engine optimization, fast business websites, and Google Maps visibility for businesses in $cName.">
  <link rel="canonical" href="https://smaranraut.com.np/$cSlug/">
  <meta name="robots" content="index, follow">

  <!-- Open Graph / Social Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://smaranraut.com.np/$cSlug/">
  <meta property="og:title" content="SEO Expert in $cName, Nepal - Smaran Raut">
  <meta property="og:description" content="SEO-optimized business websites, Google Maps rankings, and search improvements for businesses in $cName, Nepal. Services by Smaran Raut based in Itahari.">
  <meta property="og:locale" content="en_NP">

  <!-- Critical Layout Fallback -->
  <style>
    :root {
      --primary-dark: #1A1F1D;
      --accent-teal: #245037;
      --accent-gold: #8F6B38;
      --text-slate: #38403C;
      --bg-light: #FAF8F5;
    }
    body {
      margin: 0;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-light);
      color: var(--text-slate);
    }
    .mobile-nav-drawer, .modal-backdrop {
      display: none !important;
    }
    .modal-backdrop.active, .mobile-nav-drawer.active {
      display: flex !important;
    }
  </style>

  <!-- Dual-Compatible Stylesheets -->
  <link rel="stylesheet" href="../css/styles.css?v=2026_v5">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">

  <!-- JSON-LD Structured Data: ProfessionalService with explicit areaServed -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": "https://smaranraut.com.np/#organization",
        "name": "Smaran Raut - SEO & Web Development",
        "url": "https://smaranraut.com.np",
        "logo": "https://smaranraut.com.np/images/logo.png",
        "image": "https://smaranraut.com.np/images/smaran-raut-hero.jpg",
        "description": "Professional SEO and website development services serving businesses in $cName ($cDist District) and Eastern Nepal. Registered consultancy based in Itahari.",
        "telephone": "+977-9714539838",
        "email": "contact@smaranraut.com.np",
        "priceRange": "NPR",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Main Road, Ward No. 4",
          "addressLocality": "Itahari",
          "addressRegion": "Koshi Province",
          "postalCode": "56705",
          "addressCountry": "NP"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": "26.661694",
          "longitude": "87.275194"
        },
        "areaServed": [
          {
            "@type": "City",
            "name": "$cName",
            "containedInPlace": {
              "@type": "AdministrativeArea",
              "name": "$cDist District"
            }
          },
          {
            "@type": "Country",
            "name": "Nepal"
          }
        ]
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://smaranraut.com.np/" },
          { "@type": "ListItem", "position": 2, "name": "SEO Expert in $cName", "item": "https://smaranraut.com.np/$cSlug/" }
        ]
      }
    ]
  }
  </script>
</head>
<body>

  <!-- Site Header -->
  <header class="site-header">
    <div class="container nav-container">
      <a href="../index.html" class="brand-logo" aria-label="Smaran Raut Home">
        <div class="logo-icon">SR</div>
        <div class="brand-text">
          <span class="brand-name">Smaran Raut</span>
          <span class="brand-subtitle">SEO &amp; Web Development</span>
        </div>
      </a>

      <nav class="desktop-nav" aria-label="Main Navigation">
        <a href="../index.html" class="nav-link">Home</a>

        <!-- Services Dropdown -->
        <div class="nav-dropdown">
          <a href="../services/index.html" class="dropdown-toggle" aria-expanded="false" aria-haspopup="true" style="text-decoration: none;">
            Services <span class="dropdown-arrow">&#9662;</span>
          </a>
          <div class="dropdown-menu">
            <div class="dropdown-menu-header">
              <span class="dropdown-section-title">Core Services</span>
            </div>
            <a href="../services/index.html" class="dropdown-item featured">
              <span class="item-title">Services Overview &rarr;</span>
              <span class="item-desc">Browse our complete service packages</span>
            </a>
            <div class="dropdown-divider"></div>
            <a href="../services/seo-optimized-web-development/index.html" class="dropdown-item">
              <span class="item-title">SEO-Optimized Web Development</span>
              <span class="item-desc">Clean, fast business websites built for search</span>
            </a>
            <a href="../services/local-seo-itahari/index.html" class="dropdown-item">
              <span class="item-title">Local SEO &amp; Google Maps</span>
              <span class="item-desc">Rank locally in Itahari, Dharan &amp; Biratnagar</span>
            </a>
            <a href="../services/technical-seo-audit/index.html" class="dropdown-item">
              <span class="item-title">SEO for Existing Websites</span>
              <span class="item-desc">Diagnostic audits and search ranking fixes</span>
            </a>
            <a href="../services/core-web-vitals-speed/index.html" class="dropdown-item">
              <span class="item-title">Website Maintenance &amp; Speed</span>
              <span class="item-desc">Mobile optimization and ongoing technical care</span>
            </a>
            <a href="../services/ecommerce-seo-nepal/index.html" class="dropdown-item">
              <span class="item-title">E-Commerce SEO Nepal</span>
              <span class="item-desc">Product structured data and store visibility</span>
            </a>
            <a href="../services/enterprise-link-building/index.html" class="dropdown-item">
              <span class="item-title">Ongoing Website Management</span>
              <span class="item-desc">Monthly search tracking and site management</span>
            </a>
          </div>
        </div>

        <!-- Knowledge Hub Dropdown -->
        <div class="nav-dropdown">
          <button class="dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Knowledge Hub <span class="dropdown-arrow">&#9662;</span>
          </button>
          <div class="dropdown-menu">
            <div class="dropdown-menu-header">
              <span class="dropdown-section-title">Educational Guides</span>
            </div>
            <a href="../blog/index.html" class="dropdown-item featured">
              <span class="item-title">Knowledge Hub Directory &rarr;</span>
              <span class="item-desc">Explore practical web &amp; SEO guides</span>
            </a>
            <div class="dropdown-divider"></div>
            <a href="../blog/website-setup-and-management/index.html" class="dropdown-item">
              <span class="item-title">Website Setup &amp; Management</span>
              <span class="item-desc">Domains, hosting, launch &amp; maintenance</span>
            </a>
            <a href="../blog/seo-services-explained/index.html" class="dropdown-item">
              <span class="item-title">SEO Services Explained</span>
              <span class="item-desc">Keywords, content &amp; technical search</span>
            </a>
            <a href="../blog/social-media-and-online-advertising/index.html" class="dropdown-item">
              <span class="item-title">Social Media &amp; Online Ads</span>
              <span class="item-desc">Facebook, Instagram ads &amp; Google Maps</span>
            </a>
          </div>
        </div>

        <a href="../case-studies/index.html" class="nav-link">Case Studies</a>
        <a href="../about-us/index.html" class="nav-link">About</a>
        <a href="../contact-us/index.html" class="nav-link">Contact</a>
      </nav>

      <div class="header-cta-group">
        <button class="btn btn-primary btn-consultation" data-modal="consultation" aria-haspopup="dialog">
          Book Consultation
        </button>
        <button class="mobile-menu-btn" id="mobile-menu-toggle" aria-label="Open Navigation Menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Nav Drawer -->
  <div class="mobile-nav-drawer" id="mobile-nav-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation" style="display: none;">
    <div class="mobile-drawer-header">
      <div class="brand-logo">
        <div class="logo-icon">SR</div>
        <div class="brand-text">
          <span class="brand-name">Smaran Raut</span>
          <span class="brand-subtitle">SEO &amp; Web Development</span>
        </div>
      </div>
      <button class="modal-close-btn" id="mobile-menu-close" aria-label="Close Navigation Menu">&times;</button>
    </div>
    <ul class="mobile-nav-links">
      <li><a href="../index.html">Home</a></li>
      
      <!-- Mobile Services Dropdown -->
      <li class="mobile-dropdown-item">
        <button class="mobile-dropdown-toggle" aria-expanded="false">
          <span>Services</span>
          <span class="mobile-arrow">&#9662;</span>
        </button>
        <ul class="mobile-submenu" style="display: none;">
          <li><a href="../services/index.html"><strong>Services Overview &rarr;</strong></a></li>
          <li><a href="../services/seo-optimized-web-development/index.html">SEO Web Development</a></li>
          <li><a href="../services/local-seo-itahari/index.html">Local SEO Itahari &amp; Maps</a></li>
          <li><a href="../services/technical-seo-audit/index.html">SEO for Existing Websites</a></li>
          <li><a href="../services/core-web-vitals-speed/index.html">Maintenance &amp; Speed</a></li>
          <li><a href="../services/ecommerce-seo-nepal/index.html">E-Commerce SEO Nepal</a></li>
          <li><a href="../services/enterprise-link-building/index.html">Ongoing Website Management</a></li>
        </ul>
      </li>

      <!-- Mobile Knowledge Hub Dropdown -->
      <li class="mobile-dropdown-item">
        <button class="mobile-dropdown-toggle" aria-expanded="false">
          <span>Knowledge Hub</span>
          <span class="mobile-arrow">&#9662;</span>
        </button>
        <ul class="mobile-submenu" style="display: none;">
          <li><a href="../blog/index.html"><strong>Knowledge Hub Directory &rarr;</strong></a></li>
          <li><a href="../blog/google-business-profile-optimization-nepal/index.html">Google Maps &amp; Local SEO</a></li>
          <li><a href="../blog/nextjs-vs-wordpress-for-seo/index.html">Web Development &amp; Speed</a></li>
          <li><a href="../blog/schema-markup-implementation-guide/index.html">Technical SEO &amp; Schema</a></li>
          <li><a href="../blog/topical-authority-clustering-framework/index.html">Content &amp; Link Strategy</a></li>
        </ul>
      </li>

      <li><a href="../case-studies/index.html">Case Studies</a></li>
      <li><a href="../about-us/index.html">About Smaran Raut</a></li>
      <li><a href="../office-location/index.html">Office Location</a></li>
      <li><a href="../contact-us/index.html">Contact</a></li>
    </ul>
    <div style="margin-top: 2rem;">
      <button class="btn btn-primary btn-consultation" style="width: 100%;" data-modal="consultation">
        Book Consultation
      </button>
    </div>
  </div>

  <main id="main-content">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-content">
            <div class="hero-badge-wrap">
              <span class="badge badge-verified">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                SEO &amp; Web Development &middot; Serving $cName, $cDist
              </span>
            </div>

            <!-- Primary H1 -->
            <h1 class="hero-title">
              No.1 SEO Expert in $cName, Nepal - Smaran Raut
            </h1>

            <!-- H2: Semantic Triple -->
            <h2 class="hero-subtitle">
              Smaran Raut builds, optimizes, and manages business websites and their organic search visibility for enterprises in $cName.
            </h2>

            <!-- Supporting Business Description Paragraph -->
            <p class="hero-desc">
              I am an independent SEO specialist and website developer based in Itahari, proudly serving business owners, retail stores, healthcare clinics, and commercial services located in <strong>$cName</strong> and surrounding areas of $cDist District. If your business is difficult to discover when nearby customers search on Google, has a slow or outdated website, or lacks qualified inquiries, I provide straightforward, ethical search solutions engineered to deliver consistent phone calls, website visitors, and customer inquiries.
            </p>

            <!-- Core Service List -->
            <ul class="hero-service-list">
              <li>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>SEO-Optimized Business Website Development</span>
              </li>
              <li>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>Google Maps &amp; Local Business Profile Setup for $cName</span>
              </li>
              <li>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>SEO Audits &amp; Search Improvements for Existing Websites</span>
              </li>
              <li>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>Ongoing Website Management &amp; Technical Maintenance</span>
              </li>
            </ul>

            <!-- Prominent CTAs -->
            <div class="hero-cta-stack">
              <a href="../services/index.html" class="btn btn-secondary">
                Explore Services &rarr;
              </a>
              <button class="btn btn-primary btn-consultation" data-modal="consultation" id="book-consultation-btn">
                Book a Consultation
              </button>
            </div>
          </div>

          <!-- Visual Presentation Card -->
          <div class="hero-visual-card">
            <div class="photo-wrapper">
              <svg class="photo-svg-art" viewBox="0 0 520 400" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="520" height="400" fill="#F4F0E8"/>
                <rect x="20" y="20" width="480" height="360" rx="8" fill="#FAF8F5" stroke="#E5E0D6"/>
                
                <rect x="50" y="45" width="130" height="110" rx="4" fill="#EFEAE0" stroke="#E5E0D6"/>
                <line x1="115" y1="45" x2="115" y2="155" stroke="#E0DAD0" stroke-width="1.5"/>
                <line x1="50" y1="100" x2="180" y2="100" stroke="#E0DAD0" stroke-width="1.5"/>
                
                <path d="M40 280C140 270 380 270 480 280L490 370H30L40 280Z" fill="#EAE5DC" stroke="#DFD9CE"/>
                
                <rect x="200" y="220" width="120" height="80" rx="5" fill="#FFFFFF" stroke="#8F6B38" stroke-width="1.5"/>
                <rect x="210" y="230" width="100" height="12" rx="2" fill="#EBF3EE"/>
                <rect x="210" y="248" width="45" height="40" rx="2" fill="#F4F0E8"/>
                <rect x="260" y="248" width="50" height="10" rx="1" fill="#245037"/>
                <rect x="260" y="262" width="40" height="6" rx="1" fill="#D5CEC4"/>
                <rect x="260" y="272" width="45" height="6" rx="1" fill="#D5CEC4"/>
                <polygon points="190,300 330,300 325,306 195,306" fill="#D5CEC4"/>
                
                <circle cx="150" cy="165" r="32" fill="#245037"/>
                <circle cx="150" cy="165" r="24" fill="#D8A47F"/>
                <path d="M110 240C110 205 130 195 150 195C170 195 190 205 190 240V270H110V240Z" fill="#1A1F1D"/>
                <path d="M142 195L150 215L158 195H142Z" fill="#245037"/>
                
                <circle cx="370" cy="170" r="30" fill="#76562A"/>
                <circle cx="370" cy="170" r="23" fill="#E0B695"/>
                <path d="M330 240C330 208 350 200 370 200C390 200 410 208 410 240V270H330V240Z" fill="#38403C"/>
                <path d="M364 200L370 216L376 200H364Z" fill="#8F6B38"/>

                <rect x="60" y="295" width="115" height="60" rx="6" fill="#FFFFFF" stroke="#E5E0D6" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.05))"/>
                <text x="70" y="313" fill="#626C66" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="600">$cName.ToUpper() VISIBILITY</text>
                <path d="M72 342L95 330L120 335L155 318" stroke="#245037" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="155" cy="318" r="3.5" fill="#8F6B38"/>
                <text x="72" y="352" fill="#245037" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="700">+ Local Searches</text>

                <rect x="360" y="300" width="85" height="50" rx="4" fill="#FFFFFF" stroke="#E5E0D6"/>
                <line x1="370" y1="315" x2="430" y2="315" stroke="#245037" stroke-width="2"/>
                <line x1="370" y1="325" x2="420" y2="325" stroke="#D5CEC4" stroke-width="1.5"/>
                <line x1="370" y1="335" x2="410" y2="335" stroke="#D5CEC4" stroke-width="1.5"/>
              </svg>
            </div>

            <!-- Animated Qualification Chips -->
            <div class="hero-qualification-chips" aria-label="Professional Qualifications">
              <div class="qual-chip qual-chip-1">
                <span class="qual-chip-icon">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="16 18 22 12 16 6"></polyline>
                    <polyline points="8 6 2 12 8 18"></polyline>
                  </svg>
                </span>
                <span class="qual-chip-text">Experienced Web Developer</span>
              </div>
              <div class="qual-chip qual-chip-2">
                <span class="qual-chip-icon">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                  </svg>
                </span>
                <span class="qual-chip-text">Certified from Hynex AI Labs</span>
              </div>
              <div class="qual-chip qual-chip-3">
                <span class="qual-chip-icon">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                </span>
                <span class="qual-chip-text">Fluent in SEO Terminologies</span>
              </div>
            </div>

            <!-- Credential Badge with transparent location notice -->
            <div class="floating-credential-badge">
              <div class="credential-info">
                <span class="cred-name">Smaran Raut</span>
                <span class="cred-title">SEO Specialist &middot; Based in Itahari, Serving $cName</span>
              </div>
              <div class="verified-stamp" title="Verified Professional">&#10003;</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Statutory Alignment Strip -->
    <div class="regulators-strip">
      <div class="container">
        <div class="strip-inner">
          <span class="strip-label">Statutory &amp; Governance Alignment:</span>
          <div class="regulators-list">
            <span class="regulator-chip">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              Office of Company Registrar (OCR Nepal)
            </span>
            <span class="regulator-chip">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              Inland Revenue Dept (IRD PAN/VAT)
            </span>
            <span class="regulator-chip">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              Nepal Telecom Authority (NTA Standards)
            </span>
            <span class="regulator-chip">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              Vigyapan Board Nepal
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Location Context & Commercial Overview Section -->
    <section style="background-color: var(--bg-white); padding: 4.5rem 0; border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
      <div class="container">
        <div style="max-width: 820px; margin: 0 auto;">
          <div style="text-align: center; margin-bottom: 2.5rem;">
            <span class="badge badge-teal" style="margin-bottom: 0.75rem;">$cTagline</span>
            <h2 style="font-size: clamp(1.6rem, 2.5vw + 0.5rem, 2.2rem); color: var(--primary-dark); font-weight: 800; margin-bottom: 1rem;">
              Helping Businesses in $cName Win Local Google Searches
            </h2>
            <p style="color: var(--text-slate); font-size: 1.05rem; line-height: 1.6;">
              $cEco
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
            <div style="padding: 1.5rem; background-color: var(--bg-light); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <h3 style="font-size: 1.1rem; color: var(--primary-dark); margin-bottom: 0.5rem;">Targeted Search Queries</h3>
              <p style="font-size: 0.92rem; color: var(--text-slate); margin: 0; line-height: 1.5;">
                We optimize your website for high-intent queries that customers in $cName actually type, such as "best [service] in $cName" and "near me" mobile searches.
              </p>
            </div>
            <div style="padding: 1.5rem; background-color: var(--bg-light); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <h3 style="font-size: 1.1rem; color: var(--primary-dark); margin-bottom: 0.5rem;">$cName Google Maps Setup</h3>
              <p style="font-size: 0.92rem; color: var(--text-slate); margin: 0; line-height: 1.5;">
                Accurate address geocoding, verified categories, opening hours, and direct call buttons so $cName shoppers find directions straight to your doors.
              </p>
            </div>
            <div style="padding: 1.5rem; background-color: var(--bg-light); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
              <h3 style="font-size: 1.1rem; color: var(--primary-dark); margin-bottom: 0.5rem;">Fast Smartphone Loading</h3>
              <p style="font-size: 0.92rem; color: var(--text-slate); margin: 0; line-height: 1.5;">
                Engineered for rapid sub-second rendering across common 4G mobile networks throughout $cDist, preventing lost visitors and bounce-offs.
              </p>
            </div>
          </div>

          <div style="margin-top: 2.5rem; padding: 1.25rem 1.5rem; background-color: rgba(36, 80, 55, 0.05); border-left: 4px solid var(--accent-teal); border-radius: 0 var(--radius-md) var(--radius-md) 0;">
            <p style="margin: 0; font-size: 0.92rem; color: var(--text-slate); line-height: 1.55;">
              <strong>Note on Service Delivery:</strong> My primary operational base is located at Main Road, Ward 4, Itahari. For clients in $cName, all SEO consulting, strategy, and website engineering are handled through direct on-site visits across the corridor and seamless remote communication. No fictional branches or fake local addresses are ever used.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Centerpiece Interactive Utility: Local SEO & Visibility Checker -->
    <section class="container" style="padding-top: 3.5rem;">
      <div class="calculator-wrapper" id="local-seo-calculator">
        <div class="calculator-header">
          <h2 class="calculator-title">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--accent-teal)" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
            Interactive Local SEO Visibility &amp; Readiness Checker
          </h2>
          <p class="calculator-subtitle">
            Evaluate your business's local search readiness in $cName based on customer reviews and consistent directory listings.
          </p>
        </div>

        <div class="calculator-grid">
          <div class="calculator-controls">
            <div class="form-group">
              <label for="lseo-reviews">Google Reviews Count: <span id="lseo-reviews-val" class="range-val-badge">25</span></label>
              <input type="range" id="lseo-reviews" min="0" max="150" value="25" class="form-control" style="cursor: pointer;">
            </div>

            <div class="form-group">
              <label for="lseo-rating">Average Star Rating:</label>
              <select id="lseo-rating" class="form-control">
                <option value="5.0">5.0 Stars (Excellent)</option>
                <option value="4.7" selected>4.7 - 4.9 Stars (Strong)</option>
                <option value="4.2">4.0 - 4.6 Stars (Moderate)</option>
                <option value="3.5">Below 4.0 Stars (Needs Improvement)</option>
              </select>
            </div>

            <div class="form-group">
              <label for="lseo-citations">Accurate Directory Listings: <span id="lseo-citations-val" class="range-val-badge">18</span></label>
              <input type="range" id="lseo-citations" min="0" max="60" value="18" class="form-control" style="cursor: pointer;">
            </div>

            <div class="form-group">
              <label for="lseo-radius">Target Service Area:</label>
              <select id="lseo-radius" class="form-control">
                <option value="5" selected>$cName Urban Area (&le;5 km)</option>
                <option value="15">$cName + Nearby Municipalities (&le;15 km)</option>
                <option value="30">Greater Eastern Nepal Region (&le;30 km)</option>
              </select>
            </div>
          </div>

          <div class="calculator-results">
            <div class="results-top">
              <div class="score-display-block">
                <div class="score-number" id="lseo-score">72/100</div>
                <div class="score-label">Local Visibility Readiness Index</div>
                <div style="margin-top: 0.5rem;">
                  <span class="badge badge-gold" id="lseo-rank-badge">Moderate Visibility</span>
                </div>
              </div>

              <div>
                <div class="metric-row">
                  <span>Estimated Customer Inquiries:</span>
                  <span class="metric-val" id="lseo-projected-calls">~55 Inquiries/mo</span>
                </div>
                <div class="metric-row">
                  <span>Local Search Standing:</span>
                  <span class="metric-val" id="lseo-projected-rev">Moderate Local Readiness</span>
                </div>
              </div>
            </div>

            <div class="results-advice" id="lseo-advice">
              Evaluating local search readiness in $cName...
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Transparent 4-Step Process -->
    <section class="process-section">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto 3.5rem;">
          <span class="badge badge-teal" style="margin-bottom: 0.75rem;">Clear &amp; Predictable Process</span>
          <h2>How We Work With Businesses in $cName</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem;">
            A straightforward, hands-on approach from your initial consultation to long-term organic search results.
          </p>
        </div>

        <div class="process-group">
          <div class="process-flow-row">
            <div class="process-step-card">
              <span class="process-step-num">Step 1</span>
              <div class="process-step-title">Initial Consultation</div>
              <p class="process-step-desc">We review your $cName target customers, existing web presence, and primary search competitors.</p>
            </div>
            <div class="process-arrow">&rarr;</div>
            <div class="process-step-card">
              <span class="process-step-num">Step 2</span>
              <div class="process-step-title">Website &amp; Map Audit</div>
              <p class="process-step-desc">Diagnosing speed bottlenecks, mobile responsiveness, and local citation discrepancies.</p>
            </div>
            <div class="process-arrow">&rarr;</div>
            <div class="process-step-card">
              <span class="process-step-num">Step 3</span>
              <div class="process-step-title">Targeted Optimization</div>
              <p class="process-step-desc">Implementing verified Schema markup, localized keywords, fast code, and Google Business Profile fixes.</p>
            </div>
            <div class="process-arrow">&rarr;</div>
            <div class="process-step-card">
              <span class="process-step-num">Step 4</span>
              <div class="process-step-title">Search Growth</div>
              <p class="process-step-desc">Monitoring steady climb in Google search impressions, local phone calls, and foot traffic.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section: Location-Specific Guidance -->
    <section class="faq-section" style="background-color: var(--bg-white); padding: 4.5rem 0;">
      <div class="container">
        <div style="max-width: 800px; margin: 0 auto;">
          <div style="text-align: center; margin-bottom: 3rem;">
            <span class="badge badge-teal" style="margin-bottom: 0.75rem;">Frequently Asked Questions</span>
            <h2>Frequently Asked Questions About SEO in $cName</h2>
            <p style="color: var(--text-muted); font-size: 1.02rem;">
              Clear answers regarding service coverage, business location, and how we collaborate.
            </p>
          </div>

          <div class="faq-accordion">
            <div class="accordion-item">
              <button class="accordion-header" aria-expanded="true">
                <span>Do you provide on-site meetings or remote SEO services for businesses in $cName?</span>
                <span class="accordion-icon">&darr;</span>
              </button>
              <div class="accordion-content">
                Yes. While based in Itahari, I easily coordinate directly with business owners in $cName through both on-site working sessions and clear, regular digital updates.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" aria-expanded="false">
                <span>Do you have a physical office or branch in $cName?</span>
                <span class="accordion-icon">&darr;</span>
              </button>
              <div class="accordion-content">
                No. My registered business office is situated at Main Road, Ward No. 4, Itahari, Sunsari. I serve businesses in $cName as part of my regional service coverage across Koshi Province and Eastern Nepal.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" aria-expanded="false">
                <span>What types of businesses in $cName benefit most from SEO?</span>
                <span class="accordion-icon">&darr;</span>
              </button>
              <div class="accordion-content">
                In $cName, key beneficiaries include $cInd looking to capture customers searching locally for trusted providers on Google.
              </div>
            </div>

            <div class="accordion-item">
              <button class="accordion-header" aria-expanded="false">
                <span>Are invoices and contracts compliant with Nepal tax laws?</span>
                <span class="accordion-icon">&darr;</span>
              </button>
              <div class="accordion-content">
                Yes. All agreements and billing comply strictly with the Inland Revenue Department (IRD) PAN/VAT Act 2058.
              </div>
            </div>
          </div>

          <!-- Final Consultation Callout -->
          <div style="background: linear-gradient(145deg, #0A1628, #182C4E); padding: 3rem; border-radius: var(--radius-lg); text-align: center; color: white; margin-top: 3.5rem; border: 1px solid var(--border-dark);">
            <h3 style="color: white; font-size: 1.8rem; margin-bottom: 1rem;">Ready to Grow Your Search Presence in $cName?</h3>
            <p style="color: #CBD5E1; max-width: 600px; margin: 0 auto 1.75rem;">
              Schedule a 30-minute consultation. We will analyze your website, discuss your goals in $cName, and map out a clear plan of action.
            </p>
            <button class="btn btn-gold btn-consultation" data-modal="consultation" data-service="SEO Services in $cName">
              Schedule a Consultation
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Identical Service Location Map Section -->
    <section class="service-location-section" aria-label="My Service Location">
      <div class="container">
        <div class="location-map-card">
          <div class="location-map-header">
            <div class="geo-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              <span>Base of Operations &middot; Itahari</span>
            </div>
            <h2 class="location-map-title">My Service Location</h2>
            <p class="location-map-subtitle">
              Smaran Raut operates from <strong>Itahari Chowk, middle of Janta Galli</strong> (26.661694&deg; N, 87.275194&deg; E). While this page outlines SEO and web development services provided to businesses in <strong>$cName</strong>, all technical work, strategic consulting, and project management are delivered from our central office in Itahari.
            </p>
          </div>
          <div class="map-embed-wrapper">
            <iframe 
              title="Smaran Raut Service Location - Itahari Chowk, middle of Janta Galli"
              src="https://maps.google.com/maps?q=26.661694,87.275194&amp;hl=en&amp;z=17&amp;output=embed"
              width="100%" 
              height="380" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
          </div>
          <div class="location-map-footer">
            <div class="map-footer-item">
              <span class="map-icon">&#128205;</span>
              <span><strong>Physical Location:</strong> Itahari Chowk, middle of Janta Galli, Itahari, Sunsari 56705, Nepal</span>
            </div>
            <div class="map-footer-item">
              <span class="map-icon">&#9678;</span>
              <span><strong>Exact Coordinates:</strong> 26.661694, 87.275194 (26&deg;39'42.1&quot;N 87&deg;16'30.7&quot;E)</span>
            </div>
          </div>
        </div>
      </div>
    </section>

$miniTabs
  </main>

  <!-- Universal Consultation Modal Dialog -->
  <div class="modal-backdrop" id="consultation-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" style="display: none;">
    <div class="modal-card">
      <div class="modal-header">
        <div>
          <h3 id="modal-title" style="margin-bottom: 0.25rem;">Schedule a Consultation</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">Direct discussion with Smaran Raut</p>
        </div>
        <button class="modal-close-btn" aria-label="Close dialog">&times;</button>
      </div>
      <div class="modal-body">
        <form id="consultation-form" novalidate>
          <div class="form-group">
            <label for="client-name">Full Name *</label>
            <input type="text" id="client-name" name="client_name" required placeholder="e.g. Ramesh Karki" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-email">Email Address *</label>
            <input type="email" id="client-email" name="client_email" required placeholder="ramesh@company.com" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-phone">Phone / WhatsApp Number *</label>
            <input type="tel" id="client-phone" name="client_phone" required placeholder="+977 9714539838" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-website">Website URL (if you have one)</label>
            <input type="url" id="client-website" name="client_website" placeholder="https://yourwebsite.com" class="form-control">
          </div>
          <div class="form-group">
            <label for="modal-service-select">What do you need help with?</label>
            <select id="modal-service-select" name="service_interest" class="form-control">
              <option value="local-seo" selected>Local SEO &amp; Google Maps ($cName &amp; Eastern Nepal)</option>
              <option value="web-development">New SEO-Optimized Website Development</option>
              <option value="technical-audit">SEO Audit &amp; Improvements for Existing Site</option>
              <option value="core-web-vitals">Website Maintenance &amp; Speed Improvements</option>
              <option value="ecommerce-seo">E-Commerce Store Optimization</option>
            </select>
          </div>
          <div class="form-group">
            <label for="client-notes">Tell us about your project in $cName</label>
            <textarea id="client-notes" name="client_notes" rows="3" class="form-control" placeholder="Briefly describe your business in $cName and what you would like to achieve..."></textarea>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 0.5rem;">
            Submit Request
          </button>
          <p style="font-size: 0.75rem; color: var(--text-muted); text-align: center; margin-top: 0.85rem; margin-bottom: 0;">
            100% Confidential. In compliance with Nepal Data Protection regulations.
          </p>
        </form>
      </div>
    </div>
  </div>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand-title">Smaran Raut</div>
          <p style="color: #94A3B8; font-size: 0.92rem; margin-bottom: 1.25rem;">
            SEO Specialist &amp; Web Developer based in Itahari, Sunsari, Koshi Province, Nepal. Providing business website development, search optimization for existing sites, and website maintenance across Eastern Nepal.
          </p>
          <p style="font-size: 0.85rem; color: #64748B;">
            <strong>Office:</strong> Itahari Chowk, middle of Janta Galli, Itahari, Sunsari 56705, Nepal<br>
            <strong>Inquiries:</strong> contact@smaranraut.com.np &middot; <a href="tel:+9779714539838" style="color: inherit; text-decoration: none;">+977 9714539838</a>
          </p>
        </div>

        <div>
          <div class="footer-col-title">Services</div>
          <ul class="footer-links">
            <li><a href="../services/seo-optimized-web-development/index.html">SEO Web Development</a></li>
            <li><a href="../services/local-seo-itahari/index.html">Local SEO Itahari</a></li>
            <li><a href="../services/technical-seo-audit/index.html">SEO for Existing Sites</a></li>
            <li><a href="../services/core-web-vitals-speed/index.html">Maintenance &amp; Speed</a></li>
            <li><a href="../services/ecommerce-seo-nepal/index.html">E-Commerce SEO</a></li>
            <li><a href="../services/semantic-content-strategy/index.html">Content Planning</a></li>
            <li><a href="../services/enterprise-link-building/index.html">Ongoing Management</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Knowledge Hub</div>
          <ul class="footer-links">
            <li><a href="../blog/index.html">All Helpful Guides</a></li>
            <li><a href="../blog/google-business-profile-optimization-nepal/index.html">Google Maps Optimization</a></li>
            <li><a href="../blog/nextjs-vs-wordpress-for-seo/index.html">Next.js vs. WordPress</a></li>
            <li><a href="../blog/how-to-conduct-technical-seo-audit/index.html">Website SEO Checkup</a></li>
            <li><a href="../blog/mobile-first-responsive-design-checklist/index.html">Mobile Friendly Checklist</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">About &amp; Legal</div>
          <ul class="footer-links">
            <li><a href="../about-us/index.html">About Smaran Raut</a></li>
            <li><a href="../case-studies/index.html">Client Work Examples</a></li>
            <li><a href="../office-location/index.html">Office Location</a></li>
            <li><a href="../consultation/index.html">Schedule a Consultation</a></li>
            <li><a href="../disclaimer/index.html">Professional Disclaimer</a></li>
            <li><a href="../editorial-policy/index.html">Editorial Standards</a></li>
            <li><a href="../privacy-policy/index.html">Privacy Policy</a></li>
            <li><a href="../terms-and-conditions/index.html">Terms of Service</a></li>
            <li><a href="../cookie-policy/index.html">Cookie Policy</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-statutory-notes">
          &copy; 2026 Smaran Raut SEO &amp; Web Development. Registered under OCR and IRD PAN/VAT Act 2058, Nepal.
        </div>
        <div>
          <a href="../sitemap.xml" style="color: var(--accent-teal); font-size: 0.85rem; margin-right: 1rem;">XML Sitemap</a>
          <a href="../robots.txt" style="color: var(--accent-teal); font-size: 0.85rem;">Robots.txt</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Core Scripts with Cache-Busting -->
  <script src="../js/calculators.js?v=2026_v2"></script>
  <script src="../js/app.js?v=2026_v5"></script>
</body>
</html>
"@

    $outFilePath = Join-Path $targetDir "index.html"
    [System.IO.File]::WriteAllText($outFilePath, $pageHtml, [System.Text.Encoding]::UTF8)
    Write-Host "[$count/17] Generated: $cSlug/index.html" -ForegroundColor Green
}

# Update Homepage (index.html) to include the mini-tabs at the bottom
Write-Host "Updating Homepage (index.html) with Explore SEO Services in Nearby Areas..." -ForegroundColor Cyan
$homePath = Join-Path $rootDir "index.html"
$homeContent = [System.IO.File]::ReadAllText($homePath, [System.Text.Encoding]::UTF8)

# Check if already present, if not add right before </main>
$homeTabs = Get-MiniTabsHtml -currentSlug "seo-expert-itahari" -isHome $true

if ($homeContent -match 'class="geo-locations-section"') {
    $homeContent = [System.Text.RegularExpressions.Regex]::Replace($homeContent, '<!-- Regional Geographical Internal Linking Section -->[\s\S]*?</section>', $homeTabs.Trim())
} else {
    $homeContent = $homeContent.Replace("  </main>", "$homeTabs`n  </main>")
}
[System.IO.File]::WriteAllText($homePath, $homeContent, [System.Text.Encoding]::UTF8)
Write-Host "Homepage updated." -ForegroundColor Green

# Update sitemap.xml to add all 17 locations
Write-Host "Updating sitemap.xml with 17 location routes..." -ForegroundColor Cyan
$sitemapPath = Join-Path $rootDir "sitemap.xml"
$sitemapContent = [System.IO.File]::ReadAllText($sitemapPath, [System.Text.Encoding]::UTF8)

$dateStr = [DateTime]::UtcNow.ToString("yyyy-MM-dd")
$newUrls = ""
foreach ($city in $cities) {
    $locUrl = "https://smaranraut.com.np/$($city.Slug)/"
    if ($sitemapContent -notmatch [regex]::Escape($locUrl)) {
        $newUrls += @"
  <url>
    <loc>$locUrl</loc>
    <lastmod>$dateStr</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

"@
    }
}

if ($newUrls.Length -gt 0) {
    $sitemapContent = $sitemapContent.Replace("</urlset>", "$newUrls</urlset>")
    [System.IO.File]::WriteAllText($sitemapPath, $sitemapContent, [System.Text.Encoding]::UTF8)
    Write-Host "sitemap.xml updated with new locations." -ForegroundColor Green
} else {
    Write-Host "sitemap.xml already contains location routes." -ForegroundColor Yellow
}

Write-Host "ALL 17 LOCATION LANDING PAGES SUCCESSFULLY CREATED & LINKED!" -ForegroundColor Green
