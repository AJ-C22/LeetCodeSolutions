import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, how="left", left_on="departmentId", right_on="id")
    df = df[["name_x","name_y","salary"]].sort_values(by=["name_y", "salary"], ascending=False)
    df["salary_rank"] = df.groupby("name_y")["salary"].rank(ascending=False, method="dense")
    df = df[df["salary_rank"] <= 3].rename(columns={"name_x":"Employee", "name_y":"Department", "salary":"Salary"})
    df = df[["Department","Employee","Salary"]]
    return df