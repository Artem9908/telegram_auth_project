# Generated by Django 5.1.3 on 2024-12-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="telegramtoken",
            name="is_authenticated",
            field=models.BooleanField(default=False),
        ),
    ]