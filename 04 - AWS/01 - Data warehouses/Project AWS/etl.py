import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


#query to load data from S3 to redshift

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()        

#query to insert from staging to dim & fact tables

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print('Configuration file loaded.')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Connected to redshift.')
    
    load_staging_tables(cur, conn)
    print('Loading complete.')
    insert_tables(cur, conn)
    print('Insert complete.')

    conn.close()
    print('Connection closed. \n ETL complete.')


if __name__ == "__main__":
    main()