from pathlib import Path
import json
import re
from textwrap import dedent

SITE_DOMAIN = ""
SITE_NAME = "FASTSONG"
ADSENSE_CLIENT = "ca-pub-9308517202792186"
GOOGLE_VERIFY_1 = "Gw7Z7swUZPrZIYzmklJDBBAZ_T6WcayrdpFYVbQhnEg"
GOOGLE_VERIFY_2 = "xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk"

CATEGORIES = [
    "Instrumental Music",
    "Vocal Songs",
    "Short Cues | Intros",
    "Loops",
    "Sound Effects",
    "Alert",
    "Ambience | Background",
    "Click | Pop | Bell",
    "Clock | Timer | Counter",
    "Comedy | Funny",
    "Hit | Explosion | Impact",
    "Household",
    "Nature | Animal",
    "People | Human",
    "Sci-Fi | Artificial",
    "Swoosh | Rise",
    "Technology | Tools",
    "Macro Economy",
    "Explainers",
    "Manufacturing",
    "Property",
    "Health",
    "Education",
    "Lifestyle",
    "Hospitality",
    "Tech & Media",
    "SMEs",
    "Luxury",
    "Whos Who",
    "International",
    "Local Resources",
    "Politics",
    "Culture",
    "Science",
    "Public Policy",
    "Business News",
    "Sports",
    "Arts",
    "Celebrities",
    "Automotive",
    "Commentary",
    "Interview",
    "Music Instruments",
    "Music Glossary",
    "All Tools",
    "Blog",
    "Playlist Generator",
    "Genre Finder",
    "Playlist Analyzer",
    "Music Free Download",
    "Popular Genre Mood Music for",
    "Royalty Free Music",
    "Free Music Download",
    "Podcast",
    "AI Voice",
    "Text to Speech",
    "Image",
    "Video",
    "Audio",
    "Avatars",
    "Music",
    "API",
    "Promo Pages",
    "Insights",
    "Listen",
    "Catalogue",
    "Genres",
    "Podcasts",
    "Creative Commons",
    "Stock Music",
]

GENRES = [
    "Acoustic",
    "Ambient",
    "African",
    "Arabian",
    "Asian",
    "Beats",
    "Blues",
    "Celtic",
    "Chinese",
    "Classical",
    "Comedy",
    "Drums",
    "Electronic",
    "Fantasy",
    "Flute",
    "Folk",
    "Funky",
    "Guitar",
    "Indian",
    "Japanese",
    "Jazz",
    "LoFi",
    "Nature",
    "Old",
    "Orchestral",
    "Piano",
    "Pop",
    "Rock",
    "Ukulele",
    "Violin",
    "Vocal",
    "Instrumental",
    "Techno",
    "Trap",
    "World",
    "Lullaby",
    "Sitar",
    "Bach",
    "Beethoven",
    "Mozart",
    "Tropical",
    "House",
    "Future Bass",
    "Lounge",
    "Action",
    "Adventure",
    "Aesthetic",
    "Angry",
    "Bright",
    "Calm",
    "Chill",
    "Cute",
    "Cinematic",
    "Dark",
    "Dramatic",
    "Energetic",
    "Epic",
    "Fast",
    "Funny",
    "Happy",
    "Horror",
    "Motivational",
    "Mystery",
    "Noise",
    "Nostalgia",
    "Patriotic",
    "Relaxing",
    "Romantic",
    "Sad",
    "Suspense",
    "Emotional",
    "Sleep",
    "Spiritual",
    "Devotional",
    "Sweet",
    "Study",
    "Autumn",
    "Spring",
    "Summer",
    "Winter",
    "Dreamy",
    "Hopeful",
    "Night",
    "Positive",
    "Upbeat",
    "Uplifting",
    "Sentimental",
    "Dynamic",
    "Hype",
    "Downtempo",
    "Slow",
    "Groovy",
    "Advertising",
    "Birthday",
    "Cartoon",
    "Celebration",
    "Children",
    "Christmas",
    "Cooking",
    "Corporate",
    "Dance",
    "Documentary",
    "Elevator",
    "Games",
    "Halloween",
    "Historical",
    "Intro",
    "Medieval",
    "News",
    "Presentation",
    "Religious",
    "Sports",
    "Technology",
    "Trailer",
    "Vlog",
    "Wedding",
    "Educational",
    "Jingle Bells",
    "Party",
    "New Year",
    "Yoga",
    "Fashion",
    "Holiday",
    "Driving",
    "Waiting",
    "Bird",
    "Fire",
    "Forest",
    "Rain",
    "Typing",
    "Water",
    "Ocean",
    "Button",
    "Police siren",
    "Gun",
    "Heartbeat",
    "Dog",
    "Thunder",
    "Echo",
    "Laughing",
    "Wind",
    "Cat",
    "Doorbell ring",
    "Waterfall",
    "River",
    "Saxophone",
]

