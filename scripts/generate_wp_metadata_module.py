import json
import os

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'
WP_DIR = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo'

registry_file = os.path.join(STATIC_DIR, 'scripts', 'metadata_canonical_registry.json')
with open(registry_file, 'r', encoding='utf-8') as f:
    registry = json.load(f)

# Create inc dir if not exists
inc_dir = os.path.join(WP_DIR, 'inc')
os.makedirs(inc_dir, exist_ok=True)

php_code = """<?php
/**
 * Reusable Open Graph & Social Sharing Metadata System
 *
 * Automatically generates standard Open Graph, Twitter/X Cards,
 * and Canonical metadata with fallbacks for all website routes.
 *
 * @package Smaran_SEO
 * @version 2.0.0
 */

if (!defined('ABSPATH')) {
    exit;
}

// Prevent duplicate meta tags from WordPress core and Rank Math
add_action('init', function() {
    remove_action('wp_head', '_wp_render_title_tag', 1);
    remove_action('wp_head', 'rel_canonical');
    add_filter('rank_math/opengraph/facebook', '__return_false');
    add_filter('rank_math/opengraph/twitter', '__return_false');
});
add_action('wp_head', function() {
    remove_all_actions('rank_math/head');
}, 0);

function smaran_seo_get_metadata_registry() {
    static $registry = null;
    if ($registry !== null) {
        return $registry;
    }

    $registry = array(
"""

for url, data in registry.items():
    slug = data['slug']
    title = data['title'].replace("'", "\\'")
    desc = data['desc'].replace("'", "\\'")
    canonical = data['canonical']
    og_type = data['og_type']
    og_image = data['og_image']
    image_alt = data['image_alt'].replace("'", "\\'")
    pub = data.get('published_time') or ''
    mod = data.get('modified_time') or ''
    sec = (data.get('section') or '').replace("'", "\\'")
    
    php_code += f"        '{canonical}' => array(\n"
    php_code += f"            'slug' => '{slug}',\n"
    php_code += f"            'title' => '{title}',\n"
    php_code += f"            'desc' => '{desc}',\n"
    php_code += f"            'canonical' => '{canonical}',\n"
    php_code += f"            'og_type' => '{og_type}',\n"
    php_code += f"            'og_image' => '{og_image}',\n"
    php_code += f"            'image_alt' => '{image_alt}',\n"
    php_code += f"            'published_time' => '{pub}',\n"
    php_code += f"            'modified_time' => '{mod}',\n"
    php_code += f"            'section' => '{sec}',\n"
    php_code += "        ),\n"

