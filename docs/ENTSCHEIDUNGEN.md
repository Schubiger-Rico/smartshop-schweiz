
## SEBU SmarterEinkaufsBerater – Entscheide und Übergabe

**Stand:** 17. November 2026. Diese Zusammenfassung enthält alle Entscheide aus dem Chat nach dem Übergabedokument Block 9–16. Sie ergänzt dieses Dokument und ersetzt es dort, wo es widerspricht.

**Lesehinweis:** **[Entschieden]** hast du ausdrücklich bestätigt. **[Vorschlag]** stammt von mir und ist noch nicht bestätigt. **[Dok.]** steht so in deinen früheren Dokumenten.


## 1. Projekt und Grundregeln

- Titel: **SEBU SmarterEinkaufsBerater**. SEBU ist grösser, in hellem Grün mit dunkelgrünem Rand. [Entschieden]
- Die früheren Dokumente nennen „Der smarte Einkaufsbegleiter“ als Untertitel. Das widerspricht dem neuen Titel und muss in den Dokumenten angepasst werden. [Offen]
- Eine einzige Datei <code>index.html</code> auf GitHub Pages (https://schubiger-rico.github.io/smartshop-schweiz/), Mobile First, localStorage. [Dok.]
- Philosophie: Alles kann, nichts muss. SmartShop hilft, SmartShop entscheidet nicht. Nichts ist aufdringlich. Jede Automatik ist transparent, erklärbar und abschaltbar. [Dok.]
- Die App soll möglichst smart sein und aus allem lernen, was sie darf. [Entschieden]
- Schriften: Atkinson Hyperlegible für Texte (gut lesbar), Quicksand für Titel. [Entschieden]
- Schriftgrösse: Standard 18 px, einstellbar 10–40 px. rowHeight = fontSize × 1.67. [Dok.]
- Alle Knöpfe sind quadratisch, Breite gleich Höhe. [Entschieden]
- Rechtschreibung: Schweizer Schreibweise mit „ss“, nie „ß“. [Entschieden]
- Nummerierung: Block 9 enthält **Kapitel 1 Kategorien & Smart-Sortierung** und **Kapitel 2 Filialerkennung**. Block 10–16 behalten die SEBU-Nummerierung (10 Einführung, 11 Aktionen & Preise, 12 Privat/Geschäft/Verein/Events, 13 Stammartikel, 14 Ideen, 15 Smart-Aktionen, 16 Premium-KI). [Entschieden]
- Menü: Einkaufsliste, Favoriten, Aktionen, Ideen, Einstellungen, neu am Ende **Ratgeber**. Die Zusatzpunkte Anlässe, Stammartikel, Premium-KI und Test & Feedback sind in der App gebaut, ihre endgültige Stellung im Menü ist nicht geklärt. [Offen]

## 2. Block 2 – Produktzeile und Eingabe

- Nur der Produktname ist nötig. Menge und Einheit sind optional. [Dok.]
- Produkt bekommt die Restbreite. Menge: drei Ziffern breit, Startwert 0. Einheit: so breit wie das längste Wort der Auswahl. [Entschieden]
- Haken ganz rechts. Der Löschknopf entfällt. Löschen durch **Wischen nach links**. [Entschieden]
- Einheiten: Stk., kg, g, ml, lt, dazu Freitext. Selbst geschriebene Einheiten bietet die App danach in der Liste an. „Pack“ entfällt. [Entschieden]
- Eingabezeile: Beim Tippen erscheint links das erkannte Kategorie-Symbol, ein Tipp darauf ändert die Kategorie. Neben ＋ gibt es einen Kamera-Knopf zum Ratgeber. [Entschieden]
- Rechtschreibhilfe: Beim Tippen schlägt die App Produkte vor, aus Verlauf, Favoriten und einer eingebauten Liste häufiger Produkte mit Schweizer Begriffen (zum Beispiel Poulet, Rüebli, Nüsslisalat). Tippfehler wie „Milsch“ werden zu „Milch“ vorgeschlagen. [Entschieden]
- Mundart: Die App lernt Mundartwörter. Die Liste zeigt das Wort so, wie du es schreibst (zum Beispiel „Rüebli“), intern verknüpft sie es mit dem Standardprodukt („Karotten“) für Kategorie, Aktionssuche und Preisvergleich. [Entschieden]

## 3. Block 4, 5, 6, 7 – Listen und Einstellungen

- **Letzte Produkte:** unter der Einkaufsliste. Anzeige 10/20/50/100/Alle (Standard 20), Sortierung neueste oder älteste zuerst, Auswahl direkt bei der Überschrift. [Entschieden]
- **Favoriten:** automatisch ab 3, 5 oder 10 Käufen oder aus. Standard 5. Manuell gesetzte Favoriten bleiben immer. Letzte Menge wird übernommen. [Entschieden]
- **Verlauf:** bleibt auf der Seite Favoriten. Ein Tipp öffnet einen Eintrag zum Bearbeiten, Wischen nach links löscht, „Alles leeren“ fragt einmal nach. Felder: Produkt, Menge, Einheit, Datum, Laden, Aktion, Preis, Kategorie. [Entschieden]
- **Einstellungen:** Schriftgrösse, Dark Mode, Akzentfarben, benutzerdefinierte Farben, Zurücksetzen. [Dok.] Heute löscht „Zurücksetzen“ in der App alle Daten, das Dokument meint die Einstellungen. [Offen]
- **Mehrsprachigkeit** für Deutsch, Französisch, Italienisch und Englisch ist vorzubereiten. Noch nicht besprochen, in der App fehlt sie. [Dok.]

## 4. Block 8 – GPS

- Modi: Aus, Nachfragen, Automatisch. [Dok.]
- Radius: vier feste Werte **25, 50, 100, 250 m**, ohne Regler. Standard **25 m**. In Gebäuden ist GPS oft ungenau, bei 25 m erkennt die App deshalb manchmal keinen Laden. Dann den Laden von Hand wählen oder den Radius erhöhen. [Entschieden]
- Die App merkt sich die bevorzugte Filiale. [Dok.]
- Komfortfunktionen: Vibration und Liste öffnen. „Lautlos“ kann eine Web-App nicht schalten. [Dok., technisch begrenzt]

## 5. Block 9 Kapitel 1 – Kategorien & Smart-Sortierung

**Kategorien**

- Grosse Auswahl an Standard-Hauptkategorien mit Unterkategorien, dazu eigene Haupt- und Unterkategorien. [Entschieden]
- **Zwei Ebenen**: Hauptkategorie und Unterkategorie (zum Beispiel Milch & Eier → Joghurt). [Entschieden]
- Jedes Produkt hat **genau eine Kategorie** mit optionaler Unterkategorie. [Entschieden]
- Standard-Kategorien lassen sich umbenennen und ausblenden, aber nicht löschen. Ausgeblendete lassen sich wieder einblenden. Löschen geht nur bei eigenen. [Entschieden]
- Beim Löschen einer eigenen Kategorie fragt die App, in welche Kategorie die Produkte verschoben werden. [Entschieden]
- Datenmodell: <code>{id, name, parentId, icon, color, sortOrder, custom}</code>. [Dok.]
**Symbol**

- Emoji. Die Karte zeigt das Symbol der Unterkategorie, ohne Unterkategorie das der Hauptkategorie. [Entschieden]
- Design wie die Knöpfe: abgerundetes Quadrat (Breite gleich Höhe), **hellgrüner Hintergrund**, dunkelgrüner Rand, Radius 20 %, Rahmen 8 % (1–3 px), Symbol zentriert, keine Schatten, keine Animation. Der hellgrüne Hintergrund ersetzt den „transparenten Hintergrund“ der Spezifikation. [Entschieden]
- Eigene Kategorien: Symbol aus einem grossen Raster nach Themen (Essen, Getränke, Haushalt, Tiere, Sonstiges) mit Suchfeld. [Entschieden]
- Die Einkaufsliste bleibt **flach**, jedes Produkt hat links sein Symbol. [Entschieden]
**Erkennung und Ändern**

- Die App erkennt die Kategorie automatisch aus dem Produktnamen. [Entschieden]
- Ändern per Tipp aufs Symbol und im Bearbeiten-Dialog. [Entschieden]
- Bei unbekanntem Produktnamen fragt die App dezent nach der Kategorie und lernt daraus. Die Frage lässt sich überspringen, dann bleibt das Produkt ohne Kategorie. [Entschieden]
- Die Reihenfolge der Kategorien änderst du in einer eigenen Ansicht unter Einstellungen per Drag & Drop. [Entschieden]
**Smart-Sortierung**

- Grundeinstellung: deine manuelle Reihenfolge. [Entschieden]
- Erkennt die App den Laden, übernimmt sie sofort die gelernte Reihenfolge dieses Ladens. Sie lernt pro Laden aus der Abhakreihenfolge und verbessert sie mit jedem Einkauf. Ziel: kürzester Weg durch den Laden. [Entschieden]
- Gelernt wird nur beim Einkaufen: bei erkanntem Laden startet der Einkauf automatisch, sonst startest du ihn mit „Einkauf starten“ von Hand. Beides lässt sich abschalten. [Entschieden]
- Es gibt keine Ladenpläne als Datenquelle. Beim ersten Besuch gilt die manuelle Reihenfolge. [Hinweis]
**Smart-Lernen**

- Lernt aus Kategoriekorrekturen, Verlauf, Favoriten, Laden und Abhakreihenfolge. [Dok.]
- Eigene Seite „Smart-Lernen“ in den Einstellungen: zeigt das Gelernte (Produkt → Kategorie, Reihenfolge pro Laden), erlaubt Löschen einzelner Einträge, Abschalten und Zurücksetzen. Bei einer automatischen Kategorie erklärt die App kurz, warum. [Entschieden]

## 6. Block 9 Kapitel 2 – Filialerkennung

- Inhalt wie im Übergabedokument Block 9–16: Ketten erkennen (Migros, Coop, Lidl, Aldi, Denner, Spar, Volg), Filialverwaltung, eigene Läden, Komfortfunktionen. [Dok.]
- Heute über OpenStreetMap (Overpass). Das braucht Internet.

## 7. Offline-Betrieb im Laden

- Abhaken, Lernen und alle Daten funktionieren ohne Netz, sie liegen auf dem Handy. [Hinweis]
- Die App braucht eine **Offline-Funktion** (wie eine installierte App auf dem Startbildschirm), damit sie ohne Empfang öffnet. Die Schrift fällt sonst auf eine Standardschrift zurück. Noch nicht gebaut. [Vorschlag]
- Bereits gefundene Läden werden zwischengespeichert, der Laden lässt sich von Hand wählen. [Vorschlag]

## 8. Block 10 – Einführung

- Erststart in dieser Reihenfolge: 1) Name abfragen, nur wenn man möchte, sonst weiter. Der Name wird für persönliche Texte verwendet. 2) Textgrösse mit Live-Auswahl. 3) Geführte App-Erklärung, schön der Reihe nach, nur wenn man möchte. 4) Führung durch die Einstellungen mit Erklärung, nur wenn man möchte. [Entschieden]
- Der Name ist freiwillig, überspringbar, änderbar und löschbar. [Dok.]
- Die Tour soll so ausführlich werden, dass man genau weiss, wie die App funktioniert. Kategorien (Erkennung, Ändern, eigene, Reihenfolge, Smart-Sortierung) und alle weiteren Funktionen gehören hinein. Heute hat sie 5 statt etwa 24 Schritte und die Einstellungs-Führung 7. [Entschieden]
- Die weiteren Regeln der Tour stehen im Übergabedokument Block 9–16 (Schrittzähler, Abdunkeln, Aktionen wirklich ausführen, humorvolle Reaktionen, Abschlusstitel nicht speichern). [Dok.]