TOOLS = [
    {"slug": "practice-timer", "title": "Practice Timer", "icon": "⏱️", "desc": "Pomodoro-style timer for focused music practice sessions."},
    {"slug": "pitch-pipe", "title": "Pitch Pipe", "icon": "🎼", "desc": "Reference tones for all 12 chromatic notes. Perfect for singers."},
    {"slug": "circle-of-fifths", "title": "Circle of Fifths", "icon": "⭕", "desc": "Interactive diagram showing key relationships and music theory."},
    {"slug": "playlist-generator", "title": "Playlist Generator", "icon": "🎵", "desc": "Build a curated playlist from selected genres, moods, and use cases."},
    {"slug": "genre-finder", "title": "Genre Finder", "icon": "🔎", "desc": "Find genres, moods, and use-case recommendations quickly."},
    {"slug": "playlist-analyzer", "title": "Playlist Analyzer", "icon": "📊", "desc": "Review playlist balance and music sequencing for better flow."},
    {"slug": "music-tag-explorer", "title": "Music Tag Explorer", "icon": "🏷️", "desc": "Discover genre, mood, and theme tags for faster sound discovery."},
    {"slug": "mood-matcher", "title": "Mood Matcher", "icon": "🎧", "desc": "Match audio to emotional intent and scene context."},
]

LEGAL_PAGES = {
    "about-us": "About Us",
    "contact-us": "Contact Us",
    "terms": "Terms of Service",
    "privacy-policy": "Privacy Policy",
    "sitemaps": "Sitemaps",
    "rss-xml": "RSS XML",
    "atom-xml": "Atom XML",
    "dmca": "DMCA",
    "disclaimer": "Disclaimer",
    "changelog": "Changelog",
    "partner": "Partner",
    "editorial": "Editorial",
    "advertise": "Advertise",
    "join-the-team": "Join the Team",
    "news-update": "News Update",
    "academy": "Academy",
    "training": "Training",
    "private": "Private",
    "licence": "Licence",
    "choices": "Choices",
    "contact-forum-komunitas": "Contact Forum Komunitas",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value)
    return value.strip("-")


