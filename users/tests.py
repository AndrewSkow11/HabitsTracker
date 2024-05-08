from rest_framework.test import APITestCase

from rest_framework import status

from users.models import User


class UsersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='smth@mail.com')

        self.user = User.objects.create(
            email='test@test.com',
            password='1234')

    def test_create_user(self):
        """TESTING CREATE User"""

        data = {
            "email": "new_user@mail.com",
            "password": "1234"
        }

        response = self.client.post("/users/create/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(User.objects.all().exists())

        self.assertEqual(
            response.json()['email'],
            data['email']
        )

    def test_get_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/users/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_update_user(self):
        """TESTING UPDATE User"""
        self.client.force_authenticate(user=self.user)

        user_update = User.objects.create(
            email='smth2345@mail.com',
        )

        response = self.client.patch(
            f'/users/{user_update.pk}/',
            data={'email': 'something@smth.ru'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['email'], 'something@smth.ru')
