import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = subjects.merge(students, how="cross")
    df = df.sort_values("student_id")
    subjects = examinations.groupby(["subject_name", "student_id"]).size().reset_index(name='count')
    df = df.merge(subjects, on=["student_id", "subject_name"], how="left")
    df['count'] = df['count'].fillna(0)
    df = df.rename(columns={"count":"attended_exams"})
    df = df[["student_id", "student_name", "subject_name", "attended_exams"]]
    df = df.sort_values(by=["student_id", "subject_name"])
    return df
    