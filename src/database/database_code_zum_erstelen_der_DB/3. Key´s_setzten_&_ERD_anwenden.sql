-- Primary Keys setzen
ALTER TABLE album ADD CONSTRAINT pk_album PRIMARY KEY (album_id);
ALTER TABLE artist ADD CONSTRAINT pk_artist PRIMARY KEY (artist_id);
ALTER TABLE genre ADD CONSTRAINT pk_genre PRIMARY KEY (genre_id);
ALTER TABLE title ADD CONSTRAINT pk_title PRIMARY KEY (title_id);
ALTER TABLE rhythmic_features ADD CONSTRAINT pk_rhythmic_features PRIMARY KEY (title_id);
ALTER TABLE sound_attributes ADD CONSTRAINT pk_sound_attributes PRIMARY KEY (title_id);
ALTER TABLE additional_information ADD CONSTRAINT pk_additional_information PRIMARY KEY (title_id);
ALTER TABLE track_information ADD CONSTRAINT pk_track_information PRIMARY KEY (title_id);
ALTER TABLE rating ADD CONSTRAINT pk_rating PRIMARY KEY (title_id);


-- Foreign Keys setzen

ALTER TABLE title
    ADD CONSTRAINT fk_title_artist FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
    ADD CONSTRAINT fk_title_genre FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    ADD CONSTRAINT fk_title FOREIGN KEY (title_id) REFERENCES additional_information(title_id);

 ALTER TABLE rating
      ADD CONSTRAINT fk_rating_title FOREIGN KEY (title_id) REFERENCES title(title_id);

ALTER TABLE artist
    ADD CONSTRAINT fk_artist_album FOREIGN KEY (album_id) REFERENCES album(album_id);

ALTER TABLE additional_information
    ADD CONSTRAINT fk_additional_information_title FOREIGN KEY (title_id) REFERENCES track_information(title_id);

ALTER TABLE track_information
    ADD CONSTRAINT fk_track_information_title FOREIGN KEY (title_id) REFERENCES rhythmic_features(title_id);

ALTER TABLE rhythmic_features
    ADD CONSTRAINT fk_rhythmic_features_title FOREIGN KEY (title_id) REFERENCES sound_attributes(title_id);