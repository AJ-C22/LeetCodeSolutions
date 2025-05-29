import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders["order_number"].count() == 0:
        return orders[['customer_number']]
    orders = orders.drop(columns="order_number")
    df = orders.groupby("customer_number").size().reset_index(name = "count")
    m = max(df['count'])
    df = df.query('count == @m')
    return df[['customer_number']]
