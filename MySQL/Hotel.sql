-- Step 1: Create the Hotel Reservation System database
CREATE DATABASE IF NOT EXISTS Hotel_Reservation_System;

-- Step 2: Select the Hotel Reservation System database
USE Hotel_Reservation_System;

-- Step 3: Create the Ref_Countries table
CREATE TABLE IF NOT EXISTS Ref_Countries (
    country_Code VARCHAR(50) PRIMARY KEY,
    country_Currency VARCHAR(50),
    country_Name VARCHAR(255)
);

-- Step 4: Create the Ref_Star_Ratings table
CREATE TABLE IF NOT EXISTS Ref_Star_Ratings (
    star_Rating_ID INT AUTO_INCREMENT PRIMARY KEY,
    star_Rating_Code VARCHAR(50),
    star_Rating_Image VARCHAR(255)
);

-- Step 5: Create the Hotel_Chains table
CREATE TABLE IF NOT EXISTS Hotel_Chains (
    hotel_Chain_Code VARCHAR(50) PRIMARY KEY,
    hotel_Chain_Name VARCHAR(255)
);

-- Step 6: Create the Hotels table
CREATE TABLE IF NOT EXISTS Hotels (
    hotel_ID INT AUTO_INCREMENT PRIMARY KEY,
    hotel_Code VARCHAR(50),
    hotel_Name VARCHAR(255),
    hotel_Address VARCHAR(255),
    hotel_PostCode VARCHAR(50),
    hotel_City VARCHAR(255),
    hotel_URL VARCHAR(255)
);

-- Step 7: Create the Ref_Hotel_Characteristics table
CREATE TABLE IF NOT EXISTS Ref_Hotel_Characteristics (
    characteristic_ID INT AUTO_INCREMENT PRIMARY KEY,
    characteristic_Code VARCHAR(50),
    characteristic_Description VARCHAR(255)
);

-- Step 8: Create the Guests table
CREATE TABLE IF NOT EXISTS Guests (
    guest_ID INT AUTO_INCREMENT PRIMARY KEY,
    guest_Name VARCHAR(255),
    guest_Address VARCHAR(255),
    guest_City VARCHAR(255)
);

-- Step 9: Create the Bookings table
CREATE TABLE IF NOT EXISTS Bookings (
    booking_ID INT AUTO_INCREMENT PRIMARY KEY,
    guest_ID INT,
    date_From DATE,
    date_To DATE,
    FOREIGN KEY (guest_ID) REFERENCES Guests(guest_ID)
);

-- Step 10: Create the Ref_Room_Types table
CREATE TABLE IF NOT EXISTS Ref_Room_Types (
    room_Type_Code VARCHAR(50) PRIMARY KEY,
    room_Standard_Rate DECIMAL(10,2),
    room_Type_Description VARCHAR(255),
    smoking_YN VARCHAR(1)
);

-- Step 11: Create the Room_Bookings table
CREATE TABLE IF NOT EXISTS Room_Bookings (
    room_Booking_ID INT AUTO_INCREMENT PRIMARY KEY,
    booking_ID INT,
    room_Type_Code VARCHAR(50),
    date_Booking_From DATE,
    date_Booking_To DATE,
    room_Count INT,
    FOREIGN KEY (booking_ID) REFERENCES Bookings(booking_ID),
    FOREIGN KEY (room_Type_Code) REFERENCES Ref_Room_Types(room_Type_Code)
);

-- Step 12: Create the Room_Rate_Periods table
CREATE TABLE IF NOT EXISTS Room_Rate_Periods (
    rate_Period_Code VARCHAR(50) PRIMARY KEY,
    rate_Period_Description VARCHAR(255)
);

-- Step 13: Create the Period_Room_Rates table
CREATE TABLE IF NOT EXISTS Period_Room_Rates (
    period_Room_Rate_ID INT AUTO_INCREMENT PRIMARY KEY,
    room_Type_Code VARCHAR(50),
    rate_Period_Code VARCHAR(50),
    room_Rate DECIMAL(10,2),
    FOREIGN KEY (room_Type_Code) REFERENCES Ref_Room_Types(room_Type_Code)
);

