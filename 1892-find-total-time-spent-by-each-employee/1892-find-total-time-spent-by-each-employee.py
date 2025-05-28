import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(["event_day", "emp_id"])[["in_time","out_time"]].sum().reset_index()
    df["total_time"] = df["out_time"] - df["in_time"]
    df.drop(columns=["in_time", "out_time"], inplace=True)
    df.rename(columns= {"event_day" : "day"}, inplace=True)
    return df

