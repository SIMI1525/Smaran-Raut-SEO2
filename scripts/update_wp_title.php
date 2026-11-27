<?php
define('WP_USE_THEMES', false);
require_once 'C:/Users/BN/Local Sites/smaran-raut/app/public/wp-load.php';
global $wpdb;

$post_id = 149;
wp_update_post([
    'ID' => $post_id,
    'post_title' => 'SEO Experts in Nepal'
]);

$updated = get_post($post_id);
echo "Updated Post ID: " . $updated->ID . " -> Title: " . $updated->post_title . PHP_EOL;
