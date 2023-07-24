from tkinter import ttk


class Tab:
    def __init__(self, tab_controller, tab_name) -> None:
        self.tab_name = tab_name
        self.tab = ttk.Frame(tab_controller)

        self.label = ttk.Label(
            self.tab, text="Placeholder for %s section" % self.tab_name
        )

        self.label.pack(padx=10, pady=10)
        tab_controller.add(self.tab, text=self.tab_name)


class BudgetTab(Tab):
    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Budget")


class AssetTab(Tab):
    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Assets")
