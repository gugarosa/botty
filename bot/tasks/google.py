import json

import requests

# URL to call Google's API
GOOGLE_API = 'http://localhost:8080/api/google/'


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
