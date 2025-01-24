-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select the Database
USE TestDB;

-- 3. Create Employee Table with UNIQUE constraint on the 'email' column
CREATE TABLE Employee (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    PRIMARY KEY (id)
);

-- 4. Insert Valid Data into Employee Table (unique emails)
INSERT INTO Employee (name, email) 
VALUES ('John Doe', 'john.doe@example.com'), 
       ('Jane Smith', 'jane.smith@example.com');

-- 5. Try to Insert Invalid Data with Duplicate Email (violates UNIQUE constraint)
INSERT INTO Employee (name, email) 
VALUES ('Alice Brown', 'john.doe@example.com');

-- 6. Select All Data from Employee Table
SELECT * FROM Employee;
