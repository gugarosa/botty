import logging

from telegram.ext import ConversationHandler

# Path to downkoad saved voice files
DOWNLOAD_PATH = 'storage/voices/'

# Gets the logging object
logger = logging.getLogger(__name__)


def save(voice):
    """Saves a newly received voice update.

    Args:
        voice (Voice): A telegram.Voice object for further handling.

    """

    logger.info(f'Handling voice saving ...')

    # Gets its unique ID for naming the file
    voice_file = DOWNLOAD_PATH + voice.file_id + '.ogg'

    # This will get the actual voice file and download it to an .ogg extension
    voice.get_file().download(voice_file)

    logger.info(f'Voice saved to {voice_file}')
