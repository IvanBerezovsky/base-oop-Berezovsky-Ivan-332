from book import Book
from user import User
from manager import Manager
from finder import Finder


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.manager = Manager(self)
        self.finder = Finder(self)

    # Manager functions

    def add_book(self, book: Book) -> None:
        return self.manager.add_book(book)

    def give_book(self, book: Book, user: User) -> str:
        return self.manager.give_book(book, user)

    def return_book(self, book: Book, user: User) -> str:
        return self.manager.return_book(book, user)

    # Finder functions
    
    def get_all_books(self) -> str:
        return self.finder.get_all_books()
    
    def get_available_books(self) -> str:
        return self.finder.get_available_books()
    
    def get_taken_books(self) -> str:
        return self.finder.get_taken_books()

    def find_book(self, book: Book) -> str:
        return self.finder.find_book(book)

    def find_book_by_name(self, book_name) -> str:
        return self.finder.find_book_by_name(book_name)

    def find_book_by_author(self, author_name) -> str:
        return self.finder.find_book_by_author(author_name)
        