php_code += """    );

    return $registry;
}

/**
 * Render complete SEO and Social Sharing Metadata
 */
function smaran_seo_render_metadata() {
    $current_url = home_url(add_query_arg(array(), $GLOBALS['wp']->request));
    $current_url = trailingslashit(strtok($current_url, '?'));
    
    // Normalize domain to canonical https://smaranraut.com.np/
    $path = wp_parse_url($current_url, PHP_URL_PATH);
    if (empty($path) || $path === '/') {
        $canonical = 'https://smaranraut.com.np/';
    } else {
        $canonical = 'https://smaranraut.com.np' . trailingslashit($path);
    }

    $registry = smaran_seo_get_metadata_registry();
    $meta = isset($registry[$canonical]) ? $registry[$canonical] : null;

    // Intelligent Fallbacks if route not in static registry
    if (!$meta) {
        $title = wp_get_document_title();
        $desc = 'SEO-optimized business websites, technical search improvements, and website maintenance in Nepal by Smaran Raut.';
        $og_type = is_single() ? 'article' : 'website';
        $og_image = 'https://smaranraut.com.np/images/og-smaran-raut.jpg';
        $image_alt = 'Smaran Raut - Web Developer & SEO Expert in Nepal';
        $pub = '';
        $mod = '';
        $sec = '';

        if (is_front_page()) {
            $canonical = 'https://smaranraut.com.np/';
            $title = 'Smaran Raut | SEO & Business Website Development in Itahari, Nepal';
            $desc = 'Smaran Raut builds SEO-optimized business websites, improves existing websites for search engines, and provides ongoing website maintenance in Itahari, Eastern Nepal.';
            $og_image = 'https://smaranraut.com.np/images/og-smaran-raut.jpg';
        } elseif (is_page()) {
            global $post;
            $slug = $post ? $post->post_name : '';
            if (strpos($slug, 'seo-expert-') === 0 || $slug === 'office-location') {
                $og_image = 'https://smaranraut.com.np/images/og-locations.jpg';
                $image_alt = 'Local SEO & Web Development in Nepal - Smaran Raut';
            } elseif ($slug === 'services' || strpos($slug, 'seo-') !== false || strpos($slug, 'web-development') !== false) {
                $og_image = 'https://smaranraut.com.np/images/og-services.jpg';
                $image_alt = 'SEO & Website Development Services - Smaran Raut';
            } elseif ($slug === 'blog' || strpos($slug, 'guide') !== false) {
                $og_image = 'https://smaranraut.com.np/images/og-knowledge-hub.jpg';
                $image_alt = 'SEO & Web Development Knowledge Hub - Smaran Raut';
            }
        }

        $meta = array(
            'title' => $title,
            'desc' => $desc,
            'canonical' => $canonical,
            'og_type' => $og_type,
            'og_image' => $og_image,
            'image_alt' => $image_alt,
            'published_time' => $pub,
            'modified_time' => $mod,
            'section' => $sec,
        );
    }

    ?>
  <!-- Primary SEO Meta -->
  <title><?php echo esc_html($meta['title']); ?></title>
  <meta name="description" content="<?php echo esc_attr($meta['desc']); ?>">
  <link rel="canonical" href="<?php echo esc_url($meta['canonical']); ?>">
  <meta name="robots" content="index, follow">

  <!-- Open Graph / Facebook / WhatsApp -->
  <meta property="og:type" content="<?php echo esc_attr($meta['og_type']); ?>">
  <meta property="og:site_name" content="Smaran Raut">
  <meta property="og:url" content="<?php echo esc_url($meta['canonical']); ?>">
  <meta property="og:title" content="<?php echo esc_attr($meta['title']); ?>">
  <meta property="og:description" content="<?php echo esc_attr($meta['desc']); ?>">
  <meta property="og:image" content="<?php echo esc_url($meta['og_image']); ?>">
  <meta property="og:image:secure_url" content="<?php echo esc_url($meta['og_image']); ?>">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="<?php echo esc_attr($meta['image_alt']); ?>">
  <meta property="og:locale" content="en_NP">
<?php if ($meta['og_type'] === 'article') : ?>
  <meta property="article:published_time" content="<?php echo esc_attr($meta['published_time']); ?>">
  <meta property="article:modified_time" content="<?php echo esc_attr($meta['modified_time']); ?>">
  <meta property="article:author" content="https://smaranraut.com.np/">
  <meta property="article:section" content="<?php echo esc_attr($meta['section'] ?: 'Search Engine Optimization'); ?>">
<?php endif; ?>

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="<?php echo esc_attr($meta['title']); ?>">
  <meta name="twitter:description" content="<?php echo esc_attr($meta['desc']); ?>">
  <meta name="twitter:image" content="<?php echo esc_url($meta['og_image']); ?>">
  <meta name="twitter:image:alt" content="<?php echo esc_attr($meta['image_alt']); ?>">
    <?php
}
add_action('wp_head', 'smaran_seo_render_metadata', 1);
"""

out_php = os.path.join(inc_dir, 'seo-metadata.php')
with open(out_php, 'w', encoding='utf-8') as f:
    f.write(php_code)
print(f"Generated {out_php}")
