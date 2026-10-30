from pathlib import Path
import json
from textwrap import dedent

SITE_DOMAIN = "https://fastsong.eu.org"
SITE_NAME = "FASTSONG"
GOOGLE_VERIFICATION = "xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk"
ADSENSE_ID = "ca-pub-9308517202792186"

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = ''.join(ch if ch.isalnum() or ch in " -_" else "" for ch in text)
    text = text.replace(" ", "-")
    text = text.replace("_", "-")
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def render_head(title: str, description: str, keywords: str, canonical: str):
    return dedent(f"""
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta content='Gw7Z7swUZPrZIYzmklJDBBAZ_T6WcayrdpFYVbQhnEg' name='google-site-verification'/>
      <meta content='xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk' name='google-site-verification'/>
      <meta name="google-site-verification" content="xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk" />
      <meta content='ca-pub-9308517202792186' name='google-adsense-account'/>
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}"></script>
      <meta name="description" content="{description}" />
      <meta name="keywords" content="{keywords}" />
      <meta property="og:type" content="website" />
      <meta property="og:title" content="{title}" />
      <meta property="og:description" content="{description}" />
      <meta property="og:image" content="{SITE_DOMAIN}/assets/images/og-default.jpg" />
      <meta property="og:url" content="{canonical}" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content="{title}" />
      <meta name="twitter:description" content="{description}" />
      <meta name="twitter:image" content="{SITE_DOMAIN}/assets/images/og-default.jpg" />
      <link rel="canonical" href="{canonical}" />
      <link rel="manifest" href="/manifest.json" />
      <link rel="apple-touch-icon" href="/assets/icons/icon-192.png" />
      <meta name="theme-color" content="#0f172a" />
      <meta name="apple-mobile-web-app-capable" content="yes" />
      <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
      <title>{title}</title>
      <link rel="stylesheet" href="/assets/css/style.css" />
      <script defer src="/assets/js/app.js"></script>
    </head>
    """).strip()


def header():
    menu = [
        ("Home", "/"),
        ("Tools", "/tools/"),
        ("Finders", "/finders/"),
        ("Games", "/games/"),
        ("Resources", "/resources/"),
        ("Company", "/company/"),
        ("Contact", "/contact-us/"),
        ("Terms", "/terms/"),
        ("Privacy Policy", "/privacy-policy/"),
    ]
    links = "".join(f"<li><a href='{href}'>{label}</a></li>" for label, href in menu)
    langs = "".join(f"<span>{lang}</span>" for lang in ["English", "Rusia", "Eropa", "Jp", "Id", "Arab"])
    return dedent(f"""
    <header class="site-header">
      <div class="container topbar">
        <div class="logo-box">
          <a href="/" aria-label="FASTSONG Home">
            <img src="/assets/images/logo.png" alt="FASTSONG logo" />
          </a>
        </div>
        <nav>
          <ul class="nav">{links}</ul>
        </nav>
        <div class="lang-switcher">{langs}</div>
      </div>
    </header>
    """).strip()


def footer():
    return dedent(f"""
    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <img src="/assets/images/logo.png" alt="FASTSONG logo" />
          <p>FASTSONG is a modern resource hub for free music downloads, sound effects, creator tools, and media resources.</p>
        </div>
        <div>
          <h4>Tools</h4>
          <ul>
            <li><a href="/tools/">Speech to text software</a></li>
            <li><a href="/tools/">Audio converter</a></li>
            <li><a href="/tools/">MP3 converter</a></li>
            <li><a href="/tools/">MP3 Cutter</a></li>
            <li><a href="/tools/">Video converter</a></li>
          </ul>
        </div>
        <div>
          <h4>Legal</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-us/">About Us</a></li>
            <li><a href="/contact-us/">Contact Us</a></li>
            <li><a href="/privacy-policy/">Privacy Policy</a></li>
            <li><a href="/terms/">Terms of Service</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="/news-update/">News Update</a></li>
            <li><a href="/academy/">Academy</a></li>
            <li><a href="/training/">Training</a></li>
            <li><a href="/partners/">Partner</a></li>
            <li><a href="/advertise/">Advertise</a></li>
          </ul>
        </div>
      </div>
      <div class="copyright">© <a href="{SITE_DOMAIN}">FASTSONG</a> - All Rights Reserved - Powered by <a href="https://relmusic.github.io">Relmusic</a></div>
    </footer>
    """).strip()


