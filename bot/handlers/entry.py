import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)


def options(update, context):
    """Handles the initial options from first interaction.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'New entry from message: {update.message.text}')

    # Gathering user's first name
    first_name = update.message.chat.first_name

    # Creating a markup to hold options
    markup = ReplyKeyboardMarkup(
        [c.ENTRY_OPTIONS[:2], c.ENTRY_OPTIONS[2:]], one_time_keyboard=True)

    # Replies according to flow
    update.message.reply_text(c.ENTRY_OPTIONS_RESPONSE.format(name=first_name), reply_markup=markup)

    logger.info(f'Awaiting user option ...')

    return 'AWAIT_OPTIONS'
