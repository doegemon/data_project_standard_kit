import os
import random
import pandas as pd
from faker import Faker


def generate_fake_data() -> pd.DataFrame:
    """
    Function to generate fake the data to be used in the ETL pipeline.

    return: pandas dataframe
    """

    faker = Faker("pt_BR")

    departments = [
        "Recursos Humanos",
        "Financeiro",
        "Marketing",
        "TI",
        "Vendas",
        "Operacoes",
        "Juridico",
        "Engenharia",
        "Atendimento ao Cliente",
        "P&D",
    ]

    reasons = [
        "Doenca",
        "Problemas pessoais",
        "Consulta medica",
        "Viagem de negocios",
        "Outros",
    ]

    data = {
        "employee_id": [faker.unique.random_number(digits=5) for _ in range(10)],
        "employee_name": [faker.name() for _ in range(10)],
        "department": [faker.random_element(elements=departments) for _ in range(10)],
        "absence_reason": [faker.random_element(elements=reasons) for _ in range(10)],
        "absence_duration": [faker.random_int(min=1, max=8) for _ in range(10)],
        "absence_date": [
            faker.date_between_dates(
                date_start=pd.to_datetime("2023-06-01"),
                date_end=pd.to_datetime("2023-06-30"),
            )
            for _ in range(10)
        ],
        "salary": [round(random.uniform(2000, 10000), 2) for _ in range(10)],  # nosec
    }

    df = pd.DataFrame(data)
    df["absence_date"] = pd.to_datetime(df["absence_date"])

    return df


def generate_input_files(
    input_path: str, input_file_name: str, n_files: int = 10
) -> str:
    """
    Function to generate excel files from pandas dataframe with fake data.

    args: n_files (int): number of files to be generated

    return: "Files created successfully"
    """
    for i in range(n_files):
        df = generate_fake_data()

        if not os.path.exists(input_path):
            os.makedirs(input_path)

        input_file_name_adj = f"{input_file_name}_{i}.xlsx"

        df.to_excel(os.path.join(input_path, input_file_name_adj), index=False)

        print(f"File n. {i} created successfully.")

    return "Files created successfully."


if __name__ == "__main__":
    generate_input_files("../../data/input", "employee_absence_data", 50)
