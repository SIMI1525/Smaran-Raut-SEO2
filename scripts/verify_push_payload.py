import subprocess
import json
import hashlib
import os

GH_CLI = r'C:\Program Files\GitHub CLI\gh.exe'
REPO = 'SIMI1525/Smaran-Raut-SEO2'
LOCAL_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

# Get latest remote commit & tree
res = subprocess.run([GH_CLI, 'api', f'repos/{REPO}/git/ref/heads/main'], capture_output=True, text=True, check=True)
latest_sha = json.loads(res.stdout)['object']['sha']

res = subprocess.run([GH_CLI, 'api', f'repos/{REPO}/git/commits/{latest_sha}'], capture_output=True, text=True, check=True)
base_tree_sha = json.loads(res.stdout)['tree']['sha']

res = subprocess.run([GH_CLI, 'api', '--method', 'GET', f'repos/{REPO}/git/trees/{base_tree_sha}', '-f', 'recursive=1'], capture_output=True, text=True, check=True)
remote_blobs = {item['path']: item['sha'] for item in json.loads(res.stdout).get('tree', []) if item['type'] == 'blob'}

sha1 = hashlib.sha1

changed_files = []
for root, dirs, files in os.walk(LOCAL_DIR):
    if '.git' in root or 'scripts' in root:
        continue
    for f in files:
        if f in ['push-to-github.ps1', 'test.json', 'test.txt'] or f.endswith('.bak'):
            continue
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, LOCAL_DIR).replace('\\', '/')
        
        with open(full_path, 'rb') as fp:
            bytes_data = fp.read()
        
        header = f"blob {len(bytes_data)}\0".encode('ascii')
        local_sha = hashlib.sha1(header + bytes_data).hexdigest()
        
        if rel_path not in remote_blobs or remote_blobs[rel_path] != local_sha:
            changed_files.append((rel_path, 'NEW' if rel_path not in remote_blobs else 'MODIFIED', len(bytes_data)))

print(f"Total files in commit: {len(changed_files)}")
print("\nNew files:")
for p, status, sz in changed_files:
    if status == 'NEW':
        print(f"  + {p} ({sz} bytes)")

print("\nSample modified files:")
for p, status, sz in changed_files[:15]:
    if status == 'MODIFIED':
        print(f"  M {p} ({sz} bytes)")
