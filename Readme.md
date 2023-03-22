[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)
## Awards

The awards application is the website that show the link of my different project, April 5th, 2019.
## By Kayitare Cynthia

## Description
Thi sis simple website where user have to login if he/she already have an account or signup to create an account if he/she doesn't have an account. after signin he/she can create a profile adding project.or click on the screen short photo of the project where he have to rate it based on how he/she is designed.he can also view the running project by click on the title of the project.
## Specifications
* Sign in to the application for stating using the applicstion.
* he/she can see different screenshort link project photo.
* he/she can create profile,ar change password
* she can click on one of the project where he/she can view the hosted project and where he can click on rate button to rate the project
* he/she can search the project name

## Set Up and Installations
Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* django==1.11
* bootsrap
## Clone the Repository
Run the following command on the terminal:
* git clone https://github.com/KAYITARES/awardo.git
* type cd awardz on terminal

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

* virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
* Install dependancies
* Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
* psql
* CREATE DATABASE awards;
## env file
Create .env file and paste the following:

SECRET_KEY = '<Secret_key>'
DBNAME = 'insto'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

## Run initial Migration

python3.6 manage.py check
python manage.py makemigrations awardo
python3.6 manage.py sqlmigrate awardo 0001
python3.6 manage.py migrate

## Run the app

python3.6 manage.py runserver
copy: http://127.0.0.1:8000/ past to the browser
## Known bugs
No bugs but in case of encounter contact me.

## Technologies used
- Python 3.6
- HTML for the structure
- Bootstrap 4 for the design
- JavaScript
- Heroku for the deployment
- Postgresql for the database
## Support and contact details

* for any support please contact me on cyntkayitare@gmail.com or
* phone:0788774039 

## License
[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **Kayitare cynthia**

