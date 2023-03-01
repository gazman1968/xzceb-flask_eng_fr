""" This is the Flask module """
import json

from flask import Flask, render_template, request

import machinetranslation
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """ e2f translation I/O follows """
    text_to_translate = request.args.get('text_to_translate')
    #error handling for null input follows
    if text_to_translate is None:
        return "Error: no input text"
    text_out = translator.english_to_french(text_to_translate)
    return str(text_out)

@app.route("/frenchToEnglish")
def french_to_english():
    """ f2e translation I/O follows """
    text_to_translate = request.args.get('text_to_translate')
    #error handling for null input follows
    if text_to_translate is None:
        return "Error: no input text"
    text_out = translator.french_to_english(text_to_translate)
    return str(text_out)

@app.route("/")
def render_index_page():
    """ render the index.html page """
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
