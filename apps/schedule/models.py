from django.db import models

from apps.faculties.models import GroupsModel
from apps.professor.models import ProfessorModel
from ext.choices import SEMESTER, WEEK_DAYS, WEEK_VARIANCE, LESSON_TYPE, START_PERIOD, END_PERIOD, COURSE

# Create your models here.
    
    
class ScheduleModel(models.Model):
    week_day = models.CharField(max_length=100, choices=WEEK_DAYS)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE, related_name="schedules")
    semester = models.CharField(max_length=50, choices=SEMESTER)
    
    def __str__(self) -> str:
        return f"{self.group} | {self.week_day} | {self.semester}"


class LessonModel(models.Model):
    schedule = models.ForeignKey(to="ScheduleModel", on_delete=models.CASCADE)
    professor = models.OneToOneField(to=ProfessorModel, on_delete=models.CASCADE)
    start_period = models.CharField(max_length=100, null=True, blank=True, choices=START_PERIOD)
    end_period = models.CharField(max_length=100, null=True, blank=True, choices=END_PERIOD)
    week_variance = models.CharField(max_length=100, null=True, blank=True, choices=WEEK_VARIANCE)
    lesson_type = models.CharField(max_length=100, null=True, blank=True, choices=LESSON_TYPE)
    class_room = models.CharField(max_length=200)
    lesson_name = models.CharField(max_length=200)
    number_of_weeks = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.lesson_name} | {self.professor} | {self.class_room}"


class SemesterScheduleModel(models.Model):
    onset = models.DateField()
    end = models.DateField()
    semester = models.CharField(max_length=100, choices=SEMESTER)
    group = models.ForeignKey(to=GroupsModel, on_delete=models.CASCADE, related_name="group_schedule")
    schedules = models.ManyToManyField(to=ScheduleModel, related_name="semester_schedules")
    course = models.CharField(max_length=50, choices=COURSE)
    
    
    def __str__(self) -> str:
        return f"{self.semester} semester | FROM '{self.onset}' TO '{self.end}' | {self.group}"