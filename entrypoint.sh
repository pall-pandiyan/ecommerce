#!/bin/bash

cd ecommerce
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver_plus 0:8000
