# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
WORKDIR /RFT_CS
COPY pyproject.toml pyproject.toml
RUN poetry install
COPY . .
CMD [ "python3", "RFTCS", "main.py" ]
