""" This is the Flask module """
import json

from flask import Flask, render_template, request

import machinetranslation
from machinetranslation import translator

app = Flask("Web Translator")

""" This is the Flask module """
import json
from flask import Flask, render_template, request

import machinetranslation
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """ e2f translation I/O follows """
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.english_to_french(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def french_to_english():
    """ f2e translation I/O follows """
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.french_to_english(textToTranslate)
    return englishText

@app.route("/")
def render_index_page():
    """ render the index.html page """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
