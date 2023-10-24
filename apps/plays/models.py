from django.db import models
from datetime import time
from apps.games.models import Game


class Play(models.Model):
    year = models.PositiveIntegerField(default=2020)
    month = models.PositiveIntegerField(default=9)
    day = models.PositiveIntegerField(default=1)
    time = models.TimeField(default=time(16, 00))
    game = models.ForeignKey(Game, models.CASCADE)

    def __str__(self):
        if self.time is None:
            self.time = time(16, 1)
        return f"{self.game.title}: {self.year:04}, {self.day:02}.{self.month:02}, старт в {self.time}"

    class Meta:
        verbose_name = "Постановка"
        verbose_name_plural = "Постановки"


class Record(models.Model):
    play = models.ForeignKey(Play, models.CASCADE)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    need_pass = models.BooleanField("Нужен пропуск")
    patronymic = models.CharField("Отчество", max_length=50)
    vk_link = models.URLField("Ссылка на ВК")
    preferable_mates = models.TextField("Предпочтения по сессии")
    preferable_role = models.TextField("Предпочтения по роли")
    first_game = models.BooleanField("Это твоя первая игра?")

    def __str__(self):
        return f"{self.name} {self.surname}, {self.play}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
