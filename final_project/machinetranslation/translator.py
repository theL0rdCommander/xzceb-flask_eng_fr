import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['api_key']
URL = os.environ['url']
VERSION ='2022-01-10'
#englishText = 'roble'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version= VERSION,
    authenticator= authenticator
)

def setServiceUrl():
    language_translator.set_service_url(URL)

def englishToFrench(englishText):
    if (englishText == ""):
        return ""
    frenchText = language_translator.translate(englishText,
     model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    if (frenchText == ""):
        return ""
    englishText = language_translator.translate(frenchText,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return englishText

