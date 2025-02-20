# JSON Tests

# Variablen definieren

# Liste der Suchmuster und zugehörigen Versandadressen
apikey_pattern_addresses = [
    ("apikey1", "Suchmuster1", "Versandadresse1","defaultaddresse1"),
    ("apikey2", "Suchmuster2", "Versandadresse2","defaultaddresse2"),
    ("apikey3", "Suchmuster3", "Versandadresse3","defaultaddresse3"),
    # Weitere Muster und Adressen können hier hinzugefügt werden
]

# Textvariable, die untersucht werden soll
text_variable = "Dies ist ein Beispieltext mit Suchmuster1 und anderen Inhalten."



# Funktion zur Suche nach Mustern und Auswahl der Versandadresse
def find_shipping_address(text,key, apikey_pattern_addresses):
    for apikey, pattern, address, default_address in apikey_pattern_addresses:
        if apikey in key:
            if pattern in text:
                return address
            else:
                return default_address
    return "Keine passende Versandadresse gefunden."


mykey="apikey2"

# Versandadresse basierend auf dem Text ermitteln
selected_address = find_shipping_address(text_variable,mykey, apikey_pattern_addresses)

# Ergebnis ausgeben
print(f"Die ausgewählte Versandadresse ist: {selected_address}")