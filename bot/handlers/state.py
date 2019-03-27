import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from tasks import mock

# Gets the logging object
logger = logging.getLogger(__name__)

def option(update, context):
    """Handles a chosen option by the user.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Gathering user's choice
    option = (update.message.text).upper()

    logger.info(f'User option: {option}')

    # Checks the chosen option
    if option == 'CLIENTE':
        


def choice(update, context):
    # Gathering user's choice
    option = (update.message.text).upper()

    # Checks the chosen option
    if option == 'CLIENTE':
        # Replies text according to chosen option
        update.message.reply_text('Por favor, digite o nome do cliente.')

    elif option == 'VOZ':
        # Replies text according to chosen option
        update.message.reply_text('Por favor, envie uma mensagem de voz.')

    logger.info(f'Redirecting to state: {option}')

    return option


def client(update, context):
    logger.info(f'Searching for client: {update.message.text}')

    # Gathers client's name
    client = update.message.text

    # Making API call
    result = mock.check_client(client)

    # Checks if API call was possible
    if result == None:
        update.message.reply_text(
            f'Não foi possível encontrar {client}. Por favor, tente novamente.')
        return 'CLIENTE'

    logger.info(f'Client found. Replying and ending interaction.')

    # Replying correct result
    update.message.reply_text(f'{client}\nE-mail: {result}')

    # Ending conversation
    update.message.reply_text(f'Quando precisar, é só voltar a falar comigo.')

    return ConversationHandler.END
