import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from tasks import mock
from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()

# Mapping possible entries to a list of lists
entries = [lang['HANDLER_ENTRY'].split(',')]

# Creating a markup to hold options
markup = ReplyKeyboardMarkup(entries, one_time_keyboard=True)


def options(update, context):
    """Handles first options for the user's interaction.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'New entry from message: {update.message.text}')

    # Gathering user's first name
    first_name = update.message.chat.first_name

    # Composing a text reply to user
    reply = lang['HANDLER_ENTRY_OPTIONS_1'] + \
        first_name + lang['HANDLER_ENTRY_OPTIONS_2']

    # Replying text and a keyboard with options
    update.message.reply_text(reply, reply_markup=markup)

    logger.info(f'Awaiting user option ...')

    return 'AWAIT_OPTIONS'
