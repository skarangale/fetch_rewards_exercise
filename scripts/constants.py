import os

# Folder paths
RAW_DATA_FOLDER = os.path.join("..", "data")
CREATE_QUERY_FOLDER = os.path.join("sql", "create")
INSERT_QUERY_FOLDER = os.path.join("sql", "insert")
SELECT_QUERY_FOLDER = os.path.join("sql", "select")

# Database credentials
DB_NAME = "fetch_rewards"
USER = "postgres"
PASSWORD = "root"
HOST = "localhost"