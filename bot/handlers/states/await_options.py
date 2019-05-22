import logging

from telegram import ReplyKeyboardRemove

from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)


def state(update, context):
    """Handles a chosen option by the user.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Removes the reminder job if it exists
    if context.job_queue.jobs():
        for job in context.job_queue.jobs():
            job.schedule_removal()

    # Gathering user's choice
    option = context.match[0]

    logger.info(f'User option: {option}')

    # Gathering the index from options list
    state_index = c.ENTRY_OPTIONS.index(option)

    # If there is any reply keyboard, we need to remove
    keyboard_removal = ReplyKeyboardRemove()

    # Reply message according to state
    update.message.reply_text(
        c.AWAIT_OPTIONS_RESPONSES[state_index], reply_markup=keyboard_removal)

    # Defining state according to found index
    state = c.AWAIT_OPTIONS_STATES[state_index]

    logger.info(f'Redirecting to state: {state}')

    return state
