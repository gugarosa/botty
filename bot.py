import configparser
import logging

from telegram.ext import Filters, MessageHandler, Updater

from handlers import error, text, voice

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Gets the logging object
logger = logging.getLogger(__name__)


def start_bot(key):
    """Main process to initiate a customized bot needs.

    """

    logger.info(f'Starting the bot ...')

    # Initializing base class with Bot's token
    updater = Updater(key, use_context=True)

    # Getting the dispatcher to attach new handlers
    dp = updater.dispatcher

    # Part-of-speech tagging when receiving new
    dp.add_handler(MessageHandler(Filters.text, text.pos_tagger))

    # Saving a newly voice update
    dp.add_handler(MessageHandler(Filters.voice, voice.save))

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
