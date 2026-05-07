import logging

import httpx

from settings import settings

logger = logging.getLogger(__name__)


async def speech_text(audio_path: str) -> str | None:
    """Calls the API to transcribe a voice file. Returns None on failure."""
    url = f"{settings.api_base_url.rstrip('/')}/speech"
    try:
        async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
            response = await client.post(url, json={"audio_path": audio_path})
            response.raise_for_status()
            result = response.json().get("result")
            return str(result) if result is not None else None
    except (httpx.HTTPError, ValueError):
        logger.exception("Speech API call failed")
        return None
