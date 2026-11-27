const fs = require('fs');
const path = require('path');

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      if (file !== '.git' && file !== '.wrangler' && file !== 'node_modules') {
        results = results.concat(walk(fullPath));
      }
    } else if (file.endsWith('.html')) {
      results.push(fullPath);
    }
  });
  return results;
}

const rootDir = 'C:/Users/BN/.gemini/antigravity/scratch/smaran-raut-seo';
const htmlFiles = walk(rootDir);
let updatedCount = 0;

htmlFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  const original = content;

  content = content.replace(/<form id="consultation-form"(?!\s+action=)/g, '<form id="consultation-form" action="/api/submit"');
  content = content.replace(/<form id="contact-page-form"(?!\s+action=)/g, '<form id="contact-page-form" action="/api/submit"');
  content = content.replace(/<form id="standalone-consultation-form"(?!\s+action=)/g, '<form id="standalone-consultation-form" action="/api/submit"');
  content = content.replace(/app\.js\?v=2026_v5/g, 'app.js?v=2026_v6');

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    updatedCount++;
  }
});

console.log(`Successfully updated ${updatedCount} HTML files with action="/api/submit" and app.js?v=2026_v6`);
