FROM python:3.12.1-slim-bookworm

WORKDIR app/
RUN apt-get update && \
      apt-get -y install libpq-dev python3-dev gcc g++

COPY .streamlit .streamlit
COPY {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}
COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY ./README.md .


RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN export PYTHONPATH=/app

COPY .streamlit/config.toml /root/.streamlit/config.toml
