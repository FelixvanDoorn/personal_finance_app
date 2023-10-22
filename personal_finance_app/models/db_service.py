import pandas as pd
import sqlite3


class DatabaseService:
    """
    This class contains logic to interact with the applications database
    Any DB logic that is shared across different models will be configured here
    """

    def __init__(self, database_config):
        database_file_path = database_config.get("file_path")
        self.connection = sqlite3.connect(database_file_path)

    def run_query(self, query) -> None:
        self.connection.execute(query)

    def load_query_to_dataframe(self, query) -> pd.DataFrame:
        execution = self.run_query(query)
        return pd.DataFrame(execution.fetchall())