## 9. Block 11 – Aktionen

**Aktionsknopf 🔥**

- Ist die Aktionssuche **aus**, ist das 🔥 leicht transparent. Ist sie **an**, ist es voll sichtbar mit den Farben Rot, Gelb, Grün oder Grün/Gelb. [Entschieden, so verstanden]
- **2 Sekunden halten** zeigt mehr Infos zu den Aktionen des Produkts. Mein Vorschlag für den Inhalt: Kette, Aktionspreis, Normalpreis mit Ersparnis in Prozent, Preis pro Kilo oder Liter, Zeitraum mit Restlaufzeit, Entfernung zur Filiale. [Vorschlag]
- Wunsch: Beim Wählen des Knopfs im Internet suchen, wer was wo und wann im Angebot hat. Das geht nur mit einer erlaubten Datenquelle. [Offen]
**Datenquelle**

- Eine offizielle Schnittstelle von Migros oder Coop gibt es nicht. Migros gewährt laut Forum keinen Zugang und blockiert Bots, Coop schützt die Seite mit einem Anti-Bot-Dienst. [Recherche]
- Bis eine Quelle da ist, bleiben die Aktionen **Beispieldaten**, deutlich gekennzeichnet. [Entschieden]
- Zwei Anfragen sind als Entwurf vorbereitet: an Rappn (rappn.ch) und an das GitHub-Projekt grocery-discount. Ob sie versendet wurden, ist nicht bekannt. [Offen]
- Rechtslage: Automatisches Auslesen fremder Seiten ist eine Grauzone (Nutzungsbedingungen, Urheberrecht an Prospekten und Bildern, UWG). Vor einer öffentlichen oder kommerziellen Veröffentlichung ist eine Rechtsprüfung nötig. [Offen]
**Zusätzliche Quelle: Aktion per Foto**

- Du fotografierst im Laden das Aktionsschild oder den Prospekt. Die KI liest Produkt, Preis, Normalpreis, Zeitraum und Laden. [Entschieden]
- Die App zeigt die gelesenen Werte, du korrigierst bei Bedarf und **bestätigst**, erst dann wird gespeichert. [Entschieden]
- Erfasste Aktionen sehen im Moment nur du. Teilen über die Cloud ist Zukunft (Vorbereitung Block 12). [Entschieden]
- Abgelaufene Aktionen werden automatisch gelöscht. [Entschieden]
- Ausnahme: Für Produkte mit 🔥 behält die App einen unsichtbaren Eintrag (Produkt, Laden, Start, Ende, Preis). Daraus schätzt sie ab drei erfassten Aktionen den **Rhythmus** („kehrt etwa alle 6 Wochen wieder“, als Schätzung gekennzeichnet, in Block 15, abschaltbar und löschbar). [Entschieden]

## 10. Ratgeber (neues Kapitel)

- Eigener Menüpunkt am Ende des Menüs, zusätzlich der Kamera-Knopf in der Eingabezeile. Der Menüpunkt erweitert Block 1 und braucht deine Bestätigung. [Entschieden]
- Ablauf: Foto von Produkten, zum Beispiel verschiedene Mehle, die KI vergleicht nach Preis, Qualität und Zweck. [Entschieden]
- Mit Empfang vergleicht die App vor Ort. Ohne Empfang wartet das Foto auf dem Handy und wird später abgeschickt, mit Meldung, wenn die Antwort fertig ist. [Entschieden]
- Der Vergleich stützt sich auf Produkttests aus dem Internet, mit Quelle und Link. Texte werden zusammengefasst, nicht kopiert. [Entschieden]
- Antwort: kurz mit klarer Empfehlung, „Mehr“ klappt die ausführliche Übersicht auf. Was die KI nicht lesen konnte, steht kurz dabei. [Entschieden]
- Rückfragen sind möglich. Das Foto bleibt dafür verfügbar, solange der Antwort-Bildschirm offen ist, und wird beim Verlassen gelöscht. Die Antwort bleibt als Text. [Entschieden]
- Ein Knopf „Auf die Liste“ trägt die Empfehlung mit Name und Kategorie ein, nur auf dein Tippen. [Entschieden]
- Der Datenschutz-Hinweis sagt klar, dass ein Foto nur an den KI-Dienst geht, wenn du den Vergleich selbst auslöst. [Entschieden]
- **Zugang zur KI:** Zuerst ein eigener Zugangsschlüssel in den Einstellungen für deine Tests (Kosten pro Anfrage wenige Rappen, ob der Browser direkt senden darf, ist vor dem Bau zu prüfen). Später ein kleiner Server mit Premium-Abo (CHF 2) für alle. [Entschieden]
- Zum Testen kannst du Fotos auch hier im Chat schicken, ich vergleiche sie mit Tests aus dem Internet. [Hinweis]
- Quellen für Tests: Schweizer zuerst (Kassensturz, K-Tipp, Saldo, Konsumentenschutz), deutsche (Stiftung Warentest, Ökotest) nur, wenn es keinen aktuellen Schweizer Test gibt, mit Kennzeichnung. Viele Tests liegen hinter einer Bezahlschranke. [Vorschlag]
- Strichcode lesen und über Open Food Facts nachschlagen als Grundlage vor der Foto-Erkennung. [Vorschlag]
- Allgemeine Ratgeber ohne Marken und Preise (zum Beispiel Mehlsorten und Zwecke) sind ohne Datenquelle möglich. [Vorschlag]

## 11. Block 12–16

Block 12 (Privat/Geschäft/Verein/Events, Lernsystem), 13 (Stammartikel), 14 (Ideen), 15 (Smart-Aktionen), 16 (Premium-KI) und das Abo-Modell gelten wie im Übergabedokument Block 9–16, mit diesen Ergänzungen: Rhythmus der Aktionen in Block 15, Prognosen und Foto-KI in Block 16. Preisvergleich und Lernsystem sind in Block 11 und 12 eingegliedert. [Dok. + Entschieden]


## 12. Stand der App

**Gebaut** (<code>index.html</code>, ungetestet auf dem Handy, im Headless-Browser durchgeklickt): neuer Titel, Schrift, 18 px Standard, Wischen zum Löschen, Haken rechts, Mengenfeld mit 0, Erststart mit Name und Textgrösse, geführte Erklärung und Einstellungs-Führung, Block 1–8 grundlegend, Filialerkennung, Aktionsseite mit Beispieldaten, Anlässe, Stammartikel, Ideen, einfache Prognosen.

**Nicht gebaut:** Kategorien und Smart-Sortierung, Rechtschreibhilfe und Mundart, Einheiten laut Entscheid, Letzte Produkte mit Auswahl, Favoriten-Schwelle, Verlauf bearbeiten, feste GPS-Radien, Ratgeber und Foto-KI, Aktion per Foto, Rhythmus, 2-Sekunden-Halten und transparentes 🔥, Offline-Funktion, Mehrsprachigkeit, ausführliche Tour.


## 13. Offene Punkte

- Datenquelle für echte Aktionen (Anfragen an Rappn und grocery-discount, Rechtsprüfung).
- Titel und Untertitel in den früheren Dokumenten angleichen.
- Menü: Stellung von Anlässe, Stammartikel, Premium-KI und Test & Feedback.
- „Zurücksetzen“: nur Einstellungen oder alle Daten.
- Quellen für Produkttests und Strichcode bestätigen.
- Inhalt des 2-Sekunden-Halten-Infos bestätigen.
- Block 1–9 gelten in den Dokumenten als eingefroren („Änderungen nicht zulässig“). Die Erweiterungen aus diesem Chat ändern diese Blöcke und sind von dir freigegeben (17.11.2026, erledigt).
- Das „Verhältnis 30:18“ aus der technischen Dokumentation ist unklar.
- Die Preisvergleichs-Einheiten (100 g, 1 kg, 100 ml, 1 l gegenüber Liter, Kilo, Stück) sind nicht in Einklang gebracht.
- Das Abo-Modell ist nur als Testauswahl vorhanden, eine Bezahlung gibt es nicht.

## 14. Ergänzungen vom 17.11.2026 (Vormittag)

Diese Entscheide kamen nach dem ersten Stand dazu. Wo sie den Abschnitten oben widersprechen, gelten sie.

