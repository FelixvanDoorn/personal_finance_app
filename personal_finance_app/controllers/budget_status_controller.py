class BudgetStatusController:
    """
    This passes query results to the UI for Budget Status.
    """

    def __init__(self, budget_status_view, budget_data_model) -> None:
        self.budget_status_view = budget_status_view
        self.budget_data_model = budget_data_model

    def load_data(self) -> dict:
        query_result = self.budget_data_model.query_budget_status()
        return query_result

    def update_data(self, data_to_update):
        income = data_to_update.get("income", "0")
        spend = data_to_update.get("spend", "0")
        budget_balance = income - spend
        self.budget_status_view.set_total_budget_value_string(budget_balance)
