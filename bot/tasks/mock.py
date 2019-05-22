import configparser
import json

import requests

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

# Gathers the mock's task endpoint
MOCK_API = config.get('TASKS', 'MOCK')


def check_client(message):
    """Performs a call to a mock API and verify if message exists.

    Args:
        text (str): A text to check whether it exists or not

    Returns:
        An already decoded JSON object holding the desired innformation.

    """

    # Data structure
    payload = {
        'token': '1R-2K621skKO2PnZYDqHsg',
        'data': {
            'id': message,
            'avatar': 'personAvatar',
            'email': 'internetEmail',
            'phone': 'phoneHome'
        }
    }

    # Tries to perform the API call
    try:
        # POST request over the mocked API
        r = requests.post(MOCK_API, json=payload)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        result = response

        return result

    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError


def check_product(message):
    """Performs a call to a mock API and verify if message exists.

    Args:
        text (str): A text to check whether it exists or not

    Returns:
        An already decoded JSON object holding the desired innformation.

    """

    # Data structure
    payload = {
        'token': '1R-2K621skKO2PnZYDqHsg',
        'data': {
            'id': message,
            'company': 'companyName',
            'price': 'numberFloat|0,1000|2'
        }
    }

    # Tries to perform the API call
    try:
        # POST request over the mocked API
        r = requests.post(MOCK_API, json=payload)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        result = response

        return result

    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError
