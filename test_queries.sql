-- 1. Revenue per Employee
SELECT e.employee_id, e.first_name, e.last_name, SUM(o.total_amount) AS total_revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
WHERE e.employee_id BETWEEN 1000 AND 9999
GROUP BY e.employee_id, e.first_name, e.last_name
ORDER BY total_revenue DESC;

-- Explanation: This query calculates total sales revenue handled by each employee and shows who sold the most.


-- 2. Best Selling Items (Top 3)
SELECT m.item_id, m.name, SUM(od.quantity) AS total_sold
FROM menu_items m
JOIN order_details od ON m.item_id = od.item_id
GROUP BY m.item_id, m.name
ORDER BY total_sold DESC
LIMIT 3;

-- Explanation: This query finds the top 3 most popular menu items based on total quantity sold.


-- 3. Pending Orders
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.order_status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Pending';

-- Explanation: This query lists customers with pending orders, showing who is still waiting for food.


-- 4. Low Stock Inventory
SELECT inventory_id, ingredient_name, current_stock, reorder_point
FROM inventory
WHERE current_stock <= reorder_point;

-- Explanation: This query identifies inventory items that are at or below their reorder point and need restocking.


-- 5. Average Order Metrics
SELECT AVG(o.total_amount) AS avg_order_cost,
       AVG(order_item_count.item_count) AS avg_items_per_order
FROM orders o
JOIN (
    SELECT order_id, SUM(quantity) AS item_count
    FROM order_details
    GROUP BY order_id
) AS order_item_count ON o.order_id = order_item_count.order_id;

-- Explanation: This query calculates the average order cost and the average number of items per order.
