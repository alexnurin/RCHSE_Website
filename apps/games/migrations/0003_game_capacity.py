# Generated by Django 4.2.4 on 2023-10-01 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0002_alter_game_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="capacity",
            field=models.IntegerField(
                default=15,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Вместимость сессии",
            ),
        ),
    ]