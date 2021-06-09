USE sql_invoicing;

SELECT 
	p.client_id,
    c.name,
    invoice_id,
    amount,
    date AS payment_date,
    pm.name AS payment_method
FROM payments p
JOIN clients c
	ON p.client_id = c.client_id
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
ORDER BY p.client_id
