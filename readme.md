1) Start project commands:

    -python3 -m venv .venv
   
    -source .venv/bin/activate
   
    -pip install django
   
    -django-admin startproject core
   
    -cd core
   
    -python manage.py startapp test_app
   
    -python manage.py runserver 0.0.0.0:8000

    -python manage.py makemigrations
   
    -python manage.py migrate