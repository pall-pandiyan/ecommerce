#!/bin/bash

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver_plus -b 0:8000
