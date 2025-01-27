-- Step 1: Create the Real Estate database
CREATE DATABASE IF NOT EXISTS Real_Estate;

-- Step 2: Select the Real Estate database
USE Real_Estate;

-- Step 3: Create the Ref_Property_Types table
CREATE TABLE IF NOT EXISTS Ref_Property_Types (
    property_type_code VARCHAR(50) PRIMARY KEY,
    property_type_description VARCHAR(255)
);

-- Step 4: Create the Properties table
CREATE TABLE IF NOT EXISTS Properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    property_type_code VARCHAR(50),
    date_on_market DATE,
    date_sold DATE,
    property_name VARCHAR(255),
    property_owner VARCHAR(255),
    property_description TEXT,
    property_address VARCHAR(255),
    room_count INT,
    vendor_requested_price DECIMAL(10,2),
    buyer_offered_price DECIMAL(10,2),
    agreed_selling_price DECIMAL(10,2),
    other_property_details TEXT,
    FOREIGN KEY (property_type_code) REFERENCES Ref_Property_Types(property_type_code)
);

-- Step 5: Create the Apartments table
CREATE TABLE IF NOT EXISTS Apartments (
    property_id INT PRIMARY KEY,
    parking_vn VARCHAR(50),
    building_name VARCHAR(255),
    other_apartment_details TEXT,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 6: Create the Fields table
CREATE TABLE IF NOT EXISTS Fields (
    property_id INT PRIMARY KEY,
    size_in_hectares DECIMAL(10,2),
    neighbours VARCHAR(255),
    other_field_details TEXT,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 7: Create the Houses table
CREATE TABLE IF NOT EXISTS Houses (
    property_id INT PRIMARY KEY,
    other_house_details TEXT,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 8: Create the Shops table
CREATE TABLE IF NOT EXISTS Shops (
    property_id INT PRIMARY KEY,
    shopping_mall_name VARCHAR(255),
    other_shop_details TEXT,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 9: Create the Units table
CREATE TABLE IF NOT EXISTS Units (
    property_id INT PRIMARY KEY,
    unit_number VARCHAR(50),
    other_unit_details TEXT,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 10: Create the Property_Features table
CREATE TABLE IF NOT EXISTS Property_Features (
    property_id INT,
    feature_id INT,
    property_feature_description TEXT,
    PRIMARY KEY (property_id, feature_id),
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);

-- Step 11: Create the Features table
CREATE TABLE IF NOT EXISTS Features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    feature_type_code VARCHAR(50),
    feature_name VARCHAR(255),
    feature_description TEXT
);

-- Step 12: Create the Ref_Feature_Types table
CREATE TABLE IF NOT EXISTS Ref_Feature_Types (
    feature_type_code VARCHAR(50) PRIMARY KEY,
    feature_type_name VARCHAR(255)
);

-- Step 13: Create the Ref_Room_Types table
CREATE TABLE IF NOT EXISTS Ref_Room_Types (
    room_type_code VARCHAR(50) PRIMARY KEY,
    room_type_description VARCHAR(255)
);

-- Step 14: Insert sample data into the Ref_Property_Types table
INSERT INTO Ref_Property_Types (property_type_code, property_type_description)
VALUES 
    ('APT', 'Apartment'),
    ('HS', 'House'),
    ('FLD', 'Field'),
    ('SHP', 'Shop'),
    ('UNT', 'Unit');

-- Step 15: Insert sample data into the Properties table
INSERT INTO Properties (property_type_code, date_on_market, date_sold, property_name, property_owner, property_description, property_address, room_count, vendor_requested_price, buyer_offered_price, agreed_selling_price)
VALUES 
    ('APT', '2023-01-01', '2023-02-01', 'Sunny Apartment', 'John Doe', 'A sunny apartment in the city center.', '123 Main St', 3, 200000.00, 190000.00, 195000.00),
    ('HS', '2023-03-01', NULL, 'Cozy House', 'Jane Smith', 'A cozy house in the suburbs.', '456 Elm St', 4, 300000.00, NULL, NULL);

-- Step 16: Insert sample data into the Apartments table
INSERT INTO Apartments (property_id, parking_vn, building_name)
VALUES 
    (1, 'P123', 'Sunny Building');

-- Step 17: Insert sample data into the Houses table
INSERT INTO Houses (property_id)
VALUES 
    (2);

-- Step 18: View the resulting tables
SELECT * FROM Ref_Property_Types;
SELECT * FROM Properties;
SELECT * FROM Apartments;
SELECT * FROM Houses;
