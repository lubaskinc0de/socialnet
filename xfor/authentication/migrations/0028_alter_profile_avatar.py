# Generated by Django 4.0.4 on 2022-07-17 11:21

from django.db import migrations, models
import main.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default/default.png', upload_to=main.helpers.PathAndRename('photos/2022/7/17/'), verbose_name='Аватарка'),
        ),
    ]
