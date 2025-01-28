-- Step 1: Create the Pizza Deliveries database
CREATE DATABASE IF NOT EXISTS Pizza_Deliveries;

-- Step 2: Select the Pizza Deliveries database
USE Pizza_Deliveries;

-- Step 3: Create the Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    address_id INT PRIMARY KEY,
    line_1 VARCHAR(100),
    line_2 VARCHAR(100),
    line_3 VARCHAR(100),
    line_4 VARCHAR(100),
    city VARCHAR(50),
    zip_postcode VARCHAR(10),
    state_province_county VARCHAR(50),
    country VARCHAR(50),
    other_address_details VARCHAR(255)
);

-- Step 4: Create the Ref_Payment_Methods table
CREATE TABLE IF NOT EXISTS Ref_Payment_Methods (
    payment_method_code VARCHAR(10) PRIMARY KEY,
    payment_method_description VARCHAR(50)
);

-- Step 5: Create the Ref_Vehicle_Types table
CREATE TABLE IF NOT EXISTS Ref_Vehicle_Types (
    vehicle_type_code VARCHAR(10) PRIMARY KEY,
    vehicle_type_description VARCHAR(50)
);

-- Step 6: Create the Ref_Delivery_Status table
CREATE TABLE IF NOT EXISTS Ref_Delivery_Status (
    delivery_status_code VARCHAR(10) PRIMARY KEY,
    delivery_status_description VARCHAR(50)
);

-- Step 7: Create the Ref_Base_Types table
CREATE TABLE IF NOT EXISTS Ref_Base_Types (
    base_type_code VARCHAR(10) PRIMARY KEY,
    base_type_price DECIMAL(10, 2),
    base_type_description VARCHAR(50)
);

-- Step 8: Create the Ref_Toppings table
CREATE TABLE IF NOT EXISTS Ref_Toppings (
    topping_code VARCHAR(10) PRIMARY KEY,
    topping_price DECIMAL(10, 2),
    topping_description VARCHAR(50)
);

-- Step 9: Create the Vehicles table
CREATE TABLE IF NOT EXISTS Vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_type_code VARCHAR(10),
    vehicle_licence_number VARCHAR(20),
    vehicle_details VARCHAR(255),
    FOREIGN KEY (vehicle_type_code) REFERENCES Ref_Vehicle_Types(vehicle_type_code)
);

-- Step 10: Create the Employees table
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INT PRIMARY KEY,
    employee_address_id INT,
    employee_name VARCHAR(100),
    employee_phone VARCHAR(15),
    other_employee_details VARCHAR(255),
    FOREIGN KEY (employee_address_id) REFERENCES Addresses(address_id)
);

-- Step 11: Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_address_id INT,
    payment_method_code VARCHAR(10),
    customer_name VARCHAR(100),
    customer_phone VARCHAR(15),
    customer_email VARCHAR(100),
    date_of_first_order DATE,
    other_customer_details VARCHAR(255),
    FOREIGN KEY (customer_address_id) REFERENCES Addresses(address_id),
    FOREIGN KEY (payment_method_code) REFERENCES Ref_Payment_Methods(payment_method_code)
);

-- Step 12: Create the Orders table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    taken_by_employee_id INT,
    delivered_by_employee_id INT,
    delivery_status_code VARCHAR(10),
    vehicle_id INT,
    datetime_order_taken DATETIME,
    datetime_order_delivered DATETIME,
    total_order_price DECIMAL(10, 2),
    other_order_details VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (taken_by_employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (delivered_by_employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (delivery_status_code) REFERENCES Ref_Delivery_Status(delivery_status_code),
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)
);

-- Step 13: Create the Pizzas_Ordered table
CREATE TABLE IF NOT EXISTS Pizzas_Ordered (
    order_id INT,
    pizza_sequence_number INT,
    base_type_code VARCHAR(10),
    total_pizza_price DECIMAL(10, 2),
    PRIMARY KEY (order_id, pizza_sequence_number),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (base_type_code) REFERENCES Ref_Base_Types(base_type_code)
);

