# Generated by Django 5.0.4 on 2024-05-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_alter_habit_action_alter_habit_is_public_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="time_for_execute",
        ),
        migrations.AddField(
            model_name="habit",
            name="time_duration",
            field=models.PositiveSmallIntegerField(
                default="60", verbose_name="время на выполнение в секундах"
            ),
        ),
    ]