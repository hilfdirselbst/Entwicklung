
import matplotlib.pyplot as plt 


# Funktion zur Erstellung der Waage
def draw_scale(expenses, income):
    # Berechnung der Differenz
    difference = income - expenses
    
    # Erstellen der Figuren und Achsen
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Zeichnen der Waagschalen
    ax.barh(['Einnahmen', 'Ausgaben'], [income, expenses], color=['green', 'red'])
    
    # Hinzufügen der Differenzlinie
    ax.axvline(x=income, color='blue', linestyle='--', label='Einnahmen')
    ax.axvline(x=expenses, color='orange', linestyle='--', label='Ausgaben')

    # Setzen der Titel und Beschriftungen
    ax.set_title('Grafische Darstellung der Waage')
    ax.set_xlabel('Betrag')
    ax.legend()

    # Anzeigen der Grafik
    plt.show()

# Abfragen der Zahlen
try:
    expenses = float(input("Bitte geben Sie die Ausgaben ein: "))
    income = float(input("Bitte geben Sie die Einnahmen ein: "))
    draw_scale(expenses, income)
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein.")