# Generated by Django 4.0.4 on 2022-06-06 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_image_comment_alter_image_photo_alter_image_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
