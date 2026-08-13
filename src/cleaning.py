"""Herbruikbare functies voor sales data cleaning."""

import pandas as pd


def clean_sales_data(df):
    """Normaliseer, valideer en verrijk ruwe salesdata."""
    cleaned_df = df.copy()

    cleaned_df["country"] = (
        cleaned_df["country"].str.strip().str.lower().str.title()
    )
    cleaned_df = cleaned_df.drop_duplicates()

    cleaned_df["price"] = pd.to_numeric(
        cleaned_df["price"].astype("string").str.replace(",", ".", regex=False),
        errors="coerce",
    )
    cleaned_df["quantity"] = pd.to_numeric(
        cleaned_df["quantity"],
        errors="coerce",
    )

    cleaned_df = cleaned_df.dropna(subset=["price", "quantity"]).copy()
    cleaned_df["quantity"] = cleaned_df["quantity"].astype(int)
    cleaned_df["revenue"] = cleaned_df["quantity"] * cleaned_df["price"]

    return cleaned_df
