import pandas as pd

def clean_data(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["deal_value"] = (
        df["deal_value"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["close_date"] = pd.to_datetime(df["close_date"], errors="coerce")
    df["month"] = df["close_date"].dt.to_period("M").astype(str)

    df["stage"] = df["stage"].str.strip().str.title()
    df["customer_segment"] = df["customer_segment"].str.strip().str.title()

    df = df.dropna(subset=["deal_value", "close_date"])

    return df
