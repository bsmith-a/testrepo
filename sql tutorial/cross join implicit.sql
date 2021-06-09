USE sql_store;

SELECT
	c.first_name AS customer,
    p.name AS product
FROM customers c, orders o
ORDER BY c.first_name