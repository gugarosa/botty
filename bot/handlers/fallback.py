import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)


def end(update, context):
    """Handles the interaction ending.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logging.info('Current interaction ended.')

    # If there is any reply keyboard, we need to remove
    keyboard_removal = ReplyKeyboardRemove()

    # Replying a message to cancel the current interaction
    update.message.reply_text(c.FALLBACK_END_RESPONSE, reply_markup=keyboard_removal)

    return ConversationHandler.END
