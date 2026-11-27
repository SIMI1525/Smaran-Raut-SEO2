import glob
import os

theme_geo = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\geo"

for f in glob.glob(os.path.join(theme_geo, "*.php")):
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    c = c.replace(r"\'", "'")
    c = c.replace(r"\\'", "'")
    with open(f, "w", encoding="utf-8") as fp:
        fp.write(c)

print("Cleaned escaped quotes across all geo templates.")
