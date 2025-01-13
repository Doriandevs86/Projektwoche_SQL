-- Tabelle "artist" erstellen
CREATE TABLE IF NOT EXISTS artist (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Tabelle "album" erstellen
CREATE TABLE IF NOT EXISTS album (
    album_id SERIAL PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist (artist_id) ON DELETE CASCADE
);

-- Tabelle "genre" erstellen
CREATE TABLE IF NOT EXISTS genre (
    genre_id SERIAL PRIMARY KEY,
    genre VARCHAR(255) NOT NULL,
    subgenre VARCHAR(255) NOT NULL
);

-- Tabelle "title" erstellen
CREATE TABLE IF NOT EXISTS title (
    title_id SERIAL PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    duration_ms VARCHAR (255),
    FOREIGN KEY (artist_id) REFERENCES artist (artist_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE CASCADE
);

-- Tabelle "rating" erstellen
CREATE TABLE IF NOT EXISTS rating (
    rating_id SERIAL PRIMARY KEY,
    title_id INTEGER NOT NULL,
    track_popularity INTEGER NOT NULL,
    FOREIGN KEY (title_id) REFERENCES title (title_id) ON DELETE CASCADE
);

-- Tabelle "rhythmic_features" erstellen
CREATE TABLE IF NOT EXISTS rhythmic_features (
    title_id INTEGER NOT NULL,
    energy FLOAT,
    tempo VARCHAR(255) NOT NULL,
    danceability FLOAT,
    FOREIGN KEY (title_id) REFERENCES title (title_id) ON DELETE CASCADE
);

-- Tabelle "sound_attributes" erstellen
CREATE TABLE IF NOT EXISTS sound_attributes (
    title_id INTEGER NOT NULL,
    speechiness VARCHAR(255) NOT NULL,
    acousticness VARCHAR(255) NOT NULL,
    instrumentalness VARCHAR(255) NOT NULL,
    liveness VARCHAR(255) NOT NULL,
    valence VARCHAR(255) NOT NULL,
    loudness VARCHAR(255) NOT NULL,
    FOREIGN KEY (title_id) REFERENCES title (title_id) ON DELETE CASCADE
);


create table if not exists additional_information(
    title_id integer not null ,
    key text,
    mode text,
    tempo text,
    foreign key(title_id)
        references title(title_id)
        on delete cascade);

create table if not exists track_information(
    titel_id  integer not null ,
    release text,
    foreign key (titel_id) references title(title_id)
        on delete cascade);

