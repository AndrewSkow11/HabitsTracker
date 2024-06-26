# Generated by Django 5.0.4 on 2024-05-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_remove_habit_time_for_execute_habit_time_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.PositiveSmallIntegerField(
                default=1, verbose_name="периодичность выполнения (дни)"
            ),
        ),
    ]
