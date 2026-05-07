import logging

import httpx

from settings import settings

logger = logging.getLogger(__name__)


async def chat(message: str) -> str | None:
    """Calls the API chat endpoint. Returns None on failure."""
    url = f"{settings.api_base_url.rstrip('/')}/chat"
    try:
        async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
            response = await client.post(url, json={"message": message})
            response.raise_for_status()
            result = response.json().get("result")
            return str(result) if result is not None else None
    except (httpx.HTTPError, ValueError):
        logger.exception("Chat API call failed")
        return None
