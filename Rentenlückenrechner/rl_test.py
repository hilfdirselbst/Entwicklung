import matplotlib.pyplot as plt

def berechne_rentenluecke():
    # Benutzereingaben abfragen
    aktuelles_einkommen = float(input("Geben Sie Ihr aktuelles jährliches Einkommen (staatliche Rente, private Renten, etc.) ein: "))
    ausgaben = float(input("Geben Sie Ihre jährlichen Ausgaben ein: "))
    renteneintrittsalter = int(input("Geben Sie Ihr Renteneintrittsalter ein: "))
    lebensende = int(input("Geben Sie Ihr gewünschtes Lebensende ein: "))
    jahre_bis_renteneintritt = renteneintrittsalter - 2023  # Aktuelles Jahr als Basis
    inflationsrate = float(input("Geben Sie die jährliche Inflation in Prozent ein: ")) / 100
    rentenerhoehung_vor_rente = float(input("Geben Sie die jährliche Rentenerhöhung bis zum Renteneintritt in Prozent ein: ")) / 100
    rentenerhoehung_nach_rente = float(input("Geben Sie die jährliche Rentenerhöhung nach dem Renteneintritt in Prozent ein: ")) / 100

    # Listen für die Jahre, Einkünfte und Ausgaben
    jahre = []
    einkuenfte_liste = []
    ausgaben_liste = []

    # Berechnung der Gesamteinkünfte bis zum Renteneintritt
    for jahr in range(jahre_bis_renteneintritt):
        jahre.append(2023 + jahr)
        aktuelles_einkommen *= (1 + rentenerhoehung_vor_rente)
        einkuenfte_liste.append(aktuelles_einkommen)

    # Berechnung der Ausgaben und Fortführung nach Renteneintritt
    for jahr in range(lebensende - renteneintrittsalter):
        ausgaben *= (1 + inflationsrate)
        aktuelles_einkommen *= (1 + rentenerhoehung_nach_rente)  # Rentenerhöhung nach Renteneintritt
        einkuenfte_liste.append(aktuelles_einkommen)  # Einkommen nach Renteneintritt
        ausgaben_liste.append(ausgaben)

    # Ausgabe initialisieren
    ausgaben_liste = [ausgaben] * jahre_bis_renteneintritt + ausgaben_liste  # Füge Ausgaben bis zum Renteneintritt hinzu

    # Ermittlung der Rentenlücke
    gesamt_einkommen = sum(einkuenfte_liste)
    gesamt_ausgaben = sum(ausgaben_liste)
    rentenluecke = gesamt_ausgaben - gesamt_einkommen

    if rentenluecke > 0:
        print(f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
    else:
        print("Sie haben keine Rentenlücke, Ihre Einkünfte decken die Ausgaben.")

    # Diagramm erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(jahre, einkuenfte_liste, label='Einkommen', color='blue')
    plt.plot(jahre, ausgaben_liste, label='Ausgaben', color='red')
    plt.xlabel('Jahr')
    plt.ylabel('Betrag (Euro)')
    plt.title('Einkommen und Ausgaben über die Jahre')
    plt.legend()
    plt.grid()
    plt.show()

# Programm ausführen
berechne_rentenluecke()