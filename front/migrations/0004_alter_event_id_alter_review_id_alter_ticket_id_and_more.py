# Generated by Django 4.1.7 on 2023-03-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0003_alter_event_id_alter_review_id_alter_ticket_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="review",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
