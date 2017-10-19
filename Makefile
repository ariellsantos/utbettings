###################################
#
#	DEVELOPER COMMANDS
#
##################################

start:
	python manage.py runserver 8001

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations


install_paq:
	pip install -r requirements.txt

ver_paq:
	pip freeze