from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from rest_framework import routers
from users.apps import UsersConfig
from users.views import (
    UserRetrieveUpdateDestroy,
    UserCreateAPIView,
    UserListAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Create
    path("create/", UserCreateAPIView.as_view(), name="users_create"),
    # Read, Update, Delete
    path("list/", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/", UserRetrieveUpdateDestroy.as_view(), name="users_rud"),
]
