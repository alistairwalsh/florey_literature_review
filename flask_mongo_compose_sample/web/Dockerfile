FROM python:2.7
MAINTAINER Alistair Walsh "alistair.walsh@me.com"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
