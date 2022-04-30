FROM python:3.8.10-alpine
LABEL maintainer "Vinicius de Oliveira"
ENV PYTHONUNBUFFERED=1
COPY . /var/www
WORKDIR /var/www
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev python3-dev postgresql-dev && pip install -r requirements.txt && python manage.py collectstatic --noinput
ENTRYPOINT python manage.py runserver 0.0.0.0:8000 --noreload
EXPOSE 8000