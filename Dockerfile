# syntax=docker/dockerfile:1

FROM python:3.9.16-alpine

LABEL maintainer = "bulatnasirov2003@gmail.com"

WORKDIR /

# Config environment Poetry
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV ADMIN = "bulat"
ENV PATH = "${PATH}:${POETRY_VENV}/bin"

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml /

RUN poetry install


# COPY pyproject.toml pyproject.toml
COPY . .
RUN poetry install

CMD [ "poetry", "run", "python3", "RFTCS/main.py" ]
