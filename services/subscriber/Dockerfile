FROM python:3.11

WORKDIR /app

ADD . /app

RUN pip install pika

CMD ["python", "server.py"]