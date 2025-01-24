-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select the Database
USE TestDB;

-- 3. Create the Sales Table
CREATE TABLE Sales (
    id INT,
    product_id INT,
    quantity INT,
    amount DECIMAL(10, 2)
);

-- 4. Create the Product Table
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

-- 7. Use EXISTS Operator to Check if a Product Has Sales
SELECT product_name 
FROM Product 
WHERE EXISTS (SELECT 1 FROM Sales WHERE Sales.product_id = Product.product_id);

-- 8. Use EXISTS Operator with a Condition to Check if Product's Total Sales Exceed 200
SELECT product_name 
FROM Product 
WHERE EXISTS (SELECT 1 
               FROM Sales 
               WHERE Sales.product_id = Product.product_id 
               GROUP BY Sales.product_id 
               HAVING SUM(Sales.amount) > 200);
