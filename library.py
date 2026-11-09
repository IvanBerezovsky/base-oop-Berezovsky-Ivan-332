from book import Book
from user import User
from manager import Manager


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.manager = Manager(self) 

    def add_book(self, book: Book) -> None:
        return self.manager.add_book(book)

    def give_book(self, book: Book, user: User) -> str:
        return self.manager.give_book(book, user)

    def return_book(self, book: Book, user: User) -> str:
        return self.manager.return_book(book, user)
    
    def get_all_books(self) -> str:
        for book in self.books:
            print(book)
    
    def get_available_books(self) -> str:
        for book in self.books:
            if book.is_available:
                print(book)
    
    def get_taken_books(self) -> str:
        for book in self.books:
            if not book.is_available:
                print(book)
