"""Define Ingestors for different file formats."""
from abc import ABC, abstractmethod
from xmlrpc.client import boolean
from typing import List
from QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Define interface for all Ingestor classes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> boolean:
        """Return whether there is an ingestor available for this filetype."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of Quotes from a given file(path) and return it."""
        pass
