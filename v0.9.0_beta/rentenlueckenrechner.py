from datetime import datetime
import time
import re
from fpdf import FPDF

def berechne_rentenluecke():
    
    class PDFExporter(FPDF):
            def __init__(self):
                super().__init__()
                self.add_page()
                self.set_auto_page_break(auto=True, margin=15)
                self.set_font("Helvetica")

            def add_metadata_block(self, version, author, status, last_modified):
                self.set_font("Helvetica", "I", 9)
                self.set_text_color(100, 100, 100)
                metadata_text = (
                    f"Version: {version}        "
                    f"Ersteller: {author}       "
                    f"Status: {status}         "
                    f"Letzte Änderung: {last_modified}"
                )
                self.cell(0, 6, metadata_text, ln=True, align='C')
                self.ln(4)

            def add_main_title(self, text):
                self.set_font("Helvetica", "B", 20)
                self.set_text_color(0, 0, 128)
                self.cell(0, 10, text, ln=True, align='C')
                self.ln(3)

            def add_subheading(self, text):
                self.set_font("Helvetica", "B", 14)
                self.set_text_color(0, 0, 0)
                self.cell(0, 8, text, ln=True)
                self.ln(1)

            def add_description(self, text):
                self.set_font("Helvetica", "", 10)
                self.set_text_color(50, 50, 50)
                self.multi_cell(0, 7, text)
                self.ln(1)

            def add_input_text(self, text):
                self.set_font("Courier", "I", 11)
                self.set_text_color(0, 102, 204)
                self.multi_cell(0, 6, f" {text}")
                self.ln(0)

            def add_code_output(self, text):
                self.set_font("Courier", "", 11)
                self.set_text_color(0, 153, 0)
                self.set_fill_color(230, 230, 230)
                self.multi_cell(0, 6, f"Ausgabe:\n{text}", fill=True)
                self.ln(3)

    # Initialisiere die PDF-Instanz
    pdf = PDFExporter()

    # Füge Titel hinzu
    pdf.add_main_title("Rentenlückenrechner")

    # Füge Metadaten hinzu
    pdf.add_metadata_block(
    version="0.9.0",
    author="Steffen Tschirner (rlr@hilf-dir-selbst.de)",
    status="beta",
    last_modified=datetime.today().strftime("%d.%m.%Y")
    
)
 
    # RegEx Muster für Eingabenprüfung
    muster_name = r'^[A-Za-z0-9-]+$'        # Muster für Namen (Buchstaben, Zahlen und Bindestrich)
    muster_jahr = r'^\d{4}$'                # Muster für Jahr (nur 4-stellige Zahlen)
    muster_alter = r'^\d{2}$'               # Muster für Alter (nur 2-stellige Zahlen)    
    muster_betrag = r'^\d+(\.\d{1,2})?$'    # Muster für Beträge (Zahlen mit optionalen Dezimalstellen)
    
    # Variablen für Prüfung
    betrag_ungueltig ="Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl mit Punkt (1.45) ein."
    jahr_ungueltig = "Ungültige Eingabe. Bitte geben Sie ein Jahr mit 4 Zahlen ein (z.B. 1980)."
    alter_ungueltig = "Ungültige Eingabe. Bitte geben Sie ein Alter mit 2 Zahlen ein (z.B. 67)."
    name_ungueltig = "Ungültige Eingabe. Bitte benutzen Sie für die Namen nur Buchstaben, Zahlen und Bindestriche."
    
    
    # Daten abfragen

    # Geburtsjahr eingeben
    while True:
        eingabe = input("Geben Sie Ihr Geburtsjahr (z.B. 1980) ein: ")
        if re.match(muster_jahr, eingabe):
            geburtsjahr = int(eingabe)
            break
        else:
            print(f"{jahr_ungueltig}")
        
    # Renteneintrittsalter eingeben
    while True:
        eingabe = input("Geben Sie Ihr Renteneintrittsalter (z.B. 67) ein: ")
        if re.match(muster_alter, eingabe):
            renteneintrittsalter = int(eingabe)
            break
        else:
            print(f"{alter_ungueltig}")
    
    # Lebensende eingeben
    while True:
        eingabe = input("Geben Sie Ihr Wunschalter (z.B. 90) ein: ")
        if re.match(muster_alter, eingabe):
            lebensalter = int(eingabe)
            break
        else:
            print(f"{alter_ungueltig}")
    
    # aktuelles Jahr und Zeitstempel der Berechnung ermitteln
    aktuelles_jahr = datetime.now().year
    current_time=time.strftime("%d.%m.%Y %H:%M:%S")
    datei_current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    # Renteneintrittsjahr
    renteneintritt = geburtsjahr + renteneintrittsalter
    
    # Jahre bis zum Renteneintritt
    jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
    
    # Jahre mit Rentenbezug
    rentenjahre = lebensalter - renteneintrittsalter
    
    # Lebensjahre bis zum Lebensende
    lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr) 

    print("-----------------------------------------------------------------------------------")
    pdf.add_subheading("Berechnungsgrundlagen")
    pdf.add_input_text(f"Datum: {current_time}")
 

    # Eingegebene Daten ausgeben und in PDF schreiben
    # Geburtsjahr
    print(f"Geburtsjahr: {geburtsjahr}")
    pdf.add_input_text(f"Geburtsjahr: {geburtsjahr}")
    
    # Renteneintrittsalter
    print(f"Renteneintrittsalter: {renteneintrittsalter}")
    pdf.add_input_text(f"Renteneintrittsalter: {renteneintrittsalter}")
    
    # Wunschalter
    print(f"Wunschalter: {lebensalter}")
    pdf.add_input_text(f"Wunschalter: {lebensalter}")
    
    # aktuelles Jahr
    print(f"Aktuelles Jahr: {aktuelles_jahr}")
    pdf.add_input_text(f"Aktuelles Jahr: {aktuelles_jahr}")
    
    # aktuelles Alter 
    print(f"Sie sind aktuell {aktuelles_jahr - geburtsjahr} Jahre alt.")
    pdf.add_input_text(f"Sie sind aktuell {aktuelles_jahr - geburtsjahr} Jahre alt.")
    
    # Jahre bis Wunschalter
    print(f"Jahre bis zum Wunschalter: ({lebensalter}): {lebensjahre_aktuell}")
    pdf.add_input_text(f"Jahre bis zum Wunschalter: ({lebensalter}): {lebensjahre_aktuell}")
    
    # Renteneintrittsalter
    print(f"Renteneintritt: {renteneintritt}")
    pdf.add_input_text(f"Renteneintritt: {renteneintritt}")
    
    # Jahre bis zum Renteneintritt
    print(f"Jahre bis zum Renteneintritt: {jahre_bis_renteneintritt}")
    pdf.add_input_text(f"Jahre bis zum Renteneintritt: {jahre_bis_renteneintritt}")
    
    # Jahre mit Rentenbezug
    print(f"Jahre mit Rentenbezug: {rentenjahre}")
    pdf.add_input_text(f"Jahre mit Rentenbezug: {rentenjahre}")
    print("-----------------------------------------------------------------------------------")
    
    
    # Ausgaben
    while True:
        eingabe = input("Geben Sie Ihre aktuellen monatlichen Ausgaben (ohne Investitionen) ein: ")
        if re.match(muster_betrag, eingabe):
            #eingabe = re.sub(r'\,(?=\d{3})', '.', eingabe)  # 
            #eingabe_mit_punkt = re.sub(r',', '.', eingabe, 1)
            ausgaben_monatlich = float(eingabe)
            break   
        else:
            print(f"{betrag_ungueltig}")
    
        
    ausgaben = ausgaben_monatlich * 12  # jährliche Ausgaben
    #ausgaben *= (1 + float(input("Geben Sie die jährliche Ausgabensteigerung in Prozent ein: ")) / 100) ** lebensjahre_aktuell  # jährliche Ausgabensteigerung
    
    # Ausgaben
    print("Ausgaben und Inflation")
    pdf.add_subheading("Ausgaben und Inflation")
    
    # Monatliche Ausgaben
    print(f"Monatliche Ausgaben: {ausgaben_monatlich:.2f} Euro")
    pdf.add_input_text(f"Monatliche Ausgaben: {ausgaben_monatlich:.2f} Euro")
    
    # Jährliche Ausgaben
    print(f"Jährliche Ausgaben: {ausgaben:.2f} Euro")
    pdf.add_input_text(f"Jährliche Ausgaben: {ausgaben:.2f} Euro")
    
    # Inflation
    while True:
        eingabe = input("Geben Sie Ihre persönliche Inflation in Prozent ein: ")
        if re.match(muster_betrag, eingabe):
            inflationsrate = float(eingabe) / 100
            break   
        else:
            print(f"{betrag_ungueltig}")
    
    # persönliche Inflation
    print(f"Persönliche Inflation: {inflationsrate * 100:.2f}%")
    pdf.add_input_text(f"Persönliche Inflation: {inflationsrate * 100:.2f}%")
    
    print("Die eingegebene Inflation wird auf die Hochrechnung der Ausgaben angewendet.")
    pdf.add_description("Die eingegebene Inflation wird auf die Hochrechnung der Ausgaben angewendet.")
    print("-----------------------------------------------------------------------------------")
    
    
    
    # Einkommen
    while True:
        eingabe = input("Geben Sie Ihre monatliche Rente (aktuell zu erwartende Rente laut Bescheid RV) ein: ")
        if re.match(muster_betrag, eingabe):
            rente_monatlich = float(eingabe)
            break   
        else:
            print(f"{betrag_ungueltig}")

    print("Einkommen")
    pdf.add_subheading("Einkommen")
    # Monatliche Rente laut Bescheid RV
    # Tausenderpunkt im Format
    formatted_rente_montlich = f"{rente_monatlich:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f"Monatliche Rente laut Bescheid RV: {formatted_rente_montlich} Euro")
    pdf.add_input_text(f"Monatliche Rente laut Bescheid RV: {formatted_rente_montlich} Euro")

    # Monatliche Rente nach Abzug der Kranken- und Pflegeversicherung
    print("Die monatliche Rente wird um die Kranken- und Pflegeversicherung (aktuell 14,6%) reduziert.")
    pdf.add_description("Die monatliche Rente wird um die Kranken- und Pflegeversicherung (aktuell 14,6%) reduziert.")    
    # Nettorente
    netto_rente_monatlich = rente_monatlich * 0.854  # Abzug von 14,6% für Kranken- und Pflegeversicherung
    formatted_rente_montlich = f"{netto_rente_monatlich:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"Ausgezahlte Rente: {formatted_rente_montlich} Euro. (dieser Wert wird für die Berechnung der Rentenlücke verwendet)") 
    pdf.add_input_text(f"Ausgezahlte Rente: {formatted_rente_montlich} Euro.\n(dieser Wert wird für die Berechnung der Rentenlücke verwendet)")
    rente_monatlich = netto_rente_monatlich
    print("------------------------------------")
        
    rente = rente_monatlich * 12  # jährliche Rente
    #einkommen_monatlich = float(input("Geben Sie Ihr monatliches Einkommen ein: "))
    #einkommen = einkommen_monatlich * 12  # jährliches Einkommen

    # Rentenanpassungen
    # Anpassungen bis Renteneintritt
    while True:
        eingabe = input("Geben Sie die jährliche prozentuale Erhöhung der Rente bis zum Renteneintritt ein: ")
        if re.match(muster_betrag, eingabe):
            rentenerhoehung_vor_rente = float(eingabe) / 100
            break   
        else:
            print(f"{betrag_ungueltig}")
    
    # Anpassungen nach Renteneintritt    
    while True:
        eingabe = input("Geben Sie die jährliche prozentuale Erhöhung der Rente während des Rentenbezugs ein: ")
        if re.match(muster_betrag, eingabe):
            rentenerhoehung_nach_rente = float(eingabe) / 100
            break   
        else:
            print(f"{betrag_ungueltig}")

    print("Rentenanpassungen")
    pdf.add_subheading("Rentenanpassungen")
    # Rentenerhöhung bis Renteneintritt
    print(f"Jährliche Rentenerhöhung bis zum Renteneintritt: {rentenerhoehung_vor_rente * 100:.2f}%")
    pdf.add_input_text(f"Jährliche Rentenerhöhung bis zum Renteneintritt: {rentenerhoehung_vor_rente * 100:.2f}%")      
    # Rentenerhöhung während des Rentenbezugs
    print(f"Jährliche Rentenerhöhung während des Rentenbezugs: {rentenerhoehung_nach_rente * 100:.2f}%")
    pdf.add_input_text(f"Jährliche Rentenerhöhung während des Rentenbezugs: {rentenerhoehung_nach_rente * 100:.2f}%")
    print("-----------------------------------------------------------------------------------")
   

    print("Zusätzliche Einkünfte")
    pdf.add_subheading("Zusätzliche Einkünfte")    
    # zusätzliche Einkünfte 
    # Hier können Sie weitere Einkünfte hinzufügen z.B private Renten-, Lebensversicherungen oder andere Einkünfte
    einkuenfte = []
    print("Sie können jetzt weitere Einkünfte, wie private Renten-, Lebensversicherungen oder andere Einkünfte, eingeben.")
    while True:
        # Namen des Einkommens
        while True:
            eingabe = input("Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): ")
            if re.match(muster_name, eingabe):
                name = eingabe
                break   
            else:
                print(f"{name_ungueltig}")
        
        if name.lower() == 'stop':
            break
        pdf.add_input_text(f"Einkommen: {name}")
        
        # Startjahr des Einkommens
        while True:
                eingabe = input(f"Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen {name} erhalten: ")
                if re.match(muster_jahr, eingabe):
                    startjahr = int(eingabe)
                    break   
                else:
                    print(f"{jahr_ungueltig}")
           
        startjahr_rente = startjahr
        pdf.add_input_text(f"Startjahr des Einkommens {name}: {startjahr}")
        
        # monatliche Zahlung des Einkommes
        while True:
            eingabe = input(f"Geben Sie die Höhe des monatlichen Einkommens {name} ein: ")
            if re.match(muster_betrag, eingabe):
                startwert_mon = float(eingabe)
                break   
            else:
                print(f"{betrag_ungueltig}")

        startwert = startwert_mon * 12  # jährliche Zahlung
        startwert_rente = startwert
        formatted_startwert_mon = f"{startwert_mon:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        pdf.add_input_text(f"Höhe des Einkommens {name} (monatlich): {formatted_startwert_mon} Euro")
        
        # jährliche prozentuale Steigerung des Einkommens
        while True:
            eingabe = input(f"Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für {name} ein: ")
            if re.match(muster_betrag, eingabe):
                wachstum = float(eingabe) / 100
                break   
            else:
                print(f"{betrag_ungueltig}")

        pdf.add_input_text(f"Jährliche Steigerung des Einkommens {name}: {wachstum * 100:.2f}%")
    
        if startjahr < renteneintritt:
            # Berechnung der Höhe des Einkommens bis zum Renteneintritt
            print(f"Berechnung der Höhe des Einkommens {name} bis zum Renteneintritt ({renteneintritt}):")
            for jahr in range(renteneintritt - startjahr):
                startwert_rente *= (1 + wachstum)    
                print(f"{startjahr+jahr}: Höhe der {name}: {startwert_rente:.2f} Euro.")      
            startjahr_rente = renteneintritt
            #print(f"Höhe der {name}: {startwert_rente:.2f} Euro in {startjahr_rente}. Die jährliche Steigerung beträgt: {wachstum * 100:.2f}%.")
            #pdf.add_input_text(f"Höhe der {name}: {startwert_rente:.2f} Euro in {startjahr_rente}. Die jährliche Steigerung beträgt: {wachstum * 100:.2f}%.")
        
        print("-----------------------------------------------------------------------------------")
        pdf.add_input_text(f"-------------------------------------------------------------------")
        einkuenfte.append((name,startjahr,startjahr_rente, startwert,startwert_rente, wachstum))
    
    
   
   
   
   # Listen für die Jahre, Einkünfte und Ausgaben
    jahre = []
    einkommen_liste = []
    einkommen_liste_zusatz = []
    einkommen_liste_summen = []
    ausgaben_liste = []
    
    # werte zu Rentenbeginn berechnen
    print("-----------------------------------------------------------------------------------")
    print("Übersicht der monatlichen Einkünfte und Ausgaben zum Renteneintritt:")
    pdf.add_subheading("Übersicht der monatlichen Einkünfte und Ausgaben zum Renteneintritt")
    # Höhe der Rente zum Beginn der Rente berechnen
    aktuelles_einkommen = rente
    for jahr in range(jahre_bis_renteneintritt):
        aktuelles_einkommen *= (1 + rentenerhoehung_vor_rente)
    
    # Tausenderpunkt im Format
    montl_aktuelles_einkommen = aktuelles_einkommen / 12  # monatliche Rente
    formatted_aktuelles_einkommen = f"{montl_aktuelles_einkommen:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"monatliche ausgezahlte Rente zum Renteneintritt ({renteneintritt}): {formatted_aktuelles_einkommen} Euro")
    pdf.add_input_text(f"monatliche ausgezahlte Rente zum Renteneintritt ({renteneintritt}): {formatted_aktuelles_einkommen} Euro")
 
    # Höhe der Ausgaben zum Renteneintritt berechnen
    aktuelle_ausgaben = ausgaben
    for jahr in range(jahre_bis_renteneintritt):
        aktuelle_ausgaben *= (1 + inflationsrate)

    # Tausenderpunkt im Format
    montl_aktuelle_ausgaben = aktuelle_ausgaben / 12  # monatliche Ausgaben
    formatted_aktuelle_ausgaben = f"{montl_aktuelle_ausgaben:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"monatliche Ausgaben zum Renteneintritt ({renteneintritt}): {formatted_aktuelle_ausgaben} Euro")
    pdf.add_input_text(f"monatliche Ausgaben zum Renteneintritt ({renteneintritt}): {formatted_aktuelle_ausgaben} Euro")
 
    print("-----------------------------------------------------------------------------------")
    # neue Seite für die Rentenlückenberechnung
    # pdf.add_page()
    print("Berechnung der Rentenlücke")
    pdf.add_subheading("Berechnung der Rentenlücke")
     # Summen der Ausgaben und Einkünfte während der Rentenjahre 
    print(f"Während der Rentenbezugszeit von {rentenjahre} Jahren haben Sie folgende Einkünfte und Ausgaben:")
    pdf.add_description(f"Während der Rentenbezugszeit von {rentenjahre} Jahren haben Sie folgende Einkünfte und Ausgaben:")
    # Einnahmen während der Rentenjahre berechnen
    # Renteneinkünfte
    for jahr in range(rentenjahre):
        aktuelles_einkommen *= (1 + rentenerhoehung_nach_rente)
        einkommen_liste.append(aktuelles_einkommen)
    gesamt_einkommen = sum(einkommen_liste)
    # Tausenderpunkt im Format
    formatted_gesamt_einkommen = f"{gesamt_einkommen:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"Summe der Renteneinkünfte: {formatted_gesamt_einkommen} Euro")
    pdf.add_input_text(f"Summe der Renteneinkünfte: {formatted_gesamt_einkommen} Euro")

    # Zusätzliche Einkünfte
    if einkuenfte:
        for name,startjahr,startjahr_rente, startwert,startwert_rente, wachstum in einkuenfte:
            laufzeit = (geburtsjahr + lebensalter) - startjahr_rente
            #print(f"Name: {name} hat eine Laufzeit: {laufzeit} Jahren")
            #print(f"Name: {name} hat eine Laufzeit: {laufzeit} Jahren, Startjahr: {startjahr_rente}, Startwert: {startwert_rente:.2f} Euro, jährliches Wachstum: {wachstum:.2f}")
            zusatz_einkommen = 0 #initialisieren
            einkommen_liste_zusatz = [] #initialisieren
            for jahr in range(laufzeit):
                zusatz_einkommen = 0 #initialisieren
                startwert_rente *= (1 + wachstum)
                #print(f"Durchlauf: {jahr} - Höhe der {name}: {startwert_rente:.2f} Euro am 31.12.{startjahr_rente+jahr}")
                zusatz_einkommen  += startwert_rente
                einkommen_liste_zusatz.append(zusatz_einkommen)
                #print(f"Summe von {name} in Jahr {startjahr_rente+jahr}: {sum(einkommen_liste_zusatz):.2f} Euro")    
            gesamt_einkommen_zusatz = sum(einkommen_liste_zusatz)
            einkommen_liste_summen.append((name,sum(einkommen_liste_zusatz)))
            #for name,betrag in einkommen_liste_summen:
            #    print(f"Zusätzliche Einkünfte von {name} innerhalb der Rente: {betrag:.2f} Euro")
            
            #print(f"Name: {name} bringt zusätzlichen Einkünfte innerhalb der Rente von: {gesamt_einkommen_zusatz:.2f} Euro")
    
    ges_einkommen_zusatz = 0 #initialisieren
    ges_einkommen_zusatz = sum(betrag for name, betrag in einkommen_liste_summen)
    for name,betrag in einkommen_liste_summen:
        # Tausenderpunkt im Format
        formatted_betrag = f"{betrag:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Zusätzliche Einkünfte durch {name}: {formatted_betrag} Euro")
        pdf.add_input_text(f"Zusätzliche Einkünfte durch {name}: {formatted_betrag} Euro")
    
    
    # Ausgaben während der Rentenjahre berechnen
    for jahr in range(rentenjahre):
        aktuelle_ausgaben *= (1 + inflationsrate)
        ausgaben_liste.append(aktuelle_ausgaben)           
    gesamt_ausgaben = sum(ausgaben_liste)
    # Tausenderpunkt im Format
    formatted_gesamt_ausgaben = f"{gesamt_ausgaben:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"Summe der Ausgaben : {formatted_gesamt_ausgaben} Euro")
    pdf.add_input_text(f"Summe der Ausgaben: {formatted_gesamt_ausgaben} Euro")
    
    # Berechnung der Rentenlücke
    # zusätzliche Einkünfte einbeziehen
    if einkuenfte:
        gesamt_einkommen += ges_einkommen_zusatz
       
    rentenluecke = gesamt_ausgaben - (gesamt_einkommen)
 
    print("-----------------------------------------------------------------------------------")
    print("Ergebnis")
    pdf.add_subheading("Ergebnis")
 
    if rentenluecke > 0:
        # Tausenderpunkt im Format
        formatted_rentenluecke = f"{rentenluecke:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Die Rentenlücke beträgt: {formatted_rentenluecke} Euro.")
        pdf.add_input_text(f"Die Rentenlücke beträgt: {formatted_rentenluecke} Euro.")
    else:
        print("Sie haben keine Rentenlücke, Ihre Einkünfte sind höher Ihre Ausgaben.")
        pdf.add_input_text("Sie haben keine Rentenlücke, Ihre Einkünfte sind höher als Ihre Ausgaben.")
        # Überschuss
        abs_rentenluecke = abs(rentenluecke)
        formatted_abs_rentenluecke = f"{abs_rentenluecke:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Der Überschuss geträgt: {formatted_abs_rentenluecke} Euro.")
        pdf.add_input_text(f"Der Überschuss geträgt: {formatted_abs_rentenluecke} Euro.")
  
    print("-----------------------------------------------------------------------------------")
     # Speichern der PDF-Datei
    pdf_output_filename = f"Rentenluecken-Berechnung_{datei_current_time}.pdf"
    pdf.output(pdf_output_filename)
    print(f"Eine PDF Datei mit der Berechnung wurden im aktuellen Verzeichnis erstellt: {pdf_output_filename}")      

# Programm ausführen
berechne_rentenluecke()