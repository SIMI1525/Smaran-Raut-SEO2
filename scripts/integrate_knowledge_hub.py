import os

header_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\header.php"
page_blog_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\page-blog.php"
blog_index_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html"

# 1. Update header.php
with open(header_path, "r", encoding="utf-8") as f:
    header_content = f.read()

target_desktop = """            <a href="<?php echo esc_url(home_url('/blog/')); ?>" class="dropdown-item featured">
              <span class="item-title">Knowledge Hub Directory &rarr;</span>
              <span class="item-desc">Explore practical web &amp; SEO guides</span>
            </a>
            <div class="dropdown-divider"></div>"""

new_desktop = """            <a href="<?php echo esc_url(home_url('/blog/')); ?>" class="dropdown-item featured">
              <span class="item-title">Knowledge Hub Directory &rarr;</span>
              <span class="item-desc">Explore practical web &amp; SEO guides</span>
            </a>
            <div class="dropdown-divider"></div>
            <a href="<?php echo esc_url(home_url('/blog/top-seo-experts-in-nepal/')); ?>" class="dropdown-item">
              <span class="item-title">Top SEO Experts in Nepal</span>
              <span class="item-desc">Editorial directory of leading specialists</span>
            </a>"""

target_mobile = """        <ul class="mobile-submenu" style="display: none;">
          <li><a href="<?php echo esc_url(home_url('/blog/')); ?>"><strong>Knowledge Hub Directory &rarr;</strong></a></li>"""

new_mobile = """        <ul class="mobile-submenu" style="display: none;">
          <li><a href="<?php echo esc_url(home_url('/blog/')); ?>"><strong>Knowledge Hub Directory &rarr;</strong></a></li>
          <li><a href="<?php echo esc_url(home_url('/blog/top-seo-experts-in-nepal/')); ?>"><strong>Top SEO Experts in Nepal</strong></a></li>"""

if "top-seo-experts-in-nepal" not in header_content:
    if target_desktop in header_content:
        header_content = header_content.replace(target_desktop, new_desktop)
    if target_mobile in header_content:
        header_content = header_content.replace(target_mobile, new_mobile)
    with open(header_path, "w", encoding="utf-8") as f:
        f.write(header_content)
    print("Updated header.php successfully!")
else:
    print("header.php already contains top-seo-experts-in-nepal")

# 2. Update page-blog.php
with open(page_blog_path, "r", encoding="utf-8") as f:
    page_blog = f.read()

card_entry_wp = """          <!-- Featured Editorial Directory: Top SEO Experts in Nepal -->
          <div class="article-card blog-article-item" data-tag="technical-seo local-seo" style="border: 2px solid var(--accent-teal);">
            <div class="article-card-meta">
              <span class="badge badge-teal">Editorial Directory</span>
              <span>10 min read</span>
            </div>
            <h4><a href="<?php echo esc_url(home_url('/blog/top-seo-experts-in-nepal/')); ?>">Top SEO Experts in Nepal: Verified Professional Directory</a></h4>
            <p>Curated editorial directory comparing top SEO consultants, technical specialists, and digital agency leaders in Nepal. Features verified profiles, core specialisations, and hiring advice.</p>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: auto;">
              Related Offering: <a href="<?php echo esc_url(home_url('/services/')); ?>">SEO Consulting &amp; Services</a>
            </div>
          </div>\n\n"""

target_grid_wp = '<div class="cards-grid-3" id="blog-articles-grid">'
if "top-seo-experts-in-nepal" not in page_blog:
    if target_grid_wp in page_blog:
        page_blog = page_blog.replace(target_grid_wp, target_grid_wp + "\n" + card_entry_wp)
        page_blog = page_blog.replace("Showing 31 guides", "Showing 32 guides")
        page_blog = page_blog.replace("All Practice Areas (31)", "All Practice Areas (32)")
        with open(page_blog_path, "w", encoding="utf-8") as f:
            f.write(page_blog)
        print("Updated page-blog.php successfully!")
else:
    print("page-blog.php already contains top-seo-experts-in-nepal")

# 3. Update blog/index.html (Static Site)
with open(blog_index_path, "r", encoding="utf-8") as f:
    blog_index = f.read()

card_entry_html = """          <!-- Featured Editorial Directory: Top SEO Experts in Nepal -->
          <div class="article-card blog-article-item" data-tag="technical-seo local-seo" style="border: 2px solid var(--accent-teal);">
            <div class="article-card-meta">
              <span class="badge badge-teal">Editorial Directory</span>
              <span>10 min read</span>
            </div>
            <h4><a href="top-seo-experts-in-nepal/index.html">Top SEO Experts in Nepal: Verified Professional Directory</a></h4>
            <p>Curated editorial directory comparing top SEO consultants, technical specialists, and digital agency leaders in Nepal. Features verified profiles, core specialisations, and hiring advice.</p>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: auto;">
              Related Offering: <a href="../services/index.html">SEO Consulting &amp; Services</a>
            </div>
          </div>\n\n"""

target_grid_html = '<div class="cards-grid-3" id="blog-articles-grid">'
if "top-seo-experts-in-nepal" not in blog_index:
    if target_grid_html in blog_index:
        blog_index = blog_index.replace(target_grid_html, target_grid_html + "\n" + card_entry_html)
        blog_index = blog_index.replace("Showing 31 guides", "Showing 32 guides")
        blog_index = blog_index.replace("All Practice Areas (31)", "All Practice Areas (32)")
        with open(blog_index_path, "w", encoding="utf-8") as f:
            f.write(blog_index)
        print("Updated blog/index.html successfully!")
else:
    print("blog/index.html already contains top-seo-experts-in-nepal")
