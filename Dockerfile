FROM python:3.10-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=src.app.py
CMD ["flask", "run", "--host", "0.0.0.0"]

## syntax=docker/dockerfile:1
#
#ARG PYTHON_VERSION=3.10
#FROM python:${PYTHON_VERSION}-slim as base
#
## Prevents Python from writing pyc files.
#ENV PYTHONDONTWRITEBYTECODE=1
#
## Keeps Python from buffering stdout and stderr to avoid situations where
## the application crashes without emitting any logs due to buffering.
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
## Create a non-privileged user that the app will run under.
## See https://docs.docker.com/go/dockerfile-user-best-practices/
##ARG UID=10001
##RUN adduser \
###    --disabled-password \
##    --gecos "" \
##    --home "/nonexistent" \
##    --shell "/sbin/nologin" \
##    --no-create-home \
##    --uid "${UID}" \
##    appuser
#
## Install any needed packages specified in requirements.txt
#ENV PYTHONPATH=${PYTHONPATH}:${PWD}
##COPY pyproject.toml poetry.lock /
##RUN pip install poetry
##RUN poetry config virtualenvs.create false
##RUN poetry install --no-root
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#
## Switch to the non-privileged user to run the application.
##USER appuser
#
## Copy the source code into the container.
#COPY . .
#
## Expose the port that the application listens on.
#EXPOSE 8000
#
## Run the application.
#CMD ["python", "src/app.py"]
