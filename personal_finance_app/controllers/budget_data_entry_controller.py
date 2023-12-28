class BudgetDataEntryController:
    """
    This is a Controller for the input form.
    It takes data from the form and sends it to the model
    """

    def __init__(
        self,
        data_entry_view,
        budget_data_model,
        budget_status_controller
    ) -> None:
        self.data_entry_view = data_entry_view
        self.budget_data_model = budget_data_model
        self.budget_status_controller = budget_status_controller
        save_button = self.data_entry_view.get_button()
        save_button.configure(command=self.save_data)

    def save_data(self) -> None:
        data_entry_dict = self.data_entry_view.get_data_entry_dict()
        key_list = data_entry_dict.keys()
        saved_data = {key: data_entry_dict[key].get() for key in key_list}
        self.budget_data_model.create_new_transaction(saved_data)
        budget_query_result = self.budget_status_controller.load_data()
        self.budget_status_controller.update_data(budget_query_result)
