import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

service_h1s = {
    "core-web-vitals-speed": "Website Speed Optimization & Ongoing Maintenance",
    "ecommerce-seo-nepal": "E-Commerce SEO & Online Store Optimization in Nepal",
    "enterprise-link-building": "Ongoing Website Management & Search Visibility Growth",
    "local-seo-itahari": "Local SEO & Google Business Profile Ranking in Itahari & Eastern Nepal",
    "semantic-content-strategy": "Content Strategy & Search Topic Optimization",
    "seo-optimized-web-development": "Fast, SEO-Optimized Website Development for Businesses in Nepal",
    "technical-seo-audit": "SEO Health Checks & Ranking Fixes for Existing Websites",
    "services": "Services Overview"
}

def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&amp;', '&')
    return ' '.join(t.split())

for f in sorted(blog_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    
    # find links to services in the last section
    h2s = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', c))
    if not h2s:
        continue
    last_h2_pos = h2s[-1].start()
    last_section = c[last_h2_pos:]
    
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/([^/]*)/?[^"\']*)["\'][^>]*>(.*?)</a>', last_section)
    print(f"=== {slug} ===")
    print(f"Last H2: {clean(h2s[-1].group(1))}")
    if not links:
        print("  NO SERVICE LINK IN LAST SECTION!")
    for href, target_svc, anc in links:
        anc_clean = clean(anc)
        svc_key = target_svc if target_svc in service_h1s else ("services" if "services/index.html" in href else target_svc)
        expected_h1 = service_h1s.get(svc_key, "UNKNOWN")
        match = (anc_clean.lower() == expected_h1.lower())
        print(f"  Target: {svc_key} | Match: {match}")
        print(f"    Anchor:   [{anc_clean}]")
        print(f"    Expected: [{expected_h1}]")
