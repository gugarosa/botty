import logging

from telegram import Update
from telegram.ext import ContextTypes

from handlers import fallback
from tasks import mock
from utils import constants as c

logger = logging.getLogger(__name__)


async def state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int | str:
    """Handles the mockup client lookup state."""
    message = update.message
    assert message is not None and message.text is not None
    client = message.text

    logger.info("Searching for client: %s", client)
    result = await mock.check_client(client)

    if result is None:
        logger.warning("Mockup not found: %s", client)
        await message.reply_text(c.MOCKUP_ERROR)
        return "MOCKUP"

    await message.reply_html(
        c.MOCKUP_RESPONSE.format(client=client, email=result["email"], phone=result["phone"])
    )
    await message.reply_photo(result["avatar"])
    return await fallback.retry(update, context)
