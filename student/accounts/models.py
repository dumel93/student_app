from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.contrib import auth

# Create your models here.\


class User(AbstractUser):
    is_student=models.BooleanField(default=True)

