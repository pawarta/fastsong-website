import os
import json

# Konfigurasi Dasar Website
SITE_NAME = "FASTSONG"
SITE_URL = "https://fastsong.eu.org"
DOMAIN = "fastsong.eu.org"
ADSENSE_CLIENT = "ca-pub-9308517202792186"

# Kategori Artikel Makro & Global beserta jumlah target file/sub-kategori
CATEGORIES_MACRO = {
    "instrumental-music": 710,
    "vocal-songs": 528,
    "short-cues-intros": 627,
    "loops": 1460,
    "sound-effects": 314,
    "alert": 166,
    "ambience-background": 501,
    "click-pop-bell": 247,
    "clock-timer-counter": 113,
    "comedy-funny": 155,
    "hit-explosion-impact": 463,
    "household": 557,
    "nature-animal": 459,
    "people-human": 832,
    "sci-fi-artificial": 481,
    "swoosh-rise": 323,
    "technology-tools": 464,
}

INSTRUMENTS = [
    "Accordion", "Acoustic Guitar", "Bagpipes", "Banjo", "Bell / Glockenspiel", 
    "Brass", "Cello", "Claps", "Clarinet", "Dulcimer / Zither", "Electric Guitar", 
    "Electric Piano / Organ", "Finger Snaps", "Flute", "Harmonica", "Harp", 
    "Harpsichord", "Marimba / Kalimba", "Oboe", "Oud", "Percussion", "Piano", 
    "Saxophone", "Sitar", "Steel Drums", "Strings", "Synthesizer", "Ukulele", 
    "Voice / Choir", "Whistle"
]

TOOLS_LIST = [
    "Playlist Generator", "Genre Finder", "Playlist Analyzer", "All Tools", "Blog", 
    "Music Instruments", "Practice Timer", "Pitch Pipe", "Circle of Fifths",
    "Online Code Editor", "QR Code Generator", "Color Code Generator", "Equalizer & Audio Generator",
    "Keyboard Multi Bahasa", "Arabic Calligraphy Tool", "QuranClip Studio Live", "Postal Code Finder",
    "Interactive Maps Search", "SEO Performance Analyzer", "Quran Play", "WHOIS Lookup",
    "Domain Age Checker", "Domain Expiry Checker", "DNS Checker", "Reverse IP Lookup",
    "Domain to IP", "Domain Adsense Eligibility", "Domain Price", "BIMI Checker & Generator",
    "Image to Text Converter", "Runic Translator", "Invisible Character", "Internet Speed Test",
    "WiFi QR Scanner", "Minecraft Color Codes"
]

# Template Universal untuk Header & Meta Tags
def get_header_html(title, description, keywords, canonical_url):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{description}"/>
    <meta name="keywords" content="{keywords}"/>
    <link rel="canonical" href="{canonical_url}"/>
    
    <!-- Google Verification & Adsense -->
    <meta content='Gw7Z7swUZPrZIYzmklJDBBAZ_T6WcayrdpFYVbQhnEg' name='google-site-verification'/>
    <meta content='xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk' name='google-site-verification'/>
    <meta name="google-site-verification" content="xMW77g3fbb-5Di9z1eZWT9pdaR91IsnYQBhJqbOpMdk" />
    <meta content='{ADSENSE_CLIENT}' name='google-adsense-account'/>
    <script async='async' crossorigin='anonymous' src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}'></script>
    <script async='async' custom-element='amp-ad' src='https://cdn.ampproject.org/v0/amp-ad-0.1.js'></script>

    <!-- Open Graph / Social Share -->
    <meta property="og:title" content="{title} - {SITE_NAME}"/>
    <meta property="og:description" content="{description}"/>
    <meta property="og:url" content="{canonical_url}"/>
    <meta property="og:type" content="website"/>
    <meta property="og:image" content="{SITE_URL}/assets/img/meta-image.jpg"/>

    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json"/>
    <meta name="theme-color" content="#0d6efd"/>

    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "{SITE_NAME}",
      "url": "{SITE_URL}"
    }}
    </script>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
