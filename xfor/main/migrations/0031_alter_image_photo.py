# Generated by Django 4.0.4 on 2022-07-25 13:21

from django.db import migrations, models
import main.helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0030_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="photo",
            field=models.ImageField(
                upload_to=main.helpers.helpers.PathAndRenameDate(
                    "photos/posts/2022/7/25/"
                ),
                verbose_name="Фото",
            ),
        ),
    ]
