# Generated by Django 4.2.4 on 2023-09-06 13:17

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Название"
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        quality=-1,
                        scale=None,
                        size=[300, 300],
                        upload_to="media/img/",
                    ),
                ),
            ],
            options={
                "verbose_name": "Игра",
                "verbose_name_plural": "Игры",
            },
        ),
    ]
