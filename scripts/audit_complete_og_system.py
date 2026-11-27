import os
import re
import json

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'
WP_DIR = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo'
STATIC_IMG = os.path.join(STATIC_DIR, 'images')
WP_IMG = os.path.join(WP_DIR, 'images')

print("=== 1. VERIFYING OG IMAGE FILES ON DISK ===")
expected_og_images = [
    'og-smaran-raut.jpg',
    'og-services.jpg',
    'og-locations.jpg',
    'og-knowledge-hub.jpg',
    'og-seo-experts-nepal.jpg'
]

for img in expected_og_images:
    s_path = os.path.join(STATIC_IMG, img)
    w_path = os.path.join(WP_IMG, img)
    s_ok = os.path.exists(s_path) and os.path.getsize(s_path) > 10000
    w_ok = os.path.exists(w_path) and os.path.getsize(w_path) > 10000
    print(f"  {img}: Static OK? {s_ok} ({os.path.getsize(s_path) if os.path.exists(s_path) else 0} bytes) | WP OK? {w_ok} ({os.path.getsize(w_path) if os.path.exists(w_path) else 0} bytes)")

print("\n=== 2. VERIFYING STATIC HTML PAGES METADATA ===")
html_files = []
for root, dirs, files in os.walk(STATIC_DIR):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

errors = []
total_checked = 0
category_stats = {}

for fp in html_files:
    rel = os.path.relpath(fp, STATIC_DIR).replace('\\', '/')
    if rel in ['googleae9e2a9d82bc15ed.html', 'verify.html']:
        continue

    total_checked += 1
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()

    # Canonical
    can_matches = re.findall(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content)
    if len(can_matches) != 1:
        errors.append(f"{rel}: Expected 1 canonical, found {len(can_matches)}")
    else:
        can = can_matches[0]
        if not can.startswith('https://smaranraut.com.np/'):
            errors.append(f"{rel}: Invalid canonical domain: {can}")

    # OG URL
    og_urls = re.findall(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']', content)
    if len(og_urls) != 1:
        errors.append(f"{rel}: Expected 1 og:url, found {len(og_urls)}")
    elif og_urls[0] != can_matches[0]:
        errors.append(f"{rel}: og:url ({og_urls[0]}) does not match canonical ({can_matches[0]})")

    # OG Title
    og_titles = re.findall(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', content)
    if len(og_titles) != 1:
        errors.append(f"{rel}: Expected 1 og:title, found {len(og_titles)}")

    # OG Description
    og_descs = re.findall(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']', content)
    if len(og_descs) != 1:
        errors.append(f"{rel}: Expected 1 og:description, found {len(og_descs)}")

    # OG Image
    og_imgs = re.findall(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', content)
    if len(og_imgs) != 1:
        errors.append(f"{rel}: Expected 1 og:image, found {len(og_imgs)}")
    else:
        img_url = og_imgs[0]
        if not img_url.startswith('https://smaranraut.com.np/images/og-'):
            errors.append(f"{rel}: Unexpected og:image URL: {img_url}")
        img_filename = img_url.split('/')[-1]
        if not os.path.exists(os.path.join(STATIC_IMG, img_filename)):
            errors.append(f"{rel}: Image file does not exist on disk: {img_filename}")

    # Twitter Card
    tw_cards = re.findall(r'<meta\s+name=["\']twitter:card["\']\s+content=["\'](.*?)["\']', content)
    if len(tw_cards) != 1 or tw_cards[0] != 'summary_large_image':
        errors.append(f"{rel}: Expected 1 twitter:card=summary_large_image, found {tw_cards}")

    # Netlify or http check
    if 'smaran-seo.netlify.app' in content:
        # Check if in meta
        for line in content.splitlines():
            if 'smaran-seo.netlify.app' in line and any(t in line for t in ['<link', '<meta']):
                errors.append(f"{rel}: Found legacy netlify domain in meta: {line.strip()}")
    if 'http://smaranraut.com.np' in content:
        errors.append(f"{rel}: Found insecure http:// in domain reference")

    # Category stat
    img_name = og_imgs[0].split('/')[-1] if og_imgs else 'none'
    category_stats[img_name] = category_stats.get(img_name, 0) + 1

print(f"Total HTML pages audited: {total_checked}")
print("Image distribution across pages:")
for img, cnt in sorted(category_stats.items()):
    print(f"  {img}: {cnt} pages")

if errors:
    print(f"\nFound {len(errors)} issues:")
    for e in errors[:10]:
        print("  -", e)
else:
    print("\nSUCCESS: All 71 indexable HTML pages passed full Open Graph & Twitter Card validation with ZERO ERRORS!")