- **Freigabe:** Änderungen an Block 1–9 sind von dir freigegeben. [Entschieden]
- **Zurücksetzen:** zwei getrennte Knöpfe. „Einstellungen zurücksetzen“ stellt Schriftgrösse, Farben, GPS und Design auf die Standardwerte. „Alle Daten löschen“ löscht alles. Beide fragen vorher einmal nach. [Entschieden]
- **Menü:** fünf feste Punkte (Einkaufsliste, Favoriten, Aktionen, Ideen, Einstellungen), danach ein Untermenü „Mehr“ mit Ratgeber, Anlässe, Stammartikel, Premium-KI und Test & Feedback. [Entschieden]
- **2 Sekunden halten auf 🔥:** pro Aktion Kette, Aktionspreis, Normalpreis mit Ersparnis in Prozent, Preis pro Kilo oder Liter, Zeitraum mit Restlaufzeit, Entfernung zur Filiale. Bei beobachteten Produkten kommt der geschätzte Rhythmus dazu, sobald mindestens drei Aktionen erfasst sind. [Entschieden]
- **Tour:** etwa 25 Schritte in Themenbereichen (Liste, Kategorien, Aktionen, Favoriten und Verlauf, Filialen, Ratgeber, Einstellungen). Jeder Bereich lässt sich einzeln starten, die Gesamttour bleibt möglich. [Entschieden]
- **Mehrsprachigkeit:** alle Texte liegen in einer Übersetzungstabelle, aktiv ist vorerst nur Deutsch. Die Sprachwahl in den Einstellungen zeigt Französisch, Italienisch und Englisch als „bald verfügbar“. Übersetzt wird, wenn die Texte feststehen. [Entschieden]
- **Offline:** Die App ist installierbar und öffnet ohne Empfang, samt Schrift. Dafür kommen zwei kleine Dateien zur <code>index.html</code> dazu. Das weicht von der Vorgabe „eine einzige Datei“ ab und ist freigegeben. [Entschieden]
- **Produkttests im Ratgeber:** zuerst Schweizer Quellen (Kassensturz, K-Tipp, Saldo, Konsumentenschutz). Gibt es keinen aktuellen Test, nimmt der Ratgeber Stiftung Warentest oder Ökotest und kennzeichnet das. Liegt ein Test hinter einer Bezahlschranke, sagt die App das und verlinkt auf die Quelle. [Entschieden]
- **Strichcode:** Der Ratgeber liest ihn und schlägt das Produkt bei Open Food Facts nach. Preise gibst du von Hand ein. Wo das Lesen im Browser nicht geht oder das Produkt fehlt, gilt das Foto für die KI. [Entschieden]
- **Preiseinheiten:** Standard pro 100 g und 100 ml bei kleinen Mengen, pro kg und l bei grossen, pro Stück bei Stückware. In den Einstellungen lässt sich eine feste Einheit wählen. [Entschieden]
- **Abo (Zuordnung):** Gratis: Liste, Favoriten, Verlauf, Kategorien, Smart-Sortierung, Einführung, Aktionssuche mit 🔥, Aktionen per Foto. Smart (CHF 1): Preisvergleich, GPS und Filialerkennung, Preisalarme, Rhythmus. Premium (CHF 2): Ratgeber mit Foto-KI, Prognosen, Einkaufsoptimierung. Die App sperrt vorerst nichts, damit alles testbar ist. [Entschieden]
- **Verhältnis 30:18:** ist die Zeilenhöhe im Verhältnis zur Schrift (30 ÷ 18 = 1,67) und damit derselbe Faktor wie rowHeight = fontSize × 1.67. Nichts Zusätzliches. [Entschieden]

### Standard-Hauptkategorien (14)

Jede lässt sich umbenennen und ausblenden, nicht löschen. Eigene kommen dazu. [Entschieden]

Symbol

Hauptkategorie

Unterkategorien

🥦

Obst & Gemüse

Früchte, Gemüse, Salat, Kräuter, Pilze

🥛

Milch & Eier

Milch, Joghurt, Käse, Butter, Eier, Rahm

🥩

Fleisch & Fisch

Poulet, Rind, Schwein, Wurstwaren, Fisch

🍞

Brot & Backwaren

Brot, Zopf, Gebäck, Mehl & Backzutaten

🍝

Teigwaren, Reis & Konserven

Teigwaren, Reis, Konserven, Saucen

🧊

Tiefkühl

Gemüse, Fertiggerichte, Glace

🥤

Getränke

Wasser, Süssgetränke, Saft, Bier & Wein, Kaffee & Tee

🍫

Snacks & Süsses

Schokolade, Chips, Guetzli, Nüsse

🧴

Körperpflege

Haut, Haare, Zahnpflege, Hygiene

🧽

Haushalt

Reinigung, Wäsche, Küchenbedarf, Papier

🐾

Tiere

Hund, Katze, Sonstiges

👶

Baby & Kind

💊

Apotheke & Gesundheit

📦

Übrige


### Notiz vom 18.11.2026: Einkaufsort pro Produkt (nur festgehalten, noch nicht gebaut)

- Bei der Eingabe soll man wählen können, wo ein Produkt gekauft wird, zum Beispiel bei Coop, wenn man das schon weiss.
- Die Einkaufsliste eines Ladens (zum Beispiel Coop) erscheint nur, wenn man in der Nähe dieser Filiale ist. Sonst bleibt die Standardliste.
- Entschieden: Produkte ohne Ladenwahl sind der Standard und erscheinen immer in der Standardliste. Entschieden: Ein Produkt kann mehreren Läden zugeordnet sein. Es erscheint in der Liste jedes dieser Läden, sobald man in der Nähe ist, und in der Standardliste mit kleinen Ladensymbolen. Wird es abgehakt, verschwindet es überall. Hinweis: Das Sortiment eines Ladens ist nicht abfragbar (keine erlaubte Quelle), die Ladenwahl kommt allein vom Benutzer.
- Entschieden: Zweite Liste «Weitere» (Kleider, Geschenke, Baumarkt), per Umschalter oben auf der Einkaufsliste, unauffällig. Keine Ladenpflicht, optional ein Laden von Hand. Ladenerkennung und Läden-Sortierung gelten nur für Lebensmittel.
- Entschieden: Dinge ohne Eile (zum Beispiel aus dem Baumarkt) sollen nicht vergessen gehen, aber auch nicht ständig im Einkauf stehen. Sie werden erst wichtig, wenn man in der Nähe eines passenden Geschäfts ist.
- Entschieden: Auslöser ist der Ladentyp (zum Beispiel Baumarkt), nicht eine bestimmte Kette. Ohne Auslöser liegen die Produkte ruhig unter «Weitere», mit kleiner Zahl neben dem Umschalter. In der Nähe erscheint oben eine Zeile («Baumarkt in der Nähe: 2 Dinge zu besorgen»), per Tipp wegschickbar, dann kommt sie an diesem Ort nicht mehr. Vibration nur, wenn eingeschaltet. Radius und Ein/Aus wie bei der Filialerkennung.
- Entschieden: Feste Ladentypen zum Anfang: Baumarkt, Kleider und Schuhe, Elektronik, Apotheke und Drogerie, Papeterie und Bücher, Möbel und Haushalt, Garten und Pflanzen. Dazu eigene Typen mit Stichwort. Jeder Typ ist einzeln ein- und ausschaltbar. Erkennung über OpenStreetMap (Internet nötig).
- Entschieden: Der 🏪-Knopf neben der Menge zeigt oben die Lebensmittelketten und darunter die Ladentypen. Ein gewählter Ladentyp legt das Produkt unter «Weitere» ab. Die App schlägt den Typ bei bekannten Wörtern selbst vor (Schrauben → Baumarkt, Pullover → Kleider), man bestätigt oder ändert mit einem Tipp, und sie lernt aus Korrekturen wie bei den Kategorien. Ohne Wahl bleibt ein Produkt im Standard.

### Notiz vom 18.11.2026 (abends): Aktionen allgemein oder genau (nur festgehalten, für die nächste Version)

- Gibt man ein allgemeines Produkt ein (zum Beispiel «Mayo»), zeigt die 🔥-Suche Aktionen über alle passenden Produkte dieser Art (alle Mayonnaisen).
- Gibt man ein genaues Produkt ein (zum Beispiel «Thomy Mayonnaise»), wird nur angezeigt, wenn genau dieses Produkt in Aktion ist.
- Umgesetzt ist bereits die Wortregel: Ein Produkt passt zu einer Aktion, wenn alle Wörter des einen im anderen vorkommen («Mayonnaise» passt zu «Thomy Mayonnaise», «Thomy Mayonnaise» nicht zu «Mayonnaise Hela»).
- Offen für die nächste Version: Kurzformen und Mundart wie «Mayo» = «Mayonnaise» müssen als gleiche Wortart erkannt werden (Wortliste oder Alias).

### Arbeitsregel (seit 18.11.2026, 22:10)

- Neue Wünsche und Ideen werden standardmässig nur festgehalten, nicht gebaut.
- Gebaut wird erst, wenn Rico es ausdrücklich schreibt (zum Beispiel «umsetzen» oder «bauen»).

### Notiz vom 18.11.2026 (22:20): Produkte unter dem Laden ablegen (nur festgehalten)

- Wer ein Produkt an einem bestimmten Ort kauft, will es nicht in der allgemeinen Liste sehen.
- Es soll einen Menüpunkt geben, in dem diese Produkte unter dem jeweiligen Laden abgelegt sind.
- Das verändert den früheren Entscheid, dass ein Produkt mit Ladenwahl in der Standardliste mit Ladensymbolen erscheint. Entschieden (ja): Der neue Wunsch ersetzt den alten. Ein Produkt mit Ladenwahl (Kette) erscheint nicht mehr in der Hauptliste. Neuer Menüpunkt «Läden» (unter «Mehr»): Dort stehen die Läden und unter jedem Laden seine Produkte. In der Nähe eines Ladens erscheinen dessen Produkte oben in der Hauptliste und verschwinden beim Verlassen wieder. Produkte ohne Ladenwahl bleiben in der Hauptliste. Ladentypen wie Baumarkt bleiben unter «Weitere».

### Notiz vom 18.11.2026 (22:23): Eigene Läden mit Auswahlkästchen (nur festgehalten)

- In den Einstellungen unter «Filialen» haben die Ketten ein Kästchen mit Haken zum Ein- und Ausschalten, die eigenen Läden nicht. Das sieht uneinheitlich aus.
- Auch eigene Läden sollen ein Kästchen mit Haken bekommen, damit man sie für die Erkennung und die Anzeige ein- und ausschalten kann. Das Löschen (✕) bleibt daneben.

### Notiz vom 18.11.2026 (22:26): Lebensmittel-Läden in der Auswahl erweiterbar (nur festgehalten)

- In der Auswahl «Wo kaufst du das?» ist die Liste der Lebensmittel-Läden fest (Migros, Coop, Lidl, Aldi, Denner, Spar, Volg).
- Sie soll wie bei den Ladentypen erweiterbar sein: eigene Lebensmittel-Läden hinzufügen, auch ausblenden und löschen. Die eigenen Läden aus den Einstellungen sollen dort ebenfalls erscheinen.

### Titel und Design der App (notiert 20.11., noch nicht gebaut)

- Titel: **sEBU** mit kleinem «s»
- Untertitel: **smarter Einkaufs-Manager** mit kleinem «s»
- Schrift: Baloo 2, kursiv
- Hauptgrün: #25D366 (WhatsApp-Grün)
- Dazu passende dunkle Farbe (Dark-Modus) – Vorschlag folgt beim Bauen
- Hinweis: Das Schriftbild erfordert Google Fonts (Internet) oder eine eingebettete Schrift; Offline-Fallback nötig.
**Entscheid 20.11.:** Titelschrift = Baloo 2 kursiv (Alternative: Fredoka). Grüntöne werden noch verglichen.

