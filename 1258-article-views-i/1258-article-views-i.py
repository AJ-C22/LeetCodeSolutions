import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df1 = df[['author_id']]
    df1 = df1.drop_duplicates()
    df1['id'] = df1['author_id']
    return df1[['id']].sort_values("id")
