import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from utils import locale

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def end(update, context):
    """
    """

    logging.info('Current interaction ended.')

    keyboard = ReplyKeyboardRemove()

    # Replying a message to cancel the current interaction
    update.message.reply_text(lang['TEXT_LAST_RESPONSE'], reply_markup=keyboard)

    return ConversationHandler.END


def set_client(update, context):
    """
    """

    logging.info('Setting new client ...')

    try:
        client = context.args[0]

        if client == '':
            logging.info('No client found.')

            update.message.reply_text(
                'Este cliente não existe. Por favor, tente novamente.')
                
            return

        context.chat_data['client'] = client

        logging.info(f'New client: {client}')

        update.message.reply_text('O cliente foi configurado corretamente.')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')
