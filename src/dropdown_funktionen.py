import psycopg
import pandas as pd
from getpass import getpass
from sqlalchemy.orm import Session
from sqlalchemy import Text, create_engine
from psycopg import connect

# # check_in:
# pw = getpass('Please enter password: ')
# connection_url = f'postgresql://postgres:{pw}@localhost:5432/musikdatenbank'
# engine = create_engine(connection_url)
#
# # check connection:
# with engine.connect() as conn_alchemy:
#     print("SQLAlchemy connected!")
#
#
# # connection psycopg:
# pw = getpass('Please enter password: ')
# with psycopg.connect(
#     host='localhost',
#     port='5432',
#     user='postgres',
#     password=pw,
#     dbname='musikdatenbank',
#     autocommit=True
# ) as connection:
#     print("psycopg connected!")


def get_genres_from_db():
    try:
        # Verbindung zur Datenbank herstellen
        with psycopg.connect(
            host='localhost',
            port='5432',
            user='postgres',
            password='Datacraft',
            dbname='musikdatenbank',
            autocommit=True
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT DISTINCT playlist_genre, playlist_subgenre FROM "Spotifydata" group by playlist_genre, playlist_subgenre;')
                genres = cursor.fetchall()

                return [genre for genre in genres]
    except Exception as e:
        print(f"Fehler beim Abrufen der Genres: {e}")
        return []
get_genres_from_db()

#def get_genres_from_db():
#    try:
#        # Verbindung mit SQLAlchemy zur richtigen Datenbank herstellen
#        with engine.connect() as connection:
#            result = connection.execute('SELECT DISTINCT "playlist_genre" FROM public."Spotifydata";')
#            genres = [row[0] for row in result]
#            return genres
#    except Exception as e:
#        print(f"Fehler beim Abrufen der Genres: {e}")
#        return []
#get_genres_from_db()
#
#def get_interpreten_from_db():
#    conn = connect(
#        "dbname=musikdatenbank"
#        " user=postgres"
#        " password=Datacraft"
#        " host=localhost"
#        " port=5432")
#    cursor = conn.cursor()
#    cursor.execute('SELECT DISTINCT track_artist FROM "Spotifydata";')
#    artists = cursor.fetchall()
#    cursor.close()
#    conn.close()
#    return [artist[0] for artist in artists]
#print('Funktion läuft')
#
#def get_rating_from_db():
#    conn = connect(
#        "dbname=musikdatenbank"
#        " user=postgres"
#        " password=Datacraft"
#        " host=localhost"
#        " port=5432")
#    cursor = conn.cursor()
#    cursor.execute('SELECT DISTINCT track_popularity FROM "Spotifydata";')
#    ratings = cursor.fetchall()
#    cursor.close()
#    conn.close()
#    return [rating[0] for rating in ratings]
#print('Funktion läuft')
#
#
## Einfachere Abfrage, nur um zu prüfen, ob eine grundlegende SQL-Abfrage funktioniert
#with engine.connect() as connection:
#    result = connection.execute('SELECT * FROM "Spotifydata";')
#    for row in result:
#        print(row)
#
#%%
