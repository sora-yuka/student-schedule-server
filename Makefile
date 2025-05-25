r:
	./manage.py runserver 0.0.0.0:8000

m:
	./manage.py makemigrations
	./manage.py migrate

up:
	./manage.py loaddata ext/commits/general_data.json --exclude contenttypes

su:
	./manage.py createsuperuser

static:
	./manage.py collectstatic

build:
	docker compose down
	@if [ ! -z "$(shell docker images -q student-schedule__server-server)" ]; then \
        docker rmi student-schedule__server-server; \
    fi
	docker compose up --build
