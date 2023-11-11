import pandas as pd
import sqlite3


class DatabaseService:
    """
    This class contains logic to interact with the applications database.
    Any database logic that is shared across different models will be configured here.
    """

    def __init__(self, database_config) -> None:
        self.database_file_path = database_config.get("file_path")

    def run_query(self, query, insert_vals=()) -> None:
        """
        Executes a query, but without retrievingany results. 
        Use for DDL statements.
        """
        self.connection = sqlite3.connect(self.database_file_path)
        self.connection.execute(query, insert_vals)
        self.connection.commit()
        self.connection.close()

    def load_query(self, query) -> dict:
        """
        Retrieves data from the database
        """
        self.connection = sqlite3.connect(self.database_file_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        execution = self.cursor.execute(query)
        result_row = execution.fetchone()
        result = dict(result_row)
        self.cursor.close()
        self.connection.close()
        return result
