class BudgetStatusController:
    """
    This passes query results to the UI for Budget Status.
    """

    def __init__(
            self,
            budget_status_view,
            budget_data_model,
            budget_breakdown
            ) -> None:
        self.budget_status_view = budget_status_view
        self.budget_data_model = budget_data_model
        self.needs_ratio = budget_breakdown["Needs"]
        self.wants_ratio = budget_breakdown["Wants"]
        self.investments_ratio = budget_breakdown["Investments"]

    def load_data(self) -> dict:
        query_result = self.budget_data_model.query_budget_status()
        return query_result

    def update_data(self, data_to_update):
        """
        Retrieves data from budget dict and updates UI labels. 
        """
        income = data_to_update.get("income", 0)
        spend = data_to_update.get("spend", 0)
        spend_needs = data_to_update.get("spend_needs", 0)
        spend_wants = data_to_update.get("spend_wants", 0)
        spend_investments = data_to_update.get("spend_investments", 0)
        needs_balance = round(self.needs_ratio * income - spend_needs, 2)
        wants_balance = round(self.wants_ratio * income - spend_wants, 2)

        investments_balance = round(
            self.investments_ratio * income - spend_investments,
            2
        )

        budget_balance = round(income - spend, 2)
        budget_balance_string = f"Budget Balance: {budget_balance}"
        needs_balance_string = f"Needs Balance: {needs_balance}"
        wants_balance_string = f"Wants Balance: {wants_balance}"

        investments_balance_string = (
            f"Investments Balance: {investments_balance}"
        )

        self.budget_status_view.set_total_budget_value_string(
            budget_balance_string
        )
        
        self.budget_status_view.set_needs_value_string(needs_balance_string)
        self.budget_status_view.set_wants_value_string(wants_balance_string)

        self.budget_status_view.set_investment_value_string(
            investments_balance_string
        )
