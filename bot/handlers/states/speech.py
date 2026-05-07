import logging

from telegram import Update
from telegram.ext import ContextTypes

from handlers import fallback
from tasks import speech
from utils import constants as c
from utils import transcript, voice

logger = logging.getLogger(__name__)


async def state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int | str:
    """Handles the speech-recognition state."""
    message = update.message
    assert message is not None and message.voice is not None

    voice_id, voice_path = await voice.save(message.voice)
    await message.reply_text(c.SPEECH_WAITING)

    text = await speech.speech_text(voice_path)
    if text is None:
        logger.warning("Transcription not found for voice: %s", voice_path)
        await message.reply_text(c.SPEECH_ERROR)
        return "SPEECH"

    transcript.save(voice_id, text)
    await message.reply_html(c.SPEECH_RESPONSE.format(transcript=text))
    return await fallback.retry(update, context)
