with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\header.php', encoding='utf-8') as f:
    c = f.read()
import re
print('Canonical in WP header:', re.findall(r'<link[^>]*rel=["\']canonical["\'].*?>', c))
print('OG url in WP header:', re.findall(r'<meta[^>]*property=["\']og:url["\'].*?>', c))
