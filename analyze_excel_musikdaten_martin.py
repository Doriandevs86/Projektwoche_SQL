import pandas as pd

def analyze_excel(file_path):
    data = pd.read_excel(file_path)

    # Zeige die ersten 5 Zeilen der Daten
    print("Vorschau der Daten:")
    print(data.head(), "\n")

    # Zeige alle Spaltennamen
    print("Spaltennamen:")
    columns = data.columns.tolist()
    print(columns[:10])
    print(columns[10:20])
    print(columns[20:30])
    print("\n")
    
    # Zeige Informationen über die Spalten
    print("Spalteninformationen:")
    data.info()
    print("\n")

    # Überprüfe, wie viele fehlende Werte (NaN, 0, 'null') es in jeder Spalte gibt
    print("Anzahl der fehlenden Werte pro Spalte (inklusive NaN, 0 und 'null'):")
    null_counts = (data.isnull() | (data == 0) | (data == 'null')).sum()
    print(null_counts, "\n")

    # Gesamtanzahl der fehlenden Werte
    total_null_values = null_counts.sum()
    print(f"Gesamtanzahl fehlender Werte: {total_null_values}\n")

    # Zeige grundlegende statistische Informationen
    print("Statistische Übersicht (nur für numerische Spalten):")
    print(data.describe(), "\n")

# Pfad zur Excel-Datei angeben und Script ausführen
file_path = "data/database/Musikdaten_Martin_09012025.xlsx"
analyze_excel(file_path)
