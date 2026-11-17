import os
import glob
import re

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

gbp_chip_html = """              <a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" class="hero-gbp-chip" title="My Google Business Profile">
                <svg class="gbp-g-icon" width="14" height="14" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
                  <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.34 24 12 24z"/>
                  <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.98 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/>
                  <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.34 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/>
                </svg>
                <span>My Google Business Profile</span>
                <span class="gbp-check">&#10003;</span>
              </a>"""

map_footer_gbp_html = """              <div class="map-footer-item">
                <a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.35rem; color: var(--accent-teal); font-weight: 600; text-decoration: none;">
                  <span>My Google Business Profile &rarr;</span>
                </a>
              </div>"""

html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)
print(f"Total HTML files to process: {len(html_files)}")

updated_count = 0

for hf in html_files:
    if "verify.html" in hf:
        continue

    rel_path = os.path.relpath(hf, site_dir).replace("\\", "/")
    depth = rel_path.count("/")
    prefix = "../" * depth

    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Favicon links in <head>
    if '<link rel="icon"' not in content and '<link rel="apple-touch-icon"' not in content:
        favicons_block = f"""  <!-- Site Icon / Favicons -->
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="{prefix}images/android-chrome-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}images/apple-touch-icon.png">
"""
        # Inject right before </head> or before <link rel="stylesheet"
        if '<link rel="stylesheet"' in content:
            content = content.replace('<link rel="stylesheet"', favicons_block + '  <link rel="stylesheet"', 1)
        elif '</head>' in content:
            content = content.replace('</head>', favicons_block + '</head>', 1)

    # 2. Logo in Header
    # Replace `<div class="logo-icon">SR</div>` with `<img src="{prefix}images/logo.png" alt="Smaran Raut Logo" class="brand-logo-img" width="46" height="46">`
    logo_header_img = f'<img src="{prefix}images/logo.png" alt="Smaran Raut Logo" class="brand-logo-img" width="46" height="46">'
    logo_drawer_img = f'<img src="{prefix}images/logo.png" alt="Smaran Raut Logo" class="brand-logo-img" width="40" height="40">'

    # In mobile drawer
    content = re.sub(
        r'(<div class="mobile-drawer-header">[\s\S]*?)<div class="logo-icon">SR</div>',
        rf'\g<1>{logo_drawer_img}',
        content
    )

    # In main header or remaining logo-icon instances
    content = content.replace('<div class="logo-icon">SR</div>', logo_header_img)

    # 3. Hero GBP chip on Homepage and Geo landing pages
    is_home = (rel_path == "index.html")
    is_geo = rel_path.startswith("seo-expert-")

    if (is_home or is_geo) and 'class="hero-gbp-chip"' not in content:
        # Match <div class="hero-badge-wrap"> ... </span>
        content = re.sub(
            r'(<div class="hero-badge-wrap">\s*<span class="badge badge-verified">[\s\S]*?</span>)',
            rf'\g<1>\n{gbp_chip_html}',
            content
        )

    # 4. Hero SVG Framing Rectangle stroke on Homepage and Geo pages
    if is_home or is_geo:
        content = content.replace(
            '<rect x="20" y="20" width="480" height="360" rx="8" fill="#FAF8F5" stroke="#E5E0D6"/>',
            '<rect x="20" y="20" width="480" height="360" rx="8" fill="#FAF8F5" stroke="#245037" stroke-width="2"/>'
        )

    # 5. Location map card GBP link on Geo landing pages
    if is_geo and 'CXbkZaR8nj4kEBM/review' not in content:
        if '<div class="location-map-footer">' in content and 'My Google Business Profile' not in content:
            content = re.sub(
                r'(<div class="location-map-footer">[\s\S]*?<span><strong>Exact Coordinates:</strong>[\s\S]*?</div>)',
                rf'\g<1>\n{map_footer_gbp_html}',
                content
            )

    # 6. Contact Page & Office Location Page
    if rel_path == "contact-us/index.html":
        if 'My Google Business Profile &rarr;' not in content:
            content = content.replace(
                '<p style="margin-bottom: 0.5rem;"><strong>Coordinates:</strong> 26.6646&deg; N, 87.2798&deg; E</p>',
                '<p style="margin-bottom: 0.5rem;"><strong>Coordinates:</strong> 26.6646&deg; N, 87.2798&deg; E</p>\n            <p style="margin-bottom: 0.5rem;"><strong>Google Business Profile:</strong> <a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); font-weight: 600;">My Google Business Profile &rarr;</a></p>'
            )
    elif rel_path == "office-location/index.html":
        if 'My Google Business Profile &rarr;' not in content:
            content = content.replace(
                '<p style="margin-bottom: 0.5rem;"><strong>GPS Coordinates:</strong> 26.661694&deg; N, 87.275194&deg; E (Itahari Chowk, Janta Galli)</p>',
                '<p style="margin-bottom: 0.5rem;"><strong>GPS Coordinates:</strong> 26.661694&deg; N, 87.275194&deg; E (Itahari Chowk, Janta Galli)</p>\n            <p style="margin-bottom: 0.5rem;"><strong>Google Business Profile:</strong> <a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); font-weight: 600;">My Google Business Profile &rarr;</a></p>'
            )

    # 7. Global Footer updates (Company Inquiries & Footer Bottom)
    if 'Google Profile:</strong> <a href="https://g.page/r/CXbkZaR8nj4kEBM/review"' not in content:
        content = re.sub(
            r'(<strong>Inquiries:</strong>\s*contact@smaranraut\.com\.np\s*&middot;\s*<a href="tel:\+9779714539838"[^>]*>\+977 9714539838</a>)',
            r'\g<1><br>\n            <strong>Google Profile:</strong> <a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); text-decoration: none;">Smaran Raut - No.1 SEO Expert in Itahari &rarr;</a>',
            content
        )

    if '<a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); font-size: 0.85rem; margin-right: 1rem;">Smaran Raut - No.1 SEO Expert in Itahari</a>' not in content:
        content = re.sub(
            r'(<div class="footer-bottom">[\s\S]*?<div>\s*)(<a href="[^"]*sitemap[^"]*")',
            r'\g<1><a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); font-size: 0.85rem; margin-right: 1rem;">Smaran Raut - No.1 SEO Expert in Itahari</a>\n          \g<2>',
            content
        )

    if content != orig_content:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated: {rel_path}")

print(f"Total files updated: {updated_count}/{len(html_files)}")
