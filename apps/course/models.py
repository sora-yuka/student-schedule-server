from django.db import models


class Course:
    ...


class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    # professor = models.ForeignKey()