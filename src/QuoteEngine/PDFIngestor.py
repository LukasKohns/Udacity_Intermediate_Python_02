"""Define class to import Quotes from a PDF."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class PDFIngestor(IngestorInterface):
    """Define ingest of Quotes from PDF files."""

    def __repr__(self) -> str:
        """Define representation of object as string."""
        return "PDF Ingestor"

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Quotes from a PDF-file to a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        tmp = f"./tmp/{random.randint(0,10000000000)}.txt"
        call = subprocess.call(["pdftotext", path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip("\n\r").strip()
            if len(line) > 0:
                parse = line.split(" - ")
                body = parse[0].strip('"')
                new_quote = QuoteModel(body, parse[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
