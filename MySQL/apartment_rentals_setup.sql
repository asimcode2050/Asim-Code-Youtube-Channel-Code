-- Step 1: Create the Apartment Rentals database
CREATE DATABASE IF NOT EXISTS Apartment_Rentals;

-- Step 2: Select the Apartment Rentals database
USE Apartment_Rentals;

-- Step 3: Create the Apartment_Buildings table
CREATE TABLE IF NOT EXISTS Apartment_Buildings (
    building_id INT PRIMARY KEY,
    building_short_name VARCHAR(50),
    building_full_name VARCHAR(100),
    building_description VARCHAR(255),
    building_address VARCHAR(255),
    building_manager VARCHAR(100),
    building_phone VARCHAR(15),
    other_building_details VARCHAR(255)
);

-- Step 4: Create the Ref_Apartment_Types table
CREATE TABLE IF NOT EXISTS Ref_Apartment_Types (
    apt_type_code VARCHAR(10) PRIMARY KEY,
    apt_type_description VARCHAR(50)
);

-- Step 5: Create the Ref_Apartments table
CREATE TABLE IF NOT EXISTS Ref_Apartments (
    apt_id INT PRIMARY KEY,
    building_id INT,
    apt_type_code VARCHAR(10),
    apt_number VARCHAR(50),
    bathroom_count INT,
    bedroom_count INT,
    room_count INT,
    other_apartment_details VARCHAR(255),
    FOREIGN KEY (building_id) REFERENCES Apartment_Buildings(building_id),
    FOREIGN KEY (apt_type_code) REFERENCES Ref_Apartment_Types(apt_type_code)
);

-- Step 6: Create the Ref_Apartment_Facilities table
CREATE TABLE IF NOT EXISTS Ref_Apartment_Facilities (
    facility_code VARCHAR(10) PRIMARY KEY,
    facility_description VARCHAR(255)
);

-- Step 7: Create the Ref_Gender table
CREATE TABLE IF NOT EXISTS Ref_Gender (
    gender_code VARCHAR(1) PRIMARY KEY,
    gender_description VARCHAR(50)
);

-- Step 8: Create the Ref_Booking_status table
CREATE TABLE IF NOT EXISTS Ref_Booking_status (
    booking_status_code VARCHAR(10) PRIMARY KEY,
    booking_status_description VARCHAR(255)
);

-- Step 9: Create the Guests table
CREATE TABLE IF NOT EXISTS Guests (
    guest_id INT PRIMARY KEY,
    gender_code VARCHAR(1),
    guest_first_name VARCHAR(100),
    guest_last_name VARCHAR(100),
    date_of_birth DATE,
    other_guest_details VARCHAR(255),
    FOREIGN KEY (gender_code) REFERENCES Ref_Gender(gender_code)
);

-- Step 10: Create the Ref_Booking_lc table
CREATE TABLE IF NOT EXISTS Ref_Booking_lc (
    apt_booking_lc INT PRIMARY KEY,
    apt_id INT,
    guest_id INT,
    booking_status_code VARCHAR(10),
    booking_start_date DATE,
    booking_end_date DATE,
    other_booking_details VARCHAR(255),
    FOREIGN KEY (apt_id) REFERENCES Ref_Apartments(apt_id),
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (booking_status_code) REFERENCES Ref_Booking_status(booking_status_code)
);

-- Step 11: Insert sample data into the Apartment_Buildings table
INSERT INTO Apartment_Buildings (building_id, building_short_name, building_full_name, building_description, building_address, building_manager, building_phone)
VALUES 
    (1, 'BldgA', 'Building A', 'A luxurious apartment building', '123 Main St', 'John Doe', '123-456-7890');

-- Step 12: Insert sample data into the Ref_Apartment_Types table
INSERT INTO Ref_Apartment_Types (apt_type_code, apt_type_description)
VALUES 
    ('STUDIO', 'Studio Apartment'),
    ('1BED', '1 Bedroom Apartment');

-- Step 13: Insert sample data into the Ref_Apartments table
INSERT INTO Ref_Apartments (apt_id, building_id, apt_type_code, apt_number, bathroom_count, bedroom_count, room_count)
VALUES 
    (1, 1, 'STUDIO', '101', 1, 0, 1);

-- Step 14: Insert sample data into the Ref_Apartment_Facilities table
INSERT INTO Ref_Apartment_Facilities (facility_code, facility_description)
VALUES 
    ('BB', 'Broadband'),
    ('CTV', 'Cable TV');

-- Step 15: Insert sample data into the Ref_Gender table
INSERT INTO Ref_Gender (gender_code, gender_description)
VALUES 
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown');

-- Step 16: Insert sample data into the Ref_Booking_status table
INSERT INTO Ref_Booking_status (booking_status_code, booking_status_description)
VALUES 
    ('CONF', 'Confirmed'),
    ('PROV', 'Provisional');

-- Step 17: Insert sample data into the Guests table
INSERT INTO Guests (guest_id, gender_code, guest_first_name, guest_last_name, date_of_birth)
VALUES 
    (1, 'M', 'John', 'Doe', '1980-01-01');

-- Step 18: Insert sample data into the Ref_Booking_lc table
INSERT INTO Ref_Booking_lc (apt_booking_lc, apt_id, guest_id, booking_status_code, booking_start_date, booking_end_date)
VALUES 
    (1, 1, 1, 'CONF', '2023-01-01', '2023-01-07');

-- Step 19: View the resulting tables
SELECT * FROM Apartment_Buildings;
SELECT * FROM Ref_Apartment_Types;
SELECT * FROM Ref_Apartments;
SELECT * FROM Ref_Apartment_Facilities;
SELECT * FROM Ref_Gender;
SELECT * FROM Ref_Booking_status;
SELECT * FROM Guests;
SELECT * FROM Ref_Booking_lc;
