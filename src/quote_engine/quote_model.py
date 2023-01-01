class QuoteModel:
    """A quote object with text body and author"""

    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __str__ (self) -> str:
        return f'"{self.text}" - {self.author}'


