import os
import glob
import re

base_dirs = [
    r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo",
    r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
]

OLD_DOMAIN = "smaran-seo.netlify.app"
NEW_DOMAIN = "smaranraut.com.np"

total_files_modified = 0
total_replacements = 0

for bdir in base_dirs:
    if not os.path.exists(bdir):
        continue
    files = glob.glob(os.path.join(bdir, "**", "*.*"), recursive=True)
    for f in files:
        if ".git" in f or "scripts" in f or ".venv" in f:
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext not in [".html", ".xml", ".txt", ".json", ".js", ".php", ""]:
            continue
        try:
            with open(f, "r", encoding="utf-8") as fp:
                content = fp.read()
            
            if OLD_DOMAIN in content:
                c = content.count(OLD_DOMAIN)
                new_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
                with open(f, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                total_files_modified += 1
                total_replacements += c
                rel = os.path.relpath(f, bdir)
                print(f"[UPDATED] {bdir.split(os.sep)[-1]} -> {rel} ({c} replacements)")
        except Exception as e:
            print(f"[ERROR] {f}: {e}")

print(f"\nMigration finished: {total_files_modified} files modified with {total_replacements} replacements.")
