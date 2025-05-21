from django.db import models
from django.contrib.auth import get_user_model

from apps.faculties.models import GroupsModel, SpecialtyModel, FacultiesModel
from ext.choices import COURSE

# Create your models here.

User = get_user_model()


class StudentProfileModel(models.Model):
    owner = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE,
        limit_choices_to={"is_teacher": False, "is_staff": False},
    )
    pfp = models.ImageField(upload_to="uploads/pfp/", blank=True)
    course = models.CharField(max_length=100, choices=COURSE)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.owner} | {self.course} | {self.group}"