# Generated by Django 4.2.4 on 2023-09-20 16:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
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