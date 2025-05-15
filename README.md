# Django REST

This template provide a minimal setup to get Django work and some rules.

To run project type commands bellow:
```bash
python -m venv venv
. venv/bin/activate
pip install -r requiremenets.txt
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata ext/commits/general_data.json
./manage.py runserver 0.0.0.0:8000
```