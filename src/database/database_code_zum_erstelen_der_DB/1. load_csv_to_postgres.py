import psycopg
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(r'C:\Users\Admin\Documents\Projektwoche_SQL\Projektwoche_SQL\.env')

def connect_to_db():
    try:
        connection = psycopg.connect(
            host=os.getenv("host"),
            port=os.getenv("port"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            dbname=os.getenv("dbname"),
            autocommit=True
        )
        print('Verbindung erfolgreich hergestellt')
        return connection
    except Exception as e:
        print(f"Fehler beim Herstellen der Verbindung: {e}")
        return None


def load_csv_to_postgres(csv_files):
    try:
        # Verbindung zur PostgreSQL-Datenbank herstellen
        conn = connect_to_db()
        if conn is None:
            return

        cursor = conn.cursor()
        print("Erfolgreich mit der Datenbank verbunden.")

        # Durch alle CSV-Dateien iterieren
        for file_name in csv_files:
            df = pd.read_csv(file_name)  # Ändere hier von read_excel auf read_csv
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
            print(f"Die Datei '{file_name}' wurde erfolgreich als Tabelle '{table_name}' in die PostgreSQL-Datenbank importiert.")

        conn.commit()
        cursor.close()
        conn.close()
        print("Alle Daten wurden importiert und die Verbindung zur Datenbank wurde geschlossen.")
    except Exception as e:
        print(f"Fehler beim Importieren der Daten: {e}")


# Beispielaufruf
load_csv_to_postgres(
    csv_files=['spotify_songs.csv']
)
