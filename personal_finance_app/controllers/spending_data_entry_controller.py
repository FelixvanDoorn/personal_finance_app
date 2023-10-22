class SpendingDataEntryController:
    """
    This is a Controller for the input form.
    It takes data from the form and sends it to the model
    """

    def __init__(self, data_entry_view):
        self.data_entry_view = data_entry_view
        save_button = self.data_entry_view.get_button()
        save_button.configure(command=self.save_data)

    def save_data(self):
        data_entry_dict = self.data_entry_view.get_data_entry_dict()
        key_list = data_entry_dict.keys()
        saved_data = {key: data_entry_dict[key].get() for key in key_list}
