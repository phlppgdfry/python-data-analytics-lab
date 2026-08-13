"""Fase 4.3 — een schone dataset met meerdere maanden analyseren.

Voer uit met: python src/23_analyze_multiple_months.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales_analysis.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
    .sort_index()
)

print("Omzet per maand:")
print(monthly_revenue)

print("\nTotale omzet:")
print(f"€{df['revenue'].sum():.2f}")
