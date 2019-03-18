import logging

from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def await_intent(update, context):
    """
    """

    logger.info(f'New interaction message: {update.message.text}')

    # This will be an API request to check intent
    intent = 'HELLO'

    logger.info(f'Proceding to state: {intent}')

    if intent == 'HELLO':
        # Calling method to handle hello state
        hello(update, context)

    elif intent == 'NONE':
        # Calling method to handle none state
        none(update, context)

    logger.info(f'Awaiting new interaction ...')

    return 'AWAIT_INTENT'


def none(update, context):
    logger.info(f'Handling state: none ...')

    # Replying text if intent was not found
    update.message.reply_text(lang['TEXT_INTENT_FALLBACK'])


def hello(update, context):
    logger.info(f'Handling state: hello')

    # # Replying text if intent was hello
    update.message.reply_text(lang['TEXT_INTENT_HELLO'])
