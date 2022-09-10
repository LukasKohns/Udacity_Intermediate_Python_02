"""Define class to incapsulate body and author of a quote."""


class QuoteModel:
    """Store a quote in a standardized format."""

    def __init__(self, body: str, author: str):
        """Initialize new quote."""
        self.author = author
        self.body = body

    def __repr__(self) -> str:
        """Define representation of object as string."""
        return f'"{self.body}" - {self.author}'

    def __len__(self) -> int:
        """Define length of object as length of body."""
        return len(self.body)
