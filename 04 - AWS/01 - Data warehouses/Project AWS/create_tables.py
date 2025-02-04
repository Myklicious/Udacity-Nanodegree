import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# drop tables as defined in sql_queries
def drop_tables(cur, conn):
    print('Dropping tables...')
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
    print('Tables dropped.')

# create tables as defined in sql_queries
def create_tables(cur, conn):
    print('Creating tables...')
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
    print('Tables created.')

# generate tables as defined in sql_queries
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    print('Config file read.')
    
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    print('Connection complete.')
    
    drop_tables(cur, conn)
    
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()