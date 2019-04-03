import logging

# Path to downkoad saved transcript files
DOWNLOAD_PATH = 'storage/transcripts/'

# Gets the logging object
logger = logging.getLogger(__name__)


def save(id, transcript):
    """Saves a newly transcripted voice message.

    Args:
        id (str): A string containing the id of the voice message.
        transcript (str): A string containing the voice's transcription.

    """

    logger.info(f'Handling transcript saving ...')

    # Gets its unique ID for naming the file
    transcript_file = DOWNLOAD_PATH + id + '.txt'

    # This will get the actual transcript and save to its file
    with open(transcript_file, 'w') as txt:
        print(f'{transcript}', file=txt)

    logger.info(f'Transcript saved to {transcript_file}')
