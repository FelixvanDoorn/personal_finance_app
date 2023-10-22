import sqlite3


class DatabaseService:
    def __init__(self, database_config):
        database_file_path = database_config.get("file_path")
        connection = sqlite3.connect(database_file_path)
