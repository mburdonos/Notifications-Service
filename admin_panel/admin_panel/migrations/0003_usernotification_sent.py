# Generated by Django 4.1.6 on 2023-02-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0002_usernotification_enabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="usernotification",
            name="sent",
            field=models.BooleanField(default=False),
        ),
    ]