from fpdf import FPDF
from datetime import datetime
import re


def erstelle_pdf(geburtsjahr, renteneintrittsalter, lebensalter, ausgaben_monatlich, inflationsrate, rente_monatlich):
    # Erstelle eine FPDF-Instanz
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Setze Schriftart
    pdf.set_font("Arial", size=12)

    # Titel und Einführung
    pdf.cell(200, 10, txt="Rentenlückenrechner - Eingaben und Ausgaben", ln=True, align="C")
    pdf.ln(10)

    # Aktuelles Jahr und Berechnungen
    aktuelles_jahr = datetime.now().year
    renteneintritt = geburtsjahr + renteneintrittsalter
    jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
    rentenjahre = lebensalter - renteneintrittsalter
    lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr)

    pdf.cell(200, 10, txt=f"Aktuelles Jahr: {aktuelles_jahr}", ln=True)
    pdf.cell(200, 10, txt=f"Sie sind aktuell {aktuelles_jahr - geburtsjahr} Jahre alt.", ln=True)
    pdf.cell(200, 10, txt=f"Lebensjahre bis zum Lebensende: {lebensjahre_aktuell}", ln=True)
    pdf.cell(200, 10, txt=f"Renteneintritt: {renteneintritt}", ln=True)
    pdf.cell(200, 10, txt=f"Jahre bis zum Renteneintritt: {jahre_bis_renteneintritt}", ln=True)
    pdf.cell(200, 10, txt=f"Jahre mit Rentenbezug: {rentenjahre}", ln=True)
    pdf.ln(10)

    # Eingaben
    pdf.cell(200, 10, txt=f"Monatliche Ausgaben: {ausgaben_monatlich:.2f} Euro", ln=True)
    pdf.cell(200, 10, txt=f"Jährliche Inflation: {inflationsrate * 100:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"Monatliche Rente: {rente_monatlich * 0.854:.2f} Euro", ln=True)
    pdf.ln(10)

    # Berechnung der Ausgaben und Einkünfte
    ausgaben = ausgaben_monatlich * 12
    aktuelle_ausgaben = ausgaben * (1 + inflationsrate) ** jahre_bis_renteneintritt
    aktuelles_einkommen = rente_monatlich * 12  # jährliche Rente
    gesamt_einkommen = aktuelles_einkommen

    # Berechnung der Rentenlücke
    for jahr in range(rentenjahre):
        aktuelles_einkommen *= (1 + float(entry_rentenerhoehung_nach_rente.get()) / 100)
        gesamt_einkommen += aktuelles_einkommen

    rentenluecke = aktuelle_ausgaben - gesamt_einkommen

    if rentenluecke > 0:
        pdf.cell(200, 10, txt=f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.", ln=True)
    else:
        pdf.cell(200, 10, txt=f"Keine Rentenlücke, Überschuss: {abs(rentenluecke):.2f} Euro.", ln=True)

    # Speichern der PDF-Datei
    pdf_output_filename = "Rentenluecke_Berechnung.pdf"
    pdf.output(pdf_output_filename)
    print(f"Die PDF wurde erfolgreich erstellt: {pdf_output_filename}")

# Beispiel für die Eingabewerte
geburtsjahr = 1980
renteneintrittsalter = 67
lebensalter = 90
ausgaben_monatlich = 1500
inflationsrate = 0.02  # 2% Inflation
rente_monatlich = 1200

# Aufruf der PDF-Erstellung
erstelle_pdf(geburtsjahr, renteneintrittsalter, lebensalter, ausgaben_monatlich, inflationsrate, rente_monatlich)
