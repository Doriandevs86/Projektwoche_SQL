

CREATE TABLE IF NOT EXISTS title (
title_id SERIAL PRIMARY KEY,
artist_id integer,
genre_id integer,
name VARCHAR(255) NOT NULL,
duration INTEGER NOT NULL,
duration_ms INTEGER);

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






