class Bibliotek:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        if any(curr_user.user_id == user.user_id for curr_user in self.users):
            print("User ID already exists! Try another ID.")
            return
        self.users.append(user)
        # print(f"New user {user.name} added successfully!")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books
                       if title.lower() in book.title.lower()]
        return found_books

    def search_book_by_author(self, author):
        found_books = [book for book in self.books
                       if author.lower() in book.author.lower()]
        return found_books

    def list_books(self):
        if self.books:
            print("Books in the Library:")
            for book in self.books:
                book.display_book_info()
        else:
            print("No books available in the library.")


class Book:
    def __init__(self, book_id, author, title, quantity):
        self.author = author
        self.book_id = book_id
        self.quantity = quantity
        self.title = title

    def display_book_info(self):
        text = (f"ID: {self.book_id}, Title: {self.title}, "
                f"Author: {self.author}, Available Quantity: {self.quantity}")
        return text

    def check_availability(self):
        return self.quantity > 0

    def update_quantity(self, quantity):
        self.quantity += quantity


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return ""

    def borrow_book(self, book):
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)  # Decrease quantity of borrowed books
            # print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_quantity(1)  # Increase quantity of returned book
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def view_borrowed_books(self):
        if self.borrowed_books:
            # print(f"{self.name}'s Borrowed Books:")
            a = []
            for book in self.borrowed_books:
                a.append(book.title)
            return a

        else:
            return []
