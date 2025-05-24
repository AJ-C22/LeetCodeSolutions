import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products.query("low_fats == 'Y' and recyclable == 'Y'")
    return df[['product_id']]