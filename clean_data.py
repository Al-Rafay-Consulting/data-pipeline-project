import pandas as pd

def clean_data(df):
    # remove missing values
    df = df.dropna()

    # remove duplicates
    df = df.drop_duplicates()

    # convert date column if exists
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"])

    return df