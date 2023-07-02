#!/bin/bash

pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0:8000
