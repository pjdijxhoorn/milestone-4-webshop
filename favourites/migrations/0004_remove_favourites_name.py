# Generated by Django 3.0.1 on 2021-12-09 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0003_favourites_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='name',
        ),
    ]
