import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from tasks import mock

# Gets the logging object
logger = logging.getLogger(__name__)

# All possible interaction options
reply_keyboard = [['Cliente', 'Finalizar']]

# Creating a markup to hold options
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def entry(update, context):
    logger.info(f'New interaction message: {update.message.text}')

    # Gathering user's first name
    first_name = update.message.chat.first_name

    # Replying initial text
    update.message.reply_text(
        f'Olá {first_name}! Por favor, escolha alguma opção.', reply_markup=markup)

    logger.info(f'Awaiting user option ...')

    return 'AWAIT_OPTION'


def choice(update, context):
    # Gathering user's choice
    option = (update.message.text).upper()

    # Checks the chosen option
    if option == 'CLIENTE':
        # Replies text according to chosen option
        update.message.reply_text('Por favor, digite o nome do cliente.')

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
