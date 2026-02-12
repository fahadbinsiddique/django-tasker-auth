from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserAuthInfoModel(AbstractUser):
    full_name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.username}"


class ToDoModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    status_type = [
        ("Pending", "Pending"),
        ("InProgress", "InProgress"),
        ("Completed", "Completed"),
    ]
    status = models.CharField(choices=status_type,max_length=20)
