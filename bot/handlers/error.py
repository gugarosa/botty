import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def log(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs any errors caused by updates."""
    update_repr = update if isinstance(update, Update) else "<non-Update>"
    logger.warning('Update "%s" caused error "%s"', update_repr, context.error)
