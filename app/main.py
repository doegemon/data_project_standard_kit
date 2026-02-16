from utils.data_generator import generate_input_files
from pipeline.etl import etl_pipeline


if __name__ == "__main__":
    generate_input_files("data/input", "employee_absence_data", 50)
    etl_pipeline(
        input_path="data/input",
        output_path="data/output",
        output_file_name="employee_absence_data",
    )
