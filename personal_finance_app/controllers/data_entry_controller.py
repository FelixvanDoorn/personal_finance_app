class DataEntryController:
    """
    This is a Controller for the input form
    """
    def __init__(self, name_entry, value_entry, date_entry, type_entry):
        self.name_entry = name_entry
        self.value_entry = value_entry
        self.date_entry = date_entry
        self.type_entry = type_entry

    def save_data(self):
        print("Save Data")
        self.save_data_from_name_entry(self.name_entry)
        self.save_data_from_value_entry(self.value_entry)
        self.save_data_from_date_entry(self.date_entry)
        self.save_data_from_type_entry(self.type_entry)

    def save_data_from_name_entry(self, name_entry):
        name_entered = name_entry.get()
        print(name_entered)

    def save_data_from_value_entry(self, value_entry):
        value_entered = value_entry.get()
        print(value_entered)

    def save_data_from_date_entry(self, date_entry):
        date_entered = date_entry.get()
        print(date_entered)

    def save_data_from_type_entry(self, type_entry):
        type_entered = type_entry.get()
        print(type_entered)
