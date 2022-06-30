# Generated by Django 4.0.4 on 2022-05-14 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0017_alter_contact_created_at_alter_contact_user_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_set', to=settings.AUTH_USER_MODEL, verbose_name='От'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_set', to=settings.AUTH_USER_MODEL, verbose_name='На'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token', related_query_name='token', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
