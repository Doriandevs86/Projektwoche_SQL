import psycopg
import pandas as pd


def load_excel_to_postgres(database_name, host, user, password, port, excel_files):
    try:
        # Verbindung zur PostgreSQL-Datenbank herstellen
        conn = psycopg.connect(
            dbname=database_name, host=host, user=user, password=password, port=port
        )
        cursor = conn.cursor()

        print(f"Erfolgreich mit der Datenbank '{database_name}' verbunden.")

        # Durch alle Excel-Dateien iterieren
        for file_name in excel_files:
            df = pd.read_excel(file_name)
            table_name = file_name.split(".")[0]

            # Erstelle Tabelle, wenn sie nicht existiert
            column_names = df.columns
            columns_with_types = ", ".join([f'"{col}" TEXT' for col in column_names])
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS "{table_name}" (
                    {columns_with_types}
                );
            """
            cursor.execute(create_table_query)

            # Daten einfügen
            for _, row in df.iterrows():
                # Bereinige Sonderzeichen in den Daten
                values = [
                    str(val).replace("'", "''") if isinstance(val, str) else str(val)
                    for val in row
                ]
                values = ", ".join([f"'{val}'" for val in values])

                insert_query = f"""
                    INSERT INTO "{table_name}" ({', '.join([f'"{col}"' for col in column_names])})
                    VALUES ({values});
                """
                cursor.execute(insert_query)

            print(
                f"Die Datei '{file_name}' wurde erfolgreich als Tabelle '{table_name}' in die PostgreSQL-Datenbank '{database_name}' importiert.")

        # Änderungen speichern und Verbindung schließen
        conn.commit()
        cursor.close()
        conn.close()
        print("Alle Daten wurden importiert und die Verbindung zur Datenbank wurde geschlossen.")

    except Exception as e:
        print(f"Fehler beim Importieren der Daten: {e}")


# Beispielaufruf
load_excel_to_postgres(
    database_name="musikdaten",
    host="localhost",
    user="postgres",
    password="Datacraft",
    port="5432",
    excel_files=["Mappe2.xlsx", "Musikdaten_Martin_09012025.xlsx"]
)
