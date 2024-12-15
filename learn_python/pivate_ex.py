class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance  # Return the current balance (type: int)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Add the deposit to the current balance.
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


account = BankAccount("John Doe", 1000)
print(f"Account holder: {account.owner}")
print(f"Balance: {account.get_balance()}")
account.deposit(500)  # Calling the deposit method to add 500 to the balance.
account.withdraw(200)
