from tkinter import ttk


class DataEntry:
    """
    This is a container for the visual components used for entering data.
    Core components of each entry are:

    Name: What was the money spent on or where did it come from?
    Value: How much was spent or made?
    Date: When was the money spent or earned?
    """

    def __init__(self, tab_frame) -> None:
        self.name_label = ttk.Label(tab_frame, text="Entry Name")
        self.name_label.pack()
        self.name_entry = ttk.Entry(tab_frame)
        self.name_entry.pack()
        self.value_label = ttk.Label(tab_frame, text="Entry Value")
        self.value_label.pack()
        self.value_entry = ttk.Entry(tab_frame)
        self.value_entry.pack()
        self.date_label = ttk.Label(tab_frame, text="Entry Date")
        self.date_label.pack()
        self.date_entry = ttk.Entry(tab_frame)
        self.date_entry.pack()
        self.type_label = ttk.Label(tab_frame, text="Entry Type")
        self.type_label.pack()
        self.type_entry = ttk.Entry(tab_frame)
        self.type_entry.pack()
