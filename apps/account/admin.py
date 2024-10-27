from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.exceptions import AlreadyRegistered

# Register your models here.

User = get_user_model()

def admin_register(model: models.Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
    
admin_register(model=User)