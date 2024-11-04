class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def display_info(self):
        print(f"Author: {self.__name}")
        print(f"Biography: {self.__biography}")
