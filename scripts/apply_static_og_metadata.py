import os
import json
import re

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'
registry_file = os.path.join(STATIC_DIR, 'scripts', 'metadata_registry.json')

with open(registry_file, 'r', encoding='utf-8') as f:
    registry = json.load(f)

# Also index registry by rel_path for direct matching
path_to_data = {}
for url, data in registry.items():
    path_to_data[data['rel_path']] = data

updated_count = 0

for rel_path, data in path_to_data.items():
    full_path = os.path.join(STATIC_DIR, rel_path)
    if not os.path.exists(full_path):
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the <head> section
    head_match = re.search(r'(<head>)(.*?)(</head>)', html, re.DOTALL | re.IGNORECASE)
    if not head_match:
        continue

    head_open = head_match.group(1)
    head_content = head_match.group(2)
    head_close = head_match.group(3)

    # 1. Clean existing OG and Twitter meta tags to prevent any duplicates
    clean_lines = []
    skip = False
    for line in head_content.splitlines():
        trimmed = line.strip()
        # Skip existing OG tags
        if trimmed.startswith('<meta property="og:') or trimmed.startswith('<meta property=\'og:'):
            continue
        if trimmed.startswith('<meta property="article:') or trimmed.startswith('<meta property=\'article:'):
            continue
        # Skip existing Twitter tags
        if trimmed.startswith('<meta name="twitter:') or trimmed.startswith('<meta name=\'twitter:'):
            continue
        # Skip previous comments about social meta
        if '<!-- Open Graph' in trimmed or '<!-- Twitter' in trimmed or '<!-- Social' in trimmed:
            continue
        clean_lines.append(line)

    head_cleaned = "\n".join(clean_lines)

    # 2. Build standardized Social Sharing Block
    canonical = data['canonical']
    title = data['title']
    desc = data['desc']
    og_type = data['og_type']
    og_image = data['og_image']
    image_alt = data['image_alt']

    article_tags = ""
    if og_type == 'article':
        pub = data.get('published_time') or '2026-01-15'
        mod = data.get('modified_time') or '2026-11-25'
        sec = data.get('section') or 'Search Engine Optimization'
        article_tags = f"""  <meta property="article:published_time" content="{pub}">
  <meta property="article:modified_time" content="{mod}">
  <meta property="article:author" content="https://smaranraut.com.np/">
  <meta property="article:section" content="{sec}">
"""

    social_block = f"""
  <!-- Open Graph / Facebook / WhatsApp -->
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Smaran Raut">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:secure_url" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{image_alt}">
  <meta property="og:locale" content="en_NP">
{article_tags}  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="twitter:image:alt" content="{image_alt}">
"""

    # Insert before </head> or after canonical/robots
    # If robots meta exists, place right after robots
    robots_match = re.search(r'(<meta\s+name=["\']robots["\'][^>]*>)', head_cleaned, re.IGNORECASE)
    if robots_match:
        pos = robots_match.end()
        new_head = head_cleaned[:pos] + social_block + head_cleaned[pos:]
    else:
        # Place before </head>
        new_head = head_cleaned + social_block

    new_html = html[:head_match.start(2)] + new_head + html[head_match.end(2):]

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    updated_count += 1

print(f"Successfully applied Open Graph and Twitter metadata to {updated_count} static HTML files!")
