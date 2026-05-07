import logging

import uvicorn
from fastapi import FastAPI

from handlers import chat, speech
from settings import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title="Botty API", version="0.2.0")
    app.include_router(speech.router)
    app.include_router(chat.router)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    logger.info("Starting Botty API on port %d", settings.port)
    uvicorn.run("api:app", host="0.0.0.0", port=settings.port, reload=False)
