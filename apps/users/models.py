from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=255, blank=True, null=True)
    username = models.CharField(verbose_name="Username", max_length=100, unique=True)
    first_name = models.CharField(verbose_name="Name", max_length=100)
    last_name = models.CharField(verbose_name="Surname", max_length=100)
    is_admin = models.BooleanField(verbose_name="Moderator", default=False)  # Новое поле
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
