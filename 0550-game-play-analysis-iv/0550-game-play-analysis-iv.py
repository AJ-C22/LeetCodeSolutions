import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by=["player_id", "event_date"])[["player_id", "event_date"]]
    df["date_num"] = df.groupby("player_id")["event_date"].rank()
    df["date_prev"] = df.groupby('player_id')["event_date"].shift()
    df["date_diff"] = (df["event_date"] - df["date_prev"]).dt.days
    df = df.query("date_diff == 1 and date_num == 2")

    target = len(df)
    total = len(activity.groupby("player_id")["player_id"].nunique())
    print(total)
    df = pd.DataFrame({
        "fraction": round(target/total,2)
    }, index=[0])
    return df