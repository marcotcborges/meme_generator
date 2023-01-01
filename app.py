import random
import glob
import os
import requests
from flask import Flask, render_template, abort, request
from src.quote_engine.ingestor import Ingestor
from src.meme_engine.meme_engine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('static')


def setup():
    """ Load all resources """

    quote_files = ['src/_data/DogQuotes/DogQuotesTXT.txt',
                   'src/_data/DogQuotes/DogQuotesDOCX.docx',
                   'src/_data/DogQuotes/DogQuotesPDF.pdf',
                   'src/_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for quote_file in quote_files:
        if Ingestor.parse(quote_file) is not None:
            quotes += Ingestor.parse(quote_file)

    images_path = "src/_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form["image_url"]:
        return render_template('meme_form.html')

    image_url = request.form["image_url"]

    tmp = f'tmp/{random.randint(0,100000000)}.png'

    try:
        with open(tmp, 'wb') as f:
            f.write(requests.get(image_url).content)

    except Exception as e:
        print(f'meme_post error: {e}')
        return render_template('meme_form.html')

    body = request.form["body"]
    author = request.form["author"]
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    files = glob.glob('static/*')
    for f in files:
        os.remove(f)
    app.run()

    


