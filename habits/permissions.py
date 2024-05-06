from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Вы не автор привычки!"

    def has_object_permission(self, request, view, object):
        if request.user == object.user:
            return True
        else:
            return False
