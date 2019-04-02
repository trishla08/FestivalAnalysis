import pandas as pd
from datetime import datetime


def fix_columns(df):
    return df.rename(columns={"Timestamp": "timestamp",
                "Roll Number": "roll",
                "Name": "name",
                "Username": "email",
                "Contact Number": "contact",
                "Have you registered in another department for Moksha 2019?": "other"})


def get_branch(roll):
    return roll[5:7].upper()


def get_year(roll):
    return roll[:4]


def get_date(timestamp):
    date = timestamp[:10]

    return datetime.strptime(date, "%Y/%m/%d").date()


def fix_df(df):
    df = fix_columns(df)
    columns = ["timestamp", "email", "name", "roll", "contact"]
    df["branch"] = df["roll"].apply(get_branch)
    df["year"] = df["roll"].apply(get_year)
    df["date"] = df["timestamp"].apply(get_date)
    df = df.drop(columns, axis=1)

    return df
