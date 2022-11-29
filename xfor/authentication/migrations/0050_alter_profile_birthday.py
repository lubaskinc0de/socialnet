# Generated by Django 4.0.4 on 2022-09-29 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentication",
            "0049_alter_contact_options_alter_customauthtoken_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateField(
                default=datetime.datetime(2022, 9, 29, 18, 47, 58, 933344, tzinfo=utc),
                verbose_name="День рождения",
            ),
            preserve_default=False,
        ),
    ]
