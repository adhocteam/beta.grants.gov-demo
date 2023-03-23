#!/usr/bin/env bash
# start-server.sh
if [ ! -f db.sqlite3 ]; then
    curl -O https://storage.googleapis.com/beta-grants-gov-prototype_cloudbuild/db/db.sqlite3
fi
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python manage.py createsuperuser --no-input
fi
gunicorn grantsdotgov.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 &
DOLLAR='$' envsubst < /app/nginx.template > /etc/nginx/sites-available/default
nginx -g "daemon off;"
