import configparser
import json

import requests

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

# Gathers the mock's task endpoint
WEATHER_API = config.get('TASKS', 'WEATHER')


def get_temperature(location):
    """Performs a call to a mock API and verify if message exists.

    Args:
        location (dict): A dictionary containing both latitude and longitude.

    Returns:
        An already decoded JSON object holding the desired innformation.

    """

    # Composing call
    url = f'{WEATHER_API}key=e5ad8860f31f42fea5595514180903&format=json&q={location["latitude"]},{location["longitude"]}'

    # Tries to perform the API call
    try:
        # POST request over the mocked API
        r = requests.get(url)

        # Decoding response
        response = json.loads(r.text)

        # Accessing JSON object and gathering request's response
        result = response['data']['current_condition'][0]['temp_C']

        return result

    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError
