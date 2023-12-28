import pandas as pd
import sqlite3


class DatabaseService:
    """
    This class contains logic to interact with the applications database.
    Any database logic that is shared across different models will be configured here.
    """

    def __init__(self, database_config) -> None:
        self.database_file_path = database_config.get("file_path")
        self.connection = sqlite3.connect(self.database_file_path)

    def get_connection(self) -> sqlite3.Connection:
        return self.connection

    def open_connection(self) -> None:
        self.connection = sqlite3.connect(self.database_file_path)
    
    def run_query(self, query, insert_vals=()) -> None:
        """
        Executes a query, but without retrievingany results. 
        Use for DDL statements.
        """
        self.open_connection()
        self.connection.execute(query, insert_vals)
        self.connection.commit()
        self.connection.close()

    def load_query(self, query) -> sqlite3.Cursor:
        """"
        Loads query results from DB
        """
        self.open_connection()
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        execution = self.cursor.execute(query)
        return execution

    def load_query_fetch_one_to_dict(self, query) -> dict:
        """
        Retrieves one row from query execution
        """
        execution = self.load_query(query)
        result_row = execution.fetchone()
        result = dict(result_row)
        self.cursor.close()
        self.connection.close()
        return result

    def load_query_to_df(self, query) -> pd.DataFrame:
        """
        Load data from query into Pandas dataframe.
        """
        execution = self.load_query(query)
        result = pd.DataFrame(execution.fetchall())
        self.cursor.close()
        self.connection.close()
        return result

