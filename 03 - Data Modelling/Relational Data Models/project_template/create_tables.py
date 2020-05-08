import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    No Return: Create and connect to sparkify database
    
    Parameter(s):
    NA
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    No Return: This drops existing tables from db
    
    Parameter(s):
    cur as conn.cursor()
    conn as psycopg2.connect()
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    No Return: This creates tables in db defined by sql_queries.py
    
    Parameter(s):
    cur as conn.cursor()
    conn as psycopg2.connect()
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    print("Success - Table dropped.")

    create_tables(cur, conn)
    print("Success - Table created.")

    conn.close()


if __name__ == "__main__":
    main()