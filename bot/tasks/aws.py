import configparser
import json

import requests
from awsauth import S3Auth

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

# Gathers the AWS's task keys
ACCESS = config.get('AWS', 'ACCESS_KEY')
SECRET = config.get('AWS', 'SECRET_KEY')
BUCKET = config.get('AWS', 'BUCKET_URL')


def find_file(file_name):
    """Performs a call to AWS's S3 bucket to check the files list.

    Args:
        file_name (str): Filename to be searched on S3's bucket.

    Returns:
        An already decoded JSON object holding the desired innformation.

    """

    # Tries to perform the API call
    try:
        # POST request over the part-of-speech API method
        r = requests.get(BUCKET + file_name, auth=S3Auth(ACCESS, SECRET))

        # Decoding response
        response = json.loads(r.text)

        return response

    # If by any chance it fails
    except:
        # Return the response as none
        return None
