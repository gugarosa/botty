import configparser
import json

import requests

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

# Gathers the Spacy's task endpoint
SPACY_API = config.get('TASKS', 'SPACY')


def ner(message):
    """Performs a call to Spacy's API to perform a named entity recognition.

    Args:
        text (str): A text to perform named entity recognition (NER).

    Returns:
        An already decoded JSON object holding the desired innformation.
    """

    # Data structure
    data = {
        'message': message
    }

    # Dumping the data into a JSON object
    payload = json.dumps(data)

    # Tries to perform the API call
    try:
        # POST request over the named entity recognition API method
        r = requests.post(SPACY_API, data=payload)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        #result = response['result']
        result = response

        return result

    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError
