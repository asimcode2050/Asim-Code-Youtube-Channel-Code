-- 1. Create the database
CREATE DATABASE TestDB;

-- 2. Select the database to use
USE TestDB;

-- 3. Create the Events table with DATE, DATETIME, and TIMESTAMP fields
CREATE TABLE Events (
    id INT AUTO_INCREMENT,
    event_name VARCHAR(255),
    event_date DATE,
    event_datetime DATETIME,
    event_timestamp TIMESTAMP,
    PRIMARY KEY (id)
);

-- 4. Insert data into the Events table with different date formats
INSERT INTO Events (event_name, event_date, event_datetime, event_timestamp)
VALUES ('Conference', '2025-02-10', '2025-02-10 14:00:00', CURRENT_TIMESTAMP),
       ('Workshop', '2025-03-12', '2025-03-12 10:00:00', CURRENT_TIMESTAMP);

-- 5. Select all data from Events table to verify the results
SELECT * FROM Events;
