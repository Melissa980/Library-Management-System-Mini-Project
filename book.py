class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = False

    # Encapsulated Getters and Setters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return not self.__is_borrowed

    def borrow(self):
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        self.__is_borrowed = False

    def display_info(self):
        status = "Available" if not self.__is_borrowed else "Borrowed"
        print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Status: {status}")