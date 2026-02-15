from typing import List
import pandas as pd


def concat_dataframes(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function to concat all dataframes from a list into a single dataframe.

    args:
    df_list (List[pd.DataFrame]): a list containing multiple pandas Dataframes

    return:
    a single dataframe
    """
    if not df_list:
        raise ValueError("There are no dataframes to concat.")

    return pd.concat(df_list, axis=0, ignore_index=True)
