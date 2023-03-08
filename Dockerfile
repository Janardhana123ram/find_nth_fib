FROM python:3.7

RUN mkdir /fibonacci

WORKDIR /fibonacci

ADD . /fibonacci/

RUN pip install -r requirements.txt
