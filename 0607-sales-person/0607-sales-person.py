import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.merge(company, on="com_id", how="left")
    orders = orders.merge(sales_person, on="sales_id", how="left")
    orders = orders[['com_id', 'name_x','sales_id', 'name_y']]
    orders = orders.query("name_x == 'RED'")
    sales_person = sales_person[~sales_person['sales_id'].isin(orders["sales_id"])]
    return sales_person[['name']]