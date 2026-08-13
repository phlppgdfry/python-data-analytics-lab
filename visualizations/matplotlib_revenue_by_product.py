"""Fase 5.2 — omzet per product als staafgrafiek.

Voer uit met: python visualizations/matplotlib_revenue_by_product.py
"""

from pathlib import Path

import matplotlib
import pandas as pd


# Agg maakt PNG-bestanden zonder een macOS-grafisch venster te openen.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/sales_analysis.csv")
df["revenue"] = df["quantity"] * df["price"]

revenue_by_product = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

output_path = Path("reports/charts/revenue_by_product.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(7, 4.5))
plt.bar(
    revenue_by_product.index,
    revenue_by_product.values,
    color="#16a34a",
)
plt.title("Omzet per product")
plt.xlabel("Product")
plt.ylabel("Omzet (€)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(output_path, dpi=150)

print(f"Grafiek opgeslagen: {output_path}")
