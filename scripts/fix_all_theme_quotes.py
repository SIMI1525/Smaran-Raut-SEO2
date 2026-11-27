import glob
import os

theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

for f in glob.glob(os.path.join(theme_dir, "**", "*.php"), recursive=True):
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    if r"\'" in c:
        c = c.replace(r"\'", "'")
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(c)
        print(f"Cleaned {os.path.basename(f)}")

print("Scan and fix complete.")
