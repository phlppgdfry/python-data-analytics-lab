-- Fase 7.2 — zakelijke vragen in SQL.
--
-- SELECT kiest kolommen.
-- FROM kiest de tabel.
-- GROUP BY groepeert rijen, net als Pandas groupby.

-- Alle orders bekijken.
SELECT *
FROM orders
ORDER BY order_date;

-- Totale omzet per land.
SELECT
    country,
    SUM(quantity * price) AS revenue
FROM orders
GROUP BY country
ORDER BY revenue DESC;

-- Totale omzet per product.
SELECT
    product,
    SUM(quantity * price) AS revenue
FROM orders
GROUP BY product
ORDER BY revenue DESC;
