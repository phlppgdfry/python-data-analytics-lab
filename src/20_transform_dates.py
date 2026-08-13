"""Fase 3.4 — tekst omzetten naar datums en maanden.

Voer eerst de cleaning-pipeline uit: python src/19_clean_data.py
Voer daarna dit bestand uit: python src/20_transform_dates.py
"""

import pandas as pd


df = pd.read_csv("data/processed/cleaned_sales.csv")

print("Datatype vóór de omzetting:")
print(df["date"].dtype)

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

print("\nDatatype na de omzetting:")
print(df["date"].dtype)

print("\nDatum en maand per order:")
print(df[["order_id", "date", "month", "revenue"]])
