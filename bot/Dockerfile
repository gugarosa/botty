FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /botty/bot

COPY pyproject.toml /botty/bot/
RUN pip install --upgrade pip && pip install .

COPY . /botty/bot

RUN mkdir -p /botty/storage/voices /botty/storage/transcripts \
    && useradd --create-home --uid 1000 botty \
    && chown -R botty:botty /botty
USER botty

CMD ["python", "bot.py"]
