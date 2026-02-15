import os
import pandas as pd
import pytest
from app.pipeline.extract import extract_from_excel
from app.pipeline.transform import concat_dataframes
from app.pipeline.load import load_excel


df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})


@pytest.fixture
def mock_input_folder(tmpdir):
    """
    Create a temporary input directory with two sample Excel files.
    """
    input_folder = tmpdir.mkdir("input_folder")
    df1.to_excel(input_folder.join("file1.xlsx"), index=False)
    df2.to_excel(input_folder.join("file2.xlsx"), index=False)

    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    """
    Create and return a temporary output directory path.
    """
    return str(tmpdir.mkdir("output_folder"))


def test_extract(mock_input_folder):
    """
    Verifies if the extraction function returns two pandas DataFrames from the input folder.
    """
    extracted_data = extract_from_excel(mock_input_folder)
    assert len(extracted_data) == 2
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_files(tmpdir):
    """
    Verifies if the extraction function raises a ValueError when no Excel files are found.
    """
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(
        ValueError, match="No Excel files found in the specified file path."
    ):
        extract_from_excel(str(empty_folder))


def test_transform():
    """
    Verifies if the transform function combines two DataFrames and preserves the expected columns.
    """
    df_list = [df1, df2]
    consolidated_df = concat_dataframes(df_list)
    assert len(consolidated_df) == 6
    assert list(consolidated_df.columns) == ["A", "B"]


def test_transform_empty_list():
    """
    Verifies if the transform function raises a ValueError when given an empty list.
    """
    empty_list = []
    with pytest.raises(ValueError, match="There are no dataframes to concat."):
        concat_dataframes(empty_list)


def test_load(mock_output_folder):
    """
    Verifies if the load function writes an Excel file and preserves DataFrame contents.
    """
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    output_file_name = "consolidated"
    load_excel(df, mock_output_folder, output_file_name)

    output_path = os.path.join(mock_output_folder, f"{output_file_name}.xlsx")
    assert os.path.exists(output_path)
    loaded_df = pd.read_excel(output_path)

    pd.testing.assert_frame_equal(loaded_df, df)
