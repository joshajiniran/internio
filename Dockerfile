FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1dock
ENV PYTHONUNBUFFERED 1

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
    netcat \
    libpq-dev \
    python-dev \
    gcc \
    && apt-get -q clean

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python manage.py runserver 0.0.0.0:8000