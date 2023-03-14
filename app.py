import functions

from flask import Flask, render_template, request

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
        phonetics = functions.get_phonetics(word)
        partofspeech = functions.get_pos(word)
        definition = functions.get_definition(word)
        #return "Results that are close to {}".format(place)
        return render_template("results.html", word=word, phonetics=phonetics, partofspeech=partofspeech, definition=definition)
    else:
        return "Wrong HTTP method", 400
