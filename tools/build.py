# -*- coding: utf-8 -*-
"""Generator statycznych podstron demo Mazovet.
Uruchamiaj z katalogu repo:  python3 tools/build.py && bash bump.sh
Treść stron trzymana jest w tools/content.py.
"""
import os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'tools'))

SITE = 'https://impulseo-pl.github.io/mazovet-gabinet-weterynaryjny'
TEL = '794 206 306'
TEL_HREF = '+48794206306'
MAIL = 'gw.mazovet@wp.pl'
ADRES = 'ul. Sierpecka 48, 09-230 Bielsk'

NAV = [
    ('index.html', 'Start'),
    ('psy-i-koty.html', 'Psy i koty'),
    ('zwierzeta-gospodarskie.html', 'Zwierzęta gospodarskie'),
    ('gabinet.html', 'Gabinet'),
    ('galeria.html', 'Galeria'),
    ('kontakt.html', 'Kontakt'),
]

ICON = {
    'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    'paw': '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="6.5" cy="9.5" r="2.2"/><circle cx="10.5" cy="6" r="2.2"/><circle cx="15" cy="6.6" r="2.2"/><circle cx="18.4" cy="10.4" r="2.1"/><path d="M12.3 12.4c2.5 0 4.6 1.9 5.2 4 .5 1.8-.8 3.3-2.6 3.3-1 0-1.8-.4-2.6-.4s-1.6.4-2.6.4c-1.8 0-3.1-1.5-2.6-3.3.6-2.1 2.7-4 5.2-4z"/></svg>',
    'cow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7c-1.2-1.6-1.6-3-1.4-3.4.3-.6 2.4-.2 3.9 1.1"/><path d="M20 7c1.2-1.6 1.6-3 1.4-3.4-.3-.6-2.4-.2-3.9 1.1"/><path d="M6 6.5h12c.8 0 1.5.7 1.5 1.5v4.5a7.5 7.5 0 0 1-15 0V8c0-.8.7-1.5 1.5-1.5z"/><circle cx="9.3" cy="10.5" r=".9" fill="currentColor" stroke="none"/><circle cx="14.7" cy="10.5" r=".9" fill="currentColor" stroke="none"/><path d="M9.5 15.5h5"/></svg>',
    'horse': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M8.2 20.4c-2.3-1.6-3.9-4.2-3.9-7.3C4.3 8.6 7.7 5 12 5s7.7 3.6 7.7 8.1c0 3.1-1.6 5.7-3.9 7.3"/><circle cx="7.4" cy="20.9" r="1.25" fill="currentColor" stroke="none"/><circle cx="16.6" cy="20.9" r="1.25" fill="currentColor" stroke="none"/></svg>',
    'syringe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 2 4 4"/><path d="m17 7 3-3"/><path d="M19 9 9.7 18.3a2 2 0 0 1-1.1.6l-3.4.6.6-3.4a2 2 0 0 1 .6-1.1L15 5.7z"/><path d="m9 11 3 3"/><path d="m12 8 3 3"/><path d="M5 19 2 22"/></svg>',
    'scalpel': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 3 9 14l-3.5.5L6 11 17 0"/><path d="M9 14 4 19a2.8 2.8 0 0 0 4 4l5-5"/></svg>',
    'heart': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 5.6a5.5 5.5 0 0 0-7.8 0L12 6.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 22l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
    'star': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.1 8.6 22 9.6 17 14.6 18.2 21.5 12 18.2 5.8 21.5 7 14.6 2 9.6 8.9 8.6 12 2"/></svg>',
    'fb': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7h-2.5V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg>',
}


def head(title, desc, page, og_img='assets/img/klinika.webp'):
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{page}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta property="og:locale" content="pl_PL">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="icon" href="assets/img/favicon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<div class="demo-bar">
  <b>Demo Impulseo</b> — propozycja strony dla gabinetu Mazovet. Dane i zdjęcia obiektu z wizytówki Google i Facebooka, zdjęcia zwierząt poglądowe.
</div>
'''


def header(page, over=False):
    parts = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ''
        parts.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    links = ''.join(parts)
    return f'''
<header class="site-head{' over' if over else ''}">
  <div class="topbar">
    <div class="wrap">
      <span class="ti">{ICON['pin']} {ADRES}</span>
      <span class="ti hide-m">{ICON['clock']} pn–pt 8:00–18:00, sob 9:00–13:00</span>
      <a class="ti" href="tel:{TEL_HREF}">{ICON['phone']} {TEL}</a>
    </div>
  </div>
  <div class="head-bg">
  <div class="head-main">
    <a class="brand" href="index.html">
      <img src="assets/img/logo.png" alt="Mazovet — Gabinet Weterynaryjny" width="461" height="307">
    </a>
    <a class="btn btn-primary btn-sm head-cta" href="tel:{TEL_HREF}">{ICON['phone']} {TEL}</a>
    <button class="burger" aria-expanded="false" aria-controls="mainnav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <nav class="mainnav" id="mainnav" aria-label="Główna">{links}</nav>
  </div>
</header>
'''


def footer():
    links = ''.join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f'''
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="flogo" src="assets/img/logo.png" alt="Mazovet — Gabinet Weterynaryjny" width="461" height="307">
        <p class="mt0">Gabinet weterynaryjny lek. wet. Pawła Kosno.<br>Psy, koty, konie i zwierzęta gospodarskie.</p>
        <p><a href="https://www.facebook.com/profile.php?id=100063583105562" rel="noopener">{ICON['fb']} Facebook</a></p>
      </div>
      <div>
        <h4>Kontakt</h4>
        <p>{ADRES}<br>
        <a href="tel:{TEL_HREF}">{TEL}</a><br>
        <a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div>
        <h4>Strona</h4>
        <ul class="foot-links">{links}</ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Gabinet Weterynaryjny Mazovet</span>
      <span>Demo przygotowane przez Impulseo</span>
    </div>
  </div>
</footer>

<script src="assets/main.js"></script>
</body>
</html>
'''


def ldjson(page):
    return '''
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"VeterinaryCare","name":"Mazovet — Gabinet Weterynaryjny lek. wet. Paweł Kosno",
"telephone":"+48 794 206 306","email":"gw.mazovet@wp.pl",
"address":{"@type":"PostalAddress","streetAddress":"ul. Sierpecka 48","postalCode":"09-230","addressLocality":"Bielsk","addressRegion":"mazowieckie","addressCountry":"PL"},
"geo":{"@type":"GeoCoordinates","latitude":52.6791114,"longitude":19.8009251},
"areaServed":["Bielsk","Gozdowo","Drobin","Sierpc","Płock","powiat płocki"],
"openingHoursSpecification":[
{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"13:00"}],
"sameAs":["https://www.facebook.com/profile.php?id=100063583105562"]}
</script>
'''


def build(page, title, desc, body, over=False, og='assets/img/klinika.webp'):
    html = head(title, desc, page, og) + header(page, over) + body + ldjson(page) + footer()
    with open(os.path.join(BASE, page), 'w', encoding='utf-8') as f:
        f.write(html)
    print('  ', page)


if __name__ == '__main__':
    import content
    print('Generuję podstrony:')
    content.build_all(build, ICON, TEL, TEL_HREF, MAIL, ADRES)
