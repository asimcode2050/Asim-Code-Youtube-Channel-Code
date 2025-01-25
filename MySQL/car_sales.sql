-- Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID INT AUTO_INCREMENT,
    cell_Mobile_Phone VARCHAR(15),
    email_Address VARCHAR(255),
    other_Customer_Details TEXT,
    PRIMARY KEY (Customer_ID)
);

-- Insert sample data into the Customers table
INSERT INTO Customers (cell_Mobile_Phone, email_Address, other_Customer_Details)
VALUES ('123-456-7890', 'john.doe@example.com', 'Regular customer'),
       ('234-567-8901', 'jane.smith@example.com', 'VIP customer');

-- Create the Car_Features table
CREATE TABLE IF NOT EXISTS Car_Features (
    car_Feature_ID INT AUTO_INCREMENT,
    car_Feature_Description VARCHAR(255),
    PRIMARY KEY (car_Feature_ID)
);

-- Insert sample data into the Car_Features table
INSERT INTO Car_Features (car_Feature_Description)
VALUES ('Air-Conditioning'),
       ('Sunroof'),
       ('Leather Seats');

-- Create the Cars_for_Sale table
CREATE TABLE IF NOT EXISTS Cars_for_Sale (
    Clear_for_Sale_ID INT AUTO_INCREMENT,
    manufacturer_ShortName VARCHAR(255),
    model_Code VARCHAR(255),
    vehicle_Category_Code VARCHAR(255),
    asking_Price DECIMAL(10, 2),
    current_Mileage INT,
    date_Acquired DATE,
    registration_Year YEAR,
    other_Car_Details TEXT,
    PRIMARY KEY (Clear_for_Sale_ID)
);

-- Insert sample data into the Cars_for_Sale table
INSERT INTO Cars_for_Sale (manufacturer_ShortName, model_Code, vehicle_Category_Code, asking_Price, current_Mileage, date_Acquired, registration_Year, other_Car_Details)
VALUES ('Toyota', 'Camry', 'Sedan', 20000.00, 15000, '2022-01-15', 2022, 'Excellent condition'),
       ('Honda', 'Civic', 'Compact', 18000.00, 12000, '2021-11-20', 2021, 'Low mileage');

-- Create the Car_Models table
CREATE TABLE IF NOT EXISTS Car_Models (
    model_Code VARCHAR(255),
    manufacturer_code VARCHAR(255),
    model_Name VARCHAR(255),
    PRIMARY KEY (model_Code)
);

-- Insert sample data into the Car_Models table
INSERT INTO Car_Models (model_Code, manufacturer_code, model_Name)
VALUES ('Camry', 'Toyota', 'Toyota Camry'),
       ('Civic', 'Honda', 'Honda Civic');

-- Create the Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    address_ID INT AUTO_INCREMENT,
    customer_ID INT,
    address_time_1 VARCHAR(255),
    address_time_2 VARCHAR(255),
    address_time_3 VARCHAR(255),
    address_time_4 VARCHAR(255),
    town_city VARCHAR(255),
    state_County_Province VARCHAR(255),
    Country VARCHAR(255),
    post_Zip_Code VARCHAR(20),
    other_Address_Details TEXT,
    PRIMARY KEY (address_ID),
    FOREIGN KEY (customer_ID) REFERENCES Customers(Customer_ID)
);

-- Insert sample data into the Addresses table
INSERT INTO Addresses (customer_ID, address_time_1, town_city, state_County_Province, Country, post_Zip_Code)
VALUES (1, '123 Main St', 'Springfield', 'IL', 'USA', '62701'),
       (2, '456 Elm St', 'Shelbyville', 'IL', 'USA', '62702');

-- Create the Customer_Preferences table
CREATE TABLE IF NOT EXISTS Customer_Preferences (
    customer_Preference_ID INT AUTO_INCREMENT,
    car_Feature_ID INT,
    customer_ID INT,
    customer_Preference_Details TEXT,
    PRIMARY KEY (customer_Preference_ID),
    FOREIGN KEY (car_Feature_ID) REFERENCES Car_Features(car_Feature_ID),
    FOREIGN KEY (customer_ID) REFERENCES Customers(Customer_ID)
);

-- Insert sample data into the Customer_Preferences table
INSERT INTO Customer_Preferences (car_Feature_ID, customer_ID, customer_Preference_Details)
VALUES (1, 1, 'Prefers cars with air-conditioning'),
       (2, 2, 'Prefers cars with sunroof');

-- Create the features_on_Cars_for_Sale table
CREATE TABLE IF NOT EXISTS features_on_Cars_for_Sale (
    car_for_Sale_ID INT,
    car_Feature_ID INT,
    PRIMARY KEY (car_for_Sale_ID, car_Feature_ID),
    FOREIGN KEY (car_for_Sale_ID) REFERENCES Cars_for_Sale(Clear_for_Sale_ID),
    FOREIGN KEY (car_Feature_ID) REFERENCES Car_Features(car_Feature_ID)
);

