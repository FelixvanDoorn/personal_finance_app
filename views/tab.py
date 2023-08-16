from controller import save_data
from tkinter import ttk


class Tab:
    def __init__(self, tab_controller, tab_name) -> None:
        self.tab_name = tab_name
        self.tab_frame = ttk.Frame(tab_controller)
        tab_controller.add(self.tab_frame, text=self.tab_name)

    def get_tab_frame(self) -> ttk.Frame:
        return self.tab_frame

    def get_tab_name(self) -> str:
        return self.tab_name


class BudgetTab(Tab):
    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Budget")
        tab_frame = self.get_tab_frame()
        self.expense_name_label = ttk.Label(tab_frame, text="Expense Name")
        self.expense_name_label.pack()
        self.expense_name_entry = ttk.Entry(tab_frame)
        self.expense_name_entry.pack()
        self.expense_value_label = ttk.Label(tab_frame, text="Expense Value")
        self.expense_value_label.pack()
        self.expense_value_entry = ttk.Entry(tab_frame)
        self.expense_value_entry.pack()
        self.save_button = ttk.Button(tab_frame, text="Save", command=save_data)
        self.save_button.pack()


class AssetTab(Tab):
    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Assets")
        tab_frame = self.get_tab_frame()
        tab_name = self.get_tab_name()
        self.label = ttk.Label(tab_frame, text="Placeholder for %s section" % tab_name)
        self.label.pack(padx=10, pady=10)
