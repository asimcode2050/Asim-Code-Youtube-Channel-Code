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

-- 7. Use ANY operator to check if any product has total sales greater than 200
SELECT product_name 
FROM Product 
WHERE product_id = ANY (SELECT product_id FROM Sales WHERE amount > 200);

-- 8. Use ALL operator to check if all products have total sales greater than 100
SELECT product_name 
FROM Product 
WHERE product_id = ALL (SELECT product_id FROM Sales WHERE amount > 100);
