-- Step 1: Create the Help Desk database
CREATE DATABASE IF NOT EXISTS Help_Desk;

-- Step 2: Select the Help Desk database
USE Help_Desk;

-- Step 3: Create the Ref_Equipment_Types table
CREATE TABLE IF NOT EXISTS Ref_Equipment_Types (
    equipment_type_code VARCHAR(50) PRIMARY KEY,
    equipment_type_description VARCHAR(255)
);

-- Step 4: Create the Equipment table
CREATE TABLE IF NOT EXISTS Equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_type_code VARCHAR(50),
    date_equipment_acquired DATE,
    date_equipment_disposed DATE,
    equipment_code VARCHAR(50),
    equipment_name VARCHAR(255),
    equipment_description TEXT,
    manufacturer_name VARCHAR(255),
    other_details TEXT,
    FOREIGN KEY (equipment_type_code) REFERENCES Ref_Equipment_Types(equipment_type_code)
);

-- Step 5: Create the Ref_User_Types table
CREATE TABLE IF NOT EXISTS Ref_User_Types (
    user_type_code VARCHAR(50) PRIMARY KEY,
    user_type_description VARCHAR(255)
);

-- Step 6: Create the Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_type_code VARCHAR(50),
    user_first_name VARCHAR(255),
    user_last_name VARCHAR(255),
    user_phone VARCHAR(50),
    user_email VARCHAR(255),
    address VARCHAR(255),
    other_user_details TEXT,
    FOREIGN KEY (user_type_code) REFERENCES Ref_User_Types(user_type_code)
);

-- Step 7: Create the Problems table
CREATE TABLE IF NOT EXISTS Problems (
    problem_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_id INT,
    user_id INT,
    problem_reported_datetime DATETIME,
    problem_description TEXT,
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Step 8: Create the Ref_Skill_Codes table
CREATE TABLE IF NOT EXISTS Ref_Skill_Codes (
    skill_code VARCHAR(50) PRIMARY KEY,
    skill_description VARCHAR(255)
);

-- Step 9: Create the Support_Staff table
CREATE TABLE IF NOT EXISTS Support_Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    date_hired DATE,
    date_left DATE,
    staff_name VARCHAR(255),
    staff_phone VARCHAR(50),
    staff_email VARCHAR(255),
    staff_location VARCHAR(255),
    other_staff_details TEXT
);

-- Step 10: Create the Ref_Priority_Levels table
CREATE TABLE IF NOT EXISTS Ref_Priority_Levels (
    priority_level_code VARCHAR(50) PRIMARY KEY,
    priority_level_description VARCHAR(255)
);

-- Step 11: Create the Ref_Problem_Status_Codes table
CREATE TABLE IF NOT EXISTS Ref_Problem_Status_Codes (
    problem_status_code VARCHAR(50) PRIMARY KEY,
    problem_status_description VARCHAR(255)
);

-- Step 12: Create the Problem_History table
CREATE TABLE IF NOT EXISTS Problem_History (
    problem_history_id INT AUTO_INCREMENT PRIMARY KEY,
    priority_level_code VARCHAR(50),
    problem_id INT,
    problem_status_code VARCHAR(50),
    assigned_staff_id INT,
    fix_datetime DATETIME,
    FOREIGN KEY (priority_level_code) REFERENCES Ref_Priority_Levels(priority_level_code),
    FOREIGN KEY (problem_id) REFERENCES Problems(problem_id),
    FOREIGN KEY (problem_status_code) REFERENCES Ref_Problem_Status_Codes(problem_status_code),
    FOREIGN KEY (assigned_staff_id) REFERENCES Support_Staff(staff_id)
);

-- Step 13: Create the Resolutions table
CREATE TABLE IF NOT EXISTS Resolutions (
    resolution_id INT AUTO_INCREMENT PRIMARY KEY,
    problem_history_id INT,
    resolution_description TEXT,
    FOREIGN KEY (problem_history_id) REFERENCES Problem_History(problem_history_id)
);

