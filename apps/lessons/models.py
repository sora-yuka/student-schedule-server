from django.db import models
from ext.choices import LESSON_TYPE

# Create your models here.


class LessonsModel(models.Model):
    lesson_type = models.CharField(max_length=100, choices=LESSON_TYPE)
    class_room = models.CharField(max_length=200)
    lesson_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    number_of_weeks = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.lesson_name} | {self.professor} | {self.class_room}"
