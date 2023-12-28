from personal_finance_app.models.budget_data_model import BudgetDataModel
from personal_finance_app.models.db_service import DatabaseService

from scripts.utils import parse_budgetting_spread_sheet, parse_dates

import pandas as pd
import yaml

config_file_path = "config/config.yaml"

# This script imports existing bugetting spreadsheets into DB
# Formatting is specific for what I've been using for a few years.

with open(config_file_path, "r") as file:
    config = yaml.safe_load(file)

database_config = config["database"]

budget_sheet_frame_dict = pd.read_excel(
    "data/raw_data_files/Finances.xlsx",
    sheet_name=None
)

if __name__ == "__main__":
    sheet_name_list = list(budget_sheet_frame_dict.keys())
    relevant_sheet_name_list = [tab for tab in sheet_name_list if "20" in tab]
    test_frame = budget_sheet_frame_dict.get(relevant_sheet_name_list[0])

    parsed_budget_sheet_frame_dict = {
        sheet_name: parse_budgetting_spread_sheet(
            budget_sheet_frame_dict.get(sheet_name)
        )
        for sheet_name in relevant_sheet_name_list
    }

    budget_month_list = parsed_budget_sheet_frame_dict.keys()

    for budget_month in budget_month_list:
        transaction_datestr = parse_dates(budget_month)
        temp_df = parsed_budget_sheet_frame_dict.get(budget_month)
        temp_df.loc[:, "transaction_date"] = transaction_datestr
        parsed_budget_sheet_frame_dict[budget_month] = temp_df

    budget_sheet_frame_list = parsed_budget_sheet_frame_dict.values()
    total_budget_sheet_frame = pd.concat(budget_sheet_frame_list)

    total_budget_sheet_frame = total_budget_sheet_frame.reset_index().drop(
        columns=["index"]
    )
    
    database_service = DatabaseService(database_config)
    budget_data_model = BudgetDataModel(database_service)
    budget_data_model.import_budget_df(total_budget_sheet_frame)
