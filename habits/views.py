from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsUser
from habits.serializers import HabitSerializer

from rest_framework.response import Response


class HabitAPIViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def list(self, serializer):
        queryset = Habit.objects.filter(user=None)
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsUser | IsAdminUser]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsUser | IsAdminUser]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsUser | IsAdminUser]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsUser]
        return [permission() for permission in self.permission_classes]
