import json
import os
from datetime import datetime

from constants import RAW_DATA_FOLDER, CREATE_QUERY_FOLDER, INSERT_QUERY_FOLDER
from database_helper import execute_query


# raw data
USERS_JSON_PATH = os.path.join(RAW_DATA_FOLDER, "users.json")

# SQL file paths
CREATE_USER_TABLE_SQL_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_user_table.sql")

# Columns - {'signUpSource', 'active', 'lastLogin', '_id', 'state', 'createdDate', 'role'}

def create_user_table():
    with open(CREATE_USER_TABLE_SQL_PATH, "r") as file:
        query = file.read()
        execute_query(query)


def read_users():
    user_records = []
    with open(USERS_JSON_PATH, "r") as file:
        for line in file:
            user = json.loads(line)
            id: str = user["_id"]["$oid"]
            active: bool = user["active"]
            created_date: datetime = datetime.utcfromtimestamp(float(user["createdDate"]["$date"]) / 1000.0)
            last_login: datetime = datetime.utcfromtimestamp(float(user["lastLogin"]["$date"]) / 1000.0) if "lastLogin" in user else None
            role: str = user["role"]
            sign_up_source: str = user["signUpSource"] if "signUpSource" in user else None
            state: str = user["state"] if "state" in user else None
            
            user_record = (id, active, created_date, last_login, role, sign_up_source, state)
            user_records.append(user_record)