class BudgetDataModel:
    """
    This models Budget Data in the app.
    Current reponsibility is to insert budget data into the database
    """

    def __init__(self, database_service) -> None:
        self.database_service = database_service
        self.database_service.run_query(
            """
            CREATE TABLE IF NOT EXISTS budget_data(
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_description TEXT NOT NULL,
                transaction_amount DOUBLE NOT NULL,
                transaction_date DATE NOT NULL,
                transaction_category TEXT
            );
            """
        )

    def create_new_transaction(self, data_to_save) -> None:
        """Inserts a new transaction entry."""
        transaction_description_value = data_to_save.get("name", "")
        transaction_amount_value = data_to_save.get("value", "")
        transaction_date_value = data_to_save.get("date", "")
        transaction_type_value = data_to_save.get("type", "")

        self.database_service.run_query(
            """
            INSERT INTO budget_data(
                transaction_description,
                transaction_amount,
                transaction_date,
                transaction_category
            )
            VALUES (?, ?, ?, ?);
            """,
            insert_vals=(
                transaction_description_value,
                transaction_amount_value,
                transaction_date_value,
                transaction_type_value,
            ),
        )

    def query_budget_status(self) -> dict:
        """
        Query latest status of budget
        """
        query_result = self.database_service.load_query(
            """
            SELECT
              SUM(
                CASE WHEN transaction_category = 'Income'
                THEN transaction_amount
                ELSE 0
                END
              ) AS income,
              SUM(
                CASE WHEN transaction_category <> 'Income'
                THEN transaction_amount
                ELSE 0
                END
              ) AS spend
            FROM
              budget_data
            """
        )

        return query_result
