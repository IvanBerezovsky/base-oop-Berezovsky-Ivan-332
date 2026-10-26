class Book:
    _next_isbn: int = 1

    def __init__(self, name: str, author: str, is_available: bool = True) -> None:
        self._isbn = Book._next_isbn
        Book._next_isbn += 1
        self._name = name
        self._author = author
        self.__is_available = is_available
    
    @property
    def isbn(self) -> int:
        return self._isbn

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author
    
    @property
    def is_available(self) -> bool:
        return self.__is_available
    
    def get_book(self) -> bool:
        if self.is_available:
            self.__is_available = False
            return True
        raise ValueError(f'Книга "{self.name}" уже выдана')
    
    def return_book(self) -> bool:
        if not self.is_available:
            self.__is_available = True
            return True
        raise ValueError(f'Книга "{self.name}" уже возвращена')
