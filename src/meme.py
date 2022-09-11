"""Generate Memes according to given command line arguments."""
import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

DEBUG = False


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    print(path)
    print(os.getcwd())

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        if DEBUG:
            for quote in quotes:
                print(quote, ":  ", len(quote), "\n")
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run to generate a random Meme. You can choose a path,\n"
                    "body or author if you want.")
    parser.add_argument(
        "-p", "--path",
        type=str, default=None,
        help="Give a path to a specific image you want to use.",)
    parser.add_argument(
        "-b", "--body",
        type=str, default=None,
        help="Give a specific text body you want to use.",)
    parser.add_argument(
        "-a", "--author",
        type=str, default=None,
        help="Give a specific author you want to use.",)

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
