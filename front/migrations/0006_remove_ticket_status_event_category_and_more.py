# Generated by Django 4.1.7 on 2023-03-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0005_alter_event_id_alter_review_id_alter_ticket_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="event",
            name="participators",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="event",
            name="registration_deadline",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="event",
            name="state",
            field=models.CharField(default="open", max_length=50),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_img",
            field=models.CharField(default="default.png", max_length=255),
        ),
    ]
