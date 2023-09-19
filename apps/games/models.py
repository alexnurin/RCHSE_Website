from django.db import models
from django_resized import ResizedImageField


class Game(models.Model):
    title = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание")
    image = ResizedImageField(size=[300, 300], upload_to="media/img/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
