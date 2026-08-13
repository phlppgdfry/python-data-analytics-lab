"""Fase 2.5 — omzet per land groeperen met Pandas.

Voer uit met: python src/15_groupby.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales.csv")
df["revenue"] = df["quantity"] * df["price"]

revenue_by_country = (
    df.groupby("country")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("Omzet per land:")
print(revenue_by_country)
