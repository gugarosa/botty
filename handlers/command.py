import logging

from telegram.ext import ConversationHandler

from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def cancel(update, context):
    """
    """
    
    logging.info('Current interaction ended.')

    # Replying a message to cancel the current interaction
    update.message.reply_text(lang['TEXT_LAST_RESPONSE'])

    return ConversationHandler.END
