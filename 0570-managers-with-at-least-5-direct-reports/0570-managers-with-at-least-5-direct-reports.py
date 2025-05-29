import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[["managerId"]]
    df = df.groupby("managerId").size().reset_index(name="count")
    df = df.query("count >= 5")
    employee = employee[employee["id"].isin(df["managerId"])]
    return employee[["name"]]
