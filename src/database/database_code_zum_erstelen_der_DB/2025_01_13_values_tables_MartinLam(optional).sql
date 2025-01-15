-- Daten in die Tabelle artist einfügen (nur Künstlernamen)
INSERT INTO artist (name)
SELECT DISTINCT track_artist FROM spotify_songs;

Select * FROM artist;

-- Daten in die Tabelle album einfügen
INSERT INTO album (artist_id, name)
SELECT DISTINCT
    a.artist_id,
    s.track_album_name
FROM spotify_songs s
JOIN artist a ON s.track_album_name = a.name;

SELECT * FROM album;

-- Daten in die Tabelle genre einfügen
INSERT INTO genre (genre, subgenre)
SELECT DISTINCT spotify_songs.playlist_genre, spotify_songs.playlist_subgenre
FROM spotify_songs;

SELECT * FROM genre;


DELETE FROM title;

ALTER TABLE title
ALTER COLUMN name TYPE VARCHAR(5000);

ALTER TABLE title ALTER COLUMN duration TYPE TEXT;

-- Daten in die Tabelle title einfügen, Dauer in Minuten:Sekunden berechnen
INSERT INTO title (artist_id, genre_id, name, duration, duration_ms)
SELECT
    a.artist_id,
    g.genre_id,
    s.track_name,
    -- Berechnung der Dauer in Minuten:Sekunden (Format: MM:SS)
    TO_CHAR(FLOOR(CAST(s.duration_ms AS INTEGER) / 60000), 'FM00') || ':' ||
    TO_CHAR(FLOOR((CAST(s.duration_ms AS INTEGER) % 60000) / 1000), 'FM00') AS duration,  -- Minuten:Sekunden
    CAST(s.duration_ms AS INTEGER) AS duration_ms  -- Umwandlung von Text in Integer
FROM spotify_songs s
JOIN artist a ON s.track_artist = a.name
JOIN genre g ON s.playlist_genre = g.genre AND s.playlist_subgenre = g.subgenre;

SELECT * FROM title;

ALTER TABLE rating
    alter column track_popularity TYPE TEXT;

-- Daten in die Tabelle rating einfügen
INSERT INTO rating (title_id, track_popularity)
SELECT t.title_id, s.track_popularity
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM rating;


ALTER TABLE rhythmic_features
    alter column energy TYPE TEXT;
ALTER TABLE rhythmic_features
    alter column danceability TYPE TEXT;

-- Daten in die Tabelle rhythmic_features einfügen
INSERT INTO rhythmic_features (title_id, energy, tempo, danceability)
SELECT t.title_id, s.energy, s.tempo, s.danceability
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM rhythmic_features;

-- Daten in die Tabelle sound_attributes einfügen
INSERT INTO sound_attributes (title_id, speechiness, acousticness, instrumentalness, liveness, valence, loudness)
SELECT t.title_id, s.speechiness, s.acousticness, s.instrumentalness, s.liveness, s.valence, s.loudness
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM sound_attributes;


-- Daten in die Tabelle additional_information einfügen
INSERT INTO additional_information (title_id, key, mode, tempo)
SELECT t.title_id, s.key, s.mode, s.tempo
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM additional_information;

-- Daten in die Tabelle track_information einfügen
INSERT INTO track_information (titel_id, release)
SELECT t.title_id, s.track_album_release_date
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM public.track_information;



SELECT track_name,
-- Berechnung der Dauer in Minuten:Sekunden (Format: MM:SS)
    TO_CHAR(FLOOR(CAST(duration_ms AS INTEGER) / 60000), 'FM00') || ':' ||
    TO_CHAR(FLOOR((CAST(duration_ms AS INTEGER) % 60000) / 1000), 'FM00') AS duration,  -- Minuten:Sekunden
    CAST(duration_ms AS INTEGER) AS duration_ms  -- Umwandlung von Text in Integer
FROM spotify_songs
