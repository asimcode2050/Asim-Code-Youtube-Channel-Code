-- Step 1: Create the Hospital Admissions database
CREATE DATABASE IF NOT EXISTS Hospital_Admissions;

-- Step 2: Select the Hospital Admissions database
USE Hospital_Admissions;

-- Step 3: Create the Staff table
CREATE TABLE IF NOT EXISTS Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_category_code VARCHAR(50),
    gender VARCHAR(50),
    staff_lob_title VARCHAR(255),
    staff_first_name VARCHAR(255),
    staff_middle_name VARCHAR(255),
    staff_last_name VARCHAR(255),
    staff_qualifications TEXT,
    staff_birth_date DATE,
    other_staff_details TEXT
);

-- Step 4: Create the Addresses table
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

-- Step 5: Create the Patients table
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    outpatient_un VARCHAR(255),
    hospital_number VARCHAR(255),
    nhs_number VARCHAR(255),
    gender VARCHAR(50),
    date_of_birth DATE,
    patient_first_name VARCHAR(255),
    patient_middle_name VARCHAR(255),
    patient_last_name VARCHAR(255),
    height DECIMAL(5,2),
    weight DECIMAL(5,2),
    next_of_kin VARCHAR(255),
    home_phone VARCHAR(15),
    work_phone VARCHAR(15),
    cell_mobile_phone VARCHAR(15),
    other_patient_details TEXT
);

-- Step 6: Create the Ref_Payment_Methods table
CREATE TABLE IF NOT EXISTS Ref_Payment_Methods (
    payment_method_code VARCHAR(50) PRIMARY KEY,
    payment_method_description VARCHAR(255)
);

-- Step 7: Create the Patient_Payment_Methods table
CREATE TABLE IF NOT EXISTS Patient_Payment_Methods (
    patient_method_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    payment_method_code VARCHAR(50),
    payment_method_details TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (payment_method_code) REFERENCES Ref_Payment_Methods(payment_method_code)
);

