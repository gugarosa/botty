import logging

from utils import locale

from telegram.ext import ConversationHandler

# Path to downkoad saved voice files
DOWNLOAD_PATH = 'data/voices/'

# Gets the logging object
logger = logging.getLogger(__name__)

# Gathering locale strings
lang = locale.get()


def save(update, context):
    """Saves a newly received voice update.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    logger.info(f'Handling voice saving ...')

    # Gathers the voice update
    voice = update.message.voice

    # Gets its unique ID for naming the file
    voice_file = DOWNLOAD_PATH + voice.file_id + '.ogg'

    # This will get the actual voice file and download it to an .ogg extension
    voice.get_file().download(voice_file)

    logger.info(f'Voice saved to {voice_file}')

    # Replying back to user to hold for response
    update.message.reply_text(lang['VOICE_SAVE_RESPONSE'])

    # Replying voice back
    update.message.reply_voice(voice)

    # Ending conversation
    update.message.reply_text(f'Quando precisar, é só voltar a falar comigo.')

    return ConversationHandler.END
