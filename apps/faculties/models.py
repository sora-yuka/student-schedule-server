from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class GroupsModel(models.Model):
    group_name = models.CharField(max_length=100)
    group_members = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.group_name


class SpecialtyModel(models.Model):
    specialty_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.specialty_name


class FacultiesModel(models.Model):
    faculty_name = models.CharField(max_length=200)
    specialty = models.ForeignKey(to=SpecialtyModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.faculty_name
