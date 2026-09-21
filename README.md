# Mazovet, demo strony (Impulseo)

Propozycja strony dla **Gabinetu Weterynaryjnego Mazovet** lek. wet. Pawła Kosno, ul. Sierpecka 48, 09-230 Bielsk (powiat płocki). Klient nie ma własnej strony, w wizytówce Google pole „witryna” jest puste.

Podgląd: https://impulseo-pl.github.io/mazovet-gabinet-weterynaryjny/

Strona jest **wyłączona z indeksowania** (`<meta name="robots" content="noindex, nofollow">` na każdej podstronie).

## Podstrony

| Plik | Zawartość |
|---|---|
| `index.html` | hero ze zdjęciem gabinetu, zakres opieki, budynek, lekarz, ocena Google, pacjenci |
| `psy-i-koty.html` | opieka nad zwierzętami domowymi plus lista pytań do klienta |
| `zwierzeta-gospodarskie.html` | bydło i konie, kongres buiatryczny WBC 2026 |
| `gabinet.html` | budynek, zespół, wyposażenie (do uzupełnienia) |
| `galeria.html` | galeria z filtrami: gabinet / psy i koty / zwierzęta gospodarskie |
| `kontakt.html` | dane, godziny, mapa, formularz (w demie nie wysyła) |

## Skąd pochodzą treści

Do demo trafiło tylko to, co dało się potwierdzić:

- **wizytówka Google**: adres, telefon 794 206 306, godziny (pn–pt 8:00–18:00, sob 9:00–13:00), ocena 4,7 ze 117 opinii (stan 21.09.2026);
- **Facebook gabinetu**: zdjęcia budynku i wnętrza, opis lokalizacji („obok Szkoły Podstawowej, dawnego Gimnazjum”), udział lekarza w 33. Światowym Kongresie Buiatrycznym WBC w Stambule (6–10.09.2026);
- **logo klienta**: obsługiwane gatunki: koń, krowa, pies, kot.

Wszystko inne zostało jako blok „miejsce na treść” (`.todo`) do wypełnienia po rozmowie z klientką.

## Do potwierdzenia przed wysyłką / wdrożeniem

- pełna lista usług i cennik, diagnostyka na miejscu (USG, RTG, badania krwi),
- czy gabinet robi wizyty terenowe i na jakim obszarze,
- skład zespołu (w opiniach Google przewijają się imiona Kinga, Maja, Daria),
- czy `gw.mazovet@wp.pl` ma być publicznym adresem kontaktowym (adres pochodzi z CRM),
- zdjęcia pacjentów i wnętrza: w demie zwierzęta są ze stocku (Unsplash), zdjęcia obiektu są prawdziwe.

## Stack

Statyczny HTML bez build-stepu. Podstrony generuje `python3 tools/build.py` (szablon + `tools/content.py`), `bash bump.sh` dopisuje cache-buster `?v=md5` do `assets/*`. Po każdej zmianie treści lub stylów: `python3 tools/build.py && bash bump.sh`.
