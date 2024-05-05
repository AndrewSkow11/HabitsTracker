from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Вы не автор привычки!"

    def has_object_permission(self, request, view, object):
        if request.user == object.owner:
            return True
        else:
            return False
