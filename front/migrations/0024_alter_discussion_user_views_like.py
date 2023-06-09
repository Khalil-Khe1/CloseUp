# Generated by Django 4.1.7 on 2023-03-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0023_discussion_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discussion",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="front.user"
            ),
        ),
        migrations.CreateModel(
            name="Views",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="front.discussion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="front.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="front.discussion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="front.user"
                    ),
                ),
            ],
        ),
    ]
