from django.db import models
from apps.professor.models import ProfessorModel
from apps.faculties.models import GroupsModel

def directory_path(instance: models.Model, filename: str) -> str:
    return "courses/{0}/{1}".format(instance.name, filename)


class CourseContentModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.FileField(upload_to=directory_path)
    # course = models.ForeignKey(to="CourseModel", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    
class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(to=ProfessorModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name