import logging

from telegram.ext import ConversationHandler

from tasks import spacy
from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def echo(update, context):
    """Echoes the same message received by the bot.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Handling message echoing ...')

    logger.info(f'Result: {update.message.text}')

    # Sending back the same message user has received
    update.message.reply_text(update.message.text)


def pos_tagger(update, context):
    """Handles a part-of-speech tagging using an external API

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Handling part-of-speech tagging ...')

    # Calling desired task, in this case a POS tagger from Spacy's API
    pos_tag = spacy.pos_tagger(update.message.text)

    logger.info(f'Result: {pos_tag}')

    # Sending the API's call response back to user
    update.message.reply_text(pos_tag)
