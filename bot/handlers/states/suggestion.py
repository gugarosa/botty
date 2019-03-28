import logging

from handlers import fallback
from tasks import mock
from utils import constants as c

# Gets the logging object
logger = logging.getLogger(__name__)


def state(update, context):
    """Handles the suggestion state.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Searching for product: {update.message.text}')

    # Gathers client's name
    product = update.message.text

    # Making API call
    result = mock.check_product(product)

    # Checks if API call was possible
    if result == None:
        logger.warning(f'Product not found: {update.message.text}')

        # Replies text saying product was not found
        update.message.reply_text(c.SUGGESTION_ERROR)

        return 'SUGGESTION'

    logger.info(f'Product found. Replying and ending interaction.')

    # Replying correct result
    update.message.reply_html(c.SUGGESTION_RESPONSE.format(
        product=product, company=result['company'], price=result['price']))

    # Ending conversation
    return fallback.end(update, context)
