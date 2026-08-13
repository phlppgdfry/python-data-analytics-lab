"""Fase 4.2 — omzet per maand analyseren.

Voer eerst de cleaning-pipeline uit: python src/19_clean_data.py
Voer daarna dit bestand uit: python src/22_monthly_revenue.py
"""

import pandas as pd


df = pd.read_csv("data/processed/cleaned_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
    .sort_index()
)

print("Omzet per maand:")
print(monthly_revenue)
