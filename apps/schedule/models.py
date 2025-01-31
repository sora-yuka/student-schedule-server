from django.db import models

from apps.faculties.models import GroupsModel
from ext.choices import SEMESTER, WEEK_DAYS, WEEK_VARIANCE, LESSON_TYPE, PERIOD

# Create your models here.
    
    
class LessonModel(models.Model):
    schedule = models.ForeignKey(to="ScheduleModel", on_delete=models.CASCADE)
    period = models.CharField(max_length=100, null=True, blank=True, choices=PERIOD)
    week_variance = models.CharField(max_length=100, null=True, blank=True, choices=WEEK_VARIANCE)
    lesson_type = models.CharField(max_length=100, null=True, blank=True, choices=LESSON_TYPE)
    class_room = models.CharField(max_length=200)
    lesson_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    number_of_weeks = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.lesson_name} | {self.professor} | {self.class_room}"


class ScheduleModel(models.Model):
    week_day = models.CharField(max_length=100, choices=WEEK_DAYS)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE, related_name="schedule_group")
    
    def __str__(self) -> str:
        return f"{self.group} | {self.week_day}"


class SemesterScheduleModel(models.Model):
    onset = models.DateField()
    end = models.DateField()
    semester = models.CharField(max_length=100, choices=SEMESTER)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE, related_name="group_schedule")
    monday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="monday_schedule")
    tuesday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="tuesday_schedule")
    wednesday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="wednesday_schedule")
    thursday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="thursday_schedule")
    friday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="friday_schedule")
    saturday = models.ForeignKey(to=ScheduleModel, on_delete=models.CASCADE, blank=True, null=True, related_name="saturday_schema")
    
    def __str__(self) -> str:
        return f"{self.semester} semester | FROM '{self.onset}' TO '{self.end}' | {self.group}"