**Entscheid 20.11.:** Farbe = Neon-Grün (#39FF14) mit Umrandung in dunklerem Grün (Vorschlag #0a5c00). Ersetzt WhatsApp-Grün #25D366. Noch nicht gebaut.

**Slogan (notiert 20.11., noch nicht gebaut):** «sEBU, der smarte Einkaufsberater. Alles kann, nichts muss.» – Ort in der App noch offen (Begrüssung/Start, Info-Seite, Einstellungen).


### Notizen 20.11. vormittags (noch nicht gebaut)

- **Menü:** «Läden» nicht unter «Mehr», sondern eine Stufe höher, gleich wie Favoriten (Hauptmenü).
- **Einstellung Aktionen:** drei Stufen – <italic>automatisch</italic>, <italic>manuell</italic>, <italic>aus</italic>. Bei <italic>aus</italic> verschwindet der Aktionsbutton (🔥) bei den Produkten.
- Vorschlag zur Bedeutung (noch bestätigen): automatisch = neue Produkte werden automatisch beobachtet; manuell = wie heute, du tippst auf 🔥; aus = kein 🔥-Button, keine Aktions-Hinweise.
**Bestätigt 20.11.:** Aktionen automatisch = neue Produkte automatisch beobachtet; manuell = wie heute (🔥 antippen); aus = kein 🔥-Button, keine Aktions-Hinweise.


### Führungen ausbauen (notiert 20.11., noch nicht gebaut)

- **Führung durch die Einstellungen:** soll alles enthalten, jede Einstellung, damit man direkt alles einstellen kann, wenn man möchte (nicht nur die Bereiche ansehen).
- **Führung durch die App:** gleich vollständig, alle Funktionen (inkl. neue: Läden-Ansicht, Aktionen automatisch/manuell/aus, Liste teilen, Ladentypen).
- **Texte:** pro Schritt knapp erklaren. Wer mehr wissen möchte, tippt auf «Mehr» für die genauere Erklärung.
**Entscheid Führungen 20.11.:** Während eines Schritts ist nur das markierte Bedienelement (z. B. Regler/Schalter), «Weiter» und «Abbruch» antippbar. Daneben tippen löst einen lustigen Spruch aus (wie bisher). Man kann also direkt einstellen, die Führung wartet auf «Weiter».

**Ergänzung Führung 20.11.:** Auch die Ansicht und das Menü werden erklärt (jeder Menüpunkt: Einkaufsliste, Favoriten, Läden, Aktionen, Ideen, Einstellungen, Mehr mit Ratgeber, Anlässe, Stammartikel, Premium-KI, Test). Ziel: man soll wissen, was die App kann. Gleiche Regeln: knapp, «Mehr» für Details, nur markiertes Element antippbar.

**Sprüche bei Fehlklick 20.11.:** Die Sprüche wiederholen sich nicht (grössere Auswahl, zufällig, ohne direkte Wiederholung). Ab dem 2. Fehlklick darf der Spruch etwas frech werden.

**Korrektur 20.11.:** Untertitel = «smarter Einkaufsberater» (nicht Manager). Umgesetzt.

**Umgesetzt 20.11. (abends):** Läden im Hauptmenü; Aktionen automatisch/manuell/aus; Untertitel Einkaufsberater; Führung durch die App (39 Schritte, inkl. Menü und Ansicht) und durch die Einstellungen (38 Schritte, jede Einstellung), mit «Mehr» pro Schritt; nur markiertes Feld, Weiter, Pause, Beenden antippbar; wechselnde Sprüche, ab 2. Fehlklick frech; Slogan «Alles kann, nichts muss.» in der Begrüssung.

**Notiz 21.11. (noch nicht gebaut):** In den Einstellungen soll man mit einem Klick zurück auf die Einkaufsliste kommen (aus jeder Unterseite der Einstellungen). Vorschlag: ein Knopf «← Liste» oben in den Einstellungen, dazu bleibt «← Zurück» eine Ebene.

**Hinweis Adresse:** Das Repo heißt smartshop-schweiz; die App-Adresse ist vermutlich https://schubiger-rico.github.io/smartshop-schweiz/ (nicht /SEBU/). Auf GitHub liegt noch das alte icon-180.png; ersetzen ausstehend.

**Notiz 21.11. (noch nicht gebaut, Deutung zu bestätigen):** Bei der Einstellung Aktionen kommt eine weitere Stufe «immer» dazu. Die Aktions-Anzeige (🔥) soll sonst nur erscheinen, wenn tatsächlich eine Aktion für das Produkt vorhanden ist. Vorschlag: aus / nur bei Aktion (Anzeige nur wenn eine Aktion da ist) / manuell / automatisch / immer (🔥 immer sichtbar).

**Präzisiert 21.11.:** Einstellung Aktionen bekommt die Stufe «immer». Nur wenn «immer» aktiv ist, erscheint die Aktions-Anzeige in der Liste bei einem Produkt genau dann, wenn für dieses Produkt eine Aktion vorhanden ist, sonst bleibt sie unsichtbar (ersetzt die vorherige Deutung mit dauernd sichtbarem 🔥). Stufen: automatisch, manuell, immer, aus. Noch nicht gebaut.

**Umgesetzt 21.11.:** Knopf «← Liste» in den Einstellungen (Hauptseite und alle Unterseiten); Aktionen-Stufe «Immer» (alle Produkte beobachtet, 🔥 nur sichtbar, wenn eine Aktion vorhanden ist).

**Notiz 21.11. (noch nicht gebaut):** Wenn ich in einem Laden bin (z. B. Migros, Einkauf gestartet), soll die App keinen anderen Laden vorschlagen, erst wenn der Einkauf beendet ist. Vorschlag: Solange ein Einkauf läuft (Stopp-Knopf sichtbar), keine Laden-Vorschläge und kein Wechselhinweis; nach «Einkauf beenden» wieder normal. Auch bei 🔄 und beim Zurückkehren in die App.


### Offenes nicht vergessen (Vorschlag gespeichert 21.11., noch nicht gebaut)

Ausgangslage: Nach dem Einkauf noch etwas aus einem anderen Laden holen (z. B. Eier im Hofladen) und es im Auto nicht vergessen. Kein CarPlay. Der Hofladen liegt geradeaus, nicht auf dem Heimweg abbiegen. Eine Web-App kann auf dem iPhone nicht im Hintergrund erinnern (kein Push ohne Server).

- **Hinweis beim Einkaufsende:** Beim Tippen auf «Einkauf beenden» erscheint, wenn noch Produkte für andere Läden offen sind, eine ruhige Zeile: «Noch offen: Eier (Hofladen)». Knopf «Heute noch merken» (Produkt bis Tagesende oben in der Liste mit Laden-Hinweis) oder «Später» (bleibt unter Läden). Kein Alarm, kein Ton.
- **Erinnerung beim Wegfahren:** Knopf «Erinnerung beim Wegfahren» öffnet das Teilen-Menü des iPhones mit dem Text «Eier beim Hofladen holen, geradeaus fahren» (Erinnerungen-App; dort Ort = aktueller Laden, «Beim Verlassen»). Weg-Zusatz («geradeaus») einmal beim Hofladen-Eintrag erfassen. Alternative: Siri per Sprache. Hinweis in der App, dass Ortungsdienste für Erinnerungen an sein müssen.
- **Navigationsknopf 🧭:** In der Ansicht «Läden» bei jedem Laden mit gespeichertem Standort und im Hinweis am Einkaufsende. Öffnet Google Maps (Kartenlink mit Ziel-Koordinaten), sonst Browser. Ohne Standort: Suche nach dem Namen in der Nähe (ungenau).
- **Beim App-Öffnen:** ruhige Zeile «Noch offen: …», solange etwas offen ist.
- **Ohne Einkaufsende** keine Hinweise (App darf im Hintergrund keine Position prüfen).
- **Standort speichern:** Einstellungen → Filialen → Eigene Läden → Name eingeben → «Hier speichern» (am Ort selbst). Funktioniert bereits.
**Notiz 21.11. (noch nicht gebaut):** In der Einstellungen-Führung (Schritt Radius der Filialerkennung) gute Erklärung, welche Distanz wofür geeignet ist. Textvorschlag: 25 m = einzelner Laden, genau (Dorfladen, Hofladen, enge Gassen); 50 m = Standard (Einkaufsstrasse, Parkplatz vor dem Laden); 100 m = grössere Zentren mit Parkplatz oder Einkaufszentrum; 250 m = nur wenn der GPS-Empfang schlecht ist, höhere Verwechslungsgefahr mit Läden nebenan. Kleiner Radius = genauer, aber der Laden wird bei schlechtem Empfang eher nicht erkannt. Grosser Radius = findet sicher, aber evtl. falscher Laden. Mit «Mehr» ausführlich.


### Automatischer Erkennungsradius (festgehalten 21.11., noch nicht gebaut)

Idee: Die App wählt den Radius selbst, je nach Laden (Dorfmetzger vs. Migros). Ersetzt die feste Radius-Erklärung in der Führung; die frühere Tabelle 25/50/100/250 m bleibt als manuelle Wahl.

- **Grösse aus den Kartendaten:** Wenn ein Gebäudegrundriss vorhanden ist, Radius daraus ableiten (kleines Haus klein, Supermarkt mit Parkplatz grösser). Fehlt er, Standardwert nach Ladentyp (Metzgerei/Hofladen klein, Supermarkt mittel, Zentrum gross).
- **GPS-Genauigkeit:** Das iPhone meldet die Genauigkeit jeder Ortung. Bei schlechtem Empfang Toleranz nur so weit vergrössern wie nötig, bei gutem Empfang streng bleiben.
- **Nächster Laden gewinnt:** Bei zwei Treffern entscheidet der kleinere Abstand; bei Kopf-an-Kopf nachfragen statt raten.
- **Standard eher grösser:** 50 m. Kleine Läden und eigene Läden (Hofladen, Metzger) automatisch 25 m, grössere (Supermarkt, Zentrum) bis 80 m. Begründung: Nicht erkannt ist ärgerlicher als falsch erkannt, GPS springt 20 bis 40 m, Supermarkt mit Parkplatz ist 50 bis 80 m breit; ab etwa 100 m erscheinen Läden nebenan.
- **Eigene Läden:** Radius pro Laden einstellbar, Vorgabe klein.
- **Einstellung:** Radius in den Einstellungen «Automatisch (empfohlen)», alternativ 25/50/100/250 m.
- **Einstellungen-Führung:** Text «Automatisch: kleine Läden genau, grosse grosszügig», mit «Mehr» die Tabelle der Distanzen und Faustregel (kleiner Radius genauer, erkennt aber bei schlechtem Empfang eher nicht; grosser Radius findet sicher, kann aber den falschen Laden wählen).
- Ehrlicher Hinweis: Nicht jeder Laden hat einen Grundriss in den Kartendaten, dann gilt ein Näherungswert.
**Grundsatz Wegleitung/Führung 21.11.:** Die Führung erklärt bei Einstellungen mit Wirkung (z. B. Radius, Filialerkennung, Aktionen, Lernen) die Unterschiede und wofür welche Stufe geeignet ist, damit niemand denkt, die App sei schlecht, wenn sie nur anders eingestellt werden muss. Je Einstellung: kurz «Wofür geeignet» und «Wenn es nicht klappt, probiere…» (Tipp zur Fehlersuche), Details unter «Mehr». Gilt für die Einstellungen-Führung und bei Bedarf für die App-Führung. Noch nicht gebaut.


### Umgesetzt am 21.11.

- Keine Laden-Vorschläge während eines laufenden Einkaufs (🔄 manuell geht weiter).
- «Noch offen» am Einkaufsende: Heute noch merken / Später, 🔔 Erinnerung beim Wegfahren (mit Weg-Hinweis je eigenem Laden), 🧭 Navigation (Google Maps) auch in Läden, ruhige «Heute noch»-Zeile beim Öffnen.
- Erkennungsradius «Automatisch (empfohlen)» nach Ladengrösse und GPS-Genauigkeit; eigene Läden mit eigenem Radius (25/50/100); Einstellung 25/50/100/250 m.
- Tour: «Wofür geeignet» und «Wenn es nicht klappt» bei Radius, Filialerkennung, Aktionen, Smart-Lernen; Radius-Erklärung unter «Mehr».
- ~~Nicht gebaut: Kopf-an-Kopf-Nachfrage bei zwei Läden.~~ → umgesetzt am 21.11. abends, siehe unten.
### Umgesetzt am 21.11. (abends): «Welcher Laden?»

- Liegen zwei Läden weniger als 15 m auseinander (beide im Radius), fragt die App «Welcher Laden? Zwei sind fast gleich nah.» mit beiden Namen und Abstand sowie «Keiner».
- Die Wahl wird für genau dieses Läden-Paar gemerkt (`S.learn.pick`); beim nächsten Mal wählt die App ohne Nachfrage. «Gelerntes löschen» setzt das zurück.
- «Keiner» lehnt beide bis zum nächsten 🔄 ab. Ist man schon in einem der beiden Läden, wird nicht gefragt. Gilt auch bei Filialerkennung «Automatisch».
- Test: `tests/t10.py`.

### Notiz vom 21.11.2026 (abends): Führungen verbessern (nur festgehalten, noch nicht gebaut)

- **Einstellungen-Führung, Schritt 24:** Das Erklärfeld verdeckt den Button (bestätigt) – Erklärfeld unter den Button setzen, damit er frei bleibt.
- **Knopf «Mehr»** auffälliger gestalten.
- **Text unter «Mehr» strukturierter:** z. B. bei 25 / 50 / 100 / 250 m je einen eigenen Absatz, damit es übersichtlicher wird.
- **App-Führung:** Zuerst die Eingabeseite genau erklären, Schritt für Schritt. Erst danach den Rest.

### Umgesetzt am 21.11. (abends): Führungen verbessert

- Das Erklärfeld steht jetzt **unter** dem leuchtenden Feld (passt es nicht, darüber). Die Knöpfe bleiben auch bei langem Text sichtbar.
- Knopf «ℹ️ Mehr ▾» ist auffälliger (Rahmen in Akzentfarbe, fett).
- Text unter «Mehr» in Absätzen (`\n` im Text = neuer Absatz): Radius (25/50/100/250 m je eigene Zeile, «Welcher Laden?» erwähnt), Aktionen-Modi, Filialerkennung.
- App-Führung beginnt mit **«Eingabeseite»** Schritt für Schritt (Feld, Kategorie, Menge, 🏪, ＋ ausprobieren, Produktzeile, 🔥, ☆, 🛒, 🔄, 📷, ✓, Letzte Produkte), danach der Rest. App-Führung hat jetzt 47 Schritte.

### Notiz vom 21.11.2026 (abends): Einführung beim ersten Start empfehlen (nur festgehalten, noch nicht gebaut)

- Beim ersten Öffnen, nach der Namenseingabe (bei der Frage «Möchtest du eine Führung durch die App?»), einen freundlichen bis witzigen Satz ergänzen: Die Führung ist sehr sinnvoll, damit man die App richtig nutzen kann.
- Wichtig: Es soll auch klar werden, dass man ohne Führung leicht denkt, die App sei nicht gut – dabei ist oft nur eine Einstellung anders nötig.
- Vorschlag (3. Fassung, mit Slogan am Anfang): «Alles kann, nichts muss. Aber: Kurz und schmerzlos: In ein paar Minuten zeige ich dir alle Tricks. Ehrlich gesagt: Ohne Führung verpasst man vieles und denkt schnell, die App kann nichts. Dabei steckt sie voller Ideen, die du erst findest, wenn du weisst, wo sie sind. Danach kaufst du ein wie ein Profi – versprochen, ganz ohne Prüfung am Schluss. 😉»
- Slogan «Alles kann, nichts muss.» als eigene, fette Zeile oben, **gleiche Farbe wie der Titel** (Neon-Grün mit dunkelgrünem Rand).

### Notiz vom 21.11.2026 (abends): Titel anpassen (nur festgehalten, noch nicht gebaut)

- Untertitel mit grossem B: «smarter EinkaufsBerater» (vermutet, Bestätigung offen).
- Grössenverhältnis: «sEBU» bleibt gleich gross, der Untertitel wird ein wenig grösser.

### Umgesetzt am 21.11. (abends): Einführungstext und Titel

- Begrüssung, Seite «Möchtest du eine Führung durch die App?»: Slogan «Alles kann, nichts muss.» als eigene Zeile in Titelfarbe, danach der Empfehlungstext (3. Fassung, «Aber kurz und schmerzlos: …»).
- Untertitel überall «smarter EinkaufsBerater» (auch Seitentitel und manifest), Untertitel etwas grösser (.95em statt .85em), «sEBU» unverändert.

### Notiz vom 21.11.2026 (abends): Favoriten ausschaltbar (nur festgehalten, noch nicht gebaut)

- Für alle, die es möglichst unkompliziert wollen: Favoriten in der Liste ausschaltbar. Wenn aus, erscheint kein ☆-Symbol bei den Produkten.
- Vorschlag: Schalter in Einstellungen → «Favoriten und Letzte Produkte». Entschieden: Wenn aus, verschwindet auch der Menüpunkt «Favoriten» (wie bei Aktionen «aus»).
- Weitere Symbole, auf die man verzichten könnte (Liste für Rico, noch nichts entschieden): 🏪 Laden bei der Eingabe, 📷 Ratgeber, 🛒 Einkauf starten / 📍 Laden wählen / 🔄, «Letzte Produkte» unter der Liste. Bereits abschaltbar: 🔥 (Aktionen «aus»), Kategorien-Zeile.
- Idee: ein Schalter «Einfache Ansicht», der alle diese Symbole auf einmal ausblendet (einzeln wieder einschaltbar).
- **Ergänzung (21.11. abends):** Statt einem einzelnen Schalter eine **Abfrage mit drei Stufen**: «Einfach» (nur das Nötigste), «Umfänglich» (alles sichtbar), «Manuell» (selbst einzeln wählen). Danach ist jedes Symbol/Element einzeln ein- und ausschaltbar.
- In den Einstellungen eine **eigene Sparte «Einkaufsliste»** dafür.
- **Änderungen sind live sichtbar** (Vorschau der Liste direkt beim Umschalten).
- Entschieden: Die Abfrage kommt auch bei der Begrüssung beim ersten Start, gleich nach der Schriftgrösse (mit Live-Vorschau der Liste).

### Umgesetzt am 21.11. (abends): Ansicht Einfach / Umfänglich / Manuell

- Neue Einstellungen-Sparte «🧾 Einkaufsliste» und neue Begrüssungs-Seite «Wie viel möchtest du sehen?» (nach der Schriftgrösse).
- Einfach: nur Eingabefeld, Kategorie-Symbol, Menge, ＋ und ✓. Umfänglich: alles. Manuell: selbst wählen; jede einzelne Änderung schaltet auf «Manuell».
- Einzeln schaltbar: Kategorie-Symbol, Favoriten (☆ und Menüpunkt), Aktionen 🔥, 🏪 bei der Eingabe, 🛒/📍/🔄, 📷, Letzte Produkte, Kategorien-Zeile.
- Live-Vorschau direkt unter der Auswahl. Bestehende Nutzer: Umfänglich (keine Änderung).
- Führungen überspringen Schritte zu ausgeblendeten Elementen.

### Notiz vom 21.11.2026 (abends): Erinnerung ein-/ausschaltbar (nur festgehalten, noch nicht gebaut)

- Der Knopf «🔔 Erinnerung beim Wegfahren» soll ein- und ausschaltbar sein (entschieden: in der Sparte «Einkaufsliste» als weiterer Schalter, bei «Einfach» aus; 🧭 Navigation bekommt ebenfalls einen eigenen Schalter, bei «Einfach» aus).
- Rico fragte, ob er Google Maps selbst anwählen muss: Nein, 🧭 öffnet Google Maps direkt (App, falls installiert, sonst Safari). Bei 🔔 öffnet sich das Teilen-Menü, dort wählt man «Erinnerungen».
- **Problem (21.11. abends):** Nach «Einkauf beenden» → 🔔 musste Rico im Teilen-Menü «Erinnerungen» suchen. Eine Web-App darf nicht direkt in Erinnerungen schreiben.
- Lösungsideen: (a) einmalig einen iPhone-Kurzbefehl «sEBU Erinnerung» einrichten; die App ruft ihn direkt auf (`shortcuts://run-shortcut?name=…&input=text`), er legt die Erinnerung ohne Teilen-Menü an. (b) Hinweis «Erinnerungen» im Teilen-Menü als Favorit nach vorne schieben (Teilen-Menü → «Bearbeiten»). Entschieden: (a) als abschaltbare Option in den Einstellungen mit Schritt-für-Schritt-Anleitung vorsehen; (b) als Tipp in der Anleitung.

### Umgesetzt am 21.11. (abends): Schalter für 🔔/🧭 und Kurzbefehl

- In «Einkaufsliste» neue Schalter «🧭 Navigation» und «🔔 Erinnerung beim Wegfahren» (bei «Einfach» aus).
- Abschnitt «🔔 Erinnerung»: Option «Über Kurzbefehl, ohne Teilen-Menü», Name des Kurzbefehls (Standard «sEBU Erinnerung»), Anleitung zum Aufklappen, Tipp für das Teilen-Menü, «Wenn es nicht klappt».
- Fehler behoben: Zwei Funktionen hiessen `navBtn`, dadurch war der 🧭-Knopf bei «Noch offen» und unter «Läden» kaputt. Der Google-Maps-Knopf heisst jetzt `mapBtn`.
- Nicht geprüft: echter Kurzbefehl auf dem iPhone (Ort «Beim Verlassen» je nach iOS-Version).

### Idee für später (21.11.2026): Richtige App im App Store (nur festgehalten, erst wenn die Web-App fertig ist)

- Kosten: Apple-Entwicklerkonto CHF 99 pro Jahr (immer, auch für TestFlight), Google Play einmalig ca. USD 25. Bauen braucht einen Mac (Xcode) oder einen Cloud-Dienst (z. B. Codemagic).
- Weg: bestehende `index.html` mit Capacitor verpacken. Apple verlangt echte iPhone-Funktionen (sonst Ablehnung als «nur Webseite»), z. B. echte Erinnerung beim Wegfahren (Geofence), Mitteilungen, Ladenerkennung im Hintergrund.

### Ricos Vision (festgehalten 21.11.2026)

1. Produkte im Smartphone eingeben.
2. Aktionen sehen, auch **wo** es welche gibt (welcher Laden).
3. Beim Ladeneingang erkennt die App den Laden und zeigt die Reihenfolge für den **kürzesten Weg** durch den Laden.
4. Idealerweise die Liste **direkt ins Scannergerät des Ladens übermitteln** (z. B. Migros Subito, Coop Passabene), damit man nur ein Gerät braucht.
5. Produktinfos abrufen und Produkte vergleichen.

Stand heute: 1 gebaut; 2 teilweise (Aktionen, aber ohne echte Datenquelle); 3 teilweise (Ladenerkennung, gelernte Reihenfolge statt Ladenplan); 4 nicht möglich ohne Zusammenarbeit mit den Händlern (keine offenen Schnittstellen); 5 teilweise (KI-Ratgeber).

### Notiz vom 21.11.2026 (abends): Hinweis «Test» (nur festgehalten, noch nicht gebaut)

- Irgendwo soll sichtbar sein, dass sEBU eine Testversion ist (z. B. für Migros/Coop, die den Link bekommen).
- Vorschlag: kleines Schild «TEST» neben dem Titel oben (dezent, z. B. gelb), Antippen zeigt «Testversion – noch in Entwicklung. Rückmeldungen willkommen.» Zusätzlich in der Begrüssung ein Satz. Abschaltbar in den Einstellungen (Abo/Test), damit es später einfach verschwindet.
- **Ergänzung:** Überall im Menü, wo noch nicht fertig gebaut ist, erscheint beim Antippen oben gross «🚧 TEST: Ist noch in Arbeit» mit einem witzigen Spruch (zufällig wechselnd). Kandidaten (nur teilweise gebaut): Aktionen (Beispieldaten), Ideen, Anlässe, Stammartikel, Premium-KI, Abo, Sprache. Spruch-Vorschläge: «Hier wird noch geschraubt – die Einkaufswagen stehen schon Schlange.» / «Diese Abteilung ist noch im Umbau. Bitte nicht über die Kartonschachteln stolpern.» / «Unser Entwickler und die KI sind dran. Die Milch ist schon kalt gestellt.» / «Gut Ding will Weile haben – wie ein richtiger Zopfteig.» / «Noch in Arbeit. Aktion: 100 % Geduld, 0 % Aufpreis.»
- **Aktionen speziell:** Statt dem allgemeinen Test-Schild steht dort «Hier könnten Ihre Aktionen stehen!» (an Migros/Coop gerichtet) plus ein frecher Spruch. Vorschläge: «Liebe Detailhändler: Der Platz ist reserviert, das Licht ist an, nur Ihre Angebote fehlen noch.» / «Hier könnte Ihre Aktion stehen. Die Kundschaft wartet schon mit gezücktem Einkaufswagen.» / «Bis dahin: Beispieldaten. Echt wie Plastikgemüse im Schaufenster.»
- **Aktionen-Sprüche entschieden (abwechselnd, zufällig):** 1) «Hier könnten Ihre Aktionen stehen. Wir hätten sogar schon den Rotstift gespitzt.» 2) «Dieser Platz ist frei – wie ein Parkplatz am Samstag um 10 Uhr: selten und sehr begehrt.» 3) «Hier könnten Ihre Aktionen stehen. Unsere Nutzer haben die Taschen schon gepackt – leider noch leer.» 4) «Hier könnten Ihre Aktionen stehen. Sonst kaufen die Leute am Ende noch zum vollen Preis. Undenkbar!» 5) «Hier könnten Ihre Aktionen stehen. Und zwar dann, wenn die Kundschaft gerade vor dem Regal steht. Smart, oder?» (Ersetzt die früheren Aktionen-Vorschläge.)

