import logging

from telegram import Update
from telegram.ext import ContextTypes

from handlers import fallback
from tasks import chat as chat_task
from utils import constants as c

logger = logging.getLogger(__name__)


async def state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int | str:
    """Handles the LLM chat state."""
    message = update.message
    assert message is not None and message.text is not None

    await message.reply_text(c.CHAT_WAITING)
    reply = await chat_task.chat(message.text)

    if reply is None:
        logger.warning("Chat backend returned no reply")
        await message.reply_text(c.CHAT_ERROR)
        return "CHAT"

    await message.reply_text(reply)
    return await fallback.retry(update, context)
