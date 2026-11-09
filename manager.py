from book import Book
from user import User

class Manager():
    def __init__(self, library: "Library") -> None:
        self.library = library

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError('В библиотеку можно тобавлять только объекты класса Book')
        if book in self.library.books:
            raise ValueError('Книга уже есть в библиотеке')
        self.library.books.append(book)

    def give_book(self, book: Book, user: User) -> str:
        if book.is_available:
            book._is_available = False
            user.books.append(book)
            return "Книга выдана"
        raise ValueError(f'Книга "{book.name}" уже выдана')

    def return_book(self, book: Book, user: User) -> str:
        if book not in user.books:
            raise ValueError(f'Книга "{book.name}" не числится за пользователем "{user.name}" "{user.surname}"')
        if not book.is_available:
            book._is_available = True
            user.books.remove(book)
            return "Книга возвращена"
        raise ValueError(f'Книга "{book.name}" уже возвращена')
