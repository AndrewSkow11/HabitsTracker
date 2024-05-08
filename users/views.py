from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer

from users.models import User
from users.serializers import (
    UserSerializer,
    UserSerializerCreate
)

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializerCreate
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
