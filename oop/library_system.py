# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize the title and author of the book."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size in MB."""
        super().__init__(title, author)  # Call parent constructor
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"{super().__str__()} [EBook, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"{super().__str__()} [PrintBook, {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added to the library.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(book)
