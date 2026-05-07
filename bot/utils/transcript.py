import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DOWNLOAD_PATH = Path("storage/transcripts")
DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)


def save(voice_id: str, transcript: str) -> None:
    """Saves a transcripted voice message to disk."""
    transcript_file = DOWNLOAD_PATH / f"{voice_id}.txt"
    transcript_file.write_text(f"{transcript}\n", encoding="utf-8")
    logger.info("Transcript saved to %s", transcript_file)
