import os

rm_dir = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\plugins\seo-by-rank-math'
for root, dirs, files in os.walk(rm_dir):
    for f in files:
        if f.endswith('.php'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if "rank_math/head" in c or "wp_head" in c:
                    for line in c.splitlines():
                        if "add_action( 'wp_head'" in line or "add_action('wp_head'" in line:
                            rel = os.path.relpath(fp, rm_dir)
                            print(f'{rel}: {line.strip()[:100]}')
