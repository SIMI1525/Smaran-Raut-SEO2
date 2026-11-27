import os
import re

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'
WP_DIR = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo'

print("=== CHECKING WORDPRESS HEADER.PHP ===")
wp_header = os.path.join(WP_DIR, 'header.php')
with open(wp_header, 'r', encoding='utf-8') as f:
    h_content = f.read()

# Find all meta, og, twitter, canonical in header.php
head_section = re.findall(r'<head>.*?</head>', h_content, re.DOTALL)
if head_section:
    print("Found <head> in header.php:")
    print(head_section[0])
else:
    print("No <head> directly in header.php or partial head. Printing first 1000 chars:")
    print(h_content[:1000])

print("\n=== CHECKING WORDPRESS FUNCTIONS.PHP ===")
wp_functions = os.path.join(WP_DIR, 'functions.php')
with open(wp_functions, 'r', encoding='utf-8') as f:
    fn_content = f.read()

for line in fn_content.splitlines():
    if any(k in line.lower() for k in ['opengraph', 'og:', 'twitter:', 'canonical', 'wp_head', 'meta']):
        print("  ", line)

print("\n=== CHECKING STATIC SITE SAMPLE HEADS ===")
samples = [
    os.path.join(STATIC_DIR, 'index.html'),
    os.path.join(STATIC_DIR, 'about-us', 'index.html'),
    os.path.join(STATIC_DIR, 'contact-us', 'index.html'),
    os.path.join(STATIC_DIR, 'blog', 'top-seo-experts-in-nepal', 'index.html'),
    os.path.join(STATIC_DIR, 'services', 'seo-audit-nepal', 'index.html'),
    os.path.join(STATIC_DIR, 'locations', 'itahari', 'index.html')
]

for s in samples:
    if os.path.exists(s):
        with open(s, 'r', encoding='utf-8') as f:
            c = f.read()
        rel = os.path.relpath(s, STATIC_DIR)
        print(f"\n--- {rel} ---")
        m_head = re.search(r'<head>(.*?)</head>', c, re.DOTALL)
        if m_head:
            lines = [l.strip() for l in m_head.group(1).splitlines() if any(tag in l for tag in ['<title', '<meta', '<link rel="canonical"'])]
            for l in lines:
                print(" ", l)
