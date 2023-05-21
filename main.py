from db.db_utils import connect_db, insert_data_into_db
from services.data_service import fetch_data_from_api

def main():

    host = "your_aws_rds_host"
    dbname = "your_db_name"
    user = "your_username"
    password = "your_password"
    port = "your_port_number"

    # API url you want to fetch data from
    api_url = ""

    conn = connect_db(host, dbname, user, password, port)
    if conn is not None:
        data = fetch_data_from_api(api_url)
        if data is not None:
            insert_data_into_db(conn, data)
        conn.close()

if __name__ == "__main__":
    main()
