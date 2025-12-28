import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    earliest = sales.groupby("product_id").min("year")[["year"]].reset_index()
    all_data = sales.merge(right=earliest, on=["product_id", "year"], how="inner")
    df = all_data.drop(columns=["sale_id"]).rename(columns={"year":"first_year"})
    return df