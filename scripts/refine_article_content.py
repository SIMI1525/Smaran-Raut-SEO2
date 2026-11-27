import re
import os

HTML_FILE = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html'
PHP_FILE = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php'

def update_file(filepath, is_php=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hero Overlay Gradient Brightening
    content = content.replace(
        "rgba(11, 17, 26, 0.84) 0%, rgba(11, 17, 26, 0.95) 100%",
        "rgba(11, 17, 26, 0.60) 0%, rgba(11, 17, 26, 0.78) 100%"
    )

    # 2. Hero lead text simplification
    old_hero_lead = 'A verified editorial directory and comparative analysis of search engine optimization practitioners, consultants, and technical specialists serving businesses across Nepal and international markets.'
    new_hero_lead = 'A verified directory and practical guide to search engine optimization professionals and web development specialists helping businesses in Nepal grow through Google search.'
    content = content.replace(old_hero_lead, new_hero_lead)

    # 3. Editorial intro block simplification
    # Replace the macro context paragraph
    macro_pattern = r'<section class="editorial-intro-block".*?</section>'
    new_intro_block = '''<section class="editorial-intro-block" style="margin-bottom: 2.75rem;">
        <p class="lead-text" style="font-size: 1.15rem; line-height: 1.75; color: #0F172A; margin-bottom: 1.35rem;">
          SEO experts in Nepal are digital professionals who help your website appear higher in Google search results so potential customers can easily discover your business. Instead of relying only on expensive paid ads, an experienced SEO specialist ensures your business appears naturally when people search for your products or services online.
        </p>
        <p style="font-size: 1rem; line-height: 1.7; color: #334155; margin-bottom: 1.35rem;">
          Whether you run a local clinic in Biratnagar, an trekking agency in Pokhara, or an enterprise in Kathmandu, effective search engine optimization connects your business directly with ready-to-buy customers. Below is an independently researched directory of active SEO specialists in Nepal, along with practical guidelines for selecting the right partner for your business goals.
        </p>
      </section>'''
    content = re.sub(macro_pattern, new_intro_block, content, flags=re.DOTALL)

    # 4. Directory intro text under H2 "Directory of Verified SEO Experts in Nepal"
    old_dir_intro_pattern = r'(<h2 id="verified-directory"[^>]*>.*?</h2>\s*<p style="font-size: 1\.05rem;[^"]*">)(.*?)(</p>)'
    new_dir_intro = (
        'This directory presents verified SEO specialists and consultants in Nepal who help businesses improve their online visibility and attract qualified customer inquiries. '
        'Each professional listing includes their core strengths, location, and verified background to help you make an informed hiring decision.'
    )
    content = re.sub(old_dir_intro_pattern, r'\g<1>' + new_dir_intro + r'\g<3>', content, flags=re.DOTALL)

    # 5. How to Choose an SEO Expert in Nepal (H2 & Criteria H3s)
    old_eval_intro_pattern = r'(<h2 id="evaluation-criteria"[^>]*>.*?</h2>\s*<p style="font-size: 1\.05rem;[^"]*">)(.*?)(</p>)'
    new_eval_intro = (
        'Choosing an SEO expert in Nepal means finding a trustworthy partner who understands your business goals and delivers measurable customer growth rather than empty promises. '
        'Before hiring any specialist or agency, evaluate their experience across these five practical standards:'
    )
    content = re.sub(old_eval_intro_pattern, r'\g<1>' + new_eval_intro + r'\g<3>', content, flags=re.DOTALL)

    # Criteria 1: Technical Audit Depth
    c1_pattern = r'(<div class="step-badge">1</div>\s*<h3[^>]*>.*?</h3>\s*<p[^>]*>)(.*?)(</p>)'
    new_c1 = (
        'A technical audit checks whether search engines can easily find, read, and load your website pages without errors. '
        'A qualified specialist identifies slow loading pages, broken links, mobile usability issues, and confusing navigation paths that prevent Google from ranking your site properly.'
    )
    content = re.sub(c1_pattern, r'\g<1>' + new_c1 + r'\g<3>', content, flags=re.DOTALL)

    # Criteria 2: Local Map Pack Optimization
    c2_pattern = r'(<div class="step-badge">2</div>\s*<h3[^>]*>.*?</h3>\s*<p[^>]*>)(.*?)(</p>)'
    new_c2 = (
        'Local search optimization helps nearby customers find your business on Google Maps and local search results when they search for your services in your city. '
        'Your SEO consultant should optimize your Google Business Profile, verify your business contact details, and collect genuine client reviews to help you capture high-intent local buyers.'
    )
    content = re.sub(c2_pattern, r'\g<1>' + new_c2 + r'\g<3>', content, flags=re.DOTALL)

    # Criteria 3: Verifiable Case Studies & Evidence
    c3_pattern = r'(<div class="step-badge">3</div>\s*<h3[^>]*>.*?</h3>\s*<p[^>]*>)(.*?)(</p>)'
    new_c3 = (
        'Verifiable case studies show real examples of how a specialist helped past clients increase their search rankings, website traffic, and customer leads. '
        'Ask candidates to demonstrate tangible improvements they achieved for businesses with similar competition levels and market conditions in Nepal.'
    )
    content = re.sub(c3_pattern, r'\g<1>' + new_c3 + r'\g<3>', content, flags=re.DOTALL)

    # Criteria 4: Transparent Business-First KPIs
    c4_pattern = r'(<div class="step-badge">4</div>\s*<h3[^>]*>.*?</h3>\s*<p[^>]*>)(.*?)(</p>)'
    new_c4 = (
        'Business-first SEO tracking focuses on real business outcomes like phone calls, WhatsApp messages, form inquiries, and sales rather than meaningless vanity numbers. '
        'A dedicated consultant sets up clear tracking so you always know exactly how your SEO investment is contributing to your company revenue.'
    )
    content = re.sub(c4_pattern, r'\g<1>' + new_c4 + r'\g<3>', content, flags=re.DOTALL)

    # Criteria 5: Adherence to Google Search Essentials
    c5_pattern = r'(<div class="step-badge">5</div>\s*<h3[^>]*>.*?</h3>\s*<p[^>]*>)(.*?)(</p>)'
    new_c5 = (
        'Following Google\'s official guidelines protects your website from penalties, sudden ranking drops, or being removed from search results. '
        'Never hire practitioners who promise instant overnight rankings using suspicious automated backlinks or hidden text, as these shortcuts carry severe risks of Google penalties.'
    )
    content = re.sub(c5_pattern, r'\g<1>' + new_c5 + r'\g<3>', content, flags=re.DOTALL)

    # 6. Freelance SEO Expert vs SEO Agency
    model_intro_pattern = r'(<h2 id="operational-models"[^>]*>.*?</h2>\s*<p style="font-size: 1\.05rem;[^"]*">)(.*?)(</p>)'
    new_model_intro = (
        'Deciding between an independent freelance SEO expert and a full digital agency depends on your budget, communication preference, and the scope of work your business requires. '
        'Here is a straightforward comparison to help you choose the best arrangement for your company:'
    )
    content = re.sub(model_intro_pattern, r'\g<1>' + new_model_intro + r'\g<3>', content, flags=re.DOTALL)

    # 7. FAQs
    # FAQ 1: Who are the active SEO experts in Nepal?
    faq1_pattern = r'(<summary[^>]*>\s*<h3[^>]*>Who are the active SEO experts in Nepal\?</h3>\s*</summary>\s*<div[^>]*>\s*<p[^>]*>)(.*?)(</p>)'
    new_faq1 = (
        'The active SEO specialists in Nepal include experienced independent consultants and agency directors such as Smaran Raut (Web Developer &amp; SEO Expert in Itahari), Anil Parajuli, Sanjay Sheny, Saroj Bista, Kishor Kumar Maharjan, Diwas K.C., Manoj Yadav, Roshan Shrestha, and Sudit Shrestha. '
        'Each specialist brings distinct strengths in technical optimization, local search, or enterprise digital marketing.'
    )
    content = re.sub(faq1_pattern, r'\g<1>' + new_faq1 + r'\g<3>', content, flags=re.DOTALL)

    # FAQ 2: What does an SEO expert do?
    faq2_pattern = r'(<summary[^>]*>\s*<h3[^>]*>What does an SEO expert do\?</h3>\s*</summary>\s*<div[^>]*>\s*<p[^>]*>)(.*?)(</p>)'
    new_faq2 = (
        'An SEO expert helps your website rank higher on Google search results so potential customers can easily find your business online. '
        'Their day-to-day responsibilities include fixing website speed and mobile display errors, researching what questions and terms your customers type into Google, organizing page content so search engines understand it, and building high-quality local citations to strengthen your credibility.'
    )
    content = re.sub(faq2_pattern, r'\g<1>' + new_faq2 + r'\g<3>', content, flags=re.DOTALL)

    # FAQ 3: How do I choose an SEO consultant in Nepal?
    faq3_pattern = r'(<summary[^>]*>\s*<h3[^>]*>How do I choose an SEO consultant in Nepal\?</h3>\s*</summary>\s*<div[^>]*>\s*<p[^>]*>)(.*?)(</p>)'
    new_faq3 = (
        'Choose an SEO consultant in Nepal by reviewing their track record with past clients, testing how fast and responsive their own website is, and ensuring they explain their strategy in clear business terms. '
        'Avoid specialists who guarantee "#1 rankings overnight" and choose professionals who provide transparent monthly reporting on actual calls, inquiries, and customer leads.'
    )
    content = re.sub(faq3_pattern, r'\g<1>' + new_faq3 + r'\g<3>', content, flags=re.DOTALL)

    # FAQ 4: How much does SEO cost in Nepal?
    faq4_pattern = r'(<summary[^>]*>\s*<h3[^>]*>How much does SEO cost in Nepal\?</h3>\s*</summary>\s*<div[^>]*>\s*<p[^>]*>)(.*?)(</p>)'
    new_faq4 = (
        'Professional SEO services in Nepal typically range from NPR 15,000 to NPR 45,000 per month for local businesses seeking continuous visibility on Google Maps and organic search. '
        'Comprehensive technical website rebuilds, competitive e-commerce campaigns, or international export targeting generally require custom project budgets starting from NPR 50,000 to NPR 150,000+ depending on market competition.'
    )
    content = re.sub(faq4_pattern, r'\g<1>' + new_faq4 + r'\g<3>', content, flags=re.DOTALL)

    # FAQ 5: How long does SEO take to produce measurable results?
    faq5_pattern = r'(<summary[^>]*>\s*<h3[^>]*>How long does SEO take to produce measurable results\?</h3>\s*</summary>\s*<div[^>]*>\s*<p[^>]*>)(.*?)(</p>)'
    new_faq5 = (
        'SEO in Nepal typically takes between 3 to 6 months to generate substantial, consistent increases in customer inquiries, phone calls, and sales. '
        'Initial technical improvements, faster page loading, and increased Google search appearances often begin showing positive trends within the first 4 to 8 weeks after launching updates.'
    )
    content = re.sub(faq5_pattern, r'\g<1>' + new_faq5 + r'\g<3>', content, flags=re.DOTALL)

    # 8. Web Development integration section
    webdev_pattern = r'(<h2 id="development-integration"[^>]*>.*?</h2>\s*<p style="font-size: 1\.05rem;[^"]*">)(.*?)(</p>)'
    new_webdev = (
        'Building a website with SEO built-in from day one is essential when an older website has slow loading speeds, broken page code, or confusing structures that cannot be fixed by rewriting text alone. '
        'When your website code is engineered cleanly from the ground up, Google can index your pages immediately, helping you attract qualified customers much faster.'
    )
    content = re.sub(webdev_pattern, r'\g<1>' + new_webdev + r'\g<3>', content, flags=re.DOTALL)

    # 9. CTA Banner at the bottom
    cta_lead_pattern = r'(<h2 style="font-size: 2rem;[^"]*">Ready to Elevate Your Website\'s Search Visibility\?</h2>\s*<p style="font-size: 1\.1rem;[^"]*">)(.*?)(</p>)'
    new_cta_lead = (
        'Whether your business needs a modern, lightning-fast website engineered for Google rankings or a complete SEO strategy to bring more local customers to your door, let\'s discuss your goals.'
    )
    content = re.sub(cta_lead_pattern, r'\g<1>' + new_cta_lead + r'\g<3>', content, flags=re.DOTALL)

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated: {filepath}')

update_file(HTML_FILE, is_php=False)
update_file(PHP_FILE, is_php=True)
