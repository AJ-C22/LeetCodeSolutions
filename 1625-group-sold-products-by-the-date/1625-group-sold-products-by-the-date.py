import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()
    activities = activities.sort_values("product")
    df = activities.groupby("sell_date").agg(','.join).reset_index()
    df["num_sold"] = df["product"].str.split(',').str.len()
    df = pd.DataFrame({
    "sell_date": df["sell_date"],
    "num_sold": df["num_sold"],
    "products": df["product"]
    })

    return df