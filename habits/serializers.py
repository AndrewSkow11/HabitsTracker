from rest_framework import serializers

from habits.models import Habit
from habits.validators import RewardHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardHabitValidator('related_habit', 'reward')
        ]
