import logging
import random

logger = logging.getLogger(__name__)

_FAKE_AVATARS = [
    "https://i.pravatar.cc/300?img=1",
    "https://i.pravatar.cc/300?img=12",
    "https://i.pravatar.cc/300?img=33",
]


async def check_client(name: str) -> dict[str, str] | None:
    """Returns a mock client record. Always succeeds for non-empty input."""
    if not name.strip():
        return None
    slug = name.strip().lower().replace(" ", ".")
    return {
        "email": f"{slug}@example.com",
        "phone": "+1-555-0100",
        "avatar": random.choice(_FAKE_AVATARS),
    }
