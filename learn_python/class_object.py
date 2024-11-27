class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."


book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(book1.description())  # Output: '1984' by George Orwell, 328 pages.
print(book2.description())
