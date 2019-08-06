import logging

from handlers import fallback
from tasks import google, spacy, portal
from utils import constants as c
from utils import transcript, voice

# Gets the logging object
logger = logging.getLogger(__name__)


def state(update, context):
    """Handles the incidence state.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Gathers the voice update
    voice_message = update.message.voice

    # Handling voice saving
    voice_id, voice_path = voice.save(voice_message)

    # Replying back to user to hold for response
    update.message.reply_text(c.INCIDENCE_WAITING)

    # Making API call
    text = google.speech_text(voice_path)

    # Checks if API call was possible
    if text == None:
        logger.warning(f'Transcription not found for voice: {voice_path}')

        # Replies text saying client was not found
        update.message.reply_text(c.INCIDENCE_ERROR)

        return 'INCIDENCE'

    logger.info(f'Transcript found. Replying its information ...')

    # Saving transcript
    transcript.save(voice_id, text)

    # Replying transcript back
    update.message.reply_html(c.INCIDENCE_RESPONSE.format(transcript=text))

    logger.info(f'Applying NER to transcript ...')

    # Making another API call
    ner = spacy.ner(text)

    logger.info(f'NER found. Replying its information ...')

    # Replying NER back
    update.message.reply_html(c.INCIDENCE_RESPONSE_NER.format(ner=ner))

    # Making another API call
    p = portal.call_portal(ner, update.message.chat.id)

    print(p)

    # Ending conversation
    return fallback.retry(update, context)
