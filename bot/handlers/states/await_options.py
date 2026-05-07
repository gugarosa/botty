import logging

from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes

from utils import constants as c

logger = logging.getLogger(__name__)


async def state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Handles a chosen option by the user."""
    message = update.message
    assert message is not None and message.text is not None
    option = message.text

    logger.info("User option: %s", option)

    state_index = c.ENTRY_OPTIONS.index(option)
    await message.reply_text(
        c.AWAIT_OPTIONS_RESPONSES[state_index],
        reply_markup=ReplyKeyboardRemove(),
    )

    next_state = c.AWAIT_OPTIONS_STATES[state_index]
    logger.info("Redirecting to state: %s", next_state)
    return next_state
