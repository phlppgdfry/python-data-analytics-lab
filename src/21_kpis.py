"""Fase 4.1 — kern-KPI's uit schone salesdata berekenen.

Voer eerst de cleaning-pipeline uit: python src/19_clean_data.py
Voer daarna dit bestand uit: python src/21_kpis.py
"""

import pandas as pd


df = pd.read_csv("data/processed/cleaned_sales.csv")

total_revenue = df["revenue"].sum()
order_count = df["order_id"].nunique()
average_order_value = total_revenue / order_count

print("Sales KPI's")
print("-" * 20)
print(f"Totale omzet: €{total_revenue:.2f}")
print(f"Aantal orders: {order_count}")
print(f"Gemiddelde orderwaarde: €{average_order_value:.2f}")
