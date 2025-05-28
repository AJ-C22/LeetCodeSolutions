import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop(columns=["device_id", "games_played"], inplace=True)
    df = activity.groupby(["player_id"])["event_date"].min().reset_index()
    df.rename(columns = {"event_date" : "first_login"}, inplace=True)
    return df 