def page_html(title: str, description: str, keywords: str, canonical: str, body: str):
    return f"<!DOCTYPE html><html lang='en'>\n{render_head(title, description, keywords, canonical)}\n<body>\n{header()}\n<main>{body}</main>\n{footer()}\n</body></html>\n"


def build_home():
    body = dedent(f"""
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <span class="eyebrow">Royalty Free Music</span>
          <h1>Free Music Download, Sound Effects & Creative Tools</h1>
          <p>FASTSONG helps creators, editors, and media teams access free music, sound effects, music tools, and premium-style resources built for digital publishing.</p>
          <div class="cta-row">
            <a class="btn primary" href="/tools/">Explore Tools</a>
            <a class="btn ghost" href="/blog/">Browse Blog</a>
          </div>
        </div>
        <div class="hero-card">
          <div class="mini-tool"><span>⏱️</span><div><strong>Practice Timer</strong><small>Pomodoro practice timer</small></div></div>
          <div class="mini-tool"><span>🎼</span><div><strong>Pitch Pipe</strong><small>Reference tone generator</small></div></div>
          <div class="mini-tool"><span>⭕</span><div><strong>Circle of Fifths</strong><small>Music theory reference</small></div></div>
        </div>
      </div>
    </section>

    <section class="container section-block">
      <div class="section-head"><h2>Popular Categories</h2></div>
      <div class="category-grid">
        <a class="category-card" href="/blog/instrumental-music/">Instrumental Music</a>
        <a class="category-card" href="/blog/vocal-songs/">Vocal Songs</a>
        <a class="category-card" href="/blog/loops/">Loops</a>
        <a class="category-card" href="/blog/sound-effects/">Sound Effects</a>
        <a class="category-card" href="/blog/technology-tools/">Technology | Tools</a>
        <a class="category-card" href="/blog/people-human/">People | Human</a>
      </div>
    </section>

    <section class="container section-block">
      <div class="section-head"><h2>Popular Posts</h2></div>
      <div class="post-grid">
        <article class="post-card"><div class="tag">Instrumental Music</div><h3>Best royalty free music tools for content creators</h3><a href="/blog/instrumental-music/best-royalty-free-music-tools-for-content-creators.html">Read article</a></article>
        <article class="post-card"><div class="tag">Sound Effects</div><h3>How to choose the right sound effects for video editing</h3><a href="/blog/sound-effects/how-to-choose-right-sound-effects-for-video-editing.html">Read article</a></article>
        <article class="post-card"><div class="tag">Technology | Tools</div><h3>Music production basics for beginners in 2026</h3><a href="/blog/technology-tools/music-production-basics-for-beginners-in-2026.html">Read article</a></article>
      </div>
    </section>

    <section class="container section-block">
      <div class="section-head"><h2>All Tools</h2></div>
      <div class="tool-grid">
        <article class="tool-card"><div class="icon">⏱️</div><h3>Practice Timer</h3><p>Pomodoro-style timer for focused music practice sessions.</p><a href="/tools/practice-timer.html">USE NOW</a></article>
        <article class="tool-card"><div class="icon">🎼</div><h3>Pitch Pipe</h3><p>Reference tones for all 12 chromatic notes. Perfect for singers.</p><a href="/tools/pitch-pipe.html">USE NOW</a></article>
        <article class="tool-card"><div class="icon">⭕</div><h3>Circle of Fifths</h3><p>Interactive diagram showing key relationships and music theory.</p><a href="/tools/circle-of-fifths.html">USE NOW</a></article>
      </div>
    </section>
    """).strip()
    return page_html(
        title="FASTSONG | Royalty Free Music, Sound Effects & Creator Tools",
        description="Download free music, sound effects, and creator tools at FASTSONG. Explore royalty-free resources, articles, and practical audio solutions for modern creators.",
        keywords="royalty free music, free music download, sound effects, music tools, FASTSONG",
        canonical=f"{SITE_DOMAIN}/",
        body=body,
    )


