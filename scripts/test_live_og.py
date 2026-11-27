import urllib.request
import re

urls = [
    ('Homepage', 'http://smaran-raut.local/'),
    ('Directory Article', 'http://smaran-raut.local/blog/top-seo-experts-in-nepal/'),
    ('Service', 'http://smaran-raut.local/services/seo-optimized-web-development/'),
    ('Location', 'http://smaran-raut.local/seo-expert-itahari/'),
    ('About', 'http://smaran-raut.local/about-us/'),
    ('Contact', 'http://smaran-raut.local/contact-us/')
]

for label, u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'facebookexternalhit/1.1'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            og_title = re.search(r'<meta property="og:title" content="([^"]+)"', html)
            og_desc = re.search(r'<meta property="og:description" content="([^"]+)"', html)
            og_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
            og_url = re.search(r'<meta property="og:url" content="([^"]+)"', html)
            og_type = re.search(r'<meta property="og:type" content="([^"]+)"', html)
            tw_card = re.search(r'<meta name="twitter:card" content="([^"]+)"', html)
            print(f'=== {label} ===')
            print('  Status:', resp.status)
            print('  og:title:', og_title.group(1) if og_title else 'MISSING')
            print('  og:url:', og_url.group(1) if og_url else 'MISSING')
            print('  og:type:', og_type.group(1) if og_type else 'MISSING')
            print('  og:image:', og_img.group(1) if og_img else 'MISSING')
            print('  twitter:card:', tw_card.group(1) if tw_card else 'MISSING')
    except Exception as e:
        print(f'=== {label} ERROR: {e} ===')
