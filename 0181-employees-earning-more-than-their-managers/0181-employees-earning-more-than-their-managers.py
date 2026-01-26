import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, left_on="id", right_on="managerId")
    df = df[df["salary_y"] > df["salary_x"]].rename(columns={"name_y":"Employee"})[["Employee"]]
    return df
    
    