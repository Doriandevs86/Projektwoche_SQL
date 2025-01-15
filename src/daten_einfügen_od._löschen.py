import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

# Funktion zum Herstellen der Verbindung
def get_db_connection():
    connection = psycopg.connect(
        host=os.getenv('host'),
        port=os.getenv('port'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        dbname=os.getenv('dbname'),
        autocommit=True
    )
    return connection


# Funktion zum Erstellen der Tabelle
def create_playlist_table():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # SQL zum Erstellen der Tabelle, falls sie noch nicht existiert
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Meine_Playlist (
                    id SERIAL PRIMARY KEY,
                    title_name VARCHAR(255) NOT NULL,
                    artist_name VARCHAR(255) NOT NULL
                );
            """)
            print("Die Tabelle 'Meine_Playlist' wurde erstellt (falls sie nicht bereits existierte).")
    except Exception as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")
    finally:
        connection.close()


# Funktion zum Hinzufügen in die Tabelle
def add_to_playlist():
    title_name = input("Gib den Titel des Songs ein: ").strip()
    artist_name = input("Gib den Namen des Künstlers ein: ").strip()
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Daten in die Tabelle einfügen
            cursor.execute("""
                INSERT INTO Meine_Playlist (title_name, artist_name) 
                VALUES (%s, %s);
            """, (title_name, artist_name))
            print(f"Der Titel '{title_name}' von {artist_name} wurde zur 'Meine_Playlist'-Tabelle hinzugefügt.")
    except Exception as e:
        print(f"Fehler beim Hinzufügen des Titels: {e}")
    finally:
        connection.close()


# AUSFÜHRUNG!
def main():
    create_playlist_table()
    while True:
        action = input("Möchtest du einen Titel hinzufügen? (yes/no): ").strip().lower()
        if action == "yes":
            add_to_playlist()
        elif action == "no":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte 'yes' oder 'no' eingeben.")


# Aufruf der Funktion
if __name__ == "__main__":
    main()