def clean_text(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_head(title: str, description: str, keywords: str, canonical_url: str, og_image: str = f"{SITE_DOMAIN}/assets/images/og-default.jpg"):
    return dedent(f"""
    <head>
        <meta content='Gw7Z7swUZPrZIYzmklJDBBAZ_T6WcayrdpFYVbQhnEg' name='google-site-verification'/>
        <meta content='xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk' name='google-site-verification'/>
        <meta name="google-site-verification" content="xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk" />
        <meta content='ca-pub-9308517202792186' name='google-adsense-account'/><script async='async' crossorigin='anonymous' src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9308517202792186'/><script async='async' custom-element='amp-ad' src='https://cdn.ampproject.org/v0/amp-ad-0.1.js'/>
        <meta content='width=device-width, initial-scale=1' name='viewport'/>
        <title>{clean_text(title)}</title>
        <meta name="description" content="{clean_text(description)}"/>
        <meta name="keywords" content="{clean_text(keywords)}"/>
        <meta property="og:type" content="website"/>
        <meta property="og:title" content="{clean_text(title)}"/>
        <meta property="og:description" content="{clean_text(description)}"/>
        <meta property="og:image" content="{og_image}"/>
        <meta property="og:url" content="{canonical_url}"/>
        <meta name="twitter:card" content="summary_large_image"/>
        <meta name="twitter:title" content="{clean_text(title)}"/>
        <meta name="twitter:description" content="{clean_text(description)}"/>
        <meta name="twitter:image" content="{og_image}"/>
        <link rel="canonical" href="{canonical_url}"/>
        <link rel="manifest" href="/manifest.json"/>
        <meta name="theme-color" content="#0f172a"/>
        <meta name="apple-mobile-web-app-capable" content="yes"/>
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
        <link rel="apple-touch-icon" href="/assets/icons/icon-192.png"/>
        <link rel="stylesheet" href="/assets/css/style.css"/>
        <script defer src="/assets/js/app.js"></script>
        <script type="application/ld+json">
        {{
          "@context": "https://schema.org",
          "@type": "WebPage",
          "name": "{clean_text(title)}",
          "description": "{clean_text(description)}",
          "url": "{canonical_url}",
          "publisher": {{
            "@type": "Organization",
            "name": "FASTSONG",
            "url": "{SITE_DOMAIN}"
          }}
        }}
        </script>
    </head>
    """).strip()


def render_header(active_label="Home"):
    nav_items = [
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
    nav = "".join(f"<li class='nav-item'><a href='{href}' {'class=\'active\'' if label == active_label else ''}>{label}</a></li>" for label, href in nav_items)
    langs = "".join(f"<span>{lang}</span>" for lang in ["English", "Rusia", "Eropa", "Jp", "Id", "Arab"])
    return dedent(f"""
    <header class="site-header">
      <div class="container topbar">
        <div class="brand">
          <a href="/" aria-label="FASTSONG home">
            <img src="/assets/images/logo.svg" alt="FASTSONG logo" />
          </a>
        </div>
        <nav class="main-nav" aria-label="Main navigation">
          <ul>{nav}</ul>
        </nav>
        <div class="lang-switcher" aria-label="language switcher">{langs}</div>
      </div>
    </header>
    """).strip()


def render_footer():
    return dedent(f"""
    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <img src="/assets/images/logo.svg" alt="FASTSONG logo" />
          <p>FASTSONG is a modern resource hub for free music downloads, royalty-free sound collections, creator tools, and editorial resources.</p>
        </div>
        <div>
          <h4>Speech to text software</h4>
          <ul>
            <li><a href="/tools/">Audio converter</a></li>
            <li><a href="/tools/">MP3 converter</a></li>
            <li><a href="/tools/">MP3 Cutter</a></li>
            <li><a href="/tools/">Video converter</a></li>
            <li><a href="/tools/">Vocal remover</a></li>
            <li><a href="/tools/">Stem splitter</a></li>
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
            <li><a href="/dmca/">DMCA</a></li>
          </ul>
        </div>
        <div>
          <h4>Community</h4>
          <ul>
            <li><a href="/news-update/">News Update</a></li>
            <li><a href="/academy/">Academy</a></li>
            <li><a href="/training/">Training</a></li>
            <li><a href="/partner/">Partner</a></li>
            <li><a href="/advertise/">Advertise</a></li>
            <li><a href="/join-the-team/">Join the Team</a></li>
          </ul>
        </div>
      </div>
      <div class="copyright">© <a href="https://fastsong.eu.org">FASTSONG</a> - All Rights Reserved - Powered by <a href="https://relmusic.github.io">Relmusic</a></div>
    </footer>
    """).strip()


def render_page(title: str, description: str, keywords: str, canonical_url: str, content: str, active_label="Home"):
    return f"""<!DOCTYPE html>
<html lang="en">
{render_head(title, description, keywords, canonical_url)}
<body>
{render_header(active_label)}
<main>{content}</main>
{render_footer()}
</body>
</html>
"""


def make_article_body(title: str, category: str, slug: str):
    intro = f"{title} is an essential topic for modern creators and digital publishers because the right music and sound decisions directly impact clarity, audience trust, and content performance. In an ecosystem that rewards highly polished media, sound design is no longer just a background detail; it is part of the viewer experience."
    sections = [
        ("Introduction", intro),
        ("Why It Matters", "Creative projects live or die by how they feel. The moment a viewer hears a mismatched cue, a harsh transition, or a weak mood shift, attention drops. The right sonic treatment supports pacing, emotion, and brand recall. In practical terms, a well-matched soundtrack or sound effect can make an explainer feel more premium and a social video feel more intentional."),
        ("Workflow Strategy", "An effective workflow starts with a clear outcome: what the creator wants the audience to feel and what kind of content the project is meant to support. Once the purpose is clear, the next step is to evaluate library quality, licensing, metadata, and fit with the final use case. A clean process saves time and avoids expensive mistakes later in the editing pipeline."),
        ("Production Tips", "For high-performing work, choose assets based on context, not just popularity. Review tempo, tonal balance, emotional intent, and how the audio complements narration or visual pacing. Small changes in track choice can noticeably affect perceived quality. This is why many creators maintain a curated shortlist of reliable assets instead of hunting endlessly through large collections."),
        ("SEO and Discovery", "The quality of metadata is just as important as sound quality. Titles, descriptions, tags, and internal linking should support discovery. Search-friendly pages help publishers surface their resources, strengthen topical relevance, and create a consistent content system that makes future updates easier to manage."),
        ("Tools and Optimization", "The best creative teams combine library access with workflow tools. A practice timer, a playlist generator, a mood matcher, and a category explorer all reduce friction and help creators decide faster. When these tools are paired with clear editorial structure, content becomes easier to scale and easier to maintain over time."),
        ("Conclusion", f"In short, {title} should be treated as both a creative and strategic decision. The best result is not simply the loudest or most popular option; it is the asset that fits the message, supports the audience experience, and integrates properly with your production system."),
    ]

    body_html = "".join(f"<h2 id='{slugify(label)}'>{label}</h2><p>{text}</p>" for label, text in sections)
    faq_items = [
        ("Why does audio quality matter so much?", "Because it changes the emotional tone of the entire experience and influences whether viewers stay engaged."),
        ("Can I use royalty-free music in commercial content?", "Usually yes, but the license must match your use case, especially for advertising, branding, or large distribution."),
        ("How do I improve music discovery?", "Use categories, tags, keywords, and consistent metadata so your content is easier to find and understand."),
        ("Should I use more than one music source?", "A curated mix of trusted sources usually works better than an endless library without a clear system."),
        ("What is the best workflow for creators?", "Define purpose, shortlist assets, test in context, and refine based on audience reaction and final content quality."),
        ("Does SEO help sound content?", "Yes, strong structure and metadata help both search engines and human readers discover relevant resources."),
    ]
    faq_html = "".join(f"<div class='faq-item'><h4>Q: {q}</h4><p>A: {a}</p></div>" for q, a in faq_items)

    internal_links = [
        f"<a href='/{slugify(category)}/'>Category</a>",
        "<a href='/blog/'>Blog</a>",
        "<a href='/music-downloads/'>Music Downloads</a>",
        "<a href='/tools/'>Tools</a>",
        "<a href='/genre/acoustic/'>Acoustic</a>",
        "<a href='/genre/cinematic/'>Cinematic</a>",
        "<a href='/genre/lofi/'>LoFi</a>",
    ]
    external_links = [
        "<a href='https://www.wikimedia.org/'>Wikimedia</a>",
        "<a href='https://www.youtube.com/'>YouTube</a>",
        "<a href='https://www.spotify.com/'>Spotify</a>",
        "<a href='https://archive.org/'>Internet Archive</a>",
        "<a href='https://www.soundhelix.com/'>SoundHelix</a>",
        "<a href='https://www.freesound.org/'>Freesound</a>",
        "<a href='https://www.bbc.co.uk/'>BBC</a>",
    ]
    images = [
        "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1200&q=80",
    ]
    share_links = """
    <div class="share-box">
      <h3>Share This Article</h3>
      <div class="social-share">
        <a href="https://www.facebook.com/sharer/sharer.php?u={base}">Facebook</a>
        <a href="https://twitter.com/intent/tweet?url={base}">Twitter</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={base}">LinkedIn</a>
      </div>
    </div>
    """.format(base=f"{SITE_DOMAIN}/blog/{slugify(category)}/{slug}.html")

    return dedent(f"""
    <article class="container article-wrap">
      <div class="breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / <span>{category}</span></div>
      <h1>{title}</h1>
      <div class="meta-bar"><span>Category: {category}</span><span>Updated: 2026-10-31</span></div>
      <div class="hero-image-box"><img src="{images[0]}" alt="{title}" /></div>
      <div class="toc-box">
        <h3>Table of Contents</h3>
        <ul>
          <li><a href="#introduction">Introduction</a></li>
          <li><a href="#why-it-matters">Why It Matters</a></li>
          <li><a href="#workflow-strategy">Workflow Strategy</a></li>
          <li><a href="#production-tips">Production Tips</a></li>
          <li><a href="#seo-and-discovery">SEO and Discovery</a></li>
          <li><a href="#tools-and-optimization">Tools and Optimization</a></li>
          <li><a href="#conclusion">Conclusion</a></li>
        </ul>
      </div>
      <div class="article-body">
        {body_html}
        <div class="related-box">
          <h3>Internal Links</h3>
          <p>{' '.join(internal_links)}</p>
          <h3>External Links</h3>
          <p>{' '.join(external_links)}</p>
        </div>
        <div class="gallery-row">
          <img src="{images[1]}" alt="{title} visual 1" />
          <img src="{images[2]}" alt="{title} visual 2" />
        </div>
        <div class="faq-section">
          <h3>Frequently Asked Questions</h3>
          <div class="faq-grid">{faq_html}</div>
        </div>
        <h2 id="conclusion">Conclusion</h2>
        <p>In modern publishing, every sound choice should support the message. Strong audio quality, honest licensing, and a reliable workflow create trust with the audience and keep content sustainable over time. The most effective approach is to combine quality, clarity, and organized creative systems.</p>
        {share_links}
      </div>
    </article>
    """).strip()


def build_article_page(title: str, category: str, slug: str):
    content = make_article_body(title, category, slug)
    return render_page(
        title=f"{title} | FASTSONG",
        description=f"Explore a detailed editorial article about {title.lower()} with expert guidance, workflow advice, and creative discovery insights.",
        keywords=f"{title.lower()}, {category.lower()}, music article, royalty free, audio strategy, creator workflow",
        canonical_url=f"{SITE_DOMAIN}/blog/{slugify(category)}/{slug}.html",
        content=content,
        active_label="Home",
    )


def build_tool_page(tool: dict):
    internal_links = [
        "<a href='/tools/'>All Tools</a>",
        "<a href='/blog/'>Blog</a>",
        "<a href='/music-downloads/'>Music Downloads</a>",
        "<a href='/genre/cinematic/'>Cinematic</a>",
        "<a href='/genre/lofi/'>LoFi</a>",
        "<a href='/genre/acoustic/'>Acoustic</a>",
        "<a href='/genre/horror/'>Horror</a>",
    ]
    external_links = [
        "<a href='https://www.spotify.com/'>Spotify</a>",
        "<a href='https://www.youtube.com/'>YouTube</a>",
        "<a href='https://www.freesound.org/'>Freesound</a>",
        "<a href='https://www.bbc.co.uk/'>BBC</a>",
        "<a href='https://archive.org/'>Archive.org</a>",
        "<a href='https://www.wikimedia.org/'>Wikimedia</a>",
        "<a href='https://archive.org/details/audio'>Audio Archive</a>",
    ]
    content = dedent(f"""
    <section class="container tool-page">
      <div class="tool-hero">
        <div class="tool-icon">{tool['icon']}</div>
        <div>
          <h1>{tool['title']}</h1>
          <p>{tool['desc']}</p>
          <a class="btn primary" href="#">USE NOW</a>
        </div>
      </div>
      <div class="tool-layout">
        <div class="tool-main">
          <h2>How to Use This Tool</h2>
          <p>Choose the intended outcome first. Are you trying to improve focus, match soundtrack mood, or organize a playlist for social publishing? Once the objective is clear, adjust the settings and test the result in the actual content context.</p>
          <p>Good tools reduce planning friction and improve creativity. They help media teams and individual creators work faster while staying consistent with tone and quality.</p>
          <h2>Why This Matters</h2>
          <p>Sound production is not only creative; it is strategic. Playlist flow, mood alignment, and pitch awareness can change how audiences remember your content. A simple tool, when used correctly, can improve entire campaign outcomes.</p>
          <h2>Internal Links</h2>
          <p>{' '.join(internal_links)}</p>
          <h2>External Links</h2>
          <p>{' '.join(external_links)}</p>
          <h2>Popular Related Tools</h2>
          <ul>
            <li><a href="/tools/playlist-generator.html">Playlist Generator</a></li>
            <li><a href="/tools/genre-finder.html">Genre Finder</a></li>
            <li><a href="/tools/playlist-analyzer.html">Playlist Analyzer</a></li>
            <li><a href="/tools/mood-matcher.html">Mood Matcher</a></li>
          </ul>
        </div>
        <aside class="tool-side">
          <h3>Quick Links</h3>
          <ul>
            <li><a href="/tools/practice-timer.html">Practice Timer</a></li>
            <li><a href="/tools/pitch-pipe.html">Pitch Pipe</a></li>
            <li><a href="/tools/circle-of-fifths.html">Circle of Fifths</a></li>
            <li><a href="/tools/playlist-generator.html">Playlist Generator</a></li>
          </ul>
          <div class="ad-slot">AdSense 728x90</div>
        </aside>
      </div>
    </section>
    """).strip()
    return render_page(
        title=f"{tool['title']} | FASTSONG",
        description=f"Use the {tool['title']} tool from FASTSONG for music practice, discovery, mood matching, and production workflows.",
        keywords=f"{tool['title'].lower()}, music tool, creator workflow, audio productivity, FASTSONG",
        canonical_url=f"{SITE_DOMAIN}/tools/{tool['slug']}.html",
        content=content,
        active_label="Tools",
    )


def build_home_page():
    categories = "".join(f"<a class='category-card' href='/category/{slugify(cat)}/'>{cat}</a>" for cat in CATEGORIES[:20])
    posts = "".join(f"<article class='post-card'><div class='tag'>{cat}</div><h3>{cat} for modern creators</h3><a href='/category/{slugify(cat)}/'>Read category</a></article>" for cat in CATEGORIES[:6])
    tool_cards = "".join(f"<article class='tool-card'><div class='icon'>{tool['icon']}</div><h3>{tool['title']}</h3><p>{tool['desc']}</p><a href='/tools/{tool['slug']}.html'>USE NOW</a></article>" for tool in TOOLS)
    genre_cloud = "".join(f"<span>{g}</span>" for g in GENRES[:40])
    content = dedent(f"""
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <span class="eyebrow">Royalty Free Music</span>
          <h1>Free Music Download, Sound Effects, and Creator Tools</h1>
          <p>FASTSONG helps creators, editors, publishers, and teams discover royalty-free music, sound effects, mood-based resources, and AI-powered tools for modern content workflows.</p>
          <div class="cta-row">
            <a class="btn primary" href="/music-downloads/">Download Music</a>
            <a class="btn ghost" href="/blog/">Browse Blog</a>
          </div>
        </div>
        <div class="hero-card">
          <div class="mini-tool"><span>🎵</span><div><strong>Playlist Generator</strong><small>Curate themed playlists</small></div></div>
          <div class="mini-tool"><span>⏱️</span><div><strong>Practice Timer</strong><small>Pomodoro sessions</small></div></div>
          <div class="mini-tool"><span>🎼</span><div><strong>Pitch Pipe</strong><small>Reference tones</small></div></div>
        </div>
      </div>
    </section>
    <section class="container section-block">
      <div class="section-head"><h2>Popular Categories</h2></div>
      <div class="category-grid">{categories}</div>
    </section>
    <section class="container section-block">
      <div class="section-head"><h2>Popular Posts</h2></div>
      <div class="post-grid">{posts}</div>
    </section>
    <section class="container section-block">
      <div class="section-head"><h2>All Tools</h2></div>
      <div class="tool-grid">{tool_cards}</div>
    </section>
    <section class="container section-block">
      <div class="section-head"><h2>Music Genres & Moods</h2></div>
      <div class="genre-cloud">{genre_cloud}</div>
    </section>
    """).strip()
    return render_page(
        title="FASTSONG | Royalty Free Music, Sound Effects & Creator Tools",
        description="FASTSONG provides royalty-free music, sound effects, music tools, genre collections, and creator resources designed for modern digital publishing.",
        keywords="royalty free music, free music download, sound effects, music tools, playlist generator, genre finder, FASTSONG",
        canonical_url=f"{SITE_DOMAIN}/",
        content=content,
        active_label="Home",
    )


def build_blog_index_page():
    cards = "".join(f"<article class='post-card'><div class='tag'>{cat}</div><h3>{cat} collection</h3><a href='/category/{slugify(cat)}/'>Open category</a></article>" for cat in CATEGORIES[:12])
    content = dedent(f"""
    <section class="container page-header">
      <h1>FASTSONG Blog</h1>
      <p>Explore editorials, music discovery, SEO strategy, sound design, tool tutorials, and practical creator guidance.</p>
    </section>
    <section class="container section-block">
      <div class="post-grid">{cards}</div>
    </section>
    """).strip()
    return render_page(
        title="Blog | FASTSONG",
        description="Read editorial content from FASTSONG about music, sound design, royalty free libraries, tools, and modern creator workflow.",
        keywords="FASTSONG blog, music blog, sound effects, productivity tools, music discovery",
        canonical_url=f"{SITE_DOMAIN}/blog/",
        content=content,
        active_label="Home",
    )


def build_tools_page():
    cards = "".join(f"<article class='tool-card'><div class='icon'>{tool['icon']}</div><h3>{tool['title']}</h3><p>{tool['desc']}</p><a href='/tools/{tool['slug']}.html'>USE NOW</a></article>" for tool in TOOLS)
    content = dedent(f"""
    <section class="container page-header">
      <h1>Tools</h1>
      <p>Creative utilities for music practice, discovery, curation, and content planning.</p>
    </section>
    <section class="container section-block">
      <div class="tool-grid">{cards}</div>
    </section>
    """).strip()
    return render_page(
        title="Tools | FASTSONG",
        description="Use FASTSONG tools to generate playlists, practice, find genres, and match audio to mood or audience intent.",
        keywords="music tools, practice timer, pitch pipe, playlist generator, genre finder, mood matcher",
        canonical_url=f"{SITE_DOMAIN}/tools/",
        content=content,
        active_label="Tools",
    )


def build_music_downloads_page():
    genre_links = "".join(f"<a class='tag-item' href='/genre/{slugify(g)}/'>{g}</a>" for g in GENRES[:60])
    category_links = "".join(f"<a class='tag-item' href='/category/{slugify(cat)}/'>{cat}</a>" for cat in CATEGORIES[:25])
    content = dedent(f"""
    <section class="container page-header">
      <h1>Music Downloads</h1>
      <p>Browse royalty-free tracks by mood, genre, and content category for social media, ads, videos, games, and podcasts.</p>
    </section>
    <section class="container section-block">
      <div class="section-box">
        <h2>Popular Genres</h2>
        <div class="tag-cloud">{genre_links}</div>
      </div>
    </section>
    <section class="container section-block">
      <div class="section-box">
        <h2>Popular Categories</h2>
        <div class="tag-cloud">{category_links}</div>
      </div>
    </section>
    """).strip()
    return render_page(
        title="Free Music Downloads | FASTSONG",
        description="Download free music and royalty-free sound resources by genre and category from FASTSONG.",
        keywords="free music download, royalty free music, genre library, music category, FASTSONG",
        canonical_url=f"{SITE_DOMAIN}/music-downloads/",
        content=content,
        active_label="Home",
    )


def build_static_page(title: str, heading: str, description: str, slug: str):
    content = dedent(f"""
    <section class="container page-header">
      <h1>{heading}</h1>
      <p>{description}</p>
    </section>
    <section class="container section-block">
      <p>FASTSONG is built to help creators browse stable and useful music and sound resources, while keeping the editorial structure clean, discoverable, and easy to scale.</p>
      <p>This page is ready for publication and can be expanded with legal copy, detailed information, or richer editorial content if needed.</p>
    </section>
    """).strip()
    return render_page(
        title=title,
        description=description,
        keywords="FASTSONG, music resources, free downloads, digital publishing, creator tools",
        canonical_url=f"{SITE_DOMAIN}/{slug}/",
        content=content,
        active_label="Home",
    )


def build_category_page(category: str):
    article_cards = "".join(f"<article class='post-card'><div class='tag'>{category}</div><h3>{category} guide #{i}</h3><a href='/blog/{slugify(category)}/article-{i}.html'>Read article</a></article>" for i in range(1, 6))
    content = dedent(f"""
    <section class="container page-header">
      <h1>{category}</h1>
      <p>Explore the best content, ideas, and audio-related guidance for {category.lower()}.</p>
    </section>
    <section class="container section-block">
      <div class="post-grid">{article_cards}</div>
    </section>
    """).strip()
    return render_page(
        title=f"{category} | FASTSONG",
        description=f"Explore {category.lower()} resources, articles, and practical creator insights from FASTSONG.",
        keywords=f"{category.lower()}, music resources, royalty free, creator pipeline",
        canonical_url=f"{SITE_DOMAIN}/category/{slugify(category)}/",
        content=content,
        active_label="Home",
    )


def build_genre_page(genre: str):
    category_links = "".join(f"<a class='tag-item' href='/category/{slugify(cat)}/'>{cat}</a>" for cat in CATEGORIES[:12])
    content = dedent(f"""
    <section class="container page-header">
      <h1>{genre} Music</h1>
      <p>Find {genre.lower()} music ideas, sound libraries, and mood-based suggestions for content production, social videos, and media workflows.</p>
    </section>
    <section class="container section-block">
      <div class="section-box">
        <h2>Related Categories</h2>
        <div class="tag-cloud">{category_links}</div>
      </div>
    </section>
    """).strip()
    return render_page(
        title=f"{genre} Music | FASTSONG",
        description=f"Browse {genre.lower()} music suggestions and resources curated by FASTSONG for audio and media production.",
        keywords=f"{genre.lower()} music, royalty free, music downloads, soundtrack library",
        canonical_url=f"{SITE_DOMAIN}/genre/{slugify(genre)}/",
        content=content,
        active_label="Home",
    )


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_svg_logo():
    return """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 360 96'><rect width='360' height='96' rx='18' fill='#0f172a'/><text x='24' y='60' font-family='Arial, sans-serif' font-size='35' font-weight='700' fill='#f8fafc'>FASTSONG</text></svg>"""


def generate_site():
    root = Path('dist')

    write_file(root / 'index.html', build_home_page())
    write_file(root / 'blog' / 'index.html', build_blog_index_page())
    write_file(root / 'music-downloads' / 'index.html', build_music_downloads_page())
    write_file(root / 'tools' / 'index.html', build_tools_page())

    for slug, title in LEGAL_PAGES.items():
        write_file(root / f'{slug}.html', build_static_page(f"{title} | FASTSONG", title, f"{title} for FASTSONG. This page is ready for final editorial or legal expansion.", slug))

    for cat in CATEGORIES:
        write_file(root / 'category' / f'{slugify(cat)}/index.html', build_category_page(cat))

    for genre in GENRES:
        write_file(root / 'genre' / f'{slugify(genre)}/index.html', build_genre_page(genre))

    for tool in TOOLS:
        write_file(root / 'tools' / f"{tool['slug']}.html", build_tool_page(tool))

    for cat in CATEGORIES:
        cat_slug = slugify(cat)
        current_dir = root / 'blog' / cat_slug
        current_dir.mkdir(parents=True, exist_ok=True)
        for i in range(1, 6):
            title = f"{cat} Guide {i}: Creative Workflow, Sound Strategy and SEO-Ready Production"
            page_slug = f"article-{i}"
            write_file(current_dir / f'{page_slug}.html', build_article_page(title, cat, page_slug))

    manifest = {
        "name": SITE_NAME,
        "short_name": SITE_NAME,
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0b1020",
        "theme_color": "#0f172a",
        "icons": [
            {"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    write_file(root / 'manifest.json', json.dumps(manifest, indent=2))
    write_file(root / 'ads.txt', "google.com, pub-9308517202792186, DIRECT, f08c47fec0942fa0\n")
    write_file(root / 'app-ads.txt', "google.com, pub-9308517202792186, DIRECT, f08c47fec0942fa0\n")
    write_file(root / 'google510371859970acbf.html', f"<!doctype html><html><head><meta name='google-site-verification' content='{GOOGLE_VERIFY_2}' /></head><body>Google verification</body></html>")
    write_file(root / 'robots.txt', "User-agent: *\nAllow: /\nSitemap: https://fastsong.eu.org/sitemap.xml\n")
    write_file(root / 'sitemap.xml', "<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'><url><loc>https://fastsong.eu.org/</loc></url><url><loc>https://fastsong.eu.org/blog/</loc></url><url><loc>https://fastsong.eu.org/music-downloads/</loc></url><url><loc>https://fastsong.eu.org/tools/</loc></url><url><loc>https://fastsong.eu.org/privacy-policy/</loc></url><url><loc>https://fastsong.eu.org/terms/</loc></url></urlset>")
    write_file(root / 'feed.xml', "<?xml version='1.0' encoding='UTF-8'?><rss version='2.0'><channel><title>FASTSONG</title><link>https://fastsong.eu.org</link><description>FASTSONG feed</description></channel></rss>")
    write_file(root / 'CNAME', "fastsong.eu.org\n")

    assets = root / 'assets'
    (assets / 'css').mkdir(parents=True, exist_ok=True)
    (assets / 'js').mkdir(parents=True, exist_ok=True)
    (assets / 'icons').mkdir(parents=True, exist_ok=True)
    (assets / 'images').mkdir(parents=True, exist_ok=True)

    write_file(assets / 'css' / 'style.css', """:root{--bg:#07111b;--panel:#0f172a;--text:#edf2ff;--muted:#b8c3d9;--primary:#38bdf8;--accent:#f59e0b;--border:rgba(148,163,184,.2)}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:linear-gradient(180deg,#07111b,#0d1724 35%,#091421);color:var(--text)}a{text-decoration:none;color:var(--primary)}img{max-width:100%;display:block}main{padding-bottom:60px}.container{width:min(1180px,92%);margin:0 auto}.site-header{position:sticky;top:0;z-index:10;background:rgba(7,17,27,.82);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}.topbar{display:flex;justify-content:space-between;align-items:center;gap:18px;padding:14px 0}.brand img{max-width:180px}.main-nav ul{display:flex;list-style:none;padding:0;margin:0;gap:16px;flex-wrap:wrap}.nav-item a{color:var(--muted);font-weight:700}.nav-item a.active,.nav-item a:hover{color:var(--text)}.lang-switcher{display:flex;gap:8px;flex-wrap:wrap}.lang-switcher span{display:inline-block;padding:6px 10px;border:1px solid var(--border);border-radius:999px;color:var(--muted);font-size:12px}.hero{padding:80px 0 30px}.hero-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:26px;align-items:center}.hero h1{font-size:clamp(2.3rem,4vw,4rem);line-height:1.08;margin:0 0 18px}.eyebrow{display:inline-block;padding:8px 12px;border-radius:999px;border:1px solid var(--border);background:rgba(56,189,248,.08);color:var(--primary);font-size:12px;letter-spacing:.1em;text-transform:uppercase}.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.btn{display:inline-block;padding:12px 18px;border-radius:10px;font-weight:700}.btn.primary{background:var(--primary);color:#03151d}.btn.ghost{border:1px solid var(--border);color:var(--text)}.hero-card,.tool-card,.post-card,.category-card,.section-box,.faq-item,.ad-slot,.tool-side,.article-wrap,.tool-page,.share-box,.toc-box{background:rgba(17,28,45,.72);border:1px solid var(--border);border-radius:18px;box-shadow:0 16px 34px rgba(2,6,23,.18)}.hero-card{padding:22px;display:grid;gap:14px}.mini-tool{display:flex;align-items:center;gap:14px;padding:12px;border:1px solid var(--border);border-radius:12px;background:rgba(148,163,184,.04)}.mini-tool span{font-size:2rem}.section-block{padding:32px 0}.section-head h2{margin:0 0 18px;font-size:2rem}.category-grid,.post-grid,.tool-grid,.faq-grid{display:grid;gap:18px}.category-grid{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}.post-grid,.tool-grid{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}.category-card,.post-card,.tool-card{padding:18px;display:block}.category-card{font-weight:700;color:var(--text)}.tag{display:inline-block;padding:6px 10px;border-radius:999px;background:rgba(245,158,11,.12);color:var(--accent);font-size:11px}.tool-card .icon{font-size:2rem}.genre-cloud,.tag-cloud{display:flex;gap:10px;flex-wrap:wrap}.genre-cloud span,.tag-item{display:inline-block;padding:10px 12px;border:1px solid var(--border);border-radius:999px;background:rgba(148,163,184,.04);font-size:12px;color:var(--text)}.page-header{padding:50px 0 20px}.page-header h1{font-size:clamp(2.3rem,3vw,3rem);margin:0 0 10px}.article-wrap,.tool-page{padding:30px 20px}.article-wrap h1,.tool-page h1{font-size:clamp(2.3rem,3vw,3.1rem)}.breadcrumb{color:var(--muted);margin-bottom:14px}.meta-bar{display:flex;gap:20px;flex-wrap:wrap;color:var(--muted);margin:16px 0}.hero-image-box{margin:18px 0 22px;border-radius:18px;overflow:hidden;border:1px solid var(--border)}.toc-box{padding:18px 20px;margin-bottom:20px}.article-body p,.tool-main p,.tool-main li,.section-box p{color:var(--muted);line-height:1.8}.article-body h2,.tool-main h2{margin-top:30px}.faq-grid{grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:20px}.faq-item{padding:16px}.social-share{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}.share-box{padding:18px 20px;margin-top:24px}.tool-hero{display:grid;grid-template-columns:120px minmax(0,1fr);gap:18px;align-items:center}.tool-icon{height:110px;display:grid;place-items:center;border:1px solid var(--border);border-radius:18px;background:rgba(56,189,248,.08);font-size:4rem}.tool-layout{display:grid;grid-template-columns:1.45fr .55fr;gap:18px;margin-top:22px}.tool-side{padding:18px}.ad-slot{min-height:160px;display:grid;place-items:center;color:var(--muted);margin-top:18px}.site-footer{padding:40px 0 20px;border-top:1px solid var(--border);margin-top:16px;background:rgba(8,15,24,.9)}.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}.footer-grid ul{list-style:none;padding:0;margin:0;line-height:2}.copyright{padding-top:18px;border-top:1px solid var(--border);margin-top:20px;text-align:center;color:var(--muted)}@media (max-width:900px){.hero-grid,.tool-layout,.tool-hero{grid-template-columns:1fr}.topbar{display:block}.main-nav ul{justify-content:center}.lang-switcher{justify-content:center}}@media (max-width:560px){.cta-row{display:block}.btn{width:100%;text-align:center}.topbar{padding:10px 0}}""")
    write_file(assets / 'js' / 'app.js', "document.addEventListener('DOMContentLoaded', () => document.querySelectorAll('.nav-item a').forEach(a => a.addEventListener('click', () => document.querySelectorAll('.nav-item a').forEach(el => el.classList.remove('active')) && a.classList.add('active'))));")
    write_file(assets / 'images' / 'logo.svg', make_svg_logo())
    for placeholder in ['og-default.jpg', 'logo.png']:
        (assets / 'images' / placeholder).write_bytes(b'')
    for placeholder in ['icon-192.png', 'icon-512.png']:
        (assets / 'icons' / placeholder).write_bytes(b'')

    print("FASTSONG static site generated successfully in dist/")


if __name__ == "__main__":
    generate_site()
