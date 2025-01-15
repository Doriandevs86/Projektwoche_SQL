-- Tabellen in csv_Dateien Umwandeln --

COPY additional_information
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\additional_information.csv'
WITH (FORMAT CSV, HEADER);

COPY album
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\album.csv'
WITH (FORMAT CSV, HEADER);

COPY artist
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\artist.csv'
WITH (FORMAT CSV, HEADER);

COPY genre
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\genre.csv'
WITH (FORMAT CSV, HEADER);

COPY rating
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\rating.csv'
WITH (FORMAT CSV, HEADER);

COPY rhythmic_features
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\rhythmic_features.csv'
WITH (FORMAT CSV, HEADER);

COPY sound_attributes
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\sound_attributes.csv'
WITH (FORMAT CSV, HEADER);

COPY title
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\title.csv'
WITH (FORMAT CSV, HEADER);

COPY track_information
TO 'C:\Users\Admin\Documents\kursverlauf\08_Datenbanken_und_SQL\Datenbanken\track_information.csv'
WITH (FORMAT CSV, HEADER);