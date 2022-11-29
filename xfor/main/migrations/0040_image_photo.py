# Generated by Django 4.0.4 on 2022-09-11 15:39

from django.db import migrations, models
import main.helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0039_remove_image_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="photo",
            field=models.ImageField(
                default="",
                upload_to=main.helpers.helpers.PathAndRenameDate(
                    "photos/posts/2022/9/11/"
                ),
                verbose_name="Фото",
            ),
            preserve_default=False,
        ),
    ]
