FROM python:3.9

ADD . .

RUN pip install -e .
