import os

WP_FUNCTIONS = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\functions.php'

with open(WP_FUNCTIONS, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace smaran_seo_homepage_seo_meta with require_once and smaran_seo_homepage_schema
target_old = """/**
 * Output Homepage SEO Metadata and Schema.org JSON-LD
 */
function smaran_seo_homepage_seo_meta() {
    if (is_front_page()) {
        ?>
<!-- Primary SEO Meta -->
<meta name="description" content="Smaran Raut builds SEO-optimized business websites, improves existing websites for search engines, and provides ongoing website maintenance in Itahari, Eastern Nepal.">
<link rel="canonical" href="<?php echo esc_url(home_url('/')); ?>">
<meta name="robots" content="index, follow">

<!-- Open Graph / Social Meta -->
<meta property="og:type" content="website">
<meta property="og:url" content="<?php echo esc_url(home_url('/')); ?>">
<meta property="og:title" content="Smaran Raut | SEO & Business Website Development">
<meta property="og:description" content="SEO-optimized business websites, search improvements for existing websites, and website maintenance in Itahari, Nepal.">
<meta property="og:locale" content="en_NP">

<!-- JSON-LD Structured Data: ProfessionalService & LocalBusiness -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["ProfessionalService", "LocalBusiness"],
      "@id": "<?php echo esc_url(home_url('/#organization')); ?>",
      "name": "Smaran Raut - SEO & Web Development",
      "url": "<?php echo esc_url(home_url('/')); ?>",
      "description": "SEO-optimized business website development, search improvements for existing websites, and ongoing website maintenance in Itahari, Sunsari, Nepal.",
      "telephone": "+977-9714539838",
      "email": "contact@smaranraut.com.np",
      "priceRange": "$$",
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
        "latitude": "26.6646",
        "longitude": "87.2798"
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "18:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Saturday"],
          "opens": "10:00",
          "closes": "15:00"
        }
      ],
      "areaServed": [
        { "@type": "City", "name": "Itahari" },
        { "@type": "City", "name": "Dharan" },
        { "@type": "City", "name": "Biratnagar" },
        { "@type": "AdministrativeArea", "name": "Koshi Province" },
        { "@type": "Country", "name": "Nepal" }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "<?php echo esc_url(home_url('/#website')); ?>",
      "url": "<?php echo esc_url(home_url('/')); ?>",
      "name": "Smaran Raut SEO & Web Development",
      "publisher": { "@id": "<?php echo esc_url(home_url('/#organization')); ?>" }
    }
  ]
}
</script>
        <?php
    }
}
add_action('wp_head', 'smaran_seo_homepage_seo_meta', 1);"""

target_new = """/**
 * Include Reusable Open Graph & Social Sharing Metadata System
 */
require_once get_template_directory() . '/inc/seo-metadata.php';

/**
 * Output Homepage Schema.org JSON-LD
 */
function smaran_seo_homepage_schema() {
    if (is_front_page()) {
        ?>
<!-- JSON-LD Structured Data: ProfessionalService & LocalBusiness -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["ProfessionalService", "LocalBusiness"],
      "@id": "<?php echo esc_url(home_url('/#organization')); ?>",
      "name": "Smaran Raut - SEO & Web Development",
      "url": "<?php echo esc_url(home_url('/')); ?>",
      "description": "SEO-optimized business website development, search improvements for existing websites, and ongoing website maintenance in Itahari, Sunsari, Nepal.",
      "telephone": "+977-9714539838",
      "email": "contact@smaranraut.com.np",
      "priceRange": "$$",
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
        "latitude": "26.6646",
        "longitude": "87.2798"
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "18:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Saturday"],
          "opens": "10:00",
          "closes": "15:00"
        }
      ],
      "areaServed": [
        { "@type": "City", "name": "Itahari" },
        { "@type": "City", "name": "Dharan" },
        { "@type": "City", "name": "Biratnagar" },
        { "@type": "AdministrativeArea", "name": "Koshi Province" },
        { "@type": "Country", "name": "Nepal" }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "<?php echo esc_url(home_url('/#website')); ?>",
      "url": "<?php echo esc_url(home_url('/')); ?>",
      "name": "Smaran Raut SEO & Web Development",
      "publisher": { "@id": "<?php echo esc_url(home_url('/#organization')); ?>" }
    }
  ]
}
</script>
        <?php
    }
}
add_action('wp_head', 'smaran_seo_homepage_schema', 2);"""

code = code.replace(target_old, target_new)
with open(WP_FUNCTIONS, 'w', encoding='utf-8') as f:
    f.write(code)
print("Updated functions.php successfully!")
