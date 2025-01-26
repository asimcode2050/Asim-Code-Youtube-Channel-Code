-- Step 1: Create the database
CREATE DATABASE payroll_system;

-- Step 2: Select the database
USE payroll_system;

-- Step 3: Create the Ref_Adjustment_Categories table
CREATE TABLE IF NOT EXISTS Ref_Adjustment_Categories (
    deduction_category_code VARCHAR(50) PRIMARY KEY,
    parent_deduction_category_code VARCHAR(50),
    deduction_or_addition CHAR(1),
    deduction_category_description VARCHAR(255)
);

-- Step 4: Create the Ref_Adjustment_Types table
CREATE TABLE IF NOT EXISTS Ref_Adjustment_Types (
    deduction_type_code VARCHAR(50) PRIMARY KEY,
    deduction_category_code VARCHAR(50),
    deduction_type_description VARCHAR(255),
    FOREIGN KEY (deduction_category_code) REFERENCES Ref_Adjustment_Categories(deduction_category_code)
);

-- Step 5: Create the Ref_Payment_Frequencies table
CREATE TABLE IF NOT EXISTS Ref_Payment_Frequencies (
    frequency_code VARCHAR(50) PRIMARY KEY,
    frequency_description VARCHAR(255)
);

-- Step 6: Create the Ref_Job_Titles table
CREATE TABLE IF NOT EXISTS Ref_Job_Titles (
    job_title_code VARCHAR(50) PRIMARY KEY,
    payment_frequency_code VARCHAR(50),
    standard_pay DECIMAL(10, 2),
    job_title VARCHAR(255),
    FOREIGN KEY (payment_frequency_code) REFERENCES Ref_Payment_Frequencies(frequency_code)
);

-- Step 7: Create the Ref_Calendar table
CREATE TABLE IF NOT EXISTS Ref_Calendar (
    pay_period_id INT PRIMARY KEY,
    day_date DATE,
    day_number INT
);

-- Step 8: Create the Adjustment_Rules table
CREATE TABLE IF NOT EXISTS Adjustment_Rules (
    rule_id INT PRIMARY KEY,
    deduction_type_code VARCHAR(50),
    rule_name VARCHAR(255),
    rule_description VARCHAR(255),
    FOREIGN KEY (deduction_type_code) REFERENCES Ref_Adjustment_Types(deduction_type_code)
);

-- Step 9: Create the Adjustment_Rule_Lines table
CREATE TABLE IF NOT EXISTS Adjustment_Rule_Lines (
    rule_id INT,
    line_sequence INT,
    rule_sql_or_text TEXT,
    PRIMARY KEY (rule_id, line_sequence),
    FOREIGN KEY (rule_id) REFERENCES Adjustment_Rules(rule_id)
);

-- Step 10: Create the Employee_Pay_Adjustments table
CREATE TABLE IF NOT EXISTS Employee_Pay_Adjustments (
    pay_period_id INT,
    employee_id INT,
    adjustment_type_code VARCHAR(50),
    adjustment_amount DECIMAL(10, 2),
    comment VARCHAR(255),
    PRIMARY KEY (pay_period_id, employee_id, adjustment_type_code),
    FOREIGN KEY (pay_period_id) REFERENCES Ref_Calendar(pay_period_id),
    FOREIGN KEY (adjustment_type_code) REFERENCES Ref_Adjustment_Types(deduction_type_code)
);

-- Step 11: Insert sample data into Ref_Adjustment_Categories
INSERT INTO Ref_Adjustment_Categories (deduction_category_code, parent_deduction_category_code, deduction_or_addition, deduction_category_description)
VALUES ('TAX', NULL, 'D', 'Tax Deductions'),
       ('INS', NULL, 'D', 'Insurance Deductions');

-- Step 12: Insert sample data into Ref_Adjustment_Types
INSERT INTO Ref_Adjustment_Types (deduction_type_code, deduction_category_code, deduction_type_description)
VALUES ('PAYE', 'TAX', 'Pay As You Earn Tax'),
       ('BLUE', 'INS', 'Blue Cross Insurance');

-- Step 13: Insert sample data into Ref_Payment_Frequencies
INSERT INTO Ref_Payment_Frequencies (frequency_code, frequency_description)
VALUES ('MONTHLY', 'Monthly Payments'),
       ('WEEKLY', 'Weekly Payments');

-- Step 14: Insert sample data into Ref_Job_Titles
INSERT INTO Ref_Job_Titles (job_title_code, payment_frequency_code, standard_pay, job_title)
VALUES ('MGR', 'MONTHLY', 5000.00, 'Manager'),
       ('DEV', 'WEEKLY', 1200.00, 'Developer');

-- Step 15: Insert sample data into Ref_Calendar
INSERT INTO Ref_Calendar (pay_period_id, day_date, day_number)
VALUES (1, '2023-10-01', 1),
       (2, '2023-10-08', 2);

-- Step 16: Insert sample data into Adjustment_Rules
INSERT INTO Adjustment_Rules (rule_id, deduction_type_code, rule_name, rule_description)
VALUES (1, 'PAYE', 'Tax Rule 1', 'Standard Tax Deduction'),
       (2, 'BLUE', 'Insurance Rule 1', 'Standard Insurance Deduction');

-- Step 17: Insert sample data into Adjustment_Rule_Lines
INSERT INTO Adjustment_Rule_Lines (rule_id, line_sequence, rule_sql_or_text)
VALUES (1, 1, 'Deduct 20% of gross pay'),
       (2, 1, 'Deduct $100 for insurance');

-- Step 18: Insert sample data into Employee_Pay_Adjustments
INSERT INTO Employee_Pay_Adjustments (pay_period_id, employee_id, adjustment_type_code, adjustment_amount, comment)
VALUES (1, 101, 'PAYE', 1000.00, 'Tax Deduction for October'),
       (2, 102, 'BLUE', 100.00, 'Insurance Deduction for October');

-- Final Step: Display all tables as a single view
SELECT 'Ref_Adjustment_Categories' AS Table_Name, deduction_category_code AS ID, parent_deduction_category_code AS Column1, deduction_or_addition AS Column2, deduction_category_description AS Column3, NULL AS Column4, NULL AS Column5, NULL AS Column6, NULL AS Column7, NULL AS Column8, NULL AS Column9, NULL AS Column10 FROM Ref_Adjustment_Categories
UNION ALL
SELECT 'Ref_Adjustment_Types', deduction_type_code, deduction_category_code, deduction_type_description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Adjustment_Types
UNION ALL
SELECT 'Ref_Payment_Frequencies', frequency_code, frequency_description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Payment_Frequencies
UNION ALL
SELECT 'Ref_Job_Titles', job_title_code, payment_frequency_code, standard_pay, job_title, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Job_Titles
UNION ALL
SELECT 'Ref_Calendar', pay_period_id, day_date, day_number, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Calendar
UNION ALL
SELECT 'Adjustment_Rules', rule_id, deduction_type_code, rule_name, rule_description, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Adjustment_Rules
UNION ALL
SELECT 'Adjustment_Rule_Lines', rule_id, line_sequence, rule_sql_or_text, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Adjustment_Rule_Lines
UNION ALL
SELECT 'Employee_Pay_Adjustments', pay_period_id, employee_id, adjustment_type_code, adjustment_amount, comment, NULL, NULL, NULL, NULL, NULL, NULL FROM Employee_Pay_Adjustments;
