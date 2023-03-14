import functions
import images
import keys

from flask import Flask, render_template, request
from serpapi import GoogleSearch

# Create an instance of Flask

app = Flask(__name__)

# Create a view function for /

@app.route("/")
def index():
    return render_template("index.html")

# Create a view function for /results

@app.route("/results", methods=["GET","POST"])
def results():
    if request.method == "POST":
        word = request.form["word"]
        params = {
        "q": word,
        "tbm": "isch",
        "ijn": "0",
        "api_key": keys.MY_SECRET_API_KEY_1
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        images_results = results["images_results"]
        phonetics = functions.get_phonetics(word)
        partofspeech = functions.get_pos(word)
        definition = functions.get_definition(word)
        image = images_results
        #return "Results that are close to {}".format(place)
        return render_template("results.html", word=word, phonetics=phonetics, partofspeech=partofspeech, definition=definition, image=image)
    else:
        return "Wrong HTTP method", 400
