from django.contrib import admin
from .models import NewsModel, ResourceModel

# Register your models here.


class ResourceInline(admin.TabularInline):
    model = ResourceModel
    extra = 1


@admin.register(NewsModel)
class NewsModel(admin.ModelAdmin):
    inlines = [ResourceInline]