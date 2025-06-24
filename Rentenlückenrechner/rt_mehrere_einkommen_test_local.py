import matplotlib.pyplot as plt
import datetime

import funktionen as myfunc

# import matplotlib.pyplot as plt
#import funktionen as myfunc

def berechne_rentenluecke():
    # Benutzereingaben abfragendatetime.datetime.now().year
    aktuelles_alter = int(input("Geben Sie ihr aktuelles Alter ein: "))
    renteneintrittsalter = int(input("Geben Sie das Renteneintrittsalter ein: "))
    lebensende = int(input("Geben Sie Ihr gewünschtes Lebensalter ein: "))
    # Einkünfte abfragen

    einkuenfte = []
    while True:
        name = input("Geben Sie den Namen des Einkommens ein (oder 'stop' zum Beenden): ")
        if name.lower() == 'stop':
            break
        startjahr = (input(f"Geben Sie das Jahr(YYYY) ein ab dem sie das Einkommen {name} erhalten: "))
        startwert = float(input(f"Geben Sie den Startwert für {name} ein: "))
        wachstum = float(input(f"Geben Sie das jährliche Wachstum in Prozent (0 für kein Wachstum) für {name} ein: ")) / 100
        einkuenfte.append((name,startjahr, startwert, wachstum))

    ausgaben = float(input("Geben Sie Ihre jährlichen Ausgaben ein: "))
    renteneintrittsalter = int(input("Geben Sie das Renteneintrittsalter ein: "))
    lebensende = int(input("Geben Sie Ihr gewünschtes Lebensende ein: "))
    jahre_bis_renteneintritt = renteneintrittsalter - 2023  # Aktuelles Jahr als Basis
    inflationsrate = float(input("Geben Sie die jährliche Inflation in Prozent ein: ")) / 100

    monat_ausgaben = float(input("Geben Sie Ihre monatlichen Ausgaben ein: "))
    ausgaben = monat_ausgaben * 12
    aktuelles_jahr = datetime.datetime.now().year
    jahre_bis_renteneintritt = renteneintrittsalter - aktuelles_alter  # Aktuelles Jahr als Basis
    inflationsrate = float(input("Geben Sie ihre persönliche jährliche Inflation in Prozent ein: ")) / 100

    # Listen für die Jahre, Einkünfte und Ausgaben
    jahre = []
    gesamt_einkommen_liste = []
    ausgaben_liste = []

    # Berechnung der Gesamteinkünfte bis zum Renteneintritt
    for jahr in range(jahre_bis_renteneintritt):
        jahre.append(2023 + jahr)
        jahres_einkommen = 0
        for name, startwert, wachstum in einkuenfte:
            startwert *= (1 + wachstum)
            jahres_einkommen += startwert
        gesamt_einkommen_liste.append(jahres_einkommen)

    expenses, total_expense = myfunc.calculate_expenses_with_inflation(aktuelles_jahr,lebensende,monat_ausgaben,inflationsrate)
    
    print(f"Bei monatlichen Ausgaben von {monat_ausgaben} betragen die jährlichen Ausgaben unter Berücksichtigung der Inflation von {inflationsrate}:")
    # for year, expense in expenses:
    #     print(f"{year}: {expense:.2f} €")

    #print(f"\nGesamtausgaben von {aktuelles_alter} bis {lebensende}: {total_expense:.2f} €")

    # Berechnung der Ausgaben und Fortführung nach Renteneintritt
    for jahr in range(lebensende - renteneintrittsalter):
        ausgaben *= (1 + inflationsrate)
        jahres_einkommen = sum(startwert * (1 + wachstum) ** jahre_bis_renteneintritt for name, startwert, wachstum in einkuenfte)
        gesamt_einkommen_liste.append(jahres_einkommen)
        ausgaben_liste.append(ausgaben)

    # Ausgabe initialisieren
    ausgaben_liste = [ausgaben] * jahre_bis_renteneintritt + ausgaben_liste  # Füge Ausgaben bis zum Renteneintritt hinzu

    # Ermittlung der Rentenlücke
    gesamt_einkommen = sum(gesamt_einkommen_liste)
    gesamt_ausgaben = sum(ausgaben_liste)
    rentenluecke = gesamt_ausgaben - gesamt_einkommen

    if rentenluecke > 0:
        print(f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
    else:
        print("Sie haben keine Rentenlücke, Ihre Einkünfte decken die Ausgaben.")

    # Diagramm erstellen
   # plt.figure(figsize=(10, 5))
   # plt.plot(jahre, gesamt_einkommen_liste, label='Gesamteinkommen', color='blue')
   # plt.plot(jahre, ausgaben_liste, label='Ausgaben', color='red')
   # plt.xlabel('Jahr')
   # plt.ylabel('Betrag (Euro)')
   # plt.title('Einkommen und Ausgaben über die Jahre')
   # plt.legend()
   # plt.grid()
   # plt.show()

# Programm ausführen
berechne_rentenluecke()