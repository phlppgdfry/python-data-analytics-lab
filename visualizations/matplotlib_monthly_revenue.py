"""Fase 5.1 — een statische lijngrafiek met Matplotlib.

Voer uit met: python visualizations/matplotlib_monthly_revenue.py
"""

from pathlib import Path

import matplotlib
import pandas as pd


# Agg maakt PNG-bestanden zonder een macOS-grafisch venster te openen.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/sales_analysis.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M")

monthly_revenue = df.groupby("month")["revenue"].sum().sort_index()

output_path = Path("reports/charts/monthly_revenue.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 4.5))
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o",
    color="#2563eb",
    linewidth=2,
)
plt.title("Maandelijkse omzet")
plt.xlabel("Maand")
plt.ylabel("Omzet (€)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(output_path, dpi=150)

print(f"Grafiek opgeslagen: {output_path}")
