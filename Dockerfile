FROM python:3.7.3-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ADD requirements.txt /app/

RUN apt-get update \
    && apt-get install -y libpq-dev python3-dev gcc \
    && pip install -r /app/requirements.txt --no-cache-dir

RUN useradd twitter_feed && chown -R twitter_feed /app

RUN mkdir /twitter_feed_media && chown -R twitter_feed /twitter_feed_media

USER twitter_feed
COPY . /app
RUN ./manage.py collectstatic --no-input