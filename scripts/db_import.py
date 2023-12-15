from utils import parse_budgetting_spread_sheet

import pandas as pd


budget_sheet_frame_dict = pd.read_excel(
    "data/raw_data_files/Finances.xlsx", sheet_name=None
)

sheet_name_list = list(budget_sheet_frame_dict.keys())
relevant_sheet_name_list = [tab for tab in sheet_name_list if "20" in tab]
test_frame = budget_sheet_frame_dict.get(relevant_sheet_name_list[0])

parsed_budget_sheet_frame_dict = {
    sheet_name: parse_budgetting_spread_sheet(budget_sheet_frame_dict.get(sheet_name))
    for sheet_name in relevant_sheet_name_list
}


print(parsed_budget_sheet_frame_dict)