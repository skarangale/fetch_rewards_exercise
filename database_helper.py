import psycopg2
from psycopg2 import OperationalError


DB_NAME = "fetch_rewards"
USER = "postgres"
PASSWORD = "root"
HOST = "localhost"


def execute_query(query):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=USER, 
            password=PASSWORD, 
            host=HOST
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(query)

        cursor.close()
    except OperationalError as e:
        print(f"Error: {e}")
