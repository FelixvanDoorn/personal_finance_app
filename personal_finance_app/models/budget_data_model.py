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
        Query latest status of budget.
        Retrieves total spend and income, and spend breakdown by category.
        Income breakdown by category comes from a multiplier over total income.
        This does not require any further DB input.
        """
        query_result = self.database_service.load_query_fetch_one_to_dict(
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
              ) AS spend,
              SUM(
                CASE WHEN transaction_category = 'Spending: Needs'
                THEN transaction_amount
                ELSE 0
                END
              ) AS spend_needs,
              SUM(
                CASE WHEN transaction_category = 'Spending: Wants'
                THEN transaction_amount
                ELSE 0
                END
              ) AS spend_wants,
              SUM(
                CASE WHEN transaction_category LIKE '%Investment%'
                THEN transaction_amount
                ELSE 0
                END
              ) AS spend_investments
            FROM
              budget_data
            """
        )

        return query_result
    
    def import_budget_df(self, df) -> None:
        required_cols = [
            'transaction_description',
            'transaction_amount',
            'transaction_date',
            'transaction_category'
            ]   

        try:
            df = df[required_cols]
        except KeyError:
            print("Column not in dataframe")
        
        self.database_service.open_connection()
        db_connection = self.database_service.get_connection()
        df.to_sql(name='budget_data', con=db_connection, if_exists='replace', index=False)
