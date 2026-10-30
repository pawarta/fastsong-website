FASTSONG Premium Editorial Generator

This repository contains a premium static-site generator for FASTSONG using the domain:
https://fastsong.eu.org

Features:
- SEO-ready pages with meta title, description, keywords, Open Graph, canonical links
- Google verification and AdSense metadata
- PWA manifest and root static files
- Responsive premium layout
- Blog categories and article generation
- Download/genre/category pages
- Tool pages and multiple landing sections
- Automatic folder generation for category, genre, blog, and tools
- 35 article pages per category

How to generate the site:

```bash
python generate_fastsong.py
```

Then upload the contents of `dist/` to any static hosting platform such as:
- Netlify
- Vercel
- GitHub Pages
- cPanel
- S3 static hosting

Files included in generated output:
- `dist/index.html`
- `dist/blog/`
- `dist/category/`
- `dist/genre/`
- `dist/tools/`
- `dist/music-downloads/`
- `dist/manifest.json`
- `dist/robots.txt`
- `dist/sitemap.xml`
- `dist/ads.txt`
- `dist/app-ads.txt`
- `dist/google510371859970acbf.html`

This generator is designed to create the final editorial-premium site structure automatically, without needing manual HTML creation for each page.
