-- Step 1: Create the Employment Agencies database
CREATE DATABASE IF NOT EXISTS Employment_Agencies;

-- Step 2: Select the Employment Agencies database
USE Employment_Agencies;

-- Step 3: Create the Ref_Agency_Categories table
CREATE TABLE IF NOT EXISTS Ref_Agency_Categories (
    agency_category_code VARCHAR(50) PRIMARY KEY,
    agency_category_description VARCHAR(255)
);

-- Step 4: Create the Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    line_1_number_building VARCHAR(255),
    line_2_number_street VARCHAR(255),
    line_3_area_locality VARCHAR(255),
    city_town VARCHAR(255),
    state_province_country VARCHAR(255),
    country VARCHAR(255),
    other_details TEXT
);

-- Step 5: Create the Agencies table
CREATE TABLE IF NOT EXISTS Agencies (
    agency_id INT AUTO_INCREMENT PRIMARY KEY,
    address_id INT,
    agency_name VARCHAR(255),
    agency_tailing VARCHAR(255),
    agency_phone VARCHAR(50),
    agency_email VARCHAR(255),
    website_address VARCHAR(255),
    other_agency_details TEXT,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 6: Create the Agency_Categories table
CREATE TABLE IF NOT EXISTS Agency_Categories (
    agency_id INT,
    agency_category_code VARCHAR(50),
    PRIMARY KEY (agency_id, agency_category_code),
    FOREIGN KEY (agency_id) REFERENCES Agencies(agency_id),
    FOREIGN KEY (agency_category_code) REFERENCES Ref_Agency_Categories(agency_category_code)
);

-- Step 7: Create the Local_Offices table
CREATE TABLE IF NOT EXISTS Local_Offices (
    office_id INT AUTO_INCREMENT PRIMARY KEY,
    agency_id INT,
    address_id INT,
    office_phone VARCHAR(50),
    office_email VARCHAR(255),
    other_office_details TEXT,
    FOREIGN KEY (agency_id) REFERENCES Agencies(agency_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 8: Create the Contacts table
CREATE TABLE IF NOT EXISTS Contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    office_id INT,
    date_list_contact DATE,
    first_name VARCHAR(255),
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(50),
    contact_phone VARCHAR(50),
    contact_email VARCHAR(255),
    contact_from_date DATE,
    contact_to_date DATE,
    other_details TEXT,
    FOREIGN KEY (office_id) REFERENCES Local_Offices(office_id)
);

-- Step 9: Insert sample data into the Ref_Agency_Categories table
INSERT INTO Ref_Agency_Categories (agency_category_code, agency_category_description)
VALUES 
    ('ADMIN', 'Administration'),
    ('IT', 'Information Technology'),
    ('TUTOR', 'Tutoring');

-- Step 10: Insert sample data into the Addresses table
INSERT INTO Addresses (line_1_number_building, line_2_number_street, city_town, state_province_country, country)
VALUES 
    ('123', 'Main St', 'New York', 'NY', 'USA'),
    ('456', 'Elm St', 'Los Angeles', 'CA', 'USA');

-- Step 11: Insert sample data into the Agencies table
INSERT INTO Agencies (address_id, agency_name, agency_tailing, agency_phone, agency_email, website_address)
VALUES 
    (1, 'Agency A', 'Tailing A', '123-456-7890', 'agencyA@example.com', 'www.agencyA.com'),
    (2, 'Agency B', 'Tailing B', '987-654-3210', 'agencyB@example.com', 'www.agencyB.com');

-- Step 12: Insert sample data into the Agency_Categories table
INSERT INTO Agency_Categories (agency_id, agency_category_code)
VALUES 
    (1, 'ADMIN'),
    (2, 'IT');

-- Step 13: Insert sample data into the Local_Offices table
INSERT INTO Local_Offices (agency_id, address_id, office_phone, office_email)
VALUES 
    (1, 1, '555-1234', 'officeA@example.com'),
    (2, 2, '555-5678', 'officeB@example.com');

-- Step 14: Insert sample data into the Contacts table
INSERT INTO Contacts (office_id, date_list_contact, first_name, last_name, gender, contact_phone, contact_email, contact_from_date)
VALUES 
    (1, '2023-01-01', 'John', 'Doe', 'Male', '123-456-7890', 'john.doe@example.com', '2023-01-01'),
    (2, '2023-02-01', 'Jane', 'Smith', 'Female', '987-654-3210', 'jane.smith@example.com', '2023-02-01');

-- Step 15: View the resulting tables
SELECT * FROM Ref_Agency_Categories;
SELECT * FROM Addresses;
SELECT * FROM Agencies;
SELECT * FROM Agency_Categories;
SELECT * FROM Local_Offices;
SELECT * FROM Contacts;
