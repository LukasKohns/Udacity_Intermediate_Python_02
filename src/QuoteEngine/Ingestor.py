"""Define Ingestor class."""

from typing import List

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel, DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor

DEBUG = False


class Ingestor(IngestorInterface):
    """Select correct type of ingestor and parse a file with it."""

    ingestors = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quotes from a file to a list of QuoteModel objects."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                if DEBUG:
                    print("Using: ", ingestor())
                return ingestor.parse(path)
