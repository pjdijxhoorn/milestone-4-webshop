# Generated by Django 3.0.1 on 2021-12-10 09:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20211209_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
