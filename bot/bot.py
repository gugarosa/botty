import configparser
import logging

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, RegexHandler, Updater)

from handlers import command, entry, error, fallback, state
from utils import locale

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def start_bot(key):
    """Main process to initiate a customized bot needs.

    """

    logger.info(f'Starting the bot ...')

    # Initializing base class with Bot's token
    updater = Updater(key, use_context=True)

    # Getting the dispatcher to attach new handlers
    dp = updater.dispatcher

    # Add conversation handler to handle bot's states
    dp.add_handler(
        ConversationHandler(
            entry_points=[
                CommandHandler('start', entry.options, pass_user_data=True),
                MessageHandler(Filters.regex(lang['ENTRY_REGEX']), entry.options,
                               pass_user_data=True)
            ],
            states={
                'AWAIT_OPTIONS': [MessageHandler(Filters.regex(lang['STATE_AWAIT_OPTIONS_REGEX']), state.option, pass_user_data=True)],
                'CLIENT': [MessageHandler(Filters.text, state.client, pass_user_data=True)],
                'INCIDENCE': [MessageHandler(Filters.voice, state.incidence, pass_user_data=True)],
                'SUGGESTION': [MessageHandler(Filters.text, state.suggestion, pass_user_data=True)]
            },
            fallbacks=[
                CommandHandler('end', command.end),
                MessageHandler(Filters.regex(
                    lang['FALLBACK_KEYBOARD_REGEX']), fallback.keyboard, pass_user_data=True)
            ]
        )
    )

    # Creates an error logging
    dp.add_error_handler(error.log)

    # Actually start the polling of new updates
    updater.start_polling()

    # Used to handle its idle state
    updater.idle()


if __name__ == '__main__':
    # Initializing configuration object
    config = configparser.ConfigParser()

    # Parsing a new config
    config.read('config.ini')

    # Gathers the key
    key = config.get('BOT', 'TELEGRAM_KEY')

    # Initialize bot
    start_bot(key)
