# **Project: Data Warehouse**  

## **Introduction**  

In this project, we are assisting Sparkify by moving their processes and data onto the cloud. Historically, their data resides in AWS S3 storage, in a directory of JSON logs on user activityas well as a directory with JSON metadata on the songs in their app. 

This ETL pipeline will extract data from S3 and stages in AWS Redshift, and then transforms the data into a set of fact and dimension tables for analysis.


## **Project Datasets**  

There are two source datasets that reside in S3 which feed the ETL. 


>Song data: s3://udacity-dend/song_data  

>Log data: s3://udacity-dend/log_data  

>Log data json path: s3://udacity-dend/log_json_path.json  

## **Song Dataset**  

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song.  
  
>song_data/A/B/C/TRABCEI128F424C983.json  

>song_data/A/A/B/TRAABJL12903CDCF1A.json  

And below is an example of what a single song file contains (data types are what were assigned in the staging tables):  

    num_songs INTEGER
    artist_id TEXT
    artist_latitude DOUBLE PRECISION
    artist_longitude DOUBLE PRECISION
    artist_location TEXT
    artist_name TEXT
    song_id TEXT
    title TEXT
    duration DOUBLE PRECISION
    year INT,  

## **Log Dataset**  

The log  dataset consists of files stored in JSON format, for example:  

>log_data/2018/11/2018-11-12-events.json  
>log_data/2018/11/2018-11-13-events.json  

With the following information contained in the JSON files (data types are what were assigned in the staging tables):  

    event_id INT IDENTITY(0,1),
    artist TEXT,
    auth TEXT,
    firstName TEXT,
    gender CHAR(1),
    iteminSession INTEGER,
    lastName TEXT
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

## **Schema for Song Play Analysis**  

A STAR schema is utilized to to allow for efficient business analytics. The structure of this schema is described below:  

**Fact Table** 

1. songplays - records in event data associated with song plays i.e. records with page NextSong
- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent  

**Dimension Tables** 

2. users - users in the app
- user_id, first_name, last_name, gender, level
3. songs - songs in music database
- song_id, title, artist_id, year, duration
4. artists - artists in music database
- artist_id, name, location, lattitude, longitude
5. time - timestamps of records in songplays broken down into specific units
- start_time, hour, day, week, month, year, weekday


## **How to Run**  

An active AWS redshift cluster is required to be set up and running, and python for running the associated scripts.

1. Complete required information in dwh.cfg
2. Create tables utilizing the create_tables.py
3. Execute ETL process by running etl.py