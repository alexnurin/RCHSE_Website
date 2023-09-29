from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=255)
    username = models.CharField(verbose_name="username", max_length=100, unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    is_staff = models.BooleanField(verbose_name="admin", default=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
