# Generated by Django 4.0.4 on 2022-04-21 17:31

from django.db import migrations, models
import main.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default/default.png', upload_to=main.helpers.PathAndRename('photos/2022/4/21/'), verbose_name='Аватарка'),
        ),
    ]
