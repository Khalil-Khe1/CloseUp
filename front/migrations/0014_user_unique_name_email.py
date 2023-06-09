# Generated by Django 4.1.7 on 2023-03-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0013_remove_user_profile_img_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                fields=("username", "email"), name="unique_name_email"
            ),
        ),
    ]