-- Step 8: Create the Staff_Addresses table
CREATE TABLE IF NOT EXISTS Staff_Addresses (
    staff_id INT,
    address_id INT,
    date_address_from DATE,
    date_address_to DATE,
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 9: Create the Patient_Addresses table
CREATE TABLE IF NOT EXISTS Patient_Addresses (
    patient_id INT,
    address_id INT,
    date_address_from DATE,
    date_address_to DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
);

-- Step 10: Create the Patient_Rooms table
CREATE TABLE IF NOT EXISTS Patient_Rooms (
    patient_id INT,
    room_id INT,
    date_stay_from DATE,
    date_date_to DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Step 11: Create the Patient_Bills table
CREATE TABLE IF NOT EXISTS Patient_Bills (
    patient_bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    date_bill_paid DATE,
    total_amount_date DECIMAL(10,2),
    other_bill_details TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Step 12: Create the Ref_Staff_Categories table
CREATE TABLE IF NOT EXISTS Ref_Staff_Categories (
    staff_category_code VARCHAR(50) PRIMARY KEY,
    staff_category_description VARCHAR(255)
);

-- Step 13: Create the Patient_Records table
CREATE TABLE IF NOT EXISTS Patient_Records (
    patient_record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    billable_item_code VARCHAR(50),
    component_code VARCHAR(50),
    component_description TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Step 14: Create the Ref_Billable_Items table
CREATE TABLE IF NOT EXISTS Ref_Billable_Items (
    billable_item_code VARCHAR(50) PRIMARY KEY,
    billable_item_description VARCHAR(255)
);

-- Step 15: Insert sample data into the Addresses table
INSERT INTO Addresses (line_1_number_building, line_2_number_street, line_3_area_locality, city, zip_postcode, state_province_country, country)
VALUES 
    ('123 Main St', 'Apt 4B', 'Downtown', 'Springfield', '12345', 'IL', 'USA'),
    ('456 Elm St', NULL, 'Uptown', 'Shelbyville', '67890', 'IL', 'USA');

-- Step 16: Insert sample data into the Staff table
INSERT INTO Staff (staff_category_code, gender, staff_lob_title, staff_first_name, staff_middle_name, staff_last_name, staff_qualifications, staff_birth_date)
VALUES 
    ('DOC', 'Male', 'Cardiologist', 'John', 'A.', 'Doe', 'MD, PhD', '1980-05-15'),
    ('NUR', 'Female', 'Head Nurse', 'Jane', 'B.', 'Smith', 'RN, BSN', '1990-08-25');

-- Step 17: Insert sample data into the Patients table
INSERT INTO Patients (outpatient_un, hospital_number, nhs_number, gender, date_of_birth, patient_first_name, patient_middle_name, patient_last_name, height, weight, next_of_kin, home_phone, work_phone, cell_mobile_phone)
VALUES 
    ('OP123', 'H12345', 'NHS123', 'Male', '1985-05-15', 'John', 'D.', 'Doe', 175.5, 70.2, 'Jane Doe', '1234567890', '0987654321', '5551234567'),
    ('OP456', 'H67890', 'NHS456', 'Female', '1990-08-25', 'Jane', 'S.', 'Smith', 160.0, 55.0, 'John Smith', '0987654321', '1234567890', '5559876543');

-- Step 18: Insert sample data into the Ref_Payment_Methods table
INSERT INTO Ref_Payment_Methods (payment_method_code, payment_method_description)
VALUES 
    ('LC', 'Credit Card'),
    ('CH', 'Cash');

-- Step 19: Insert sample data into the Patient_Payment_Methods table
INSERT INTO Patient_Payment_Methods (patient_id, payment_method_code, payment_method_details)
VALUES 
    (1, 'LC', 'Card Number: 1234-5678-9012-3456, Expiry Date: 12/25'),
    (2, 'CH', 'Paid in cash');

-- Step 20: Insert sample data into the Staff_Addresses table
INSERT INTO Staff_Addresses (staff_id, address_id, date_address_from, date_address_to)
VALUES 
    (1, 1, '2020-01-01', NULL),
    (2, 2, '2021-01-01', NULL);

-- Step 21: Insert sample data into the Patient_Addresses table
INSERT INTO Patient_Addresses (patient_id, address_id, date_address_from, date_address_to)
VALUES 
    (1, 1, '2020-01-01', NULL),
    (2, 2, '2021-01-01', NULL);

-- Step 22: Insert sample data into the Patient_Rooms table
INSERT INTO Patient_Rooms (patient_id, room_id, date_stay_from, date_date_to)
VALUES 
    (1, 101, '2023-10-01', '2023-10-05'),
    (2, 102, '2023-10-02', NULL);

-- Step 23: Insert sample data into the Patient_Bills table
INSERT INTO Patient_Bills (patient_id, date_bill_paid, total_amount_date, other_bill_details)
VALUES 
    (1, '2023-10-05', 500.00, 'Paid in full'),
    (2, NULL, 750.00, 'Pending payment');

-- Step 24: Insert sample data into the Ref_Staff_Categories table
INSERT INTO Ref_Staff_Categories (staff_category_code, staff_category_description)
VALUES 
    ('DOC', 'Doctor'),
    ('NUR', 'Nurse');

-- Step 25: Insert sample data into the Patient_Records table
INSERT INTO Patient_Records (patient_id, billable_item_code, component_code, component_description)
VALUES 
    (1, 'MED', 'ADM', 'Admission for hypertension'),
    (2, 'TRE', 'DIA', 'Diagnosis for migraine');

-- Step 26: Insert sample data into the Ref_Billable_Items table
INSERT INTO Ref_Billable_Items (billable_item_code, billable_item_description)
VALUES 
    ('MED', 'Medication'),
    ('TRE', 'Treatment');

-- Step 27: View the resulting tables
SELECT * FROM Staff;
SELECT * FROM Patients;
SELECT * FROM Ref_Payment_Methods;
SELECT * FROM Patient_Payment_Methods;
SELECT * FROM Staff_Addresses;
SELECT * FROM Patient_Addresses;
SELECT * FROM Patient_Rooms;
SELECT * FROM Patient_Bills;
SELECT * FROM Ref_Staff_Categories;
SELECT * FROM Patient_Records;
SELECT * FROM Ref_Billable_Items;
