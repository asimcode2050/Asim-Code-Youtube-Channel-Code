-- 1. Create Database
CREATE DATABASE TestDB;

-- 2. Select the Database
USE TestDB;

-- 3. Create the Departments Table with PRIMARY KEY
CREATE TABLE Departments (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

-- 4. Create the Employee Table with FOREIGN KEY constraint referencing Departments
CREATE TABLE Employee (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    department_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (department_id) REFERENCES Departments(id)
);

-- 5. Insert Valid Data into Departments Table
INSERT INTO Departments (name) 
VALUES ('Human Resources'), 
       ('Sales'), 
       ('Engineering');

-- 6. Insert Valid Data into Employee Table with valid department_id (foreign key reference)
INSERT INTO Employee (name, department_id) 
VALUES ('John Doe', 1), 
       ('Jane Smith', 2), 
       ('Alice Brown', 3);

-- 7. Try inserting Invalid Data with a non-existent department_id (violates FOREIGN KEY constraint)
INSERT INTO Employee (name, department_id) 
VALUES ('Bob White', 999);

-- 8. Select All Data from Employee Table to see the results
SELECT * FROM Employee;