-- Step 14: Insert sample data into the Ref_Countries table
INSERT INTO Ref_Countries (country_Code, country_Currency, country_Name)
VALUES 
    ('US', 'USD', 'United States'),
    ('UK', 'GBP', 'United Kingdom');

-- Step 15: Insert sample data into the Ref_Star_Ratings table
INSERT INTO Ref_Star_Ratings (star_Rating_Code, star_Rating_Image)
VALUES 
    ('5-STAR', '5-star.png'),
    ('4-STAR', '4-star.png');

-- Step 16: Insert sample data into the Hotel_Chains table
INSERT INTO Hotel_Chains (hotel_Chain_Code, hotel_Chain_Name)
VALUES 
    ('HC1', 'Luxury Hotels'),
    ('HC2', 'Budget Hotels');

-- Step 17: Insert sample data into the Hotels table
INSERT INTO Hotels (hotel_Code, hotel_Name, hotel_Address, hotel_PostCode, hotel_City, hotel_URL)
VALUES 
    ('H1', 'Luxury Hotel New York', '123 Main St', '10001', 'New York', 'http://luxuryhotelny.com'),
    ('H2', 'Budget Hotel London', '456 Elm St', 'SW1A 1AA', 'London', 'http://budgethotellondon.com');

-- Step 18: Insert sample data into the Ref_Hotel_Characteristics table
INSERT INTO Ref_Hotel_Characteristics (characteristic_Code, characteristic_Description)
VALUES 
    ('POOL', 'Hotel has a swimming pool'),
    ('GYM', 'Hotel has a gym');

-- Step 19: Insert sample data into the Guests table
INSERT INTO Guests (guest_Name, guest_Address, guest_City)
VALUES 
    ('John Doe', '123 Main St', 'New York'),
    ('Jane Smith', '456 Elm St', 'London');

-- Step 20: Insert sample data into the Bookings table
INSERT INTO Bookings (guest_ID, date_From, date_To)
VALUES 
    (1, '2023-10-01', '2023-10-05'),
    (2, '2023-11-01', '2023-11-07');

-- Step 21: Insert sample data into the Ref_Room_Types table
INSERT INTO Ref_Room_Types (room_Type_Code, room_Standard_Rate, room_Type_Description, smoking_YN)
VALUES 
    ('SINGLE', 100.00, 'Single Room', 'N'),
    ('DOUBLE', 150.00, 'Double Room', 'Y');

-- Step 22: Insert sample data into the Room_Bookings table
INSERT INTO Room_Bookings (booking_ID, room_Type_Code, date_Booking_From, date_Booking_To, room_Count)
VALUES 
    (1, 'SINGLE', '2023-10-01', '2023-10-05', 1),
    (2, 'DOUBLE', '2023-11-01', '2023-11-07', 2);

-- Step 23: Insert sample data into the Room_Rate_Periods table
INSERT INTO Room_Rate_Periods (rate_Period_Code, rate_Period_Description)
VALUES 
    ('JAN-MAR', 'January to March'),
    ('SEP-DEC', 'September to December');

-- Step 24: Insert sample data into the Period_Room_Rates table
INSERT INTO Period_Room_Rates (room_Type_Code, rate_Period_Code, room_Rate)
VALUES 
    ('SINGLE', 'JAN-MAR', 90.00),
    ('DOUBLE', 'SEP-DEC', 140.00);

-- Step 25: View the resulting tables
SELECT * FROM Ref_Countries;
SELECT * FROM Ref_Star_Ratings;
SELECT * FROM Hotel_Chains;
SELECT * FROM Hotels;
SELECT * FROM Ref_Hotel_Characteristics;
SELECT * FROM Guests;
SELECT * FROM Bookings;
SELECT * FROM Ref_Room_Types;
SELECT * FROM Room_Bookings;
SELECT * FROM Room_Rate_Periods;
SELECT * FROM Period_Room_Rates;
