#!/bin/sh
# backend/entrypoint.sh

# Espera a que la base de datos esté lista
echo "Esperando a la base de datos..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "Base de datos lista."

# Ejecuta los comandos de Django
echo "Ejecutando comandos de Django..."
python manage.py collectstatic --no-input
python manage.py makemigrations --noinput
python manage.py makemigrations blog --noinput
python manage.py makemigrations project --noinput
python manage.py makemigrations me --noinput
python manage.py makemigrations experience --noinput
python manage.py makemigrations contact --noinput
python manage.py makemigrations skill --noinput
python manage.py migrate blog --noinput
python manage.py migrate
 

# Inicia Gunicorn
echo "Iniciando servidor Gunicorn..."
exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
