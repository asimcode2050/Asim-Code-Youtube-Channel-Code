-- Create the Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    line_1 VARCHAR(255),
    line_2 VARCHAR(255),
    line_3 VARCHAR(255),
    city VARCHAR(255),
    zip_or_postcode VARCHAR(20),
    state_province_country VARCHAR(255),
    country VARCHAR(255),
    other_address_details TEXT
);

-- Insert sample data into the Addresses table
INSERT INTO Addresses (line_1, line_2, line_3, city, zip_or_postcode, state_province_country, country, other_address_details)
VALUES ('123 Main St', 'Apt 4B', NULL, 'Springfield', '62701', 'IL', 'USA', 'Headquarters'),
       ('456 Elm St', NULL, NULL, 'Shelbyville', '62702', 'IL', 'USA', 'Warehouse');

-- Create the Suppliers table
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(255),
    supplier_email VARCHAR(255),
    supplier_phone VARCHAR(15),
    supplier_cell_phone VARCHAR(15),
    other_supplier_details TEXT
);

-- Insert sample data into the Suppliers table
INSERT INTO Suppliers (supplier_name, supplier_email, supplier_phone, supplier_cell_phone, other_supplier_details)
VALUES ('Supplier A', 'supplierA@example.com', '123-456-7890', '234-567-8901', 'Primary supplier'),
       ('Supplier B', 'supplierB@example.com', '345-678-9012', '456-789-0123', 'Secondary supplier');

-- Create the Ref_Item_Categories table
CREATE TABLE IF NOT EXISTS Ref_Item_Categories (
    item_category_code VARCHAR(255) PRIMARY KEY,
    item_category_description VARCHAR(255)
);

-- Insert sample data into the Ref_Item_Categories table
INSERT INTO Ref_Item_Categories (item_category_code, item_category_description)
VALUES ('CAMERA', 'Digital Camera'),
       ('LAPTOP', 'Laptop Computers');

-- Create the Brands table
CREATE TABLE IF NOT EXISTS Brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_short_name VARCHAR(255),
    brand_full_name VARCHAR(255)
);

-- Insert sample data into the Brands table
INSERT INTO Brands (brand_short_name, brand_full_name)
VALUES ('Nikon', 'Nikon Corporation'),
       ('Olympus', 'Olympus Corporation');

-- Create the Ref_Address_Types table
CREATE TABLE IF NOT EXISTS Ref_Address_Types (
    address_type_code VARCHAR(255) PRIMARY KEY,
    address_type_description VARCHAR(255)
);

-- Insert sample data into the Ref_Address_Types table
INSERT INTO Ref_Address_Types (address_type_code, address_type_description)
VALUES ('HQ', 'Headquarters'),
       ('WH', 'Warehouse');

-- Create the Supplier_Addresses table
CREATE TABLE IF NOT EXISTS Supplier_Addresses (
    supplier_address_id INT AUTO_INCREMENT PRIMARY KEY,
    address_id INT,
    supplier_id INT,
    address_type_code VARCHAR(255),
    date_address_from DATE,
    date_address_to DATE,
    FOREIGN KEY (address_id) REFERENCES Addresses(address_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id),
    FOREIGN KEY (address_type_code) REFERENCES Ref_Address_Types(address_type_code)
);

-- Insert sample data into the Supplier_Addresses table
INSERT INTO Supplier_Addresses (address_id, supplier_id, address_type_code, date_address_from, date_address_to)
VALUES (1, 1, 'HQ', '2023-01-01', NULL);

-- Create the Inventory_Items table
CREATE TABLE IF NOT EXISTS Inventory_Items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT,
    item_category_code VARCHAR(255),
    item_description VARCHAR(255),
    average_monthly_usage INT,
    reorder_level INT,
    reorder_quantity INT,
    other_item_details TEXT,
    FOREIGN KEY (brand_id) REFERENCES Brands(brand_id),
    FOREIGN KEY (item_category_code) REFERENCES Ref_Item_Categories(item_category_code)
);

