-- Fase 7.3 — lokale CSV-data in PostgreSQL laden.
--
-- Uitvoeren met:
-- psql -h 127.0.0.1 -d analytics_lab -f sql/import_sales.sql

TRUNCATE TABLE orders;

\copy orders (order_id, order_date, country, product, quantity, price) FROM 'data/raw/sales_analysis.csv' WITH (FORMAT csv, HEADER true);
