"""Fase 3.3 — een eenvoudige sales-cleaning-pipeline.

Voer uit met: python src/19_clean_data.py
"""

from pathlib import Path

import pandas as pd

from cleaning import clean_sales_data


input_path = Path("data/raw/sales_dirty.csv")
output_path = Path("data/processed/cleaned_sales.csv")

df = pd.read_csv(input_path)
print(f"Rijen vóór cleaning: {len(df)}")

df = clean_sales_data(df)

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Rijen na cleaning: {len(df)}")
print(f"Schoon bestand opgeslagen: {output_path}")
print("\nSchone data:")
print(df)
