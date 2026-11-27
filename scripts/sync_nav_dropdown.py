import os
import glob
import re

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
target_file = os.path.join(site_dir, "blog", "top-seo-experts-in-nepal", "index.html")

html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

updated_count = 0

for hf in html_files:
    if "verify.html" in hf or os.path.samefile(hf, target_file):
        continue
        
    doc_dir = os.path.dirname(hf)
    rel_target = os.path.relpath(target_file, doc_dir).replace('\\', '/')
    rel_blog = os.path.relpath(os.path.join(site_dir, "blog", "index.html"), doc_dir).replace('\\', '/')
    
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for desktop dropdown
    # Looking for Knowledge Hub featured item followed by divider
    desktop_pattern = r'(<a\s+href="[^"]*blog(?:/index\.html)?"\s+class="dropdown-item featured"[^>]*>.*?</a>\s*<div class="dropdown-divider"></div>)'
    
    # We want to add the Top SEO Experts entry right after divider
    desktop_entry = f'''
            <a href="{rel_target}" class="dropdown-item">
              <span class="item-title">Top SEO Experts in Nepal</span>
              <span class="item-desc">Editorial directory of leading specialists</span>
            </a>'''
            
    # Pattern for mobile drawer
    mobile_pattern = r'(<li><a\s+href="[^"]*blog(?:/index\.html)?"[^>]*><strong>Knowledge Hub Directory &rarr;</strong></a></li>)'
    mobile_entry = f'''
          <li><a href="{rel_target}"><strong>Top SEO Experts in Nepal</strong></a></li>'''

    changed = False
    if "top-seo-experts-in-nepal" not in content:
        if re.search(desktop_pattern, content, re.DOTALL):
            content = re.sub(desktop_pattern, r'\1' + desktop_entry, content, count=1, flags=re.DOTALL)
            changed = True
        if re.search(mobile_pattern, content):
            content = re.sub(mobile_pattern, r'\1' + mobile_entry, content, count=1)
            changed = True

    if changed:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Updated navigation dropdown in {updated_count} HTML files!")