-- Insert sample data into the Inventory_Items table
INSERT INTO Inventory_Items (brand_id, item_category_code, item_description, average_monthly_usage, reorder_level, reorder_quantity, other_item_details)
VALUES (1, 'CAMERA', 'Nikon DSLR Camera', 50, 20, 100, 'High-demand item');

-- Create the Item_Suppliers table
CREATE TABLE IF NOT EXISTS Item_Suppliers (
    item_id INT,
    supplier_id INT,
    value_supplied_to_date DECIMAL(10, 2),
    total_quantity_supplied_to_date INT,
    first_item_supplied_date DATE,
    last_item_supplied_date DATE,
    delivery_lead_time INT,
    standard_price DECIMAL(10, 2),
    percentage_discount DECIMAL(5, 2),
    minimum_order_quantity INT,
    maximum_order_quantity INT,
    other_item_suppliers_details TEXT,
    PRIMARY KEY (item_id, supplier_id),
    FOREIGN KEY (item_id) REFERENCES Inventory_Items(item_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- Insert sample data into the Item_Suppliers table
INSERT INTO Item_Suppliers (item_id, supplier_id, value_supplied_to_date, total_quantity_supplied_to_date, first_item_supplied_date, last_item_supplied_date, delivery_lead_time, standard_price, percentage_discount, minimum_order_quantity, maximum_order_quantity, other_item_suppliers_details)
VALUES (1, 1, 5000.00, 100, '2023-01-01', '2023-10-01', 7, 50.00, 10.00, 10, 100, 'Primary supplier for cameras');

-- Create the Item_Stock_Levels table
CREATE TABLE IF NOT EXISTS Item_Stock_Levels (
    item_id INT,
    stock_taking_date DATE,
    quantity_in_stock INT,
    PRIMARY KEY (item_id, stock_taking_date),
    FOREIGN KEY (item_id) REFERENCES Inventory_Items(item_id)
);

-- Insert sample data into the Item_Stock_Levels table
INSERT INTO Item_Stock_Levels (item_id, stock_taking_date, quantity_in_stock)
VALUES (1, '2023-10-01', 150);

-- Final Query to Show All Tables as a Single View
SELECT 'Addresses' AS Table_Name, address_id AS ID, line_1 AS Column1, line_2 AS Column2, line_3 AS Column3, city AS Column4, zip_or_postcode AS Column5, state_province_country AS Column6, country AS Column7, other_address_details AS Column8, NULL AS Column9, NULL AS Column10 FROM Addresses
UNION ALL
SELECT 'Suppliers', supplier_id, supplier_name, supplier_email, supplier_phone, supplier_cell_phone, other_supplier_details, NULL, NULL, NULL, NULL, NULL FROM Suppliers
UNION ALL
SELECT 'Ref_Item_Categories', NULL, item_category_code, item_category_description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Item_Categories
UNION ALL
SELECT 'Brands', brand_id, brand_short_name, brand_full_name, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Brands
UNION ALL
SELECT 'Supplier_Addresses', supplier_address_id, address_id, supplier_id, address_type_code, date_address_from, date_address_to, NULL, NULL, NULL, NULL, NULL FROM Supplier_Addresses
UNION ALL
SELECT 'Ref_Address_Types', NULL, address_type_code, address_type_description, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Ref_Address_Types
UNION ALL
SELECT 'Inventory_Items', item_id, brand_id, item_category_code, item_description, average_monthly_usage, reorder_level, reorder_quantity, other_item_details, NULL, NULL, NULL FROM Inventory_Items
UNION ALL
SELECT 'Item_Suppliers', item_id, supplier_id, value_supplied_to_date, total_quantity_supplied_to_date, first_item_supplied_date, last_item_supplied_date, delivery_lead_time, standard_price, percentage_discount, minimum_order_quantity, maximum_order_quantity FROM Item_Suppliers
UNION ALL
SELECT 'Item_Stock_Levels', item_id, stock_taking_date, quantity_in_stock, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL FROM Item_Stock_Levels;
