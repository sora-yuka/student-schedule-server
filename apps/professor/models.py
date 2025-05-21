from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfessorModel(models.Model):
    owner = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE, 
        limit_choices_to={"is_teacher": True, "is_staff": False},
    )
    pfp = models.ImageField(upload_to="uploads/pfp/", blank=True)
    
    def __str__(self) -> str:
        return self.owner.username
