from .data_entry import DataEntry
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

    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Budget")
        tab_frame = self.get_tab_frame()
        self.data_entry = DataEntry(tab_frame)



class AssetTab(Tab):
    """
    This displays part of the app that is used for managing asset portfolio.
    """

    def __init__(self, tab_controller) -> None:
        super().__init__(tab_controller, "Assets")
        tab_frame = self.get_tab_frame()
        tab_name = self.get_tab_name()
        self.label = ttk.Label(tab_frame, text="Placeholder for %s section" % tab_name)
        self.label.pack(padx=10, pady=10)
