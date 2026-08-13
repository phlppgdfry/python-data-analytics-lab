"""Fase 2.4 — rijen in een DataFrame filteren.

Voer uit met: python src/14_filter_rows.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales.csv")
df["revenue"] = df["quantity"] * df["price"]

belgium_orders = df[df["country"] == "Belgium"]
expensive_orders = df[df["revenue"] >= 100]

print("Belgische orders:")
print(belgium_orders[["product", "revenue"]])

print("\nOrders met minstens €100 omzet:")
print(expensive_orders[["product", "country", "revenue"]])
