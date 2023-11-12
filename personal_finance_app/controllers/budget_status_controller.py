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
        income = data_to_update.get("income", 0)
        spend = data_to_update.get("spend", 0)

        spend_needs = data_to_update.get("spend_needs", 0)

        spend_wants = data_to_update.get("spend_wants", 0)
        spend_investments = data_to_update.get("spend_investments", 0)

        needs_balance = self.needs_ratio * income - spend_needs
        wants_balance = self.wants_ratio * income - spend_wants

        investments_balance = (
            self.investments_ratio * income - spend_investments
            )
        budget_balance = income - spend
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
