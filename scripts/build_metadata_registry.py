import os
import re
import json

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

metadata_by_path = {}
metadata_by_canonical = {}

for root, dirs, files in os.walk(STATIC_DIR):
    for f in files:
        if f.endswith('.html'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, STATIC_DIR).replace('\\', '/')
            
            # Skip verification tokens
            if rel_path in ['googleae9e2a9d82bc15ed.html', 'verify.html']:
                continue
                
            with open(full_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Title
            t_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = t_match.group(1).strip() if t_match else 'Smaran Raut | Web Developer & SEO Expert in Nepal'
            
            # Meta description
            d_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
            desc = d_match.group(1).strip() if d_match else 'Professional SEO and website development services in Nepal.'
            
            # Canonical
            c_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
            if c_match:
                canonical = c_match.group(1).strip()
            else:
                if rel_path == 'index.html':
                    canonical = 'https://smaranraut.com.np/'
                else:
                    slug = rel_path.replace('/index.html', '').replace('.html', '')
                    canonical = f'https://smaranraut.com.np/{slug}/'
            
            # H1
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
            h1 = re.sub(r'<[^>]+>', ' ', h1_match.group(1)).strip() if h1_match else ''
            
            # Slug
            if rel_path == 'index.html':
                slug = 'home'
            else:
                slug = rel_path.replace('/index.html', '').replace('.html', '')
                if '/' in slug:
                    slug = slug.split('/')[-1]
                    
            # Determine type, image, alt, etc.
            og_type = 'website'
            published_time = None
            modified_time = None
            section = None
            
            if rel_path.startswith('blog/'):
                if rel_path == 'blog/index.html':
                    og_type = 'website'
                    og_image = 'https://smaranraut.com.np/images/og-knowledge-hub.jpg'
                    image_alt = 'Smaran Raut - SEO & Web Development Knowledge Hub Nepal'
                else:
                    og_type = 'article'
                    section = 'Search Engine Optimization'
                    pub_m = re.search(r'"datePublished":\s*"([^"]+)"', content)
                    mod_m = re.search(r'"dateModified":\s*"([^"]+)"', content)
                    published_time = pub_m.group(1) if pub_m else '2026-01-15'
                    modified_time = mod_m.group(1) if mod_m else '2026-11-25'
                    
                    if rel_path == 'blog/top-seo-experts-in-nepal/index.html':
                        og_image = 'https://smaranraut.com.np/images/og-seo-experts-nepal.jpg'
                        image_alt = 'Top SEO Experts in Nepal - Verified Directory 2026'
                    else:
                        og_image = 'https://smaranraut.com.np/images/og-knowledge-hub.jpg'
                        image_alt = f'{h1 or title} - Smaran Raut Knowledge Hub'
            elif rel_path.startswith('services/'):
                og_type = 'website'
                og_image = 'https://smaranraut.com.np/images/og-services.jpg'
                image_alt = f'{h1 or title} - Smaran Raut Services'
            elif rel_path.startswith('seo-expert-') or rel_path == 'office-location/index.html':
                og_type = 'website'
                og_image = 'https://smaranraut.com.np/images/og-locations.jpg'
                image_alt = f'{h1 or title} - Local SEO in Nepal'
            else:
                og_type = 'website'
                og_image = 'https://smaranraut.com.np/images/og-smaran-raut.jpg'
                image_alt = 'Smaran Raut - Web Developer & SEO Expert in Nepal'
                
            item = {
                'rel_path': rel_path,
                'slug': slug,
                'title': title,
                'desc': desc,
                'canonical': canonical,
                'og_type': og_type,
                'og_image': og_image,
                'image_alt': image_alt,
                'published_time': published_time,
                'modified_time': modified_time,
                'section': section
            }
            metadata_by_path[rel_path] = item
            # Only let non-redirects populate metadata_by_canonical
            if 'http-equiv="refresh"' not in content or canonical not in metadata_by_canonical:
                metadata_by_canonical[canonical] = item

print(f"Total HTML files indexed: {len(metadata_by_path)}")
print(f"Total Canonical URLs indexed: {len(metadata_by_canonical)}")

# Save path registry
out_file = os.path.join(STATIC_DIR, 'scripts', 'metadata_registry.json')
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(metadata_by_path, f, indent=2, ensure_ascii=False)

# Save canonical registry for WordPress
wp_registry_file = os.path.join(STATIC_DIR, 'scripts', 'metadata_canonical_registry.json')
with open(wp_registry_file, 'w', encoding='utf-8') as f:
    json.dump(metadata_by_canonical, f, indent=2, ensure_ascii=False)

print("Saved both path and canonical registries!")
