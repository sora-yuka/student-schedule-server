# This package used to test some things
import os
import sys
import django
from django.contrib.auth.hashers import make_password
from uuid import uuid4


project_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
    
def make_password(password: str) -> None:
    hashed_password = make_password(password="qwerty")
    print(hashed_password)


def calculate_differences():
    from datetime import datetime
    date_now = datetime.now()
    print(type(date_now))
    
    
calculate_differences()