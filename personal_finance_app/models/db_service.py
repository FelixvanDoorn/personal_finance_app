import pandas as pd
import sqlite3


class DatabaseService:
    """
    This class contains logic to interact with the applications database
    Any DB logic that is shared across different models will be configured here
    """

    def __init__(self, database_config):
        self.database_file_path = database_config.get("file_path")

    def run_query(self, query, insert_vals=()) -> None:
        self.connection = sqlite3.connect(self.database_file_path)
        self.connection.execute(query, insert_vals)
        self.connection.commit()
        self.connection.close()

    def load_query_to_dataframe(self, query) -> pd.DataFrame:
        self.connection = sqlite3.connect(self.database_file_path)
        execution = self.connection.execute(query)
        self.connection.close()
        return pd.DataFrame(execution.fetchall())
