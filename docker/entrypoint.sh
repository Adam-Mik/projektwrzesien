#!/bin/sh

# Wykonaj migracje
echo "Running Django migrations..."
python manage.py migrate --noinput

# Utwórz superużytkownika, jeśli nie istnieje
echo "Creating Django superuser..."
export DJANGO_SUPERUSER_PASSWORD=adminpassword
python manage.py createsuperuser --noinput --username admin --email admin@example.com

# Uruchom serwer Django
exec "$@"