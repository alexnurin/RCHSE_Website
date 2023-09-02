from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        max_length=255
    )
    first_name = models.CharField(
        verbose_name='name',
        max_length=100
    )
    last_name = models.CharField(
        verbose_name='surname',
        max_length=100
    )
    is_staff = models.BooleanField(
        verbose_name='admin',
        default=False
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


