import os
import glob
import re

blog_files = glob.glob(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html')

broken_links = 0
total_checked = 0

for bf in blog_files:
    dir_name = os.path.dirname(bf)
    with open(bf, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Extract links in header and mobile drawer
    header_drawer = re.search(r'<header class="site-header">[\s\S]*?<main', c)
    if not header_drawer:
        print(f"ERROR: No header+drawer found in {bf}")
        broken_links += 1
        continue
    
    chunk = header_drawer.group(0)
    links = re.findall(r'href="([^"#]+)"', chunk)
    img_srcs = re.findall(r'src="([^"#]+)"', chunk)
    
    for l in links:
        total_checked += 1
        # Resolve target
        target = os.path.normpath(os.path.join(dir_name, l))
        if not os.path.exists(target):
            print(f"BROKEN LINK in {bf}: {l} -> {target}")
            broken_links += 1
            
    for s in img_srcs:
        total_checked += 1
        target = os.path.normpath(os.path.join(dir_name, s))
        if not os.path.exists(target):
            print(f"BROKEN IMG in {bf}: {s} -> {target}")
            broken_links += 1

print(f"Checked {total_checked} links/assets across 33 blog files. Broken count: {broken_links}")