### Umgesetzt am 21.11. (abends): Test-Hinweise

- Gelbes Schild «🚧 TEST: Ist noch in Arbeit» mit wechselndem Spruch in Ideen, Anlässe, Stammartikel, Premium-KI, Abo und Sprache.
- Bei Aktionen «🚧 Hier könnten Ihre Aktionen stehen!» mit den fünf gewählten Sprüchen.
- Abschaltbar unter Darstellung → «Test-Hinweise anzeigen». Das kleine «TEST»-Schild neben dem Titel ist nicht gebaut (durch die Menü-Hinweise ersetzt).

### Durchsicht 21.11.2026 (abends): Auffälligkeiten (nur festgehalten)

- **Fehler:** Einstellungen → Einführung → Bereich «Filialen» startet die ganze Einstellungen-Führung statt nur «Filialen» (alter Sonderfall `w==='6'` in `tourSteps`).
- **Führung:** Der dunkle Hintergrund deckt bei kurzen Seiten den unteren Bildschirmteil nicht ab (grauer Streifen unten).
- **Symbol im manifest.json:** noch das alte hellgrüne «SEBU»-Bild und alte Themenfarbe; passt nicht zum neuen neon-grünen Symbol (betrifft v. a. Android).
- **Rezept Risotto:** Zutat heisst «Risotto», besser «Risottoreis».
- CLAUDE.md-Slogan noch alt («sEBU der smarte Einkaufsberater»).
- **Behoben am 21.11. (abends):** alle vier Punkte oben – Bereich «Filialen» startet nur noch seine Schritte; dunkler Hintergrund der Führung deckt den ganzen Bildschirm (`html.touring`); manifest nutzt `icon-180.png`, Name «sEBU smarter EinkaufsBerater»; Rezept «Risottoreis». CLAUDE.md-Slogan aktualisiert.

