Installing Updown
=================


Below are some commands for installing Updown.


## Clone the repository.

git clone https://github.com/patrickwayodi/updown.git


## If you don't have Python, install it.

sudo apt-get update

sudo apt-get install python3


## Create a virtual environment and activate it.

python3 -m venv ~/virtualenvs/updown

source ~/virtualenvs/updown/bin/activate


## Install Updown's dependencies.

cd updown/src

pip install --upgrade pip wheel

pip install --upgrade -r requirements/local.txt


## Migrate the database models.

python manage.py makemigrations

python manage.py migrate


## Create an admin account.

python manage.py createsuperuser


## Run the project.

python manage.py runserver

Open http://localhost:8000 on your browser.

