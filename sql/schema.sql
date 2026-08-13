-- Fase 7.1 — een eenvoudige sales-tabel in PostgreSQL.
--
-- Uitvoeren nadat de database bestaat:
-- psql -d analytics_lab -f sql/schema.sql

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE NOT NULL,
    country TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);
