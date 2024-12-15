# In Python, private variables are those that are intended to be used only within the class they are defined in, and not accessed directly from outside the class. These variables are typically indicated by prefixing their names with two underscores , such as __variable. This convention triggers name mangling, where Python changes the variables name to include the class name (for example, _ClassName__variable), making it harder (but not impossible) to access from outside the class. The purpose of private variables is to promote encapsulation, preventing accidental modification and ensuring that the internal state of an object is managed properly through methods, such as getters and setters. However, its important to note that Pythons approach to "private" variables is more of a guideline than a strict enforcement.
# This example demonstrates how to create a simple bank account system in Python using the concept of encapsulation with private variables and public methods.
# This is a class definition that simulates a simple BankAccount system.
# The purpose of this class is to model a bank account with an owners name and a balance.
# We will demonstrate the usage of private variables, methods, and encapsulation.
class BankAccount:
    # Constructor method that initializes the BankAccount object.
    # It takes in the owners name and the initial balance as input.
    def __init__(self, owner, balance):
        # 'owner' is a string that stores the name of the account holder. It is a public variable.
        # The type of 'owner' is str (string).
        # Public variable to store account holders name (for example, "John Doe")
        self.owner = owner
        # '__balance' is an integer that stores the balance of the bank account.
        # The type of '__balance' is int (integer).
        # The double underscore makes this a private variable to prevent direct modification.
        # Private variable to store the account balance (for example, 1000)
        self.__balance = balance
    # Function to retrieve the balance of the bank account.
    # This is a getter method that returns the value of the private '__balance'.
    def get_balance(self):
        # The method returns the private '__balance' value to allow controlled access.
        # '__balance' is an integer.
        return self.__balance  # Return the current balance (type: int)
    # Function to deposit money into the account.
    # It takes an amount (int) as a parameter and adds it to the balance.
    def deposit(self, amount):
        # 'amount' is an integer that represents the money to be deposited.
        # The type of 'amount' is int.
        # Logic expression to check if the 'amount' to deposit is positive.
        if amount > 0:
            # The deposit is valid if 'amount' is greater than 0.
            # We modify the private '__balance' by adding the deposit amount.
            # '__balance' is an integer, and we are incrementing it.
            self.__balance += amount  # Add the deposit to the current balance.
            # Print a message showing the deposited amount and the new balance.
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            # If the deposit amount is not positive, print an error message.
            print("Deposit amount must be positive.")

    # Function to withdraw money from the account.
    # It takes an 'amount' as a parameter and deducts it from the balance if possible.
    def withdraw(self, amount):
        # 'amount' is an integer that represents the money to be withdrawn.
        # The type of 'amount' is int.
        # Logic expression to check if the 'amount' is positive and less than or equal to the balance.
        if amount > 0 and amount <= self.__balance:
            # The withdrawal is valid if 'amount' is greater than 0 and less than or equal to '__balance'.
            # We modify the private '__balance' by subtracting the withdrawal amount.
            # '__balance' is an integer, and we are decrementing it.
            # Subtract the withdrawal amount from the balance.
            self.__balance -= amount
            # Print a message showing the withdrawn amount and the new balance.
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            # If the withdrawal conditions are not met (for example, insufficient funds or invalid amount), print an error.
            print("Invalid withdrawal amount or insufficient funds.")
# Creating an object (instance) of the BankAccount class.
# Here, we are creating a bank account for an individual named "John Doe" with an initial balance of 1000.
# Creating a new BankAccount object for John with a balance of 1000.
account = BankAccount("John Doe", 1000)
# Displaying the account holders name. We are accessing the public 'owner' variable.
# 'owner' is a string.
# Output the account holders name (for example, "John Doe")
print(f"Account holder: {account.owner}")
# Using the 'get_balance' method to safely check the account balance.
# This method returns the private '__balance' variables value.
# '__balance' is an integer, and this is a controlled way of accessing it.
# Output the current balance (for example, 1000)
print(f"Balance: {account.get_balance()}")
# Depositing money into the account. Here, we deposit 500 units of currency.
# '500' is the argument passed to the deposit function. The type of '500' is int.
account.deposit(500)  # Calling the deposit method to add 500 to the balance.
# Withdrawing money from the account. Here, we withdraw 200 units of currency.
# '200' is the argument passed to the withdraw function. The type of '200' is int.
# Calling the withdraw method to subtract 200 from the balance.
account.withdraw(200)
