# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL, 
        start_time TIMESTAMP, 
        user_id INT NOT NULL, 
        level VARCHAR, 
        song_id VARCHAR(18), 
        artist_id VARCHAR(18), 
        session_id INT, 
        location VARCHAR, 
        user_agent VARCHAR,
        PRIMARY KEY (songplay_id)
        );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id INT, 
        first_name VARCHAR, 
        last_name VARCHAR, 
        gender VARCHAR, 
        level VARCHAR,
        PRIMARY KEY (user_id)
        );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(18),
        title VARCHAR(120), 
        artist_id VARCHAR(18) NOT NULL, 
        year INT, 
        duration float NOT NULL,
        PRIMARY KEY (song_id)
        );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(18), 
        name VARCHAR(120), 
        location VARCHAR, 
        latitude FLOAT, 
        longitude FLOAT,
        PRIMARY KEY (artist_id)
        );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP, 
        hour INT, day INT, week INT, 
        month INT, year INT, weekday INT,
        PRIMARY KEY (start_time)
        );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
        (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users
        (user_id, first_name, last_name, gender, level)
VALUES
        (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE
SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs
        (song_id, title, artist_id, year, duration)
VALUES
        (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE
SET artist_id = EXCLUDED.artist_id, title = EXCLUDED.title, duration = EXCLUDED.duration;
""")

artist_table_insert = ("""
INSERT INTO artists 
        (artist_id, name, location, latitude, longitude)
VALUES
        (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO UPDATE
SET name = EXCLUDED.name;
""")


time_table_insert = ("""
INSERT INTO time
        (start_time, hour, day, week, month, year, weekday)
VALUES
        (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT
        s.song_id, s.artist_id
FROM
        songs s
        JOIN artists a
        ON s.artist_id = a.artist_id
WHERE
        s.title = %s
        AND a.name = %s
        AND s.duration = %s 
""")
#
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]