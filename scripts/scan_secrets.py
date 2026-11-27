import os
import re

LOCAL_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

# Patterns that might indicate secrets or sensitive credentials
PATTERNS = [
    r'api[_-]?key\s*[:=]\s*["\'][a-zA-Z0-9_\-]{16,}["\']',
    r'secret\s*[:=]\s*["\'][a-zA-Z0-9_\-]{16,}["\']',
    r'password\s*[:=]\s*["\'][^"\']+["\']',
    r'bearer\s+[a-zA-Z0-9_\-\.]{20,}',
    r'ghp_[a-zA-Z0-9]{30,}',
    r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----',
    r'localhost:\d+',
    r'127\.0\.0\.1:\d+',
    r'smaran-raut\.local'
]

findings = []

for root, dirs, files in os.walk(LOCAL_DIR):
    if '.git' in root or 'scripts' in root:
        continue
    for f in files:
        if f in ['push-to-github.ps1', 'test.json', 'test.txt'] or f.endswith(('.jpg', '.png', '.bak')):
            continue
        full = os.path.join(root, f)
        rel = os.path.relpath(full, LOCAL_DIR).replace('\\', '/')
        
        with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
            
        for pat in PATTERNS:
            matches = re.findall(pat, content, re.IGNORECASE)
            for m in matches:
                # Filter out harmless html forms or schema
                if 'id="client-phone"' in str(m) or 'type="password"' in str(m):
                    continue
                findings.append((rel, pat, str(m)[:80]))

print(f"Total sensitive pattern matches found: {len(findings)}")
for rel, pat, match in findings:
    print(f"  {rel}: {match}")
