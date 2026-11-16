from book import Book

class Finder:
    def __init__(self, library: "Library") -> None:
            self.library = library

    def get_all_books(self) -> str:
        count = 0
        for book in self.library.books:
            print(book)
            count += 1

        if count == 0:
            return "Список пуст"
    
    def get_available_books(self) -> str:
        count = 0
        for book in self.library.books:
            if book.is_available:
                count += 1
                print(book)

        if count == 0:
            return "Список пуст"
    
    def get_taken_books(self) -> str:
        count = 0
        for book in self.library.books:
            if not book.is_available:
                count += 1
                print(book)

        if count == 0:
            return "Список пуст"

    def find_book(self, book: Book) -> str:
        if not isinstance(book, Book):
            raise TypeError('В библиотеке существуют только объекты класса Book')
        if book not in self.library.books:
            return "Книги нет в библиотеке"
        return book

    def find_book_by_name(self, book_name) -> str:
        count = 0
        for book in self.library.books:
            if book.name == book_name:
                count += 1
                print(book)
        if count == 0:
            return "Книги нет в библиотеке"

    def find_book_by_author(self, author_name) -> str:
            count = 0
            for book in self.library.books:
                if book.author == author_name:
                    print(book)
                    count += 1
            if count == 0:
                return "Книги нет в библиотеке"
