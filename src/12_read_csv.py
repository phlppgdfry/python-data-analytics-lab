"""Fase 2.2 — een CSV-bestand inlezen met Pandas.

Voer uit met: python src/12_read_csv.py
"""

import pandas as pd


file_path = "data/raw/sales.csv"
df = pd.read_csv(file_path)

print(df.head())
print(f"\nVorm (rijen, kolommen): {df.shape}")
print(f"\nKolommen: {list(df.columns)}")
print("\nInformatie over de DataFrame:")
df.info()
