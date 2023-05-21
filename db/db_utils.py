import psycopg2

def connect_db(host, dbname, user, password, port):
    conn = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )
        print("Connected to the database")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


def insert_data_into_db(conn, data):
    #implement this function based on your specific table schema
    pass
