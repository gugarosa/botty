import io
import os

from google.cloud.speech import enums, types
from tornado import escape
from tornado.web import RequestHandler


class GoogleHandler(RequestHandler):
    """A Google's handler class used to handle new requests to this part of the API.

    Properties:
        client (SpeechClient): A speech client from google.cloud.speech.

    """

    def initialize(self, **kwargs):
        """Initializes the handler for Google's.

        """

        # Initializes the property to model
        self.client = kwargs['client']

    def post(self):
        """POST request when calling google's API. For now, it will only be a single method.

        """

        # Decode the body looking for information
        body = escape.json_decode(self.request.body)

        # Parsing the message
        audio_path = body.get('audio_path', None)

        # Verifies if its a string
        if not isinstance(audio_path, str):
            # Raises error if not
            raise RuntimeError('audio_path should be a string')

        # Tries to actually call the google's speech-to-text service
        try:
            with io.open(audio_path, 'rb') as audio_file:
                content = audio_file.read()
                audio = types.RecognitionAudio(content=content)

            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
                sample_rate_hertz=16000,
                language_code='pt-BR')

            # Detects speech in the audio file
            #res = self.client.recognize(config, audio)

            # Creates an operation to detects speech in a long audio file
            operation = self.client.long_running_recognize(config, audio)

            # Gathers the result of the operation
            res = operation.result(timeout=90)

            # Creates an empty variable to hold the result
            result = ''

            # Iterate through every result
            for r in res.results:
                # Gathers the best transcription for each chunk
                result += r.alternatives[0].transcript

            # Writes the final result back
            self.write(dict(result=result))

        except:
            # If not possible, raises an error
            raise RuntimeError('Failed to perform speech recognition.')
