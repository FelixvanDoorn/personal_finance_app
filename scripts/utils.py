import pandas as pd


def parse_budgetting_spread_sheet(budget_frame: pd.DataFrame) -> pd.DataFrame:
    transactions_df = budget_frame.iloc[8:]
    return transactions_df