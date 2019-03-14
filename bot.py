import json
import logging

import requests
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Gets the logging object
logger = logging.getLogger(__name__)

# URL to call external API
PREDICT_URL = 'http://localhost:8080'


def start(update, context):
    """Send a message when the command /start is issued.

    """

    update.message.reply_text('Olá. Sou um comando /start')


def help(update, context):
    """Send a message when the command /help is issued.

    """

    update.message.reply_text('Olá. Sou um comando /help!')


def predict(message):
    # Defines the data structure
    data = {
        'message': message
    }

    # Transform object into json
    payload = json.dumps(data)

    # Tries to perform the request
    try:
        # Performs the post
        r = requests.post(PREDICT_URL, data=payload)

        # Gets the response
        response = json.loads(r.text)

        # Gathers the result key
        result = response['result']

        return result

    except:
        raise ConnectionError


def echo(update, context):
    """Echo the user message.

    """

    # Calls the predict method
    pred = predict(update.message.text)

    # Logs that prediction was successfull
    logger.info(f'Message sent: {update.message.text}.')

    # Sends the message back
    update.message.reply_text(pred)


def error(update, context):
    """Log Errors caused by Updates.

    """

    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot.

    """

    logger.info(f'Starting the bot ...')

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "707625587:AAHJ4oox7UfFd1DIgo3Vrbri8eJRvfqNRoU", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
