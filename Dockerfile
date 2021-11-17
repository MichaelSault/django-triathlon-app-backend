FROM python:3.9-alpine
LABEL maintainer="MichaelSault"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk update
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cahce --virtual .temp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