-- Insert sample data into the features_on_Cars_for_Sale table
INSERT INTO features_on_Cars_for_Sale (car_for_Sale_ID, car_Feature_ID)
VALUES (1, 1),
       (2, 2);

-- Create the Vehicle_Categories table
CREATE TABLE IF NOT EXISTS Vehicle_Categories (
    vehicle_Category_Code VARCHAR(255),
    vehicle_Category_Description VARCHAR(255),
    PRIMARY KEY (vehicle_Category_Code)
);

-- Insert sample data into the Vehicle_Categories table
INSERT INTO Vehicle_Categories (vehicle_Category_Code, vehicle_Category_Description)
VALUES ('Sedan', '4-door sedan'),
       ('Compact', 'Compact car');

-- Create the Payment_Status table
CREATE TABLE IF NOT EXISTS Payment_Status (
    payment_Status_Code VARCHAR(255),
    payment_Status_Description VARCHAR(255),
    PRIMARY KEY (payment_Status_Code)
);

-- Insert sample data into the Payment_Status table
INSERT INTO Payment_Status (payment_Status_Code, payment_Status_Description)
VALUES ('Paid', 'Payment completed'),
       ('Pending', 'Payment pending');

-- Create the Cars_Sold table
CREATE TABLE IF NOT EXISTS Cars_Sold (
    car_Sold_ID INT AUTO_INCREMENT,
    car_for_Sale_ID INT,
    customer_ID INT,
    agreed_Price DECIMAL(10, 2),
    date_Sold DATE,
    monthly_Payment_Amount DECIMAL(10, 2),
    monthly_Payment_Date DATE,
    other_Details TEXT,
    PRIMARY KEY (car_Sold_ID),
    FOREIGN KEY (car_for_Sale_ID) REFERENCES Cars_for_Sale(Clear_for_Sale_ID),
    FOREIGN KEY (customer_ID) REFERENCES Customers(Customer_ID)
);

-- Insert sample data into the Cars_Sold table
INSERT INTO Cars_Sold (car_for_Sale_ID, customer_ID, agreed_Price, date_Sold, monthly_Payment_Amount, monthly_Payment_Date, other_Details)
VALUES (1, 1, 19500.00, '2023-03-01', 500.00, '2023-04-01', 'Financed through bank'),
       (2, 2, 17500.00, '2023-03-15', 450.00, '2023-04-15', 'Financed through credit union');

