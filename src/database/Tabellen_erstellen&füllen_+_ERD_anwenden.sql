-- artist Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS artist (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO artist (name)
SELECT DISTINCT track_artist
FROM spotify_songs;

SELECT * FROM artist;



-- genre Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS genre (
    genre_id SERIAL PRIMARY KEY,
    genre VARCHAR(255) NOT NULL,
    subgenre VARCHAR(255) NOT NULL
);

INSERT INTO genre (genre, subgenre)
SELECT DISTINCT spotify_songs.playlist_genre, spotify_songs.playlist_subgenre
FROM spotify_songs;

SELECT * FROM genre;



-- title Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS title (
    title_id SERIAL PRIMARY KEY,
    artist_id INTEGER,
    genre_id INTEGER,
    name VARCHAR(2555),
    duration INTEGER NOT NULL,
    duration_ms TEXT
);

ALTER TABLE title ALTER COLUMN duration TYPE TEXT;
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
LEFT JOIN artist a ON s.track_artist = a.name
LEFT JOIN genre g ON s.playlist_genre = g.genre AND s.playlist_subgenre = g.subgenre;

SELECT * FROM title;



-- album Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS album (
    album_id SERIAL PRIMARY KEY,
    artist_id INTEGER,
    name VARCHAR(255) NOT NULL
);

INSERT INTO album (artist_id, name)
SELECT DISTINCT a.artist_id, s.track_album_name
FROM spotify_songs s
LEFT JOIN artist a ON s.track_album_name = a.name;

SELECT * FROM album;



-- additional_information Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS additional_information (
    title_id INT,
    key VARCHAR(255) NOT NULL,
    mode VARCHAR(255) NOT NULL
);

INSERT INTO additional_information (title_id, key, mode)
SELECT DISTINCT ON (t.title_id) t.title_id, s.key, s.mode
FROM spotify_songs s
JOIN title t ON s.track_name = t.name
ORDER BY t.title_id, s.key, s.mode, s.tempo;

SELECT * FROM additional_information;


-- rating Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS rating (
    rating_id SERIAL PRIMARY KEY,
    title_id INTEGER NOT NULL,
    track_popularity TEXT
);

INSERT INTO rating (title_id, track_popularity)
SELECT DISTINCT ON (t.title_id) t.title_id, s.track_popularity
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM rating;


-- rhythmic_features Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS rhythmic_features (
    title_id INTEGER NOT NULL,
    energy TEXT,
    tempo VARCHAR(255) NOT NULL,
    danceability FLOAT
);

INSERT INTO rhythmic_features (title_id, energy, tempo, danceability)
SELECT DISTINCT ON (t.title_id) t.title_id, CAST(s.energy AS DOUBLE PRECISION), s.tempo, CAST(s.danceability AS DOUBLE PRECISION)
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM rhythmic_features;



-- sound_attributes Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS sound_attributes (
    title_id INTEGER NOT NULL,
    speechiness VARCHAR(255) NOT NULL,
    acousticness VARCHAR(255) NOT NULL,
    instrumentalness VARCHAR(255) NOT NULL,
    liveness VARCHAR(255) NOT NULL,
    valence VARCHAR(255) NOT NULL,
    loudness VARCHAR(255) NOT NULL
);

INSERT INTO sound_attributes (title_id, speechiness, acousticness, instrumentalness, liveness, valence, loudness)
SELECT DISTINCT ON (t.title_id) t.title_id, s.speechiness, s.acousticness, s.instrumentalness, s.liveness, s.valence, s.loudness
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM sound_attributes;



-- Trackinfromation-Tabelle erstellen und füllen
create table if not exists track_information(
    titel_id  integer not null ,
    release text
);

INSERT INTO track_information (titel_id, release)
SELECT DISTINCT ON (t.title_id)t.title_id, s.track_album_release_date
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

SELECT * FROM public.track_information;



-- Fremdschlüsselbeziehungen hinzufügen
ALTER TABLE title
    ADD CONSTRAINT fk_title_artist FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE,
    ADD CONSTRAINT fk_title_genre FOREIGN KEY (genre_id) REFERENCES genre(genre_id) ON DELETE CASCADE;

ALTER TABLE additional_information
    ADD CONSTRAINT fk_additional_information_title FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE;

ALTER TABLE rating
    ADD CONSTRAINT fk_rating_title FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE;

ALTER TABLE rhythmic_features
    ADD CONSTRAINT fk_rhythmic_features_title FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE;

ALTER TABLE sound_attributes
    ADD CONSTRAINT fk_sound_attributes_title FOREIGN KEY (title_id) REFERENCES title(title_id) ON DELETE CASCADE;

ALTER TABLE album
    ADD CONSTRAINT fk_album_artist FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE;

ALTER TABLE track_information
    ADD CONSTRAINT fk_title_id FOREIGN KEY (titel_id) REFERENCES title(title_id)
        ON DELETE CASCADE;



CREATE TABLE IF NOT EXISTS songs AS
SELECT
    track_id,
    track_name,
    track_artist,
    playlist_genre,
    playlist_subgenre,
    track_popularity,
    duration_ms,
    danceability,
    loudness
FROM spotify_songs
WHERE FALSE;



INSERT INTO songs (    track_id,
    track_name,
    track_artist,
    playlist_genre,
    playlist_subgenre,
    track_popularity,
    duration_ms,
    danceability,
    loudness)

SELECT track_id, track_name, track_artist, playlist_genre,
       playlist_subgenre, track_popularity, duration_ms, danceability, loudness
FROM spotify_songs;

