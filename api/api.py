import logging

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from handlers.spacy import SpacyHandler

from utils import loader

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Gets the logging object
logger = logging.getLogger(__name__)

# Port constant
PORT = 8080

# Path to the models
MODEL_PATH = '../models/'


class Server(Application):
    """A class to hold the actual server class.

    """

    def __init__(self, spacy_model):
        """Initializes the application.

        Args:
            spacy_model (Spacy): A Spacy's already loaded model.

        """

        # Default API handlers
        handlers = [(r'/api/spacy/', SpacyHandler, dict(model=spacy_model))]

        # Bootstrap the Application class
        Application.__init__(self, handlers, debug=True, autoreload=True)


if __name__ == '__main__':
    # Loading model
    logging.debug('Loading model ...')

    # Actually calling spacing and loading the model
    spacy_model = loader.load_spacy()

    # Logging important information
    logging.debug('Starting server ...')

    # Tries to start a tornado webserver
    try:
        # Logs its port
        logging.info(f'Port: {PORT}')

        # Creates an application
        app = HTTPServer(Server(spacy_model))

        # Servers the application on desired port
        app.listen(PORT)

        # Starts a IOLoop instance
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()
