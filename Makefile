r:
	./manage.py runserver

m:
	./manage.py makemigrations
	./manage.py migrate

su:
	./manage.py createsuperuser

dev:
	./manage.py runserver 0.0.0.0:8000