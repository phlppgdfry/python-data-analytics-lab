"""Fase 2.3 — een berekende kolom toevoegen aan een DataFrame.

Voer uit met: python src/13_calculated_columns.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales.csv")

df["revenue"] = df["quantity"] * df["price"]

print(df[["product", "quantity", "price", "revenue"]])

total_revenue = df["revenue"].sum()

print(f"\nTotale omzet: €{total_revenue:.2f}")
