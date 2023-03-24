FROM python:3.11-buster

RUN apt-get update && apt-get install nginx nodejs npm gettext-base vim -y --no-install-recommends
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN npm install
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/grantsdotgov
ENV DJANGO_SETTINGS_MODULE=grantsdotgov.production_settings
ENV PYTHONUNBUFFERED=1
RUN python manage.py collectstatic
RUN chown -R www-data:www-data /app

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD exec ../start-server.sh
