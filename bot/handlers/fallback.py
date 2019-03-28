import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def keyboard(update, context):
    """Handles a 'fallback_regex' emitted by the user.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logging.info('Current interaction ended.')

    # If there is any reply keyboard, we need to remove
    keyboard_removal = ReplyKeyboardRemove()

    # Replying a message to cancel the current interaction
    update.message.reply_text(lang['FALLBACK_KEYBOARD_END'], reply_markup=keyboard_removal)

    return ConversationHandler.END
