from datetime import datetime
import time
import re


def berechne_rentenluecke():
   # aktuelles Jahr ermitteln
    aktuelles_jahr = datetime.now().year
    print(f"Aktuelles Jahr: {aktuelles_jahr}")
    
    # RegEx Muster für Eingabenprüfung
    muster_name = r'^[A-Za-z0-9-]+$'        # Muster für Namen (Buchstaben, Zahlen und Bindestrich)
    muster_jahr = r'^\d{4}$'                # Muster für Jahr (nur 4-stellige Zahlen)
    muster_alter = r'^\d{2}$'               # Muster für Alter (nur 2-stellige Zahlen)    
    muster_betrag = r'^\d+(\.\d{1,2})?$'    # Muster für Beträge (Zahlen mit optionalen Dezimalstellen)
    
    
    print("_______________________________Rentenlückenrechner_______________________________________")
    print("")
    print("Die Rentenlücke ist definiert als die Differenz zwischen den Einnahmen vor Renteneintritt und")
    print("den Einnahmen nach Renteneintritt.")
    print("")
    print("Der Rentenlückenrechner soll für das Thema sensibilieren und die Stellschrauben zeigen, ")
    print("die Einfluss auf die Größe der zu erwartenden Rentenlücken haben.")
    print("Da wir alle nicht die steuerliche Situation zu unserem Renteneintritt kennen,")
    print("sollte das Ergebnis als Annäherung verstanden und ")
    print("zur Sicherheit ein entsprechender Puffer eingebaut werden.")
    print("")
    print("Bitte beachten Sie, dass auf die Rente und sonstige Einkommen unter Umständen Steuern und")
    print("Sozialabgaben anfallen können, die hier nicht berücksichtigt sind.") 
    
    
    # Daten abfragen

    # Geburtsjahr eingeben
    while True:
        eingabe = input("Geben Sie Ihr Geburtsjahr (z.B. 1980) ein: ")
        if re.match(muster_jahr, eingabe):
            geburtsjahr = int(eingabe)
            break
        else:
            print("Ungültige Eingabe. Bitte geben Sie ein Jahr mit 4 Ziffern ein (z.B. 1980).")
        
    # Renteneintrittsalter eingeben
    while True:
        eingabe = input("Geben Sie Ihr Renteneintrittsalter (z.B. 67) ein: ")
        if re.match(muster_alter, eingabe):
            renteneintrittsalter = int(eingabe)
            break
        else:
            print("Ungültige Eingabe. Bitte geben Sie ein Alter mit 2 Ziffern ein (z.B. 67).")
    
    # Lebensende eingeben
    while True:
        eingabe = input("Geben Sie Ihr gewünschtes Lebensende (z.B. 90) ein: ")
        if re.match(muster_alter, eingabe):
            lebensalter = int(eingabe)
            break
        else:
            print("Ungültige Eingabe. Bitte geben Sie ein Alter mit 2 Ziffern ein (z.B. 90).")
    
    
        
    renteneintritt = geburtsjahr + renteneintrittsalter
    jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
    rentenjahre = lebensalter - renteneintrittsalter
    lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr) 
    print(f"Sie sind aktuell {aktuelles_jahr - geburtsjahr} Jahre alt.")
    print(f"Lebensjahre bis zum Lebensende: {lebensjahre_aktuell}")
    print(f"Renteneintritt: {renteneintritt}")
    print(f"Jahre bis zum Renteneintritt: {jahre_bis_renteneintritt}")
    print(f"Jahre mit Rentenbezug: {rentenjahre}")
    
    # Ausgaben
    while True:
        eingabe = input("Geben Sie Ihre monatlichen Ausgaben (ohne Investitionen) ein: ")
        if re.match(muster_betrag, eingabe):
            ausgaben_monatlich = float(eingabe)
            break   
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")
    
        
    ausgaben = ausgaben_monatlich * 12  # jährliche Ausgaben
    #ausgaben *= (1 + float(input("Geben Sie die jährliche Ausgabensteigerung in Prozent ein: ")) / 100) ** lebensjahre_aktuell  # jährliche Ausgabensteigerung
    print(f"Jährliche Ausgaben: {ausgaben:.2f} Euro")
    
    
    # Inflation
    print("Die Inflation wird auf die jährlichen Ausgaben angewendet.")
    while True:
        eingabe = input("Geben Sie die jährliche Inflation in Prozent ein: ")
        if re.match(muster_betrag, eingabe):
            inflationsrate = float(eingabe) / 100
            break   
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")
    
    
    # Einkommen
    while True:
        eingabe = input("Geben Sie Ihre monatliche Rente (aktuell zu erwartende Rente laut Bescheid RV) ein: ")
        if re.match(muster_betrag, eingabe):
            rente_monatlich = float(eingabe)
            break   
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")

    print(f"Die aktuellen Ausgaben für Kranken- und Pflegeversicherung getraten 14,6%, damit ergibt sich eine monatliche Rente von: {rente_monatlich * 0.854} Euro.")
    rente_monatlich = rente_monatlich * 0.854
    
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
            print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")
    
    # Anpassungen nach Renteneintritt    
    while True:
        eingabe = input("Geben Sie die jährliche Rentenerhöhung während des Rentenbezugs ein: ")
        if re.match(muster_betrag, eingabe):
            rentenerhoehung_nach_rente = float(eingabe) / 100
            break   
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")

    
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
                print("Ungültige Eingabe. Bitte benutzen Sie für die Namen nur Buchstaben, Zahlen und Bindestriche.")
        
        if name.lower() == 'stop':
            break
        
        # Startjahr des Einkommens
        while True:
                eingabe = input(f"Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen {name} erhalten: ")
                if re.match(muster_jahr, eingabe):
                    startjahr = int(eingabe)
                    break   
                else:
                    print("Ungültige Eingabe. Bitte geben Sie ein Jahr mit 4 Ziffern ein (z.B. 1980).")
           
        startjahr_rente = startjahr
        
        # monatliche Zahlung des Einkommes
        while True:
            eingabe = input(f"Geben Sie die Höhe der monatlichen Zahlung für {name} ein: ")
            if re.match(muster_betrag, eingabe):
                startwert_mon = float(eingabe)
                break   
            else:
                print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")

        startwert = startwert_mon * 12  # jährliche Zahlung
        startwert_rente = startwert

        # jährliche prozentuale Steigerung des Einkommens
        while True:
            eingabe = input(f"Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für {name} ein: ")
            if re.match(muster_betrag, eingabe):
                wachstum = float(eingabe) / 100
                break   
            else:
                print("Ungültige Eingabe. Bitte geben Sie einen gültigen Betrag als Ganzzahl oder Dezimalzahl ein.")


        if startjahr < renteneintritt:
            for jahr in range(renteneintritt - startjahr):
                startwert_rente *= (1 + wachstum)    
                print(f"Durchlauf: {jahr} - Höhe der {name}: {startwert_rente:.2f} Euro am 31.12.{startjahr+jahr}")      
            startjahr_rente = renteneintritt
            print(f"Höhe der {name}: {startwert_rente:.2f} Euro in {startjahr_rente}.")
        einkuenfte.append((name,startjahr,startjahr_rente, startwert,startwert_rente, wachstum))
    
   
   
   
   # Listen für die Jahre, Einkünfte und Ausgaben
    jahre = []
    einkommen_liste = []
    einkommen_liste_zusatz = []
    einkommen_liste_summen = []
    ausgaben_liste = []
    
    # Werte zu Rentenbeginn berechnen
    # Höhe der Rente zum Beginn der Rente berechnen
    aktuelles_einkommen = rente
    for jahr in range(jahre_bis_renteneintritt):
        aktuelles_einkommen *= (1 + rentenerhoehung_vor_rente)
    
    print(f"Jährliche Rente zum Renteneintritt: {aktuelles_einkommen:.2f} Euro")
    
 
    # Höhe der Ausgaben zum Renteneintritt berechnen
    aktuelle_ausgaben = ausgaben
    for jahr in range(jahre_bis_renteneintritt):
        aktuelle_ausgaben *= (1 + inflationsrate)
    print(f"Jährliche Ausgaben zum Renteneintritt: {aktuelle_ausgaben:.2f} Euro")
 
 
 
 
    # Summen der Ausgaben und Einkünfte während der Rentenjahre 
    # Einnahmen während der Rentenjahre berechnen
    # Renteneinkünfte
    for jahr in range(rentenjahre):
        aktuelles_einkommen *= (1 + rentenerhoehung_nach_rente)
        einkommen_liste.append(aktuelles_einkommen)
    gesamt_einkommen = sum(einkommen_liste)
    print(f"Summe der Renteneinkünfte innerhalb der Rente: {gesamt_einkommen:.2f} Euro")

    # Zusätzliche Einkünfte
    if einkuenfte:
        for name,startjahr,startjahr_rente, startwert,startwert_rente, wachstum in einkuenfte:
            laufzeit = (geburtsjahr + lebensalter) - startjahr_rente
            print(f"Name: {name} hat eine Laufzeit: {laufzeit} Jahren")
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
        print(f"Zusätzliche Einkünfte von {name} innerhalb der Rente: {betrag:.2f} Euro")
    
    
    # Ausgaben während der Rentenjahre berechnen
    for jahr in range(rentenjahre):
        aktuelle_ausgaben *= (1 + inflationsrate)
        ausgaben_liste.append(aktuelle_ausgaben)           
    gesamt_ausgaben = sum(ausgaben_liste)
    print(f"Summe der Ausgaben innerhalb der Rente: {gesamt_ausgaben:.2f} Euro")
    
    # Berechnung der Rentenlücke
    # zusätzliche Einkünfte einbeziehen
    if einkuenfte:
        gesamt_einkommen += ges_einkommen_zusatz
       
    rentenluecke = gesamt_ausgaben - (gesamt_einkommen)
    if rentenluecke > 0:
        print(f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
    else:
        print("Sie haben keine Rentenlücke, Ihre Einkünfte decken die Ausgaben.")
        print(f"Der Überschuss geträgt: {abs(rentenluecke):.2f} Euro.")
      

# Programm ausführen
berechne_rentenluecke()