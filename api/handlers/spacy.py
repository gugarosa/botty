from tornado import escape
from tornado.web import RequestHandler
import json


class SpacyHandler(RequestHandler):
    """A Spacy's handler class used to handle new requests to this part of the API.

    Properties:
        model (Spacy): A Spacy's pre-loaded model.

    """

    def initialize(self, **kwargs):
        """Initializes the handler for Spacy's.

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
            #result = [f'{entity} - {entity.label_}' for entity in predict.ents]

            prod, qty, und = [], [], []
            for entity in predict.ents:
                if entity.label_ == 'PROD':
                    prod.append(str(entity))
                if entity.label_ == 'QTD':
                    qty.append(str(entity))
                if entity.label_ == 'UND':
                    und.append(str(entity))

            temp = []

            # for i, (p, q, u) in enumerate(zip(prod, qty, und)):
            #     temp.append({
            #         'cnpj': '1',
            #         'id': f'item{i+1}',
            #         'nome_cliente': 'Kibon',
            #         'ds_sku_input': p,
            #         'qty': q
            #     })

            temp.append({
                'cnpj': '1',
                'id': '',
                'nome_cliente': 'Kibon',
                'ds_sku_input': prod,
                'qty': qty
            })

            final = {
                'data': temp
            }

            # Writes the final result back
            self.write(dict(final))

        except:
            # If not possible, raises an error
            raise RuntimeError('Failed to perform prediction.')
