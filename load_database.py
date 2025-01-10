import sqlite3
import pandas as pd

def load_excel_to_database(database_name, folder_path):
    conn = sqlite3.connect(database_name)

    # Musikdaten von Excel files importieren
    excel_files = ["Mappe2.xlsx", "Musikdaten_Martin_09012025.xlsx"]

    for file_name in excel_files:
        file_path = f"{folder_path}/{file_name}"

        df = pd.read_excel(file_path)
        table_name = file_name.split(".")[0]

        # DataFrame in die SQLite-Datenbank schreiben
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"Die Datei '{file_name}' wurde erfolgreich"
              f" als Tabelle '{table_name}' in die Datenbank '{database_name}' importiert.")

    # Verbindung schließen
    conn.close()
    print("Alle Daten wurden importiert und die Verbindung zur Datenbank wurde geschlossen.")


# Die Funktion aufrufen um DB zu erstellen
load_excel_to_database("musikdaten.db", "data/database")