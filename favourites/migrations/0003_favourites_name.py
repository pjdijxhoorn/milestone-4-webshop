# Generated by Django 3.0.1 on 2021-12-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0002_auto_20211209_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourites',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]