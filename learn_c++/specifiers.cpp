#include <iostream>
using namespace std;
class BankAccount
{
private:
    double balance;

public:
    BankAccount(double initialBalance)
    {
        if (initialBalance > 0)
        {
            balance = initialBalance;
        }
        else
        {
            balance = 0; // If invalid input is given (negative or zero), set balance to zero.
            cout << "Invalid initial balance. Setting balance to zero." << endl;
        }
    }
    void deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
            cout << "Deposited: " << amount << endl;
        }
        else
        {
            cout << "Invalid deposit amount." << endl;
        }
    }
    void withdraw(double amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            cout << "Withdrew: " << amount << endl;
        }
        else
        {
            cout << "Invalid withdrawal amount or insufficient funds." << endl;
        }
    }
    double getBalance() const
    {
        return balance;
    }
};
int main()
{
    BankAccount myAccount(1000);
    cout << "Initial Balance: " << myAccount.getBalance() << endl;
    myAccount.deposit(500);
    cout << "Balance after deposit: " << myAccount.getBalance() << endl;
    myAccount.withdraw(200);
    cout << "Balance after withdrawal: " << myAccount.getBalance() << endl;
    myAccount.withdraw(2000);
    return 0;
}
