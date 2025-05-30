FROM python:3.13-slim AS base

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=$PYTHONPATH:/app/src

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq5

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app
WORKDIR /app
RUN uv sync --locked

EXPOSE 8000
RUN ["chmod", "+x", "/app/compose/entrypoint.sh"]
ENTRYPOINT ["/app/compose/entrypoint.sh"]