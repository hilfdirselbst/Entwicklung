from datetime import datetime

import matplotlib.pyplot as plt

def berechne_rentenluecke():
   # aktuelles Jahr ermitteln
    aktuelles_jahr = datetime.now().year
    print(f"Aktuelles Jahr: {aktuelles_jahr}")
    
    # Benutzereingaben abfragen
    # Zeitrahmen
    geburtsjahr = int(input("Geben Sie Ihr Geburtsjahr (z.B. 1980) ein: "))
    renteneintrittsalter = int(input("Geben Sie Ihr Renteneintrittsalter (z.B. 67) ein: "))
    lebensalter = int(input("Geben Sie Ihr gewünschtes Lebensende (z.B. 90) ein: "))
    jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
    rentenjahre = lebensalter - renteneintrittsalter
    lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr) 
    print(f"Lebensjahre: {lebensjahre_aktuell}")
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


   
   # Listen für die Jahre, Einkünfte und Ausgaben
    jahre = []
    einkommen_liste = []
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
    for jahr in range(rentenjahre):
        aktuelles_einkommen *= (1 + rentenerhoehung_nach_rente)
        einkommen_liste.append(aktuelles_einkommen)
    gesamt_einkommen = sum(einkommen_liste)
    print(f"Summe der Renteneinkünfte innerhalb der Rente: {gesamt_einkommen:.2f} Euro")

    
    # Ausgaben während der Rentenjahre berechnen
    for jahr in range(rentenjahre):
        aktuelle_ausgaben *= (1 + inflationsrate)
        ausgaben_liste.append(aktuelle_ausgaben)           
    gesamt_ausgaben = sum(ausgaben_liste)
    print(f"Summe der Ausgaben innerhalb der Rente: {gesamt_ausgaben:.2f} Euro")
    
    # Berechnung der Rentenlücke
    rentenluecke = gesamt_ausgaben - gesamt_einkommen
    if rentenluecke > 0:
        print(f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
    else:
        print("Sie haben keine Rentenlücke, Ihre Einkünfte decken die Ausgaben.")
      
 
   
    # Berechnung der Gesamteinkünfte bis zum Renteneintritt
  #  for jahr in range(jahre_bis_renteneintritt):
  #      jahre.append(aktuelles_jahr + jahr)
  #      aktuelles_einkommen *= (1 + rentenerhoehung_vor_rente)
  #      einkuenfte_liste.append(aktuelles_einkommen)

    # Berechnung der Ausgaben und Fortführung nach Renteneintritt
  #  for jahr in range(rentenjahre):
  #      ausgaben *= (1 + inflationsrate)
  #      aktuelles_einkommen *= (1 + rentenerhoehung_nach_rente)  # Rentenerhöhung nach Renteneintritt
  #      einkuenfte_liste.append(aktuelles_einkommen)  # Einkommen nach Renteneintritt
  #      ausgaben_liste.append(ausgaben)

    # Ausgabe initialisieren
  #  ausgaben_liste = [ausgaben] * jahre_bis_renteneintritt + ausgaben_liste  # Füge Ausgaben bis zum Renteneintritt hinzu

    # Ermittlung der Rentenlücke
  #  gesamt_einkommen = sum(einkuenfte_liste)
  #  gesamt_ausgaben = sum(ausgaben_liste)
  # rentenluecke = gesamt_ausgaben - gesamt_einkommen

  #  if rentenluecke > 0:
  #      print(f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
  #  else:
  #      print("Sie haben keine Rentenlücke, Ihre Einkünfte decken die Ausgaben.")

    # Diagramm erstellen
  #  plt.figure(figsize=(10, 5))
  #  plt.plot(jahre, einkuenfte_liste, label='Einkommen', color='blue')
  #  plt.plot(jahre, ausgaben_liste, label='Ausgaben', color='red')
  # plt.xlabel('Jahr')
  #  plt.ylabel('Betrag (Euro)')
  #  plt.title('Einkommen und Ausgaben über die Jahre')
  #  plt.legend()
  #  plt.grid()
  #  plt.show()


# Programm ausführen
berechne_rentenluecke()