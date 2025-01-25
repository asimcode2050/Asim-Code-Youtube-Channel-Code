-- 1. Create the database
CREATE DATABASE TestDB;

-- 2. Select the database to use
USE TestDB;

-- 3. Create the Users table with an AUTO_INCREMENT field for the 'id'
CREATE TABLE Users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    PRIMARY KEY (id)
);

-- 4. Insert data into the Users table (AUTO_INCREMENT generates 'id' values)
INSERT INTO Users (name, email)
VALUES ('John Doe', 'john.doe@example.com'),
       ('Jane Smith', 'jane.smith@example.com'),
       ('Alice Brown', 'alice.brown@example.com');

-- 5. Select all data from the Users table to verify the results
SELECT * FROM Users;
