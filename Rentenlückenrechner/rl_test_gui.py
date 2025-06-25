import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re

# Die Berechnungsfunktion
def berechne_rentenluecke_gui():
    try:
        # Eingabewerte aus den GUI-Feldern abrufen
        geburtsjahr = int(entry_geburtsjahr.get())
        renteneintrittsalter = int(entry_renteneintrittsalter.get())
        lebensalter = int(entry_lebensende.get())
        ausgaben_monatlich = float(entry_ausgaben.get())
        inflationsrate = float(entry_inflation.get()) / 100
        rente_monatlich = float(entry_rente.get()) * 0.854  # abzüglich Sozialabgaben

        # Berechnungen
        aktuelles_jahr = datetime.now().year
        renteneintritt = geburtsjahr + renteneintrittsalter
        jahre_bis_renteneintritt = renteneintrittsalter - (aktuelles_jahr - geburtsjahr)
        rentenjahre = lebensalter - renteneintrittsalter
        lebensjahre_aktuell = lebensalter - (aktuelles_jahr - geburtsjahr)

        ausgaben = ausgaben_monatlich * 12
        aktuelle_ausgaben = ausgaben * (1 + inflationsrate) ** jahre_bis_renteneintritt

        aktuelles_einkommen = rente_monatlich * 12  # jährliche Rente
        gesamt_einkommen = aktuelles_einkommen

        # Berechnung der Rentenlücke
        for jahr in range(rentenjahre):
            aktuelles_einkommen *= (1 + float(entry_rentenerhoehung_nach_rente.get()) / 100)
            gesamt_einkommen += aktuelles_einkommen

        rentenluecke = aktuelle_ausgaben - gesamt_einkommen

        # Ausgabe der Ergebnisse
        if rentenluecke > 0:
            label_ergebnis.config(text=f"Die Rentenlücke beträgt: {rentenluecke:.2f} Euro.")
        else:
            label_ergebnis.config(text=f"Keine Rentenlücke, Überschuss: {abs(rentenluecke):.2f} Euro.")

    except ValueError as e:
        messagebox.showerror("Fehler", "Bitte stellen Sie sicher, dass alle Eingaben korrekt sind.")
        
# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Rentenlückenrechner")
root.geometry("500x600")

# Erstelle die Eingabefelder und Labels
label_geburtsjahr = tk.Label(root, text="Geben Sie Ihr Geburtsjahr (z.B. 1980):")
label_geburtsjahr.pack()

entry_geburtsjahr = tk.Entry(root)
entry_geburtsjahr.pack()

label_renteneintrittsalter = tk.Label(root, text="Geben Sie Ihr Renteneintrittsalter (z.B. 67):")
label_renteneintrittsalter.pack()

entry_renteneintrittsalter = tk.Entry(root)
entry_renteneintrittsalter.pack()

label_lebensende = tk.Label(root, text="Geben Sie Ihr gewünschtes Lebensende (z.B. 90):")
label_lebensende.pack()

entry_lebensende = tk.Entry(root)
entry_lebensende.pack()

label_ausgaben = tk.Label(root, text="Geben Sie Ihre monatlichen Ausgaben (z.B. 1500):")
label_ausgaben.pack()

entry_ausgaben = tk.Entry(root)
entry_ausgaben.pack()

label_inflation = tk.Label(root, text="Geben Sie die jährliche Inflation in Prozent (z.B. 2):")
label_inflation.pack()

entry_inflation = tk.Entry(root)
entry_inflation.pack()

label_rente = tk.Label(root, text="Geben Sie Ihre monatliche Rente (z.B. 1200):")
label_rente.pack()

entry_rente = tk.Entry(root)
entry_rente.pack()

label_rentenerhoehung_nach_rente = tk.Label(root, text="Geben Sie die jährliche Rentenerhöhung nach Renteneintritt in Prozent (z.B. 2):")
label_rentenerhoehung_nach_rente.pack()

entry_rentenerhoehung_nach_rente = tk.Entry(root)
entry_rentenerhoehung_nach_rente.pack()

# Ergebnis-Label
label_ergebnis = tk.Label(root, text="", fg="blue")
label_ergebnis.pack()

# Button zum Berechnen der Rentenlücke
button_berechnen = tk.Button(root, text="Berechnen", command=berechne_rentenluecke_gui)
button_berechnen.pack()

# Fenster starten
root.mainloop()