"""

# Template Navigasi Bar & Header Utama
def get_navbar_html():
    return f"""
    <header class="site-header">
        <div class="logo-container">
            <a href="{SITE_URL}/"><img src="{SITE_URL}/assets/img/logo.png" alt="{SITE_NAME} Logo"> <span>{SITE_NAME}</span></a>
        </div>
        <nav class="main-nav">
            <ul>
                <li><a href="{SITE_URL}/">Home</a></li>
                <li class="dropdown">
                    <a href="#">Tools</a>
                    <div class="dropdown-content">
                        <a href="{SITE_URL}/tools/playlist-generator.html">Playlist Generator</a>
                        <a href="{SITE_URL}/tools/genre-finder.html">Genre Finder</a>
                        <a href="{SITE_URL}/tools/practice-timer.html">Practice Timer</a>
                        <a href="{SITE_URL}/tools/pitch-pipe.html">Pitch Pipe</a>
                    </div>
                </li>
                <li><a href="{SITE_URL}/finders/">Finders</a></li>
                <li><a href="{SITE_URL}/games/">Games</a></li>
                <li><a href="{SITE_URL}/resources/">Resources</a></li>
                <li><a href="{SITE_URL}/company/about.html">Company</a></li>
                <li><a href="{SITE_URL}/contact.html">Contact</a></li>
                <li><a href="{SITE_URL}/terms.html">Terms</a></li>
                <li><a href="{SITE_URL}/privacy.html">Privacy Policy</a></li>
            </ul>
        </nav>
        <div class="language-selector">
            🌐 
            <select onchange="location = this.value;">
                <option value="/en/">English</option>
                <option value="/ru/">Rusia</option>
                <option value="/eu/">Eropa</option>
                <option value="/jp/">Jp</option>
                <option value="/id/">Id</option>
                <option value="/ar/">Arab</option>
            </select>
        </div>
    </header>
    <div class="adsense-banner">
        <ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    """

# Template Footer Lengkap
def get_footer_html():
    return f"""
    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-col">
                <img src="{SITE_URL}/assets/img/logo.png" alt="{SITE_NAME}">
                <p>Your ultimate platform for royalty-free music, sound effects, audio tools, and comprehensive global resources.</p>
            </div>
            <div class="footer-col">
                <h3>Software & Tools</h3>
                <ul>
                    <li><a href="{SITE_URL}/tools/speech-to-text.html">Speech to text software</a></li>
                    <li><a href="{SITE_URL}/tools/audio-converter.html">Audio converter</a></li>
                    <li><a href="{SITE_URL}/tools/mp3-converter.html">MP3 converter</a></li>
                    <li><a href="{SITE_URL}/tools/mp3-cutter.html">MP3 Cutter</a></li>
                    <li><a href="{SITE_URL}/tools/video-converter.html">Video converter</a></li>
                    <li><a href="{SITE_URL}/tools/vocal-remover.html">Vocal remover</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>Legal & Sitemap</h3>
                <ul>
                    <li><a href="{SITE_URL}/">Home</a></li>
                    <li><a href="{SITE_URL}/company/about.html">About Us</a></li>
                    <li><a href="{SITE_URL}/sitemap.xml">Sitemap XML</a></li>
                    <li><a href="{SITE_URL}/contact.html">Contact Us</a></li>
                    <li><a href="{SITE_URL}/privacy.html">Privacy Policy</a></li>
                    <li><a href="{SITE_URL}/terms.html">Terms of Service</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© <a href="{SITE_URL}">FASTSONG</a> - All Rights Reserved - Powered by <a href="https://relmusic.github.io">Relmusic</a></p>
        </div>
    </footer>
    </body>
    </html>
    """

# Fungsi untuk membuat file direktori otomatis
def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {path}")

# Generator Utama
def generate_website():
    print("Mulai membuat struktur file dan folder website FASTSONG...")

    # 1. File Verifikasi Google, Ads.txt, App-Ads.txt, Manifest, Sitemap
    create_file("google510371859970acbf.html", "google-site-verification: google510371859970acbf.html")
    create_file("ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0")
    create_file("app-ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0")
    
    manifest_data = {
        "name": "FASTSONG Music Platform",
        "short_name": "FASTSONG",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#0d6efd"
    }
    create_file("manifest.json", json.dumps(manifest_data, indent=2))

    # 2. Halaman Utama (Index.html)
    index_content = get_header_html("Royalty Free Music & Audio Generator", "Download free royalty free music, sound effects, and use professional audio tools.", "music, free download, sound effects, fastsong", SITE_URL) + \
                    get_navbar_html() + \
                    """
                    <main class="container">
                        <h1>Welcome to FASTSONG - Free Music & Audio Tools</h1>
                        <p>Explore thousands of instrumental tracks, vocal songs, loops, and professional tools for creators.</p>
                        <section class="quick-tools">
                            <h2>Featured Tools & Practice Gear</h2>
                            <div class="tool-card">
                                <h3>⏱️ Practice Timer</h3>
                                <p>Pomodoro-style timer for focused music practice sessions.</p>
                                <a href="/tools/practice-timer.html">USE NOW →</a>
                            </div>
                            <div class="tool-card">
                                <h3>🎼 Pitch Pipe</h3>
                                <p>Reference tones for all 12 chromatic notes. Perfect for singers.</p>
                                <a href="/tools/pitch-pipe.html">USE NOW →</a>
                            </div>
                            <div class="tool-card">
                                <h3>⭕ Circle of Fifths</h3>
                                <p>Interactive diagram showing key relationships and music theory.</p>
                                <a href="/tools/circle-of-fifths.html">USE NOW →</a>
                            </div>
                        </section>
                    </main>
                    """ + get_footer_html()
    create_file("index.html", index_content)

    # 3. Kategori Artikel Makro & Global (Simulasi Pembuatan Artikel)
    for category, count in CATEGORIES_MACRO.items():
        # Untuk demonstrasi skrip otomatis, kita buat sampel artikel representatif per kategori
        for i in range(1, min(count + 1, 4)): # Dibatasi sampel agar eksekusi cepat, bisa disesuaikan
            filename = f"category/{category}/article-{i}.html"
            title = f"{category.replace('-', ' ').title()} - Guide & Free Download #{i}"
            desc = f"Comprehensive 3000-6000 words human-written article regarding {category} with FAQ, table of contents, and internal/external links."
            
            article_content = get_header_html(title, desc, f"{category}, music, royalty free", f"{SITE_URL}/category/{category}/article-{i}.html") + \
                              get_navbar_html() + \
                              f"""
                              <main class="container article-page">
                                  <h1>{title}</h1>
                                  <div class="toc">Table of Contents</div>
                                  <p>Human written detailed article content (3000-6000 words length context)...</p>
                                  <h2>FAQ</h2>
                                  <ul><li>Q1? A1.</li><li>Q2? A2.</li></ul>
                                  <h3>Conclusion</h3>
                                  <p>Summary and final thoughts on {title}.</p>
                              </main>
                              """ + get_footer_html()
            create_file(filename, article_content)

    # 4. Halaman Tools
    for tool in TOOLS_LIST:
        slug = tool.lower().replace(" ", "-").replace("/", "-")
        tool_filename = f"tools/{slug}.html"
        tool_content = get_header_html(f"{tool} - Online Tool", f"Use free online {tool} instantly on FASTSONG.", tool, f"{SITE_URL}/tools/{slug}.html") + \
                       get_navbar_html() + \
                       f"""
                       <main class="container tool-page">
                           <h1>{tool}</h1>
                           <div class="tool-interface">
                               <p>Interactive tool interface for <strong>{tool}</strong> goes here.</p>
                           </div>
                           <div class="guide">
                               <h3>How to Use {tool}</h3>
                               <p>Step-by-step instructions and guidelines.</p>
                           </div>
                       </main>
                       """ + get_footer_html()
        create_file(tool_filename, tool_content)

    # 5. Halaman Statis & Legal (Contact, Terms, Privacy, About)
    static_pages = {
        "contact.html": ("Contact Us", "Get in touch with FASTSONG team."),
        "terms.html": ("Terms of Service", "Terms and conditions of using FASTSONG."),
        "privacy.html": ("Privacy Policy", "Privacy policy regarding user data."),
        "company/about.html": ("About Us", "Learn more about FASTSONG mission and vision.")
    }
    
    for page_path, (p_title, p_desc) in static_pages.items():
        content = get_header_html(p_title, p_desc, p_title.lower(), f"{SITE_URL}/{page_path}") + \
                  get_navbar_html() + \
                  f"""
                  <main class="container">
                      <h1>{p_title}</h1>
                      <p>Detailed information regarding {p_title.lower()} for FASTSONG platform users.</p>
                  </main>
                  """ + get_footer_html()
        create_file(page_path, content)

    print("Generasi file dan folder website FASTSONG selesai!")

if __name__ == "__main__":
    generate_website()