### Notiz vom 21.11.2026 (abends): Rückgängig nach dem Löschen (nur festgehalten, noch nicht gebaut)

- Nach dem Wegwischen (Löschen) eines Produkts erscheint kurz «↩ Rückgängig», ein Tipp holt es zurück (an gleicher Stelle, mit Menge, Laden, Kategorie).
- Weitere Ideen (nicht gewählt, nur notiert): Liste als Text teilen (WhatsApp/SMS), Erinnerung an Sicherung, Produktinfos per Strichcode (Open Food Facts).
- Rückgängig: 4 Sekunden sichtbar (entschieden).

### Notiz vom 21.11.2026 (abends): Sicherung automatisch (nur festgehalten, noch nicht gebaut)

- Rico wünscht automatische Sicherung. Grenze: Eine Web-App darf nicht unbemerkt Dateien speichern (auch nicht in iCloud).
- Möglich: (a) automatische Sicherung in der eigenen Datenbank (Firebase, wie beim Teilen) mit Wiederherstellen-Code – schützt auch beim Handywechsel; (b) zusätzlich automatische Zwischenkopien auf dem Gerät (schützt vor Fehlern, nicht vor Handyverlust). Entschieden: (a) + (b), beides abschaltbar, mit Datenschutz-Hinweis.

### Notiz vom 21.11.2026 (abends): Produktinfos per Strichcode (nur festgehalten, noch nicht gebaut)

- Rico will Idee 4: Produktinfos aus Open Food Facts (frei, gratis, ohne Händler). Strichcode mit der Kamera scannen (oder Nummer eingeben) → Name, Marke, Menge, Nährwerte/Nutri-Score, Zutaten; Produkt mit einem Tipp auf die Liste. Später vergleichen.
- Hinweis: Nicht jedes Schweizer Produkt ist in der Datenbank; dann «nicht gefunden» und von Hand weiter. Abschaltbar wie alles.
- Entschieden: Scan-Knopf über 📷 beim Eingabefeld mit Wahl «Strichcode» oder «Ratgeber». Ein- und ausschaltbar (Sparte «Einkaufsliste», bei «Einfach» aus) und in Führung/Einstellungen erklärt (Wofür geeignet / Wenn es nicht klappt: Licht, Abstand, Nummer von Hand eingeben).

### Umgesetzt am 21.11. (abends): Rückgängig, automatische Sicherung, Strichcode

- «↩ Rückgängig» nach dem Löschen (Wischen oder «Löschen»), 4 Sekunden, Produkt kommt an die gleiche Stelle zurück.
- Daten und Datenschutz → «Automatische Sicherung»: Zwischenkopien auf dem Gerät (täglich, letzte 5, wiederherstellbar) und Sicherung in der eigenen Firebase-Datenbank (täglich, Wiederherstellen-Code, ohne KI-Schlüssel), «Sicherung mit Code holen». Beides abschaltbar, mit Datenschutz-Hinweis und «Wenn es nicht klappt». Firebase-Regeln in der Einrichtung um «backups» ergänzt. «Alle Daten löschen» löscht auch die Zwischenkopien.
- 🔎 Strichcode scannen (Sparte «Einkaufsliste», bei «Einfach» aus): 📷 → «Strichcode scannen» oder «Ratgeber fragen». Kamera, Foto oder Nummer von Hand; zeigt Name, Marke, Menge, Nutri-Score, Zutaten aus Open Food Facts; «＋ Auf die Liste». In Führungen erklärt.
- Nicht echt geprüft: Kamera-Scan auf dem iPhone (Safari hat keinen eingebauten Strichcode-Leser, darum wird ein Scanner aus dem Internet nachgeladen), echte Firebase-Sicherung.
- **Behoben am 22.11.:** Firebase-Sicherung schlug bei Rico fehl (Regeln kannten «backups» nicht). Sicherung liegt jetzt unter `lists/bak-<Code>`, die bestehenden Teilen-Regeln reichen, keine Änderung in Firebase nötig. Fehlermeldung nennt jetzt den Grund (Zugriff verweigert / Adresse falsch / kein Internet). Schalter-Zeilen umbrechen nicht mehr.
- 22.11.: Firebase-Sicherung auf Ricos iPhone mit echter Datenbank erfolgreich getestet. Hinweis: Neue Versionen kommen wegen GitHub-Zwischenspeicher bis zu 10 Minuten verspätet an (Umgesetzt 22.11.: Service Worker fragt bei eigenen Dateien still immer beim Server nach (`cache:"no-cache"`, `updateViaCache:"none"`, Cache `sebu-v2`); offline weiter aus dem Speicher.)