-- Step 14: Create the Toppings table
CREATE TABLE IF NOT EXISTS Toppings (
    order_id INT,
    pizza_sequence_number INT,
    topping_sequence_number INT,
    topping_code VARCHAR(10),
    PRIMARY KEY (order_id, pizza_sequence_number, topping_sequence_number),
    FOREIGN KEY (order_id, pizza_sequence_number) REFERENCES Pizzas_Ordered(order_id, pizza_sequence_number),
    FOREIGN KEY (topping_code) REFERENCES Ref_Toppings(topping_code)
);

-- Step 15: Insert sample data into the Addresses table
INSERT INTO Addresses (address_id, line_1, city, zip_postcode, country)
VALUES 
    (1, '123 Main St', 'Springfield', '12345', 'USA');

-- Step 16: Insert sample data into the Ref_Payment_Methods table
INSERT INTO Ref_Payment_Methods (payment_method_code, payment_method_description)
VALUES 
    ('CASH', 'Cash'),
    ('CC', 'Credit Card');

-- Step 17: Insert sample data into the Ref_Vehicle_Types table
INSERT INTO Ref_Vehicle_Types (vehicle_type_code, vehicle_type_description)
VALUES 
    ('BIKE', 'Bicycle'),
    ('CAR', 'Car');

-- Step 18: Insert sample data into the Ref_Delivery_Status table
INSERT INTO Ref_Delivery_Status (delivery_status_code, delivery_status_description)
VALUES 
    ('COMP', 'Completed'),
    ('RET', 'Returned');

-- Step 19: Insert sample data into the Ref_Base_Types table
INSERT INTO Ref_Base_Types (base_type_code, base_type_price, base_type_description)
VALUES 
    ('THIN', 5.00, 'Thin Crust'),
    ('DEEP', 7.00, 'Deep Dish');

-- Step 20: Insert sample data into the Ref_Toppings table
INSERT INTO Ref_Toppings (topping_code, topping_price, topping_description)
VALUES 
    ('HAM', 1.50, 'Ham'),
    ('PINE', 1.00, 'Pineapple');

-- Step 21: Insert sample data into the Vehicles table
INSERT INTO Vehicles (vehicle_id, vehicle_type_code, vehicle_licence_number)
VALUES 
    (1, 'BIKE', 'BIKE123');

-- Step 22: Insert sample data into the Employees table
INSERT INTO Employees (employee_id, employee_address_id, employee_name, employee_phone)
VALUES 
    (1, 1, 'Jane Smith', '987-654-3210');

-- Step 23: Insert sample data into the Customers table
INSERT INTO Customers (customer_id, customer_address_id, payment_method_code, customer_name, customer_phone, customer_email, date_of_first_order)
VALUES 
    (1, 1, 'CASH', 'John Doe', '123-456-7890', 'john.doe@example.com', '2023-01-01');

-- Step 24: Insert sample data into the Orders table
INSERT INTO Orders (order_id, customer_id, taken_by_employee_id, delivered_by_employee_id, delivery_status_code, vehicle_id, datetime_order_taken, total_order_price)
VALUES 
    (1, 1, 1, 1, 'COMP', 1, '2023-01-01 12:00:00', 15.00);

-- Step 25: Insert sample data into the Pizzas_Ordered table
INSERT INTO Pizzas_Ordered (order_id, pizza_sequence_number, base_type_code, total_pizza_price)
VALUES 
    (1, 1, 'THIN', 10.00);

-- Step 26: Insert sample data into the Toppings table
INSERT INTO Toppings (order_id, pizza_sequence_number, topping_sequence_number, topping_code)
VALUES 
    (1, 1, 1, 'HAM'),
    (1, 1, 2, 'PINE');

-- Step 27: View the resulting tables
SELECT * FROM Customers;

SELECT * FROM Addresses;

SELECT * FROM Ref_Payment_Methods;

SELECT * FROM Ref_Delivery_Status;

SELECT * FROM Employees;

SELECT * FROM Vehicles;

SELECT * FROM Ref_Vehicle_Types;

SELECT * FROM Ref_Base_Types;

SELECT * FROM Ref_Toppings;

SELECT * FROM Orders;

SELECT * FROM Pizzas_Ordered;

SELECT * FROM Toppings;
