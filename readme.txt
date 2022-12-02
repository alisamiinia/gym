create virtual env with cmd and install packages

1-python -m venv env
2-env\Scripts\activate

installed packages : 
pip install djangorestframework
pip install django-rest-knox
pip install django
python -m pip install django-cors-headers
pip install djoser
python -m pip install pillow

run server :
python .\manage.py runserver

apis :
#http://localhost:8000/api/register/
#http://localhost:8000/api/login/

(urls are in account urls .)

Python 3.10.8