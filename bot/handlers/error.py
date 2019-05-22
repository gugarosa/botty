import logging

# Gets the logging object
logger = logging.getLogger(__name__)


def log(update, context):
    """Logs any errors caused by any updates.

    Args:
        update (Update): An update object, basically holding vital information from a new user interaction.
        context (CallbackContext): A context object, if additional information is needed.

    """

    # Actually logs as a warning
    logger.warning('Update "%s" caused error "%s"', update, context.error)
