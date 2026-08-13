"""Fase 6.2 — een interactieve omzettrend met Plotly.

Voer uit met: python visualizations/plotly_monthly_revenue.py
Open daarna reports/charts/monthly_revenue.html in je browser.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px


df = pd.read_csv("data/raw/sales_analysis.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.groupby("month", as_index=False)["revenue"]
    .sum()
    .sort_values("month")
)

fig = px.line(
    monthly_revenue,
    x="month",
    y="revenue",
    title="Maandelijkse omzet",
    labels={"month": "Maand", "revenue": "Omzet (€)"},
    markers=True,
)
fig.update_traces(line_color="#2563eb")

output_path = Path("reports/charts/monthly_revenue.html")
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.write_html(output_path)

print(f"Interactieve grafiek opgeslagen: {output_path}")
