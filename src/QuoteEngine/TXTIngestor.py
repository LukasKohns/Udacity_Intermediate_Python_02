"""Define class to import Quotes from a TXT file."""

from typing import List

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class TXTIngestor(IngestorInterface):
    """Define ingest of Quotes from TXT files."""

    def __repr__(self) -> str:
        """Define representation of object as string."""
        return "TXT Ingestor"

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quotes from a TXT-file to a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        file = open(path, "r")
        quotes = []

        for line in file.readlines():
            line = line.strip("\n\r").strip()
            if len(line) > 0:
                parse = line.split(" - ")
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
