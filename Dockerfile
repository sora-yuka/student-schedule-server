FROM python:3.13.1

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
&& apt-get install -y build-essential make \
&& pip install --upgrade pip \
&& pip install -r requirements.txt

COPY . /app

CMD [ "make", "m", "up", "r" ]
# CMD ["make", "m", "r"]