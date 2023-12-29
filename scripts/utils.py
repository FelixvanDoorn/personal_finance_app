from datetime import datetime

import pandas as pd
import re


def add_transaction_categories(budget_category_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Adds transaction categories to dataframe

    Args: budget_category_frame, a pandas Dataframe
    Represents a month of transactions, with categories split by columns
    """
    category_name = budget_category_frame.iloc[0, 0]
    category_name = category_name.replace("Expenses", "Spending:")
    category_name = "Investments" if 'Investment' in category_name else category_name 
    result_frame = budget_category_frame.copy()
    result_frame.columns = ["transaction_description", "transaction_amount"]
    result_frame["transaction_category"] = category_name
    result_frame = result_frame.iloc[1:]
    return result_frame


def parse_budgetting_spread_sheet(budget_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Reads sheets for each month.
    For each individual sheet, parses columns values and categorizes them. 
    Also removes duplicate entries or subtotals.
    """
    transactions_df = budget_frame.iloc[8:].reset_index()
    
    col_pairs = [
        ("Post", "Total Income"),
        ("Investments", "Unnamed: 5"),
        ("Unnamed: 8", "Unnamed: 9"),
        ("Unnamed: 12", "Unnamed: 13"),
    ]

    frame_list = [transactions_df.loc[:, cols] for cols in col_pairs]

    frames_with_transaction_categories = [
        add_transaction_categories(frame) for frame in frame_list
    ]

    unfiltered_total_frame_with_duplicates = pd.concat(frames_with_transaction_categories).dropna()
    unfiltered_total_frame_deduped = unfiltered_total_frame_with_duplicates.reset_index().drop(columns=["index"])
    filtered_total_frame_deduped = unfiltered_total_frame_deduped.query("transaction_description != 'Totaal'")

    return filtered_total_frame_deduped

def find_first_numeric_char_position(datestr: str) -> int:
    str_match = re.search(r'\d', datestr)

    if str_match:
        str_match_index = str_match.start()
    else:
        raise Exception("No numeric values found")
    return str_match_index


def space_datestr(datestr: str, index: int) -> str:
    spaced_datestr = None

    if index < len(datestr):
        if datestr[index-1] == " ":
            spaced_datestr = datestr 
        else:
            spaced_datestr = datestr[:index] + " " + datestr[index:]
    else:
        raise Exception("Cannot space string at this index")
    
    return spaced_datestr
        


def parse_dates(datestr: str) -> str:
    index_to_space = find_first_numeric_char_position(datestr)
    spaced_datestr = space_datestr(datestr, index_to_space)
    date = None

    try:
        date = datetime.strptime(spaced_datestr, "%b %Y")
    except ValueError:
        date = datetime.strptime(spaced_datestr, "%B %Y")

    return date.strftime("%Y-%m-%d")
