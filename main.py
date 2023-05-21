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
    api_url = "https://api.bls.gov/publicAPI/v2/timeseries/data/LAUCN040010000000005"
    api_key = "0b0b20cb-e45b-4ff6-9c4c-234fc5302b5d"

    conn = connect_db(host, dbname, user, password, port)
    if conn is not None:
        data = fetch_data_from_api(api_url, api_key)
        if data is not None:
            insert_data_into_db(conn, data)
        conn.close()

if __name__ == "__main__":
    main()
