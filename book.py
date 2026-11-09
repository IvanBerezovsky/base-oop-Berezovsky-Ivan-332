class Book:
    _next_isbn: int = 1

    def __init__(self, name: str, author: str, is_available: bool = True) -> None:
        self._isbn = Book._next_isbn
        Book._next_isbn += 1
        self._name = name
        self._author = author
        self._is_available = is_available

    def __repr__(self) -> str:
        if self.is_available:
            return f"Book({self.isbn}, {self.name!r}, {self.author!r}, available)"
        return f"Book({self.isbn}, {self.name!r}, {self.author!r}, not available)"
    
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
        return self._is_available
