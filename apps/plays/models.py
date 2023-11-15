from django.db import models
from datetime import datetime
from datetime import time
from apps.games.models import Game


class Play(models.Model):
    play_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime(year=2020, month=9, day=1, hour=16))
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    sessions_number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Постановка: {self.game.title} {self.date}"

    class Meta:
        verbose_name = "Постановка"
        verbose_name_plural = "Постановки"


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    play = models.ForeignKey(Play, models.CASCADE)
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    need_pass = models.BooleanField("Нужен пропуск", default=False)
    patronymic = models.CharField("Отчество", max_length=50, blank=True)
    vk_link = models.URLField("Ссылка на ВК")
    preferable_mates = models.TextField("Предпочтения по сессии")
    preferable_role = models.TextField("Предпочтения по роли")
    first_game = models.BooleanField("Это твоя первая игра?")

    def __str__(self):
        return f"{self.name} {self.surname}, {self.play}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
