CREATE OR REPLACE FUNCTION create_quelldatei_table() RETURNS void AS $$
BEGIN
    DROP TABLE IF EXISTS Quelldatei;
    CREATE TABLE Quelldatei (
        id SERIAL PRIMARY KEY,
        title TEXT,
        artist TEXT,
        album_single TEXT,
        genre TEXT,
        artist_followers TEXT,
        explicit TEXT,
        album TEXT,
        release_day TEXT,
        track_number TEXT,
        tracks_in_album TEXT,
        duration_ms TEXT,
        genre_new TEXT,
        days_since_release TEXT,
        popu_max TEXT,
        cluster TEXT
    );

    INSERT INTO Quelldatei (title, artist, album_single, genre, artist_followers, explicit, album, release_day,
                            track_number, tracks_in_album, duration_ms, genre_new, days_since_release, popu_max, cluster)
    SELECT "Title",
           "Artist",
           "Album/Single",
           "Genre",
           "Artist_followers",
           "Explicit",
           "Album",
           "Release_date",
           "Track_number",
           "Tracks_in_album",
           "duration_ms",
           "Genre_new",
           "Days_since_release",
           "Popu_max",
           "Cluster"
    FROM "Mappe2";
END;
$$ LANGUAGE plpgsql;
