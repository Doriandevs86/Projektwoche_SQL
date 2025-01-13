CREATE TABLE IF NOT EXISTS genre (
genre_id SERIAL PRIMARY KEY,
genre VARCHAR(255) NOT NULL,
subgenre VARCHAR(255) NOT NULL
);

INSERT INTO genre (genre, subgenre)
SELECT DISTINCT playlist_genre, playlist_subgenre
FROM spotify_songs
WHERE playlist_genre IS NOT NULL AND playlist_subgenre IS NOT NULL