from tkinter import ttk

import tkinter as tk


class BudgetStatusView:
    """
    This view will contain all relevant information about budget status.
    It will include status vs target, in total and by category.

    It consists of a number of tkinter String variables.
    These represent relevant categories of budget allocation.
    """

    def __init__(self, tab_frame) -> None:

        self.budget_status_frame = ttk.Frame(
            tab_frame,
            borderwidth=2,
            relief="solid"
        )

        self.total_budget_value_string = tk.StringVar()
        self.needs_value_string = tk.StringVar()
        self.wants_value_string = tk.StringVar()
        self.investment_value_string = tk.StringVar()

        total_budget_label = tk.Label(
            self.budget_status_frame,
            textvariable=self.total_budget_value_string
        )

        total_budget_label.pack()

        needs_budget_label = tk.Label(
            self.budget_status_frame,
            textvariable=self.needs_value_string
        )

        needs_budget_label.pack()

        wants_budget_label = tk.Label(
            self.budget_status_frame,
            textvariable=self.wants_value_string
        )

        wants_budget_label.pack()

        investment_budget_label = tk.Label(
            self.budget_status_frame,
            textvariable=self.investment_value_string
        )

        investment_budget_label.pack()

    def get_budget_status_frame(self) -> ttk.Frame:
        return self.budget_status_frame

    def set_total_budget_value_string(self, budget_value_to_set) -> None:
        self.total_budget_value_string.set(budget_value_to_set)

    def set_needs_value_string(self, needs_value_to_set) -> None:
        self.needs_value_string.set(needs_value_to_set)

    def set_wants_value_string(self, wants_value_to_set) -> None:
        self.wants_value_string.set(wants_value_to_set)

    def set_investment_value_string(self, investment_value_to_set) -> None:
        self.investment_value_string.set(investment_value_to_set)
