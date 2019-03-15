from tornado import escape
from tornado.web import RequestHandler


class SpacyHandler(RequestHandler):
    """A Spacy's handler class used to handle new requests to this part of the API.

    Properties:
        model (Spacy): A model from Spacy's loading.

    Methods:
        initialize(**kwagrs): Initializes the handler.
        post(): Performs POST request.

    """

    def initialize(self, **kwargs):
        """Initializes the handler for Spacy's.

        Args:
            kwargs (**): Additional keyword arguments

        """

        # Initializes the property to model
        self.model = kwargs['model']

    def post(self):
        """POST request when calling spacy's API. For now, it will only be a single method.

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
            predict = self.model(message)
            
            # Creates a list holding the results
            result = [f'{token.text} - {token.pos_} - {token.dep_}' for token in predict]

            # Writes the final result back
            self.write(dict(result=result))

        except:
            # If not possible, raises an error
            raise RuntimeError('Failed to perform prediction.')