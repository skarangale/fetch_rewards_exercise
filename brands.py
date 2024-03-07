import json
import os

from constants import RAW_DATA_FOLDER, CREATE_QUERY_FOLDER, INSERT_QUERY_FOLDER
from database_helper import execute_query


# raw data
BRANDS_JSON_PATH = os.path.join(RAW_DATA_FOLDER, "brands.json")

# SQL file paths
CREATE_COGS_TABLE_SQL_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_cogs_table.sql")
CREATE_CPGS_TABLE_SQL_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_cpgs_table.sql")
CREATE_BRAND_TABLE_SQL_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_brand_table.sql")

# Columns - {'barcode', 'category', '_id', 'topBrand', 'categoryCode', 'cpg', 'name', 'brandCode'}

def create_brand_table():
    with open(CREATE_COGS_TABLE_SQL_PATH, "r") as file:
        query = file.read()
        execute_query(query)
    with open(CREATE_CPGS_TABLE_SQL_PATH, "r") as file:
        query = file.read()
        execute_query(query)
    with open(CREATE_BRAND_TABLE_SQL_PATH, "r") as file:
        query = file.read()
        execute_query(query)


def read_brands():
    cogs_records = []
    cpgs_records = []
    brand_records = []
    with open(BRANDS_JSON_PATH, "r") as file:
        for line in file:
            brand = json.loads(line)
            id: str = brand["_id"]["$oid"]
            barcode: str = brand["barcode"]
            brand_code: str = brand["brandCode"] if "brandCode" in brand else None
            category: str = brand["category"] if "category" in brand else None
            category_code: str = brand["categoryCode"] if "categoryCode" in brand else None
            cpg = brand["cpg"]
            cogs_id = cpg["$id"]["$oid"] if cpg["$ref"].lower() == "cogs" else None
            cpgs_id = cpg["$id"]["$oid"] if cpg["$ref"].lower() == "cpgs" else None
            name: str = brand["name"]
            top_brand: bool = brand["topBrand"] if "topBrand" in brand else None

            if cogs_id:
                cogs_records.append((cogs_id))
            if cpgs_id:
                cpgs_records.append((cpgs_id))
            brand_record = (id, barcode, brand_code, category, category_code, cogs_id, cpgs_id, name, top_brand)
            brand_records.append(brand_record)
    
