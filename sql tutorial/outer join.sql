SELECT 
	c.customer_id,
    c.first_name,
    o.order_id
FROM orders o
RIGHT OUTER JOIN customers c
	ON c.customer_id = o.customer_id