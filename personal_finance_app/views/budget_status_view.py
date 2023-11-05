from tkinter import ttk

import tkinter as tk


class BudgetStatusView:
    """
    This view will contain all relevant information about budget status.
    It will include status vs target, in total and by category.
    """

    def __init__(self, tab_frame) -> None:
        self.budget_status_frame = ttk.Frame(tab_frame, borderwidth=2, relief="solid")
        self.total_budget_value_string = tk.StringVar()
        self.needs_budget_value_string = tk.StringVar()
        self.wants_budget_value_string = tk.StringVar()
        self.investments_budget_value_string = tk.StringVar()
        total_budget_label = tk.Label(self.budget_status_frame, textvariable=self.total_budget_value_string)

    def get_budget_status_frame(self) -> ttk.Frame:
        return self.budget_status_frame
