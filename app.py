from personal_finance_app.controllers.budget_data_entry_controller import (
    BudgetDataEntryController,
)
from personal_finance_app.controllers.budget_status_controller import (
    BudgetStatusController,
)
from personal_finance_app.models.db_service import DatabaseService
from personal_finance_app.models.budget_data_model import BudgetDataModel
from personal_finance_app.views.tab import AssetTab
from personal_finance_app.views.tab import BudgetTab
from tkinter import ttk

import tkinter as tk
import yaml

config_file_path = "config/config.yaml"

with open(config_file_path, "r") as file:
    config = yaml.safe_load(file)

database_config = config["database"]
ui_dropdown_options = config["user_interface"]["drop_down_options"]

if __name__ == "__main__":
    database_service = DatabaseService(database_config)
    budget_data_model = BudgetDataModel(database_service)
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Personal Finance Toolkit")
    tab_control = ttk.Notebook(root)
    budget_tab = BudgetTab(tab_control, ui_dropdown_options)
    asset_tab = AssetTab(tab_control)
    tab_control.pack(expand=1, fill="both")

    budget_data_entry_controller = BudgetDataEntryController(
        budget_tab.get_data_entry(), budget_data_model
    )

    status_view = budget_tab.get_status_view()
    budget_status_controller = BudgetStatusController(status_view, budget_data_model)

    budget_query_result = budget_status_controller.load_data()
    budget_status_controller.update_data(budget_query_result)

    root.mainloop()
