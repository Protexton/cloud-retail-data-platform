-- 📈 Ingresos totales por categoría de producto
SELECT category, SUM(price * quantity) AS total_revenue
FROM sales_enriched
GROUP BY category
ORDER BY total_revenue DESC;

-- 🧍 Clientes que más han gastado
SELECT client_name, SUM(price * quantity) AS total_spent
FROM sales_enriched
GROUP BY client_name
ORDER BY total_spent DESC
LIMIT 10;

-- 🏬 Ticket medio por tienda
SELECT store_name, AVG(price * quantity) AS avg_ticket
FROM sales_enriched
GROUP BY store_name
ORDER BY avg_ticket DESC;

-- 🗓️ Ventas por mes
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(price * quantity) AS total_monthly_sales
FROM sales_enriched
GROUP BY month
ORDER BY month;
