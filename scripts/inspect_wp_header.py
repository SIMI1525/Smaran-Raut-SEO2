with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\header.php', encoding='utf-8') as f:
    wp_header = f.read()

print("Length of WP header:", len(wp_header))
print("nav-dropdown in WP header:", 'nav-dropdown' in wp_header)
print("mobile-nav-drawer in WP header:", 'mobile-nav-drawer' in wp_header)
print("mobile-menu-toggle in WP header:", 'mobile-menu-toggle' in wp_header)
