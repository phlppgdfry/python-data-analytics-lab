"""Fase 3.3 — een eenvoudige sales-cleaning-pipeline.

Voer uit met: python src/19_clean_data.py
"""

from pathlib import Path

import pandas as pd


input_path = Path("data/raw/sales_dirty.csv")
output_path = Path("data/processed/cleaned_sales.csv")

df = pd.read_csv(input_path)
print(f"Rijen vóór cleaning: {len(df)}")

# Maak categorische tekstwaarden consistent.
df["country"] = df["country"].str.strip().str.lower().str.title()

# Verwijder exacte dubbele rijen.
df = df.drop_duplicates()

# Zet Europese komma's om en maak ongeldige getallen ontbrekend (NaN).
df["price"] = pd.to_numeric(
    df["price"].str.replace(",", ".", regex=False),
    errors="coerce",
)
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Een order zonder prijs of aantal kan geen betrouwbare omzet krijgen.
df = df.dropna(subset=["price", "quantity"])
df["quantity"] = df["quantity"].astype(int)

df["revenue"] = df["quantity"] * df["price"]

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Rijen na cleaning: {len(df)}")
print(f"Schoon bestand opgeslagen: {output_path}")
print("\nSchone data:")
print(df)
