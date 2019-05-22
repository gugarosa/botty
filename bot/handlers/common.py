import logging

from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)

def location(update, context):
    """
    """

    logger.info(f'Handling user location ...')

    # Saving latitude to user data
    context.user_data['latitude'] = update.message.location['latitude']
    
    # Saving longitude to user data
    context.user_data['longitude'] = update.message.location['longitude']


    logger.info(f'Location saved to user data.')


def reminder(context):
    """Sends a reminder to user warning that he needs to choose an option.

    Args:
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Reminding user to choose an option ...')

    # Sends a reminder to the user
    context.bot.send_message(
        chat_id=context.job.context, text=c.ENTRY_REMINDER)
