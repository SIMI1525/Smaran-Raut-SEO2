<?php
define('WP_USE_THEMES', false);
require_once 'C:/Users/BN/Local Sites/smaran-raut/app/public/wp-load.php';
global $wpdb;

$post69 = $wpdb->get_row("SELECT * FROM {$wpdb->posts} WHERE ID = 69", ARRAY_A);
echo "Post 69 details:\n";
print_r($post69);

// Check if top-seo-experts-in-nepal exists
$existing = $wpdb->get_row("SELECT * FROM {$wpdb->posts} WHERE post_name = 'top-seo-experts-in-nepal'", ARRAY_A);
if ($existing) {
    echo "\nExisting post found: ID " . $existing['ID'] . "\n";
} else {
    echo "\nPost does not exist in DB yet. Creating it...\n";
    $new_post_id = wp_insert_post([
        'post_title'   => 'Top SEO Experts in Nepal',
        'post_name'    => 'top-seo-experts-in-nepal',
        'post_status'  => 'publish',
        'post_type'    => $post69['post_type'] ?? 'page',
        'post_author'  => 1,
        'post_parent'  => $post69['post_parent'] ?? 0,
        'post_content' => '', // Content is loaded from template-parts/blog/top-seo-experts-in-nepal.php
    ]);
    echo "Created post ID: " . $new_post_id . "\n";
    echo "Permalink: " . get_permalink($new_post_id) . "\n";
}
