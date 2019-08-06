import configparser
import json

import requests

# Initializing configuration object
config = configparser.ConfigParser()

# Parsing a new config
config.read('bot/config.ini')

PORTAL_URL_LOGIN = config.get('PORTAL', 'LOGIN')
PORTAL_URL_API = config.get('PORTAL', 'API')

# GET request to login and to get a valid token.
def call_portal(input, chat_id):
    session = requests.Session()
    
    response = session.get(PORTAL_URL_LOGIN, params={'email':"admin-kibon@smart.com.br", 'password':"quvkat-febJyp-1kuzsa"},)
    
    json_response = response.json()
    if response.status_code == 200:
        token = json_response['token']
        cookie = session.cookies.get_dict()['session']
        print('Authenticate ... OK: ' + str(json_response['message']))
    elif response.status_code == 400:
        print('Authentication: ' + str(json_response['message']))
    
    headers = {'Content-type': 'application/json', "Authorization": "Bearer " + token, 'cookie':"session="+cookie}
    
    for d in input['data']:
        d['id'] = chat_id

    try:
        # # POST request over the Portal API
        r = requests.post(PORTAL_URL_API, data=json.dumps(input), headers=headers)
        
        print("Connection to portal API ... ", r.status_code)
        if(r.status_code == 200):
            return r.json()
    
    # If by any chance it fails
    except:
        # Raises a ConnectionError (this should be enough)
        raise ConnectionError