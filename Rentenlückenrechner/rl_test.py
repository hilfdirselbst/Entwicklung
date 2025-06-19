from datetime import datetime
import time
import re


#from matplotlib import matplotlib.pyplot as plt

def berechne_rentenluecke():
   # aktuelles Jahr ermitteln
    aktuelles_jahr = datetime.now().year
    print(f"Aktuelles Jahr: {aktuelles_jahr}")
    
    # RegEx Muster für Eingabenprüfung
    muster_name = r'^[A-Za-z0-9-]+$'        # Muster für Namen (Buchstaben, Zahlen und Bindestrich)
    muster_jahr = r'^\d{4}$'                # Muster für Jahr (nur 4-stellige Zahlen)
    muster_alter = r'^\d{2}$'               # Muster für Alter (nur 2-stellige Zahlen)    
    muster_betrag = r'^\d+(\.\d{1,2})?$'    # Muster für Beträge (Zahlen mit optionalen Dezimalstellen)
    
    # Benutzereingaben abfragen
    # Zeitrahmen
    geburtsjahr = int(input("Geben Sie Ihr Geburtsjahr (z.B. 1980) ein: "))
    renteneintrittsalter = int(input("Geben Sie Ihr Renteneintrittsalter (z.B. 67) ein: "))
    renteneintritt = geburtsjahr + renteneintrittsalter
    lebensalter = int(input("Geben Sie Ihr gewünschtes Lebensende (z.B. 90) ein: "))
    jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
    rentenjahre = lebensalter - renteneintrittsalter
    lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr) 
    print(f"Sie sind aktuell {aktuelles_jahr - geburtsjahr} Jahre alt.")
    print(f"Ihre Lebensjahre bis zum Lebensende: {lebensjahre_aktuell}")
    print(f"Renteneintritt: {renteneintritt}")
    print(f"Jahre bis zum Renteneintritt: {jahre_bis_renteneintritt}")
    print(f"Jahre nach dem Renteneintritt: {rentenjahre}")
    
    # Ausgaben
    ausgaben_monatlich = float(input("Geben Sie Ihre monatlichen Ausgaben (ohne Investitionen) ein: "))
    ausgaben = ausgaben_monatlich * 12  # jährliche Ausgaben
    #ausgaben *= (1 + float(input("Geben Sie die jährliche Ausgabensteigerung in Prozent ein: ")) / 100) ** lebensjahre_aktuell  # jährliche Ausgabensteigerung
    print(f"Jährliche Ausgaben: {ausgaben:.2f} Euro")
    
    # Inflation
    print("Die Inflation wird auf die jährlichen Ausgaben angewendet.")
    inflationsrate = float(input("Geben Sie die jährliche Inflation in Prozent ein: ")) / 100
    

    # Einkommen
    rente_monatlich = float(input("Geben Sie Ihre monatliche Rente (aktuell zu erwartende Rente laut Bescheid RV) ein: "))
    rente = rente_monatlich * 12  # jährliche Rente
    #einkommen_monatlich = float(input("Geben Sie Ihr monatliches Einkommen ein: "))
    #einkommen = einkommen_monatlich * 12  # jährliches Einkommen

    # Rentenanpassungen
    rentenerhoehung_vor_rente = float(input("Geben Sie die jährliche Rentenerhöhung bis zum Renteneintritt in Prozent ein: ")) / 100
    rentenerhoehung_nach_rente = float(input("Geben Sie die jährliche Rentenerhöhung nach dem Renteneintritt in Prozent ein: ")) / 100

    # zusätzliche Einkünfte 
    # Hier können Sie weitere Einkünfte hinzufügen z.B private Renten-, Lebensversicherungen oder andere Einkünfte
    einkuenfte = []
    print("Sie können jetzt weitere Einkünfte, wie private Renten-, Lebensversicherungen oder andere Einkünfte, eingeben.")
    while True:
        name = input("Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): ")
        if name.lower() == 'stop':
            break
        startjahr = int(input(f"Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen {name} erhalten: "))
        startjahr_rente = startjahr
        startwert_mon = float(input(f"Geben Sie die Höhe der monatlichen Zahlung für {name} ein: "))
        startwert = startwert_mon * 12  # jährliche Zahlung
        startwert_rente = startwert
        wachstum = float(input(f"Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für {name} ein: ")) / 100
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