# syntax=docker/dockerfile:1

FROM python:3.9.16-alpine

LABEL maintainer = "bulatnasirov2003@gmail.com"

# COnfig environment Poetry
ENV ADMIN = "bulat"
ENV POETRY_VERSION = 1.0.0
ENV POETRY_HOME = /opt/poetry
ENV POETRY_VENV = /opt/poetry-venv
ENV POETRY_CACHE_DIR = /opt/.cache
# ENV POETRY_VIRTUALENVS_CREATE = false

WORKDIR /RFT_CS

RUN python3 - m .venv ${POETRY_VENV} \
    && ${POETRY_VENV}/bin/pip install -U pip setuptools \
    && ${POETRY_VENV}/bin/pip install poetry==${POETRY_VERSION}

ENV PATH = "${PATH}:${POETRY_VENV}/bin"

# COPY pyproject.toml pyproject.toml
COPY . .
RUN poetry install

CMD [ "poetry", "run", "python3", "RFTCS/main.py" ]
