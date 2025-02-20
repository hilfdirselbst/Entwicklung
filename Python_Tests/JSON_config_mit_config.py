# JSON Tests

import json

# Funktion zur Suche nach Mustern und Auswahl der Versandadresse
def find_shipping_address(text, key, apikey_pattern_addresses):
    for apikey, pattern, address in apikey_pattern_addresses:
        if apikey == key:  # Prüfen, ob der API-Schlüssel übereinstimmt
            if pattern in text:  # Prüfen, ob das Muster im Text vorkommt
                return address
    return "Keine passende Versandadresse gefunden."

# JSON-Datei laden
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# Variablen aus der JSON-Datei
apikey_pattern_addresses = config["data"]
text_variable = config["text_variable"]

# API-Schlüssel (kann zur Laufzeit definiert werden)
mykey = config["sendgrid_api_key"]

# Anzahl der zu prüfenden Datensätze
my_error_count = config["error_count"]

# Versandadresse basierend auf dem Text und API-Schlüssel ermitteln
selected_address = find_shipping_address(text_variable, mykey, apikey_pattern_addresses)

# Ergebnis ausgeben
print(f"Die ausgewählte Versandadresse ist: {selected_address}")


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