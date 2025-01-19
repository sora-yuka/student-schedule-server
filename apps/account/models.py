from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        from uuid import uuid4
        username = f"admin | {email}"
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
    object = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return f"{self.username} - {self.email}"