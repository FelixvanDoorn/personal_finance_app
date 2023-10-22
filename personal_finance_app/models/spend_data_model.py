class SpendDataModel:
    def __init__(self, database_service):
        self.database_service = database_service
        self.database_service.run_query(
            """
            CREATE TABLE IF NOT EXISTS spending_data(
                transaction_id INTEGER PRIMARY KEY,
                transaction_description TEXT NOT NULL,
                transaction_amount DOUBLE NOT NULL,
                transaction_date DATE NOT NULL,
                transaction_category TEXT
            );
            """
        )
