import configparser
import json

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('config.ini')

# Gets the key from bot's language
key = config.get('BOT', 'LANGUAGE')

# Defines the input language
INPUT_LANG = 'utils/lang/' + key

def get():
    """Parses an input json and gather its content.

    Returns:
        A dictionary holding the json's values.

    """

    # Defines a new dictionary
    keys = {}

    # Trying to open JSON file
    with open(INPUT_LANG + '.json') as json_file:  
        # Actually load the file
        lang = json.load(json_file)

    # Iterating through its (key, value) pairs
    for k, v in lang.items():
        # Creating a new key
        keys[k] = v

    return keys
