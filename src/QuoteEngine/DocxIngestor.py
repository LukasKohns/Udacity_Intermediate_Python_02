"""Define class to import Quotes from a Docx-file."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class DocxIngestor(IngestorInterface):
    """Define ingest of Quotes from Docx files."""

    def __repr__(self) -> str:
        """Define representation of object as string."""
        return "Docx Ingestor"

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quotes from a Docx-file to a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(" - ")
                body = parse[0].strip('"')
                new_quote = QuoteModel(body, parse[1])
                quotes.append(new_quote)

        return quotes
