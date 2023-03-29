# Generated by Django 4.1.7 on 2023-03-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0018_discussion_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="discussion",
            name="parent",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="front.discussion",
            ),
        ),
    ]