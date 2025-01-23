FROM python:3.13.1

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get install -y build-essential make \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

CMD [ "make", "m", "up", "r" ]