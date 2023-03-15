import functions
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
        images_result_link = results["images_results"][0]['thumbnail']
        phonetics = functions.get_phonetics(word)
        partofspeech = functions.get_pos(word)
        definition = functions.get_definition(word)
        return render_template("results.html", word=word, phonetics=phonetics, partofspeech=partofspeech, definition=definition, images_result_link=images_result_link)
    else:
        return render_template("get.html")
