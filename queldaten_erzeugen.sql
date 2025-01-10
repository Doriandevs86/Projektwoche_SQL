CREATE TABLE IF NOT EXISTS quelldaten (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Artist TEXT,
    Album_Single TEXT,
    Genre TEXT,
    Artist_followers TEXT,
    Explicit TEXT,
    Album TEXT,
    Release_date DATE,
    Track_number INT,
    Tracks_in_album INT,
    duration_ms INT,
    Genre_new TEXT ,
    Days_since_release INT,
    Popu_max INT,
    Cluster TEXT
);

--Daten aus der Tabelle "Mappe2" einfügen
INSERT INTO quelldaten (Title, Artist, Album_Single, Genre, Artist_followers, Explicit, Album, Release_date,
                        Track_number, Tracks_in_album, duration_ms, Genre_new, Days_since_release, Popu_max, Cluster)
SELECT
    Title,
    Artist,
    Album/Single,
    Genre,
    Artist_followers,
    Explicit,
    Album,
    Release_date,
    Track_number,
    Tracks_in_album,
    duration_ms,
    Genre_new ,
    Days_since_release,
    Popu_max,
    Cluster
FROM Mappe2;

--Duplikate entfernen, falls nötig
DELETE FROM quelldaten
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM quelldaten
    GROUP BY Title, Artist, Album_Single, Genre, Artist_followers, Explicit, Album, Release_date,
            Track_number, Tracks_in_album, duration_ms, Genre_new, Days_since_release, Popu_max, Cluster
);

--Let´s Test it!
SELECT * from quelldaten;
