-- Step 1: Create the Pharmacies and Prescriptions database
CREATE DATABASE IF NOT EXISTS Pharmacies_Prescriptions;

-- Step 2: Select the Pharmacies and Prescriptions database
USE Pharmacies_Prescriptions;

-- Step 3: Create the Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    line_1_number_building VARCHAR(255),
    line_2_number_street VARCHAR(255),
    line_3_area_locality VARCHAR(255),
    city VARCHAR(255),
    zip_postcode VARCHAR(50),
    state_province_country VARCHAR(255),
    country VARCHAR(255),
    other_address_details TEXT
);

-- Step 4: Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    address_id INT,
    customer_name VARCHAR(255),
    date_became_customer DATE,
    credit_card_number VARCHAR(50),
    card_expiry_date DATE,
    other_customer_details TEXT,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 5: Create the Drug_Companies table
CREATE TABLE IF NOT EXISTS Drug_Companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255),
    other_company_details TEXT
);

-- Step 6: Create the Drugs_and_Medication table
CREATE TABLE IF NOT EXISTS Drugs_and_Medication (
    drug_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    drug_name VARCHAR(255),
    drug_cost DECIMAL(10,2),
    drug_available_date DATE,
    drug_withdrawn_date DATE,
    drug_description TEXT,
    generic_vn VARCHAR(50),
    generic_equivalent_drug_id INT,
    other_drug_details TEXT,
    FOREIGN KEY (company_id) REFERENCES Drug_Companies(company_id)
);

-- Step 7: Create the Physicians table
CREATE TABLE IF NOT EXISTS Physicians (
    physician_id INT AUTO_INCREMENT PRIMARY KEY,
    address_id INT,
    physician_details TEXT,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 8: Create the Ref_Payment_Methods table
CREATE TABLE IF NOT EXISTS Ref_Payment_Methods (
    payment_method_code VARCHAR(50) PRIMARY KEY,
    payment_method_description VARCHAR(255)
);

-- Step 9: Create the Ref_Prescription_Status table
CREATE TABLE IF NOT EXISTS Ref_Prescription_Status (
    prescription_status_code VARCHAR(50) PRIMARY KEY,
    prescription_status_description VARCHAR(255)
);

-- Step 10: Create the Prescriptions table
CREATE TABLE IF NOT EXISTS Prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    physician_id INT,
    prescription_status_code VARCHAR(50),
    payment_method_code VARCHAR(50),
    prescription_issued_date DATE,
    prescription_filled_date DATE,
    other_details TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (physician_id) REFERENCES Physicians(physician_id),
    FOREIGN KEY (prescription_status_code) REFERENCES Ref_Prescription_Status(prescription_status_code),
    FOREIGN KEY (payment_method_code) REFERENCES Ref_Payment_Methods(payment_method_code)
);

-- Step 11: Create the Prescription_Items table
CREATE TABLE IF NOT EXISTS Prescription_Items (
    prescription_id INT,
    drug_id INT,
    prescription_quantity INT,
    instructions_to_customer TEXT,
    PRIMARY KEY (prescription_id, drug_id),
    FOREIGN KEY (prescription_id) REFERENCES Prescriptions(prescription_id),
    FOREIGN KEY (drug_id) REFERENCES Drugs_and_Medication(drug_id)
);

-- Step 12: Insert sample data into the Addresses table
INSERT INTO Addresses (line_1_number_building, line_2_number_street, city, zip_postcode, country)
VALUES 
    ('123', 'Main St', 'New York', '10001', 'USA'),
    ('456', 'Elm St', 'Los Angeles', '90001', 'USA');

-- Step 13: Insert sample data into the Customers table
INSERT INTO Customers (address_id, customer_name, date_became_customer, credit_card_number, card_expiry_date)
VALUES 
    (1, 'John Doe', '2023-01-01', '1234-5678-9012-3456', '2025-12-31'),
    (2, 'Jane Smith', '2023-02-01', '9876-5432-1098-7654', '2026-11-30');

-- Step 14: Insert sample data into the Drug_Companies table
INSERT INTO Drug_Companies (company_name)
VALUES 
    ('Pharma Inc.'),
    ('MediCorp');

-- Step 15: Insert sample data into the Drugs_and_Medication table
INSERT INTO Drugs_and_Medication (company_id, drug_name, drug_cost, drug_available_date, drug_description)
VALUES 
    (1, 'Drug A', 10.50, '2023-01-01', 'Pain reliever'),
    (2, 'Drug B', 20.00, '2023-02-01', 'Antibiotic');

-- Step 16: Insert sample data into the Physicians table
INSERT INTO Physicians (address_id, physician_details)
VALUES 
    (1, 'Dr. John Smith, General Practitioner'),
    (2, 'Dr. Jane Doe, Cardiologist');

-- Step 17: Insert sample data into the Ref_Payment_Methods table
INSERT INTO Ref_Payment_Methods (payment_method_code, payment_method_description)
VALUES 
    ('CASH', 'Cash'),
    ('CC', 'Credit Card');

-- Step 18: Insert sample data into the Ref_Prescription_Status table
INSERT INTO Ref_Prescription_Status (prescription_status_code, prescription_status_description)
VALUES 
    ('FILLED', 'Filled'),
    ('PART-FILLED', 'Part-Filled'),
    ('NOT-COLLECTED', 'Filled but not collected');

-- Step 19: Insert sample data into the Prescriptions table
INSERT INTO Prescriptions (customer_id, physician_id, prescription_status_code, payment_method_code, prescription_issued_date)
VALUES 
    (1, 1, 'FILLED', 'CC', '2023-03-01'),
    (2, 2, 'PART-FILLED', 'CASH', '2023-03-02');

-- Step 20: Insert sample data into the Prescription_Items table
INSERT INTO Prescription_Items (prescription_id, drug_id, prescription_quantity, instructions_to_customer)
VALUES 
    (1, 1, 2, 'Take twice daily with meals.'),
    (2, 2, 1, 'Take once daily before bedtime.');

-- Step 21: View the resulting tables
SELECT * FROM Addresses;
SELECT * FROM Customers;
SELECT * FROM Drug_Companies;
SELECT * FROM Drugs_and_Medication;
SELECT * FROM Physicians;
SELECT * FROM Ref_Payment_Methods;
SELECT * FROM Ref_Prescription_Status;
SELECT * FROM Prescriptions;
SELECT * FROM Prescription_Items;
