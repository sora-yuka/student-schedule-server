from django.db import models

# Create your models here.


class FacultiesModel(models.Model):
    faculty_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.faculty_name


class SpecialtyModel(models.Model):
    faculty = models.ForeignKey(to=FacultiesModel, on_delete=models.CASCADE)
    specialty_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.faculty.faculty_name} | {self.specialty_name}"


class GroupsModel(models.Model):
    faculty = models.ForeignKey(to=FacultiesModel, on_delete=models.CASCADE)
    specialty = models.ForeignKey(to=SpecialtyModel, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.faculty.faculty_name} | {self.specialty.specialty_name} | {self.group_name}"
