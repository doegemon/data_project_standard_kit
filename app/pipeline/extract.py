import glob
import os
import pandas as pd
from typing import List


def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Function to read Excel files from a specific folder, convert them to pandas Dataframes, and append these dataframes into a list.

    args:
    input_path (str): file path with the Excel files

    return:
    list with multiple pandas Dataframes
    """
    files = glob.glob(os.path.join(input_path, "*.xlsx"))

    if not files:
        raise ValueError("No Excel files found in the specified file path.")
    df_list = [pd.read_excel(file) for file in files]

    return df_list


if __name__ == "__main__":
    dataframe_list = extract_from_excel("../../data/input")
    print(dataframe_list)
