from django.contrib import admin
from django.db.models import Model
from django.contrib.admin.exceptions import AlreadyRegistered
from .models import Room, Message

# Register your models here.


def register_admin(model: Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
    
register_admin(model=Room)
register_admin(model=Message)