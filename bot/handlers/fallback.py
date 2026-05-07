import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes, ConversationHandler

from utils import constants as c

logger = logging.getLogger(__name__)


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles the interaction ending."""
    logger.info("Current interaction ended.")
    message = update.message
    assert message is not None
    await message.reply_text(c.FALLBACK_END_RESPONSE, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def retry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Asks the user whether to retry the flow."""
    message = update.message
    assert message is not None
    keyboard = [c.ENTRY_OPTIONS[:2], c.ENTRY_OPTIONS[2:]]
    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await message.reply_text(c.FALLBACK_RETRY_RESPONSE, reply_markup=markup)
    return "AWAIT_OPTIONS"
