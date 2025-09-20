FROM python:3.13.1-slim-bookworm AS base

FROM base AS builder
WORKDIR /code
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1
COPY pyproject.toml uv.lock /code/
RUN uv sync \
    --frozen \
    --no-dev \
    --no-install-project
COPY . /code
WORKDIR /code
RUN uv sync --frozen --no-dev --no-editable



FROM base AS runner
RUN groupadd --gid 2000 nonroot && useradd --uid 1000 --gid 2000 -m nonroot
WORKDIR /code
COPY --from=builder --chown=nonroot:nonroot /code /code
ENV PATH="/code/.venv/bin:$PATH"
USER nonroot
ENTRYPOINT ["python", "app.py"]
