# Generated by Django 4.0.4 on 2022-04-19 23:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайкнувшие'),
        ),
    ]
