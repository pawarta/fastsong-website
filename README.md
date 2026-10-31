# FASTSONG generator

This repository contains a Python static-site generator for FASTSONG with:
- responsive layout
- automatic subfolder generation
- article generation
- category and genre pages
- tools, music downloads page
- SEO metadata, Open Graph, JSON-LD, manifest, sitemap, robots, ads.txt, app-ads.txt
- CNAME for GitHub Pages custom domain: `fastsong.eu.org`

Run:

```bash
python generate_fastsong.py
```

Then upload the contents of the `dist/` folder to GitHub Pages, Netlify, Vercel, or any static hosting provider.

Custom domain:
- `https://fastsong.eu.org`

A `CNAME` file is already generated in the output to support custom domain deployment.
