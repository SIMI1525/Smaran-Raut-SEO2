import os
import glob
import re

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

missing_assets = []
broken_internal_links = []
checked_files = 0

for hf in html_files:
    if "verify.html" in hf:
        continue
    checked_files += 1
    doc_dir = os.path.dirname(hf)
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    # Check images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in img_srcs:
        if src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
            continue
        # Strip query string
        clean_src = src.split("?")[0]
        full_path = os.path.normpath(os.path.join(doc_dir, clean_src))
        if not os.path.exists(full_path):
            missing_assets.append((os.path.relpath(hf, site_dir), src, full_path))

    # Check favicons / stylesheets
    link_hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
    for href in link_hrefs:
        if href.startswith("http://") or href.startswith("https://") or href.startswith("data:"):
            continue
        clean_href = href.split("?")[0]
        full_path = os.path.normpath(os.path.join(doc_dir, clean_href))
        if not os.path.exists(full_path):
            missing_assets.append((os.path.relpath(hf, site_dir), href, full_path))

    # Check internal relative links
    a_hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    for href in a_hrefs:
        if href.startswith("http://") or href.startswith("https://") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#"):
            continue
        clean_href = href.split("?")[0].split("#")[0]
        if not clean_href:
            continue
        full_path = os.path.normpath(os.path.join(doc_dir, clean_href))
        # If it points to a directory, check for index.html inside
        if os.path.isdir(full_path):
            full_path = os.path.join(full_path, "index.html")
        if not os.path.exists(full_path):
            broken_internal_links.append((os.path.relpath(hf, site_dir), href, full_path))

print(f"Total HTML files verified: {checked_files}")
print(f"Missing Assets / Images: {len(missing_assets)}")
if missing_assets:
    for src_doc, ref, full in missing_assets[:10]:
        print(f"  [MISSING ASSET] In {src_doc}: ref '{ref}' -> {full}")

print(f"Broken Internal Links: {len(broken_internal_links)}")
if broken_internal_links:
    for src_doc, ref, full in broken_internal_links[:10]:
        print(f"  [BROKEN LINK] In {src_doc}: ref '{ref}' -> {full}")
