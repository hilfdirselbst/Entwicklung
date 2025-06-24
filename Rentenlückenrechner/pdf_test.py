from fpdf import FPDF

# Beispielausgaben
ausgaben = [
    "Erste Ausgabe",
    "Zweite Zeile mit Infos",
    "Noch eine Ausgabe mit mehr Text",
    "Letzte Zeile"
]


version = "v0.9.0"

pdf = FPDF()
pdf.add_page()

# --- Überschrift (links oder zentriert) ---
pdf.set_font("Arial", style="B", size=16)
pdf.cell(0, 10, txt="Rentenlückenrechner", ln=0, align="C")  # ln=0 = gleiche Zeile

# --- Version rechts ---
pdf.set_font("Arial", size=10)
pdf.cell(0, 10, txt=version, ln=1, align="R")  # ln=1 = neue Zeile nach dieser

# Optional: etwas Abstand danach
pdf.ln(5)

# --- Ausgabezeilen ---
pdf.set_font("Arial", size=12)
for zeile in ausgaben:
    pdf.cell(200, 10, txt=zeile, ln=True)
    
# Linker Textblock
pdf.set_xy(10, 30)
pdf.multi_cell(100, 10, "Langer beschreibender Text mit Zeilenumbruch.",border=1)

# Rechter Block (kleinere Box mit Hinweis oder Version)
pdf.set_xy(120, 30)
pdf.set_font("Arial", size=10)
pdf.multi_cell(70, 10, "Version 1.2.3", align="R", border=1)


pdf.output("ausgaben_mit_ueberschrift_und_version.pdf")
