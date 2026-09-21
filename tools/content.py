# -*- coding: utf-8 -*-
"""Treść podstron demo Mazovet.

ZASADA: wchodzi tu wyłącznie to, co potwierdzone: wizytówka Google (adres,
godziny, telefon, ocena), Facebook gabinetu (zdjęcia obiektu, opis lokalizacji,
udział w kongresie WBC 2026) i logo klienta (obsługiwane gatunki).
Wszystko, czego nie dało się potwierdzić, zostaje jako blok .todo do uzupełnienia
po rozmowie z klientem.
"""

RATING = '4,7'
RATING_COUNT = '117'
GMB = 'https://www.google.com/maps/place/MAZOVET/@52.6791114,19.8009251,17z/data=!4m6!3m5!1s0x471c698608b34605:0xea645ec139fa9902!8m2!3d52.6791114!4d19.8009251!16s%2Fg%2F11pqcb60nr'
FB = 'https://www.facebook.com/profile.php?id=100063583105562'
MAPA_EMBED = 'https://www.google.com/maps?q=Sierpecka%2048,%2009-230%20Bielsk&hl=pl&z=16&output=embed'


def strip(I, TEL, TEL_HREF, ADRES):
    return '''
<div class="strip">
  <div class="wrap">
    <div class="it"><span class="ic">%s</span><span><b>%s</b><span>Bielsk, powiat płocki, obok szkoły podstawowej</span></span></div>
    <div class="it"><span class="ic">%s</span><span><b>pn–pt 8:00–18:00 · sob 9:00–13:00</b><span data-open-status>Niedziela nieczynne</span></span></div>
    <div class="it"><span class="ic">%s</span><span><b><a href="tel:%s" style="text-decoration:none">%s</a></b><span>Rejestracja telefoniczna</span></span></div>
  </div>
</div>
''' % (I['pin'], ADRES, I['clock'], I['phone'], TEL_HREF, TEL)


def cta(I, TEL, TEL_HREF):
    return '''
<section class="cta">
  <div class="wrap">
    <h2>Umów wizytę telefonicznie</h2>
    <p>Rejestracja czynna w godzinach pracy gabinetu. W sprawach nagłych prosimy o telefon przed przyjazdem, przygotujemy gabinet na przyjęcie pacjenta.</p>
    <p style="margin-top:26px"><a class="btn btn-ghost" href="tel:%s">%s %s</a></p>
  </div>
</section>
''' % (TEL_HREF, I['phone'], TEL)


def rating_box(I):
    return '''
<div class="rating">
  <div>
    <div class="score">%s</div>
    <div class="stars">★★★★★</div>
  </div>
  <div style="flex:1;min-width:260px">
    <h3 class="mt0">Ocena w wizytówce Google</h3>
    <p class="muted" style="margin-bottom:.6em">Średnia z %s opinii wystawionych przez właścicieli zwierząt (stan na wrzesień 2026).</p>
    <a class="btn btn-line btn-sm" href="%s" rel="noopener">Zobacz opinie w Google</a>
  </div>
</div>
''' % (RATING, RATING_COUNT, GMB)


