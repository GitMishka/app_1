from db.db_utils import connect_db, insert_data_into_db
from services.data_service import fetch_data_from_api

def main():
    # Replace these with your AWS RDS details
    host = "your_aws_rds_host"
    dbname = "your_db_name"
    user = "your_username"
    password = "your_password"
    port = "your_port_number"

    # Replace these with your API details
    api_url = "your_api_url"
    api_key = "your_api_key"

    conn = connect_db(host, dbname, user, password, port)
    if conn is not None:
        data = fetch_data_from_api(api_url, api_key)
        if data is not None:
            insert_data_into_db(conn, data)
        conn.close()

if __name__ == "__main__":
    main()
