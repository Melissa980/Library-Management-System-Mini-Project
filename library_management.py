from book import Book
from user import User
from author import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Select an option: ")
            
            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                print("Exiting system.")
                break
            else:
                print("Invalid option, please try again.")

    def book_operations(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date: ")
            new_book = Book(title, author, genre, publication_date)
            self.books.append(new_book)
            print("Book added successfully.")
        elif choice == "2":
            title = input("Enter the book title to borrow: ")
            for book in self.books:
                if book.get_title() == title and book.borrow():
                    print(f"{title} has been borrowed.")
                    return
            print("Book not available.")
        elif choice == "3":
            title = input("Enter the book title to return: ")
            for book in self.books:
                if book.get_title() == title:
                    book.return_book()
                    print(f"{title} has been returned.")
                    return
            print("Book not found.")
        elif choice == "4":
            title = input("Enter the book title to search for: ")
            for book in self.books:
                if book.get_title() == title:
                    book.display_info()
                    return
            print("Book not found.")
        elif choice == "5":
            for book in self.books:
                book.display_info()
        else:
            print("Invalid option.")

    def user_operations(self):
        # Similar to book_operations, handle user-related tasks here
        pass

    def author_operations(self):
        # Similar to book_operations, handle author-related tasks here
        pass

# Run the application
if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.main_menu() 