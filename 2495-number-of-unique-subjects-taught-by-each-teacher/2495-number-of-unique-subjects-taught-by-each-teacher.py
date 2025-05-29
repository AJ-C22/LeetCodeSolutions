import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher.drop(columns = "dept_id", inplace=True)
    df = teacher.drop_duplicates()
    df = df.drop(columns = "subject_id")
    df = df.groupby("teacher_id").size().reset_index(name="count")
    df = df.rename(columns = {"count" : "cnt"})
    return df