from django.db import models
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание")
    capacity = models.IntegerField(
        "Вместимость сессии",
        default=15,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
    )
    image = ResizedImageField(size=[300, 300], upload_to="img/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
