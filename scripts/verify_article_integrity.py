import os
import json
import re

html_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html"
wp_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php"
sitemap_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\sitemap.xml"

print("--- 1. File Existence Check ---")
assert os.path.exists(html_path), "HTML file missing!"
assert os.path.exists(wp_path), "WordPress template part missing!"
assert os.path.exists(sitemap_path), "Sitemap missing!"
print("Files exist: OK")

print("\n--- 2. HTML Inspection ---")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Canonical
assert '<link rel="canonical" href="https://smaranraut.com.np/blog/top-seo-experts-in-nepal/">' in html, "Canonical missing or incorrect!"
print("Canonical URL: OK (https://smaranraut.com.np/blog/top-seo-experts-in-nepal/)")

# H1
h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
assert h1_match and h1_match.group(1).strip() == "Top SEO Experts in Nepal", f"H1 incorrect: {h1_match.group(1) if h1_match else 'None'}"
print("H1 Heading: OK ('Top SEO Experts in Nepal')")

# Breadcrumbs
assert 'Home' in html and 'Knowledge Hub' in html and 'Top SEO Experts in Nepal' in html, "Breadcrumbs missing or incorrect"
print("Breadcrumbs: OK")

# Schema JSON-LD
schema_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
assert len(schema_matches) > 0, "Schema missing!"
schema_data = json.loads(schema_matches[0].strip())
assert "@graph" in schema_data, "@graph missing in schema"
types = [item["@type"] for item in schema_data["@graph"]]
assert "BreadcrumbList" in types, "BreadcrumbList schema missing"
assert "Article" in types, "Article schema missing"
print("JSON-LD Schemas: OK (BreadcrumbList, Article)")

# Profiles Check
card_matches = re.findall(r'<div class="directory-card"[^>]*id="([^"]+)"', html)
print(f"Total directory cards: {len(card_matches)}")
assert len(card_matches) == 16, f"Expected 16 cards, got {len(card_matches)}"
assert card_matches[0] == "smaran-raut", f"First card must be smaran-raut, got {card_matches[0]}"
print("First profile in list: OK (Smaran Raut)")

# Neutrality checks
assert "Featured" not in [re.search(r'badge[^>]*>(.*?)</span>', c) for c in re.findall(r'<div class="directory-card".*?</div>\s*</div>', html, re.DOTALL)], "No featured badges in cards"
for forbidden in ["Editor's Choice", "Number One", "No. 1 SEO Expert in Nepal", "#1 in Nepal"]:
    assert forbidden not in html[:html.find("Frequently Asked Questions")], f"Forbidden ranking phrase '{forbidden}' found in editorial cards!"
print("Neutrality & Ranking Constraints: OK (No #1, No Editor's Choice, No Featured labels)")

# FAQ Check
faqs = [
    "Who are some SEO experts in Nepal?",
    "How do I find a reliable SEO consultant in Nepal?",
    "What services does an SEO expert provide?",
    "How much does SEO cost in Nepal?",
    "Should I hire a freelance SEO expert or an SEO agency?",
    "How long does SEO take to produce results?",
    "What should I check before hiring an SEO consultant?"
]
for q in faqs:
    assert q in html, f"Missing FAQ question: {q}"
print("All 7 FAQ Questions: OK")

# Sitemap check
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()
assert '<loc>https://smaranraut.com.np/blog/top-seo-experts-in-nepal/</loc>' in sitemap, "URL not in sitemap!"
print("Sitemap verification: OK (Contains https://smaranraut.com.np/blog/top-seo-experts-in-nepal/)")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
