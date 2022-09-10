"""Run web interface for Meme generator."""
import random
import os
import sys
import requests
from flask import Flask, render_template, abort, request
import urllib.request
from PIL import Image

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # Get user input
    image_url = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    tmp_path = "./tmp/pic.png"
    # Get image from url with requests
    urllib.request.urlretrieve(image_url, tmp_path)

    # Use the meme object to generate a meme using this temp file and the body and author form paramaters.
    path = meme.make_meme(tmp_path, body, author)

    # Remove the temporary saved image.
    os.remove(tmp_path)

    if os.path.exists(path):
        return render_template('meme.html', path=path)
    else:
        return render_template('error.html', error=path)


if __name__ == "__main__":
    app.run()
