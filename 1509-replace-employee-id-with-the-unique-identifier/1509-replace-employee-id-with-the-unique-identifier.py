import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, how="left", on="id")
    df = pd.DataFrame({
        "unique_id": df["unique_id"],
        "name": df["name"]
    })
    return df