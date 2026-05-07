import logging

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers import entry, error, fallback
from handlers.states import await_options, chat, mockup, speech
from settings import settings
from utils import constants as c

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def build_app() -> Application:
    if not settings.telegram_key:
        raise RuntimeError("TELEGRAM_KEY is not set. Copy bot/.env.example to bot/.env.")
    logger.info("Initializing the bot ...")
    app = Application.builder().token(settings.telegram_key).build()

    app.add_handler(
        ConversationHandler(
            entry_points=[
                CommandHandler("start", entry.options),
                MessageHandler(filters.Regex(c.ENTRY_REGEX), entry.options),
            ],
            states={
                "AWAIT_OPTIONS": [
                    MessageHandler(filters.Regex(c.AWAIT_OPTIONS_REGEX), await_options.state),
                ],
                "MOCKUP": [MessageHandler(filters.TEXT & ~filters.COMMAND, mockup.state)],
                "SPEECH": [MessageHandler(filters.VOICE, speech.state)],
                "CHAT": [MessageHandler(filters.TEXT & ~filters.COMMAND, chat.state)],
            },
            fallbacks=[
                CommandHandler("end", fallback.end),
                MessageHandler(filters.Regex(c.FALLBACK_REGEX), fallback.end),
            ],
        )
    )
    app.add_error_handler(error.log)
    return app


def main() -> None:
    app = build_app()
    app.run_polling()


if __name__ == "__main__":
    main()