def build_all(build, I, TEL, TEL_HREF, MAIL, ADRES):
    tel_btn = '<a class="btn btn-primary" href="tel:%s">%s Zadzwoń %s</a>' % (TEL_HREF, I['phone'], TEL)

    # ---------------------------------------------------------------- START
    index = '''
<section class="hero">
  <div class="hero-img">
    <img src="assets/img/klinika.webp" alt="Budynek gabinetu weterynaryjnego Mazovet przy ulicy Sierpeckiej 48 w Bielsku" width="1440" height="810" fetchpriority="high">
  </div>
  <div class="wrap hero-in">
    <span class="hero-badge">%s <b>%s / 5</b> z %s opinii w Google</span>
    <h1>Gabinet weterynaryjny<br>Mazovet w Bielsku</h1>
    <p>Opieka nad psami i kotami oraz nad zwierzętami gospodarskimi i końmi. Przyjmujemy przy ulicy Sierpeckiej 48, obok szkoły podstawowej.</p>
    <div class="hero-actions">%s<a class="btn btn-ghost" href="kontakt.html">Godziny i dojazd</a></div>
  </div>
</section>
''' % (I['star'], RATING, RATING_COUNT, tel_btn)

    index += strip(I, TEL, TEL_HREF, ADRES)

    index += '''
<section>
  <div class="wrap">
    <div class="sec-head center reveal">
      <span class="kicker">Zakres opieki</span>
      <h2>Zwierzęta domowe i gospodarskie pod jednym adresem</h2>
      <p class="lead" style="margin:0 auto">Gabinet prowadzi lek. wet. Paweł Kosno. Przyjmujemy pacjentów z Bielska i okolicznych gmin, od psów i kotów po bydło i konie.</p>
    </div>
    <div class="grid g3">
      <a class="card reveal" href="psy-i-koty.html" style="text-decoration:none">
        <span class="ic">%s</span>
        <h3>Psy i koty</h3>
        <p>Wizyty, profilaktyka i zabiegi dla zwierząt domowych, w gabinecie przy Sierpeckiej 48.</p>
      </a>
      <a class="card reveal" href="zwierzeta-gospodarskie.html" style="text-decoration:none">
        <span class="ic">%s</span>
        <h3>Bydło</h3>
        <p>Opieka nad stadami bydła. Lekarz szkoli się w buiatrii, czyli medycynie bydła.</p>
      </a>
      <a class="card reveal" href="zwierzeta-gospodarskie.html" style="text-decoration:none">
        <span class="ic">%s</span>
        <h3>Konie</h3>
        <p>Koń jest jednym z gatunków, którymi zajmuje się gabinet, tak jak pokazuje to znak Mazovet.</p>
      </a>
      <div class="card reveal">
        <span class="ic">%s</span>
        <h3>Szczepienia i profilaktyka</h3>
        <p>Szczepienia, odrobaczanie i badania kontrolne. Terminy ustalamy telefonicznie.</p>
      </div>
      <div class="card reveal">
        <span class="ic">%s</span>
        <h3>Zabiegi chirurgiczne</h3>
        <p>Gabinet wykonuje zabiegi w znieczuleniu, między innymi sterylizacje i kastracje.</p>
      </div>
      <div class="card reveal todo" style="display:flex;flex-direction:column;justify-content:center">
        <p><b>Miejsce na pełną listę usług.</b></p>
        <p>Diagnostyka, stomatologia, wizyty terenowe, cennik. Dopiszemy dokładnie to, co robicie, po krótkiej rozmowie.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="split">
      <div class="split-txt reveal">
        <span class="kicker">Gabinet</span>
        <h2>Nowy budynek przy Sierpeckiej 48</h2>
        <p>Gabinet mieści się w wolnostojącym budynku na skraju Bielska, obok szkoły podstawowej, dawnego gimnazjum. Przed wejściem jest utwardzony plac, a do drzwi prowadzi podjazd z poręczą, więc wjazd z transporterem lub większym psem nie wymaga pokonywania schodów.</p>
        <ul class="ticks">
          <li>Miejsce do zaparkowania przed budynkiem</li>
          <li>Szyld widoczny z drogi, podświetlony po zmroku</li>
          <li>Rejestracja telefoniczna w godzinach pracy</li>
        </ul>
        <a class="btn btn-line" href="gabinet.html">Zobacz gabinet</a>
      </div>
      <div class="split-imgs reveal">
        <img class="wide" src="assets/img/klinika-wieczorem.webp" alt="Podświetlony szyld gabinetu Mazovet po zmroku" width="640" height="480" loading="lazy">
        <img src="assets/img/recepcja.webp" alt="Wnętrze gabinetu Mazovet, recepcja" width="622" height="280" loading="lazy">
        <img src="assets/img/klinika-zima.webp" alt="Budynek gabinetu Mazovet zimą" width="622" height="280" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split rev">
      <div class="split-txt reveal">
        <span class="kicker">Lekarz</span>
        <h2>lek. wet. Paweł Kosno</h2>
        <p>Założyciel i właściciel gabinetu. We wrześniu 2026 roku brał udział w 33. Światowym Kongresie Buiatrycznym WBC w Stambule, największym spotkaniu lekarzy zajmujących się zdrowiem bydła.</p>
        <div class="todo">
          <p><b>Miejsce na notkę o lekarzu i zespole.</b></p>
          <p>Uczelnia i rok dyplomu, specjalizacje, kursy, imiona osób z zespołu. Uzupełnimy je po rozmowie.</p>
        </div>
      </div>
      <div class="split-imgs reveal">
        <img class="wide" src="assets/img/kongres-wbc.webp" alt="Centrum kongresowe WBC 2026 w Stambule" width="1280" height="960" loading="lazy">
        <img src="assets/img/kongres-grupa.webp" alt="Uczestnicy kongresu buiatrycznego WBC 2026" width="1280" height="960" loading="lazy">
        <img src="assets/img/gabinet-wnetrze.webp" alt="Wnętrze gabinetu Mazovet" width="640" height="480" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="sec-head center reveal">
      <span class="kicker">Opinie</span>
      <h2>Co mówią właściciele zwierząt</h2>
    </div>
    <div class="reveal">%s</div>
    <div class="grid g3" style="margin-top:22px">
      <div class="card todo reveal"><p><b>Miejsce na opinię</b></p><p>Po Waszej akceptacji wstawimy tu trzy opinie z wizytówki Google, z imieniem autora i datą.</p></div>
      <div class="card todo reveal"><p><b>Miejsce na opinię</b></p><p>Opinie można też pobierać automatycznie, wtedy najnowsze pojawiają się na stronie same.</p></div>
      <div class="card todo reveal"><p><b>Miejsce na opinię</b></p><p>Publikujemy wyłącznie prawdziwe opinie klientów, nic nie dopisujemy.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center reveal">
      <span class="kicker">Pacjenci</span>
      <h2>Kogo przyjmujemy</h2>
      <p class="lead" style="margin:0 auto">Psy, koty, bydło i konie, czyli cztery gatunki, które widać w znaku gabinetu.</p>
    </div>
    <div class="gal reveal">
      <figure><img src="assets/img/pies-gabinet.webp" alt="Pies na stole zabiegowym w gabinecie weterynaryjnym" width="1200" height="1797" loading="lazy"></figure>
      <figure><img src="assets/img/kot-badanie.webp" alt="Kot podczas badania u weterynarza" width="1200" height="800" loading="lazy"></figure>
      <figure><img src="assets/img/krowy.webp" alt="Krowy na pastwisku" width="1200" height="1800" loading="lazy"></figure>
    </div>
    <p class="center muted" style="margin-top:20px;font-size:.9rem">Zdjęcia poglądowe. Docelowo wstawimy tu zdjęcia Waszych pacjentów i wnętrza gabinetu.</p>
    <p class="center" style="margin-top:14px"><a class="btn btn-line" href="galeria.html">Zobacz galerię</a></p>
  </div>
</section>
''' % (I['paw'], I['cow'], I['horse'], I['syringe'], I['scalpel'], rating_box(I))

    index += cta(I, TEL, TEL_HREF)

    build('index.html',
          'Gabinet Weterynaryjny Mazovet | weterynarz Bielsk, Sierpecka 48',
          'Gabinet weterynaryjny Mazovet w Bielsku (ul. Sierpecka 48): psy, koty, bydło i konie. Rejestracja telefoniczna: 794 206 306. Pn–pt 8:00–18:00, sob 9:00–13:00.',
          index, over=True)

    # ------------------------------------------------------------ PSY I KOTY
    psy = '''
<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Psy i koty</p>
    <h1>Opieka nad psami i kotami</h1>
    <p>Wizyty w gabinecie przy ulicy Sierpeckiej 48 w Bielsku. Terminy ustalamy telefonicznie pod numerem %s.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="split">
      <div class="split-txt">
        <h2 class="mt0">Wizyta w gabinecie</h2>
        <p>Na wizytę umawiamy się telefonicznie, dzięki temu lekarz ma przygotowany gabinet i czas na spokojne badanie. Prosimy o zabranie książeczki zdrowia zwierzęcia, jeśli ją Państwo mają.</p>
        <ul class="ticks">
          <li>Badanie kliniczne i konsultacja</li>
          <li>Szczepienia ochronne i odrobaczanie</li>
          <li>Zabiegi chirurgiczne w znieczuleniu, m.in. sterylizacja i kastracja</li>
          <li>Opieka po zabiegu i kontrola gojenia</li>
        </ul>
      </div>
      <div class="split-img"><img src="assets/img/piesek-gabinet.webp" alt="Pies u weterynarza" width="1200" height="1800" loading="lazy"></div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="sec-head center">
      <h2>Co jeszcze wpiszemy na tę stronę</h2>
      <p class="lead" style="margin:0 auto">Poniższe punkty zostawiamy puste celowo. Wypełnimy je dokładnie tym, co robicie, żeby na stronie nie było ani jednej obietnicy na wyrost.</p>
    </div>
    <div class="grid g3">
      <div class="card todo"><p><b>Diagnostyka</b></p><p>USG, RTG, badania krwi na miejscu czy w laboratorium zewnętrznym (do potwierdzenia).</p></div>
      <div class="card todo"><p><b>Stomatologia i zabiegi dodatkowe</b></p><p>Skaling, usuwanie zębów, chirurgia tkanek miękkich (do potwierdzenia).</p></div>
      <div class="card todo"><p><b>Cennik i sposób płatności</b></p><p>Widełki cen najczęstszych usług oraz informacja, czy przyjmujecie karty.</p></div>
      <div class="card todo"><p><b>Paszporty i mikroczipowanie</b></p><p>Czy gabinet wystawia paszporty i czipuje zwierzęta.</p></div>
      <div class="card todo"><p><b>Wizyty domowe</b></p><p>Czy i na jakim obszarze lekarz dojeżdża do zwierząt domowych.</p></div>
      <div class="card todo"><p><b>Nagłe przypadki</b></p><p>Zasady przyjęć poza godzinami pracy (do ustalenia).</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid g3">
      <figure style="margin:0"><img src="assets/img/kotek.webp" alt="Kotek na badaniu" width="1200" height="800" loading="lazy" style="border-radius:14px"></figure>
      <figure style="margin:0"><img src="assets/img/szczeniak.webp" alt="Szczeniak na rękach" width="1200" height="2137" loading="lazy" style="border-radius:14px;max-height:320px;object-fit:cover;width:100%%"></figure>
      <figure style="margin:0"><img src="assets/img/pies-kot.webp" alt="Pies i kot" width="1200" height="900" loading="lazy" style="border-radius:14px"></figure>
    </div>
    <p class="center muted" style="margin-top:18px;font-size:.9rem">Zdjęcia poglądowe, do podmiany na zdjęcia pacjentów gabinetu.</p>
  </div>
</section>
''' % TEL

    psy += cta(I, TEL, TEL_HREF)
    build('psy-i-koty.html',
          'Weterynarz dla psa i kota w Bielsku | Gabinet Mazovet',
          'Opieka nad psami i kotami w gabinecie Mazovet w Bielsku: badanie, szczepienia, zabiegi chirurgiczne. Rejestracja: 794 206 306.',
          psy, og='assets/img/pies-gabinet.webp')

    # -------------------------------------------------- ZWIERZĘTA GOSPODARSKIE
    gosp = '''
<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Zwierzęta gospodarskie</p>
    <h1>Bydło i konie</h1>
    <p>Gabinet Mazovet zajmuje się nie tylko zwierzętami domowymi. Bydło i koń są w znaku gabinetu od początku jego działalności.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="split">
      <div class="split-txt">
        <h2 class="mt0">Bydło</h2>
        <p>Lek. wet. Paweł Kosno rozwija się w buiatrii, czyli medycynie bydła. We wrześniu 2026 roku uczestniczył w 33. Światowym Kongresie Buiatrycznym WBC w Stambule, gdzie omawiano zdrowie stad i profilaktykę w oborach.</p>
        <div class="todo">
          <p><b>Miejsce na zakres opieki nad stadem.</b></p>
          <p>Wizyty w gospodarstwach, badania rozrodu, profilaktyka stada, obsługa porodów, dokumentacja. Dopiszemy to, co faktycznie prowadzicie, razem z obszarem dojazdu.</p>
        </div>
      </div>
      <div class="split-img"><img src="assets/img/krowa.webp" alt="Krowa na pastwisku" width="1200" height="800" loading="lazy"></div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="split rev">
      <div class="split-txt">
        <h2 class="mt0">Konie</h2>
        <p>Koń jest jednym z czterech gatunków pokazanych w znaku Mazovet, obok krowy, psa i kota.</p>
        <div class="todo">
          <p><b>Miejsce na zakres opieki nad końmi.</b></p>
          <p>Badania, szczepienia, stomatologia koni, wizyty w stajniach (do uzupełnienia po rozmowie).</p>
        </div>
      </div>
      <div class="split-img"><img src="assets/img/kon.webp" alt="Koń" width="1200" height="801" loading="lazy"></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split">
      <div class="split-txt">
        <h2 class="mt0">Kongres buiatryczny WBC 2026</h2>
        <p>Stambuł, 6–10 września 2026 roku. Kongres organizowany przez World Association for Buiatrics gromadzi lekarzy weterynarii zajmujących się bydłem z całego świata.</p>
      </div>
      <div class="split-imgs">
        <img class="wide" src="assets/img/kongres-wbc.webp" alt="Centrum kongresowe WBC 2026 w Stambule" width="1280" height="960" loading="lazy">
        <img src="assets/img/kongres-grupa.webp" alt="Uczestnicy kongresu WBC 2026" width="1280" height="960" loading="lazy">
        <img src="assets/img/krowy.webp" alt="Krowy na pastwisku" width="1200" height="1800" loading="lazy">
      </div>
    </div>
  </div>
</section>
'''
    gosp += cta(I, TEL, TEL_HREF)
    build('zwierzeta-gospodarskie.html',
          'Weterynarz dla bydła i koni w Bielsku | Gabinet Mazovet',
          'Opieka nad bydłem i końmi w gabinecie weterynaryjnym Mazovet, ul. Sierpecka 48 w Bielsku. Kontakt: 794 206 306.',
          gosp, og='assets/img/krowa.webp')

    # ---------------------------------------------------------------- GABINET
    gab = '''
<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Gabinet</p>
    <h1>O gabinecie</h1>
    <p>Mazovet to gabinet weterynaryjny lek. wet. Pawła Kosno w Bielsku w powiecie płockim.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="split">
      <div class="split-txt">
        <h2 class="mt0">Gdzie nas znaleźć</h2>
        <p>Gabinet działa przy ulicy Sierpeckiej 48 w Bielsku, obok szkoły podstawowej, dawnego gimnazjum. Budynek stoi przy drodze, z własnym placem manewrowym i parkingiem, więc można podjechać samochodem pod samo wejście.</p>
        <ul class="ticks">
          <li>Wolnostojący budynek z widocznym szyldem, także po zmroku</li>
          <li>Podjazd z poręczą przy wejściu głównym</li>
          <li>Utwardzony plac przed wejściem</li>
        </ul>
        <a class="btn btn-line" href="kontakt.html">Dojazd i mapa</a>
      </div>
      <div class="split-img"><img src="assets/img/klinika.webp" alt="Budynek gabinetu Mazovet" width="1440" height="810" loading="lazy"></div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="split rev">
      <div class="split-txt">
        <h2 class="mt0">Zespół</h2>
        <p>Gabinet prowadzi lek. wet. Paweł Kosno. W opiniach w Google właściciele zwierząt dziękują imiennie także pozostałym osobom z zespołu.</p>
        <div class="todo">
          <p><b>Miejsce na prezentację zespołu.</b></p>
          <p>Imiona i nazwiska, funkcje, zdjęcia. Wstawimy je dokładnie w takiej formie, w jakiej sobie Państwo życzą. Bez zgody nikogo nie wymieniamy z imienia.</p>
        </div>
      </div>
      <div class="split-img"><img src="assets/img/gabinet-wnetrze.webp" alt="Wnętrze gabinetu Mazovet" width="640" height="480" loading="lazy"></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center">
      <h2>Wyposażenie i możliwości gabinetu</h2>
    </div>
    <div class="grid g2">
      <div class="card todo"><p><b>Sprzęt diagnostyczny</b></p><p>Co macie na miejscu: USG, RTG, analizator krwi, mikroskop. Ta lista robi największe wrażenie na stronie, więc warto ją wypełnić dokładnie.</p></div>
      <div class="card todo"><p><b>Sala zabiegowa i hospitalizacja</b></p><p>Czy zwierzę może zostać na obserwację, ile stanowisk, jak wygląda opieka po zabiegu.</p></div>
    </div>
  </div>
</section>
'''
    gab += cta(I, TEL, TEL_HREF)
    build('gabinet.html',
          'O gabinecie | Mazovet, weterynarz w Bielsku',
          'Gabinet weterynaryjny Mazovet przy ul. Sierpeckiej 48 w Bielsku: budynek, zespół i wyposażenie. Telefon: 794 206 306.',
          gab)

    # ---------------------------------------------------------------- GALERIA
    fotki = [
        ('klinika.webp', 'Budynek gabinetu Mazovet od frontu', 'gabinet'),
        ('klinika-wieczorem.webp', 'Podświetlony szyld gabinetu po zmroku', 'gabinet'),
        ('klinika-zima.webp', 'Gabinet zimą, ul. Sierpecka 48', 'gabinet'),
        ('recepcja.webp', 'Recepcja gabinetu', 'gabinet'),
        ('gabinet-wnetrze.webp', 'Wnętrze gabinetu', 'gabinet'),
        ('kongres-wbc.webp', 'Kongres buiatryczny WBC 2026 w Stambule', 'gabinet'),
        ('kongres-grupa.webp', 'Uczestnicy kongresu WBC 2026', 'gabinet'),
        ('pies-gabinet.webp', 'Pies na stole zabiegowym', 'pacjenci'),
        ('piesek-gabinet.webp', 'Pies u weterynarza', 'pacjenci'),
        ('kot-badanie.webp', 'Kot podczas badania', 'pacjenci'),
        ('kotek.webp', 'Kotek na badaniu', 'pacjenci'),
        ('szczeniak.webp', 'Szczeniak na rękach', 'pacjenci'),
        ('pies-kot.webp', 'Pies i kot', 'pacjenci'),
        ('krowy.webp', 'Krowy na pastwisku', 'gospodarskie'),
        ('krowa.webp', 'Krowa mleczna', 'gospodarskie'),
        ('kon.webp', 'Koń', 'gospodarskie'),
        ('kon-portret.webp', 'Portret konia', 'gospodarskie'),
    ]
    figs = ''.join(
        '<figure data-cat="%s"><img src="assets/img/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (cat, f, alt, alt)
        for f, alt, cat in fotki
    )
    gal = '''
<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Galeria</p>
    <h1>Galeria</h1>
    <p>Zdjęcia budynku i wnętrza pochodzą z profilu gabinetu na Facebooku. Zdjęcia zwierząt są poglądowe, zastąpimy je zdjęciami Waszych pacjentów.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="filters">
      <button data-filter="all" aria-pressed="true">Wszystko</button>
      <button data-filter="gabinet" aria-pressed="false">Gabinet</button>
      <button data-filter="pacjenci" aria-pressed="false">Psy i koty</button>
      <button data-filter="gospodarskie" aria-pressed="false">Zwierzęta gospodarskie</button>
    </div>
    <div class="gal">%s</div>
    <div class="todo" style="margin-top:34px">
      <p><b>Miejsce na Wasze zdjęcia.</b></p>
      <p>Najlepiej działają zdjęcia z gabinetu: sala zabiegowa, sprzęt, zespół przy pracy i zadowoleni pacjenci (za zgodą właścicieli). Wystarczy je przesłać, obróbką i opisami zajmiemy się my.</p>
    </div>
  </div>
</section>
''' % figs
    gal += cta(I, TEL, TEL_HREF)
    build('galeria.html',
          'Galeria | Gabinet Weterynaryjny Mazovet w Bielsku',
          'Zdjęcia gabinetu weterynaryjnego Mazovet przy ul. Sierpeckiej 48 w Bielsku oraz pacjentów, którymi się zajmujemy.',
          gal)

    # ---------------------------------------------------------------- KONTAKT
    kont = '''
<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Kontakt</p>
    <h1>Kontakt i godziny</h1>
    <p>Rejestracja telefoniczna w godzinach pracy gabinetu.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <ul class="info-list">
          <li><span class="ic">%s</span><span><b>Telefon</b><a href="tel:%s">%s</a></span></li>
          <li><span class="ic">%s</span><span><b>E-mail</b><a href="mailto:%s">%s</a></span></li>
          <li><span class="ic">%s</span><span><b>Adres</b><span>%s</span></span></li>
        </ul>

        <h3 style="margin-top:34px">Godziny przyjęć</h3>
        <table class="hours">
          <tr data-day="1"><td>Poniedziałek</td><td>8:00–18:00</td></tr>
          <tr data-day="2"><td>Wtorek</td><td>8:00–18:00</td></tr>
          <tr data-day="3"><td>Środa</td><td>8:00–18:00</td></tr>
          <tr data-day="4"><td>Czwartek</td><td>8:00–18:00</td></tr>
          <tr data-day="5"><td>Piątek</td><td>8:00–18:00</td></tr>
          <tr data-day="6"><td>Sobota</td><td>9:00–13:00</td></tr>
          <tr data-day="0"><td>Niedziela</td><td>nieczynne</td></tr>
        </table>
        <p class="muted" style="font-size:.9rem;margin-top:12px">Godziny za wizytówką Google (wrzesień 2026). Jeśli coś się zmieniło, poprawimy.</p>
      </div>
      <div class="map">
        <iframe src="%s" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa dojazdu do gabinetu Mazovet"></iframe>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--bg-2)">
  <div class="wrap-narrow">
    <div class="sec-head center" style="margin-bottom:26px">
      <h2>Napisz do nas</h2>
      <p class="lead" style="margin:0 auto">Formularz trafia na skrzynkę gabinetu. W sprawach nagłych prosimy o telefon, odpowiadamy szybciej.</p>
    </div>
    <form data-demo-form>
      <div class="row">
        <div><label for="imie">Imię i nazwisko</label><input id="imie" name="imie" required></div>
        <div><label for="tel">Telefon</label><input id="tel" name="tel" type="tel" required></div>
      </div>
      <label for="gatunek">Zwierzę</label>
      <select id="gatunek" name="gatunek">
        <option>Pies</option><option>Kot</option><option>Bydło</option><option>Koń</option><option>Inne</option>
      </select>
      <label for="tresc">Wiadomość</label>
      <textarea id="tresc" name="tresc" required></textarea>
      <button class="btn btn-primary" type="submit">Wyślij wiadomość</button>
      <p class="form-result form-note" hidden></p>
      <p class="form-note" style="margin-top:14px">To wersja demonstracyjna strony, formularz uruchamiamy przy wdrożeniu. Wiadomości będą wtedy trafiać na wskazany adres e-mail.</p>
    </form>
  </div>
</section>
''' % (I['phone'], TEL_HREF, TEL, I['mail'], MAIL, MAIL, I['pin'], ADRES, MAPA_EMBED)

    kont += cta(I, TEL, TEL_HREF)
    build('kontakt.html',
          'Kontakt | Gabinet Weterynaryjny Mazovet, Bielsk',
          'Gabinet Mazovet, ul. Sierpecka 48, 09-230 Bielsk. Telefon 794 206 306. Pn–pt 8:00–18:00, sob 9:00–13:00.',
          kont)
