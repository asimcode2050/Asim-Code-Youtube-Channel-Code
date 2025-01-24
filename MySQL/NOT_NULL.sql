-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select the Database
USE TestDB;

-- 3. Create Employee Table with NOT NULL Constraint on 'name' and 'salary' columns
CREATE TABLE Employee (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
);

-- 4. Insert Valid Data into Employee Table
INSERT INTO Employee (name, salary) 
VALUES ('John Doe', 50000.00), 
       ('Jane Smith', 55000.00);

-- 5. Try to Insert Invalid Data with NULL for 'name' (Violates NOT NULL Constraint)
INSERT INTO Employee (name, salary) 
VALUES (NULL, 60000.00);

-- 6. Try to Insert Invalid Data with NULL for 'salary' (Violates NOT NULL Constraint)
INSERT INTO Employee (name, salary) 
VALUES ('Alice Brown', NULL);

-- 7. Select All Data from Employee Table
SELECT * FROM Employee;
