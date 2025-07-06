# 🧮 Rentenlückenrechner

**Version:** 0.9.0  
**Sprache:** Python  
**Lizenz:**  MIT

📃 Lizenz
Dieses Projekt steht unter der MIT-Lizenz – siehe LICENSE für Details.

👤 Autor
[Steffen Tschirner]
📧 [rlr@hilf-dir-selber.de]
🌐 GitHub: github.com/hilfdirselbst


## 📌 Beschreibung

Der **Rentenlückenrechner** ist ein einfaches Python-Skript zur Berechnung der voraussichtlichen Rentenlücke im Alter.
Basierend auf:
- aktuellen Ausgaben
- persönlichen Inflation
- voraussichtlicher Rente laut Renteninformation
  - jährliche prozentuale Erhöhung der Rente bis zum Renteneintritt
  - jährliche prozentuale Erhöhung der Rente während der Rentenbezugszeit 
- Renteneintrittsalter
- Wunschalter
- Eingabe bereits vorhandener Zusatzeinkommen z.B. Zusatzrenten, Versicherungen, Kapitalerträge
werden die Summe der Einkünfte und Ausgaben während der Rentenbezugszeit ermittelt und daraus die Rentenlücke bzw. ein vorhandener Überschuss errechnet.

Die Ergenisse werden anschließend in eine PDF Datei geschrieben.

---

## 🚀 Funktionen

- Kommandozeilenbasiertes Interface
- Berechnung der Rentenlücke
- Export der Ergebnisse als **PDF-Bericht** (via `fpdf`)

---

## 🛠️ Installation

### Voraussetzungen

- Python 3.8 oder höher
- fpdf

---

## ▶️ Verwendung

python rentenlueckenrechner.py

### 📄 Beispielausgabe
```
Geben Sie Ihr Geburtsjahr (z.B. 1980) ein: 1978
Geben Sie Ihr Renteneintrittsalter (z.B. 67) ein: 67
Geben Sie Ihr Wunschalter (z.B. 90) ein: 90
-----------------------------------------------------------------------------------
Geburtsjahr: 1978
Renteneintrittsalter: 67
Wunschalter: 90
Aktuelles Jahr: 2025
Sie sind aktuell 47 Jahre alt.
Jahre bis zum Wunschalter: (90): 43
Renteneintritt: 2045
Jahre bis zum Renteneintritt: 20
Jahre mit Rentenbezug: 23
-----------------------------------------------------------------------------------
Geben Sie Ihre aktuellen monatlichen Ausgaben (ohne Investitionen) ein: 1800
Ausgaben und Inflation
.
Persönliche Inflation: 3.00%
Die eingegebene Inflation wird auf die Hochrechnung der Ausgaben angewendet.
-----------------------------------------------------------------------------------
Geben Sie Ihre monatliche Rente (aktuell zu erwartende Rente laut Bescheid RV) ein: 1500
Einkommen
Monatliche Rente laut Bescheid RV: 1.500,00 Euro
Die monatliche Rente wird um die Kranken- und Pflegeversicherung (aktuell 14,6%) reduziert.
Ausgezahlte Rente: 1.281,00 Euro. (dieser Wert wird für die Berechnung der Rentenlücke verwendet)
------------------------------------
Geben Sie die jährliche prozentuale Erhöhung der Rente bis zum Renteneintritt ein: 2
Geben Sie die jährliche prozentuale Erhöhung der Rente während des Rentenbezugs ein: 2
Rentenanpassungen
Jährliche Rentenerhöhung bis zum Renteneintritt: 2.00%
Jährliche Rentenerhöhung während des Rentenbezugs: 2.00%
-----------------------------------------------------------------------------------
Zusätzliche Einkünfte
Sie können jetzt weitere Einkünfte, wie private Renten-, Lebensversicherungen oder andere Einkünfte, eingeben.
Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): Direktversicherung
Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen Direktversicherung erhalten: 2045
Geben Sie die Höhe des monatlichen Einkommens Direktversicherung ein: 200
Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für Direktversicherung ein: 0
-----------------------------------------------------------------------------------
Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): Dividenden-und-Zinsen
Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen Dividenden-und-Zinsen erhalten: 2045
Geben Sie die Höhe des monatlichen Einkommens Dividenden-und-Zinsen ein: 500
Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für Dividenden-und-Zinsen ein: 3
-----------------------------------------------------------------------------------
Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): stop
-----------------------------------------------------------------------------------
Übersicht der monatlichen Einkünfte und Ausgaben zum Renteneintritt:
monatliche ausgezahlte Rente zum Renteneintritt (2045): 1.903,50 Euro
monatliche Ausgaben zum Renteneintritt (2045): 3.251,00 Euro
-----------------------------------------------------------------------------------
Berechnung der Rentenlücke
Während der Rentenbezugszeit von 23 Jahren haben Sie folgende Einkünfte und Ausgaben:
Summe der Renteneinkünfte: 672.053,69 Euro
Zusätzliche Einkünfte durch Direktversicherung: 55.200,00 Euro
Zusätzliche Einkünfte durch Dividenden-und-Zinsen: 200.558,82 Euro
Summe der Ausgaben : 1.304.033,55 Euro
-----------------------------------------------------------------------------------
Ergebnis
Die Rentenlücke beträgt: 376.221,03 Euro.
-----------------------------------------------------------------------------------
Eine PDF Datei mit der Berechnung wurden im aktuellen Verzeichnis erstellt: Rentenluecken-Berechnung_06-07-2025_17-32-16.pdf
``
