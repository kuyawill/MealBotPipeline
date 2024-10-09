import mysql.connector
import pandas as pd
from mysql.connector import Error

def fetch_latest_data_to_dataframe():
    try:
        connection = mysql.connector.connect(
            host = "localhost", #this localhost database
            database = "dbname", #add your database name
            user = "username", #add your user name
            password = "pass" #add your password name
        )

        if connection.is_connected():
            query = """
                SELECT *
                FROM bantay_presyo
                WHERE Date = (
                    SELECT DISTINCT(Date)
                    FROM bantay_presyo
                    ORDER BY Date DESC
                    LIMIT 1
                );
            """

            df = pd.read_sql(query, connection)
            connection.close()
            return df

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            connection.close()
