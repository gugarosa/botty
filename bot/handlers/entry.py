import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from handlers import common
from tasks import weather
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

    # Checks if there is any location data
    if context.user_data:
        # If yes, gathers the current temperature from that location
        temp = weather.get_temperature(context.user_data)

        # Replies according to flow
        update.message.reply_text(c.ENTRY_OPTIONS_RESPONSE.format(
            name=first_name, temperature=temp), reply_markup=markup)

    # If not
    else:
        # Replies as if user has not shared its location
        update.message.reply_text(c.ENTRY_OPTIONS_RESPONSE_NO_LOCATION.format(
            name=first_name), reply_markup=markup)

    # Starts the job queue and dispatches a job after 10 minutes
    context.job_queue.run_once(
        common.reminder, 600, context=update.message.chat_id)

    logger.info(f'Awaiting user option ...')

    return 'AWAIT_OPTIONS'
