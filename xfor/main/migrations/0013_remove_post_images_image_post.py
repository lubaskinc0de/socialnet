# Generated by Django 4.0.4 on 2022-04-23 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_post_liked"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="images",
        ),
        migrations.AddField(
            model_name="image",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                related_query_name="images",
                to="main.post",
            ),
        ),
    ]
