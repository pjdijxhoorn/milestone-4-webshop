# Generated by Django 3.0.1 on 2021-12-10 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0004_remove_favourites_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favourites',
        ),
    ]
