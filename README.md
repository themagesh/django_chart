Python install 
Linux Terminal open 
 #Linux: sudo apt install python3
#Check Python 3 version:python3  - -Version

 #Windows: https://www.python.org/downloads/
Windows cmd and windows powershell open
 #Check version:python --version

Python version:

#linux : python -m ensurepip --upgrade
#windows : py -m ensurepip --upgrade
Pip version check:

#Linux :  pip --version
#windows:pip --version
Django install:
Windows :pipenv install django
Linux :pipenv install django
Pip Environment:
Windows: pipenv shell
Linux : pipenv shell

Windows and linux Start project django:
//django-admin
//django-admin startproject  png_dcm 
//python manage.py
//python manage.py startapp  png_dcmapp
//python manage.py runserver
Linux : 
//python3 manage.py 
//python3 manage.py runserver
Create Virtual Environment:

#Windows:py -m venv .venv
#linux: python3 -m venv .venv

Activate environment:
windows:
.venv\Scripts\activate.bat
Linux:
source .venv/bin/activate

#File collectstatic;
   python manage.py collectstatic

#pip package delete
  pip3 uninstall TIME-python

#Django-related packages and their versions:
  pip freeze | grep Django

#Django installed packages
  pip list
you can also check that file for the list of Django packages and their versions.

Creat file:
  requirements.txt
Django's get_version method
   python manage.py shell
Django packages installed
  import django
print(django.get_version())
