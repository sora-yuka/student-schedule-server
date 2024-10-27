from django.db import models

from apps.lessons.models import LessonsModel
from apps.faculties.models import GroupsModel
from ext.choices import DAYS

# Create your models here.


class ScheduleModel(models.Model):
    today = models.CharField(max_length=100, choices=DAYS)
    first_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="first_lesson_set"
        )
    second_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="second_lesson_set"
        )
    third_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="third_lesson_set"
        )
    fourth_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="fourth_lesson_set"
        )
    fifth_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="fifth_lesson_set"
        )
    sixth_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="sixth_lesson_set"
        )
    seventh_lesson = models.ForeignKey(
        to=LessonsModel, on_delete=models.CASCADE,
        blank=True, null=True, related_name="seventh_lesson_set"
        )
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.today} | {self.group.group_name}"