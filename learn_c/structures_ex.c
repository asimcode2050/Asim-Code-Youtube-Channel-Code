#include <stdio.h>
struct Book
{
    char title[100];
    char author[100];
    int year;
    float price;
};
int main()
{
    struct Book myBook;
    myBook.year = 1925;
    myBook.price = 10.99;
    snprintf(myBook.title, sizeof(myBook.title), "The Great Gatsby");
    snprintf(myBook.author, sizeof(myBook.author), "F. Scott Fitzgerald");
    printf("Book Title: %s\n", myBook.title);
    printf("Author: %s\n", myBook.author);
    printf("Year: %d\n", myBook.year);
    printf("Price: $%.2f\n", myBook.price);
    return 0;
}
