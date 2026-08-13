"""Fase 8.1 — eerste Streamlit sales-dashboard.

Start met: streamlit run dashboard/app.py
"""

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Sales Analytics", page_icon="📊", layout="wide")


@st.cache_data
def load_sales_data():
    """Lees de analyse-data in en voeg analysekolommen toe."""
    df = pd.read_csv("data/raw/sales_analysis.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


df = load_sales_data()

st.title("📊 Sales Analytics")
st.caption("Interactief overzicht van omzet, orders en producten.")

all_countries = sorted(df["country"].unique())
selected_countries = st.sidebar.multiselect(
    "Landen",
    options=all_countries,
    default=all_countries,
)

filtered_df = df[df["country"].isin(selected_countries)]

total_revenue = filtered_df["revenue"].sum()
order_count = filtered_df["order_id"].nunique()
customer_count = filtered_df["country"].nunique()
average_order_value = total_revenue / order_count if order_count else 0

revenue_col, orders_col, countries_col, aov_col = st.columns(4)
revenue_col.metric("Totale omzet", f"€{total_revenue:,.2f}")
orders_col.metric("Aantal orders", order_count)
countries_col.metric("Landen", customer_count)
aov_col.metric("Gemiddelde orderwaarde", f"€{average_order_value:,.2f}")

monthly_revenue = (
    filtered_df.groupby("month", as_index=False)["revenue"]
    .sum()
    .sort_values("month")
)
revenue_by_product = (
    filtered_df.groupby("product", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

monthly_chart = px.line(
    monthly_revenue,
    x="month",
    y="revenue",
    markers=True,
    title="Maandelijkse omzet",
    labels={"month": "Maand", "revenue": "Omzet (€)"},
)
product_chart = px.bar(
    revenue_by_product,
    x="product",
    y="revenue",
    color="product",
    title="Omzet per product",
    labels={"product": "Product", "revenue": "Omzet (€)"},
)
product_chart.update_layout(showlegend=False)

left_column, right_column = st.columns(2)
left_column.plotly_chart(monthly_chart, use_container_width=True)
right_column.plotly_chart(product_chart, use_container_width=True)

st.subheader("Orders")
st.dataframe(
    filtered_df[
        ["order_id", "date", "country", "product", "quantity", "price", "revenue"]
    ],
    use_container_width=True,
    hide_index=True,
)
