import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'])
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    df = employee.query('rank == @N')
    df[f'getNthHighestSalary({N})'] = df['salary']

    return df[[f'getNthHighestSalary({N})']] if not df.empty else pd.DataFrame({f'getNthHighestSalary({N})': [None]})