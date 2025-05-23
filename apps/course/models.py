from django.db import models
from apps.professor.models import ProfessorModel
from apps.faculties.models import GroupsModel


class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(to=ProfessorModel, on_delete=models.CASCADE)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name