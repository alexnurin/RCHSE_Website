from django.db import models
from django_resized import ResizedImageField


class Users(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.TextField('Почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Games(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = ResizedImageField(size=[300, 300], upload_to='img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
