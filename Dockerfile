FROM python:3.11

RUN apt-get update && apt-get install -y \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

