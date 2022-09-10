"""Define class to import Quotes from a CSV."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class CSVIngestor(IngestorInterface):
    """Define ingest of Quotes from CSV files."""

    def __repr__(self) -> str:
        """Define representation of object as string."""
        return "CSV Ingestor"

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quotes from a CSV-file to a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row["body"].strip('"'), row["author"])
            quotes.append(new_quote)

        return quotes
