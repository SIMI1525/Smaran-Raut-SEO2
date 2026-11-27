import subprocess
import json
import hashlib
import os

GH_CLI = r'C:\Program Files\GitHub CLI\gh.exe'
REPO = 'SIMI1525/Smaran-Raut-SEO2'
LOCAL_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

# 1. Fetch remote commit and tree
cmd = [GH_CLI, 'api', f'repos/{REPO}/git/ref/heads/main']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
ref_data = json.loads(res.stdout)
commit_sha = ref_data['object']['sha']

cmd = [GH_CLI, 'api', f'repos/{REPO}/git/commits/{commit_sha}']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
commit_data = json.loads(res.stdout)
tree_sha = commit_data['tree']['sha']

cmd = [GH_CLI, 'api', '--method', 'GET', f'repos/{REPO}/git/trees/{tree_sha}', '-f', 'recursive=1']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
tree_data = json.loads(res.stdout)

remote_blobs = {}
for item in tree_data.get('tree', []):
    if item['type'] == 'blob':
        remote_blobs[item['path']] = item['sha']

print(f"Remote tree contains {len(remote_blobs)} blobs (commit: {commit_sha[:8]})")
print("Does remote contain 'scripts/'?", any(p.startswith('scripts/') for p in remote_blobs))

# 2. Scan local files
local_files = {}
for root, dirs, files in os.walk(LOCAL_DIR):
    # Exclude internal/temp items
    if '.git' in root or 'scripts' in root:
        continue
    for f in files:
        if f in ['push-to-github.ps1', 'test.json', 'test.txt'] or f.endswith('.bak'):
            continue
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, LOCAL_DIR).replace('\\', '/')
        
        with open(full_path, 'rb') as fp:
            content = fp.read()
        
        # Git blob sha1 format: sha1("blob " + size + "\0" + content)
        header = f"blob {len(content)}\0".encode('ascii')
        sha = hashlib.sha1(header + content).hexdigest()
        local_files[rel_path] = sha

print(f"Local files to consider (excluding scripts/temp): {len(local_files)}")

# 3. Find modified, new, deleted
new_files = []
modified_files = []
identical_files = []

for rel_path, l_sha in local_files.items():
    if rel_path not in remote_blobs:
        new_files.append((rel_path, l_sha))
    elif remote_blobs[rel_path] != l_sha:
        modified_files.append((rel_path, remote_blobs[rel_path], l_sha))
    else:
        identical_files.append(rel_path)

deleted_files = [p for p in remote_blobs if p not in local_files and not p.startswith('scripts/')]

print(f"\n--- AUDIT SUMMARY ---")
print(f"Identical files: {len(identical_files)}")
print(f"Modified files:  {len(modified_files)}")
print(f"New files:       {len(new_files)}")
print(f"Deleted files:   {len(deleted_files)}")

print(f"\n--- NEW FILES ({len(new_files)}) ---")
for p, s in sorted(new_files):
    print("  +", p)

print(f"\n--- MODIFIED FILES ({len(modified_files)}) ---")
for p, r_sha, l_sha in sorted(modified_files)[:30]:
    print("  M", p)
if len(modified_files) > 30:
    print(f"  ... and {len(modified_files) - 30} more modified files")

if deleted_files:
    print(f"\n--- DELETED FILES ({len(deleted_files)}) ---")
    for p in sorted(deleted_files):
        print("  D", p)
