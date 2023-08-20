#!/bin/bash

pip install -r requirements.txt

# cd ecommerce
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py runserver_plus 0:8000
