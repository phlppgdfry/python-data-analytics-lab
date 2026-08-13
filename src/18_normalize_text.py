"""Fase 3.2 — tekstwaarden consistent maken.

Voer uit met: python src/18_normalize_text.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales_dirty.csv")

print("Landen vóór cleaning:")
print(df["country"].unique())

df["country"] = (
    df["country"]
    .str.strip()
    .str.lower()
    .str.title()
)

print("\nLanden na cleaning:")
print(df["country"].unique())
