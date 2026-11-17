import os
import glob
import re

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

print("=================================================================")
print(" NETLIFY FORMS AUTOMATED COMPLIANCE & INTEGRITY AUDIT")
print("=================================================================")

form_names_expected = {
    "consultation-modal": {
        "required_fields": ["client_name", "client_email", "client_phone"],
        "optional_fields": ["client_website", "service_interest", "client_notes", "bot-field", "form-name"]
    },
    "contact-page": {
        "required_fields": ["name", "email", "phone", "message"],
        "optional_fields": ["bot-field", "form-name"]
    },
    "consultation-page": {
        "required_fields": ["name", "email", "phone"],
        "optional_fields": ["website", "focus", "bot-field", "form-name"]
    }
}

detected_forms = {}
validation_errors = []

for hf in html_files:
    if "verify.html" in hf:
        continue
    rel = os.path.relpath(hf, site_dir).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        c = f.read()

    # Find forms
    forms = re.findall(r'<form\b[^>]*>[\s\S]*?</form>', c, re.IGNORECASE)
    for f_html in forms:
        tag_m = re.search(r'<form\b([^>]*)>', f_html, re.IGNORECASE)
        attrs = tag_m.group(1) if tag_m else ""

        name_m = re.search(r'name=["\']([^"\']+)["\']', attrs)
        if not name_m:
            validation_errors.append(f"{rel}: Form missing name attribute: {attrs}")
            continue

        fname = name_m.group(1)
        if fname not in detected_forms:
            detected_forms[fname] = []
        detected_forms[fname].append(rel)

        # Check Netlify attributes
        if 'data-netlify="true"' not in attrs:
            validation_errors.append(f"{rel}: Form '{fname}' missing data-netlify='true'")
        if 'netlify-honeypot="bot-field"' not in attrs:
            validation_errors.append(f"{rel}: Form '{fname}' missing netlify-honeypot='bot-field'")
        if 'method="POST"' not in attrs and 'method="post"' not in attrs:
            validation_errors.append(f"{rel}: Form '{fname}' missing method='POST'")

        # Check hidden form-name
        if f'name="form-name" value="{fname}"' not in f_html:
            validation_errors.append(f"{rel}: Form '{fname}' missing hidden form-name input")

        # Check honeypot input
        if 'name="bot-field"' not in f_html:
            validation_errors.append(f"{rel}: Form '{fname}' missing bot-field honeypot input")

        # Check required fields
        exp = form_names_expected.get(fname)
        if exp:
            for req in exp["required_fields"]:
                if f'name="{req}"' not in f_html:
                    validation_errors.append(f"{rel}: Form '{fname}' missing required field '{req}'")

print(f"\n1. Detected Form Definitions:")
for fname, pages in detected_forms.items():
    print(f"   - Form '{fname}': Present across {len(pages)} static HTML page(s)")

print(f"\n2. Validation & Compliance Check:")
if validation_errors:
    print(f"   [FAIL] Found {len(validation_errors)} error(s):")
    for err in validation_errors[:10]:
        print(f"     - {err}")
else:
    print("   [PASS] 100% of forms satisfy Netlify Forms requirements perfectly!")

# Check JavaScript app.js
app_js_path = os.path.join(site_dir, "js", "app.js")
with open(app_js_path, "r", encoding="utf-8") as f:
    js_c = f.read()

print(f"\n3. JavaScript Submission Handler Check (app.js):")
checks = [
    ("application/x-www-form-urlencoded", "URL-encoded payload"),
    ("URLSearchParams", "FormData serialization"),
    ("form-name", "Hidden form-name injection"),
    ("showToast", "User feedback preserved"),
    ("Submitting...", "Submit button loading state"),
    ("closeModal", "Modal dismissal on completion")
]

for needle, label in checks:
    status = "[PASS]" if needle in js_c else "[FAIL]"
    print(f"   {status} {label} ({needle})")

print("\n=================================================================")
