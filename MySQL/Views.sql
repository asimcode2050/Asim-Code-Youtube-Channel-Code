-- 1. Create the database
CREATE DATABASE TestDB;

-- 2. Select the database to use
USE TestDB;

-- 3. Create the Employees table with columns for employee details
CREATE TABLE Employees (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    department VARCHAR(255),
    salary DECIMAL(10, 2),
    PRIMARY KEY (id)
);

-- 4. Insert data into the Employees table
INSERT INTO Employees (name, department, salary)
VALUES ('John Doe', 'HR', 55000.00),
       ('Jane Smith', 'Engineering', 75000.00),
       ('Alice Brown', 'Marketing', 62000.00);

-- 5. Create a view named EmployeeView to select only name and department columns from Employees table
CREATE VIEW EmployeeView AS
SELECT name, department
FROM Employees;

-- 6. Select all data from EmployeeView to check the result of the view
SELECT * FROM EmployeeView;
