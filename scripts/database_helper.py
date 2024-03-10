import psycopg2
from psycopg2 import OperationalError

from constants import DB_NAME, USER, PASSWORD, HOST


def execute_query(query: str):
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

        result = None
        if cursor.description is not None:
            result = cursor.fetchall()

        cursor.close()

        return result
    except OperationalError as e:
        print(f"Error: {e}")


def executemany(query: str, params: list[tuple]):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=USER, 
            password=PASSWORD, 
            host=HOST
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.executemany(query, params)

        conn.commit()

        cursor.close()
    except OperationalError as e:
        print(f"Error: {e}")