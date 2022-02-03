FROM python:3.9

WORKDIR /app

RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .

ENV POETRY_VIRTUALENVS_CREATE false
RUN poetry install --no-dev --no-interaction --no-ansi
COPY . /app
