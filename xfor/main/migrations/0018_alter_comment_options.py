# Generated by Django 4.0.4 on 2022-05-08 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_image_created_at_alter_image_post_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
