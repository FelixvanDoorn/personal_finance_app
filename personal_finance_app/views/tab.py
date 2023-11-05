from .budget_data_entry import BudgetDataEntryView
from .budget_status_view import BudgetStatusView
from tkinter import ttk


class Tab:
    """
    Tab forms the foundation of the GUI.
    """

    def __init__(self, tab_controller, tab_name) -> None:
        self.tab_name = tab_name
        self.tab_frame = ttk.Frame(tab_controller)
        tab_controller.add(self.tab_frame, text=self.tab_name)

    def get_tab_frame(self) -> ttk.Frame:
        return self.tab_frame

    def get_tab_name(self) -> str:
        return self.tab_name


class BudgetTab(Tab):
    """
    This will display the parts of the application used for budgetting
    At the moment, this just displays data entry.
    """

    def __init__(self, tab_controller, dropdown_options) -> None:
        super().__init__(tab_controller, "Budget")
        tab_frame = self.get_tab_frame()
        self.data_entry = BudgetDataEntryView(tab_frame, dropdown_options)
        self.budget_status = BudgetStatusView(tab_frame)
        budget_entry_frame = self.data_entry.get_budget_entry_frame()
        budget_status_frame = self.budget_status.get_budget_status_frame()
        budget_entry_frame.grid(row=0, column=0, padx=10, pady=10)
        budget_status_frame.grid(row=0, column=1, padx=10, pady=10)

    def get_data_entry(self) -> BudgetDataEntryView:
        return self.data_entry


class AssetTab(Tab):
    """
    This displays part of the app that is used for managing asset portfolio.
    """

    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Assets")
        tab_frame = self.get_tab_frame()
        tab_name = self.get_tab_name()

        self.label = ttk.Label(
            tab_frame,
            text="Placeholder for %s section" % tab_name
        )
        self.label.pack(padx=10, pady=10)
