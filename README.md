FASTSONG Premium Static Generator

This repository now includes a more complete static website generator for FASTSONG using the domain `https://fastsong.eu.org`.

What is included:
- Premium responsive homepage and blog layout
- Music download and genre/category landing pages
- Category pages and article pages
- Support tools and tool landing pages
- SEO metadata, JSON-LD, Open Graph, canonical, adsense, verification
- PWA manifest and root files for static publishing

How to generate the site:

```bash
python generate_fastsong.py
```

The generated upload-ready static output is placed in:

```bash
dist/
```

The static site is designed to be uploaded to:
- Netlify
- Vercel
- GitHub Pages
- cPanel
- S3 static hosting

Notes:
- The domain used is `https://fastsong.eu.org`
- All head metadata includes Google verification and AdSense setup
- The folder is ready for direct upload after generation
