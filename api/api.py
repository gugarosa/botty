import logging

from tornado import escape
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

import spacy

# Defining logs format
FORMATTER = "%(asctime)s - %(name)s — %(levelname)s — %(message)s"

# Defines basic logging level
logging.basicConfig(level=logging.DEBUG, format=FORMATTER)

# Port constant
PORT=8080

# Path to the models
MODEL_PATH = '../models/'

class DefaultHandler(RequestHandler):
    """DefaultHandler 
    """

    def initialize(self, **kwargs):
        """
        """

        # Initializes the property to model
        self.model = kwargs['model']

    def post(self):
        """
        """

        # Decode the body looking for information
        body = escape.json_decode(self.request.body)

        # Parsing the message
        message = body.get('message', None)

        # Verifies if its a string
        if not isinstance(message, str):
            # Raises error if not
            raise RuntimeError('message should be a string')
        
        # Tries to actually call the model's prediction
        try:
            # Predicts the message using desired model
            predict = model(message)
            
            # Creates a list holding the results
            result = [f'{token.text} - {token.pos_} - {token.dep_}' for token in predict]

            # Writes the final result back
            self.write(dict(result=result))
        except:
            # If not possible, raises an error
            raise RuntimeError('Failed to perform prediction.')


class Server(Application):
    """
    """

    def __init__(self, model):
        """
        """

        # Default API handlers
        handlers = [(r'/', DefaultHandler, dict(model=model))]

        # Bootstrap the Application class
        Application.__init__(self, handlers, debug=True, autoreload=True)


if __name__ == '__main__':
    # Loading model
    logging.debug('Loading model ...')

    # Actually calling spacing and loading the model
    model = spacy.load('pt_core_news_sm')

    # Logging important information
    logging.debug('Starting server ...')

    # Tries to start a tornado webserver
    try:
        # Logs its port
        logging.info(f'Port: {PORT}')

        # Creates an application
        app = HTTPServer(Server(model))

        # Servers the application on desired port
        app.listen(PORT)

        # Starts a IOLoop instance
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()
