-- 1. Create the database
CREATE DATABASE TestDB;

-- 2. Select the database to use
USE TestDB;

-- 3. Create the Employees table with columns for employee details
CREATE TABLE Employees (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    PRIMARY KEY (id)
);

-- 4. Insert data into the Employees table
INSERT INTO Employees (name, email)
VALUES ('John Doe', 'john.doe@example.com'),
       ('Jane Smith', 'jane.smith@example.com'),
       ('Alice Brown', 'alice.brown@example.com'),
       ('Bob White', 'bob.white@example.com');

-- 5. Create an index on the 'email' column of the Employees table
CREATE INDEX idx_email ON Employees(email);

-- 6. Select all data from the Employees table to check the results
SELECT * FROM Employees;
