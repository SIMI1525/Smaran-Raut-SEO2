<?php
define('WP_USE_THEMES', false);
require_once 'C:/Users/BN/Local Sites/smaran-raut/app/public/wp-load.php';
global $wpdb;
$posts = $wpdb->get_results("SELECT ID, post_title, post_name, post_type FROM {$wpdb->posts} WHERE post_status = 'publish' AND post_type IN ('page', 'post') ORDER BY post_type, post_title");
echo 'Total published posts/pages in DB: ' . count($posts) . PHP_EOL;
foreach ($posts as $p) {
    echo "[{$p->ID}] ({$p->post_type}) {$p->post_name} -> {$p->post_title}" . PHP_EOL;
}
