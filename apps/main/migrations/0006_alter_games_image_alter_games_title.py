# Generated by Django 4.2.4 on 2023-09-04 15:05

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_delete_users"),
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
                upload_to="media/img/",
            ),
        ),
        migrations.AlterField(
            model_name="games",
            name="title",
            field=models.CharField(max_length=50, unique=True, verbose_name="Название"),
        ),
    ]
