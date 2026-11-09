from book import Book

class User:
    _next_id: int = 1

    def __init__(self, name, surname) -> None:
        self._id = User._next_id
        User._next_id += 1
        self.books: list[Book] = []
        self._name = name
        self._surname = surname

    @property
    def name(self) -> str:
        return self._name

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def id(self) -> int:
        return self._id
    
    def get_all_books(self) -> str:
        count = 0

        for book in self.books:
            print(book)
            count += 1
        
        if count == 0:
            print(f'User "{self.name}" "{self.surname}" has no books.')
    
