"""
Python getpass module
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/p7fr8y11RH0
"""
from getpass import getpass

def get_username_password():
    username = input("Please enter Username: ")
    password = None
    while not password:
        password = getpass("Please enter Password: ")
        password_confirm = getpass("**Confirm Password: ")
        if password != password_confirm:
            print("Passwords do not match!")
            password = None
    print(username, password)
    return username, password


get_username_password()
