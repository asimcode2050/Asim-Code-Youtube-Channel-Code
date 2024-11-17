import sqlite3
connection = sqlite3.connect("customer_data.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT
)
''')


def add_customer(name, email, phone):
    cursor.execute('''
    INSERT INTO customers (name, email, phone)
    VALUES (?, ?, ?)
    ''', (name, email, phone))
    connection.commit()
    print("Customer added successfully!")


def display_customers():
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {
              customer[2]}, Phone: {customer[3]}")


def find_customer_by_email(email):
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    customer = cursor.fetchone()
    if customer:
        print(f"Customer found: ID: {customer[0]}, Name: {
              customer[1]}, Email: {customer[2]}, Phone: {customer[3]}")
    else:
        print("No customer found with that email.")


add_customer("John Doe", "johndoe@example.com", "123-456-7890")
add_customer("Jane Smith", "janesmith@example.com", "987-654-3210")
display_customers()
find_customer_by_email("johndoe@example.com")
connection.close()
