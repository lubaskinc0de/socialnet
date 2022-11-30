# Generated by Django 4.0.4 on 2022-05-22 09:44

from django.db import migrations, models
import main.helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0021_alter_token_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
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
