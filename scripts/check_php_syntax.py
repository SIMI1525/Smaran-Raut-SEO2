import subprocess
import glob
import os

php_exe = r"C:\Users\BN\AppData\Roaming\Local\lightning-services\php-8.2.29+0\bin\win64\php.exe"
theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

files = glob.glob(os.path.join(theme_dir, "**", "*.php"), recursive=True)
print(f"Total PHP files to check: {len(files)}")

errors = 0
for f in files:
    res = subprocess.run([php_exe, "-l", f], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR in {f}: {res.stderr or res.stdout}")
        errors += 1

if errors == 0:
    print(f"SUCCESS: All {len(files)} PHP theme templates passed syntax check with zero defects!")
else:
    print(f"FAILED: {errors} files had syntax errors.")
