import logging

from handlers import fallback
from tasks import google
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
    update.message.reply_text(c.GOOGLE_WAITING)

    # Making API call
    text = google.speech_text(voice_path)

    # Checks if API call was possible
    if text == None:
        logger.warning(f'Transcription not found for voice: {voice_path}')

        # Replies text saying client was not found
        update.message.reply_text(c.GOOGLE_ERROR)

        return 'GOOGLE'

    logger.info(f'Transcript found. Replying its information ...')

    # Saving transcript
    transcript.save(voice_id, text)

    # Replying transcript back
    update.message.reply_html(c.GOOGLE_RESPONSE.format(transcript=text))

    # Ending conversation
    return fallback.retry(update, context)
