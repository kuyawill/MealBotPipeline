import mysql.connector
import pandas as pd
from mysql.connector import Error

def fetch_latest_data_to_dataframe():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            database = "sql_bantaypresyodb",
            user = "",
            password = ""
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
