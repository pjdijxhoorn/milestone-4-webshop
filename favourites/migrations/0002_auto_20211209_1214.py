# Generated by Django 3.0.1 on 2021-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='product',
        ),
        migrations.AddField(
            model_name='favourites',
            name='favourites_list',
            field=models.TextField(default=''),
        ),
    ]
