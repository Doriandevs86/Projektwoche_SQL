import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

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

def create_playlist_table():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
CREATE TABLE IF NOT EXISTS Meine_Playlist (
                    id SERIAL PRIMARY KEY,
                    title_id INTEGER,
                    track_name VARCHAR(255),
                    track_artist VARCHAR(255),
                    FOREIGN KEY (title_id) REFERENCES title (titel_id) ON DELETE CASCADE
                );
            """)
            print("Die Tabelle 'Meine_Playlist' wurde erstellt (falls sie nicht bereits existierte).")
    except Exception as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")
    finally:
        connection.close()

def title_exists_in_spotify(track_name, track_artist):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) FROM spotify_songs
                WHERE track_name = %s AND track_artist = %s;
            """, (track_name, track_artist))
            result = cursor.fetchone()
            return result[0] > 0
    except Exception as e:
        print(f"Fehler beim Überprüfen des Titels: {e}")
        return False
    finally:
        connection.close()

def add_to_playlist():
    track_name = input("Gib den Titel des Songs ein: ").strip()
    track_artist = input("Gib den Künstler des Songs ein: ").strip()

    if not title_exists_in_spotify(track_name, track_artist):
        print(f"Der Titel '{track_name}' von '{track_artist}' existiert nicht in der Spotify-Datenbank.")
        return

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Meine_Playlist (track_name, track_artist)
                VALUES (%s, %s);
            """, (track_name, track_artist))
            print(f"Der Titel '{track_name}' von '{track_artist}' wurde zur Playlist hinzugefügt.")
    except Exception as e:
        print(f"Fehler beim Hinzufügen des Titels: {e}")
    finally:
        connection.close()

def delete_from_playlist():
    track_name = input("Gib den Titel des Songs ein, den du löschen möchtest: ").strip()
    track_artist = input("Gib den Künstler des Songs ein, den du löschen möchtest: ").strip()

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM Meine_Playlist
                WHERE track_name = %s AND track_artist = %s;
            """, (track_name, track_artist))

            if cursor.rowcount > 0:
                print(f"Der Titel '{track_name}' von '{track_artist}' wurde aus der Playlist gelöscht.")
            else:
                print(f"Der Titel '{track_name}' von '{track_artist}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Löschen des Titels: {e}")
    finally:
        connection.close()

# Hauptprogramm
def main():
    create_playlist_table()
    while True:
        print("\nAktionen:")
        print("1: Titel hinzufügen")
        print("2: Titel löschen")
        print("3: Beenden")
        action = input("Wähle eine Aktion (1/2/3): ")

        if action == "1":
            add_to_playlist()
        elif action == "2":
            delete_from_playlist()
        elif action == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Nur 1, 2 oder 3 du Kasper!")

# Programmstart
if __name__ == "__main__":
    main()