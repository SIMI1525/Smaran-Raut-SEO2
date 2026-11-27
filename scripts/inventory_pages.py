import os
import glob
import re

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

for root, dirs, files in os.walk(STATIC_DIR):
    for f in files:
        if f.endswith('.html'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, STATIC_DIR).replace('\\', '/')
            if not rel_path.startswith(('services/', 'blog/', 'about-us/', 'contact-us/')) and rel_path != 'index.html':
                print(rel_path)