def build_blog_index():
    body = dedent(f"""
    <section class="container page-header"><h1>Blog</h1><p>Discover music inspiration, tools, sound design, production guides, and editorial resources.</p></section>
    <section class="container section-block">
      <div class="post-grid">
        <article class="post-card"><div class="tag">Instrumental Music</div><h3>Best royalty free music tools for content creators</h3><a href="/blog/instrumental-music/best-royalty-free-music-tools-for-content-creators.html">Read article</a></article>
        <article class="post-card"><div class="tag">Sound Effects</div><h3>How to choose the right sound effects for video editing</h3><a href="/blog/sound-effects/how-to-choose-right-sound-effects-for-video-editing.html">Read article</a></article>
        <article class="post-card"><div class="tag">Technology | Tools</div><h3>Music production basics for beginners in 2026</h3><a href="/blog/technology-tools/music-production-basics-for-beginners-in-2026.html">Read article</a></article>
      </div>
    </section>
    """).strip()
    return page_html(
        title="Blog | FASTSONG",
        description="Blog by FASTSONG covering royalty free music, sound effects, content creation, and audio tools.",
        keywords="FASTSONG blog, music blog, sound effects, creator tools",
        canonical=f"{SITE_DOMAIN}/blog/",
        body=body,
    )


def build_tools_index():
    body = dedent(f"""
    <section class="container page-header"><h1>Tools</h1><p>Use practical music and creator tools for practice, theory, editing, and content workflows.</p></section>
    <section class="container section-block">
      <div class="tool-grid">
        <article class="tool-card"><div class="icon">⏱️</div><h3>Practice Timer</h3><p>Pomodoro-style timer for focused music practice sessions.</p><a href="/tools/practice-timer.html">USE NOW</a></article>
        <article class="tool-card"><div class="icon">🎼</div><h3>Pitch Pipe</h3><p>Reference tones for all 12 chromatic notes. Perfect for singers.</p><a href="/tools/pitch-pipe.html">USE NOW</a></article>
        <article class="tool-card"><div class="icon">⭕</div><h3>Circle of Fifths</h3><p>Interactive diagram showing key relationships and music theory.</p><a href="/tools/circle-of-fifths.html">USE NOW</a></article>
      </div>
    </section>
    """).strip()
    return page_html(
        title="Tools | FASTSONG",
        description="Music and creator tools by FASTSONG, including practice timer, pitch pipe, and circle of fifths.",
        keywords="music tools, practice timer, pitch pipe, circle of fifths",
        canonical=f"{SITE_DOMAIN}/tools/",
        body=body,
    )


