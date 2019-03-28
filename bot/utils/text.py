import logging

from tasks import spacy

# Gets the logging object
logger = logging.getLogger(__name__)


def pos_tagger(sentence):
    """Handles a part-of-speech tagging using an external API

    Args:
        sentence (str): A string that will suffer part-of-speech tagging.

    Returns:
        Part-of-speech tags from input sentence.

    """

    logger.info(f'Handling part-of-speech tagging ...')

    # Calling desired task, in this case a POS tagger from Spacy's API
    pos_tag = spacy.pos_tagger(sentence)

    logger.info(f'Part-of-speech tagging: {pos_tag}')

    return pos_tag
