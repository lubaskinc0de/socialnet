# Generated by Django 4.0.4 on 2022-04-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Действует?'),
        ),
        migrations.AddField(
            model_name='token',
            name='token_type',
            field=models.CharField(default='confirm', max_length=50, verbose_name='Тип'),
        ),
    ]
