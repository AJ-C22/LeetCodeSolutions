import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema["description"] != "boring") & (cinema["id"] % 2 == 1)]
    df = df.sort_values("rating", ascending=False)
    return df