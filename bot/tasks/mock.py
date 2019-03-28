import json

import requests

# URL to call mocked API
MOCK_API = 'https://app.fakejson.com/q'


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
