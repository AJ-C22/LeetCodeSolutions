import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.drop(columns="timestamp")
    actor_director = actor_director.groupby(["actor_id", "director_id"]).size().reset_index(name="count")
    actor_director = actor_director.query("count >= 3")
    return actor_director[["actor_id", "director_id"]]