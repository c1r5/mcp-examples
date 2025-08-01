FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY servers /app/servers
COPY pyproject.toml /app/
COPY uv.lock /app/
COPY .python-version /app/

RUN uv sync --locked

CMD ["uv", "run", "-m", "servers.main"]