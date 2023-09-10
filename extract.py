"""
Description: Script to extract data from the csv.
"""
import pandas as pd


def extract():
    """
    Description: Method to read a CSV file.
    Input: None
    Output: data (Pandas Objectdict)
    """
    csv_file = "sales.csv"
    try:
        data = pd.read_csv(csv_file)
    except Exception as FileNotFoundError:
        print("File not found.")
        return None
    return data



