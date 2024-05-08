from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsUser
from habits.serializers import HabitSerializer

from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination


class HabitAPIViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

    def list(self, request):

        habits = Habit.objects.filter(is_public=True)
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(habits, request)
        serializer = HabitSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

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


class UserHabitListApiView(generics.ListAPIView):
    """Только пользовательские привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
