# Generated by Django 4.0.4 on 2022-04-13 21:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0003_alter_profile_options_alter_token_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="followers",
            field=models.ManyToManyField(
                related_name="followers",
                related_query_name="followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
