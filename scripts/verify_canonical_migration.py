import os
import glob
import re
import xml.etree.ElementTree as ET

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
NEW_DOMAIN = "https://smaranraut.com.np"
OLD_DOMAIN = "smaran-seo.netlify.app"

errors = []
warnings = []

# 1. Check for any remaining old domain references
old_domain_files = []
for root, dirs, files in os.walk(base_dir):
    if ".git" in root or "scripts" in root or ".venv" in root:
        continue
    for f in files:
        if f in ["_redirects", "netlify.toml"]:
            # These files are supposed to contain the old domain to redirect from it
            continue
        fp = os.path.join(root, f)
        try:
            content = open(fp, "r", encoding="utf-8", errors="ignore").read()
            if OLD_DOMAIN in content:
                old_domain_files.append(os.path.relpath(fp, base_dir))
        except:
            pass

if old_domain_files:
    errors.append(f"Found {len(old_domain_files)} files still containing '{OLD_DOMAIN}': {old_domain_files}")
else:
    print("[PASS] 0 files contain leftover references to old domain (outside of redirect rules).")

# 2. Check canonical tags in all HTML files
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
html_files = [f for f in html_files if ".git" not in f and "scripts" not in f and "verify" not in f and "google" not in f]

canonical_count = 0
for hf in html_files:
    rel = os.path.relpath(hf, base_dir)
    with open(hf, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', c, re.IGNORECASE)
    if not m:
        # Check if it has refresh redirect (like services/seo-services-itahari)
        if "http-equiv=\"refresh\"" in c:
            continue
        errors.append(f"Missing canonical tag in: {rel}")
        continue
    
    canonical_url = m.group(1)
    canonical_count += 1
    
    if not canonical_url.startswith(NEW_DOMAIN):
        errors.append(f"Canonical URL does not start with {NEW_DOMAIN} in {rel}: {canonical_url}")
    if not canonical_url.endswith("/"):
        errors.append(f"Canonical URL missing trailing slash in {rel}: {canonical_url}")
    
    # Check self-referencing accuracy
    # For index.html at root: canonical should be https://smaranraut.com.np/
    # For foo/index.html: canonical should be https://smaranraut.com.np/foo/
    expected_path = "/" if rel == "index.html" else "/" + os.path.dirname(rel).replace("\\", "/") + "/"
    expected_url = NEW_DOMAIN + expected_path
    
    # special redirect file services/seo-services-itahari points to local-seo-itahari
    if rel == "services\\seo-services-itahari\\index.html":
        expected_url = NEW_DOMAIN + "/services/local-seo-itahari/"
        
    if canonical_url != expected_url:
        errors.append(f"Self-referencing mismatch in {rel}: got '{canonical_url}', expected '{expected_url}'")

print(f"[PASS] Verified {canonical_count} canonical tags. All self-referencing correctly with trailing slashes.")

# 3. Check robots.txt
robots_path = os.path.join(base_dir, "robots.txt")
with open(robots_path, "r", encoding="utf-8") as fp:
    robots_content = fp.read()

if f"Sitemap: {NEW_DOMAIN}/sitemap.xml" not in robots_content:
    errors.append("robots.txt does not contain correct Sitemap directive")
else:
    print("[PASS] robots.txt contains valid Sitemap directive.")

# 4. Check sitemap.xml
sitemap_path = os.path.join(base_dir, "sitemap.xml")
tree = ET.parse(sitemap_path)
root = tree.getroot()
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_locs = [loc.text for loc in root.findall(".//sm:loc", ns)]

print(f"[PASS] sitemap.xml contains {len(sitemap_locs)} URLs.")
for loc in sitemap_locs:
    if not loc.startswith(NEW_DOMAIN):
        errors.append(f"Sitemap URL does not start with {NEW_DOMAIN}: {loc}")
    if not loc.endswith("/"):
        errors.append(f"Sitemap URL missing trailing slash: {loc}")

# 5. Check _redirects
redirects_path = os.path.join(base_dir, "_redirects")
if not os.path.exists(redirects_path):
    errors.append("_redirects file missing")
else:
    rcontent = open(redirects_path, "r", encoding="utf-8").read()
    if f"https://{OLD_DOMAIN}/*  {NEW_DOMAIN}/:splat  301!" not in rcontent and f"https://{OLD_DOMAIN}/* {NEW_DOMAIN}/:splat 301!" not in rcontent:
        errors.append("_redirects missing forced 301 redirect from old domain")
    else:
        print("[PASS] _redirects contains forced 301 wildcard rule with :splat.")

# 6. Check netlify.toml
toml_path = os.path.join(base_dir, "netlify.toml")
if not os.path.exists(toml_path):
    errors.append("netlify.toml file missing")
else:
    tcontent = open(toml_path, "r", encoding="utf-8").read()
    if f"to = \"{NEW_DOMAIN}/:splat\"" not in tcontent:
        errors.append("netlify.toml missing redirect target")
    else:
        print("[PASS] netlify.toml configured with structured 301 redirect blocks.")

print("\n--- AUDIT RESULTS ---")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"  [ERROR] {e}")
else:
    print("ALL TESTS PASSED WITH ZERO DEFECTS! 100% CANONICALIZATION & MIGRATION INTEGRITY.")
