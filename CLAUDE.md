# sEBU – smarter Einkaufsberater

Mobile-first Web-App (eine Datei), gehostet auf GitHub Pages: https://schubiger-rico.github.io/smartshop-schweiz/
Besitzer: Rico Schubiger (GitHub `Schubiger-Rico`), Schweiz, Deutsch. Er arbeitet vom Natel aus. Es gibt nur diesen einen Arbeitsort (diese Code-Sitzung); der frühere Chat wird nicht mehr gebraucht.

## Regeln für die Zusammenarbeit (verbindlich)
- Sprache: Deutsch, **Schweizer Rechtschreibung (ss, nie ß)**. App-Texte ebenso.
- **Bei unklarer Definition immer nachfragen**, bevor gebaut wird (z. B. welcher Knopf, wo genau, wie lange). Nicht raten.
- **Nur eine Frage auf einmal**, mit einem Vorschlag daneben. Kurz antworten, keine langen Listen.
- **Wünsche zuerst nur festhalten** (in `docs/ENTSCHEIDUNGEN.md` unter «Gewünscht, noch nicht gebaut»). **Bauen erst**, wenn Rico ausdrücklich sagt: «umsetzen», «erstelle», «setze alles um». Bei Fehlern sagt er «bitte beheben», dann sofort beheben.
- App-Prinzip: **«Alles kann, nichts muss.»** Nichts ist aufdringlich, jede Automatik ist erklärbar und abschaltbar. Die App hilft, sie entscheidet nicht.
- **Jede neue Funktion und Einstellung automatisch in die Wegleitung aufnehmen** (App-Führung und/oder Einstellungen-Führung, Arrays `AREAS`/`SA`, ggf. `NEED`), ohne dass Rico es extra sagen muss.
- Wegleitung/Tour: Bei Einstellungen immer erklären, wofür welcher Wert geeignet ist und «Wenn es nicht klappt, probiere …», damit niemand denkt, die App sei schlecht, wenn nur die Einstellung nicht passt.
- Nach jeder Änderung: Tests laufen lassen (siehe unten), dann auf `main` committen und pushen. GitHub Pages ist nach etwa einer Minute live. Rico sagen, was geändert wurde (1–3 Sätze) und was er tun muss (meist nichts; bei Symbolwechsel iPhone-Homescreen-Symbol neu hinzufügen).
- Nie Geheimnisse (API-Schlüssel) ins Repo schreiben.

## Dateien
- `index.html` – die ganze App (HTML + CSS + ein JS in einer IIFE am Ende). **Quelle der Wahrheit, direkt hier ändern.**
- `manifest.json`, `sw.js`, `icon-180.png` – PWA. `sw.js` lädt eigene Dateien immer frisch (no-cache), offline aus dem Speicher. Das Symbol ist neon-grünes «sEBU» auf dunklem Grund (apple-touch-icon).
- `docs/ENTSCHEIDUNGEN.md` – alle Entscheide, Wünsche, offene Punkte (ausführlich, zuerst lesen!). `ROADMAP.md` – ältere Roadmap.
- `tests/t*.py` – Playwright-Tests (Python). Aufruf im Repo-Hauptordner: `python3 tests/t.py` (sie öffnen `index.html` per file:// aus dem aktuellen Ordner; Chromium + playwright sind vorinstalliert). Jeder Test endet mit `[]` = keine JS-Fehler. t.py allgemein+Tour, t2 Teilen (zwei Handys, Firebase gemockt), t3 Ladentypen/Overpass gemockt, t4 Läden/Ketten/eigene Läden, t5 Aktionen-Modi, t6 App-Tour, t7 Einstellungs-Tour, t8 «← Liste»/«Immer», t9 Einkaufsende «Noch offen», t10 «Welcher Laden?», t11 Ansicht Einfach/Umfänglich/Manuell, t12 Test-Hinweise «🚧», t13 Rückgängig/Sicherung/Strichcode (Firebase und Open Food Facts gemockt), t14 Notfall/dringend, t15 Symbole/Auto-Symbol/Kategorie-Farben, t16 Kopfzeile/Sprache (gemockt)/Öle, t17 Nur Symbole/Erklärung beim Gedrückthalten/Schriftgrösse, t18 Sprach-Parser (gemockt), t19 Kategorien/Auto-Kategorie/Kategorie-Auswahl.
- Falls `playwright` fehlt: `pip install playwright`, dann Chromium-Pfad `/opt/pw-browsers/chromium` als `executable_path` übergeben (nicht `playwright install`).
- Syntaxprüfung: letztes `<script>` extrahieren und `node --check`.
- Alte Dateien im Repo (`SmartShop_V5.html`, `SEBU-*.zip`, `sw.js.txt`) sind überflüssig und dürfen gelöscht werden.

## Technik
- Alles in localStorage-Key `sebu.v1`; State `S`: items, favs, hist, cats, learn, mine (eigene Läden: name, lat, lon, off, r, hint), cchains, chains, cache, ev, deals, queue, ob, shop, share, set (dm, radius, fbUrl …), types, dismiss. `item.today` = «Heute noch» (Datum).
- UI: Event-Delegation über `data-a` (Funktion `act()`), Änderungen über `data-chg`, Neuzeichnen mit `R()`. Tour mit `.hl` Hervorhebung, `tourGuard`.
- Ladenerkennung: GPS + Overpass/OpenStreetMap (`out bb tags`), Ketten-Liste `CHB` (46 Ketten inkl. Otto's, Landi, Manor, Jumbo, Apodro …), Radius `auto` (Ladengrösse aus OSM, GPS-Genauigkeit, nächster gewinnt, Gleichstand <15 m → Nachfrage «Welcher Laden?», Wahl wird gemerkt) oder 25/50/100/250 m; eigene Läden mit eigenem Radius.
- Ansicht der Liste: `S.set.view` (simple/full/manual) und `S.set.show` (cat, catcol, fav, urg, shop, bar, voice, cam, scan, nav, remind, recent); 🔥 = `S.set.dm`, Kategorien-Zeile = `S.set.cats`. Hilfsfunktionen `on(k)`, `setOn`, `setView`, `viewBlock()` (Einstellungen-Sparte «Einkaufsliste» und Begrüssung nach der Schriftgrösse). Tour-Schritte zu ausgeblendeten Elementen werden übersprungen (`NEED`).
- Während eines Einkaufs (`S.shop`) keine Laden-Vorschläge (🔄 manuell geht). Einkaufsende zeigt «Noch offen» (Heute noch merken / Später / 🔔 Erinnerung beim Wegfahren per Teilen-Text / 🧭 Navigation = Google-Maps-Link `mapBtn()`). Erinnerung optional über iPhone-Kurzbefehl (`S.set.remSc`, `S.set.scName`, URL `shortcuts://run-shortcut`).
- Aktionen (🔥): Modi automatisch / manuell / immer / aus. Hinweis oben nur für echte (nicht Beispiel-)Aktionen, bei jedem Öffnen, ✕ blendet bis zum nächsten Öffnen aus (`dealHid`). Unter «Aktionen» Händler-Links (`DLINK` direkte Adressen für alle 9: Migros, Coop, Denner, Aldi, Lidl, Volg, Spar, Aligro (Prospekte), Otto's; Rückfall Google-Suche, `#dlinks`). Teilen über Firebase RTDB (optional). KI-Ratgeber über Anthropic-API (optional, Schlüssel nur lokal beim Nutzer).
- Menü: ☰ rechts auf der Anrede-Zeile «Hallo …» (`hrow` unter dem Titel). Läden steht in der Hauptnavigation (wie Favoriten). Titel «sEBU», Untertitel «smarter EinkaufsBerater» (kleines s, grosses B, etwas grösser als früher), Schrift Baloo 2 kursiv, Neon-Grün `#39FF14` mit dunkelgrünem Rand `#0a5c00`. Slogan: «Alles kann, nichts muss.» (in Neon-Grün wie der Titel)
- Test-Hinweise: gelbes «🚧 TEST: Ist noch in Arbeit» (Sprüche `WIPQ`) in Ideen, Anlässe, Stammartikel, Premium-KI, Abo, Sprache; bei Aktionen «Hier könnten Ihre Aktionen stehen!» (`DEALQ`). Abschaltbar: Darstellung → «Test-Hinweise anzeigen» (`S.set.testBan`).
- Notfall: `item.urg` (❗ bei der Eingabe `draft.urg`, im Bearbeiten, rotes ❗ auf der Karte entfernt es). Dringendes immer zuoberst (`sortedItems`), in jedem Laden sichtbar, rot umrandet und grösser; Einkaufsende-Hinweis «Dringend noch offen» (`urgEnd`).
- Kategorien: `STD` 19 Hauptkategorien (m0–m18; m4 heisst «Vorräte», neu m14 Internationale Küche, m15 Bio/Vegi/Vegan, m16 Fertiggerichte, m17 Non-Food, m18 Frühstück; m4s7/m4s8 stillgelegt = 3. Feld 1 → versteckt, Inhalte einmalig nach m18 verschoben, `S.set.migFr`), Unterkategorien nur **hinten anfügen** (IDs `m<i>s<j>` nach Position!). `addStdCats()` ergänzt fehlende Standard-Kategorien bei bestehenden Nutzern (vor «Übrige»). Auto-Kategorie `detectKw`: Stichwort, das am **weitesten hinten** im Namen endet, gewinnt (Grundwort), bei Gleichstand das spätere/längere; dann Einzahl/Mehrzahl-Varianten, dann Symbol-Gruppe (`ICAT`). Strichcode: Kategorie aus Open Food Facts (`offCat`). Liste innerhalb einer Unterkategorie alphabetisch. Gedrückthalten aufs Produkt-Symbol zeigt «gehört zu Haupt › Unter» (`catPath`). Auswahl-Sheet `shCat`: Suche `catQ`, Hauptkategorien mit ▸ aufklappbar (`catOpen`).
- Symbole: `EMO` (16 Gruppen, Suchwörter inkl. Schweizerdeutsch, Wortstämme wie «erdbeer»). `iconOf()`: gelerntes Symbol (`S.learn.icons[name]`) → `autoIcon(name)` (frühestes Wort ≥4 Zeichen im Namen gewinnt: Paprikapulver → 🫑) → Kategorie-Symbol. Eigenes Symbol über Kategorie-Auswahl «Eigenes Symbol für das Produkt» (`picon`).
- Kategorie-Farben: `cat.color` (frei wählbar unter Kategorien, `data-ccol`), Standard `DEFCOL` für die 14 Hauptkategorien, Unterkategorien erben; Streifen links an der Karte (`catColor`), Schalter `catcol`.
- Kopfzeile (`shopBar`, Klasse `topbar`): 🛒, 📍, 🔄, 📷 – nur Symbole (🎤 steht in der Eingabezeile vor dem Feld, Klasse `hasmic`); Text «Start»/«Laden» nur mit `S.set.btnText`. Erklärung beim Gedrückthalten (2 s, `HELP`-Texte nach `data-a`, sonst aria-label; Klick danach wird unterdrückt), abschaltbar `S.set.lpHelp`. Neue Knöpfe: HELP-Text ergänzen! Eingabefeld eigene Zeile, wenn Breite/Schrift < 24 (`html.addwrap`, Grid): ＋ rechts doppelt hoch über beide Zeilen.
- Sprache: 🎤 → Sheet `voice`, `webkitSpeechRecognition` (de-CH), `parseSpeech()` trennt an Komma/«und»/«sowie», Menge vor oder nach dem Produkt, Teil nur mit Menge gehört zum Produkt davor, Füllwörter (`FILL`) weg; Bestätigung mit änderbaren Feldern (`data-vi`) und ✕, dann «＋ n auf die Liste». Ohne Spracherkennung Hinweis auf Tastatur-Diktat.
- Hinweis «nach links wischen» nur bis 3× gewischt (`S.set.swipeN`, Knopf «Wieder anzeigen» unter Darstellung). Letzte Produkte: Anzahl/Sortierung nur in den Einstellungen.
- Zeilenhöhe: `S.set.rows` compact (Standard) / normal, Klasse `html.compact` in `applyLook()`.
- Rückgängig: `delItem()` + `undo` (4 s, Leiste unten). Wischen und «Löschen» nutzen es.
- Sicherung: Zwischenkopien täglich in localStorage `sebu.bak` (letzte 5, `snap()`), optional täglich in eigene Firebase `/lists/bak-<bakCode>.json` als `{t,j}` (unter `lists`, damit die bestehenden Teilen-Regeln reichen) (JSON-String, ohne apiKey; `cloudBak()`); Holen per Code. Hilfsfunktion `fbSet()` (nicht mit `fbOk()` vom Teilen verwechseln).
- Strichcode: 📷 → Wahl «Strichcode»/«Ratgeber» (`camwhich`), Sheet `scan`: Kamera (BarcodeDetector, sonst ZXing von jsdelivr `@zxing/library@0.21.3`, nachgeladen), Foto, Nummer von Hand; Daten von Open Food Facts API v2.
- iPhone-Homescreen-App hat eigenen Speicher (Backup/Restore über Text in den Einstellungen).
- Die Umgebung hat evtl. kein Internet für pip/npm; Fonts (Baloo 2) sind nicht lokal installierbar.

## Offene Punkte (Stand 21.11.2026)
- Erledigt 21.11.: Nachfrage «Welcher Laden?» bei zwei fast gleich nahen Läden (gemerkt pro Paar in `S.learn.pick`).
- Zurückgestellt: Autokorrektur aus (nicht genehmigt), Quelle/Anfragen für Aktionsdaten, rechtliche Prüfung, Abo/Server, Übersetzungen, echter KI-Schlüsseltest, echter Firebase-Teilen-Test.
- Tour Schritt «Im Verlauf» und «🧭» haben keine Hervorhebung, wenn Verlauf/Läden leer sind (akzeptiert).
- Details und alle früheren Entscheide: `docs/ENTSCHEIDUNGEN.md`.
