"""Fase 3.1 — datakwaliteit inspecteren vóór we data aanpassen.

Voer uit met: python src/17_inspect_dirty_data.py
"""

import pandas as pd


df = pd.read_csv("data/raw/sales_dirty.csv")

print("Brondata:")
print(df)

print("\nOntbrekende waarden per kolom:")
print(df.isna().sum())

print(f"\nAantal dubbele rijen: {df.duplicated().sum()}")

print("\nDatatypes en aanwezige waarden:")
df.info()
