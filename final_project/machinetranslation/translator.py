""" This is the Translator Module """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#evetually had to change naming below to raise pylint score ... snake-case issue
def english_to_french(englishText):
    """ Translation EN to FR """
    translation = language_translator.translate(
        text = englishText,
        model_id='en-fr'
    ).get_result()

    frenchText = translation['translations'][0]['translation']
    return frenchText

#eventually had to change naming below to raise pylint score ... snake-case issue
def french_to_english(frenchText):
    """  Translation FR to EN """
    translation = language_translator.translate(
        text = frenchText,
        model_id='fr-en'
    ).get_result()

    englishText = translation['translations'][0]['translation']

    return englishText
 