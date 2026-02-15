from .extract import extract_from_excel
from .transform import concat_dataframes
from .load import load_excel


def etl_pipeline(input_path: str, output_path: str, output_file_name: str) -> str:
    """
    Function to execute all the steps of the ETL pipeline.

    args:
    input_path (str): file path with the excel files
    output_path (str): the path where the consolidated excel file will be saved
    output_file_name (str): the name of the consolidated excel file

    return:
    "Pipeline executed successfully"
    """
    df_list = extract_from_excel(input_path)
    consolidated_df = concat_dataframes(df_list)
    load_excel(consolidated_df, output_path, output_file_name)

    return print("Pipeline executed successfully.")


if __name__ == "__main__":
    etl_pipeline(
        input_path="../../data/input",
        output_path="../../data/output",
        output_file_name="employee_absence_data",
    )
