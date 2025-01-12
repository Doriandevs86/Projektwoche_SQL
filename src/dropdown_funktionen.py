import psycopg
import pandas as pd
from getpass import getpass
from sqlalchemy.orm import Session
from sqlalchemy import Text, create_engine
from psycopg import connect

# check_in:
def connect_to_db():
    try:
        connection = psycopg.connect(
            host='localhost',
            port='5432',
            user='postgres',
            password='Datacraft',
            dbname='musikdatenbank',
            autocommit=True
        )
        print('Verbindung erfolgreich hergestellt')
        return connection
    except Exception as e:
        print(f"Fehler beim Herstellen der Verbindung: {e}")
        return None


def get_interpreten_from_db(connection, genre, subgenre):
    try:
        with connection.cursor() as cursor:
            # Abfrage der Interpreten basierend auf Genre und Subgenre
            cursor.execute('''
                SELECT DISTINCT track_artist
                FROM "Spotifydata"
                WHERE playlist_genre = %s AND playlist_subgenre = %s;
            ''', (genre, subgenre))
            rows = cursor.fetchall()
            return [f"{row[0]}" for row in rows]
    except Exception as e:
        print(f"Fehler beim Abrufen oder Verarbeiten der Interpreten: {e}")
        return []



def get_genres_from_db(connection):
    try:
        with connection.cursor() as cursor:
            # Abfrage der einzigartigen Künstler
            cursor.execute('''
                SELECT DISTINCT playlist_genre
                FROM "Spotifydata";
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
                SELECT DISTINCT playlist_subgenre
                FROM "Spotifydata"
                WHERE playlist_genre = %s;
            ''', (genre,))
            rows = cursor.fetchall()
            return [f"{row[0]}" for row in rows]
    except Exception as e:
        print(f"Fehler beim Abrufen oder Verarbeiten der Subgenres: {e}")
        return []

