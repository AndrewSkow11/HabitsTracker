from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitAPIViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer