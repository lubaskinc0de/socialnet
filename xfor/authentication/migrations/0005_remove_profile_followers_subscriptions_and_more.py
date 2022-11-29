# Generated by Django 4.0.4 on 2022-04-18 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0004_profile_followers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="followers",
        ),
        migrations.CreateModel(
            name="Subscriptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supporter",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчик",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub",
                        to="authentication.profile",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leader",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Тот на кого подписаны",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="subscriptions",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("from_user", django.db.models.expressions.F("to_user"))
                ),
                name="true_subscriber",
            ),
        ),
    ]
