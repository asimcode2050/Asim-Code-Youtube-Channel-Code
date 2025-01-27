-- Step 1: Create the Airline Booking System database
CREATE DATABASE IF NOT EXISTS Airline_Booking_System;

-- Step 2: Select the Airline Booking System database
USE Airline_Booking_System;

-- Step 3: Create the Travel_Class table
CREATE TABLE IF NOT EXISTS Travel_Class (
    travel_class_id INT AUTO_INCREMENT PRIMARY KEY,
    seat_capacity INT,
    travel_class_description VARCHAR(255)
);

-- Step 4: Create the Passengers table
CREATE TABLE IF NOT EXISTS Passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(50),
    email_address VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    other_address_details TEXT,
    other_passenger_details TEXT
);

-- Step 5: Create the Flights table
CREATE TABLE IF NOT EXISTS Flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(50),
    destination VARCHAR(255),
    starting_from VARCHAR(255),
    departure_time DATETIME,
    arrival_time DATETIME,
    aircraft_type VARCHAR(255)
);

-- Step 6: Create the Bookings table
CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    flight_id INT,
    date_booking_made DATE,
    booking_status_code VARCHAR(50),
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);

-- Step 7: Create the Payments table
CREATE TABLE IF NOT EXISTS Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    payment_amount DECIMAL(10,2),
    payment_date DATE,
    payment_status_code VARCHAR(50),
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
);

-- Step 8: Insert sample data into the Travel_Class table
INSERT INTO Travel_Class (seat_capacity, travel_class_description)
VALUES 
    (50, 'Economy'),
    (30, 'Business'),
    (20, 'First Class');

-- Step 9: Insert sample data into the Passengers table
INSERT INTO Passengers (first_name, last_name, phone_number, email_address, address, city)
VALUES 
    ('John', 'Doe', '123-456-7890', 'john.doe@example.com', '123 Main St', 'New York'),
    ('Jane', 'Smith', '987-654-3210', 'jane.smith@example.com', '456 Elm St', 'Los Angeles');

-- Step 10: Insert sample data into the Flights table
INSERT INTO Flights (flight_number, destination, starting_from, departure_time, arrival_time, aircraft_type)
VALUES 
    ('AA123', 'New York', 'Los Angeles', '2023-12-01 08:00', '2023-12-01 16:00', 'Boeing 737'),
    ('BA456', 'London', 'New York', '2023-12-02 09:00', '2023-12-02 17:00', 'Airbus A320');

-- Step 11: Insert sample data into the Bookings table
INSERT INTO Bookings (passenger_id, flight_id, date_booking_made, booking_status_code)
VALUES 
    (1, 1, '2023-11-01', 'CONFIRMED'),
    (2, 2, '2023-11-02', 'PENDING');

-- Step 12: Insert sample data into the Payments table
INSERT INTO Payments (booking_id, payment_amount, payment_date, payment_status_code)
VALUES 
    (1, 300.00, '2023-11-01', 'PAID'),
    (2, 250.00, '2023-11-02', 'PENDING');

-- Step 13: View the contents of the Travel_Class table
SELECT * FROM Travel_Class;

-- Step 14: View the contents of the Passengers table
SELECT * FROM Passengers;

-- Step 15: View the contents of the Flights table
SELECT * FROM Flights;

-- Step 16: View the contents of the Bookings table
SELECT * FROM Bookings;

-- Step 17: View the contents of the Payments table
SELECT * FROM Payments;
