from rest_framework import routers

from habits.models import Habit
from habits.views import HabitAPIViewSet

router = routers.SimpleRouter()
router.register('habits', HabitAPIViewSet)

urlpatterns = []
urlpatterns += router.urls
