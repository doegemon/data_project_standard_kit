import os
import pandas as pd


def load_excel(df: pd.DataFrame, output_path: str, output_file_name: str) -> str:
    """
    Function to convert a single dataframe to an excel file.

    args:
    df (pd.DataFrame): pandas dataframe to be converted to excel
    output_path (str): the path where the excel will be saved
    output_file_name (str): the name of the excel file

    return: "File saved successfully"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    df.to_excel(os.path.join(output_path, output_file_name), index=False)

    return "File saved successfully"
