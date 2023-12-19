from utils import parse_budgetting_spread_sheet, parse_dates

import pandas as pd

# This script imports existing bugetting spreadsheets into DB
# Formatting is specific for what I've been using for a few years. 

budget_sheet_frame_dict = pd.read_excel(
    "data/raw_data_files/Finances.xlsx",
    sheet_name=None
)

sheet_name_list = list(budget_sheet_frame_dict.keys())
relevant_sheet_name_list = [tab for tab in sheet_name_list if "20" in tab]
test_frame = budget_sheet_frame_dict.get(relevant_sheet_name_list[0])

parsed_budget_sheet_frame_dict = {
    sheet_name: parse_budgetting_spread_sheet(budget_sheet_frame_dict.get(sheet_name))
    for sheet_name in relevant_sheet_name_list
}

budget_month_list = parsed_budget_sheet_frame_dict.keys()

for budget_month in budget_month_list:
    transaction_datestr = parse_dates(budget_month)
    temp_df = parsed_budget_sheet_frame_dict.get(budget_month)
    temp_df.loc[:, "transaction_date"] = transaction_datestr
    parsed_budget_sheet_frame_dict[budget_month] = temp_df

budget_sheet_frame_list = parsed_budget_sheet_frame_dict.values()
total_budget_sheet_frame = pd.concat(budget_sheet_frame_list).reset_index().drop(columns=["index"])

print(total_budget_sheet_frame.tail())