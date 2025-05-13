from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # foydalanuvchi yoshini yozmasa ham bo'ladi
    age = models.PositiveIntegerField(null=True, blank=True)
