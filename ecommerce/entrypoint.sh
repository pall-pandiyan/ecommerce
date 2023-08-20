#!/bin/bash

# updating the python package manager first
echo "==> Upgrading pip!"
pip install --upgrade pip

# install any missing python packages
echo
echo
echo "===> Installing pip packages!"
pip install -r requirements.txt

# if encountered any migration issue we can manually wipe out the old migrations.
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -name "*.pyc" -delete

# just to be sure run migration for all databases configured
echo
echo
echo "===> Running database migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# collect the static files into BASE_DIR / static
echo
echo
echo "===> Collecting static files"
python manage.py collectstatic --noinput

if [[ "$PRODUCTION_SERVER" == "0" ]]; then
    # running the development server on 0:8000
    echo
    echo
    echo "===> Running the developement server"
    # python manage.py runserver 0.0.0.0:8000
    python manage.py runserver_plus 0.0.0.0:8000
else
    # to deploy the production server
    echo
    echo
    echo "===> Running the production server"
    gunicorn --workers=4 -b 0.0.0.0 ecommerce.wsgi
fi
