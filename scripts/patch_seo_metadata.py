with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\inc\seo-metadata.php', 'r', encoding='utf-8') as f:
    c = f.read()

# Add filters at the top of seo-metadata.php right after defined check
insertion = """
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
"""

c = c.replace("if (!defined('ABSPATH')) {\n    exit;\n}", "if (!defined('ABSPATH')) {\n    exit;\n}\n" + insertion)

with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\inc\seo-metadata.php', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added anti-duplicate hooks to inc/seo-metadata.php!")
