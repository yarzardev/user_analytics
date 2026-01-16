import pandas as pd


def active_users(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["active"] == True]


def average_age_by_country(df: pd.DataFrame) -> pd.Series:
    return df.groupby("country")["age"].mean()
