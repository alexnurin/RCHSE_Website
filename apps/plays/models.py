from django.db import models
from apps.games.models import Game


class Play(models.Model):
    year = models.IntegerField()
    game = models.ForeignKey(Game, models.CASCADE)

    def __str__(self):
        return f"{self.game.title}: {self.year}"

    class Meta:
        verbose_name = "Постановка"
        verbose_name_plural = "Постановки"
