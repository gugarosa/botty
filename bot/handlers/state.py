import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from handlers import fallback
from tasks import mock
from utils import locale, voice

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def _handle_states(state, update):
    """Handles a state to the desired response.

    Args:
        state (str): A string containing the desired state.
        update (Update): An update object, basically holding vital information from a new user interaction.

    """

    # If there is any reply keyboard, we need to remove
    keyboard_removal = ReplyKeyboardRemove()

    # Checks which state the user has chosen
    if state == 'CLIENT':
        # Reply message according to state
        update.message.reply_text(lang['STATE_CLIENT'], reply_markup=keyboard_removal)

    elif state == 'INCIDENCE':
        # Reply message according to state
        update.message.reply_text(lang['STATE_INCIDENCE'], reply_markup=keyboard_removal)

    elif state == 'SUGGESTION':
        # Reply message according to state
        update.message.reply_text(lang['STATE_SUGGESTION'], reply_markup=keyboard_removal)


def option(update, context):
    """Handles a chosen option by the user.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Gathering user's choice
    option = update.message.text

    logger.info(f'User option: {option}')

    # Mapping possible entries to a list of lists
    entries = lang['HANDLER_ENTRY'].split(',')

    # Iterate through all entries
    for entry in entries:
        # If entry is desired option
        if entry == option:
            # Creates a state string
            state = lang[option.upper()]

    # Handling response to desired state
    _handle_states(state, update)

    logger.info(f'Redirecting to state: {state}')

    return state


def client(update, context):
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
        update.message.reply_text(lang['STATE_CLIENT_ERROR'])

        return 'CLIENT'

    logger.info(f'Client found. Replying and ending interaction.')

    # Replying correct result
    update.message.reply_html(
        f"<b>Cliente:</b> {client}\n<b>E-mail:</b> {result['email']}\n<b>Telefone:</b> {result['phone']}")

    # Ending conversation
    return fallback.keyboard(update, context)


def incidence(update, context):
    """Handles the incidence state.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Gathers the voice update
    voice_message = update.message.voice

    # Handling voice saving
    voice.save(voice_message)

    # Replying back to user to hold for response
    update.message.reply_text(lang['STATE_INCIDENCE_OK'])

    # Replying voice back
    update.message.reply_voice(voice_message)

    # Ending conversation
    return fallback.keyboard(update, context)


def suggestion(update, context):
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
        update.message.reply_text(lang['STATE_SUGGESTION_ERROR'])

        return 'SUGGESTION'

    logger.info(f'Product found. Replying and ending interaction.')

    # Replying correct result
    update.message.reply_html(
        f"O produto <b>{product}</b> pertence à empresa <b>{result['company']}</b> e está custando <b>R$ {result['price']}</b>.")

    # Ending conversation
    return fallback.keyboard(update, context)

