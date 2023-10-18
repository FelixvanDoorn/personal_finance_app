from personal_finance_app.controllers.spending_data_entry_controller import (
    SpendingDataEntryController,
)
from personal_finance_app.views.tab import AssetTab
from personal_finance_app.views.tab import BudgetTab
from tkinter import ttk

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Personal Finance Toolkit")
    tab_control = ttk.Notebook(root)
    budget_tab = BudgetTab(tab_control)
    asset_tab = AssetTab(tab_control)
    tab_control.pack(expand=1, fill="both")

    spend_data_entry_controller = SpendingDataEntryController(
        budget_tab.get_data_entry()
    )
    root.mainloop()
