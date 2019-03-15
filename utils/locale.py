import json

# Defines the input language
INPUT_LANG = 'utils/lang/pt'

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
