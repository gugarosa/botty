import logging
from pathlib import Path

from telegram import Voice

logger = logging.getLogger(__name__)

DOWNLOAD_PATH = Path("storage/voices")
DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)


async def save(voice: Voice) -> tuple[str, str]:
    """Saves a newly received voice update.

    Returns the voice file_id and the local path it was saved to.
    """
    voice_path = DOWNLOAD_PATH / f"{voice.file_id}.ogg"

    file = await voice.get_file()
    await file.download_to_drive(custom_path=str(voice_path))

    logger.info("Voice saved to %s", voice_path)
    return voice.file_id, str(voice_path)
