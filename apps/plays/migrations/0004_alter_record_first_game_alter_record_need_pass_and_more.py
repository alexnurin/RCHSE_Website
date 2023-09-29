# Generated by Django 4.2.4 on 2023-09-22 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("plays", "0003_record"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="first_game",
            field=models.BooleanField(verbose_name="Это твоя первая игра?"),
        ),
        migrations.AlterField(
            model_name="record",
            name="need_pass",
            field=models.BooleanField(verbose_name="Нужен пропуск"),
        ),
        migrations.AlterField(
            model_name="record",
            name="play",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plays.play"
            ),
        ),
    ]
