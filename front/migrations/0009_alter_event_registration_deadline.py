# Generated by Django 4.1.7 on 2023-03-25 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0008_event_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="registration_deadline",
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]