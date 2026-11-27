import os
import glob
import re

html_base = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
wp_base = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

# 1. Homepage index.html
hp_file = os.path.join(html_base, "index.html")
with open(hp_file, "r", encoding="utf-8") as f:
    hp = f.read()

hp_new = hp.replace(
    "SEO & Web Development &middot; Itahari, Sunsari, Nepal",
    "SEO Optimization &middot; Itahari, Sunsari, Nepal"
).replace(
    "SEO &amp; Web Development &middot; Itahari, Sunsari, Nepal",
    "SEO Optimization &middot; Itahari, Sunsari, Nepal"
)

with open(hp_file, "w", encoding="utf-8") as f:
    f.write(hp_new)
print("Updated index.html")

# 2. WordPress hero.php
hero_wp = os.path.join(wp_base, "template-parts", "hero.php")
with open(hero_wp, "r", encoding="utf-8") as f:
    hwp = f.read()

hwp_new = hwp.replace(
    "SEO & Web Development &middot; Itahari, Sunsari, Nepal",
    "SEO Optimization &middot; Itahari, Sunsari, Nepal"
).replace(
    "SEO &amp; Web Development &middot; Itahari, Sunsari, Nepal",
    "SEO Optimization &middot; Itahari, Sunsari, Nepal"
)

with open(hero_wp, "w", encoding="utf-8") as f:
    f.write(hwp_new)
print("Updated template-parts/hero.php")

# 3. 17 Geo landing pages in HTML
geo_html_files = glob.glob(os.path.join(html_base, "seo-expert-*", "index.html"))
for ghf in geo_html_files:
    with open(ghf, "r", encoding="utf-8") as f:
        c = f.read()
    c_new = re.sub(
        r'SEO\s+(?:&|&amp;)\s+Web\s+Development\s+&middot;\s+Serving',
        'SEO Optimization &middot; Serving',
        c
    )
    with open(ghf, "w", encoding="utf-8") as f:
        f.write(c_new)
print(f"Updated {len(geo_html_files)} geo HTML files")

# 4. 17 Geo templates in WP
geo_wp_files = glob.glob(os.path.join(wp_base, "template-parts", "geo", "*.php"))
for gwf in geo_wp_files:
    with open(gwf, "r", encoding="utf-8") as f:
        c = f.read()
    c_new = re.sub(
        r'SEO\s+(?:&|&amp;)\s+Web\s+Development\s+&middot;\s+Serving',
        'SEO Optimization &middot; Serving',
        c
    )
    with open(gwf, "w", encoding="utf-8") as f:
        f.write(c_new)
print(f"Updated {len(geo_wp_files)} geo WP files")

# 5. scripts/generate-locations.ps1
gen_ps1 = os.path.join(html_base, "scripts", "generate-locations.ps1")
if os.path.exists(gen_ps1):
    with open(gen_ps1, "r", encoding="utf-8") as f:
        ps1 = f.read()
    ps1_new = ps1.replace(
        "SEO &amp; Web Development &middot; Serving $cName, $cDist",
        "SEO Optimization &middot; Serving $cName, $cDist"
    )
    with open(gen_ps1, "w", encoding="utf-8") as f:
        f.write(ps1_new)
    print("Updated generate-locations.ps1")
