from views.tab import AssetTab
from views.tab import BudgetTab
from tkinter import ttk

import tkinter as tk

root = tk.Tk()
root.title("Personal Finance Toolkit")
tab_control = ttk.Notebook(root)
budget_tab = BudgetTab(tab_control)
asset_tab = AssetTab(tab_control)
tab_control.pack(expand=1, fill="both")
root.mainloop()
