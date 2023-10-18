from personal_finance_app.controllers.spending_data_entry_controller import (
    SpendingDataEntryController,
)
from tkinter import ttk

import tkinter as tk


class SpendingDataEntryView:
    """
    This is a container for the visual components used for entering data.
    Core components of each entry are:

    Name: What was the money spent on or where did it come from?
    Value: How much was spent or made?
    Date: When was the money spent or earned?
    """

    def __init__(self, tab_frame) -> None:
        self.name_var = tk.StringVar()
        self.value_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.type_var = tk.StringVar()
        self.name_label = ttk.Label(tab_frame, text="Entry Name")
        self.name_label.pack()
        self.name_entry = ttk.Entry(tab_frame, textvariable=self.name_var)
        self.name_entry.pack()
        self.value_label = ttk.Label(tab_frame, text="Entry Value")
        self.value_label.pack()
        self.value_entry = ttk.Entry(tab_frame, textvariable=self.value_var)
        self.value_entry.pack()
        self.date_label = ttk.Label(tab_frame, text="Entry Date")
        self.date_label.pack()
        self.date_entry = ttk.Entry(tab_frame, textvariable=self.date_var)
        self.date_entry.pack()
        self.type_label = ttk.Label(tab_frame, text="Entry Type")
        self.type_label.pack()
        self.type_entry = ttk.Entry(tab_frame, textvariable=self.type_var)
        self.type_entry.pack()
        self.save_button = ttk.Button(tab_frame, text="Save")
        self.save_button.pack()

    def get_button(self):
        return self.save_button

    def get_name_entry(self):
        return self.name_entry

    def get_value_entry(self):
        return self.value_entry

    def get_date_entry(self):
        return self.date_entry

    def get_type_entry(self):
        return self.type_entry

    def get_data_entry_dict(self):
        self.entry_dict = {
            "name": self.get_name_entry(),
            "value": self.get_value_entry(),
            "date": self.get_date_entry(),
            "type": self.get_type_entry(),
        }

        return self.entry_dict
