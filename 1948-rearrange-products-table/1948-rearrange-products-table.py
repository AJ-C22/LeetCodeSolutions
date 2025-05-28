import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    reshaped = products.melt(id_vars="product_id", var_name="store", value_name="price")

    # Drop rows where price is NaN
    reshaped = reshaped.dropna(subset=["price"]).reset_index(drop=True)
    return reshaped