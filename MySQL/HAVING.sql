-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select Database
USE TestDB;

-- 3. Create Sales Table
CREATE TABLE Sales (
    id INT,
    product_id INT,
    quantity INT,
    amount DECIMAL(10, 2)
);

-- 4. Create Product Table
CREATE TABLE Product (
    product_id INT,
    product_name VARCHAR(255)
);

-- 5. Insert Data into Sales Table
INSERT INTO Sales (id, product_id, quantity, amount) 
VALUES 
(1, 101, 5, 150.00), 
(2, 102, 2, 80.00), 
(3, 101, 3, 90.00), 
(4, 103, 10, 500.00), 
(5, 102, 7, 210.00);

-- 6. Insert Data into Product Table
INSERT INTO Product (product_id, product_name) 
VALUES 
(101, 'Laptop'), 
(102, 'Smartphone'), 
(103, 'Tablet');

-- 7. Use GROUP BY with HAVING clause to filter total sales by product_id
SELECT product_id, SUM(amount) AS total_sales 
FROM Sales 
GROUP BY product_id
HAVING SUM(amount) > 200;

-- 8. Use JOIN with GROUP BY and HAVING clause to filter total sales by product_name
SELECT Product.product_name, SUM(Sales.amount) AS total_sales 
FROM Sales 
JOIN Product ON Sales.product_id = Product.product_id 
GROUP BY Product.product_name
HAVING SUM(Sales.amount) > 200;
