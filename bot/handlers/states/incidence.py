import logging

from handlers import fallback
from utils import constants as c
from utils import voice

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
    voice.save(voice_message)

    # Replying back to user to hold for response
    update.message.reply_text(c.INCIDENCE_RESPONSE)

    # Replying voice back
    update.message.reply_voice(voice_message)

    # Ending conversation
    return fallback.retry(update, context)
