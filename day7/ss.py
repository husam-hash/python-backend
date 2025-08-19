# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


# Library class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print("Cannot remove book; it's currently borrowed.")
                else:
                    self.books.remove(book)
                    print(f"Book removed: {title}")
                return
        print("Book not found.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print("Sorry, the book is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You borrowed: {title}")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned: {title}")
                return
        print("This book wasn't borrowed or doesn't exist.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print(f"\nBooks in {self.name}:")
            for book in self.books:
                print(f"  - {book}")


# Sample usage
library = Library("Central Library")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.borrow_book("1984")
library.borrow_book("1984")  # Already borrowed
library.return_book("1984")
library.remove_book("1984")
library.display_books()
