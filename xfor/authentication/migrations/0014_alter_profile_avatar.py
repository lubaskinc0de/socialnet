# Generated by Django 4.0.4 on 2022-04-25 18:28

from django.db import migrations, models
import main.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default/default.png', upload_to=main.helpers.PathAndRename('photos/2022/4/25/'), verbose_name='Аватарка'),
        ),
    ]
