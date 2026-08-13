"""Fase 2.1 — een eerste Pandas DataFrame.

Voer uit met: python src/11_pandas_dataframe.py
"""

import pandas as pd


sales_data = {
    "order_id": [1, 2, 3],
    "country": ["Belgium", "France", "Belgium"],
    "product": ["Shoes", "Shirt", "Jacket"],
    "quantity": [2, 1, 1],
    "price": [89.99, 49.99, 129.99],
}

df = pd.DataFrame(sales_data)

print(df)
print(f"\nAantal rijen en kolommen: {df.shape}")
print(f"Kolommen: {list(df.columns)}")
