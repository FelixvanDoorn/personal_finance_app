class SpendDataModel:
    def __init__(self, database_service):
        self.database_service = database_service
        self.database_service.run_query(
            """
            CREATE TABLE IF NOT EXISTS spending_data(
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_description TEXT NOT NULL,
                transaction_amount DOUBLE NOT NULL,
                transaction_date DATE NOT NULL,
                transaction_category TEXT
            );
            """
        )

    def create_new_transaction(self, data_to_save):
        transaction_description_value = data_to_save.get("name", "")
        transaction_amount_value = data_to_save.get("value", "")
        transaction_date_value = data_to_save.get("date", "")
        transaction_type_value = data_to_save.get("type", "")

        self.database_service.run_query(
            f"""
            INSERT INTO spending_data(
                transaction_description,
                transaction_amount,
                transaction_date,
                transaction_category
            )
            VALUES (
                '{transaction_description_value}',
                {transaction_amount_value},
                {transaction_date_value},
                '{transaction_type_value}'
            );
            """
        )
