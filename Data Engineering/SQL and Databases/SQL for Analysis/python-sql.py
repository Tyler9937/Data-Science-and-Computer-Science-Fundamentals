from pandas._config.config import describe_option
import psycopg2
import pandas as pd


# ElephanteSQL Database Acess
DBNAME = 'zpnhihap'
USER = 'zpnhihap'
PASSWORD = 'ywfAnBkcpbZ8kUNK587DfvymNQJoBfpI'
HOST = 'kashin.db.elephantsql.com'

# Grabbing data to be entered into database
data_path = 'data/mr_beast_youtube_stats.csv'
df = pd.read_csv(data_path)


def connect(DBNAME, USER, PASSWORD, HOST):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

         # Connect to ElephantSQL-hosted PostgreSQL
        conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    return conn


def create_table(conn):
    ''' Creating a table based on data found in the mr beast csv file'''

    # For the purposes of this I will handwrite the sql commands but will use sqlalchemy in future projects
    command = """
        CREATE TABLE mrbeast (
        id           SERIAL PRIMARY KEY,
        title        varchar(500) NOT NULL,
        description  varchar(1000) NOT NULL,
        viewCount    int,
        likeCount    int
        )
        """
    

    try:
        # Connect to ElephantSQL-hosted PostgreSQL
        conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)

        # A "cursor", a structure to iterate over db records to perform queries
        cur = conn.cursor()

        # Execute commands in order
        cur.execute(command)

        # Close communication with the PostgreSQL database server
        cur.close()

        # Commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()


def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cur = conn.cursor()
    try:
        cur.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()

if __name__ == '__main__':
    # Creating the connection to database
    conn = connect(DBNAME, USER, PASSWORD, HOST)

    # Create table
    create_table(conn)

    # dropping rows with nan values
    df.dropna(inplace=True)

    # Inserting data from dataframe --- obviously not optimal but good for demonstration
    for index, row in df.iterrows():
        title = row.title.replace("'", "")
        title = title.replace('"', '')
        description = row.description.replace("'", "")
        description = description.replace('"', '')
        query = "INSERT INTO mrbeast (title, description, viewCount, likeCount) VALUES ('{}', '{}', {}, {})".format(title, description, row.viewCount, row.likeCount)
        single_insert(conn, query)

    # Close the connection
    conn.close()