sitemap_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\sitemap.xml"

with open(sitemap_path, "r", encoding="utf-8") as f:
    text = f.read()

target = '<loc>https://smaranraut.com.np/blog/social-media-and-online-advertising/</loc>'
new_entry = '''  <url>
    <loc>https://smaranraut.com.np/blog/top-seo-experts-in-nepal/</loc>
    <lastmod>2026-11-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''

if 'top-seo-experts-in-nepal' not in text:
    idx = text.find('</url>', text.find(target)) + len('</url>')
    updated = text[:idx] + '\n' + new_entry + text[idx:]
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("Added top-seo-experts-in-nepal to sitemap.xml")
else:
    print("Already in sitemap.xml")

with open(sitemap_path, "r", encoding="utf-8") as f:
    import re
    urls = re.findall(r'<loc>(.*?)</loc>', f.read())
    print("New total URLs in sitemap:", len(urls))
