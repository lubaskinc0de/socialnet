# Generated by Django 4.0.4 on 2022-05-14 10:06

from django.db import migrations, models
import main.helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0015_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="default/default.png",
                upload_to=main.helpers.helpers.PathAndRenameDate("photos/"),
                verbose_name="Аватарка",
            ),
        ),
    ]
