# **Readme text for Project: Data Modeling with Postgres**

## **Description taken from Udacity course:**
  
### **Introduction**
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.  

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.  
  
### **Project Description**
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.  


## **1.) Purpose of database in context of startup, Sparkify**  
The startup company Sparkify wants to analyze the data they've collected on songs and user activity for their music streaming app. At the start of the project, there is not an easy way to query their information, which resides in several directories with JSON logs and metadata for the user activity and songs in their app. This project is to create an ETL pipeline to make it simple to query information and analyze the data.  

## **2.) Database Schema design and ETL Pipeline**  

A star schema will be generated for this dataset, optimized to query for song play analysis. This denormalized set up allows for quick querying of data, joining together song, artists, and user information based off the song plays from various users.  

The schema is described in detail below:  
 
## ***Fact Table***  

### **songplays**  

This table serves as a fact table, and creates a log of all song plays where the `page` is set to `NextSong`    

- songplay_id `SERIAL` *as* **primary key**
- start_time `TIMESTAMP`
- user_id `INT` NOT NULL
- level `VARCHAR`
- song_id `VARCHAR(18)`
- artist_id `VARCHAR(18)`
- session_id `INT`
- location `VARCHAR`
- user_agent `VARCHAR`

## ***Dimension Tables***  

### **users**  
users in app  
- user_id `INT` *as*  **primary key**
- first_name `VARCHAR`
- last_name `VARCHAR`
- gender `VARCHAR`
- level `VARCHAR`

### **songs**  
songs in music database  
- song_id `VARCHAR` *as* **primary key**
- title `VARCHAR(120)`
- artist_id `VARCHAR` not null
- year `INT`
- duration `FLOAT`

### **artists**  
artists in music database  
- artist_id `VARCHAR(18)` *as* **primary key**
- name `VARCHAR(120)`
- location `VARCHAR`
- latitude `FLOAT`
- longitude `FLOAT`

### **time**  
timestamps for records in `songplays` broken down into specific units
- start_time `TIMESTAMP` *as*  **primary key**
- hour `INT`
- day `INT`
- week `INT`
- month `INT`
- year `INT`
- weekday `INT`

The ETL pipeline developed will read the JSON files and automatically transcribe all the values into their respective SQL tables.

## **Instructions for running scripts**  

To run the associated queries, navigate to the terminal application of your choice and change to the project directory

    python create_tables.py

This command will clear existing, and re-generate appropriate tables

    python etl.py

This command will run through the associated log and song data to populate tables

The included test.ipynb jupyter notebook can be used verify that the data populated correctly.

## **File Repository Explanation**  

all raw data on log files and song files are contained within the `./data` folder  

- the `create_tables.py` script will generate clean set of tables  

- the `etl.pynb` jupyter notebook was used for the generation and testing of the ELTL script  

- the `elt.py` script grabs song and play data from the data folder and populates tables  

- the `test.ipynb` notebook can be used to validate the quality of the transfer

- the `sql_queries.py` script contains the SQL queries for `create_tables.py`