import json

import requests

# URL to call Spacy's API
SPACY_API = 'http://localhost:8080/api/spacy/'


def pos_tagger(message):
    """Performs a call to Spacy's API to perform a part-of-speech tagging.

    Args:
        text (str): A text to perform part-of-speech (POS) tagging.

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
        # POST request over the part-of-speech API method
        r = requests.post(SPACY_API, data=payload)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        result = response['result']

        return result

    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError
