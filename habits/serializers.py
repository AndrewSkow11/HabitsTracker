from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    RewardHabitValidator,
    HabitRelatedIsNiceValidator,
    NiceHabbitValidator,
    DurationValidatior,
    PeriodicValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardHabitValidator("related_habit", "reward"),
            HabitRelatedIsNiceValidator("related_habit",
                                        "is_nice"),
            NiceHabbitValidator("related_habit", "reward",
                                "is_nice"),
            DurationValidatior("time_duration"),
            PeriodicValidator("periodicity"),
        ]
