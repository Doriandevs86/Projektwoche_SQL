from psycopg import connect

def get_genres_from_db():
    conn = connect(
        "dbname=musikdaten"
        " user=postgres"
        " password=Datacraft"
        " host=localhost"
        " port=5432")
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT genre_new FROM quelldatei;')
    genres = cursor.fetchall()
    cursor.close()
    conn.close()
    return [genre[0] for genre in genres]

def get_interpreten_from_db():
    conn = connect(
        "dbname=musikdaten"
        " user=postgres"
        " password=Datacraft"
        " host=localhost"
        " port=5432")
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT artist FROM quelldatei;')
    artists = cursor.fetchall()
    cursor.close()
    conn.close()
    return [artist[0] for artist in artists]

def get_rating_from_db():
    conn = connect(
        "dbname=musikdaten"
        " user=postgres"
        " password=Datacraft"
        " host=localhost"
        " port=5432")
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT popu_max FROM quelldatei;')
    ratings = cursor.fetchall()
    cursor.close()
    conn.close()
    return [rating[0] for rating in ratings]