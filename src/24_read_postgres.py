"""Fase 7.4 — PostgreSQL-queryresultaten als Pandas DataFrame lezen.

Vereist een draaiende lokale PostgreSQL-server met de analytics_lab-database.
Voer uit met: python src/24_read_postgres.py
"""

import getpass

import pandas as pd
from sqlalchemy import create_engine, text


database_url = (
    f"postgresql+psycopg://{getpass.getuser()}@127.0.0.1:5432/analytics_lab"
)
engine = create_engine(database_url)

query = text(
    """
    SELECT
        country,
        SUM(quantity * price) AS revenue
    FROM orders
    GROUP BY country
    ORDER BY revenue DESC;
    """
)

with engine.connect() as connection:
    revenue_by_country = pd.read_sql(query, connection)

print("Omzet per land, gelezen uit PostgreSQL:")
print(revenue_by_country)
