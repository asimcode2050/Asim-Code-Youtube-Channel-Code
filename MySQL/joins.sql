-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select Database
USE TestDB;

-- 3. Create Employee Table
CREATE TABLE Employee (
    id INT,
    name VARCHAR(255),
    department_id INT,
    salary DECIMAL(10,2)
);

-- 4. Create Department Table
CREATE TABLE Department (
    department_id INT,
    department_name VARCHAR(255)
);

-- 5. Insert Data into Employee Table
INSERT INTO Employee (id, name, department_id, salary) 
VALUES 
(1, 'John Doe', 1, 3500.00), 
(2, 'Jane Smith', 2, 4200.00), 
(3, 'Emily Davis', 1, 5500.00), 
(4, 'Michael Brown', 3, 3800.00), 
(5, 'Sarah Wilson', 2, 3000.00);

-- 6. Insert Data into Department Table
INSERT INTO Department (department_id, department_name) 
VALUES 
(1, 'Sales'), 
(2, 'Marketing'), 
(3, 'Engineering');

-- 7. Perform INNER JOIN between Employee and Department
SELECT Employee.id, Employee.name, Department.department_name, Employee.salary 
FROM Employee 
INNER JOIN Department ON Employee.department_id = Department.department_id;

-- 8. Perform LEFT JOIN between Employee and Department
SELECT Employee.id, Employee.name, Department.department_name, Employee.salary 
FROM Employee 
LEFT JOIN Department ON Employee.department_id = Department.department_id;

-- 9. Perform RIGHT JOIN between Employee and Department
SELECT Employee.id, Employee.name, Department.department_name, Employee.salary 
FROM Employee 
RIGHT JOIN Department ON Employee.department_id = Department.department_id;

-- 10. Simulate FULL OUTER JOIN using UNION
SELECT Employee.id, Employee.name, Department.department_name, Employee.salary 
FROM Employee 
LEFT JOIN Department ON Employee.
