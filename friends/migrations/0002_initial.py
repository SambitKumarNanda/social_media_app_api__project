# Generated by Django 4.2.2 on 2023-07-11 08:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("friends", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="friendmodel",
            name="target_user",
            field=models.ManyToManyField(
                blank=True,
                related_name="FriendModel_target_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