def build_static_page(title: str, heading: str, description: str):
    body = dedent(f"""
    <section class="container page-header">
      <h1>{heading}</h1>
      <p>{description}</p>
    </section>
    <section class="container section-block">
      <p>FASTSONG is built to provide reliable creative resources, royalty-free music, sound effects, tools, and useful educational content for modern creators.</p>
      <p>This page is ready for further editorial updates and can be expanded with detailed FAQ sections, legal details, team information, and relevant resource links.</p>
    </section>
    """).strip()
    return page_html(
        title=title,
        description=description,
        keywords="FASTSONG, media resources, privacy, legal, contact",
        canonical=f"{SITE_DOMAIN}/" + slugify(heading).replace("-policy","-policy").replace("-terms","-terms") + "/",
        body=body,
    )


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_project():
    root = Path("dist")
    write_file(root / "index.html", build_home())
    write_file(root / "blog" / "index.html", build_blog_index())
    write_file(root / "tools" / "index.html", build_tools_index())

    # static legal pages
    static_pages = {
        "about-us": ("About Us | FASTSONG", "About Us", "Learn more about FASTSONG and our mission to organize creative, music, and audio resources."),
        "contact-us": ("Contact Us | FASTSONG", "Contact Us", "Contact FASTSONG for media, partnership, editorial, and resource or question requests."),
        "terms": ("Terms of Service | FASTSONG", "Terms of Service", "Read the terms of use and service rules for FASTSONG."),
        "privacy-policy": ("Privacy Policy | FASTSONG", "Privacy Policy", "Understand how FASTSONG handles information and user privacy."),
        "news-update": ("News Update | FASTSONG", "News Update", "Keep up with FASTSONG updates, resources, and the latest creative trends."),
        "academy": ("Academy | FASTSONG", "Academy", "Learn practical knowledge about music, sound, media, and production workflows."),
        "training": ("Training | FASTSONG", "Training", "Training content and educational resources for creators, teams, and music enthusiasts."),
        "partners": ("Partners | FASTSONG", "Partners", "Discover partnerships and related creator collaborations supported by FASTSONG."),
        "advertise": ("Advertise | FASTSONG", "Advertise", "Advertise on FASTSONG and reach creators, musicians, and digital media audiences."),
    }
    for slug, data in static_pages.items():
        title, heading, description = data
        write_file(root / f"{slug}.html", build_static_page(title, heading, description))

    # tools pages
    tool_pages = {
        "practice-timer": ("Practice Timer | FASTSONG", "Practice Timer", "Pomodoro-style timer for focused music practice sessions."),
        "pitch-pipe": ("Pitch Pipe | FASTSONG", "Pitch Pipe", "Reference tones for all 12 chromatic notes. Perfect for singers."),
        "circle-of-fifths": ("Circle of Fifths | FASTSONG", "Circle of Fifths", "Interactive diagram showing key relationships and music theory."),
    }
    for slug, data in tool_pages.items():
        title, heading, description = data
        body = dedent(f"""
        <section class="container tool-page">
          <div class="tool-hero">
            <div class="tool-icon">{'⏱️' if 'timer' in slug else '🎼' if 'pitch' in slug else '⭕'}</div>
            <div>
              <h1>{heading}</h1>
              <p>{description}</p>
              <a class="btn primary" href="#">USE NOW</a>
            </div>
          </div>
          <div class="tool-layout">
            <div class="tool-main">
              <h2>How to use this tool</h2>
              <p>Start by selecting the goal or function you want. Adjust the values, parameters, or settings to fit the exercise or project, then apply the result to your workflow.</p>
              <p>These tools are designed to support creativity, structure, and efficiency for musicians, editors, students, and professional content creators.</p>
              <h2>Why it matters</h2>
              <p>Using focused tools helps reduce guesswork, supports consistency, and speeds up content production while preserving quality and sound.</p>
              <h2>Related articles</h2>
              <ul>
                <li><a href="/blog/instrumental-music/best-royalty-free-music-tools-for-content-creators.html">Best royalty free music tools for content creators</a></li>
                <li><a href="/blog/sound-effects/how-to-choose-right-sound-effects-for-video-editing.html">How to choose the right sound effects for video editing</a></li>
                <li><a href="/blog/technology-tools/music-production-basics-for-beginners-in-2026.html">Music production basics for beginners in 2026</a></li>
              </ul>
            </div>
            <aside class="tool-side">
              <h3>Quick Links</h3>
              <ul>
                <li><a href="/tools/">All Tools</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/contact-us/">Contact</a></li>
              </ul>
              <div class="ad-slot">Google Ads</div>
            </aside>
          </div>
        </section>
        """).strip()
        write_file(root / "tools" / f"{slug}.html", page_html(title, description, "FASTSONG tool, music tool, audio tool", f"{SITE_DOMAIN}/tools/{slug}.html", body))

    # article pages
    article_pages = {
        "best-royalty-free-music-tools-for-content-creators": ("Best Royalty Free Music Tools for Content Creators | FASTSONG", "Best Royalty Free Music Tools for Content Creators", "Instrumental Music"),
        "how-to-choose-right-sound-effects-for-video-editing": ("How to Choose the Right Sound Effects for Video Editing | FASTSONG", "How to Choose the Right Sound Effects for Video Editing", "Sound Effects"),
        "music-production-basics-for-beginners-in-2026": ("Music Production Basics for Beginners in 2026 | FASTSONG", "Music Production Basics for Beginners in 2026", "Technology | Tools"),
    }
    for slug, data in article_pages.items():
        title, heading, category = data
        article_body = dedent(f"""
        <article class="container article-wrap">
          <div class="breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / <span>{category}</span></div>
          <h1>{heading}</h1>
          <div class="meta-bar"><span>Category: {category}</span><span>Updated: 2026-10-30</span></div>
          <div class="hero-image-box"><img src="https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=80" alt="{heading}" /></div>
          <div class="toc-box"><h3>Table of Contents</h3><ul><li><a href="#intro">Introduction</a></li><li><a href="#why-it-matters">Why It Matters</a></li><li><a href="#workflow">Workflow</a></li><li><a href="#tips">Tips</a></li><li><a href="#faq">FAQ</a></li><li><a href="#conclusion">Conclusion</a></li></ul></div>
          <div class="article-body">
            <h2 id="intro">Introduction</h2>
            <p>Content creators increasingly need reliable music and sound resources that are fast to access, easy to use, and legally safe for publishing. Royalty-free music plays a central role in helping creators maintain quality while avoiding licensing issues and expensive production bottlenecks.</p>
            <p>When a creator picks the right tool, the impact is visible across the entire production process. The workflow becomes cleaner, the final result feels more refined, and the value of the content increases for viewers. This is why thoughtful selection matters more than simply choosing a random track or sound pack.</p>
            <h2 id="why-it-matters">Why It Matters</h2>
            <p>Modern audiences respond strongly to audio quality. A polished opening, a clean mood fit, and a reliable sound design can make a video or product page feel more professional and trustworthy. Strong sound also supports retention, storytelling, and emotional continuity.</p>
            <p>For creators, the challenge is often not the availability of resources but the ability to choose the right option for the right context. Good curation helps reduce wasted time and improves the consistency of a project across multiple outputs.</p>
            <h2 id="workflow">Workflow</h2>
            <p>To build a sustainable workflow, start by defining your needs, your audience, and your visual tone. Then compare available libraries, tools, and licensing terms. It is important to review whether a piece of audio is truly suitable for commercial use, whether it fits the mood, and whether it will maintain clarity against voiceover or visuals.</p>
            <p>After you identify a sound or music resource, test it in context before final publishing. Listen on different devices, check how it interacts with speech, and confirm whether it supports the stronger emotional direction you want to create.</p>
            <h2 id="tips">Tips</h2>
            <p>Look for quality metadata, clear licensing explanations, and consistent audio production standards. Licensing clarity is especially important for businesses publishing on social media, websites, and branded content. A good library or tool should match your production values and support your publishing goals.</p>
            <p>Use a shortlist approach: keep a small set of trusted resources, evaluate their flexibility, and update your collection based on actual publishing results and audience feedback. This strategy is more efficient than collecting too many random files without any system.</p>
            <div class="faq-section"><h3 id="faq">Frequently Asked Questions</h3><div class="faq-grid"><div class="faq-item"><h4>Q: Is royalty free always safe to use?</h4><p>A: Usually yes, but you still need to review the terms and understand the allowed use cases.</p></div><div class="faq-item"><h4>Q: Can I use music in ads?</h4><p>A: Many royalty-free libraries can be used in ads, but some require extended licenses or commercial terms.</p></div><div class="faq-item"><h4>Q: What matters more: quality or licensing?</h4><p>A: Both matter, but legal clarity is essential before publishing any material.</p></div></div></div>
            <h2 id="conclusion">Conclusion</h2>
            <p>Choosing the right royalty-free music tools is not just a technical choice; it is a creative and strategic decision. The best approach combines quality, legal clarity, and a consistent workflow. When creators make thoughtful choices, the result is clearer storytelling, stronger brand perception, and a smoother production process.</p>
          </div>
        </article>
        """).strip()
        category_path = root / "blog" / slugify(category)
        category_path.mkdir(parents=True, exist_ok=True)
        write_file(category_path / f"{slug}.html", page_html(title, "SEO description for this article.", f"{category.lower()}, royalty free, music tools", f"{SITE_DOMAIN}/blog/{slugify(category)}/{slug}.html", article_body))

    # manifest and other root files
    write_file(root / "manifest.json", json.dumps({
        "name": SITE_NAME,
        "short_name": SITE_NAME,
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0b1020",
        "theme_color": "#0f172a",
        "icons": [{"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}]
    }, indent=2))
    write_file(root / "robots.txt", "User-agent: *\nAllow: /\nSitemap: https://fastsong.eu.org/sitemap.xml\n")
    write_file(root / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://fastsong.eu.org/</loc></url><url><loc>https://fastsong.eu.org/blog/</loc></url><url><loc>https://fastsong.eu.org/tools/</loc></url><url><loc>https://fastsong.eu.org/privacy-policy/</loc></url><url><loc>https://fastsong.eu.org/terms/</loc></url></urlset>')
    write_file(root / "ads.txt", "google.com, pub-9308517202792186, DIRECT, f08c47fec0942fa0\n")
    write_file(root / "app-ads.txt", "google.com, pub-9308517202792186, DIRECT, f08c47fec0942fa0\n")
    write_file(root / "google510371859970acbf.html", '<!doctype html><html><head><meta name="google-site-verification" content="xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk" /></head><body>Google verification</body></html>')
    write_file(root / "feed.xml", '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>FASTSONG</title><link>https://fastsong.eu.org</link><description>FASTSONG blog feed</description><item><title>Best Royalty Free Music Tools for Content Creators</title><link>https://fastsong.eu.org/blog/instrumental-music/best-royalty-free-music-tools-for-content-creators.html</link></item></channel></rss>')

    # assets
    write_file(root / "assets" / "css" / "style.css", """:root{--bg:#07111b;--panel:#0f172a;--text:#edf2ff;--muted:#b8c3d9;--primary:#38bdf8;--accent:#f59e0b;--border:rgba(148,163,184,.16)}*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:linear-gradient(180deg,#07111b,#0d1724 35%,#091421);color:var(--text)}a{color:var(--primary);text-decoration:none}img{max-width:100%;display:block}main{padding-bottom:50px}.container{width:min(1180px,92%);margin:0 auto}.site-header{position:sticky;top:0;background:rgba(7,17,27,.82);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);z-index:10}.topbar{display:flex;justify-content:space-between;align-items:center;gap:18px;padding:14px 0}.logo-box img{max-width:170px}.nav{display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:0;gap:14px}.nav a{color:var(--muted);font-weight:600}.nav a:hover{color:var(--text)}.lang-switcher{display:flex;gap:8px;flex-wrap:wrap;color:var(--muted);font-size:12px}.lang-switcher span{padding:6px 10px;border:1px solid var(--border);border-radius:999px}.hero{padding:70px 0 30px}.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:center}.hero h1{font-size:clamp(2.2rem,4vw,4.2rem);line-height:1.05;margin:0 0 16px}.eyebrow{display:inline-block;padding:8px 12px;border:1px solid var(--border);border-radius:999px;background:rgba(56,189,248,.08);color:var(--primary);font-size:12px;text-transform:uppercase;letter-spacing:.08em}.btn{display:inline-block;padding:12px 18px;border-radius:10px;font-weight:700}.btn.primary{background:var(--primary);color:#03151d}.btn.ghost{border:1px solid var(--border);color:var(--text)}.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.hero-card,.tool-card,.post-card,.category-card,.faq-item,.toc-box,.callout,.tool-side,.article-wrap,.tool-page,.share-box{background:rgba(17,28,45,.72);border:1px solid var(--border);border-radius:18px;box-shadow:0 12px 30px rgba(2,6,23,.15)}.hero-card{padding:22px;display:grid;gap:12px}.mini-tool{display:flex;gap:12px;align-items:center;padding:12px;border:1px solid var(--border);border-radius:12px;background:rgba(148,163,184,.03)}.mini-tool span{font-size:2rem}.section-block{padding:32px 0}.section-head h2{margin:0 0 18px;font-size:2rem}.category-grid,.post-grid,.tool-grid,.faq-grid{display:grid;gap:18px}.category-grid{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}.post-grid,.tool-grid{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.category-card,.post-card,.tool-card{padding:18px;display:block}.category-card{font-weight:700;color:var(--text)} .tag{display:inline-block;padding:6px 10px;border-radius:999px;background:rgba(245,158,11,.12);color:var(--accent);font-size:11px}.tool-card .icon{font-size:2rem}.page-header{padding:50px 0 16px}.page-header h1{font-size:clamp(2.3rem,3vw,3.1rem);margin:0 0 12px}.tool-page,.article-wrap{padding:28px 20px 24px;margin:30px auto}.article-wrap h1,.tool-page h1{font-size:clamp(2.2rem,3vw,3.2rem)}.meta-bar{display:flex;gap:24px;flex-wrap:wrap;color:var(--muted);margin:16px 0}.hero-image-box{margin:18px 0 22px;border-radius:18px;overflow:hidden;border:1px solid var(--border)}.toc-box{padding:18px 20px;margin-bottom:18px}.article-body p,.tool-main p,.tool-main li{color:var(--muted);line-height:1.8}.tool-layout{display:grid;grid-template-columns:1.4fr .6fr;gap:18px;margin-top:20px}.tool-hero{display:grid;grid-template-columns:120px minmax(0,1fr);gap:18px;align-items:center}.tool-icon{height:110px;display:grid;place-items:center;font-size:4rem;border:1px solid var(--border);border-radius:18px;background:rgba(56,189,248,.08)}.ad-slot{min-height:160px;display:grid;place-items:center;color:var(--muted);border:1px solid var(--border);border-radius:12px;margin-top:16px}.site-footer{padding:40px 0 18px;border-top:1px solid var(--border);margin-top:20px;background:rgba(8,15,24,.9)}.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}.footer-grid ul{list-style:none;padding:0;margin:0;line-height:2}.copyright{padding-top:18px;border-top:1px solid var(--border);margin-top:18px;text-align:center;color:var(--muted)}@media(max-width:900px){.hero-grid,.tool-layout,.tool-hero{grid-template-columns:1fr}.topbar{display:block}.nav{justify-content:center;margin:12px 0}.lang-switcher{justify-content:center}}@media(max-width:560px){.cta-row{display:block}.btn{width:100%;text-align:center}.nav{justify-content:center}}""")
    write_file(root / "assets" / "js" / "app.js", "document.addEventListener('DOMContentLoaded', ()=>{document.querySelectorAll('.nav a').forEach(a=>a.classList.add('nav-link'));});")

    # placeholder icons/images
    for p in [root / "assets" / "icons" / "icon-192.png", root / "assets" / "icons" / "icon-512.png", root / "assets" / "images" / "og-default.jpg", root / "assets" / "images" / "logo.png"]:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"")

if __name__ == "__main__":
    build_project()
    print("FASTSONG website generated successfully in dist/ using domain https://fastsong.eu.org")
