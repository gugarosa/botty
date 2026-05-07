import pytest

from tasks import mock
from utils import constants as c


def test_constants_states_align_with_options() -> None:
    # Each non-terminate option must have a state and response.
    assert len(c.AWAIT_OPTIONS_STATES) == len(c.ENTRY_OPTIONS) - 1
    assert len(c.AWAIT_OPTIONS_RESPONSES) == len(c.ENTRY_OPTIONS) - 1


@pytest.mark.asyncio
async def test_mock_check_client_returns_record() -> None:
    result = await mock.check_client("Ada Lovelace")
    assert result is not None
    assert result["email"].endswith("@example.com")
    assert "phone" in result
    assert "avatar" in result


@pytest.mark.asyncio
async def test_mock_check_client_rejects_empty() -> None:
    assert await mock.check_client("   ") is None
