import os
import tempfile
import pandas as pd
from app.pipeline.etl import etl_pipeline


def test_integration():
    """
    Validate the ETL pipeline end-to-end by writing a sample Excel input file,
    running the pipeline, and asserting the generated output file exists and
    contains the same data.
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_folder = os.path.join(tmpdirname, "input")
        output_folder = os.path.join(tmpdirname, "output")
        os.makedirs(input_folder)

        test_data = pd.DataFrame({"A": list(range(1, 11)), "B": list("abcdefghij")})
        test_file_path = os.path.join(input_folder, "sample.xlsx")
        test_data.to_excel(test_file_path, index=False)

        etl_pipeline(input_folder, output_folder, "test")

        output_path = os.path.join(output_folder, "test.xlsx")
        assert os.path.exists(output_path)

        loaded_data = pd.read_excel(output_path)
        pd.testing.assert_frame_equal(loaded_data, test_data)
