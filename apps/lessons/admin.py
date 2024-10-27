from django.db.models import Model
from django.contrib import admin
from django.contrib.admin.exceptions import AlreadyRegistered

from .models import LessonsModel

# Register your models here.

def admin_register(model: Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass

admin_register(model=LessonsModel)