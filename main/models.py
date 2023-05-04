from django.db import models


class Users(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