### Notiz vom 22.11.2026: Notfall-Produkt (nur festgehalten, noch nicht gebaut)

- Bei der Eingabe ein Notfall-Knopf (z. B. ❗), damit ein Produkt als «dringend» markiert wird.
- Dringende Produkte stehen **immer an erster Stelle** (vor jeder Sortierung, auch im Laden), fallen auf (rote Umrandung/Hintergrund) und haben **grössere Schrift**.
- Ideen dazu (Vorschlag, noch offen): dringend auch nachträglich per Antippen umschaltbar; dringend erscheint unabhängig vom zugeordneten Laden in jeder Liste; Hinweis beim Einkaufsende, falls Dringendes offen bleibt; ein- und ausschaltbar in der Sparte «Einkaufsliste».

### Umgesetzt am 22.11.: Notfall / dringend

- ❗ bei der Eingabe (vor ＋), im Bearbeiten und als rotes ❗ auf der Karte (Antippen nimmt es weg).
- Dringendes steht immer zuoberst, rot umrandet, grössere fette Schrift, in jedem Laden sichtbar.
- Beim Einkaufsende roter Hinweis «❗ Dringend noch offen: …» mit «Verstanden».
- Schalter in «Einkaufsliste» (bei «Einfach» aus), in App- und Einstellungen-Führung erklärt.

### Arbeitsregel (seit 22.11.2026)

- Alle neuen Funktionen und Einstellungen kommen automatisch in die Wegleitung (Führung durch App bzw. Einstellungen), mit «Wofür geeignet» und «Wenn es nicht klappt». Nachgetragen: «↩ Rückgängig» in der App-Führung (Schritt ✓).

### Notiz vom 22.11.2026: Mehr Symbole (nur festgehalten, noch nicht gebaut)

- Emoji-Auswahl für Kategorien und Produkte erweitern (heute ca. 90 in 5 Gruppen: Essen, Getränke, Haushalt, Tiere, Sonstiges).
- Neu/mehr: Obst & Gemüse, Brot & Backwaren, Fleisch & Fisch, Milchprodukte, Süsses & Snacks, Getränke, Drogerie & Hygiene, Baby, Haushalt & Putzen, Tiere, Baumarkt & Garten, Büro & Schule, Apotheke, Kleider, Freizeit. Mit Suchwörtern (Schweizerdeutsch inkl., z. B. «rüebli», «gipfeli»).
- Ergänzung: Deutlich mehr Gemüse und Früchte (z. B. Paprika, Gurke, Lauch, Zucchetti, Aubergine, Spinat, Salat, Pilze, Zwiebel, Knoblauch, Kürbis, Kiwi, Mango, Ananas, Melone, Kirschen, Pfirsich, Birne, Orange, Kokosnuss …).
- Suchfeld in der Auswahl bleibt (Rico findet es gut).
- **Automatisches Produkt-Symbol:** Steckt ein bekanntes Wort im Produktnamen, erscheint dessen Symbol, auch in zusammengesetzten Wörtern: «Paprikapulver» → 🫑, «Tomatensauce» → 🍅, «Erdbeerjoghurt» → 🍓. Von Hand änderbar, die App merkt sich die Wahl.

### Notiz vom 22.11.2026: Farbe pro Kategorie (nur festgehalten, noch nicht gebaut)

- Jede Kategorie kann eine eigene Farbe bekommen (Einstellungen → Kategorien, Farbpunkt antippen, Auswahl wie bei der Akzentfarbe).
- Vorschlag Anzeige: farbiger Streifen links an der Produktkarte und farbiger Rahmen ums Kategorie-Symbol; Standardfarben für die 14 Hauptkategorien vorgegeben, abschaltbar («Kategorie-Farben anzeigen»).
- Ergänzung: Farben frei selbst wählbar (Farbpalette plus eigener Farbwähler), nicht nur Vorgaben. Anzeige als farbiger Streifen links an der Karte (Vorschlag, noch nicht bestätigt).

### Umgesetzt am 22.11.: Mehr Symbole, automatisches Produkt-Symbol, Kategorie-Farben

- Symbol-Auswahl von ca. 90 auf über 200 Symbole in 16 Gruppen (Früchte, Gemüse, Brot & Backen, Milch & Eier, Fleisch & Fisch, Vorrat, Getränke, Drogerie, Baby, Haushalt, Tiere, Baumarkt & Garten, Büro & Schule, Apotheke, Kleider, Sonstiges), mit Suchwörtern.
- Automatisches Produkt-Symbol aus dem Namen, auch in zusammengesetzten Wörtern (Paprikapulver → 🫑). Eigenes Symbol pro Produkt wählbar, wird gemerkt, «Wieder automatisch» möglich; «Gelerntes löschen» setzt zurück.
- Kategorie-Farben: Standardfarben für die 14 Hauptkategorien, frei wählbar (Farbpunkt unter Kategorien), farbiger Streifen links an der Karte, Schalter «Kategorie-Farben» in «Einkaufsliste» (bei «Einfach» aus). In den Führungen erklärt.

### Notiz vom 23.11.2026: Produktzeilen schmaler (nur festgehalten, noch nicht gebaut)

- Rahmen/Zeile um die Produkte schmaler im Verhältnis zur Schrift (weniger Innenabstand, kleinere Knöpfe ☆ ✓ 🔥), damit mehr Produkte auf den Bildschirm passen.
- Vorschlag: Einstellung «Zeilenhöhe: Kompakt / Normal» unter Darstellung, Standard neu «Kompakt»; «Normal» für alle, die grosse Tippflächen brauchen.

- **Umgesetzt am 23.11.:** Darstellung → «Zeilenhöhe: Kompakt / Normal», Standard Kompakt (Zeile ca. 30 % niedriger, kleinere Knöpfe). In der Einstellungen-Führung erklärt.
- 23.11.: «Kompakt» nochmals enger (Zeile ca. 40 % niedriger als «Normal»), da Rico zu wenig Unterschied sah.

### Notiz vom 23.11.2026: Oberer Bereich aufräumen (nur festgehalten, noch nicht gebaut)

- Produktliste gefällt Rico. Oben wirkt es chaotisch.
- Knöpfe kürzer: «🛒 Start» statt «Einkauf starten», «📍 Laden» statt «Laden wählen».
- Vorschlag: alle vier Knöpfe in **einer** ruhigen Zeile (🛒 Start · 📍 Laden · 🔄 · 📷); darunter das Eingabefeld über die ganze Breite, die kleinen Knöpfe (Kategorie, Menge, 🏪, ❗, ＋) in einer Zeile darunter, wenn der Platz nicht reicht.
- Offen von vorher: Öle (Rapsöl, Olivenöl, Sonnenblumenöl …) als Symbol ergänzen (Rapsöl zeigte 🍅).

### Notiz vom 23.11.2026: Sprachsteuerung (nur festgehalten, noch nicht gebaut)

- Heute schon möglich: Mikrofon 🎤 der iPhone-Tastatur (Diktieren) im Eingabefeld.
- Idee: eigener 🎤-Knopf; man sagt «Milch, Brot und zwei Kilo Äpfel» → mehrere Produkte mit Mengen auf einmal auf der Liste. Safari unterstützt Spracherkennung (webkitSpeechRecognition), in der Homescreen-App nicht immer zuverlässig → Rückfall auf Tastatur-Diktat. Abschaltbar, in Führung erklären.

### Umgesetzt am 23.11.: Kopfzeile aufgeräumt, Sprache, Öle

- Kopfzeile in einer Zeile: «🛒 Start» · «📍 Laden» · 🔄 · 🎤 · 📷. Bei grosser Schrift steht das Eingabefeld allein über die ganze Breite, die kleinen Knöpfe darunter, ＋ rechts.
- 🎤 Sprache: «Milch, Brot und zwei Kilo Äpfel» → Liste zum Bestätigen, dann alle auf einmal hinzufügen (Mengen und Einheiten erkannt). Ohne Spracherkennung Hinweis auf das Tastatur-Mikrofon. Schalter in «Einkaufsliste» (bei «Einfach» aus), in der Führung erklärt.
- Öle (Rapsöl, Olivenöl, Sonnenblumenöl …) bekommen 🫗.
- Nicht echt geprüft: Spracherkennung in Safari/Homescreen-App auf dem iPhone.

### Notiz vom 23.11.2026: ＋ doppelt hoch (nur festgehalten, noch nicht gebaut)

- Wenn das Eingabefeld eine eigene Zeile hat: ＋ rechts in doppelter Höhe, von der Zeile «Produkt hinzufügen» bis zur Knopfzeile darunter (grosser, gut treffbarer Knopf).
- **Umgesetzt am 23.11.:** ＋ doppelt hoch rechts neben Eingabefeld und Knopfzeile (Grid, `--n` = Anzahl kleiner Knöpfe), Kopfzeile wieder sicher einzeilig.

### Notiz vom 23.11.2026: Nur Symbole + Erklärung beim Gedrückthalten (nur festgehalten, noch nicht gebaut)

- Alle kleinen Knöpfe nur mit Symbol (ohne Text).
- 2 Sekunden auf einem Knopf bleiben → kurze Erklärung erscheint, wofür er ist (z. B. «🛒 Einkauf starten: Die App lernt deine Reihenfolge im Laden»). Gilt für alle Symbol-Knöpfe (🛒 📍 🔄 🎤 📷 🏪 ❗ ☆ ✓ 🔥 …). Achtung: 🔥 hat heute schon langes Drücken (Aktionen) – abklären.
- Offen: Ob auch «🛒 Start» und «📍 Laden» nur noch Symbol sein sollen (Vorschlag: ja). In der Führung erwähnen.

### Umgesetzt am 23.11.: Nur Symbole, Erklärung beim Gedrückthalten

- Alle kleinen Knöpfe nur mit Symbol, auch 🛒 und 📍 (Text wieder einschaltbar: Darstellung → «Knöpfe mit Text»).
- 2 Sekunden auf einem Knopf bleiben zeigt, wofür er ist; der Knopf wird dabei nicht ausgelöst. Abschaltbar: Darstellung → «Erklärung beim Gedrückthalten». 🔥 behält sein eigenes langes Drücken (Aktionen).
- In App- und Einstellungen-Führung erklärt.

### Notiz vom 23.11.2026: 🎤 vor das Eingabefeld (nur festgehalten, noch nicht gebaut)

- 🎤 aus der Kopfzeile nehmen und direkt vor «Produkt hinzufügen» setzen (in der Eingabezeile).
- **Umgesetzt am 23.11.:** 🎤 steht jetzt direkt vor «Produkt hinzufügen»; Eingabefeld bekommt schon ab normaler Schrift eine eigene Zeile (Schwelle 24).

### Notiz vom 23.11.2026: Schriftgrösse mit − / Wert / + (nur festgehalten, noch nicht gebaut)

