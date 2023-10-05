# Generated by Django 4.2.5 on 2023-10-03 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("donations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="campaign",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="donations.campaign"
            ),
        ),
        migrations.AlterField(
            model_name="donation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
