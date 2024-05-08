from rest_framework.test import APITestCase

from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="smth@mail.com",
                                        is_superuser=True)

        self.habit = Habit.objects.create(
            place="your favorite place",
            action="do_something"
        )

        self.user = User.objects.create(email="test@test.com",
                                        is_superuser=True)

    def test_get_list(self):
        """TESTING READ (LIST)"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get("/habits/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        """TESTING CREATE"""
        self.client.force_authenticate(user=self.user)

        data = {
            "place": self.habit.place,
            "owner": self.user.id,
            "action": self.habit.action,
        }

        response = self.client.post("/habits/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Habit.objects.all().exists())

        self.assertEqual(response.json()["place"], data["place"])

        self.assertEqual(response.json()["action"], data["action"])

    def test_update_habit(self):
        """TESTING UPDATE"""
        self.client.force_authenticate(user=self.user)
        habit_update = Habit.objects.create(
            place="new habit ", action="new random action", user=self.user
        )

        response = self.client.patch(
            f"/habits/{habit_update.pk}/", data={"place": "new place"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            "id": habit_update.id,
            "place": "new place",
            "time_execute": "00:00:00",
            "action": "new random action",
            "is_nice": False,
            "periodicity": 1,
            "reward": None,
            "time_duration": 60,
            "is_public": True,
            "user": self.user.id,
            "related_habit": None,
        }

        self.assertEqual(response.json(), data)

    def test_delete_habit(self):
        """ТESTING DELETE"""

        self.client.force_authenticate(user=self.user)

        habit_for_delete = Habit.objects.create(
            place="deleting_place",
            action="deleting_action",
            user=self.user,
        )

        response = self.client.delete(f"/habits/{habit_for_delete.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_habit(self):
        """TESTING UPDATE"""
        self.client.force_authenticate(user=self.user)
        habit_retrieve = Habit.objects.create(
            place="new habit", action="new random action", user=self.user
        )

        response = self.client.patch(
            f"/habits/{habit_retrieve.pk}/", data={"is_nice": "False"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            "id": habit_retrieve.id,
            "place": "new habit",
            "time_execute": "00:00:00",
            "action": "new random action",
            "is_nice": False,
            "periodicity": 1,
            "reward": None,
            "time_duration": 60,
            "is_public": True,
            "user": self.user.id,
            "related_habit": None,
        }

        self.assertEqual(response.json(), data)

    def test_duration_habit(self):
        """Тестирование создания привычки со
        временем исполнения более 2 минут"""

        self.client.force_authenticate(user=self.user)

        data = {"time_duration": 130}

        response = self.client.post("/habits/", data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {
                "non_field_errors": [
                    "Превышено время выполнение"
                    " привычкине более 120 секунд)!"
                ]
            },
        )

    def test_periodicity_habit(self):
        self.client.force_authenticate(user=self.user)

        data = {"periodicity": 8}

        response = self.client.post("/habits/", data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.json(),
            {"non_field_errors": ["Интервал задания"
                                  " периодичности [1; 7]!"]},
        )
