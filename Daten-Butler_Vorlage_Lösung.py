import pandas as pd
daten = pd.read_csv("sales_messy.csv")
print("Originaldaten:")
daten.info()

# Definiere eine Funktion namens "bereinige_verkaufsdaten", die einen DataFrame namens "daten" entgegennimmt und diesen am Ende wieder zurückgibt.
def bereinige_verkaufsdaten(daten):
    # Fülle fehlende Werte in der Spalte 'Sales' mit dem Wert 0
    daten['Sales'] = daten['Sales'].fillna(0)
    # Konvertiere die Spalte 'Order Date' in ein Datumsformat, ignoriere dabei Fehler
    daten['Order Date'] = pd.to_datetime(daten['Order Date'], errors='coerce')
    
    return daten

# Wende die Funktion auf die geladenen Daten an
saubere_daten = bereinige_verkaufsdaten(daten)
# Überprüfe das saubere Ergebnis
print("\nGereinigte Daten:")
print(saubere_daten.head())
saubere_daten.info()