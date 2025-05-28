import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses.drop(columns="student", inplace=True)
    df = courses.groupby("class").size().reset_index(name="count")
    df1 = df[df["count"] >= 5]
    return df1[["class"]]


