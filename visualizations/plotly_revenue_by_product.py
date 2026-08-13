"""Fase 6.1 — een interactieve productgrafiek met Plotly.

Voer uit met: python visualizations/plotly_revenue_by_product.py
Open daarna reports/charts/revenue_by_product.html in je browser.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px


df = pd.read_csv("data/raw/sales_analysis.csv")
df["revenue"] = df["quantity"] * df["price"]

revenue_by_product = (
    df.groupby("product", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

fig = px.bar(
    revenue_by_product,
    x="product",
    y="revenue",
    title="Omzet per product",
    labels={"product": "Product", "revenue": "Omzet (€)"},
    color="product",
    text_auto=".2f",
)
fig.update_layout(showlegend=False)

output_path = Path("reports/charts/revenue_by_product.html")
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.write_html(output_path)

print(f"Interactieve grafiek opgeslagen: {output_path}")
