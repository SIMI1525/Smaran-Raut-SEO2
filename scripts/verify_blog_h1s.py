import os
import glob
import re

wp_theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
blog_files = glob.glob(os.path.join(wp_theme_dir, "template-parts", "blog", "*.php"))

print(f"Checking all {len(blog_files)} WordPress blog template files:")
for bf in sorted(blog_files):
    with open(bf, "r", encoding="utf-8") as f:
        c = f.read()
    h1s = re.findall(r'<h1[^>]*>[\s\S]*?</h1>', c)
    if len(h1s) != 1:
        print(f"ERROR: {bf} has {len(h1s)} H1s!")
    else:
        clean = ' '.join(re.sub(r'<[^>]+>', '', h1s[0]).split())
        print(f" - {os.path.basename(bf)}: {clean}")
