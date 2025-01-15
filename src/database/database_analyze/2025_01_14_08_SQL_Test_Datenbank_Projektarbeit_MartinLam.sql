-- Durchschnittliche Popularität aller Tracks:
SELECT AVG(CAST(track_popularity AS FLOAT)) AS avg_popularity FROM rating;

-- Häufigkeit von Popularitätsstufen:
SELECT track_popularity,
       COUNT(*) AS count
FROM rating
GROUP BY track_popularity
ORDER BY count DESC;

--Top 5 Tracks nach Popularität (falls Popularität numerisch ist
SELECT MIN(r.title_id) AS title_id, -- Beispielhaft eine beliebige ID wählen
       MAX(CAST(r.track_popularity AS FLOAT)) AS track_popularity,
       t.name
FROM rating r
JOIN title t ON r.title_id = t.title_id
GROUP BY t.name
ORDER BY track_popularity DESC
LIMIT 15;

-- Top 5 Jahre mit den meisten Veröffentlichungen
SELECT
    EXTRACT(YEAR FROM TO_DATE(release, 'YYYY-MM-DD')) AS release_year,
    COUNT(*) AS count
FROM
    track_information
GROUP BY
    release_year
ORDER BY
    count DESC
LIMIT 5;

-- Top 5 loudest Tracks:

WITH ranked_titles AS (
    SELECT
        so.title_id,
        CAST(so.loudness AS DOUBLE PRECISION) AS loudness,
        t.name,
        ROW_NUMBER() OVER (PARTITION BY t.name ORDER BY CAST(so.loudness AS DOUBLE PRECISION) DESC) AS row_num
    FROM
        sound_attributes so
    JOIN
        title t ON so.title_id = t.title_id
)
SELECT  title_id,
        loudness,
        name
FROM ranked_titles
WHERE row_num = 1
ORDER BY loudness DESC
LIMIT 5;


-- 18. Änderung der Popularität bei instrumentalen Songs im Zeitverlauf
SELECT
    EXTRACT(YEAR FROM TO_DATE(release, 'YYYY-MM-DD')) AS release_year,
    AVG(CAST(track_popularity AS DOUBLE PRECISION)) AS avg_popularity
FROM
    track_information ti
JOIN
    sound_attributes sa ON ti.titel_id = sa.title_id
JOIN
    rating r ON ti.titel_id = r.title_id
WHERE
    CAST(instrumentalness AS DOUBLE PRECISION) > 0.5
GROUP BY
    release_year
ORDER BY
    release_year;








