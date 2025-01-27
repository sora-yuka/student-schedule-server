from django.contrib import admin
from django.db.models import Model
from django.contrib.admin.exceptions import AlreadyRegistered

from .models import LessonModel, ScheduleModel, SemesterScheduleModel

# Register your models here.


class LessonInline(admin.TabularInline):
    model = LessonModel
    extra = 1
    
    
@admin.register(ScheduleModel)
class ScheduleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


def admin_register(model: Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
    
admin_register(model=SemesterScheduleModel)
