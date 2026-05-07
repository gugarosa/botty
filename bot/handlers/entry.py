import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from utils import constants as c

logger = logging.getLogger(__name__)


async def options(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Handles the initial options from first interaction."""
    message = update.message
    assert message is not None and message.chat is not None

    logger.info("New entry from message: %s", message.text)

    first_name = message.chat.first_name or "there"
    keyboard = [c.ENTRY_OPTIONS[:2], c.ENTRY_OPTIONS[2:]]
    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await message.reply_text(
        c.ENTRY_OPTIONS_RESPONSE.format(name=first_name),
        reply_markup=markup,
    )
    return "AWAIT_OPTIONS"
