from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


from rest_framework.viewsets import ModelViewSet
from users.models import User
# from users.permissions import IsOwnerOrStaff
from users.serializers import (
    UserSerializer,
    UserSerializerCreate
)
from rest_framework.filters import SearchFilter
# import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

# from users.services import (create_stripe_price, create_stripe_product,
#                             create_stripe_sessions)




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
    # permission_classes = [IsOwnerOrStaff]


