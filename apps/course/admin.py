from django.contrib import admin
from django.db.models import Model
from django.contrib.admin.exceptions import AlreadyRegistered

from .models import CourseModel, CourseContentModel, ContentModel

# Register your models here.


class ContentInline(admin.TabularInline):
    model = ContentModel
    extra = 1
    

@admin.register(CourseContentModel)
class CourseContentModel(admin.ModelAdmin):
    inlines = [ContentInline]


admin.site.register(CourseModel)