from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.serializers import HabitSerializer


class HabitAPIViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    # def get_permissions(self):
    #     if self.action == 'create':
    #         self.permission_classes = [IsAuthenticated, ~IsModerator]
    #     elif self.action == 'list':
    #         self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    #     elif self.action == 'retrieve':
    #         self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    #     elif self.action == 'update':
    #         self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    #     elif self.action == 'destroy':
    #         self.permission_classes = [IsAuthenticated, IsOwner, ~IsModerator]
    #     return [permission() for permission in self.permission_classes]

