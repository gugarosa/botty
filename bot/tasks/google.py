import configparser
import json

import requests

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

# Gathers the google's task endpoint
GOOGLE_API = config.get('TASKS', 'GOOGLE')


def speech_text(audio_path):
    """Performs a call to Google's API to perform speech-to-text.

    Args:
        audio_path (str): Path to audio that needs to be transcripted.

    Returns:
        An already decoded JSON object holding the desired innformation.

    """

    # Data structure
    data = {
        'audio_path': audio_path
    }

    # Dumping the data into a JSON object
    payload = json.dumps(data)

    # Tries to perform the API call
    try:
        # POST request over the part-of-speech API method
        r = requests.post(GOOGLE_API, data=payload)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        result = response['result']

        return result

    # If by any chance it fails
    except:
        # Return the response as none
        return None