- Beim Schieberegler sieht man die Grösse beim Verschieben nicht (Finger deckt ab).
- Neu: Knopf «−», dazwischen gross die aktuelle Grösse (z. B. «22 px»), Knopf «+». Gilt in der Begrüssung und unter Darstellung; Vorschau-Zeile ändert sich sofort. Regler evtl. zusätzlich behalten.
- **Umgesetzt am 23.11.:** Schriftgrösse nur noch mit «−», Anzeige «xx px», «+» (Begrüssung und Darstellung), Schieberegler entfernt; Führung angepasst.
- 23.11.: «−»/«+» grösser (1,3-fache Knopfhöhe) und grün umrandet wie die Eingabe-Knöpfe.

### Notiz vom 23.11.2026: Spracheingabe verbessern (nur festgehalten, noch nicht gebaut)

- Rico sprach «Brot und 1 Stk und 1 kg stopp» → nur «Brot» kam heraus (Mengen ohne Produkt werden verworfen).
- Verbessern: Menge auch **nach** dem Produkt verstehen («Brot 1 Stück», «Mehl ein Kilo»); Teil nur mit Menge an das vorherige Produkt hängen («Brot und 1 Stück» → Brot 1 Stk.); Füllwörter wie «stopp», «fertig», «bitte», «noch» ignorieren; in der Bestätigung Menge/Produkt antippen und korrigieren können. Hinweis-Beispiel im Sheet zeigen.
- Später evtl.: Befehle («Milch abhaken», «Einkauf starten»).
- **Umgesetzt am 23.11.:** Spracheingabe versteht Mengen vor und nach dem Produkt («Brot 1 Stück», «Mehl ein Kilo»), hängt reine Mengen an das Produkt davor, ignoriert «stopp/fertig/bitte»; in der Bestätigung Name, Menge, Einheit änderbar und Zeilen entfernbar. Test t18.

### Notiz vom 23.11.2026: Kategorie-Auswahl übersichtlicher, mehr Kategorien (nur festgehalten, noch nicht gebaut)

- Kategorie-Auswahl (beim Produkt) so übersichtlich wie die Liste unter Einstellungen → Kategorien: untereinander, eine Hauptkategorie pro Zeile mit grossem Symbol, Unterkategorien eingerückt darunter (aufklappbar). Grösser, gut lesbar.
- Mehr vordefinierte Kategorien und Unterkategorien. **Asia fehlt komplett** (neu z. B. «Internationale Küche»: Asia, Mexiko/Tex-Mex, Italien, Orient, Indien).
- Orientierung an einer gängigen Einteilung: Rubriken der Onlineshops von Migros/Coop (Früchte & Gemüse, Brot & Backwaren, Milchprodukte & Eier, Fleisch & Fisch, Vorräte, Süsses & Salziges, Getränke, Tiefkühl, Fertiggerichte, Internationale Küche, Bio/Vegi/Vegan, Drogerie & Kosmetik, Haushalt, Baby, Tiere …); offizieller Standard wäre GS1 GPC (für den Alltag zu fein). Bestehende eigene Anpassungen dürfen nicht verloren gehen.
- **Ergänzung: Automatische Kategorie noch besser** (weniger suchen):
  - Viel mehr Stichwörter (heute ca. 400), inkl. Asia (Sojasauce, Kokosmilch, Reisnudeln, Currypaste, Tofu …), Bio/Vegan, Fertiggerichte, Schweizer Marken und Eigenmarken (Rivella, Ovomaltine, Aromat, Cailler, Zweifel …).
  - Bei zusammengesetzten Wörtern zählt für die Kategorie das **Grundwort am Ende** (Erdbeer**joghurt** → Joghurt, Paprika**pulver** → Gewürze), beim Symbol bleibt das erste Wort (🍓, 🫑).
  - Einzahl/Mehrzahl und Tippfehler toleranter; Rückfall über das erkannte Symbol (🫑 → Gemüse).
  - Gescannte Produkte: Kategorie aus Open Food Facts übernehmen.
  - Bleibt: Korrekturen werden gelernt und haben Vorrang.

### Umgesetzt am 23.11.: Mehr Kategorien, bessere Auto-Kategorie, neue Kategorie-Auswahl

- 4 neue Hauptkategorien (Internationale Küche mit Asia/Mexiko/Italien/Orient/Indien, Bio/Vegi/Vegan, Fertiggerichte & Convenience, Non-Food) und über 40 neue Unterkategorien (z. B. Gewürze, Öl & Essig, Hülsenfrüchte, Milchalternativen, Windeln, Erste Hilfe). Bestehende Nutzer bekommen sie automatisch dazu, eigene Anpassungen bleiben.
- Hunderte neue Stichwörter (inkl. Schweizer Marken). Grundwort am Ende entscheidet (Erdbeerjoghurt → Joghurt), Einzahl/Mehrzahl toleranter, Rückfall über das Symbol, Strichcode übernimmt Kategorie von Open Food Facts.
- Kategorie-Auswahl: grosse Zeilen untereinander mit Symbol und Farbe, Suche oben, Unterkategorien mit ▸ aufklappbar, aktuelle Kategorie markiert.

### Notiz vom 23.11.2026: Ähnliche Produkte nacheinander (nur festgehalten, noch nicht gebaut)

- Ziel: Ähnliche Produkte stehen in der Liste direkt nacheinander. Rico weiss z. B. nicht, wohin Essig gehört.
- Heute: Liste ist nach Haupt- und Unterkategorie sortiert; Essig → «Öl & Essig» in der Hauptkategorie «Teigwaren, Reis & Konserven» (Name passt schlecht).
- Vorschlag: Hauptkategorie umbenennen in **«Vorräte»** (Teigwaren, Reis, Konserven, Hülsenfrüchte, Öl & Essig, Gewürze, Saucen, Konfitüre, Müesli); innerhalb einer Unterkategorie alphabetisch sortieren (Olivenöl neben Rapsöl, Essig daneben); beim Gedrückthalten auf dem Kategorie-Symbol zeigen «gehört zu: Vorräte › Öl & Essig».
- Ergänzung: **«Frühstück»** als eigene Hauptkategorie (Müesli & Flocken, Konfitüre & Honig, Brotaufstrich), herausgelöst aus Vorräte; Unterkategorien in «Vorräte» nach typischer Ladenordnung (Teigwaren & Reis, Konserven, Hülsenfrüchte, Saucen, Öl & Essig, Gewürze). Echte Ladenreihenfolge lernt die App weiterhin mit «Einkauf starten».

- **Umgesetzt am 23.11.:** Hauptkategorie heisst «Vorräte» (Unterkategorien in Ladenordnung), neue Hauptkategorie «Frühstück» (Müesli & Flocken, Konfitüre & Honig, Brotaufstrich; bestehende Produkte automatisch verschoben), innerhalb einer Unterkategorie alphabetisch, Gedrückthalten aufs Produkt-Symbol zeigt «gehört zu …».

### Notiz vom 23.11.2026: Menü-Knopf auf Höhe der Anrede (nur festgehalten, noch nicht gebaut)

- ☰ nicht mehr neben dem Titel, sondern rechts auf der Zeile «Hallo Rico». Ohne Namen trotzdem eine Zeile mit ☰ rechts.
- **Umgesetzt am 23.11.:** ☰ steht rechts auf der Zeile «Hallo Rico» (Klasse `hrow`, in jeder Ansicht; Anrede nur in der Liste).
- **Umgesetzt am 23.11.:** Hinweis «Zum Löschen nach links wischen» verschwindet nach 3× Wischen (`S.set.swipeN`), «Wieder anzeigen» unter Darstellung. «Letzte Produkte»: Anzahl und Sortierung nur noch in den Einstellungen (nicht mehr in der Liste). Führung angepasst.
- **Umgesetzt am 24.11.:** Aktionshinweis oben hat ✕; blendet ihn für heute aus (`S.dismiss`, Schlüssel mit Datum und Inhalt), bei neuer Aktion erscheint er wieder. In der Führung erklärt.
- 24.11. korrigiert: Aktionshinweis erscheint bei jedem Öffnen der App; ✕ blendet ihn nur bis zum nächsten Öffnen aus (`dealHid`, wird beim Wechsel in den Hintergrund zurückgesetzt).
- 24.11.: ✕ beim Aktionshinweis grösser und immer rechts neben dem Text.

### Arbeitsregel (seit 24.11.2026)

- Bei unklarer Definition immer nachfragen, bevor gebaut wird – nicht raten (Anlass: ✕ beim Aktionshinweis zuerst «für heute» statt «bis zum nächsten Öffnen» gebaut).
- 24.11.: Aktionshinweis ohne Klammer und ohne «Beispiel»: «Butter Aldi −29%».

### Notiz vom 24.11.2026: Echte Aktionen aus dem Internet (nur festgehalten, noch nicht gebaut)

- Rico möchte echte Aktionen aus dem Internet statt Beispieldaten.
- Grenzen: Migros/Coop/Aldi/Lidl haben keine offene Schnittstelle; Aktionsportale (z. B. aktionis.ch, profital.ch) automatisch auslesen verstösst meist gegen deren Nutzungsbedingungen und wird vom Browser blockiert (bräuchte eigenen Server). Rechtliche Prüfung war zurückgestellt.
- Machbar ohne Server: (a) 🔥 «Aktionen im Internet suchen» über den KI-Ratgeber mit Websuche (eigener Schlüssel, auf Knopfdruck, Ergebnis mit Quelle und Datum, nur als Hinweis); (b) Link «Aktionen ansehen» zu den offiziellen Aktionsseiten der Händler; (c) Aktionsschild fotografieren (gibt es schon).
- Offen: Beispiel-Aktionen nicht mehr als Hinweis oben zeigen (Vorschlag), weil «Butter Aldi −29%» ohne «Beispiel» echt wirkt.
- **Entschieden 24.11.:** (1) Links «Aktionen ansehen» zu den offiziellen Aktionsseiten von Migros, Coop, Aldi, Lidl (gratis); (2) Beispiel-Aktionen nicht mehr als Hinweis oben zeigen (nur unter «Aktionen», markiert). KI-Suche (ca. 1–4 Rappen pro Suche, eigener Schlüssel) später, falls gewünscht. Noch nicht gebaut.
- **Umgesetzt am 24.11.:** Beispiel-Aktionen erscheinen nicht mehr als Hinweis oben (nur echte, z. B. fotografierte). Unter «Aktionen» neu «Aktionen der Händler ansehen»: Migros, Coop, Denner, Aldi, Lidl, Volg, Spar als Links (Google-Suche «Aktionen <Händler> Schweiz diese Woche», weil die genauen Händler-Adressen hier nicht prüfbar waren). In der Führung erklärt.
