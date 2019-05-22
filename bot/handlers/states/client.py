import logging

from telegram import InputMediaPhoto

from handlers import fallback
from tasks import mock
from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)


def state(update, context):
    """Handles the client state.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Searching for client: {update.message.text}')

    # Gathers client's name
    client = update.message.text

    # Making API call
    result = mock.check_client(client)

    # Checks if API call was possible
    if result == None:
        logger.warning(f'Client not found: {update.message.text}')

        # Replies text saying client was not found
        update.message.reply_text(c.CLIENT_ERROR)

        return 'CLIENT'

    logger.info(f'Client found. Replying its information ...')

    # Replying client's text
    update.message.reply_html(c.CLIENT_RESPONSE.format(
        client=client, email=result['email'], phone=result['phone']))

    # Replying client's image
    update.message.reply_photo(result['avatar'])

    # Ending conversation
    return fallback.retry(update, context)
