#include <iostream>
#include <string>
using namespace std;
class Book
{
public:
    string title;
    string author;
    double price;
    void displayDetails()
    {
        cout << "Book Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Price: $" << price << endl;
    }
    void applyDiscount(double discountPercentage)
    {
        price -= price * (discountPercentage / 100);
        cout << "After applying the discount, the new price is: $" << price << endl;
    }
    void setDetails(string bookTitle, string bookAuthor, double bookPrice)
    {
        title = bookTitle;
        author = bookAuthor;
        price = bookPrice;
    }
};
int main()
{
    Book book1;
    Book book2;
    book1.setDetails("The Great Gatsby", "F. Scott Fitzgerald", 15.99);
    book2.setDetails("1984", "George Orwell", 9.99);
    book1.displayDetails();
    book2.displayDetails();
    book1.applyDiscount(10);
    book2.applyDiscount(20);
    return 0;
}
