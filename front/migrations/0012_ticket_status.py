# Generated by Django 4.1.7 on 2023-03-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0011_remove_ticket_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="status",
            field=models.CharField(default=None, max_length=50),
        ),
    ]
