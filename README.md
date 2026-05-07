# Botty: A Python Telegram Bot

An async, two-service Telegram bot. The `bot/` service runs the Telegram conversation; the `api/` service exposes speech-to-text and chat endpoints backed by Azure.

Botty requires **Python 3.12+**.

---

## Architecture

```
- botty
    - api            # FastAPI service
        - handlers
            - speech.py   # POST /speech  → Azure AI Speech
            - chat.py     # POST /chat    → Azure OpenAI
    - bot            # Telegram bot (python-telegram-bot v21, async)
        - handlers
            - entry, error, fallback
            - states
                - await_options
                - mockup    # Local fake-data lookup
                - speech    # Voice transcription via /speech
                - chat      # LLM chat via /chat
        - tasks      # API clients (httpx)
        - utils      # voice/transcript helpers, constants
    - storage
        - voices         # downloaded .ogg voice messages
        - transcripts    # saved transcripts
```

### Bot conversation

On `/start` or any greeting, the bot offers four options:

- **Mockup** — looks up a (locally generated) fake client record.
- **Speech Recognition** — transcribes a voice message via Azure Speech.
- **Chat** — replies via Azure OpenAI.
- **Terminate** — ends the session.

---

## Configuration

Both services read configuration from `.env` files via `pydantic-settings`. Copy the templates:

```bash
cp api/.env.example api/.env
cp bot/.env.example bot/.env
```

### `api/.env`

| Variable | Purpose |
|---|---|
| `PORT` | API port (default `8080`) |
| `AZURE_SPEECH_KEY` / `AZURE_SPEECH_REGION` | Azure AI Speech resource |
| `AZURE_SPEECH_LANGUAGE` | Recognition language (default `en-US`) |
| `AZURE_OPENAI_ENDPOINT` | e.g. `https://your-resource.openai.azure.com` |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI key |
| `AZURE_OPENAI_API_VERSION` | API version (default `2024-10-21`) |
| `AZURE_OPENAI_DEPLOYMENT` | Your deployment name |
| `AZURE_OPENAI_SYSTEM_PROMPT` | Overrides the default system prompt |

### `bot/.env`

| Variable | Purpose |
|---|---|
| `TELEGRAM_KEY` | Telegram bot token from BotFather |
| `API_BASE_URL` | URL of the API service (default `http://api:8080`) |
| `REQUEST_TIMEOUT_SECONDS` | Per-request timeout (default `120`) |

---

## Running

### Local development

```bash
# API
cd api
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
python api.py

# Bot (in another shell)
cd bot
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
python bot.py
```

### Docker Compose

```bash
docker compose build
docker compose up -d
```

To stop:

```bash
docker compose down
```

---

## Testing & quality

```bash
# from api/ or bot/
ruff check .
mypy .
pytest
```

CI runs the same three steps for both services on every push and PR (`.github/workflows/ci.yml`).

---

## Support

If you find a bug, please open an issue on GitHub.
