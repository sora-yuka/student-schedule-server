from django.db import models
from apps.professor.models import ProfessorModel
from apps.faculties.models import GroupsModel

def directory_path(instance: models.Model, filename: str) -> str:
    return "courses/{course_name}/{content_name}/{file_name}".format(
        course_name=instance.course_content.course.name, 
        content_name=instance.course_content.name, 
        file_name=filename,
    )


class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(to=ProfessorModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    group = models.ManyToManyField(to=GroupsModel, blank=True)
    
    def __str__(self) -> str:
        return self.name


class CourseContentModel(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(to=CourseModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.course} | {self.name}"

    
class ContentModel(models.Model):
    course_content = models.ForeignKey(to=CourseContentModel, on_delete=models.CASCADE)
    content = models.FileField(upload_to=directory_path)