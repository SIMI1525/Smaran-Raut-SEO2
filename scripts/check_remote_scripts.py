import subprocess
import json

GH_CLI = r'C:\Program Files\GitHub CLI\gh.exe'
REPO = 'SIMI1525/Smaran-Raut-SEO2'

cmd = [GH_CLI, 'api', f'repos/{REPO}/git/trees/main?recursive=1']
res = subprocess.run(cmd, capture_output=True, text=True, check=True)
data = json.loads(res.stdout)

remote_scripts = [item['path'] for item in data.get('tree', []) if item['path'].startswith('scripts/')]
print(f"Remote contains {len(remote_scripts)} files in scripts/:")
for s in sorted(remote_scripts):
    print(" ", s)
