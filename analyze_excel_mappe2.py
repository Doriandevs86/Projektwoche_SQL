import pandas as pd

def analyze_excel(file_path):
    data = pd.read_excel(file_path)

    # Zeige die ersten 5 Zeilen der Daten
    print("Vorschau der Daten:")
    print(data.head(), "\n")

    # Zeige alle Spaltennamen, mit Umbruch nach jeder 10. Spalte
    print("Spaltennamen:")
    columns = data.columns.tolist()
    print(columns[:10])
    print(columns[10:20])
    print(columns[20:30])
    print(columns[30:40])
    print(columns[40:50])
    print(columns[50:60])
    print(columns[60:70])
    print(columns[70:80])
    print(columns[80:90])
    print(columns[90:100])
    print(columns[100:110])
    print(columns[110:120])
    print(columns[120:130])
    print(columns[130:140])
    print(columns[140:150])
    print(columns[150:])

    print("\n")

    # Zeige Informationen über die Spalten (Datentypen und nicht-leere Werte)
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
file_path = "data/database/Mappe2.xlsx"
analyze_excel(file_path)
