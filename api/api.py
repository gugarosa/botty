import logging

from google.cloud import speech
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from handlers.google import GoogleHandler
from spacy import load

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Gets the logging object
logger = logging.getLogger(__name__)

# Port constant
PORT = 8080


class Server(Application):
    """A class to hold the actual server class.

    """

    def __init__(self, speech_client):
        """Initializes the application.

        Args:
            speech_client (SpeechClient): A speech client from google.cloud.speech.

        """

        # Default API handlers
        handlers = [
            (r'/google', GoogleHandler, dict(client=speech_client))
        ]

        # Bootstrap the Application class
        Application.__init__(self, handlers, debug=True, autoreload=True)


if __name__ == '__main__':
    # Loading Google's speech client
    logging.debug('Loading speech client ...')

    # Instantiates a Google's speech-to-text client
    speech_client = speech.SpeechClient()

    # Logging important information
    logging.debug('Starting server ...')

    # Tries to start a tornado webserver
    try:
        # Logs its port
        logging.info(f'Port: {PORT}')

        # Creates an application
        app = HTTPServer(Server(speech_client))

        # Servers the application on desired port
        app.listen(PORT)

        # Starts a IOLoop instance
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()
