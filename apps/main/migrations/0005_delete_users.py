# Generated by Django 4.2.4 on 2023-09-02 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_games_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]