-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select the Database
USE TestDB;

-- 3. Create Employee Table with PRIMARY KEY constraint on 'id' column
CREATE TABLE Employee (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    PRIMARY KEY (id)
);

-- 4. Insert Valid Data into Employee Table (unique id will be automatically assigned)
INSERT INTO Employee (name, email) 
VALUES ('John Doe', 'john.doe@example.com'), 
       ('Jane Smith', 'jane.smith@example.com');

-- 5. Try to Insert Invalid Data with Duplicate id (violates PRIMARY KEY constraint)
INSERT INTO Employee (id, name, email) 
VALUES (1, 'Alice Brown', 'alice.brown@example.com');

-- 6. Select All Data from Employee Table
SELECT * FROM Employee;
