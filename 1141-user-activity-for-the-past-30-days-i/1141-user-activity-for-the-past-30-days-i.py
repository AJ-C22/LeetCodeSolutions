import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[(activity["activity_date"] <= "2019-07-27") & (activity["activity_date"] > "2019-06-27")]
    df = df[["user_id", "activity_date"]]
    df = df.drop_duplicates()
    df = df.groupby("activity_date")["user_id"].count().reset_index().rename(columns={"activity_date":"day", "user_id":"active_users"})
    return df
    