-- Create the Customer_Payments table
CREATE TABLE IF NOT EXISTS Customer_Payments (
    customer_Payment_ID INT AUTO_INCREMENT,
    car_Sold_ID INT,
    customer_ID INT,
    payment_Status_Code VARCHAR(255),
    customer_Payment_Date_Due DATE,
    customer_Payment_Date_Made DATE,
    actual_Payment_Amount DECIMAL(10, 2),
    PRIMARY KEY (customer_Payment_ID),
    FOREIGN KEY (car_Sold_ID) REFERENCES Cars_Sold(car_Sold_ID),
    FOREIGN KEY (customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (payment_Status_Code) REFERENCES Payment_Status(payment_Status_Code)
);

-- Insert sample data into the Customer_Payments table
INSERT INTO Customer_Payments (car_Sold_ID, customer_ID, payment_Status_Code, customer_Payment_Date_Due, customer_Payment_Date_Made, actual_Payment_Amount)
VALUES (1, 1, 'Paid', '2023-04-01', '2023-04-01', 500.00),
       (2, 2, 'Pending', '2023-04-15', NULL, 450.00);

-- Create the Finance_Companies table
CREATE TABLE IF NOT EXISTS Finance_Companies (
    finance_Company_ID INT AUTO_INCREMENT,
    finance_Company_Name VARCHAR(255),
    other_Details TEXT,
    PRIMARY KEY (finance_Company_ID)
);

-- Insert sample data into the Finance_Companies table
INSERT INTO Finance_Companies (finance_Company_Name)
VALUES ('Bank of America'),
       ('Chase');

-- Create the Car_Loans table
CREATE TABLE IF NOT EXISTS Car_Loans (
    loan_ID INT AUTO_INCREMENT,
    car_Sold_ID INT,
    repayment_Start_date DATE,
    repayment_End_Date DATE,
    monthly_Repayments DECIMAL(10, 2),
    other_Details TEXT,
    finance_Company_ID INT,
    PRIMARY KEY (loan_ID),
    FOREIGN KEY (car_Sold_ID) REFERENCES Cars_Sold(car_Sold_ID),
    FOREIGN KEY (finance_Company_ID) REFERENCES Finance_Companies(finance_Company_ID)
);

-- Insert sample data into the Car_Loans table
INSERT INTO Car_Loans (car_Sold_ID, repayment_Start_date, repayment_End_Date, monthly_Repayments, finance_Company_ID)
VALUES (1, '2023-04-01', '2025-04-01', 500.00, 1),
       (2, '2023-04-15', '2025-04-15', 450.00, 2);

-- Create the Insurance_Companies table
CREATE TABLE IF NOT EXISTS Insurance_Companies (
    insurance_Company_ID INT AUTO_INCREMENT,
    insurance_Company_Name VARCHAR(255),
    other_Details TEXT,
    PRIMARY KEY (insurance_Company_ID)
);

-- Insert sample data into the Insurance_Companies table
INSERT INTO Insurance_Companies (insurance_Company_Name)
VALUES ('Geico'),
       ('State Farm');

-- Create the Insurance_Policies table
CREATE TABLE IF NOT EXISTS Insurance_Policies (
    policy_ID INT AUTO_INCREMENT,
    car_Sold_ID INT,
    insurance_Company_ID INT,
    policy_Start_date DATE,
    policy_Renewal_Date DATE,
    monthly_Payments DECIMAL(10, 2),
    other_Details TEXT,
    PRIMARY KEY (policy_ID),
    FOREIGN KEY (car_Sold_ID) REFERENCES Cars_Sold(car_Sold_ID),
    FOREIGN KEY (insurance_Company_ID) REFERENCES Insurance_Companies(insurance_Company_ID)
);

-- Insert sample data into the Insurance_Policies table
INSERT INTO Insurance_Policies (car_Sold_ID, insurance_Company_ID, policy_Start_date, policy_Renewal_Date, monthly_Payments)
VALUES (1, 1, '2023-04-01', '2024-04-01', 100.00),
       (2, 2, '2023-04-15', '2024-04-15', 90.00);

-- Display all tables as a single view
SELECT 'Customers' AS Table_Name, Customer_ID AS ID, cell_Mobile_Phone AS Column1, email_Address AS Column2, other_Customer_Details AS Column3, NULL AS Column4, NULL AS Column5, NULL AS Column6, NULL AS Column7, NULL AS Column8, NULL AS Column9, NULL AS Column10 FROM Customers
UNION ALL
SELECT 'Car_Features', car_Feature_ID, car_Feature_Description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Car_Features
UNION ALL
SELECT 'Cars_for_Sale', Clear_for_Sale_ID, manufacturer_ShortName, model_Code, vehicle_Category_Code, asking_Price, current_Mileage, date_Acquired, registration_Year, other_Car_Details, NULL, NULL FROM Cars_for_Sale
UNION ALL
SELECT 'Car_Models', NULL, model_Code, manufacturer_code, model_Name, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Car_Models
UNION ALL
SELECT 'Addresses', address_ID, address_time_1, address_time_2, address_time_3, address_time_4, town_city, state_County_Province, Country, post_Zip_Code, other_Address_Details, NULL FROM Addresses
UNION ALL
SELECT 'Customer_Preferences', customer_Preference_ID, car_Feature_ID, customer_ID, customer_Preference_Details, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Customer_Preferences
UNION ALL
SELECT 'features_on_Cars_for_Sale', car_for_Sale_ID, car_Feature_ID, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM features_on_Cars_for_Sale
UNION ALL
SELECT 'Vehicle_Categories', NULL, vehicle_Category_Code, vehicle_Category_Description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Vehicle_Categories
UNION ALL
SELECT 'Payment_Status', NULL, payment_Status_Code, payment_Status_Description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Payment_Status
UNION ALL
SELECT 'Cars_Sold', car_Sold_ID, car_for_Sale_ID, customer_ID, agreed_Price, date_Sold, monthly_Payment_Amount, monthly_Payment_Date, other_Details, NULL, NULL, NULL FROM Cars_Sold
UNION ALL
SELECT 'Customer_Payments', customer_Payment_ID, car_Sold_ID, customer_ID, payment_Status_Code, customer_Payment_Date_Due, customer_Payment_Date_Made, actual_Payment_Amount, NULL, NULL, NULL, NULL FROM Customer_Payments
UNION ALL
SELECT 'Finance_Companies', finance_Company_ID, finance_Company_Name, other_Details, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Finance_Companies
UNION ALL
SELECT 'Car_Loans', loan_ID, car_Sold_ID, repayment_Start_date, repayment_End_Date, monthly_Repayments, other_Details, finance_Company_ID, NULL, NULL, NULL, NULL FROM Car_Loans
UNION ALL
SELECT 'Insurance_Companies', insurance_Company_ID, insurance_Company_Name, other_Details, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Insurance_Companies
UNION ALL
SELECT 'Insurance_Policies', policy_ID, car_Sold_ID, insurance_Company_ID, policy_Start_date, policy_Renewal_Date, monthly_Payments, other_Details, NULL, NULL, NULL, NULL FROM Insurance_Policies;
