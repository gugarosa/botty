FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /botty/api

COPY pyproject.toml /botty/api/
RUN pip install --upgrade pip && pip install .

COPY . /botty/api

RUN useradd --create-home --uid 1000 botty && chown -R botty:botty /botty
USER botty

EXPOSE 8080
CMD ["python", "api.py"]
