import configparser
import logging

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from handlers import entry, error, fallback
from handlers.states import await_options, client, incidence, suggestion
from utils import constants as c

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Gets the logging object
logger = logging.getLogger(__name__)


def init(key):
    """Main process to initiate a customized bot needs.

    Args:
        key (str): A string holding the Telegram's API bot key.

    """

    logger.info(f'Initializing the bot ...')

    # Initializing base class with Bot's token
    updater = Updater(key, use_context=True)

    # Getting the dispatcher to attach new handlers
    dp = updater.dispatcher

    # Add conversation handler to handle bot's states
    dp.add_handler(
        ConversationHandler(
            entry_points=[
                CommandHandler('start', entry.options, pass_user_data=True),
                MessageHandler(Filters.regex(c.ENTRY_REGEX), entry.options,
                               pass_user_data=True)
            ],
            states={
                'AWAIT_OPTIONS': [MessageHandler(Filters.regex(c.AWAIT_OPTIONS_REGEX), await_options.state, pass_user_data=True)],
                'CLIENT': [MessageHandler(Filters.text, client.state, pass_user_data=True)],
                'INCIDENCE': [MessageHandler(Filters.voice, incidence.state, pass_user_data=True)],
                'SUGGESTION': [MessageHandler(Filters.text, suggestion.state, pass_user_data=True)]
            },
            fallbacks=[
                CommandHandler('end', fallback.end),
                MessageHandler(Filters.regex(c.FALLBACK_REGEX), fallback.end)
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
    init(key)
