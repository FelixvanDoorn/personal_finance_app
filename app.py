from tab import Tab
from tkinter import ttk

import tkinter as tk

root = tk.Tk()
root.title("Personal Finance Toolkit")

tab_control = ttk.Notebook(root)
budget_tab = Tab(tab_control, "Monthly Spending")
investing_tab = Tab(tab_control, "Assets")
tab_control.pack(expand=1, fill="both")

root.mainloop()
