import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from handlers import common
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

    # Removes the reminder job if it exists
    if context.job_queue.jobs():
        for job in context.job_queue.jobs():
            job.schedule_removal()

    # If there is any reply keyboard, we need to remove
    keyboard_removal = ReplyKeyboardRemove()

    # Replying a message to cancel the current interaction
    update.message.reply_text(c.FALLBACK_END_RESPONSE,
                              reply_markup=keyboard_removal)

    return ConversationHandler.END


def retry(update, context):
    """Handles whenever the user wants to retry the flow.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Awaiting if user wants to retry the flow ...')

    # Creating a markup to hold options
    markup = ReplyKeyboardMarkup(
        [c.ENTRY_OPTIONS[:2], c.ENTRY_OPTIONS[2:]], one_time_keyboard=True)

    # Replying text and a keyboard with options
    update.message.reply_text(c.FALLBACK_RETRY_RESPONSE, reply_markup=markup)

    # Starts the job queue and dispatches a job after 10 minutes
    context.job_queue.run_once(
        common.reminder, 600, context=update.message.chat_id)

    return 'AWAIT_OPTIONS'
