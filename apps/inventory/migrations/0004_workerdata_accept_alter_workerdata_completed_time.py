# Generated by Django 4.2.1 on 2023-05-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_workerdata_match_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="workerdata",
            name="accept",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="workerdata",
            name="completed_time",
            field=models.DateTimeField(null=True),
        ),
    ]
