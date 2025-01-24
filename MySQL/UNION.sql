-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select Database
USE TestDB;

-- 3. Create Employee Table
CREATE TABLE Employee (
    id INT,
    name VARCHAR(255),
    position VARCHAR(255)
);

-- 4. Create Contractor Table
CREATE TABLE Contractor (
    id INT,
    name VARCHAR(255),
    position VARCHAR(255)
);

-- 5. Insert Data into Employee Table
INSERT INTO Employee (id, name, position) 
VALUES 
(1, 'John Doe', 'Manager'), 
(2, 'Jane Smith', 'Developer'), 
(3, 'Emily Davis', 'Designer');

-- 6. Insert Data into Contractor Table
INSERT INTO Contractor (id, name, position) 
VALUES 
(1, 'Michael Brown', 'Contract Developer'), 
(2, 'Sarah Wilson', 'Contract Designer');

-- 7. Perform UNION to combine Employee and Contractor data (removes duplicates)
SELECT id, name, position FROM Employee 
UNION 
SELECT id, name, position FROM Contractor;
