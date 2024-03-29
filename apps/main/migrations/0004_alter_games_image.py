# Generated by Django 4.2.4 on 2023-08-23 11:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_games_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="games",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format=None,
                keep_meta=True,
                quality=-1,
                scale=None,
                size=[300, 300],
                upload_to="img/",
            ),
        ),
    ]
