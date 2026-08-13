"""Fase 2.5 — dezelfde groupby-analyse, nu per product.

Voer uit met: python src/16_groupby_products.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales.csv")
df["revenue"] = df["quantity"] * df["price"]

revenue_by_product = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("Omzet per product:")
print(revenue_by_product)
