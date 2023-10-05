FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY server /server
WORKDIR /server
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser -D service-user

USER service-user
