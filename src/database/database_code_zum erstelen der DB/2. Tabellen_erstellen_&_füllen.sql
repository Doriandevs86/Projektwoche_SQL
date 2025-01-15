-- artist Tabelle erstellen
CREATE TABLE IF NOT EXISTS artist (
    artist_id SERIAL,
    album_id INTEGER ,
    name VARCHAR(255)
);

-- genre Tabelle erstellen
CREATE TABLE IF NOT EXISTS genre (
    genre_id SERIAL,
    genre VARCHAR(255) NOT NULL,
    subgenre VARCHAR(255) NOT NULL
);

-- title Tabelle erstellen
CREATE TABLE IF NOT EXISTS title (
    title_id SERIAL,
    artist_id INTEGER,
    genre_id INTEGER,
    name VARCHAR(2555),
    duration INTEGER NOT NULL,
    duration_ms TEXT
);

-- album Tabelle erstellen
CREATE TABLE IF NOT EXISTS album (
    album_id SERIAL,
    name VARCHAR(255)
);

-- additional_information Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS additional_information (
    title_id INT,
    key VARCHAR(255) NOT NULL,

    mode VARCHAR(255) NOT NULL
);

-- rating Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS rating (
    title_id SERIAL ,
    track_popularity TEXT
);

-- rhythmic_features Tabelle erstellen und füllen
CREATE TABLE IF NOT EXISTS rhythmic_features (
    title_id INTEGER NOT NULL,
    energy TEXT,
    tempo VARCHAR(255) NOT NULL,
    danceability FLOAT
);

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

-- Track_infromation-Tabelle erstellen und füllen
create table if not exists track_information(
    title_id  integer not null ,
    release text
);



-- fill Table --

INSERT INTO artist (name)
SELECT DISTINCT  track_artist
FROM spotify_songs;

INSERT INTO genre (genre, subgenre)
SELECT DISTINCT spotify_songs.playlist_genre, spotify_songs.playlist_subgenre
FROM spotify_songs;

INSERT INTO title (artist_id, genre_id, name, duration, duration_ms)
SELECT
    a.artist_id,
    g.genre_id,
    s.track_name,
    TO_NUMBER(s.duration_ms, '999999999') / 60000 AS duration,  -- Dauer in Sekunden als Integer
    TO_NUMBER(s.duration_ms, '999999999') AS duration_ms
FROM spotify_songs s
LEFT JOIN artist a ON s.track_artist = a.name
LEFT JOIN genre g ON s.playlist_genre = g.genre AND s.playlist_subgenre = g.subgenre;


INSERT INTO album (name)
SELECT DISTINCT s.track_album_name
FROM spotify_songs s
LEFT JOIN artist a ON s.track_album_name = a.name;

INSERT INTO additional_information (title_id, key, mode)
SELECT DISTINCT ON (t.title_id) t.title_id, s.key, s.mode
FROM spotify_songs s
JOIN title t ON s.track_name = t.name
ORDER BY t.title_id, s.key, s.mode, s.tempo;

INSERT INTO rating (title_id, track_popularity)
SELECT DISTINCT ON (t.title_id) t.title_id, s.track_popularity
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

INSERT INTO rhythmic_features (title_id, energy, tempo, danceability)
SELECT DISTINCT ON (t.title_id) t.title_id, CAST(s.energy AS DOUBLE PRECISION), s.tempo, CAST(s.danceability AS DOUBLE PRECISION)
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

INSERT INTO sound_attributes (title_id, speechiness, acousticness, instrumentalness, liveness, valence, loudness)
SELECT DISTINCT ON (t.title_id) t.title_id, s.speechiness, s.acousticness, s.instrumentalness, s.liveness, s.valence, s.loudness
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;

INSERT INTO track_information (title_id, release)
SELECT DISTINCT ON (t.title_id)t.title_id, s.track_album_release_date
FROM spotify_songs s
JOIN title t ON s.track_name = t.name;