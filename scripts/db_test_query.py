from personal_finance_app.models.db_service import DatabaseService

import sqlite3 
import yaml

config_file_path = "config/config.yaml"

with open(config_file_path, "r") as file:
    config = yaml.safe_load(file)

database_config = config["database"]
database_service = DatabaseService(database_config)

while True:
    query_string = input()
    df = database_service.load_query_to_df(query_string)
    print(df)


