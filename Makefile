r:
	./manage.py runserver 0.0.0.0:8000

m:
	./manage.py makemigrations
	./manage.py migrate

up:
	./manage.py loaddata ext/commits/general_data.json

su:
	./manage.py createsuperuser

static:
	./manage.py collectstatic

build:
	docker-compose down
	@if [ ! -z "$(shell docker images -q student-schedule-web)" ]; then \
        docker rmi student-schedule-web; \
    fi
	docker-compose up --build