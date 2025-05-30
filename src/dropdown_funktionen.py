import psycopg
import os
from flask.cli import load_dotenv


load_dotenv(r'C:\Users\Admin\Desktop\Projektwoche_SQL\.env')

# check_in:
def connect_to_db():
    try:
        connection = psycopg.connect(
            host=os.getenv("host") ,
            port=os.getenv("port") ,
            user=os.getenv("user") ,
            password=os.getenv("password"),
            dbname=os.getenv("dbname"),
            autocommit=True
        )
        print('Verbindung erfolgreich hergestellt')
        return connection
    except Exception as e:
        print(f"Fehler beim Herstellen der Verbindung: {e}")
        return None



def get_genres_from_db(connection):
    try:
        with connection.cursor() as cursor:
            # Abfrage der einzigartigen Künstler
            cursor.execute('''
                SELECT DISTINCT genre
                FROM "genre";
            ''')
            rows = cursor.fetchall()
            return [f"{row[0]}" for row in rows]
    except Exception as e:
        print(f"Fehler beim Abrufen oder Verarbeiten der Künstler: {e}")
        return []


def get_subgenres_from_db(connection, genre):
    try:
        with connection.cursor() as cursor:
            # Hole die Subgenres basierend auf dem Genre
            cursor.execute('''
                SELECT DISTINCT subgenre
                FROM "genre"
                WHERE genre = %s;
            ''', (genre,))
            rows = cursor.fetchall()
            return [f"{row[0]}" for row in rows]
    except Exception as e:
        print(f"Fehler beim Abrufen oder Verarbeiten der Subgenres: {e}")
        return []


def get_interpreten_from_db(connection, genre, subgenre):
    try:
        with connection.cursor() as cursor:
            # Abfrage aller Interpreten, die nicht im ausgewählten Genre und Subgenre vorkommen
            cursor.execute('''
                SELECT DISTINCT a.name
                FROM "artist" a
                WHERE a.artist_id NOT IN (
                    SELECT t.artist_id
                    FROM "title" t
                    INNER JOIN "genre" g ON t.genre_id = g.genre_id
                    WHERE g.genre = %s AND g.subgenre = %s
                );
            ''', (genre, subgenre))
            rows = cursor.fetchall()
            return [f"{row[0]}" for row in rows]
    except Exception as e:
        print(f"Fehler beim Abrufen oder Verarbeiten der nicht-assoziierten Interpreten: {e}")
        return []