-- Step 14: Insert sample data into the Ref_Equipment_Types table
INSERT INTO Ref_Equipment_Types (equipment_type_code, equipment_type_description)
VALUES 
    ('PDA', 'Personal Digital Assistant'),
    ('LAP', 'Laptop'),
    ('DESK', 'Desktop Computer');

-- Step 15: Insert sample data into the Equipment table
INSERT INTO Equipment (equipment_type_code, date_equipment_acquired, equipment_code, equipment_name, equipment_description, manufacturer_name)
VALUES 
    ('PDA', '2023-01-01', 'PDA001', 'PDA Device', 'A portable device for personal use.', 'PDA Inc.'),
    ('LAP', '2023-02-01', 'LAP001', 'Laptop Device', 'A portable computer.', 'Laptop Corp.');

-- Step 16: Insert sample data into the Ref_User_Types table
INSERT INTO Ref_User_Types (user_type_code, user_type_description)
VALUES 
    ('ADMIN', 'Administrator'),
    ('MGT', 'Management'),
    ('USER', 'Regular User');

-- Step 17: Insert sample data into the Users table
INSERT INTO Users (user_type_code, user_first_name, user_last_name, user_phone, user_email, address)
VALUES 
    ('ADMIN', 'John', 'Doe', '123-456-7890', 'john.doe@example.com', '123 Main St'),
    ('USER', 'Jane', 'Smith', '987-654-3210', 'jane.smith@example.com', '456 Elm St');

-- Step 18: Insert sample data into the Problems table
INSERT INTO Problems (equipment_id, user_id, problem_reported_datetime, problem_description)
VALUES 
    (1, 2, '2023-03-01 10:00:00', 'PDA not turning on.'),
    (2, 1, '2023-03-02 11:00:00', 'Laptop screen flickering.');

-- Step 19: Insert sample data into the Ref_Skill_Codes table
INSERT INTO Ref_Skill_Codes (skill_code, skill_description)
VALUES 
    ('DBA', 'Database Administrator'),
    ('TEL', 'Telecommunications Specialist');

-- Step 20: Insert sample data into the Support_Staff table
INSERT INTO Support_Staff (date_hired, staff_name, staff_phone, staff_email, staff_location)
VALUES 
    ('2023-01-01', 'Alice Johnson', '555-1234', 'alice.johnson@example.com', 'HQ'),
    ('2023-02-01', 'Bob Brown', '555-5678', 'bob.brown@example.com', 'Remote');

-- Step 21: Insert sample data into the Ref_Priority_Levels table
INSERT INTO Ref_Priority_Levels (priority_level_code, priority_level_description)
VALUES 
    ('HI', 'High'),
    ('MED', 'Medium'),
    ('LOW', 'Low');

-- Step 22: Insert sample data into the Ref_Problem_Status_Codes table
INSERT INTO Ref_Problem_Status_Codes (problem_status_code, problem_status_description)
VALUES 
    ('OPEN', 'Open'),
    ('ASSIGNED', 'Assigned'),
    ('CLOSED', 'Closed');

-- Step 23: Insert sample data into the Problem_History table
INSERT INTO Problem_History (priority_level_code, problem_id, problem_status_code, assigned_staff_id, fix_datetime)
VALUES 
    ('HI', 1, 'ASSIGNED', 1, '2023-03-01 12:00:00'),
    ('MED', 2, 'OPEN', 2, NULL);

-- Step 24: Insert sample data into the Resolutions table
INSERT INTO Resolutions (problem_history_id, resolution_description)
VALUES 
    (1, 'Replaced the battery.'),
    (2, 'Replaced the screen.');

-- Step 25: View the resulting tables
SELECT * FROM Ref_Equipment_Types;
SELECT * FROM Equipment;
SELECT * FROM Ref_User_Types;
SELECT * FROM Users;
SELECT * FROM Problems;
SELECT * FROM Ref_Skill_Codes;
SELECT * FROM Support_Staff;
SELECT * FROM Ref_Priority_Levels;
SELECT * FROM Ref_Problem_Status_Codes;
SELECT * FROM Problem_History;
SELECT * FROM Resolutions;
