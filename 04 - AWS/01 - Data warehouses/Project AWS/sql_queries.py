import configparser
# CONFIGPARSER IS USED TO PULL VALUES FROM CONFIG FILE

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events
(
    event_id INT IDENTITY(0,1),
    artist TEXT,
    auth TEXT,
    firstName TEXT,
    gender CHAR(1),
    iteminSession INTEGER,
    lastName TEXT,
    length DOUBLE PRECISION,
    level CHAR(4),
    location TEXT,
    method CHAR(3),
    page TEXT,
    registration TEXT,
    sessionId INTEGER,
    song TEXT,
    status INTEGER,
    ts BIGINT,
    useragent TEXT,
    userId INT,
    PRIMARY KEY (event_id)
)

""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs
(
    num_songs INTEGER, 
    artist_id TEXT, 
    artist_latitude DOUBLE PRECISION, 
    artist_longitude DOUBLE PRECISION, 
    artist_location TEXT, 
    artist_name TEXT, 
    song_id TEXT, 
    title TEXT, 
    duration DOUBLE PRECISION, 
    year INT,
    PRIMARY KEY (song_id)
)

""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(
    songplay_id INT IDENTITY(0,1), 
    start_time TIMESTAMP, 
    user_id INT,
    level CHAR(4), 
    song_id TEXT, 
    artist_id TEXT, 
    session_id INTEGER, 
    location TEXT, 
    user_agent TEXT,
    PRIMARY KEY (songplay_id)
)

""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(
    user_id INT, 
    first_name TEXT, 
    last_name TEXT, 
    gender CHAR(1), 
    level CHAR(4),
    PRIMARY KEY (user_id)
)

""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(
    song_id TEXT, 
    title TEXT, 
    artist_id TEXT, 
    year INT, 
    duration DOUBLE PRECISION,
    PRIMARY KEY (song_id)
)

""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(
    artist_id TEXT, 
    name TEXT, 
    location TEXT, 
    latitude DOUBLE PRECISION, 
    longitude DOUBLE PRECISION,
    PRIMARY KEY (artist_id)
)

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(
    start_time TIMESTAMP, 
    hour INT, 
    day INT, 
    week INT, 
    month INT, 
    year INT, 
    weekday INT,
    PRIMARY KEY (start_time)
)


""")

# STAGING TABLES

staging_events_copy = ("""
COPY staging_events 
FROM '{}'
credentials 'aws_iam_role={}'
region 'us-west-2'
JSON '{}'
""").format(
            config.get('S3','LOG_DATA'),
            config.get('IAM_ROLE', 'ARN'),
            config.get('S3','LOG_JSONPATH')
            )


staging_songs_copy = ("""
COPY staging_songs 
FROM '{}'
credentials 'aws_iam_role={}'
region 'us-west-2' 
JSON 'auto'
""").format(
            config.get('S3','SONG_DATA'), 
            config.get('IAM_ROLE', 'ARN')
            )

# FINAL TABLES
# https://stackoverflow.com/questions/39815425/how-to-convert-epoch-to-datetime-redshift

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent) 
SELECT  DISTINCT
    TIMESTAMP 'epoch' + e.ts/1000 * INTERVAL '1 second' AS start_time, 
    e.userId, 
    e.level, 
    s.song_id,
    s.artist_id, 
    e.sessionId,
    e.location, 
    e.useragent
FROM staging_events e, staging_songs s
    WHERE e.page = 'NextSong' 
    AND e.song = s.title 
    AND e.artist = s.artist_name 

""")

user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level)
SELECT DISTINCT  
    userId, 
    firstName, 
    lastName, 
    gender, 
    level
FROM staging_events
    WHERE page = 'NextSong'
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration) 
SELECT DISTINCT 
    song_id, 
    title,
    artist_id,
    year,
    duration
FROM staging_songs
WHERE song_id IS NOT NULL
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude) 
SELECT DISTINCT 
    artist_id,
    artist_name,
    artist_location,
    artist_latitude,
    artist_longitude
FROM staging_songs
WHERE artist_id IS NOT NULL
""")

time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday)
SELECT 
    start_time, 
    extract(hour from start_time),
    extract(day from start_time),
    extract(week from start_time), 
    extract(month from start_time),
    extract(year from start_time), 
    extract(dayofweek from start_time)
FROM songplays
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
