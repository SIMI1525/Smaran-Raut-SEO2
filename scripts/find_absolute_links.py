import os, glob, re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

absolute_internal_links = []

for f in files:
    rel = os.path.relpath(f, base_dir)
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', c, re.IGNORECASE)
    for l in links:
        if "smaran-seo.netlify.app" in l or "smaranraut.com.np" in l:
            absolute_internal_links.append((rel, l))

print(f"Total absolute internal links found: {len(absolute_internal_links)}")
for r, l in absolute_internal_links:
    print(f"[{r}] -> {l}")
