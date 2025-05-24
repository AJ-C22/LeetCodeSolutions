import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on = "departmentId", right_on = "id")
    df['rank'] =  df.groupby('departmentId')['salary'].rank(method="dense", ascending=False)
    df = df[df['rank'] == 1]
    df['Department'] = df['name_y']
    df['Employee'] = df['name_x']
    df['Salary'] = df['salary']
    return df[['Department', 'Employee', 'Salary']]